# Optional structural validation

The Persona Design v0.2 protocol runs from Markdown. This small Python 3 standard-library script is an optional verification aid, not an application, runtime, questionnaire engine, persona generator, or backend. Manual review and explicit human confirmation remain required.

From the repository root:

```sh
python validation/validate_spec.py preview validation/fixtures/all-unspecified-preview.md
python validation/validate_spec.py spec validation/fixtures/mixed-spec.md --preview validation/fixtures/mixed-preview.md
python validation/validate_spec.py spec validation/fixtures/mixed-spec.md --preview validation/fixtures/mixed-preview.md --reload validation/fixtures/mixed-spec.md
python -m unittest discover -s validation -p 'test_*.py' -v
```

Exit status 0 means the represented structure passed; 1 means invalid input or a failed comparison. The preview command also prints a digest. These fixture commands exercise only synthetic records. Their confirmation metadata is fictional and does not authorize any actual design.

## Record format and comparison

Each input is Markdown containing exactly one `json` fence. See [the fillable template](../persona-design-v0.2/spec-template.md) and [synthetic fixtures](fixtures/). The template is deliberately incomplete until scenario, provenance, and answer records are filled. The fixtures are hand-authored protocol examples, not generated-agent outputs, observed trials, reusable persona presets, or a runtime inventory.

A preview uses `schema_version: persona-design-v0.2`, `kind: preview`, and revision `r1`, `r2`, etc. Targets contain exactly the registry's ten `bfas.*` IDs with `low`, `middle`, `high`, or `unspecified`. These are requested qualitative design directions, never measured scores. Every requested target requires exactly one mapping with a resolvable answer, project mapping source, mapping ID, behavior rule, and boundary. An unspecified target has no mapping. An all-unspecified preview is valid and imposes no aspect behavior; it never silently selects middle.

Source records name `src.deyoung2007`, `src.ipip.bfas-table`, and `src.project-mapping-v0.2`. The first two support human vocabulary only; agent mappings must cite the project's hypothesis source. The script checks identifiers and nonempty citation text, not external sources' contents or whether a citation was faithfully transcribed.

The final wrapper has exactly `kind: spec`, `approved_preview` (the complete frozen preview), `approval`, and `review: Pass`. Approval has `status: confirmed`, matching `revision`, `digest`, `confirmed_by`, and `record_ref`. Keep `digest: null` for Markdown-only work without a computed hash. If a digest is supplied, it must match SHA-256 over UTF-8 JSON serialized with recursively sorted object keys, compact separators, `ensure_ascii=False`, and no added newline, prefixed `sha256:`. List order and all field values remain significant; Markdown prose and JSON indentation are outside this comparison.

The spec command requires the separately supplied approved preview and compares its complete JSON payload with the nested preview even when the digest is null. An optional `--reload` checks the reloaded spec against the preview and original spec, including its metadata. This detects changed content, but cannot authenticate the supplied original or who approved it. Never reconstruct an approval record or invent a hash to make validation pass.

Conflicts retain at least two candidate records and their answer references, including after withdrawal to unspecified. Same-level conflicts with distinct answer evidence remain representable; exact duplicate candidate records are rejected. They may concern a `bfas.*` aspect or `workflow_controls.<key>`; workflow candidates contain behavioral text. Finalization requires a resolution and a resolvable resolution-answer record. The script cannot interpret whether that answer actually resolves the conflict; human review must check it.

## Scope and limits

The baseline checker requires fictional, low-stakes, ephemeral, accuracy, explicit uncertainty, privacy, safety, tool-permission, and human-final-judgment invariants. Boundary posture uses the template's fixed sentence. This deliberately narrow baseline accepts only `panel_authorized: false` and `persistence_authorized: false`; a separately authorized optional workflow needs its own review and is outside this checker's scope. It does not reject those workflows as prohibited by the project.

The five non-claim tokens are `psychometric_validity`, `real_person_traits`, `behavioral_validation`, `provider_reliability`, and `real_user_readiness`. Evidence kind is only `not_run` or `synthetic_protocol_fixture`, with `behavioral_validation: false`. Actual requested observations belong in the separate [behavior protocol](BEHAVIOR_PROTOCOL.md), with run context, outputs, and limitations; they are not fabricated inside a passing fixture.

A digest proves only a content relationship. Names, confirmation references, and `Pass` are structural records, not authenticated human consent. The script cannot verify user intent, semantic truth, safety of arbitrary prose, faithful source interpretation, whether an unrecorded conflict exists, implementation compliance, or behavioral reliability. Review the surrounding Markdown as well as the JSON. Structural tests are not behavioral trials and support no psychometric, general-reliability, cross-provider, or readiness claim.

The existing [Persona Pack manual checklist](persona-pack-v0.1-manual-validator-checklist.md) remains a separate optional handoff review.
