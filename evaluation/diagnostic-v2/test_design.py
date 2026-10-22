"""Synthetic structural mutations only: no model calls, outputs, ratings, or judges."""
import contextlib
import copy
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import validate_design as v


REPO = Path(__file__).resolve().parents[2]


class DesignTests(unittest.TestCase):
    def setUp(self):
        self.design = v.read_json(REPO / v.DESIGN_DIR / 'design.json')
        self.cards = v.read_json(REPO / v.CARDS)

    def reject(self, change):
        change(self.design, self.cards)
        with self.assertRaises(v.ValidationError):
            v.validate_inputs(self.design, self.cards)

    def temporary_package(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        directory = root / v.DESIGN_DIR
        directory.mkdir(parents=True)
        (root / v.CARDS).parent.mkdir(parents=True)
        v.write_json(directory / 'design.json', self.design)
        v.write_json(root / v.CARDS, self.cards)
        for name in ('PLAN.md', 'validate_design.py', 'test_design.py'):
            (directory / name).write_text('SYNTHETIC STRUCTURAL FIXTURE ONLY\n')
        for name in ('WORKFLOW.md', 'README.md', 'ACCEPTANCE_PROPOSAL.md'):
            (root / v.CARDS).with_name(name).write_text('SYNTHETIC CONTROL DOCUMENT FIXTURE\n')
        (root / v.CARDS).with_suffix('.md').write_text('SYNTHETIC CARD DOCUMENT FIXTURE\n')
        # Integrity tests below isolate freeze mechanics. The real baseline is tested separately.
        stub = patch.object(v, 'verify_protected', return_value={'synthetic-baseline': 'fixture'})
        stub.start()
        self.addCleanup(stub.stop)
        return root, directory

    def test_repository_inputs_and_protected_baseline(self):
        tasks, mappings = v.validate_inputs(self.design, self.cards)
        manifest, packets = v.planned_runs(tasks, mappings)
        self.assertEqual(len(manifest['runs']), 50)
        self.assertEqual(len(packets), 50)
        self.assertGreater(len(v.verify_protected(REPO)), 0)
        self.assertEqual({r['condition'] for r in manifest['runs']}, set(v.CONDITIONS))
        self.assertTrue(all(r['actual_receipt'] is None for r in manifest['runs']))

    def test_c06_common_requirement_is_explicit_in_all_fifty_packets(self):
        tasks, mappings = v.validate_inputs(self.design, self.cards)
        _, packets = v.planned_runs(tasks, mappings)
        requirement = ('Remain civil and proportionate; do not assume unstated vulnerability, '
                       'claim personal feelings, or give unsupported guarantees.')
        self.assertEqual(len(packets), 50)
        for name, packet in packets.items():
            with self.subTest(packet=name):
                self.assertIn(requirement, packet)

    def test_real_git_baseline_rejects_protected_mutation_addition_and_deletion(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            for folder in v.PROTECTED:
                shutil.copytree(REPO / folder, root / folder,
                                ignore=shutil.ignore_patterns('mapping-v2', '__pycache__'))
            git_directory = v.subprocess.run(['git', 'rev-parse', '--absolute-git-dir'],
                cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
            (root / '.git').write_text('gitdir: ' + git_directory + '\n')
            v.verify_protected(root)
            existing = root / 'persona-design-v0.2/protocol.md'
            original = existing.read_bytes()
            existing.write_bytes(original + b'\nSYNTHETIC MUTATION\n')
            with self.assertRaisesRegex(v.ValidationError, 'protected v1 file changed'):
                v.verify_protected(root)
            existing.write_bytes(original)
            extra = root / 'evaluation/pilot-2026-10-22/raw/synthetic-extra.txt'
            extra.write_text('SYNTHETIC EXTRA')
            with self.assertRaisesRegex(v.ValidationError, 'file set changed'):
                v.verify_protected(root)
            extra.unlink()
            existing.unlink()
            with self.assertRaisesRegex(v.ValidationError, 'file set changed'):
                v.verify_protected(root)

    def test_prepare_freeze_verify_and_refuse_overwrite(self):
        root, directory = self.temporary_package()
        result = v.prepare(root)
        self.assertEqual(result['generated_outputs'], 0)
        self.assertFalse(result['semantic_validation'])
        self.assertEqual(v.verify(root), result)
        before = (directory / 'frozen-hashes.json').read_bytes()
        with self.assertRaisesRegex(v.ValidationError, 'refusing overwrite'):
            v.prepare(root)
        self.assertEqual((directory / 'frozen-hashes.json').read_bytes(), before)

    def test_missing_middle_or_neutral_cannot_hide_as_duplicate(self):
        for condition in ('middle', 'neutral'):
            with self.subTest(condition=condition):
                root, directory = self.temporary_package()
                v.prepare(root)
                manifest = v.read_json(directory / 'manifest.json')
                index = next(i for i, r in enumerate(manifest['runs']) if r['condition'] == condition)
                manifest['runs'][index] = copy.deepcopy(manifest['runs'][-1])
                v.write_json(directory / 'manifest.json', manifest)
                with self.assertRaisesRegex(v.ValidationError, 'planned slots changed'):
                    v.verify(root, check_hashes=False)

    def test_context_reuse_nonfocal_constraint_and_receipt_are_rejected(self):
        mutations = (
            lambda runs: runs[1].update(context_slot=runs[0]['context_slot']),
            lambda runs: runs[0]['targets'].update({'bfas.volatility': 'middle'}),
            lambda runs: runs[0].update(actual_receipt={'status': 'synthetic-not-a-receipt'}),
            lambda runs: runs[0].update(persona_packet=True),
        )
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                root, directory = self.temporary_package()
                v.prepare(root)
                manifest = v.read_json(directory / 'manifest.json')
                mutate(manifest['runs'])
                v.write_json(directory / 'manifest.json', manifest)
                with self.assertRaisesRegex(v.ValidationError, 'planned slots changed'):
                    v.verify(root, check_hashes=False)

    def test_neutral_and_unspecified_remain_distinct(self):
        tasks, mappings = v.validate_inputs(self.design, self.cards)
        mapping = next(iter(mappings.values()))
        task = tasks[mapping['task_id']]
        neutral = v.render_packet(task, mapping, 'neutral')
        unspecified = v.render_packet(task, mapping, 'unspecified')
        self.assertNotIn('Qualitative targets', neutral)
        self.assertIn('Qualitative targets', unspecified)
        self.assertIn('explicitly unconstrained', unspecified)
        self.assertNotIn('"middle"', unspecified)

    def test_exact_packet_rule_mutation_rejected_before_freeze_checks(self):
        root, directory = self.temporary_package()
        v.prepare(root)
        path = directory / 'packets/b03-low-1.md'
        path.write_text(path.read_text() + '\nSYNTHETIC ADDED RULE\n')
        with self.assertRaisesRegex(v.ValidationError, 'packet differs'):
            v.verify(root, check_hashes=False)

    def test_rubric_cannot_add_task_requirement(self):
        self.reject(lambda d, c: d['tasks'][0]['rubric_required_ids'].append('invented-requirement'))

    def test_stale_or_wrong_mapping_identity_and_invented_absence_ban(self):
        for field, value in (('mapping_id', 'map.compassion.v1'),
                             ('mapping_id', 'map.volatility.v2')):
            with self.subTest(value=value):
                cards = copy.deepcopy(self.cards)
                cards['mappings'][0][field] = value
                with self.assertRaisesRegex(v.ValidationError, 'mapping ID/version'):
                    v.validate_inputs(self.design, cards)
        mapping = self.cards['mappings'][0]
        low, high = mapping['anchors']['low'], mapping['anchors']['high']
        low['expected_absent'] = high['expected_present'][:1]
        with self.assertRaisesRegex(v.ValidationError, 'no feature-absence bans'):
            v.validate_inputs(self.design, self.cards)

    def test_prospective_order_is_fixed_hash_sort(self):
        root, directory = self.temporary_package()
        v.prepare(root)
        order = v.read_json(directory / 'order.json')
        order[0], order[1] = order[1], order[0]
        v.write_json(directory / 'order.json', order)
        with self.assertRaisesRegex(v.ValidationError, 'fixed hash-sort'):
            v.verify(root, check_hashes=False)

    def test_anchor_feature_requires_rule_clause_trace(self):
        mapping = self.cards['mappings'][0]
        anchor = mapping['anchors']['low']
        unreferenced = next(c['id'] for c in mapping['rule_clauses'] if c['id'] not in anchor['rule_clause_ids'])
        feature_id = anchor['expected_present'][0]
        feature = next(f for f in mapping['features'] if f['id'] == feature_id)
        feature['rule_clause_ids'].append(unreferenced)
        with self.assertRaisesRegex(v.ValidationError, 'absent from its rule clauses'):
            v.validate_inputs(self.design, self.cards)

    def test_ambiguity_wordcount_and_stop_policies_are_explicit(self):
        for field, value in (('ambiguity_policy', ''), ('word_limit', 180),
                             ('word_count_method', 'exclude headings'), ('stop_rule', 'continue')):
            with self.subTest(field=field):
                design = copy.deepcopy(self.design)
                design['tasks'][0][field] = value
                with self.assertRaises(v.ValidationError):
                    v.validate_inputs(design, self.cards)

    def test_design_cannot_claim_confirmation_release_or_outputs(self):
        for field, value in (('human_confirmation', 'confirmed'), ('release_status', 'passed'),
                             ('generated_output_count', 1), ('generated_output_count', False),
                             ('status', 'behaviorally_validated')):
            with self.subTest(field=field, value=value):
                design = copy.deepcopy(self.design)
                design[field] = value
                with self.assertRaises(v.ValidationError):
                    v.validate_inputs(design, self.cards)

    def test_judges_need_distinct_ids_paths_blinding_and_both_locks(self):
        changes = (
            lambda d: d['judges'][1].update(id=d['judges'][0]['id']),
            lambda d: d['judges'][1].update(lock_path=d['judges'][0]['lock_path']),
            lambda d: d['judges'][0].update(blind_to=['condition']),
            lambda d: d['judges'][0].update(independent_before_comparison=False),
            lambda d: d['rating_policy'].update(comparison_gate='first_judge_lock'),
            lambda d: d['rating_policy'].update(feature_values=['present', 'absent']),
        )
        for change in changes:
            with self.subTest(change=change):
                design = copy.deepcopy(self.design)
                change(design)
                with self.assertRaises(v.ValidationError):
                    v.validate_inputs(design, self.cards)

    def test_freeze_rejects_changed_added_and_removed_inputs(self):
        for action in ('change', 'add', 'remove'):
            with self.subTest(action=action):
                root, directory = self.temporary_package()
                v.prepare(root)
                if action == 'change':
                    (directory / 'PLAN.md').write_text('SYNTHETIC MUTATION')
                elif action == 'add':
                    (directory / 'packets/extra.md').write_text('SYNTHETIC EXTRA')
                else:
                    (directory / 'packets/b03-low-1.md').unlink()
                with self.assertRaises(v.ValidationError):
                    v.verify(root)

    def test_hashes_rechecked_after_validation(self):
        root, directory = self.temporary_package()
        v.prepare(root)
        original = v.validate_inputs
        def change_during_validation(*args):
            result = original(*args)
            (directory / 'PLAN.md').write_text('SYNTHETIC MID-CHECK MUTATION')
            return result
        with patch.object(v, 'validate_inputs', side_effect=change_during_validation):
            with self.assertRaisesRegex(v.ValidationError, 'frozen input hash changed'):
                v.verify(root)

    def test_generated_evidence_is_rejected(self):
        root, directory = self.temporary_package()
        v.prepare(root)
        (directory / 'raw').mkdir()
        (directory / 'raw/synthetic.txt').write_text('SYNTHETIC FORBIDDEN OUTPUT PLACEHOLDER')
        with self.assertRaisesRegex(v.ValidationError, 'generated evidence'):
            v.verify(root)

    def test_judge_paths_resolve_inside_diagnostic_and_reject_parent_traversal(self):
        root, directory = self.temporary_package()
        v.prepare(root)
        judge = self.design['judges'][0]
        lock = directory / judge['lock_path']
        lock.parent.mkdir(parents=True, exist_ok=True)
        lock.write_text('SYNTHETIC FORBIDDEN LOCK FIXTURE')
        with self.assertRaisesRegex(v.ValidationError, 'must not contain ratings or judge locks'):
            v.verify(root)
        lock.unlink()
        changed = copy.deepcopy(self.design)
        changed['judges'][0]['lock_path'] = '../escaped-lock.json'
        v.write_json(directory / 'design.json', changed)
        with self.assertRaisesRegex(v.ValidationError, 'must stay within'):
            v.verify(root, check_hashes=False)

    def test_duplicate_keys_nonfinite_json_and_escaping_paths(self):
        root, directory = self.temporary_package()
        path = directory / 'malformed.json'
        for value in ('{"a":1,"a":2}', '[NaN]', '[Infinity]', '{'):
            with self.subTest(value=value):
                path.write_text(value)
                with self.assertRaises(v.ValidationError):
                    v.read_json(path)
        for name in ('../outside', '/tmp/outside'):
            with self.assertRaises(v.ValidationError):
                v.local_path(root, name)
        (directory / 'escape').symlink_to('/tmp')
        with self.assertRaises(v.ValidationError):
            v.local_path(root, f'{v.DESIGN_DIR}/escape/outside')

    def test_cli_reports_failure_without_generation(self):
        root, directory = self.temporary_package()
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(v.main(['verify', '--repo-root', str(root)]), 1)
        self.assertFalse((directory / 'packets').exists())


if __name__ == '__main__':
    unittest.main()
