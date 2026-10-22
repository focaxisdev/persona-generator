# Confirmed single-agent core — unreleased candidate

Canonical route: [README](../README.md) → [Quickstart](../docs/QUICKSTART.md) → this contract. Configure desired behavior for one fictional, low-stakes, ephemeral advisory agent, then stop when its bounded task is complete. No panel or Persona Pack is required.

## Version and supported surface

| Identifier | Meaning |
| --- | --- |
| v0.2 candidate | Unreleased package increment, not a release announcement |
| `persona-core-v1` | New JSON preview/spec contract checked by [compiler.py](compiler.py) |
| `persona-core-catalog-v1` | Exact trusted [catalog](catalog-v1.json), pinned by SHA-256 |
| `persona-core-projection-v1` | Typed effective projection produced after spec validation |
| `op.planning_structure.v1` | Untested planning-format analogue, associated with Orderliness vocabulary |
| `op.advisory_initiative.v1` | Untested advisory-initiative analogue, associated with Assertiveness vocabulary |

These names are separate from historical `map.*.v1`/`map.*.v2`. No migration or evidence is inherited. [COVERAGE](COVERAGE.md) owns the ten-aspect vocabulary, eight omitted operational settings, triggers, non-triggers, exclusions and confounds; [SOURCES](SOURCES.md) owns research provenance and access limitations. Neither source research nor an operation name establishes human traits in a model.

The two operations offer `low`, `middle`, `high`, or `unspecified` design targets, never human scores. All eight unsupported aspects must remain unspecified. The independent `response_detail` workflow control exposes its exact approved catalog `rule` in the preview and offers `concise`, `standard`, `detailed`, or `unspecified`; it is not a personality aspect or quality setting. Every setting preserves required work, accuracy, calibrated uncertainty, privacy, safety, task constraints, permissions and human choice.

The exact field/digest definitions and public API are in [CONTRACT](CONTRACT.md); the workflow below explains their human use.

## Protocol: real intent to exact confirmed artifact

1. Collect guided choices or short answers about desired agent behavior. Record answer IDs and origin honestly: `owner` for actual owner input; `synthetic_fixture` for handwritten demonstration. Keep private record references private. Do not infer the owner's personality or convert free text directly into execution instructions.
2. Start all ten targets and the response-detail control unspecified. Propose only supported catalog candidates where the owner asks for them. Show each exact version, anchor, trigger, rule and boundary, the source/coverage rationale, exclusions and unknowns. Resolve contradictions through an actual selection or withdrawal; never average them or silently select the latest phrase.
3. Obtain explicit approval for the exact candidate settings and literal rules. `approvals` bind answer provenance and a digest of each candidate; `mappings` and the optional control reference those approvals. These are structural records of an action, not a mechanism that performs consent.
4. Present the complete preview file, including its revision, catalog identity/hash, scope, answers, all targets, mappings, approvals, controls, conflicts, unknowns, sources, history and untested evidence status. Let the owner inspect the exact content. Stop for actual confirmation of that complete revision; partial agreement does not confirm the full artifact.
5. Create a spec embedding the unchanged `approved_preview`. Record confirmation revision, canonical snapshot digest, SHA-256 of the exact presented file bytes, actual record reference, confirmer and origin, plus manual review status/reference. Verify the separate presented file as well as the embedded snapshot. The compiler requires structural `confirmed` and review `Pass`; it cannot authenticate the person, interpret actual consent, or certify semantic safety.
6. Validate the exact spec with the separately preserved presented preview locally. Keep projection JSON as audit data: it contains labels and provenance and is not the model input. Use only exact `render` stdout as the persona payload in the fixed [request envelope](REQUEST_ENVELOPE.md), with the bounded task as a separate component. Spec, preview, trace and aspect/condition labels never go to the evaluated model.
7. A behavior edit creates a new preview revision and invalidates prior confirmation. Preserve the old revision as history; obtain new candidate approvals where changed and a new full-preview confirmation. A fresh session must load the exact confirmed spec/preview, validate and rederive the projection rather than reconstructing intent from conversation memory. Missing or mismatched content blocks use.

## Executable boundary

