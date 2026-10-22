"""Launch the adjacent installed profile package without a working-dir dependency."""
from pathlib import Path
import runpy
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "runtime"))
runpy.run_module("profiles", run_name="__main__")
