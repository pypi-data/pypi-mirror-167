use crate::module_writer::{add_data, ModuleWriter};
use crate::{BuildContext, PyProjectToml, SDistWriter};
use anyhow::{bail, Context, Result};
use cargo_metadata::Metadata;
use fs_err as fs;
use std::collections::HashMap;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::str;

const LOCAL_DEPENDENCIES_FOLDER: &str = "local_dependencies";

/// We need cargo to load the local dependencies from the location where we put them in the source
/// distribution. Since there is no cargo-backed way to replace dependencies
/// (see https://github.com/rust-lang/cargo/issues/9170), we do a simple
/// Cargo.toml rewrite ourselves.
/// A big chunk of that comes from cargo edit, and esp.
/// https://github.com/killercup/cargo-edit/blob/2a08f0311bcb61690d71d39cb9e55e69b256c8e1/src/manifest.rs
/// This method is rather frail, but unfortunately I don't know a better solution.
fn rewrite_cargo_toml(
    manifest_path: impl AsRef<Path>,
    known_path_deps: &HashMap<String, PathBuf>,
    local_deps_folder: String,
    root_crate: bool,
) -> Result<String> {
    let text = fs::read_to_string(&manifest_path).context(format!(
        "Can't read Cargo.toml at {}",
        manifest_path.as_ref().display(),
    ))?;
    let mut data = text.parse::<toml_edit::Document>().context(format!(
        "Failed to parse Cargo.toml at {}",
        manifest_path.as_ref().display()
    ))?;
    let mut rewritten = false;
    //  ˇˇˇˇˇˇˇˇˇˇˇˇ dep_category
    // [dependencies]
    // some_path_dep = { path = "../some_path_dep" }
    //                          ^^^^^^^^^^^^^^^^^^ table[&dep_name]["path"]
    // ^^^^^^^^^^^^^ dep_name
    for dep_category in &["dependencies", "dev-dependencies", "build-dependencies"] {
        if let Some(table) = data.get_mut(*dep_category).and_then(|x| x.as_table_mut()) {
            let dep_names: Vec<_> = table.iter().map(|(key, _)| key.to_string()).collect();
            for dep_name in dep_names {
                // There should either be no value for path, or it should be a string
                if table.get(&dep_name).and_then(|x| x.get("path")).is_none() {
                    continue;
                }
                if !table[&dep_name]["path"].is_str() {
                    bail!(
                        "In {}, {} {} has a path value that is not a string",
                        manifest_path.as_ref().display(),
                        dep_category,
                        dep_name
                    )
                }
                if !known_path_deps.contains_key(&dep_name) {
                    bail!(
                        "cargo metadata does not know about the path for {}.{} present in {}, \
                        which should never happen ಠ_ಠ",
                        dep_category,
                        dep_name,
                        manifest_path.as_ref().display()
                    );
                }
                // This is the location of the targeted crate in the source distribution
                table[&dep_name]["path"] = if root_crate {
                    toml_edit::value(format!("{}/{}", local_deps_folder, dep_name))
                } else {
                    // Cargo.toml contains relative paths, and we're already in LOCAL_DEPENDENCIES_FOLDER
                    toml_edit::value(format!("../{}", dep_name))
                };
                rewritten = true;
            }
        }
    }
    if root_crate {
        // Update workspace members
        if let Some(workspace) = data.get_mut("workspace").and_then(|x| x.as_table_mut()) {
            if let Some(members) = workspace.get_mut("members").and_then(|x| x.as_array_mut()) {
                let mut new_members = toml_edit::Array::new();
                for member in members.iter() {
                    if let toml_edit::Value::String(ref s) = member {
                        let path = Path::new(s.value());
                        if let Some(name) = path.file_name().and_then(|x| x.to_str()) {
                            if known_path_deps.contains_key(name) {
                                new_members.push(format!("{}/{}", LOCAL_DEPENDENCIES_FOLDER, name));
                            }
                        }
                    }
                }
                if !new_members.is_empty() {
                    workspace["members"] = toml_edit::value(new_members);
                    rewritten = true;
                }
            }
        }
    } else {
        // Update package.workspace
        // https://rust-lang.github.io/rfcs/1525-cargo-workspace.html#implicit-relations
        // https://doc.rust-lang.org/cargo/reference/manifest.html#the-workspace-field
        if let Some(package) = data.get_mut("package").and_then(|x| x.as_table_mut()) {
            if let Some(workspace) = package.get("workspace").and_then(|x| x.as_str()) {
                // This is enough to fix https://github.com/PyO3/maturin/issues/838
                // Other cases can be fixed on demand
                if workspace == ".." || workspace == "../" {
                    package.remove("workspace");
                    rewritten = true;
                }
            }
        }
    }
    if rewritten {
        Ok(data.to_string())
    } else {
        Ok(text)
    }
}

