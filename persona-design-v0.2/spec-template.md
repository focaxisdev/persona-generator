# Persona Design v0.2 spec template

Use [protocol.md](protocol.md) and [interview.md](interview.md). The JSON record below is the authoritative design payload. This surrounding prose explains the format; do not add behavior-changing instructions outside the payload. Copy the template to a working document and replace placeholder text before previewing it. The template itself is not an approved or completed design.

The ten `targets` are qualitative **agent design requests**, not measurements of a human or an agent's personality. Keep all ten keys, including unspecified values. `unspecified` means no aspect instruction; it never means middle. Workflow controls remain separate. Their boundary posture is mandatory; their other empty settings below are expressly unspecified until the user supplies instructions.

## Preview record

This empty starting record intentionally has no mappings or answer evidence. A complete preview needs a real fictional scenario, the required source records, and an explicit user answer supporting its mandatory boundary posture. Record further user answers only as needed for requested design settings. An unspecified target needs no invented answer or behavior rule.

```json
{
  "schema_version": "persona-design-v0.2",
  "kind": "preview",
  "revision": "r1",
  "scenario": "REPLACE: fictional low-stakes scenario, role, intended artifact, allowed use, exclusions, and human reviewer",
  "answers": [],
  "sources": [],
  "targets": {
    "bfas.volatility": "unspecified",
    "bfas.withdrawal": "unspecified",
    "bfas.compassion": "unspecified",
    "bfas.politeness": "unspecified",
    "bfas.industriousness": "unspecified",
    "bfas.orderliness": "unspecified",
    "bfas.enthusiasm": "unspecified",
    "bfas.assertiveness": "unspecified",
    "bfas.intellect": "unspecified",
    "bfas.openness": "unspecified"
  },
  "workflow_controls": {
    "decision_tempo": "unspecified",
    "evidence_posture": "unspecified",
    "uncertainty_posture": "unspecified",
    "communication_posture": "unspecified",
    "creative_posture": "unspecified",
    "collaboration_posture": "unspecified",
    "time_horizon": "unspecified",
    "boundary_posture": "Preserve accuracy, explicit uncertainty, privacy, safety, tool permissions, and human final judgment."
  },
  "mappings": [],
  "conflicts": [],
  "unknowns": [
    "All ten aspect targets are intentionally unspecified until explicitly selected or clarified.",
    "No behavioral test has been run."
  ],
  "non_claims": [
    "behavioral_validation",
    "provider_reliability",
    "psychometric_validity",
    "real_person_traits",
    "real_user_readiness"
  ],
  "boundaries": {
    "fictional": true,
    "low_stakes": true,
    "ephemeral": true,
    "accuracy": true,
    "explicit_uncertainty": true,
    "privacy": true,
    "safety": true,
    "tool_permissions": true,
    "human_final_judgment": true,
    "panel_authorized": false,
    "persistence_authorized": false
  },
  "evidence": {
    "kind": "not_run",
    "behavioral_validation": false
  }
}
```

## Field rules and traceability

