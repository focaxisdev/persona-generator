"""Fictional assignment lifecycle checks; no owner consent or model observation.

The existing fixture builder invents format assertions explicitly labeled
synthetic_fixture. Nothing here completes the private human onboarding gates.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from profiles import compiler as c
from profiles.fixtures.build_fixtures import make

ROOT = Path(__file__).resolve().parents[1]
V1 = 'persona-profile-catalog-v1'
V2 = 'persona-profile-catalog-v2'


class AssignmentJourneyTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = self.root / 'store'

    def bytes_in_store(self):
        return {str(path.relative_to(self.store)): path.read_bytes()
                for path in self.store.rglob('*') if path.is_file()}

    def publish(self, profile_id, revision='r1', catalog_id=V1):
        preview, presented, spec = make(profile_id, ('high',) * 10, revision,
                                        catalog_id=catalog_id)
        spec_path = self.root / (profile_id + '-' + revision + '-spec.json')
        preview_path = self.root / (profile_id + '-' + revision + '-preview.json')
        spec_path.write_bytes(c.canonical_bytes(spec))
        preview_path.write_bytes(presented)
        receipt = c.preview_receipt(presented)
        self.assertEqual(receipt['confirmation_status'], 'NOT_CONFIRMED')
        self.assertEqual(spec['confirmation']['origin'], 'synthetic_fixture')
        # This only validates invented test records. It never authenticates consent.
        pin = c.publish(spec_path, preview_path, self.store)
        return pin, spec_path, preview_path

    def bind(self, agent, pin, expected=None):
        return c.bind(self.store, agent, pin['profile_id'], pin['revision'],
                      pin['snapshot_sha256'], pin['effective_sha256'],
                      expected_current_sha256=expected)

    def retained_pin(self, profile_id, revision):
        directory = self.store / 'versions' / profile_id / revision
        spec, _, text = c.validate(directory / 'spec.json', directory / 'presented.json')
        # Public validation plus fresh load verify the retained artifacts before use.
        stored_spec, stored_text = c.load_version(self.store, profile_id, revision)
        self.assertEqual(stored_spec, spec)
        self.assertEqual(stored_text, text)
        confirmation = spec['confirmation']
        return {'profile_id': profile_id, 'revision': revision,
                'snapshot_sha256': confirmation['snapshot_sha256'],
                'effective_sha256': confirmation['effective_sha256']}

    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'profiles', *map(str, args)],
                              cwd=ROOT, capture_output=True)

    def current_expectation(self, agent):
        result = self.cli('load', '--store', self.store, '--agent', agent)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)['binding_sha256']

    def test_optional_children_upgrade_and_rollback_leave_other_bytes_exact(self):
        shared, _, _ = self.publish('fictional-shared')
        different, _, _ = self.publish('fictional-different')
        self.bind('fictional-parent', shared)
        # Parent-only use works. Children are neither required nor inherited.
        self.assertEqual(c.load_binding(self.store, 'fictional-parent')[0]['revision'], 'r1')
        with self.assertRaises(c.ProfileError):
            c.load_binding(self.store, 'fictional-child-a')
        self.bind('fictional-child-a', shared)
        self.bind('fictional-child-b', different)
        initial = self.bytes_in_store()
        old_pin = self.retained_pin('fictional-shared', 'r1')
        old_text = c.load_binding(self.store, 'fictional-child-a')[1]
        upgraded, _, _ = self.publish('fictional-shared', 'r2', V2)
        self.assertEqual(c.load_binding(self.store, 'fictional-child-a')[0]['revision'], 'r1')
        before_rebind = self.bytes_in_store()
        old_expectation = self.current_expectation('fictional-child-a')
        self.bind('fictional-child-a', upgraded, old_expectation)
        new_text = c.load_binding(self.store, 'fictional-child-a')[1]
        self.assertNotEqual(new_text, old_text)
        after_upgrade = self.bytes_in_store()
        changed = {key for key in before_rebind if before_rebind[key] != after_upgrade[key]}
        self.assertEqual(changed, {'bindings/fictional-child-a.json'})
        self.assertEqual(before_rebind.keys(), after_upgrade.keys())
        with self.assertRaises(c.ProfileError):
            self.bind('fictional-child-a', old_pin, old_expectation)
        self.assertEqual(after_upgrade, self.bytes_in_store())
        # A retained r1 is rebound, never republished as a backwards revision.
        old_pin = self.retained_pin('fictional-shared', 'r1')
        current_expectation = self.current_expectation('fictional-child-a')
        self.assertNotEqual(current_expectation, old_expectation)
        self.bind('fictional-child-a', old_pin, current_expectation)
        after_rollback = self.bytes_in_store()
        self.assertEqual(before_rebind, after_rollback)
        for key, value in initial.items():
            self.assertEqual(after_rollback[key], value, key)
        # A new process reads the actual restored binding and exact prior payload.
        result = self.cli('render', '--store', self.store, '--agent', 'fictional-child-a')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, old_text.encode('utf-8'))
        self.assertEqual(hashlib.sha256(result.stdout).hexdigest(), old_pin['effective_sha256'])
        self.assertEqual(after_rollback, self.bytes_in_store())

    def test_missing_expectation_missing_revision_and_tampering_cannot_roll_back(self):
        old_pin, _, _ = self.publish('fictional-rollback')
        new_pin, _, _ = self.publish('fictional-rollback', 'r2', V2)
        self.bind('fictional-child', new_pin)
        expectation = self.current_expectation('fictional-child')
        before = self.bytes_in_store()
        for expected in (None, '0' * 64, 'malformed'):
            with self.subTest(expected=expected), self.assertRaises(c.ProfileError):
                self.bind('fictional-child', old_pin, expected)
            self.assertEqual(before, self.bytes_in_store())
        with self.assertRaises(c.ProfileError):
            self.bind('fictional-missing', old_pin, expectation)
        with self.assertRaises(c.ProfileError):
            self.bind('fictional-child', {**old_pin, 'revision': 'r9'}, expectation)
        with self.assertRaises(c.ProfileError):
            self.bind('fictional-child', {**old_pin, 'snapshot_sha256': '0' * 64}, expectation)
        self.assertEqual(before, self.bytes_in_store())
        artifact = self.store / 'versions/fictional-rollback/r1/presented.json'
        original = artifact.read_bytes()
        for damaged in (None, original + b'\n'):
            if damaged is None:
                artifact.unlink()
            else:
                artifact.write_bytes(damaged)
            damaged_store = self.bytes_in_store()
            with self.subTest(damaged=damaged is None), self.assertRaises(c.ProfileError):
                self.bind('fictional-child', old_pin, expectation)
            self.assertEqual(damaged_store, self.bytes_in_store())
            self.assertEqual(c.load_binding(self.store, 'fictional-child')[0]['revision'], 'r2')
            artifact.write_bytes(original)
        # A broken current binding cannot be bypassed using a previously read digest.
        binding_path = self.store / 'bindings/fictional-child.json'
        binding = c.load_document(binding_path.read_bytes())
        binding_path.write_bytes(c.canonical_bytes({**binding, 'effective_sha256': '0' * 64}))
        damaged_store = self.bytes_in_store()
        with self.assertRaises(c.ProfileError):
            self.bind('fictional-child', old_pin, expectation)
        self.assertEqual(damaged_store, self.bytes_in_store())
        rendered = self.cli('render', '--store', self.store, '--agent', 'fictional-child')
        self.assertEqual(rendered.returncode, 2)
        self.assertEqual(rendered.stdout, b'')
        self.assertIn(b'REJECTED:', rendered.stderr)


if __name__ == '__main__':
    unittest.main()
