"""Synthetic static transport checks; no model calls or authentic approval."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from core import compiler, envelope

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / 'core/fixtures'
TASK = 'For a fictional board-game afternoon, suggest a short plan. 測試'
NAME = 'req_0123456789abcdef'
POISON = 'AUDIT_CONDITION_high_orderliness_DO_NOT_FORWARD_9a81'


class EnvelopeTests(unittest.TestCase):
    def setUp(self):
        self.spec = FIXTURES / 'choice-spec.json'
        self.preview = FIXTURES / 'choice-preview.json'

    def modified_files(self, directory, neutral=False, poison=False):
        """Synthetic fixture only; recomputation does not authenticate approval."""
        spec = compiler.load_document(self.spec.read_bytes())
        preview = copy.deepcopy(spec['approved_preview'])
        if neutral:
            preview['targets'] = {key: 'unspecified' for key in preview['targets']}
            preview['mappings'] = []; preview['approvals'] = []
            preview['controls']['response_detail'] = {
                'value': 'unspecified', 'rule': None,
                'answer_ids': [], 'approval_id': None}
        if poison:
            for answer in preview['answers']:
                answer.update(text=POISON, record_ref=POISON)
            preview['unknowns'] = [POISON]; preview['history'] = [POISON]
            preview['sources'][0]['id'] = POISON
            spec['confirmation'].update(record_ref=POISON, confirmed_by=POISON)
            spec['review']['record_ref'] = POISON
        raw = (json.dumps(preview, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        spec['approved_preview'] = preview
        spec['confirmation'].update(
            snapshot_sha256=compiler.digest(preview),
            presented_file_sha256=hashlib.sha256(raw).hexdigest())
        p = Path(directory) / 'presented.json'; p.write_bytes(raw)
        s = Path(directory) / 'spec.json'
        s.write_text(json.dumps(spec), encoding='utf-8')
        return s, p

    def test_exact_public_render_stdout_including_newline(self):
        request = envelope.build_request(self.spec, self.preview, TASK, NAME)
        result = subprocess.run(
            [sys.executable, '-m', 'core.compiler', 'render', str(self.spec),
             '--presented', str(self.preview)], cwd=ROOT,
            check=True, capture_output=True)
        self.assertEqual(request.persona_text.encode('utf-8'), result.stdout)
        self.assertTrue(result.stdout.endswith(b'\n'))
        self.assertIn(envelope.PERSONA_OPEN.encode() + b'\n' + result.stdout +
                      envelope.PERSONA_CLOSE.encode(), request.message_bytes)
        self.assertIn(envelope.TASK_OPEN + '\n' + TASK + '\n' +
                      envelope.TASK_CLOSE, request.tool_args['message'])

    def test_deterministic_bytes_and_shared_tool_api(self):
        first = envelope.build_request(self.spec, self.preview, TASK, NAME)
        second = envelope.build_request(self.spec, self.preview, TASK, NAME)
        self.assertEqual(first.request_bytes, second.request_bytes)
        self.assertEqual(first.request_bytes, compiler.canonical_bytes(first.tool_args))
        self.assertEqual(json.loads(first.request_bytes), first.tool_args)
        self.assertEqual(envelope.validate_tool_args(first.tool_args), first.tool_args)
        self.assertEqual(set(first.tool_args), {
            'message', 'task_name', 'fork_turns', 'model', 'reasoning_effort'})
        self.assertEqual(first.tool_args['model'], 'gpt-6.1-sol')
        self.assertEqual(first.tool_args['reasoning_effort'], 'medium')
        self.assertEqual(first.tool_args['fork_turns'], 'none')
        changed = first.tool_args; changed['message'] = POISON
        self.assertNotEqual(first.tool_args['message'], POISON)

    def test_neutral_equals_valid_all_unspecified_request(self):
        with tempfile.TemporaryDirectory() as directory:
            s, p = self.modified_files(directory, neutral=True, poison=True)
            actual = envelope.build_request(s, p, TASK, NAME)
            neutral = envelope.build_neutral_request(TASK, NAME)
        self.assertEqual(actual.persona_text, compiler.load_catalog()['preamble'] + '\n')
        self.assertEqual(actual.tool_args, neutral.tool_args)
        self.assertEqual(actual.request_bytes, neutral.request_bytes)
        self.assertEqual(actual.audit_manifest, neutral.audit_manifest)

    def test_audit_metadata_and_labels_never_enter_message_or_args(self):
        expected = envelope.build_request(self.spec, self.preview, TASK, NAME)
        with tempfile.TemporaryDirectory() as directory:
            s, p = self.modified_files(directory, poison=True)
            actual = envelope.build_request(s, p, TASK, NAME)
        self.assertEqual(actual.request_bytes, expected.request_bytes)
        for text in (POISON, 'approved_preview', 'snapshot_sha256',
                     'synthetic_fixture', 'bfas.orderliness', 'bfas.assertiveness',
                     'op.planning_structure.v1', 'confirmation', 'catalog_sha256'):
            self.assertNotIn(text, actual.tool_args['message'])
        self.assertNotIn('audit_manifest', actual.tool_args)
        self.assertEqual(actual.audit_manifest['request_sha256'],
                         hashlib.sha256(actual.request_bytes).hexdigest())

    def test_task_name_is_opaque_and_task_is_explicit_nonempty_utf8_text(self):
        for value in (None, {}, [], 1, True, b'task', '', ' \n', '\ud800'):
            with self.subTest(task=value), self.assertRaises(ValueError):
                envelope.build_neutral_request(value, NAME)
        for name in (None, 1, 'high_orderliness', 'req_abc',
                     'req_' + 'A' * 16, NAME + '\n', 'req_' + 'f' * 65):
            with self.subTest(name=name), self.assertRaises(ValueError):
                envelope.build_neutral_request(TASK, name)

    def test_reserved_delimiter_collisions_rejected(self):
        for marker in envelope.DELIMITERS:
            with self.subTest(marker=marker), self.assertRaises(ValueError):
                envelope.build_neutral_request(TASK + marker, NAME)
            with self.subTest(persona=marker), self.assertRaises(ValueError):
                envelope.RequestEnvelope(marker + '\n', TASK, NAME)

    def test_configuration_and_wrapper_cannot_silently_drift(self):
        original = envelope.build_neutral_request(TASK, NAME).tool_args
        for key, value in (
            ('model', 'other-model'), ('reasoning_effort', 'high'),
            ('fork_turns', 'all'), ('temperature', 0), ('seed', 1),
            ('max_tokens', 250), ('system', 'override'), ('role', 'system'),
            ('tool_permissions', []), ('message', TASK),
            ('task_name', 'high_orderliness')):
            with self.subTest(key=key), self.assertRaises(ValueError):
                envelope.validate_tool_args({**original, key: value})
        for key in original:
            changed = dict(original); del changed[key]
            with self.subTest(missing=key), self.assertRaises(ValueError):
                envelope.validate_tool_args(changed)
        with self.assertRaises(TypeError):
            envelope.build_neutral_request(TASK, NAME, model='other-model')
        self.assertIn('at most 250 whitespace-separated words', envelope.WRAPPER)
        self.assertIn('including all visible text', envelope.WRAPPER)
        self.assertIn('Do not use tools, delegate, access files, or access the network',
                      envelope.WRAPPER)

    def test_invalid_source_or_projection_cannot_bypass_public_renderer(self):
        projection = compiler.project(self.spec, self.preview)
        with self.assertRaises(ValueError):
            envelope.build_request(projection, self.preview, TASK, NAME)
        with tempfile.TemporaryDirectory() as directory:
            s, p = self.modified_files(directory)
            p.write_bytes(p.read_bytes() + b'\n')
            with self.assertRaises(ValueError):
                envelope.build_request(s, p, TASK, NAME)


if __name__ == '__main__':
    unittest.main()