/// Copies the files of a crate to a source distribution, recursively adding path dependencies
/// and rewriting path entries in Cargo.toml
///
/// Runs `cargo package --list --allow-dirty` to obtain a list of files to package.
fn add_crate_to_source_distribution(
    writer: &mut SDistWriter,
    pyproject_toml_path: impl AsRef<Path>,
    pyproject: &PyProjectToml,
    manifest_path: impl AsRef<Path>,
    prefix: impl AsRef<Path>,
    known_path_deps: &HashMap<String, PathBuf>,
    root_crate: bool,
) -> Result<()> {
    let manifest_path = manifest_path.as_ref();
    let pyproject_toml_path = pyproject_toml_path.as_ref();
    let output = Command::new("cargo")
        .args(&["package", "--list", "--allow-dirty", "--manifest-path"])
        .arg(manifest_path)
        .output()
        .with_context(|| {
            format!(
                "Failed to run `cargo package --list --allow-dirty --manifest-path {}`",
                manifest_path.display()
            )
        })?;
    if !output.status.success() {
        bail!(
            "Failed to query file list from cargo: {}\n--- Manifest path: {}\n--- Stdout:\n{}\n--- Stderr:\n{}",
            output.status,
            manifest_path.display(),
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr),
        );
    }

    let file_list: Vec<&Path> = str::from_utf8(&output.stdout)
        .context("Cargo printed invalid utf-8 ಠ_ಠ")?
        .lines()
        .map(Path::new)
        .collect();

    let abs_manifest_path = manifest_path.canonicalize()?;
    let abs_manifest_dir = abs_manifest_path.parent().unwrap();
    let pyproject_dir = pyproject_toml_path.parent().unwrap();
    let cargo_toml_in_subdir = root_crate
        && abs_manifest_dir != pyproject_dir
        && abs_manifest_dir.starts_with(&pyproject_dir);

    // manifest_dir should be a relative path
    let manifest_dir = manifest_path.parent().unwrap();
    let mut target_source: Vec<(PathBuf, PathBuf)> = file_list
        .iter()
        .map(|relative_to_manifests| {
            let relative_to_cwd = manifest_dir.join(relative_to_manifests);
            if root_crate && cargo_toml_in_subdir {
                (relative_to_cwd.clone(), relative_to_cwd)
            } else {
                (relative_to_manifests.to_path_buf(), relative_to_cwd)
            }
        })
        // We rewrite Cargo.toml and add it separately
        .filter(|(target, source)| {
            // Skip generated files. See https://github.com/rust-lang/cargo/issues/7938#issuecomment-593280660
            // and https://github.com/PyO3/maturin/issues/449
            if target == Path::new("Cargo.toml.orig")
                || (root_crate && target.file_name() == Some("Cargo.toml".as_ref()))
            {
                false
            } else {
                source.exists()
            }
        })
        .collect();

    if root_crate
        && !target_source
            .iter()
            .any(|(target, _)| target == Path::new("pyproject.toml"))
    {
        // Add pyproject.toml to the source distribution
        // if Cargo.toml is in subdirectory of pyproject.toml directory
        if cargo_toml_in_subdir {
            target_source.push((
                PathBuf::from("pyproject.toml"),
                pyproject_toml_path.to_path_buf(),
            ));
            // Add readme, license and python source files
            if let Some(project) = pyproject.project.as_ref() {
                if let Some(pyproject_toml::ReadMe::RelativePath(readme)) = project.readme.as_ref()
                {
                    target_source.push((PathBuf::from(readme), pyproject_dir.join(readme)));
                }
                if let Some(pyproject_toml::License {
                    file: Some(license),
                    text: None,
                }) = project.license.as_ref()
                {
                    target_source.push((PathBuf::from(license), pyproject_dir.join(license)));
                }
                if let Some(python_source) = pyproject.python_source() {
                    for entry in ignore::Walk::new(pyproject_dir.join(python_source)) {
                        let path = entry?.into_path();
                        let relative_path = path.strip_prefix(&pyproject_dir)?;
                        target_source.push((relative_path.to_path_buf(), path));
                    }
                }
            }
        } else {
            bail!(
                "pyproject.toml was not included by `cargo package`. \
                     Please make sure pyproject.toml is not excluded or build without `--sdist`"
            )
        }
    }

    let local_deps_folder = if cargo_toml_in_subdir {
        let level = abs_manifest_dir
            .strip_prefix(pyproject_dir)?
            .components()
            .count();
        format!("{}{}", "../".repeat(level), LOCAL_DEPENDENCIES_FOLDER)
    } else {
        LOCAL_DEPENDENCIES_FOLDER.to_string()
    };
    let rewritten_cargo_toml = rewrite_cargo_toml(
        &manifest_path,
        known_path_deps,
        local_deps_folder,
        root_crate,
    )?;

    let prefix = prefix.as_ref();
    writer.add_directory(prefix)?;

    let cargo_toml = if cargo_toml_in_subdir {
        prefix.join(manifest_path)
    } else {
        prefix.join(manifest_path.file_name().unwrap())
    };
    writer.add_bytes(cargo_toml, rewritten_cargo_toml.as_bytes())?;
    for (target, source) in target_source {
        writer.add_file(prefix.join(target), source)?;
    }

    Ok(())
}

