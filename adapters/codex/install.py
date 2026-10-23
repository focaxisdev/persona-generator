"""Copy the explicit-invocation Codex adapter into a requested repository.

This local installer neither starts Codex nor activates any profile.
"""
from __future__ import annotations

import sys

if sys.version_info < (3, 9):
    print("REJECTED: Persona Generator requires Python 3.9 or newer", file=sys.stderr)
    raise SystemExit(2)

import argparse
from pathlib import Path
import shutil
import tempfile


SKILL_NAME = "persona-profile"
SOURCE_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_ROOT = Path(__file__).resolve().parent
RUNTIME_FILES = (
    "LICENSE",
    "profiles/__init__.py",
    "profiles/__main__.py",
    "profiles/compiler.py",
    "profiles/catalog-v1.json",
    "profiles/catalog-v2.json",
    "core/__init__.py",
    "core/compiler.py",
    "persona-design-v0.2/construct-registry.md",
    "persona-design-v0.2/sources.md",
)


def _no_symlink_components(path: Path) -> None:
    for component in (path, *path.parents):
        if component.is_symlink():
            raise ValueError("installation path contains a symlink: " + str(component))


def install(target_repo: Path, source_root: Path = SOURCE_ROOT) -> Path:
    """Install the allowlisted local package; refuse an existing skill path."""
    target_repo = Path(target_repo).absolute()
    _no_symlink_components(target_repo)
    if not target_repo.is_dir():
        raise ValueError("target repository must be an existing directory")
    destination = target_repo / ".agents" / "skills" / SKILL_NAME
    _no_symlink_components(destination)
    if destination.exists():
        raise ValueError("skill already exists; refusing to overwrite: " + str(destination))
    for relative in RUNTIME_FILES:
        source = source_root / relative
        if not source.is_file() or source.is_symlink():
            raise ValueError("missing or symlinked runtime source: " + relative)
    with tempfile.TemporaryDirectory(prefix="persona-codex-install-") as temporary:
        staged = Path(temporary) / SKILL_NAME
        shutil.copytree(ADAPTER_ROOT / "skill", staged)
        for relative in RUNTIME_FILES:
            output = staged / "runtime" / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source_root / relative, output)
        shutil.copyfile(ADAPTER_ROOT / "run.py", staged / "run.py")
        destination.parent.mkdir(parents=True, exist_ok=True)
        # copytree reserves the destination with mkdir(exist_ok=False).
        # An existing directory, file or symlink is never merged or replaced.
        shutil.copytree(staged, destination)
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-repo", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        destination = install(args.target_repo)
    except (OSError, ValueError) as error:
        print("REJECTED: " + str(error), file=sys.stderr)
        return 2
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
