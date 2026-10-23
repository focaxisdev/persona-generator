"""Local filesystem and subprocess checks; never starts a host/model session."""
import importlib.util
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from profiles.fixtures.build_fixtures import make


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
spec = importlib.util.spec_from_file_location("codex_install", HERE / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.target = self.root / "target repo with spaces"
        self.target.mkdir()

    def test_layout_is_self_contained_and_exact(self):
        destination = installer.install(self.target)
        actual = {str(path.relative_to(destination)) for path in destination.rglob("*") if path.is_file()}
        expected = {"SKILL.md", "agents/openai.yaml", "run.py"}
        expected.update("runtime/" + relative for relative in installer.RUNTIME_FILES)
        self.assertEqual(actual, expected)
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