/// Finds all path dependencies of the crate
fn find_path_deps(cargo_metadata: &Metadata) -> Result<HashMap<String, PathBuf>> {
    let root = cargo_metadata
        .root_package()
        .context("Expected the dependency graph to have a root package")?;
    // scan the dependency graph for path dependencies
    let mut path_deps = HashMap::new();
    let mut stack: Vec<&cargo_metadata::Package> = vec![root];
    while let Some(top) = stack.pop() {
        for dependency in &top.dependencies {
            if let Some(path) = &dependency.path {
                // we search for the respective package by `manifest_path`, there seems
                // to be no way to query the dependency graph given `dependency`
                let dep_manifest_path = path.join("Cargo.toml");
                path_deps.insert(
                    dependency.name.clone(),
                    PathBuf::from(dep_manifest_path.clone()),
                );
                if let Some(dep_package) = cargo_metadata
                    .packages
                    .iter()
                    .find(|package| package.manifest_path == dep_manifest_path)
                {
                    // scan the dependencies of the path dependency
                    stack.push(dep_package)
                }
            }
        }
    }
    Ok(path_deps)
}

/// Creates a source distribution, packing the root crate and all local dependencies
///
/// The source distribution format is specified in
/// [PEP 517 under "build_sdist"](https://www.python.org/dev/peps/pep-0517/#build-sdist)
/// and in
/// https://packaging.python.org/specifications/source-distribution-format/#source-distribution-file-format
pub fn source_distribution(
    build_context: &BuildContext,
    pyproject: &PyProjectToml,
) -> Result<PathBuf> {
    let metadata21 = &build_context.metadata21;
    let manifest_path = &build_context.manifest_path;
    let pyproject_toml_path = build_context.pyproject_toml_path.canonicalize()?;

    let known_path_deps = find_path_deps(&build_context.cargo_metadata)?;

    let mut writer = SDistWriter::new(&build_context.out, metadata21)?;
    let root_dir = PathBuf::from(format!(
        "{}-{}",
        &metadata21.get_distribution_escaped(),
        &metadata21.get_version_escaped()
    ));

    // Add local path dependencies
    for (name, path_dep) in known_path_deps.iter() {
        add_crate_to_source_distribution(
            &mut writer,
            &pyproject_toml_path,
            pyproject,
            &path_dep,
            &root_dir.join(LOCAL_DEPENDENCIES_FOLDER).join(name),
            &known_path_deps,
            false,
        )
        .context(format!(
            "Failed to add local dependency {} at {} to the source distribution",
            name,
            path_dep.display()
        ))?;
    }

    // Add the main crate
    add_crate_to_source_distribution(
        &mut writer,
        &pyproject_toml_path,
        pyproject,
        &manifest_path,
        &root_dir,
        &known_path_deps,
        true,
    )?;

    let manifest_dir = manifest_path.parent().unwrap();
    let include_cargo_lock =
        build_context.cargo_options.locked || build_context.cargo_options.frozen;
    if include_cargo_lock {
        let cargo_lock_path = manifest_dir.join("Cargo.lock");
        let target = root_dir.join("Cargo.lock");
        writer.add_file(&target, &cargo_lock_path)?;
    }

    if let Some(include_targets) = pyproject.sdist_include() {
        for pattern in include_targets {
            println!("📦 Including files matching \"{}\"", pattern);
            for source in glob::glob(&manifest_dir.join(pattern).to_string_lossy())
                .expect("No files found for pattern")
                .filter_map(Result::ok)
            {
                let target = root_dir.join(&source.strip_prefix(manifest_dir)?);
                writer.add_file(target, source)?;
            }
        }
    }

    writer.add_bytes(
        root_dir.join("PKG-INFO"),
        metadata21.to_file_contents()?.as_bytes(),
    )?;

    add_data(&mut writer, build_context.project_layout.data.as_deref())?;
    let source_distribution_path = writer.finish()?;

    println!(
        "📦 Built source distribution to {}",
        source_distribution_path.display()
    );

    Ok(source_distribution_path)
}
