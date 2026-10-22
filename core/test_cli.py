"""Local subprocess checks only; synthetic fixtures, no model or paid API calls."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from core import compiler

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / 'fixtures'


class CLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'core.compiler', *map(str, args)],
                              cwd=ROOT, text=True, capture_output=True)

    def test_actual_validate_project_and_render_commands(self):
        for name in ('choice', 'short-answer'):
            preview = FIXTURES / f'{name}-preview.json'
            spec = FIXTURES / f'{name}-spec.json'
            with self.subTest(name=name):
                self.assertEqual(self.run_cli('validate-preview', preview).returncode, 0)
                self.assertEqual(self.run_cli('validate', spec, '--presented', preview).returncode, 0)
                projected = self.run_cli('project', spec, '--presented', preview)
                self.assertEqual(projected.returncode, 0, projected.stderr)
                projection = json.loads(projected.stdout)
                self.assertEqual(projection, compiler.project(spec, preview))
                rendered = self.run_cli('render', spec, '--presented', preview)
                self.assertEqual(rendered.returncode, 0, rendered.stderr)
                self.assertEqual(rendered.stdout, compiler.render(spec, preview))
                self.assertEqual(projection['confirmation_origin'], 'synthetic_fixture')
                self.assertEqual(projection['validation_status'], 'structural_only')

    def test_missing_presented_argument_fails(self):
        result = self.run_cli('render', FIXTURES / 'choice-spec.json')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')

    def test_whitespace_only_presented_byte_change_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            preview = Path(directory) / 'same-value.json'
            preview.write_bytes((FIXTURES / 'choice-preview.json').read_bytes() + b'\n')
            for command in ('validate', 'project', 'render'):
                with self.subTest(command=command):
                    result = self.run_cli(command, FIXTURES / 'choice-spec.json', '--presented', preview)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, '')

    def test_unknown_version_and_malformed_payload_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bad.json'
            for payload in ('{"schema_version":"persona-design-v0.2"}',
                            '{"schema_version":NaN}', '{"x":1,"x":2}'):
                path.write_text(payload)
                with self.subTest(payload=payload):
                    result = self.run_cli('render', path, '--presented', FIXTURES / 'choice-preview.json')
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