- `revision` identifies one exact frozen preview, such as `r1`, then `r2`. Any payload change creates a new revision and clears approval. Never reuse a revision for different payloads.
- `scenario` includes the fictional role, artifact, permitted scope, prohibitions, human reviewer, and stop condition. All runtime guidance, tensions and calibration instructions must live in approved payload fields, such as the relevant workflow control or mapping boundary.
- `answers` contains records with unique `id` and faithful `text`. Store only the minimum relevant user-provided design evidence. Do not put inferred traits or invented approvals here. A resolution or explicit withdrawal is itself an answer with its own ID.
- `sources` contains unique `id` and `citation` records from [sources.md](sources.md). Preserve the registry's exact source IDs and scope. Include `src.deyoung2007`, `src.ipip.bfas-table`, and `src.project-mapping-v0.2`: the first two support human construct vocabulary and the last identifies the proposed translation. A citation is not a behavioral observation.
- `targets` contains exactly the ten `bfas.*` keys shown above. Allowed values are `low`, `middle`, `high`, and `unspecified`; no other spelling, score, vector, domain aggregate, or midpoint fallback is allowed.
- `workflow_controls` contains exactly the eight keys shown above. Values are qualitative instructions or the explicit string `unspecified`. Include supporting answer IDs in concrete workflow instructions. Keep `boundary_posture` exactly as shown and retain an answer confirming it; it cannot be unspecified or contradicted by another control. Put additional scenario restrictions and the boundary answer reference in `scenario`. The other seven strings may include context, without adding BFAS targets.
- Every `mappings` record has `id`, `answer_id`, `source_id`, `aspect`, `target`, `behavior_rule`, and `boundary`. Use `map.<aspect>.v1`, the approving answer ID, `src.project-mapping-v0.2`, the exact `bfas.*` key, and a selected non-unspecified target. `behavior_rule` states an observable trigger and action; `boundary` states limits, known gaps, and calibration if needed. Example shape in prose: id `map.assertiveness.v1`, answer_id `A03`, aspect `bfas.assertiveness`, target `high`, behavior_rule “When comparing allowed options, propose a concrete advisory next step or process with reasons while preserving viable alternatives and human choice,” boundary “Preserve uncertainty and human choice; no tool use without existing permission.” This is a format example, not a preset or active persona.
- Every requested non-unspecified target needs its traceable mapping. Unspecified targets must not acquire an implicit aspect rule. Mapping content is proposed behavior, not evidence that the behavior occurs. Registry cases B01–B10 follow the same aspect order as the template, and are test references only.
- Every `conflicts` record has `id`, `aspect`, `candidates`, `status`, `resolution`, and `resolution_answer_id`. Each candidate has `target` and `answer_ids`; retain all alternatives and original evidence even after resolution. Different candidate rules may share the same target level; their distinct answer records must preserve the full conflicting rule text. `status` is `unresolved` or `resolved`. An unresolved record has empty resolution and resolution-answer fields and blocks finalization. A resolved record cites an actual answer choosing one target and one rule, or explicitly withdrawing to `unspecified`. This schema allows only one active target and one mapping per aspect; it cannot represent context splitting. If separate contexts are needed, retain the unresolved conflict and propose a narrower, separate future reviewed design. Never synthesize an average. Preserve withdrawn and superseded rule text in the record's resolution history; do not leave it active in `mappings`. For a workflow conflict, use `workflow_controls.<key>` in `aspect` and retain candidate instruction text as the candidate target.
- `unknowns` remains an explicit string array; remove stale unknowns only through a new preview. `non_claims` contains exactly the five tokens shown: they disclaim behavioral validation, cross-provider reliability, psychometric validity, real-person trait inference, and real-user readiness. These never permit diagnosis, emotional-state claims, or sensitive-attribute inference. Retain scope and additional limitations in `scenario`, `unknowns`, and mapping boundaries.
- All fixed boundary booleans remain `true`. This baseline validator requires both optional authorization flags to stay `false`: panel rehearsal and persistence are outside its accepted path. If explicitly requested, record that requirement and route through the existing separately reviewed optional protocol rather than claiming this baseline validates it. Authorization never grants permission beyond the user's scope or bypasses a tool's approval requirements.
- `evidence.kind` is `not_run` or `synthetic_protocol_fixture`; `behavioral_validation` stays `false`. Synthetic structural checks are not observed agent behavior. Any separately requested behavioral study needs its own explicit evidence artifact with inputs, outputs, case IDs, agent context, and limitations; this schema never represents it as personality validation. Adding a report reference to approved content requires a new revision.

## Exact-preview approval and final wrapper

Preview the full payload as readable Markdown plus its authoritative JSON, and ask the user to confirm that exact revision. Keep the actual presented preview for comparison. The final wrapper must preserve the entire approved payload exactly. For a Markdown-only workflow, manually compare that complete immutable snapshot with the presented preview and set `approval.digest` to `null`; do not invent a hash. When a trusted tool computes a digest, use SHA-256 over canonical JSON: UTF-8, keys sorted recursively, compact separators, non-ASCII preserved, and no trailing newline. Any provided digest must match. A digest never replaces exact payload comparison or the user's explicit confirmation. The optional validator compares the final snapshot with a separately supplied actual preview even when the digest is null.

After explicit confirmation and successful manual review, a final record has exactly four top-level fields: `kind` set to `spec`; `approved_preview` containing the complete unchanged preview object; `approval` containing `status` set to `confirmed`, the exact `revision`, `digest` (a trusted computed hash or `null`), `confirmed_by`, and `record_ref` identifying the actual user confirmation; and `review` set to `Pass`. Approval is evidence of a user's design choice, not validation of personality or source claims. A structural checker cannot authenticate who spoke; the executing agent and reviewer must verify the confirmation exists and applies to this exact preview.

Manual review outcomes are `Not reviewed`, `Pass`, `Revise`, or `Block`. Only `Pass` permits the final wrapper. Draft outcomes and issues may be recorded outside the payload as review metadata, never as extra operating instructions. Review checks fictional/low-stakes scope, all ten keys and enums, explicit unspecified semantics, supporting answer/source/mapping traces, retained conflict candidates, invariant boundary posture, non-claims, authorizations, and exact-preview approval. If correction changes the payload, increment revision and obtain fresh confirmation; do not patch a confirmed preview in place. Allow at most one minimal correction pass for manual review, then stop for owner direction if further corrections are needed. This does not limit user-requested interview revisions.

On reload, preserve `approved_preview` and its digest value, including `null`, exactly. Never fill missing traits, remove history, silently reinterpret mappings, or add a default-middle value. Missing or incompatible material blocks use and requires an explicit amendment through a new preview; it does not license reconstruction from memory.
