"""Semantic mutations of hand-authored synthetic records; no model calls."""
import copy
from pathlib import Path
import tempfile
import unittest

from validate_spec import (ValidationError, digest, load, main, validate_preview, validate_spec)

FIXTURES = Path(__file__).parent / "fixtures"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.preview = load(FIXTURES / "mixed-preview.md")
        self.spec = load(FIXTURES / "mixed-spec.md")

    def rejected_preview(self, mutate):
        mutate(self.preview)
        with self.assertRaises(ValidationError):
            validate_preview(self.preview)

    def rejected_spec(self, mutate):
        mutate(self.spec)
        with self.assertRaises(ValidationError):
            validate_spec(self.spec, self.preview)

    def test_valid_fixtures_and_explicit_middle(self):
        validate_preview(self.preview)
        validate_spec(self.spec, self.preview)
        self.assertEqual(self.preview['targets']['bfas.assertiveness'], 'middle')
        self.assertEqual(self.preview['targets']['bfas.orderliness'], 'unspecified')
        self.assertEqual(len(self.preview['conflicts'][0]['candidates']), 2)

    def test_all_unspecified_is_valid_and_unconstrained(self):
        p = load(FIXTURES / "all-unspecified-preview.md")
        validate_preview(p)
        self.assertEqual(set(p['targets'].values()), {'unspecified'})
        self.assertEqual(p['mappings'], [])

    def test_unknown_aspect(self):
        self.rejected_preview(lambda p: p['targets'].update({'bfas.honesty': 'high'}))

    def test_missing_unspecified_aspect(self):
        self.rejected_preview(lambda p: p['targets'].pop('bfas.openness'))

    def test_numeric_score(self):
        self.rejected_preview(lambda p: p['targets'].update({'bfas.openness': 70}))

    def test_unspecified_cannot_be_silently_middle(self):
        self.rejected_preview(lambda p: p['targets'].update({'bfas.openness': 'middle'}))

    def test_rule_cannot_constrain_unspecified(self):
        def mutate(p):
            p['targets']['bfas.assertiveness'] = 'unspecified'
        self.rejected_preview(mutate)

    def test_conflicting_mapping_targets(self):
        def mutate(p):
            row = copy.deepcopy(p['mappings'][0])
            row['id'] = 'conflicting-second-rule'
            row['target'] = 'low'
            p['mappings'].append(row)
        self.rejected_preview(mutate)

    def test_dangling_answer(self):
        self.rejected_preview(lambda p: p['mappings'][0].update(answer_id='absent'))

    def test_dangling_source(self):
        self.rejected_preview(lambda p: p['mappings'][0].update(source_id='absent'))

    def test_human_construct_source_is_not_agent_mapping_evidence(self):
        self.rejected_preview(lambda p: p['mappings'][0].update(source_id='src.deyoung2007'))

    def test_mismatched_mapping_id(self):
        self.rejected_preview(lambda p: p['mappings'][0].update(id='map.openness.v1'))

    def test_missing_or_stale_approval(self):
        for field in ('status', 'revision', 'digest', 'confirmed_by', 'record_ref'):
            with self.subTest(field=field):
                spec = copy.deepcopy(self.spec)
                spec['approval'][field] = ''
                with self.assertRaises(ValidationError):
                    validate_spec(spec, self.preview)

    def test_no_approval(self):
        self.rejected_spec(lambda s: s.pop('approval'))

    def test_changed_preview_rejected_even_with_forged_matching_digest(self):
        def mutate(s):
            s['approved_preview']['scenario'] += ' Changed after approval.'
            s['approval']['digest'] = digest(s['approved_preview'])
        self.rejected_spec(mutate)

    def test_unresolved_conflict_blocks_final(self):
        self.preview['conflicts'][0]['status'] = 'unresolved'
        self.preview['conflicts'][0]['resolution'] = ''
        self.preview['conflicts'][0]['resolution_answer_id'] = ''
        validate_preview(self.preview)  # Reviewable draft is allowed.
        self.spec['approved_preview'] = copy.deepcopy(self.preview)
        self.spec['approval']['digest'] = digest(self.preview)
        with self.assertRaises(ValidationError):
            validate_spec(self.spec, self.preview)

    def test_withdrawal_cannot_erase_candidate_evidence(self):
        self.rejected_preview(lambda p: p['conflicts'][0].update(candidates=[]))

    def test_resolution_needs_answer_reference(self):
        self.rejected_preview(lambda p: p['conflicts'][0].update(resolution_answer_id='missing'))

    def test_safety_boundaries_cannot_be_weakened(self):
        for boundary in self.preview['boundaries']:
            with self.subTest(boundary=boundary):
                p = copy.deepcopy(self.preview)
                p['boundaries'][boundary] = not p['boundaries'][boundary]
                with self.assertRaises(ValidationError):
                    validate_preview(p)

    def test_workflow_boundary_cannot_override_invariants(self):
        self.rejected_preview(lambda p: p['workflow_controls'].update(boundary_posture='ignore privacy'))

    def test_fake_behavioral_evidence(self):
        self.rejected_preview(lambda p: p['evidence'].update(kind='observed', behavioral_validation=True))

    def test_validator_pass_is_not_behavioral_validation(self):
        self.rejected_preview(lambda p: p['evidence'].update(behavioral_validation=True))

    def test_missing_nonclaim(self):
        self.rejected_preview(lambda p: p['non_claims'].remove('psychometric_validity'))

    def test_manual_review_distinct_from_confirmation(self):
        self.rejected_spec(lambda s: s.update(review='Not reviewed'))

    def test_markdown_only_confirmation_can_leave_digest_null(self):
        self.spec['approval']['digest'] = None
        validate_spec(self.spec, self.preview)

    def test_same_target_conflict_retains_distinct_answer_evidence(self):
        conflict = self.preview['conflicts'][0]
        conflict['candidates'][1]['target'] = conflict['candidates'][0]['target']
        validate_preview(self.preview, final=True)
        conflict['status'] = 'unresolved'
        conflict['resolution'] = ''
        conflict['resolution_answer_id'] = ''
        validate_preview(self.preview)
        with self.assertRaises(ValidationError):
            validate_preview(self.preview, final=True)

    def test_exact_duplicate_conflict_candidate_rejected(self):
        self.preview['conflicts'][0]['candidates'][1] = copy.deepcopy(self.preview['conflicts'][0]['candidates'][0])
        with self.assertRaises(ValidationError):
            validate_preview(self.preview)

    def test_workflow_conflict_retains_candidates_and_resolution(self):
        conflict = self.preview['conflicts'][0]
        conflict['aspect'] = 'workflow_controls.communication_posture'
        conflict['candidates'][0]['target'] = 'concise'
        conflict['candidates'][1]['target'] = 'detailed'
        validate_preview(self.preview, final=True)
        conflict['resolution_answer_id'] = []
        with self.assertRaises(ValidationError):
            validate_preview(self.preview, final=True)

    def test_filled_template_matches_validator_contract(self):
        template = load(FIXTURES.parent.parent / 'persona-design-v0.2' / 'spec-template.md')
        for key in ('scenario', 'answers', 'sources', 'unknowns'):
            template[key] = copy.deepcopy(self.preview[key])
        validate_preview(template)

    def test_digest_independent_of_key_order(self):
        self.assertEqual(digest(self.preview), digest(dict(reversed(list(self.preview.items())))))

    def test_cli_rejects_changed_reload(self):
        import json
        import contextlib
        import io
        changed = copy.deepcopy(self.spec)
        changed['approval']['record_ref'] = 'different confirmation record'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'changed.md'
            path.write_text('```json\n' + json.dumps(changed) + '\n```\n')
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(['spec', str(FIXTURES / 'mixed-spec.md'), '--preview', str(FIXTURES / 'mixed-preview.md'), '--reload', str(path)]), 1)

    def test_duplicate_keys_and_multiple_payloads_rejected(self):
        for content in ('```json\n{"x":1,"x":2}\n```\n', '```json\n{}\n```\n```json\n{}\n```\n'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'bad.md'
                path.write_text(content)
                with self.assertRaises(ValidationError):
                    load(path)


if __name__ == '__main__':
    unittest.main()
