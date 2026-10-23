"""Static regression checks for versioned rules and deliberate binding replacement."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from profiles import compiler as c
from profiles.fixtures.build_fixtures import make

ROOT = Path(__file__).resolve().parents[1]
V1 = 'persona-profile-catalog-v1'
V2 = 'persona-profile-catalog-v2'
ANCHORS = ('high',) * 10


class RepairTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = self.root / 'store'

    def publish(self, catalog_id=V1, revision='r1'):
        preview, presented, spec = make('synthetic-repair', ANCHORS, revision, catalog_id=catalog_id)
        sp = self.root / (revision + '-spec.json'); pp = self.root / (revision + '-preview.json')
        sp.write_bytes(c.canonical_bytes(spec)); pp.write_bytes(presented)
        return c.publish(sp, pp, self.store)

    def bind(self, agent, pin, **kwargs):
        return c.bind(self.store, agent, pin['profile_id'], pin['revision'],
                      pin['snapshot_sha256'], pin['effective_sha256'], **kwargs)

    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'profiles', *map(str, args)],
                              cwd=ROOT, capture_output=True, text=True)

    def binding_bytes(self):
        return {p.name: p.read_bytes() for p in (self.store / 'bindings').iterdir()}

    def test_original_fixture_builder_and_render_bytes_remain_exact(self):
        for name, anchors in (
            ('combination-a', ('low', 'high', 'middle', 'low', 'high', 'low', 'middle', 'high', 'low', 'high')),
            ('combination-b', ('high', 'low', 'high', 'middle', 'low', 'high', 'low', 'middle', 'high', 'low')),
        ):
            _, presented, spec = make('synthetic-' + name, anchors)
            fixture = ROOT / 'profiles/fixtures'
            self.assertEqual(presented, (fixture / (name + '-preview.json')).read_bytes())
            self.assertEqual((json.dumps(spec, indent=2, ensure_ascii=False) + '\n').encode(),
                             (fixture / (name + '-spec.json')).read_bytes())
            self.assertEqual(hashlib.sha256(c.validate_spec(spec, presented).encode()).hexdigest(),
                             spec['confirmation']['effective_sha256'])

    def test_catalog_versions_only_change_politeness_and_preserve_schema(self):
        old = c.load_catalog(); new = c.load_catalog(catalog_id=V2)
        self.assertEqual(new['schema_version'], old['schema_version'])
        expected = copy.deepcopy(old); expected['id'] = V2
        expected['hypotheses']['hyp.politeness.v2'] = expected['hypotheses'].pop('hyp.politeness.v1')
        expected['hypotheses']['hyp.politeness.v2']['anchors']['high']['rule'] = new['hypotheses']['hyp.politeness.v2']['anchors']['high']['rule']
        self.assertEqual(expected, new)
        rule = new['hypotheses']['hyp.politeness.v2']['anchors']['high']['rule']
        self.assertIn('brief neutral acknowledgment', rule)
        self.assertIn('without attributing merit, agreement, or an unstated aim', rule)
        old_spec = make('synthetic-old', ANCHORS)
        new_spec = make('synthetic-new', ANCHORS, catalog_id=V2)
        self.assertNotEqual(c.validate_spec(old_spec[2], old_spec[1]), c.validate_spec(new_spec[2], new_spec[1]))
        for version in (V1, V2):
            preview, presented, spec = make('synthetic-version', ANCHORS, catalog_id=version)
            c.validate_spec(spec, presented)
            for ref in ({'id': version, 'sha256': '0' * 64}, {'id': 'unknown', 'sha256': '0' * 64}, {'id': [], 'sha256': '0' * 64}, {'id': version}):
                broken = copy.deepcopy(preview); broken['catalog'] = ref
                with self.subTest(version=version, ref=ref), self.assertRaises(c.ProfileError):
                    c.validate_preview(broken)
            broken = copy.deepcopy(preview)
            mapping = next(m for m in broken['mappings'] if m['aspect'] == 'bfas.politeness')
            mapping['id'] = 'hyp.politeness.v1' if version == V2 else 'hyp.politeness.v2'
            with self.assertRaises(c.ProfileError): c.validate_preview(broken)

    def test_versioned_politeness_conflict_lookup_and_stale_wording(self):
        for version in (V1, V2):
            preview, _, _ = make('synthetic-conflict', ANCHORS, catalog_id=version)
            catalog = c.load_catalog(catalog_id=version)
            alternatives = []
            for anchor in ('low', 'high'):
                exact = c.hypothesis_for_aspect(catalog, 'bfas.politeness')[1]['anchors'][anchor]
                alternatives.append({'id': 'alternative-' + anchor, 'anchor': anchor,
                                     **{k: exact[k] for k in ('trigger', 'rule', 'boundary')},
                                     'answer_ids': ['answer-politeness']})
            conflict = {'id': 'politeness-conflict', 'aspect': 'bfas.politeness', 'candidates': alternatives,
                        'status': 'unresolved', 'selected_candidate_id': None, 'resolution_answer_id': None}
            preview['conflicts'] = [conflict]
            c.validate_preview(preview, allow_unresolved=True)
            with self.assertRaises(c.ProfileError): c.validate_preview(preview)
            conflict.update(status='selected', selected_candidate_id='alternative-high', resolution_answer_id='answer-politeness')
            c.validate_preview(preview)
            other = c.load_catalog(catalog_id=V1 if version == V2 else V2)
            alternatives[1]['rule'] = c.hypothesis_for_aspect(other, 'bfas.politeness')[1]['anchors']['high']['rule']
            with self.assertRaises(c.ProfileError): c.validate_preview(preview)

    def test_both_catalogs_and_sources_revalidate_their_pins(self):
        checkout = self.root / 'checkout'
        for version, (path, _) in c.TRUSTED_CATALOGS.items():
            target = checkout / path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / path).read_bytes())
        for path, _ in c.TRUSTED_DEPENDENCIES:
            target = checkout / path; target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, target)
        for version, (path, _) in c.TRUSTED_CATALOGS.items():
            c.load_catalog(checkout, version)
            target = checkout / path; original = target.read_bytes(); target.write_bytes(original + b' ')
            with self.subTest(version=version), self.assertRaises(c.ProfileError): c.load_catalog(checkout, version)
            target.write_bytes(original)
        (checkout / c.TRUSTED_DEPENDENCIES[0][0]).write_bytes(b'tampered source')
        for version in (V1, V2):
            with self.assertRaises(c.ProfileError): c.load_catalog(checkout, version)

    def test_binding_guard_create_replace_and_independent_agents(self):
        first = self.publish(); second = self.publish(V2, 'r2')
        old = self.bind('parent', first); self.bind('child', first)
        original = self.binding_bytes()
        for expected in (None, '0' * 64, '', True, [], 'A' * 64):
            with self.subTest(expected=expected), self.assertRaises(c.ProfileError):
                self.bind('parent', first, expected_current_sha256=expected)
            self.assertEqual(self.binding_bytes(), original)
        with self.assertRaises(c.ProfileError):
            self.bind('missing', second, expected_current_sha256=c.digest(old))
        self.assertEqual(self.binding_bytes(), original)
        # An exact expectation also permits an intentional identical replacement.
        self.assertEqual(self.bind('parent', first, expected_current_sha256=c.digest(old)), old)
        new = self.bind('parent', second, expected_current_sha256=c.digest(old))
        self.assertEqual(c.load_binding(self.store, 'parent')[0], new)
        self.assertEqual(c.load_binding(self.store, 'child')[0]['revision'], 'r1')
        with self.assertRaises(c.ProfileError):
            self.bind('parent', first, expected_current_sha256=c.digest(old))
        self.assertEqual(c.load_binding(self.store, 'parent')[0], new)

    def test_binding_guard_revalidates_existing_and_new_artifacts_before_writes(self):
        first = self.publish(); second = self.publish(V2, 'r2')
        old = self.bind('parent', first)
        path = self.store / 'bindings/parent.json'
        for raw in (b'{bad json', c.canonical_bytes({**old, 'extra': True}), c.canonical_bytes({**old, 'effective_sha256': '0' * 64})):
            path.write_bytes(raw)
            with self.assertRaises(c.ProfileError): self.bind('parent', second, expected_current_sha256=c.digest(old))
            self.assertEqual(path.read_bytes(), raw)
        path.write_bytes(c.canonical_bytes(old))
        for revision in ('r1', 'r2'):
            artifact = self.store / 'versions/synthetic-repair' / revision / 'presented.json'
            original = artifact.read_bytes(); artifact.write_bytes(original + b' ')
            before = self.binding_bytes()
            with self.assertRaises(c.ProfileError): self.bind('parent', second, expected_current_sha256=c.digest(old))
            self.assertEqual(self.binding_bytes(), before)
            artifact.write_bytes(original)

    def test_cli_audit_digest_and_guard(self):
        first = self.publish(); second = self.publish(V2, 'r2')
        self.bind('parent', first)
        loaded = self.cli('load', '--store', self.store, '--agent', 'parent')
        self.assertEqual(loaded.returncode, 0, loaded.stderr)
        audit = json.loads(loaded.stdout)
        self.assertEqual(audit['binding_sha256'], c.digest(c.load_binding(self.store, 'parent')[0]))
        args = ('bind', '--store', self.store, '--agent', 'parent', '--profile', second['profile_id'],
                '--revision', second['revision'], '--snapshot', second['snapshot_sha256'], '--effective', second['effective_sha256'])
        for extra in ((), ('--expected-current', '0' * 64), ('--expected-current', 'bad')):
            before = self.binding_bytes(); result = self.cli(*args, *extra)
            self.assertEqual(result.returncode, 2); self.assertEqual(result.stdout, '')
            self.assertIn('REJECTED:', result.stderr); self.assertEqual(self.binding_bytes(), before)
        result = self.cli(*args, '--expected-current', audit['binding_sha256'])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['revision'], 'r2')
        rendered = self.cli('render', '--store', self.store, '--agent', 'parent')
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertEqual(hashlib.sha256(rendered.stdout.encode()).hexdigest(), second['effective_sha256'])
        self.assertNotIn('binding_sha256', rendered.stdout)


if __name__ == '__main__':
    unittest.main()
