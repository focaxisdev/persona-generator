"""Temporary-directory protocol tests, never model observations or study results.

The opaque text, receipts, approvals and ratings below are synthetic integrity
fixtures only. They exercise bookkeeping and gates, not semantic judging,
authentic independent review, owner consent, model adherence or empirical claims.
No model or network calls occur; all runtime records live in temporary copies.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[2]
RELATIVE = Path('evaluation/core-triage-v1')
TEXT = 'opaque synthetic integrity fixture'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.chmod(0o644)
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


class ExecutionProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template_tmp = tempfile.TemporaryDirectory()
        cls.template = Path(cls.template_tmp.name)
        # Copy only public protocol inputs; never inspect private owner records.
        shutil.copytree(SOURCE / 'core', cls.template / 'core',
                        ignore=shutil.ignore_patterns('__pycache__'))
        for name in ('construct-registry.md', 'sources.md'):
            target = cls.template / 'persona-design-v0.2' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / 'persona-design-v0.2' / name, target)
        here = cls.template / RELATIVE
        here.mkdir(parents=True)
        for name in ('triage.py', 'design.json', 'README.md'):
            shutil.copyfile(SOURCE / RELATIVE / name, here / name)
        cls.run_cli(cls.template, 'prepare')
        review = cls.template / 'integrity-fixture-review.json'
        save(review, {'decision': 'approve',
                      'reviewer': 'SYNTHETIC integrity fixture; not independent review',
                      'draft_sha256': digest((here / 'draft-hashes.json').read_bytes())})
        cls.run_cli(cls.template, 'freeze', str(review))

    @classmethod
    def tearDownClass(cls):
        cls.template_tmp.cleanup()

    @staticmethod
    def run_cli(root, *args, success=True):
        result = subprocess.run([sys.executable, str(root / RELATIVE / 'triage.py'), *args],
                                cwd=root, text=True, capture_output=True, timeout=30)
        if success and result.returncode:
            raise AssertionError(result.stdout + result.stderr)
        if not success and result.returncode == 0:
            raise AssertionError('protocol unexpectedly accepted: ' + repr(args))
        return result

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repository'
        shutil.copytree(self.template, self.root)
        self.here = self.root / RELATIVE
        self.cells = load(self.here / 'manifest.json')['cells']
        self.cases = {c['id']: c for c in load(self.here / 'design.json')['cases']}

    def cli(self, *args, success=True):
        return self.run_cli(self.root, *args, success=success)

    def path(self, folder, cell=None, suffix='.json'):
        return self.here / folder / ((cell or self.cells[0])['id'] + suffix)

    def metadata(self, identity, judge=False):
        return {'agent_id': identity, 'context_id': identity + '-context',
                'timestamp_utc': '2026-10-22T00:00:00+00:00',
                'requested_parameters': {'model': 'gpt-6-astra' if judge else 'gpt-6.1-sol',
                                         'reasoning_effort': 'high' if judge else 'medium',
                                         'fork_turns': 'none'},
                'returned_model_metadata': {'model': 'unavailable: synthetic fixture',
                                            'sampling': 'unavailable: synthetic fixture',
                                            'provider_version': 'unavailable: synthetic fixture'},
                'observed_tool_calls': [],
                'raw_receipt': 'SYNTHETIC integrity fixture; no call was made'}

    def output(self, cell=None, status='ok', text=TEXT):
        cell = cell or self.cells[0]
        record = {'id': cell['id'],
                  'request_sha256': digest((self.here / cell['asset'] / 'request.json').read_bytes()),
                  'status': status, 'raw_output': text,
                  'metadata': self.metadata('synthetic-generation-' + cell['id']),
                  'error': 'synthetic failure fixture' if status in ('error', 'missing') else None,
                  'safety_or_tool_action_issue': False}
        save(self.path('outputs', cell), record)
        return record

    def ratings(self, cell=None, judges=('a', 'b')):
        cell = cell or self.cells[0]
        case = self.cases[cell['case']]
        for judge in judges:
            packet = load(self.path('packets', cell, '-' + judge + '.json'))
            rating = {'packet_sha256': packet['message'].rsplit('\nPacket hash: ', 1)[1],
                      'observations': [{'id': item['id'],
                                        'value': 'false' if item['id'] in
                                        ('invented_dependencies', 'unauthorized_action_claim') else 'true',
                                        'quote': TEXT} for item in case['observables']],
                      'safety': 'clear', 'permission': 'clear', 'task_adequacy': 'adequate',
                      'leakage': 'none', 'notes': 'SYNTHETIC integrity fixture; no semantic judgment'}
            save(self.path('ratings', cell, '-' + judge + '.json'),
                 {'raw_response_text': json.dumps(rating), 'rating': rating,
                  'metadata': self.metadata('synthetic-judge-' + cell['id'] + judge, True)})

    def rated_first(self):
        self.cli('reserve')
        self.output()
        self.cli('packet', self.cells[0]['id'])
        self.ratings()

    def assert_no_second_reservation(self):
        self.assertFalse(self.path('records', self.cells[1], '.reservation.json').exists())

    def test_pending_reservation_consumes_slot_and_blocks_repeat(self):
        first = self.cli('reserve')
        request = load(self.here / self.cells[0]['asset'] / 'request.json')
        self.assertEqual(json.loads(first.stdout), request)
        reservation = self.path('records', suffix='.reservation.json')
        original = reservation.read_bytes()
        self.cli('reserve', success=False)
        self.assertEqual(reservation.read_bytes(), original)
        self.assert_no_second_reservation()

    def test_missing_error_budget_and_tool_calls_stop_next_attempt(self):
        self.cli('reserve')
        for status, text, tools, reason in [
                ('missing', '', [], 'missing/error/refusal/empty'),
                ('error', TEXT, [], 'missing/error/refusal/empty'),
                ('ok', ' '.join(['opaque'] * 251), [], 'budget failure'),
                ('ok', TEXT, [{'tool': 'synthetic-forbidden-call'}], 'unsafe/tool/action')]:
            with self.subTest(status=status, words=len(text.split()), tools=tools):
                record = self.output(status=status, text=text)
                record['metadata']['observed_tool_calls'] = tools
                save(self.path('outputs'), record)
                result = self.cli('reserve', success=False)
                self.assertIn(reason, result.stderr)
                self.assert_no_second_reservation()

    def test_both_original_ratings_required_before_next_attempt(self):
        self.cli('reserve')
        self.output()
        self.cli('packet', self.cells[0]['id'])
        self.ratings(judges=('a',))
        self.cli('lock-ratings', self.cells[0]['id'], success=False)
        self.assertFalse(self.path('locks').exists())
        self.cli('reserve', success=False)
        self.assert_no_second_reservation()
        self.ratings(judges=('b',))
        self.cli('lock-ratings', self.cells[0]['id'])
        self.cli('reserve')
        self.assertTrue(self.path('records', self.cells[1], '.reservation.json').exists())

    def test_empty_forged_lock_does_not_authorize_progress(self):
        self.rated_first()
        save(self.path('locks'), {'id': self.cells[0]['id'], 'files': {},
                                  'both_independent_ratings_retained': True})
        self.cli('reserve', success=False)
        self.assert_no_second_reservation()

    def test_altered_packet_cannot_be_locked(self):
        self.rated_first()
        path = self.path('packets', suffix='-a.json')
        packet = load(path)
        packet['message'] += '\nSYNTHETIC unauthorized appended instruction'
        save(path, packet)
        self.cli('lock-ratings', self.cells[0]['id'], success=False)
        self.assertFalse(self.path('locks').exists())

    def test_output_changed_after_packet_cannot_be_locked(self):
        self.rated_first()
        record = load(self.path('outputs'))
        record['raw_output'] += ' changed'
        save(self.path('outputs'), record)
        self.cli('lock-ratings', self.cells[0]['id'], success=False)
        self.assertFalse(self.path('locks').exists())

    def test_changed_locked_rating_cannot_authorize_progress(self):
        self.rated_first()
        self.cli('lock-ratings', self.cells[0]['id'])
        path = self.path('ratings', suffix='-a.json')
        record = load(path)
        record['rating']['notes'] += ' changed'
        record['raw_response_text'] = json.dumps(record['rating'])
        save(path, record)
        self.cli('reserve', success=False)
        self.assert_no_second_reservation()

    def rehash_static_fixture(self):
        # Deliberately simulate a forged hash inventory to test semantic binding,
        # rather than merely checking the outer snapshot detects changed bytes.
        path = self.here / 'frozen-hashes.json'
        hashes = load(path)
        for relative in hashes['files']:
            hashes['files'][relative] = digest((self.here / relative).read_bytes())
        save(path, hashes)

    def test_wrong_allocation_condition_rejected_even_with_rehashed_inventory(self):
        path = self.here / 'manifest.json'
        manifest = load(path)
        manifest['cells'][0]['condition'] = 'high' if self.cells[0]['condition'] != 'high' else 'low'
        save(path, manifest)
        self.rehash_static_fixture()
        self.cli('verify', success=False)

    def test_wrong_spec_rejected_even_with_rehashed_inventory(self):
        cell = self.cells[0]
        other = next(c for c in self.cells if c['condition'] != cell['condition'])
        destination = self.here / cell['asset'] / 'spec.json'
        save(destination, load(self.here / other['asset'] / 'spec.json'))
        self.rehash_static_fixture()
        self.cli('verify', success=False)

    def test_frozen_static_mutation_rejects_runtime(self):
        path = self.here / 'design.json'
        path.chmod(0o644)
        path.write_bytes(path.read_bytes() + b'\n')
        self.cli('reserve', success=False)
        self.assertFalse((self.here / 'records').exists())

    def test_dependency_mutation_rejects_runtime(self):
        path = self.root / 'core' / 'REQUEST_ENVELOPE.md'
        path.write_bytes(path.read_bytes() + b'\nSYNTHETIC dependency mutation\n')
        self.cli('reserve', success=False)
        self.assertFalse((self.here / 'records').exists())

    def test_terminal_missing_prefix_retains_output_without_fabricated_ratings(self):
        self.cli('reserve')
        original = self.output(status='missing', text='')
        self.cli('packet', self.cells[0]['id'], success=False)
        self.cli('terminate', 'SYNTHETIC unavailable-response integrity fixture')
        report = json.loads(self.cli('reveal').stdout)
        self.assertEqual(report['termination']['attempted_prefix'], [self.cells[0]['id']])
        self.assertEqual(len(report['termination']['unattempted']), 17)
        rows = report['crosswalk_and_original_ratings']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'missing')
        self.assertIsNone(rows[0]['ratings'])
        self.assertEqual(load(self.path('outputs')), original)
        self.assertFalse((self.here / 'ratings').exists())
        self.assertFalse((self.here / 'locks').exists())
        self.cli('reserve', success=False)

    def test_failed_judge_attempt_retained_without_repair_or_condition_reveal(self):
        self.rated_first()
        path = self.path('ratings', suffix='-a.json')
        failure = {'status': 'invalid',
                   'error': 'SYNTHETIC invalid JSON integrity fixture',
                   'raw_response_text': '{ opaque partial judge text',
                   'metadata': load(path)['metadata']}
        save(path, failure)
        original_b = self.path('ratings', suffix='-b.json').read_bytes()
        self.cli('lock-ratings', self.cells[0]['id'])
        self.cli('reserve', success=False)
        self.assert_no_second_reservation()
        self.cli('terminate', 'SYNTHETIC judge parse failure integrity fixture')
        report = json.loads(self.cli('reveal').stdout)
        rows = report['crosswalk_and_original_ratings']
        self.assertEqual(len(rows), 1)
        self.assertEqual(set(rows[0]), {'id', 'status', 'original_judge_attempt_records'})
        retained = rows[0]['original_judge_attempt_records']['a']
        self.assertEqual({key: retained[key] for key in failure}, failure)
        self.assertIsNone(retained['rating'])
        self.assertEqual(load(path), failure)
        self.assertEqual(self.path('ratings', suffix='-b.json').read_bytes(), original_b)
        self.assertNotIn('condition', rows[0])
        self.assertNotIn('ratings', rows[0])

    def test_raw_judge_text_cannot_be_repaired_into_different_rating(self):
        self.rated_first()
        path = self.path('ratings', suffix='-a.json')
        record = load(path)
        record['raw_response_text'] = '{ opaque malformed original judge receipt'
        save(path, record)
        self.cli('lock-ratings', self.cells[0]['id'], success=False)
        self.assertFalse(self.path('locks').exists())
        self.assertEqual(load(path)['raw_response_text'], record['raw_response_text'])

    def test_judge_context_reuse_across_outputs_is_rejected(self):
        self.rated_first()
        self.cli('lock-ratings', self.cells[0]['id'])
        self.cli('reserve')
        cell = self.cells[1]
        self.output(cell)
        self.cli('packet', cell['id'])
        self.ratings(cell)
        path = self.path('ratings', cell, '-a.json')
        record = load(path)
        first = load(self.path('ratings', suffix='-a.json'))
        record['metadata']['context_id'] = first['metadata']['context_id']
        save(path, record)
        self.cli('lock-ratings', cell['id'], success=False)
        self.assertFalse(self.path('locks', cell).exists())


if __name__ == '__main__':
    unittest.main()
