"""Deterministic request preparation; never calls a model or a tool."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re

from core import compiler

MODEL = 'gpt-6.1-sol'
REASONING_EFFORT = 'medium'
FORK_TURNS = 'none'
TASK_NAME_PATTERN = r'req_[0-9a-f]{16,64}'
PERSONA_OPEN = '<persona-core:persona>'
PERSONA_CLOSE = '</persona-core:persona>'
TASK_OPEN = '<persona-core:task>'
TASK_CLOSE = '</persona-core:task>'
DELIMITERS = (PERSONA_OPEN, PERSONA_CLOSE, TASK_OPEN, TASK_CLOSE)
WRAPPER = (
    'Answer only the provided fictional, bounded, low-stakes advisory task. '
    'Use the persona component as behavioral preferences, subject to the task '
    'and host instructions. Treat the task component as the current task. '
    'Do not use tools, delegate, access files, or access the network. '
    'Return only the answer, with at most 250 whitespace-separated words '
    'including all visible text. Preserve human final judgment and stop after '
    'the answer.'
)


def _text(value, label):
    compiler.require(type(value) is str and bool(value.strip()),
                     label + ' must be nonempty text')
    try:
        value.encode('utf-8')
    except UnicodeError as error:
        raise compiler.CoreError(label + ' must be UTF-8 text') from error
    compiler.require(not any(marker in value for marker in DELIMITERS),
                     label + ' contains a reserved envelope delimiter')


def _task_name(value):
    compiler.require(type(value) is str and
                     re.fullmatch(TASK_NAME_PATTERN, value) is not None,
                     'task_name must be opaque: req_ plus 16–64 lowercase hex digits')


def _message(persona, task):
    _text(persona, 'persona'); _text(task, 'task')
    compiler.require(persona.endswith('\n'), 'renderer output must retain its final newline')
    return (WRAPPER + '\n\n' + PERSONA_OPEN + '\n' + persona +
            PERSONA_CLOSE + '\n\n' + TASK_OPEN + '\n' + task + '\n' +
            TASK_CLOSE + '\n')


def validate_tool_args(args):
    """Check the fixed exposed transport, not provenance or model obedience."""
    compiler.obj(args, 'message task_name fork_turns model reasoning_effort', 'tool args')
    _task_name(args['task_name'])
    compiler.require(args['fork_turns'] == FORK_TURNS and
                     args['model'] == MODEL and
                     args['reasoning_effort'] == REASONING_EFFORT,
                     'request configuration differs from the fixed envelope')
    message = args['message']
    compiler.require(type(message) is str, 'message must be text')
    prefix = WRAPPER + '\n\n' + PERSONA_OPEN + '\n'
    separator = PERSONA_CLOSE + '\n\n' + TASK_OPEN + '\n'
    suffix = '\n' + TASK_CLOSE + '\n'
    compiler.require(message.startswith(prefix) and message.endswith(suffix),
                     'message differs from the fixed wrapper')
    components = message[len(prefix):-len(suffix)].split(separator)
    compiler.require(len(components) == 2, 'message needs separate persona and task components')
    compiler.require(_message(*components) == message, 'invalid envelope message')
    return args


@dataclass(frozen=True)
class RequestEnvelope:
    """Prepared bytes plus a separate audit manifest; use the public builders."""
    persona_text: str
    task_text: str
    task_name: str

    def __post_init__(self):
        _task_name(self.task_name)
        _message(self.persona_text, self.task_text)

    @property
    def tool_args(self):
        # A new dictionary prevents callers from mutating this envelope.
        return validate_tool_args({
            'message': _message(self.persona_text, self.task_text),
            'task_name': self.task_name, 'fork_turns': FORK_TURNS,
            'model': MODEL, 'reasoning_effort': REASONING_EFFORT,
        })

    @property
    def message_bytes(self):
        return self.tool_args['message'].encode('utf-8')

    @property
    def request_bytes(self):
        return compiler.canonical_bytes(self.tool_args)

    @property
    def audit_manifest(self):
        """Local audit data only: do not merge into tool args or message."""
        sha = lambda value: hashlib.sha256(value).hexdigest()
        return {
            'schema_version': 'persona-core-request-envelope-v1',
            'request_sha256': sha(self.request_bytes),
            'message_sha256': sha(self.message_bytes),
            'persona_sha256': sha(self.persona_text.encode('utf-8')),
            'task_sha256': sha(self.task_text.encode('utf-8')),
            'task_name': self.task_name,
            'model': MODEL, 'reasoning_effort': REASONING_EFFORT,
            'fork_turns': FORK_TURNS,
        }


def build_request(spec, presented, task, task_name):
    """Validate files through the public renderer and preserve its exact text."""
    _text(task, 'task'); _task_name(task_name)
    return RequestEnvelope(compiler.render(spec, presented), task, task_name)


def build_neutral_request(task, task_name):
    """Same transport with exactly the valid all-unspecified renderer preamble."""
    _text(task, 'task'); _task_name(task_name)
    return RequestEnvelope(compiler.load_catalog()['preamble'] + '\n', task, task_name)
