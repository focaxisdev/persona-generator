# Canonical request envelope — unreleased candidate

[envelope.py](envelope.py) prepares a single request for the exposed
`collaboration.spawn_agent` surface. It uses only the Python standard library and
makes no model or tool calls. Ordinary adapters and prospective evaluation must
use the same builders; independently handwritten prompt packets are outside this
contract.

From the repository root, this runnable example prepares a request from the
existing handwritten synthetic fixtures. It demonstrates preparation only,
without authentic owner approval or model execution:

```sh
python - <<'PY'
from core.envelope import build_request

request = build_request(
    'core/fixtures/choice-spec.json',
    'core/fixtures/choice-preview.json',
    'For a fictional board-game afternoon, suggest a short setup plan. '
    'Keep suggestions advisory and leave the final choice to the human host.',
    'req_0123456789abcdef',
)
args = request.tool_args          # Reviewable spawn_agent arguments; no call.
payload = request.request_bytes   # Deterministic canonical UTF-8 JSON of args.
audit = request.audit_manifest    # Separate local audit data; never send as args.
print(payload.decode('utf-8'))
PY
```

`build_request(spec, presented, task, task_name)` calls the public validating
`compiler.render(spec, presented)` API. Its persona component is exactly the
renderer's output, including its final newline, equivalent to successful render
CLI stdout. Spec, preview, projection JSON, provenance, answers, trace text,
aspect IDs, anchor labels, condition labels and audit manifests are not appended
to the message. Only approved rendered instructions enter that component.

The fixed wrapper and the separately delimited explicit current task follow the
same construction for every request. Task text must be nonempty UTF-8 text.
Reserved persona/task opening and closing delimiters are rejected inside either
component, preventing ambiguous component boundaries. These structural checks
do not semantically inspect task instructions or guarantee injection resistance.
The wrapper requests fictional, bounded, low-stakes advisory work; forbids tools,
delegation, file and network access; requests only the answer; and caps all
visible text at 250 whitespace-separated words. The wrapper is a model
instruction, not an enforced sandbox or token cap.

The neutral builder uses exactly `compiler.load_catalog()['preamble'] + '\n'`.
With the same task and task name its entire tool argument object and bytes equal
those from a valid all-unspecified spec. Neutral does not mean removal of the
invariant boundary, and an unspecified setting does not imply a middle anchor.
`build_neutral_request(task, task_name)` is only a static audit/control
equivalence route. It is not a scheduled neutral experiment cell or an ordinary
product path. Ordinary product requests must use `build_request` with the full
confirmed spec and exact presented preview, including when every setting is
unspecified.

The exact argument keys are `message`, `task_name`, `fork_turns`, `model` and
`reasoning_effort`. Configuration is fixed to `fork_turns='none'`,
`model='gpt-6.1-sol'`, and `reasoning_effort='medium'`. Task names must match
`req_[0-9a-f]{16,64}`; choose opaque IDs and keep semantic condition/task labels
in a separate audit manifest. The transport has no role/system-message,
temperature, seed, max-token or tool-permission controls. Do not invent those
controls or claim they were set. `validate_tool_args` checks exact transport
keys, configuration and wrapper structure, but does not authenticate the origin
of a manually supplied persona component. Constructing `RequestEnvelope`
directly likewise provides structural sanity checks, not provenance proof.
Supported consumers use `build_request` and retain their confirmed spec and
exact presented file. A frozen-request verifier must rebuild the request from
those actual source files and compare its bytes; transport validation alone
does not establish that the public renderer produced a supplied message.

`fork_turns='none'` omits parent conversation turns. Host instructions, available
tools, and the shared workspace remain available. This is not full isolation.
An authorized executor must separately review whether execution is permitted;
preparation, hashes and static tests do not authorize a model run or establish
model adherence, authentic owner approval, safety, or behavioral validity.

`RequestEnvelope` exposes `persona_text`, `task_text`, `task_name`, `tool_args`,
`message_bytes`, `request_bytes`, and `audit_manifest`. Every `tool_args` or
manifest access returns a fresh dictionary. Manifest fields contain request,
message, persona and task SHA-256 hashes plus the fixed exposed configuration;
they remain outside model arguments. Callers may retain source identity and
condition labels separately without adding them to the request. Preserve
canonical request bytes for auditing the actual transport, rather than treating
a reconstructed equivalent prompt as identical.

Run static synthetic tests with `python -m unittest core.test_envelope -v`.
No model behavior is observed by those tests.
