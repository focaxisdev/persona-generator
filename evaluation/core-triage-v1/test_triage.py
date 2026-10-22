"""Static protocol integrity checks; no task answers, model calls or ratings."""
import copy
from contextlib import redirect_stdout
import io
import json
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('triage', Path(__file__).with_name('triage.py'))
triage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(triage)

class PreparationTests(unittest.TestCase):
    def test_complete_real_envelope_grid_and_neutral_equivalence(self):
        design = triage.read(Path(__file__).with_name('design.json'))
        triage.validate_design(design)
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            cells = triage.make_assets(base, design)
            self.assertEqual(len(cells), 18)
            self.assertEqual(len({c['id'] for c in cells}), 18)
            self.assertEqual([c['order'] for c in cells], list(range(1, 19)))
            from core.envelope import build_request, build_neutral_request
            cases = {c['id']: c for c in design['cases']}
            for cell in cells:
                asset = base / cell['asset']
                envelope = build_request(asset / 'spec.json', asset / 'preview.json', cases[cell['case']]['task'], cell['id'])
                self.assertEqual(envelope.request_bytes, (asset / 'request.json').read_bytes())
                self.assertEqual(envelope.tool_args['fork_turns'], 'none')
                preview = triage.read(asset / 'preview.json')
                self.assertEqual(preview['controls']['response_detail']['value'], 'unspecified')
                active = [v for v in preview['targets'].values() if v != 'unspecified']
                self.assertEqual(active, [] if cell['condition'] == 'unspecified' else [cell['condition']])
                if cell['condition'] == 'unspecified':
                    self.assertEqual(envelope.request_bytes, build_neutral_request(cases[cell['case']]['task'], cell['id']).request_bytes)
            self.assertFalse((base / 'outputs').exists())
            self.assertFalse((base / 'ratings').exists())

    def test_incomplete_allocation_rejected(self):
        design = copy.deepcopy(triage.read(Path(__file__).with_name('design.json')))
        design['cases'][0]['category'] = 'nontrigger'
        with self.assertRaises(ValueError):
            triage.validate_design(design)

    def test_judge_observables_identical_and_partial_overrides(self):
        design = triage.read(Path(__file__).with_name('design.json'))
        self.assertTrue(all(c['observables'] == design['cases'][0]['observables'] for c in design['cases']))
        for case in design['cases']:
            if case['category'] == 'override':
                self.assertEqual(case['applicability']['low'], 'applicable')
                self.assertEqual(case['applicability']['high'], 'partially_overridden')
            self.assertEqual(case['applicability']['unspecified'], 'no_active_operation')

    def test_forged_empty_lock_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            triage.write(base / 'locks' / 'req_test.json', {'id': 'req_test', 'files': {}, 'both_independent_ratings_retained': True})
            with patch.object(triage, 'HERE', base), self.assertRaises(ValueError):
                triage.locked('req_test')

    def test_packet_derivation_binds_output_and_common_rubric(self):
        case = triage.read(Path(__file__).with_name('design.json'))['cases'][0]
        # Generic strings test byte binding; neither is a task answer or rating.
        first = triage.packet_payload('req_test', case, {'raw_output': 'opaque integrity fixture one'}, 'a')
        changed = triage.packet_payload('req_test', case, {'raw_output': 'opaque integrity fixture two'}, 'a')
        self.assertNotEqual(first['message'], changed['message'])
        edited = copy.deepcopy(first)
        edited['message'] += ' extra instruction'
        self.assertNotEqual(edited, triage.packet_payload('req_test', case, {'raw_output': 'opaque integrity fixture one'}, 'a'))
        other_judge = triage.packet_payload('req_test', case, {'raw_output': 'opaque integrity fixture one'}, 'b')
        self.assertEqual(first['message'], other_judge['message'])
        self.assertNotEqual(first['task_name'], other_judge['task_name'])
        self.assertNotIn('required_content"', first['message'])
        self.assertNotIn('record_status', first['message'])

    def test_high_planning_uncertain_invented_dependency_is_unclear(self):
        case = triage.read(Path(__file__).with_name('design.json'))['cases'][0]
        values = {o['id']: 'true' for o in case['observables']}
        values['unauthorized_action_claim'] = 'false'
        values['invented_dependencies'] = 'unclear'
        rating = {'observations': [{'id': k, 'value': v} for k, v in values.items()], 'safety': 'clear', 'permission': 'clear', 'task_adequacy': 'adequate', 'leakage': 'none'}
        self.assertEqual(triage.adherence({'condition': 'high'}, case, rating), 'unclear')

    def test_terminal_partial_error_not_completed_adherence(self):
        cell = {'id': 'req_test', 'case': 'p1', 'condition': 'high'}
        case = triage.read(Path(__file__).with_name('design.json'))['cases'][0]
        output = {'status': 'error', 'raw_output': 'opaque retained partial text', 'safety_or_tool_action_issue': False, 'metadata': {'observed_tool_calls': []}}
        with tempfile.TemporaryDirectory() as directory, patch.object(triage, 'HERE', Path(directory)), patch.object(triage, 'verify', return_value=({'cells': [cell]}, {'p1': case})), patch.object(triage, 'output_record', return_value=(cell, case, output)), patch.object(triage, 'locked', return_value={'id': 'req_test'}), patch.object(triage, 'rating_record', return_value={'rating': {'observations': []}}):
            stream = io.StringIO()
            with redirect_stdout(stream):
                triage.reveal()
            joined = json.loads(stream.getvalue())['crosswalk_and_original_ratings'][0]
            self.assertEqual(joined['response_classification'], 'missing/error')
            self.assertFalse(joined['contrast_eligible'])
            self.assertFalse(joined['completed_response_adherence_eligible'])
            self.assertEqual(set(joined['adherence_by_judge'].values()), {'not_evaluated:missing/error'})

    def test_reveal_contrast_requires_clean_opportunity_and_both_ratings(self):
        base_case = triage.read(Path(__file__).with_name('design.json'))['cases'][0]
        observations = {o['id']: 'false' for o in base_case['observables']}
        observations.update(required_content_complete='true', facts_supported='true', scope_preserved='true', explicit_task_format_followed='not_applicable')
        clean = {'observations': [{'id': k, 'value': v} for k, v in observations.items()], 'safety': 'clear', 'permission': 'clear', 'leakage': 'none', 'task_adequacy': 'adequate'}
        variants = [(base_case, clean, clean, True)]
        inadequate = {**clean, 'task_adequacy': 'inadequate'}
        uncertain = copy.deepcopy(clean)
        next(o for o in uncertain['observations'] if o['id'] == 'facts_supported')['value'] = 'unclear'
        variants += [(base_case, clean, inadequate, False), (base_case, inadequate, inadequate, False), (base_case, clean, uncertain, False)]
        variants += [({**base_case, 'category': category}, clean, clean, False) for category in ('nontrigger', 'override')]
        for case, first, second, expected in variants:
            cell = {'id': 'req_test', 'case': 'p1', 'condition': 'high'}
            output = {'status': 'ok', 'raw_output': 'opaque retained protocol fixture', 'safety_or_tool_action_issue': False, 'metadata': {'observed_tool_calls': []}}
            def rating_for(cell_id, judge, task_case, raw):
                return {'rating': first if judge == 'a' else second}
            with tempfile.TemporaryDirectory() as directory, patch.object(triage, 'HERE', Path(directory)), patch.object(triage, 'verify', return_value=({'cells': [cell]}, {'p1': case})), patch.object(triage, 'output_record', return_value=(cell, case, output)), patch.object(triage, 'locked', return_value={'id': 'req_test'}), patch.object(triage, 'rating_record', side_effect=rating_for):
                stream = io.StringIO()
                with redirect_stdout(stream):
                    triage.reveal()
                joined = json.loads(stream.getvalue())['crosswalk_and_original_ratings'][0]
                self.assertEqual(joined['contrast_eligible'], expected)
                self.assertTrue(joined['completed_response_adherence_eligible'])

if __name__ == '__main__':
    unittest.main()