The compiler does not call a model or interview an owner. It validates a manually prepared contract; it does not implement a web UI, sign identities or infer settings from text. Unknown fields and unsupported/custom rules are rejected. It checks the trusted catalog and pinned historical vocabulary dependencies, so modifying a dependency is a versioned contract change, never a silent refresh. [SOURCES](SOURCES.md) and [COVERAGE](COVERAGE.md) provide current explanatory context; they are not free-form executable rule sources.

`compile_spec` emits the invariant catalog preamble, active approved operations in deterministic ID order, and an explicitly approved response-detail control if present. Unspecified emits no preference. The public `render`/`render_text` API takes spec and presented-preview paths and validates them before formatting. Its private projection formatter accepts only matching typed instructions and trusted catalog templates; a typed projection alone is not proof of approval. Answers, source excerpts, unknowns, rationale, history, conflict candidates and approval record text remain inert, even if they contain imperative language. The renderer adds no unapproved rules, guesses or free-text instructions.

Ordinary use, reuse and future behavioral evaluation use the same validating renderer and request-envelope builder. The supported prospective transport is `collaboration.spawn_agent` with a new `fork_turns="none"` context and an exact initial message. The tool does not expose separate system/developer roles, sampling parameters or a tools-off sandbox; inherited host instructions and available tools remain a limitation. The fixed wrapper prohibits tool use, and any observed use stops dependent evaluation. See [REQUEST_ENVELOPE](REQUEST_ENVELOPE.md) for exact configuration and boundaries. A separately handwritten prompt or projection JSON would test a different intervention. Structural receipt validity is not proof of authentic approval or successful behavior.

## Runnable synthetic demonstration

From the repository root, use Python 3 with only the standard library:

```bash
python -m core.compiler validate-preview core/fixtures/choice-preview.json
python -m core.compiler validate core/fixtures/choice-spec.json --presented core/fixtures/choice-preview.json
python -m core.compiler project core/fixtures/choice-spec.json --presented core/fixtures/choice-preview.json
python -m core.compiler render core/fixtures/choice-spec.json --presented core/fixtures/choice-preview.json
python -m core.compiler validate core/fixtures/short-answer-spec.json --presented core/fixtures/short-answer-preview.json
python -m unittest core.test_compiler -v
```

[Choice preview](fixtures/choice-preview.json) / [spec](fixtures/choice-spec.json) and [short-answer preview](fixtures/short-answer-preview.json) / [spec](fixtures/short-answer-spec.json) are **handwritten synthetic fixtures**, not transcripts, genuine owner approval or model observations. Do not relabel them `owner`. Validation/project/render do not contact a model, activate a persona or execute advisory suggestions. Projection output reports `validation_status: structural_only` and its confirmation origin.

Validation succeeds only for this new core contract. It is not the historical validator and makes no frozen mapping-v2 compatibility claim. Changing preview whitespace alters its presented-file byte digest even when canonical JSON content is unchanged; preserve the exact presented file. Duplicated keys, unsupported JSON values, stale versions, missing approvals, changed source dependencies and stale confirmations must fail closed.

## Evidence and remaining work

The initial integration checks are recorded in [VERIFICATION](VERIFICATION.md), with their separate [independent review](INDEPENDENT_REVIEW.md). The envelope/triage follow-up has its own [verification](../evaluation/core-triage-v1/VERIFICATION.md) and [independent review](../evaluation/core-triage-v1/INDEPENDENT_REVIEW.md); historical records retain their original file identities.

New core behavior and authentic owner E2E are **NOT RUN**. Compiler tests establish only their actual checked software properties. [OWNER_TEST_PROTOCOL](OWNER_TEST_PROTOCOL.md) describes private authentic confirmation/change/reconfirmation/reuse for both interview modes. [EVIDENCE_PLAN](EVIDENCE_PLAN.md) describes prospective, bounded operation probes using this exact renderer. Neither plan authorizes model collection or substitutes for the unchanged historical 400-response gate. Release acceptance remains pending; see [claims](../docs/CLAIMS_MATRIX.md) and [release acceptance](../docs/RELEASE_ACCEPTANCE.md).
