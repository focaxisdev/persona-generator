"""Launch the adjacent installed profile package without a working-dir dependency."""
import sys

if sys.version_info < (3, 9):
    print("REJECTED: Persona Generator requires Python 3.9 or newer", file=sys.stderr)
    raise SystemExit(2)

from pathlib import Path
import runpy

runtime = Path(__file__).resolve().parent / "runtime"
# Check package directories before their files so missing __init__.py cannot
# turn a local package into a namespace that falls through to ambient code.
required_directories = (runtime, runtime / "profiles", runtime / "core")
required_files = tuple(runtime / relative for relative in (
    "profiles/__init__.py", "profiles/__main__.py", "profiles/compiler.py",
    "core/__init__.py", "core/compiler.py",
))
for path in (*required_directories, *required_files):
    present = path.is_dir() if path in required_directories else path.is_file()
    if path.is_symlink() or not present:
        relative = "runtime" if path == runtime else "runtime/" + path.relative_to(runtime).as_posix()
        print("REJECTED: missing or symlinked installed runtime code: " + relative,
              file=sys.stderr)
        raise SystemExit(2)

sys.path.insert(0, str(runtime))
runpy.run_module("profiles", run_name="__main__")
