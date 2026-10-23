"""Synthetic mechanical join tests; no substantive ratings or pilot results."""
import json
from pathlib import Path
import tempfile
import unittest

import pilot
import summarize_pilot as summary
import verify_ratings as vr


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'frozen').mkdir()
        names = ['volatility', 'withdrawal', 'compassion', 'politeness', 'industriousness',
                 'orderliness', 'enthusiasm', 'assertiveness', 'intellect', 'openness']
        registry = self.root / 'synthetic-registry.md'
        registry.write_text('\n'.join(f'| `map.{name}.v1` | fixture | SYNTHETIC LOW | fixture | SYNTHETIC HIGH | fixture |' for name in names))
        (self.root / 'frozen/plan.md').write_text('SYNTHETIC structural test only\n' + '\n'.join(
            f'| A{i:02} | map.{name}.v1 / B{i:02} | Synthetic | fixture |' for i, name in enumerate(names, 1)))
        pilot.write_json(self.root / 'frozen/scenarios.json', {'output_budget_words': 250,
            'scenarios': [{'id': f'S{i}', 'round1': f'SYNTHETIC task {i}', 'round2': f'SYNTHETIC changed {i}'} for i in range(1, 4)],
            'round3': 'SYNTHETIC pressure task'})
        pilot.write_json(self.root / 'frozen/rubric.json', {'axes': [
            {'id': f'A{i:02}', 'categories': {f'fixture_{j}': 'synthetic' for j in range(3)}, 'evidence_class': 'synthetic'}
            for i in range(1, 11)], 'guardrails': [{'id': f'G{i:02}'} for i in range(1, 10)],
            'common_axis_categories': {'unclear': 'synthetic'}})
        pilot.prepare(self.root, registry, 20261022)
        manifest = pilot.read_json(self.root / 'manifest.json')
        for output in manifest['outputs']:
            path = self.root / output['raw']
            path.write_text('SYNTHETIC response ' + output['run_id'])
            agent = '/root/synthetic_' + output['session_id']
            output['receipt'] = {'sha256': pilot.digest(path), 'agent_id': agent,
                'started_at': '2026-10-22T09:00:00Z', 'ended_at': '2026-10-22T09:00:01Z',
                'requested_tool': 'collaboration.spawn_agent' if output['turn'] == 1 else 'collaboration.followup_task',
                'requested_parameters': {'message': (self.root / output['message']).read_text(),
                    **({'task_name': agent, **manifest['tested_requested']} if output['turn'] == 1 else {'target': agent})},
                'returned_metadata': {'task_name': agent, 'acknowledged': True},
                'limitations': ['SYNTHETIC fixture; acknowledgment is not completion proof']}
        pilot.write_json(self.root / 'manifest.json', manifest)
        pilot.blind(self.root)
        (self.root / 'ratings').mkdir()
        self.ratings = []
        for i, path in enumerate(sorted((self.root / 'blind').glob('*.json'))):
            self.ratings.append({'blind_id': path.stem,
                'axes': [{'axis_id': f'A{a:02}', 'category': f'fixture_{i % 3}', 'quotes': ['SYNTHETIC'],
                          'reason': 'SYNTHETIC fixture', 'confidence': 'limited'} for a in range(1, 11)],
                'guardrails': [{'guardrail_id': f'G{g:02}', 'rating': 'violation' if i == 0 and g == 1 else 'unclear',
                                'quotes': [], 'reason': 'SYNTHETIC fixture'} for g in range(1, 10)],
                'blind_leakage': {'present': i == 0, 'quotes': ['SYNTHETIC'] if i == 0 else [], 'reason': 'SYNTHETIC fixture'},
                'limitations': ['SYNTHETIC fixture only']})
        pilot.write_json(self.root / 'ratings/batch01.json', self.ratings)

    def test_lock_gate_precedes_crosswalk_read_and_no_files_written(self):
        (self.root / 'blind-crosswalk.json').write_text('not JSON')
        with self.assertRaisesRegex(ValueError, 'Ratings lock required'):
            summary.summarize(self.root)
        self.assertFalse((self.root / 'analysis').exists())

    def test_complete_join_baselines_flags_and_tables(self):
        vr.lock(self.root)
        doc = summary.summarize(self.root)
        self.assertEqual(len(doc['outputs']), 102)
        self.assertEqual(len(doc['initial_pairs']), 30)
        self.assertEqual(len(doc['repeat_comparisons']), 13)
        self.assertEqual(len(doc['multi_round']), 13)
        self.assertEqual(len(doc['a05_a06_cross_axis']), 18)
        self.assertEqual(len(doc['guardrail_violations']), 1)
        self.assertEqual(len(doc['blind_leakage_present']), 1)
        self.assertTrue(all(r['word_count_whitespace'] == 3 for r in doc['outputs']))
        by_blind = {r['blind_id']: r for r in self.ratings}
        for pair in doc['initial_pairs']:
            for role in ('low', 'high', 'shared_baseline'):
                observed = pair[role]
                exact = next(a['category'] for a in by_blind[observed['blind_id']]['axes'] if a['axis_id'] == pair['axis_id'])
                self.assertEqual(observed['categories'][pair['axis_id']], exact)
            baseline_ids = {p['shared_baseline']['blind_id'] for p in doc['initial_pairs'] if p['scenario'] == pair['scenario']}
            self.assertEqual(len(baseline_ids), 1)
        self.assertEqual(len({p['shared_baseline']['blind_id'] for p in doc['initial_pairs']}), 3)
        table = (self.root / 'analysis/report-tables.md').read_text()
        self.assertIn('B05 / A05 / S1', table)
        self.assertIn('SYNTHETIC fixture', table)
        self.assertIn('guardrail', table)
        self.assertEqual(json.loads((self.root / 'analysis/observations.json').read_text()), doc)
        with self.assertRaisesRegex(ValueError, 'refusing overwrite'):
            summary.summarize(self.root)

    def test_changed_ratings_and_raw_block_summary(self):
        vr.lock(self.root)
        path = self.root / 'ratings/batch01.json'
        original = path.read_bytes()
        path.write_bytes(original + b' ')
        with self.assertRaisesRegex(ValueError, 'Locked ratings'):
            summary.summarize(self.root)
        path.write_bytes(original)
        output = pilot.read_json(self.root / 'manifest.json')['outputs'][0]
        (self.root / output['raw']).write_text('SYNTHETIC tampering')
        with self.assertRaisesRegex(ValueError, 'Raw output'):
            summary.summarize(self.root)
        self.assertFalse((self.root / 'analysis').exists())

    def test_crosswalk_must_cover_and_match_conversations(self):
        vr.lock(self.root)
        path = self.root / 'blind-crosswalk.json'
        crosswalk = pilot.read_json(path)
        original = dict(crosswalk)
        keys = list(crosswalk)
        crosswalk.pop(keys[0])
        pilot.write_json(path, crosswalk)
        with self.assertRaisesRegex(ValueError, 'coverage mismatch'):
            summary.summarize(self.root)
        crosswalk = original.copy()
        crosswalk[keys[0]], crosswalk[keys[1]] = crosswalk[keys[1]], crosswalk[keys[0]]
        pilot.write_json(path, crosswalk)
        with self.assertRaisesRegex(ValueError, 'conversation mismatch'):
            summary.summarize(self.root)
        self.assertFalse((self.root / 'analysis').exists())


if __name__ == '__main__':
    unittest.main()
