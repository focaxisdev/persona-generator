"""Local filesystem and subprocess checks; never starts a host/model session."""
import importlib.util
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from profiles.fixtures.build_fixtures import make


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
spec = importlib.util.spec_from_file_location("codex_install", HERE / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
ADAPTER_ASSETS = (
    ("skill/SKILL.md", "SKILL.md"),
    ("skill/agents/openai.yaml", "agents/openai.yaml"),
    ("run.py", "run.py"),
)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.target = self.root / "target repo with spaces"
        self.target.mkdir()

    def disposable_sources(self):
        source = self.root / "source"
        adapter = source / "adapters/codex"
        for relative in installer.RUNTIME_FILES:
            output = source / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / relative, output)
        for relative, _ in ADAPTER_ASSETS:
            output = adapter / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(HERE / relative, output)
        return source, adapter

    def assert_manifest_bytes(self, destination, source, adapter):
        expected = {installed: (adapter / relative).read_bytes()
                    for relative, installed in ADAPTER_ASSETS}
        expected.update({"runtime/" + relative: (source / relative).read_bytes()
                         for relative in installer.RUNTIME_FILES})
        actual = {p.relative_to(destination).as_posix(): p.read_bytes()
                  for p in destination.rglob("*") if p.is_file()}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 13)
        self.assertFalse(any(p.is_symlink() for p in destination.rglob("*")))

    def test_unlisted_source_content_is_ignored(self):
        source, adapter = self.disposable_sources()
        extras = (
            "private-profile.json", "store/versions/private/r1/spec.json",
            "store/bindings/private-agent.json", "__pycache__/private.pyc",
            "agents/private-record.json",
        )
        for relative in extras:
            path = adapter / "skill" / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"synthetic private record: must not ship")
        (adapter / "skill/empty-store").mkdir()
        (source / "profiles/private-profile.json").write_text("unlisted runtime record")
        (adapter / "private-profile.json").write_text("unlisted adapter record")
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "private.json").write_text("unlisted external record")
        for name, target, is_directory in (
                ("linked-file", outside / "private.json", False),
                ("linked-store", outside, True),
                ("broken-link", outside / "absent", False)):
            (adapter / "skill" / name).symlink_to(target, target_is_directory=is_directory)
        with mock.patch.object(installer, "ADAPTER_ROOT", adapter):
            destination = installer.install(self.target, source_root=source)
        self.assert_manifest_bytes(destination, source, adapter)
        directories = {p.relative_to(destination).as_posix()
                       for p in destination.rglob("*") if p.is_dir()}
        self.assertEqual(directories, {"agents", "runtime", "runtime/profiles",
                                      "runtime/core", "runtime/persona-design-v0.2"})

    def test_required_assets_reject_before_target_writes(self):
        source, adapter = self.disposable_sources()
        marker = self.target / ".agents/keep.txt"
        marker.parent.mkdir()
        marker.write_bytes(b"preserve existing target content")
        before = {p.relative_to(self.target).as_posix():
                  p.read_bytes() if p.is_file() else None
                  for p in self.target.rglob("*")}
        required = [(adapter / relative, "adapter") for relative, _ in ADAPTER_ASSETS]
        required.extend((source / relative, "runtime") for relative in installer.RUNTIME_FILES)
        for path, kind in required:
            original = path.read_bytes()
            for defect in ("missing", "symlink"):
                with self.subTest(asset=path.relative_to(source), defect=defect):
                    path.unlink()
                    if defect == "symlink":
                        replacement = self.root / "replacement"
                        replacement.write_bytes(original)
                        path.symlink_to(replacement)
                    try:
                        with mock.patch.object(installer, "ADAPTER_ROOT", adapter):
                            with self.assertRaisesRegex(ValueError, kind + " source"):
                                installer.install(self.target, source_root=source)
                        after = {p.relative_to(self.target).as_posix():
                                 p.read_bytes() if p.is_file() else None
                                 for p in self.target.rglob("*")}
                        self.assertEqual(after, before)
                    finally:
                        if path.is_symlink():
                            path.unlink()
                        path.write_bytes(original)

    def test_required_source_directory_symlinks_reject_before_target_writes(self):
        source, adapter = self.disposable_sources()
        directories = (adapter / "skill/agents", adapter / "skill",
                       source / "profiles", source / "core", source / "persona-design-v0.2")
        for index, path in enumerate(directories):
            with self.subTest(directory=path.relative_to(source)):
                replacement = self.root / ("directory-" + str(index))
                path.rename(replacement)
                path.symlink_to(replacement, target_is_directory=True)
                try:
                    with mock.patch.object(installer, "ADAPTER_ROOT", adapter):
                        with self.assertRaisesRegex(ValueError, "symlinked .* source"):
                            installer.install(self.target, source_root=source)
                    self.assertEqual(list(self.target.iterdir()), [])
                finally:
                    path.unlink()
                    replacement.rename(path)

    def test_version_guards_reject_before_work_and_allow_minimum_boundary(self):
        # Simulated version_info exercises guard logic, not Python 3.9 execution.
        destination = installer.install(self.target)
        never_installed = self.root / "never installed target"
        never_installed.mkdir()
        entries = (
            (str(HERE / "install.py"), ["--target-repo", str(never_installed)]),
            (str(destination / "run.py"), ["--help"]),
            (str(REPO / "profiles" / "__main__.py"), ["--help"]),
        )
        untouched = self.root / "untouched"
        untouched.mkdir()
        for entry, args in entries:
            for version, expected in (((3, 8), 2), ((3, 9), 0)):
                with self.subTest(entry=entry, simulated_version=version):
                    # --help on accepted versions avoids installing or loading data.
                    cli_args = args if version < (3, 9) else ["--help"]
                    code = (
                        "import runpy, sys; "
                        "sys.path.insert(0, sys.argv[1]); "
                        "entry = sys.argv[2]; "
                        "sys.argv = [entry] + sys.argv[3:]; "
                        "sys.version_info = " + repr(version) + "; "
                        + ("runpy.run_module('profiles', run_name='__main__')"
                           if entry.endswith("__main__.py")
                           else "runpy.run_path(entry, run_name='__main__')")
                    )
                    result = subprocess.run(
                        [sys.executable, "-B", "-c", code, str(REPO), entry, *cli_args],
                        cwd=untouched, capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if expected:
                        self.assertEqual(result.stdout, "")
                        self.assertIn("REJECTED: Persona Generator requires Python 3.9 or newer", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
                    else:
                        self.assertIn("usage:", result.stdout)
                    self.assertEqual(list(untouched.iterdir()), [])
                    self.assertFalse((never_installed / ".agents").exists())
                    self.assertEqual(list(never_installed.iterdir()), [])

    def test_layout_is_self_contained_and_exact(self):
        destination = installer.install(self.target)
        actual = {str(path.relative_to(destination)) for path in destination.rglob("*") if path.is_file()}
        expected = {"SKILL.md", "agents/openai.yaml", "run.py"}
        expected.update("runtime/" + relative for relative in installer.RUNTIME_FILES)
        self.assertEqual(actual, expected)
        self.assert_manifest_bytes(destination, REPO, HERE)
        for relative in installer.RUNTIME_FILES:
            self.assertEqual((destination / "runtime" / relative).read_bytes(),
                             (REPO / relative).read_bytes())
        self.assertIn("allow_implicit_invocation: false", (destination / "agents/openai.yaml").read_text())
        self.assertNotIn("fixtures", " ".join(actual))

    def test_existing_skill_is_not_overwritten(self):
        destination = installer.install(self.target)
        marker = destination / "keep.txt"
        marker.write_text("preserve this exact file")
        before = {str(p.relative_to(destination)): p.read_bytes() for p in destination.rglob("*") if p.is_file()}
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            installer.install(self.target)
        after = {str(p.relative_to(destination)): p.read_bytes() for p in destination.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_file_collision_is_not_overwritten(self):
        destination = self.target / ".agents" / "skills" / installer.SKILL_NAME
        destination.parent.mkdir(parents=True)
        destination.write_text("existing file")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            installer.install(self.target)
        self.assertEqual(destination.read_text(), "existing file")

    def test_symlinked_installation_parent_is_rejected(self):
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        (self.target / ".agents").symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.target)
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_missing_dependency_fails_before_target_writes(self):
        with self.assertRaisesRegex(ValueError, "runtime source"):
            installer.install(self.target, source_root=self.root / "missing")
        self.assertEqual(list(self.target.iterdir()), [])

    def test_explicit_target_required(self):
        result = subprocess.run([sys.executable, str(HERE / "install.py")],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("--target-repo", result.stderr)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_installed_loader_runs_from_unrelated_directory(self):
        destination = installer.install(self.target)
        result = subprocess.run([sys.executable, str(destination / "run.py"), "--help"],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("render", result.stdout)

    def installed_runtime_commands(self):
        destination = installer.install(self.target)
        store = self.root / "runtime boundary store"
        fixture = REPO / "profiles/fixtures"
        preview = fixture / "combination-a-preview.json"
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(REPO)

        def run(*arguments, env=environment):
            return subprocess.run(
                [sys.executable, "-B", str(destination / "run.py"), *map(str, arguments)],
                cwd=self.root, env=env, capture_output=True, text=True,
            )

        published = run("publish", fixture / "combination-a-spec.json",
                        "--presented", preview, "--store", store)
        self.assertEqual(published.returncode, 0, published.stderr)
        pin = json.loads(published.stdout)
        bound = run("bind", "--store", store, "--agent", "synthetic-boundary",
                    "--profile", pin["profile_id"], "--revision", pin["revision"],
                    "--snapshot", pin["snapshot_sha256"],
                    "--effective", pin["effective_sha256"])
        self.assertEqual(bound.returncode, 0, bound.stderr)
        commands = (("validate-preview", preview),
                    ("render", "--store", store, "--agent", "synthetic-boundary"))
        return destination, run, commands, environment, pin

    def test_intact_installed_runtime_wins_over_ordinary_ambient_checkout(self):
        destination, run, commands, _, pin = self.installed_runtime_commands()
        for arguments in commands:
            result = run(*arguments)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout)
        self.assertEqual(hashlib.sha256(result.stdout.encode()).hexdigest(),
                         pin["effective_sha256"])

    def test_broken_installed_code_rejects_before_ambient_import(self):
        destination, run, commands, environment, _ = self.installed_runtime_commands()
        runtime = destination / "runtime"
        marker = self.root / "ambient package executed"
        ambient = self.root / "fake ambient"
        for package in ("profiles", "core"):
            path = ambient / package
            path.mkdir(parents=True)
            (path / "__init__.py").write_text(
                "from pathlib import Path\nPath(" + repr(str(marker)) + ").write_text('executed')\n"
            )
            (path / "__main__.py").write_text("print('ambient fallback')\n")
        fake_environment = dict(environment, PYTHONPATH=str(ambient))
        required = (".", "profiles", "core", "profiles/__init__.py",
                    "profiles/__main__.py", "profiles/compiler.py",
                    "core/__init__.py", "core/compiler.py")
        for relative in required:
            path = runtime if relative == "." else runtime / relative
            replacement = self.root / "saved installed code"
            for defect in ("missing", "symlink"):
                path.rename(replacement)
                if defect == "symlink":
                    path.symlink_to(replacement, target_is_directory=replacement.is_dir())
                try:
                    for ambient_environment in (environment, fake_environment):
                        for arguments in commands:
                            with self.subTest(path=relative, defect=defect,
                                              ambient=ambient_environment["PYTHONPATH"],
                                              command=arguments[0]):
                                result = run(*arguments, env=ambient_environment)
                                self.assertEqual(result.returncode, 2, result.stderr)
                                self.assertEqual(result.stdout, "")
                                self.assertEqual(result.stderr,
                                    "REJECTED: missing or symlinked installed runtime code: "
                                    + ("runtime" if relative == "." else "runtime/" + relative)
                                    + "\n")
                                self.assertFalse(marker.exists())
                finally:
                    if path.is_symlink():
                        path.unlink()
                    replacement.rename(path)

    def test_installed_two_catalogs_and_guarded_replacement(self):
        destination = installer.install(self.target)
        store = self.root / "two catalog store"

        def run(*args):
            return subprocess.run([sys.executable, str(destination / "run.py"), *map(str, args)],
                                  cwd=self.root, capture_output=True, text=True)

        pins = []
        for revision, version in (("r1", "persona-profile-catalog-v1"), ("r2", "persona-profile-catalog-v2")):
            _, presented, spec = make("synthetic-installed-versions", ("high",) * 10, revision, catalog_id=version)
            sp = self.root / (revision + "-spec.json"); pp = self.root / (revision + "-preview.json")
            sp.write_text(json.dumps(spec)); pp.write_bytes(presented)
            result = run("publish", sp, "--presented", pp, "--store", store)
            self.assertEqual(result.returncode, 0, result.stderr)
            pins.append(json.loads(result.stdout))

        def bind(agent, pin, *extra):
            return run("bind", "--store", store, "--agent", agent, "--profile", pin["profile_id"],
                       "--revision", pin["revision"], "--snapshot", pin["snapshot_sha256"],
                       "--effective", pin["effective_sha256"], *extra)

        for agent in ("parent", "child"):
            self.assertEqual(bind(agent, pins[0]).returncode, 0)
        before = {p.name: p.read_bytes() for p in (store / "bindings").iterdir()}
        for extra in ((), ("--expected-current", "0" * 64)):
            rejected = bind("child", pins[1], *extra)
            self.assertEqual(rejected.returncode, 2); self.assertEqual(rejected.stdout, "")
            self.assertEqual(before, {p.name: p.read_bytes() for p in (store / "bindings").iterdir()})
        audit = run("load", "--store", store, "--agent", "child")
        self.assertEqual(audit.returncode, 0, audit.stderr)
        replaced = bind("child", pins[1], "--expected-current", json.loads(audit.stdout)["binding_sha256"])
        self.assertEqual(replaced.returncode, 0, replaced.stderr)
        for agent, pin in (("parent", pins[0]), ("child", pins[1])):
            result = run("render", "--store", store, "--agent", agent)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(hashlib.sha256(result.stdout.encode()).hexdigest(), pin["effective_sha256"])
        # A changed copied catalog rejects only the binding selecting that version.
        path = destination / "runtime/profiles/catalog-v2.json"
        path.write_bytes(path.read_bytes() + b" ")
        rejected = run("render", "--store", store, "--agent", "child")
        self.assertEqual(rejected.returncode, 2); self.assertEqual(rejected.stdout, "")
        self.assertEqual(run("render", "--store", store, "--agent", "parent").returncode, 0)

    def test_unbound_loader_fails_closed_in_fresh_processes(self):
        destination = installer.install(self.target)
        store = self.root / "empty store"
        store.mkdir()
        for agent in ("parent", "child"):
            result = subprocess.run([sys.executable, str(destination / "run.py"), "render",
                                     "--store", str(store), "--agent", agent],
                                    cwd=self.root, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            self.assertTrue(result.stderr)

    def test_installed_fresh_and_child_bindings_revalidate_without_source_checkout(self):
        destination = installer.install(self.target)
        store = self.root / "independent store"
        launcher = destination / "run.py"

        def run(*arguments):
            return subprocess.run([sys.executable, str(launcher), *map(str, arguments)],
                                  cwd=self.root, capture_output=True, text=True)

        pins = []
        for name in ("combination-a", "combination-b"):
            # These are explicitly synthetic software fixtures, never owner consent.
            fixture = REPO / "profiles" / "fixtures"
            published = run("publish", fixture / (name + "-spec.json"),
                            "--presented", fixture / (name + "-preview.json"),
                            "--store", store)
            self.assertEqual(published.returncode, 0, published.stderr)
            pins.append(json.loads(published.stdout))
        for agent, pin in (("parent", pins[0]), ("child-same", pins[0]), ("child-different", pins[1])):
            bound = run("bind", "--store", store, "--agent", agent,
                        "--profile", pin["profile_id"], "--revision", pin["revision"],
                        "--snapshot", pin["snapshot_sha256"], "--effective", pin["effective_sha256"])
            self.assertEqual(bound.returncode, 0, bound.stderr)
        rendered = {}
        for agent in ("parent", "child-same", "child-different"):
            result = run("render", "--store", store, "--agent", agent)
            self.assertEqual(result.returncode, 0, result.stderr)
            rendered[agent] = result.stdout
        self.assertEqual(rendered["parent"], rendered["child-same"])
        self.assertNotEqual(rendered["parent"], rendered["child-different"])
        self.assertEqual(hashlib.sha256(rendered["parent"].encode()).hexdigest(), pins[0]["effective_sha256"])
        self.assertEqual(hashlib.sha256(rendered["child-different"].encode()).hexdigest(), pins[1]["effective_sha256"])
        # Same agent reloads in another fresh Python process using stored bytes.
        self.assertEqual(run("render", "--store", store, "--agent", "parent").stdout,
                         rendered["parent"])
        # Installation alone never creates a child binding.
        absent = run("render", "--store", store, "--agent", "child-unbound")
        self.assertNotEqual(absent.returncode, 0)
        self.assertEqual(absent.stdout, "")
        # Metadata is not the instruction payload.
        self.assertNotIn('"snapshot_sha256"', rendered["parent"])
        # A stored preview change is detected at fresh load, never adopted.
        pin = pins[0]
        presented = store / "versions" / pin["profile_id"] / pin["revision"] / "presented.json"
        presented.write_bytes(presented.read_bytes() + b"\n")
        stale = run("render", "--store", store, "--agent", "parent")
        self.assertNotEqual(stale.returncode, 0)
        self.assertEqual(stale.stdout, "")
        # Another agent's different immutable profile remains independently valid.
        still_valid = run("render", "--store", store, "--agent", "child-different")
        self.assertEqual(still_valid.returncode, 0, still_valid.stderr)
        self.assertEqual(still_valid.stdout, rendered["child-different"])
        # Changing the copied versioned source blocks even that binding.
        source = destination / "runtime" / "persona-design-v0.2" / "sources.md"
        source.write_bytes(source.read_bytes() + b"\n")
        changed = run("render", "--store", store, "--agent", "child-different")
        self.assertNotEqual(changed.returncode, 0)
        self.assertEqual(changed.stdout, "")


if __name__ == "__main__":
    unittest.main()
