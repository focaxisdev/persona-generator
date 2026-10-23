"""Launch the adjacent installed profile package without a working-dir dependency."""
import sys

if sys.version_info < (3, 9):
    print("REJECTED: Persona Generator requires Python 3.9 or newer", file=sys.stderr)
    raise SystemExit(2)

from pathlib import Path
import runpy

sys.path.insert(0, str(Path(__file__).resolve().parent / "runtime"))
runpy.run_module("profiles", run_name="__main__")
