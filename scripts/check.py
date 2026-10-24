"""Run repository software checks using only the Python standard library."""

import ast
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
GROUPS = (
    ("profiles-core", (
        "-m", "unittest", "profiles.test_profiles", "profiles.test_repair",
        "profiles.test_assignment_journey", "core.test_compiler", "core.test_cli",
        "core.test_envelope", "-q",
    )),
    ("adapter", ("-m", "unittest", "discover", "-s", "adapters/codex", "-p", "test_*.py", "-q")),
    ("triage-v1", ("-m", "unittest", "discover", "-s", "evaluation/core-triage-v1", "-p", "test_*.py", "-q")),
    ("triage-v2", ("-m", "unittest", "discover", "-s", "evaluation/core-triage-v2", "-p", "test_*.py", "-q")),
    ("validation", ("-m", "unittest", "discover", "-s", "validation", "-p", "test_*.py", "-q")),
    ("evaluation", ("-m", "unittest", "discover", "-s", "evaluation", "-p", "test_*.py", "-q")),
    ("diagnostic-v2", ("-m", "unittest", "discover", "-s", "evaluation/diagnostic-v2", "-p", "test_*.py", "-q")),
)


def check_syntax():
    """Parse tracked Python source without importing it or writing bytecode."""
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.py"], cwd=ROOT, env=ENV,
        stdout=subprocess.PIPE, check=True,
    )
    paths = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    failures = []
    for path in paths:
        try:
            ast.parse((ROOT / path).read_bytes(), filename=path)
        except (OSError, SyntaxError, ValueError) as error:
            print(f"{path}: {error}", flush=True)
            failures.append(path)
    print(f"Parsed {len(paths)} tracked Python files; {len(failures)} failed.", flush=True)
    return not failures


def main():
    failed = []
    print("=== syntax ===", flush=True)
    try:
        if not check_syntax():
            failed.append("syntax")
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Syntax check could not run: {error}", flush=True)
        failed.append("syntax")

    for name, arguments in GROUPS:
        print(f"=== {name} ===", flush=True)
        try:
            result = subprocess.run([sys.executable, *arguments], cwd=ROOT, env=ENV)
            if result.returncode:
                failed.append(name)
        except OSError as error:
            print(f"Group could not run: {error}", flush=True)
            failed.append(name)

    if failed:
        print("Failed groups: " + ", ".join(failed), flush=True)
        return 1
    print("All software check groups passed.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
