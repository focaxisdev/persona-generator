"""Synthetic structural-lint fixtures only; no substantive judging evidence."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import verify_ratings as vr


class RatingIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ('frozen', 'blind', 'ratings'):
            (self.root / folder).mkdir()
        # All text and categories here are synthetic, never actual ratings.
        rubric = {'axes': [{'id': f'A{i:02}', 'categories': {'synthetic': 'fixture'}}
                           for i in range(1, 11)],
                  'guardrails': [{'id': f'G{i:02}'} for i in range(1, 10)],
                  'common_axis_categories': {'unclear': 'fixture'}}
        self.write('frozen/rubric.json', rubric)
        self.write('frozen-hashes.json', {'files': {'frozen/rubric.json': vr.digest(self.root / 'frozen/rubric.json')}})
        self.ratings = []
        for i in range(1, 103):
            item_id = f'item{i:03}'
            self.write(f'blind/{item_id}.json', {'item_id': item_id, 'conversation': [
                {'task': 'Synthetic earlier task', 'response': 'SYNTHETIC PRIOR ONLY'},
                {'task': 'Synthetic current task', 'response': 'SYNTHETIC CURRENT RESPONSE'}]})
            self.ratings.append({'blind_id': item_id,
                'axes': [{'axis_id': f'A{a:02}', 'category': 'synthetic',
                          'quotes': ['CURRENT'], 'reason': 'Synthetic reason', 'confidence': 'limited'}
                         for a in range(1, 11)],
                'guardrails': [{'guardrail_id': f'G{g:02}', 'rating': 'unclear',
                                'quotes': [], 'reason': 'Synthetic absence explanation'}
                               for g in range(1, 10)],
                'blind_leakage': {'present': False, 'quotes': [], 'reason': 'Synthetic observation limit'},
                'limitations': ['Synthetic fixture only']})
        self.write('blind-hashes.json', vr.file_hashes(self.root / 'blind'))
        self.write('ratings/batch01.json', self.ratings)

    def write(self, name, value):
        (self.root / name).write_text(json.dumps(value), encoding='utf-8')

    def reject_rating(self, change):
        rows = copy.deepcopy(self.ratings)
        change(rows)
        self.write('ratings/batch01.json', rows)
        with self.assertRaises(ValueError):
            vr.verify(self.root)

    def test_complete_lock_and_unchanged_verify(self):
        state = vr.verify(self.root)
        self.assertEqual(state['item_count'], 102)
        self.assertFalse((self.root / vr.LOCK_NAME).exists())
        vr.lock(self.root)
        locked = json.loads((self.root / vr.LOCK_NAME).read_text())
        self.assertEqual(locked['rating_hashes'], state['rating_hashes'])
        self.assertEqual(vr.verify(self.root), state)
        before = (self.root / vr.LOCK_NAME).read_bytes()
        with self.assertRaisesRegex(ValueError, 'refusing overwrite'):
            vr.lock(self.root)
        self.assertEqual(before, (self.root / vr.LOCK_NAME).read_bytes())

    def test_coverage_missing_duplicate_unknown_and_split_batches(self):
        self.reject_rating(lambda rows: rows.pop())
        self.reject_rating(lambda rows: rows.append(copy.deepcopy(rows[0])))
        self.reject_rating(lambda rows: rows[0].update(blind_id='unknown'))
        self.write('ratings/batch01.json', self.ratings[:51])
        self.write('ratings/batch02.json', self.ratings[51:])
        vr.verify(self.root)
        self.write('ratings/old-attempt.json', [self.ratings[0]])
        with self.assertRaisesRegex(ValueError, 'duplicate blind_id'):
            vr.verify(self.root)

    def test_all_evidence_must_be_from_current_response(self):
        for target in ('axes', 'guardrails', 'blind_leakage'):
            with self.subTest(target=target):
                def change(rows):
                    value = rows[0][target]
                    (value if isinstance(value, dict) else value[0])['quotes'] = ['PRIOR ONLY']
                self.reject_rating(change)
        self.reject_rating(lambda rows: rows[0]['axes'][0].update(quotes=['current']))
        self.reject_rating(lambda rows: rows[0]['axes'][0].update(quotes=['']))
        self.reject_rating(lambda rows: rows[0]['axes'][0].update(quotes='CURRENT'))

    def test_axis_and_guardrail_cardinality_and_enums(self):
        cases = [
            lambda r: r[0]['axes'].pop(),
            lambda r: r[0]['axes'].append(copy.deepcopy(r[0]['axes'][0])),
            lambda r: r[0]['axes'][0].update(axis_id='A99'),
            lambda r: r[0]['axes'][0].update(category='invalid'),
            lambda r: r[0]['axes'][0].update(confidence='high'),
            lambda r: r[0]['guardrails'].pop(),
            lambda r: r[0]['guardrails'].append(copy.deepcopy(r[0]['guardrails'][0])),
            lambda r: r[0]['guardrails'][0].update(guardrail_id='G99'),
            lambda r: r[0]['guardrails'][0].update(rating='fail'),
        ]
        for change in cases:
            with self.subTest(change=change):
                self.reject_rating(change)
        rows = copy.deepcopy(self.ratings)
        rows[0]['axes'][0].update(category='unclear', quotes=[])
        self.write('ratings/batch01.json', rows)
        vr.verify(self.root)

    def test_declared_axis_category_requires_quotes_but_absence_does_not(self):
        self.reject_rating(lambda rows: rows[0]['axes'][0].update(quotes=[]))
        rows = copy.deepcopy(self.ratings)
        rows[0]['axes'][0].update(category='unclear', quotes=[])
        rows[0]['guardrails'][0].update(rating='pass', quotes=[])
        self.write('ratings/batch01.json', rows)
        vr.verify(self.root)

    def test_exact_fields_reasons_and_types(self):
        cases = [
            lambda r: r[0].update(extra='forbidden'),
            lambda r: r[0]['axes'][0].update(extra='forbidden'),
            lambda r: r[0]['axes'][0].update(reason='  '),
            lambda r: r[0]['guardrails'][0].update(reason=None),
            lambda r: r[0]['blind_leakage'].update(reason=''),
            lambda r: r[0]['blind_leakage'].update(present=1),
            lambda r: r[0].update(limitations='synthetic'),
            lambda r: r[0].update(limitations=[None]),
            lambda r: r[0].update(axes=None),
            lambda r: r[0].update(guardrails={}),
            lambda r: r[0].update(blind_id=[]),
            lambda r: r[0]['axes'][0].update(axis_id=[]),
            lambda r: r[0]['guardrails'][0].update(rating=[]),
            lambda r: r.__setitem__(0, None),
        ]
        for change in cases:
            with self.subTest(change=change):
                self.reject_rating(change)

    def test_postlock_rating_changes_even_valid_revisions_rejected(self):
        vr.lock(self.root)
        self.ratings[0]['axes'][0]['reason'] = 'Another structurally valid synthetic reason'
        self.write('ratings/batch01.json', self.ratings)
        with self.assertRaisesRegex(ValueError, 'Locked ratings or blind inputs changed'):
            vr.verify(self.root)

    def test_postlock_rating_file_set_changes_rejected(self):
        vr.lock(self.root)
        (self.root / 'ratings/batch01.json').rename(self.root / 'ratings/renamed.json')
        with self.assertRaisesRegex(ValueError, 'Locked ratings or blind inputs changed'):
            vr.verify(self.root)

    def test_blind_and_rubric_mutation_rejected(self):
        path = self.root / 'blind/item001.json'
        path.write_text(path.read_text() + ' ')
        with self.assertRaisesRegex(ValueError, 'Blind file/hash set changed'):
            vr.verify(self.root)
        self.write('blind-hashes.json', vr.file_hashes(self.root / 'blind'))
        vr.lock(self.root)
        path.write_text(path.read_text() + ' ')
        self.write('blind-hashes.json', vr.file_hashes(self.root / 'blind'))
        with self.assertRaisesRegex(ValueError, 'Locked ratings or blind inputs changed'):
            vr.verify(self.root)
        path = self.root / 'frozen/rubric.json'
        path.write_text(path.read_text() + ' ')
        with self.assertRaisesRegex(ValueError, 'Frozen rubric hash changed'):
            vr.verify(self.root)

    def test_malformed_json_duplicate_keys_and_constants(self):
        for value in ('{', '{"x":1,"x":2}', '[NaN]', '[Infinity]', '{}', 'null', '[[]]'):
            with self.subTest(value=value):
                (self.root / 'ratings/batch01.json').write_text(value)
                with self.assertRaises(ValueError):
                    vr.verify(self.root)

    def test_malformed_blind_and_rubric_fail_cleanly(self):
        for value in ([], None, {}, {'item_id': [], 'conversation': []},
                      {'item_id': 'item001', 'conversation': [None]}):
            with self.subTest(value=value):
                self.write('blind/item001.json', value)
                self.write('blind-hashes.json', vr.file_hashes(self.root / 'blind'))
                with self.assertRaises(ValueError):
                    vr.verify(self.root)
        for value in ([], None, {}, {'axes': [None], 'guardrails': [], 'common_axis_categories': {}}):
            with self.subTest(rubric=value):
                self.write('frozen/rubric.json', value)
                self.write('frozen-hashes.json', {'files': {'frozen/rubric.json': vr.digest(self.root / 'frozen/rubric.json')}})
                with self.assertRaises(ValueError):
                    vr.verify(self.root)

    def test_incomplete_lock_writes_nothing_and_repairs_allowed_before_lock(self):
        self.write('ratings/batch01.json', self.ratings[:-1])
        with self.assertRaises(ValueError):
            vr.lock(self.root)
        self.assertFalse((self.root / vr.LOCK_NAME).exists())
        self.write('ratings/batch01.json', self.ratings)
        vr.lock(self.root)


if __name__ == '__main__':
    unittest.main()
