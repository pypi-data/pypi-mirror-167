import os
from glob import glob

from .dataclasses import LocalComparisonResult, Manifest
from .exceptions import ManifestError, PathError
from .paths import generate_path_pattern, resolve_paths
from .transformers import alt_dict_to_template, dict_to_template, is_alt_format


def generate_manifest(template_dict: dict, *args: str) -> Manifest:
    try:
        if is_alt_format(template_dict):
            template = alt_dict_to_template(template_dict)
        else:
            template = dict_to_template(template_dict)

        path_patterns = [
            generate_path_pattern(template.path_prefix, path_pattern, *args)
            for path_pattern in template.path_patterns
        ]
    except Exception as e:
        raise ManifestError("Error parsing manifest") from e

    return Manifest(
        name=template.name,
        template=template,
        args=args,
        path_patterns=path_patterns,
    )


def compare_manifest_to_local(
    template_dict: dict, local_dir: str, *args: str
) -> LocalComparisonResult:
    manifest = generate_manifest(template_dict, *args)
    resolved_paths = []
    found = []
    missing = []
    for path_pattern in manifest.path_patterns:
        pattern, paths = resolve_paths(local_dir, path_pattern)
        if len(paths) > 0:
            found.extend(paths)
        else:
            missing.append(pattern)
        resolved_paths.append(
            (
                pattern,
                paths,
            )
        )
    return LocalComparisonResult(
        local_dir=local_dir,
        manifest=manifest,
        resolved_paths=resolved_paths,
        found=found,
        missing=missing,
    )
