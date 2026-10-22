# Mapping v2 Markdown workflow

Status: **proposed independent contract; actual owner E2E NOT RUN; behavioral evidence NOT RUN; coordinator acceptance PENDING.** Read [README.md](README.md), [cards.json](cards.json), the [source ledger](../sources.md), [safety boundaries](../../docs/SAFETY_BOUNDARIES.md) and [acceptance proposal](ACCEPTANCE_PROPOSAL.md). This Markdown sequence can be followed without software, paid APIs or private conversation history. Software checks are optional structural checks; the old `validation/validate_spec.py` does not define or validate this separate v2 contract. Extension-validator acceptance is pending and must not be claimed from v1 tests.

## Scope and version selection

Ask about the desired **observable behavior of a fictional agent** for a bounded low-stakes task. Choices, terse replies and free text are design requests, never evidence of the user's real personality, mental states, sensitive attributes, intelligence, morality or suitability. Do not collect biography, feelings or self-ratings to fill settings. Explain: “Choose a behavior, describe your own, or skip. Your answers describe the agent you want. Skipping leaves it unspecified; middle is a deliberate choice.”

Accuracy, explicit uncertainty, privacy, safety, existing tool permissions and human final judgment are invariant. All anchors require adequate work under the same task budget; no anchor permits less accurate work or more authority. Stop for real-person profiling, psychometric measurement, diagnosis, sensitive inference, covert manipulation, high-stakes decisions or autonomous final judgment. Default to ephemeral use, no panel and no Persona Pack/persistence; explicit optional requests require their separately reviewed protocols.

| Case | Aspect | Explicitly available mapping ID | Scope |
| --- | --- | --- | --- |
| B01 | `bfas.volatility` | `map.volatility.v1` | Experimental expression control only: setback emphasis |
| B02 | `bfas.withdrawal` | `map.withdrawal.v1` | Experimental expression control only: known-downside placement |
| B03 | `bfas.compassion` | `map.compassion.v2` | Revised proposed behavior; read exact card |
| B04 | `bfas.politeness` | `map.politeness.v1` | Retained wording hypothesis; explicit opt-in |
| B05 | `bfas.industriousness` | `map.industriousness.v2` | Revised proposed behavior; read exact card |
| B06 | `bfas.orderliness` | `map.orderliness.v2` | Revised proposed behavior; read exact card |
| B07 | `bfas.enthusiasm` | `map.enthusiasm.v1` | Retained wording hypothesis; explicit opt-in |
| B08 | `bfas.assertiveness` | `map.assertiveness.v2` | Revised proposed behavior; read exact card |
| B09 | `bfas.intellect` | `map.intellect.v1` | Retained reasoning-route hypothesis; explicit opt-in |
| B10 | `bfas.openness` | `map.openness.v2` | Revised narrow feasible-option hypothesis; read exact card |

This is not an automatic migration. All ten keys start unspecified even when an old spec exists. Treat old instructions as context only until the owner explicitly selects a mapping version, anchor and rule for this new design. Remaining `.v1` mappings are not silently enabled or renamed `.v2`. Preserve the original spec, approvals and observations unchanged. No v1 approval, source status, pilot result, static pass or evidence label transfers to a v2 rule. The v1 pilot remains evidence only about its actual v1 instructions and conditions.

The five revised cards use B-case identifiers in `aspect_id`; the table above supplies their exact `bfas.*` payload keys. An anchor's complete rule is the ordered text of its `rule_clause_ids` resolved against that card's `rule_clauses`; show all of it, along with the card's `nonclaims` and relevant common task requirements. Do not show a clause ID as if it were the rule text. The five retained `.v1` mappings are not revised cards: consult the exact [existing interview](../interview.md) and [registry](../construct-registry.md), preserve their full text as dependencies, and require the same explicit opt-in. A card's diagnostic scenario requirements are not a general license to impose those requirements on another task. Different scenario-specific wording is a new disclosed custom rule and does not inherit that card's future evidence.

The revised anchors can overlap: low B03 does not forbid comparing accommodations, low B05 does not prohibit milestones, low B06 does not forbid stages, and low B08 does not prohibit recommendations. Do not turn absence of a required feature into a forbidden feature. Distinguish adherence to the selected clauses from discriminability across conditions, task usefulness and safety. B10 instead explicitly varies exactly one/two/three materially distinct feasible approaches; those counts describe requested output breadth, not scores or measured traits.

## Reproducible execution sequence

1. **Open the bounded task.** Record the fictional scenario, role, intended output, allowed use, exclusions, human final reviewer and stop condition. Obtain the owner's explicit agreement to the fixed boundary posture. Retain minimal faithful answers as unique `A01`, `A02`, … records, with `origin: owner` only when the answer actually came from the owner. No answer or approval may be fabricated.
2. **Initialize a draft.** Create revision `r1` with exactly the ten aspect keys listed below, all `unspecified`. Include the eight workflow controls separately; the first seven default to `unspecified`, and the boundary posture retains the fixed invariants with its supporting answer ID. Preserve unknowns and the explicit absence of behavior evidence.
3. **Offer choices or free text.** In B01–B10 order, show the current card's exact low/middle/high anchors, its mapping ID, limitations and “unspecified / skip”; always accept the owner's own behavioral wording. A batch is optional at the owner's request. Record each answer verbatim or with a faithful minimal excerpt and an ID. An omission, ambiguous short reply, refusal or skip is not middle. Personal self-description is not an agent setting; redirect to desired agent behavior without inferring a trait.
4. **Propose a traceable translation.** For each requested setting, show the answer IDs, aspect, versioned mapping ID, selected anchor, complete trigger/action rule and its boundary. Say: “From [answer IDs], I propose [mapping ID], [anchor], with this exact rule and boundary: [full text]. Do you approve this translation, prefer different wording, or leave it unspecified?” A choice selects a candidate; it is not silent approval of an undisclosed rule. Record actual affirmative approval as another answer ID bound to all these fields. Until that happens, the aspect remains unspecified and the candidate stays outside active mappings. A clear free-text instruction can remain a qualitative workflow instruction without a BFAS mapping if the owner rejects the label; do not classify it anyway. Custom wording must be identified as a custom rule, not attributed to the frozen card, and cannot inherit diagnostic evidence for that card.
5. **Handle conflicts explicitly.** Preserve all candidate anchors, distinct rule/boundary text, answer IDs and version IDs. Newer does not automatically win; two incompatible rules at the same anchor also conflict. Ask the owner to choose one exact candidate or withdraw to unspecified. Record the resolution answer and retain the original history. Do not average or split contexts in this minimal contract. An unresolved conflict blocks finalization, as does an instruction weakening an invariant.
6. **Show the complete preview.** Include the authoritative JSON and a readable explanation of every active rule, all unspecified settings and all limitations. The full field checklist is below. Freeze one explicit revision and preserve exactly what was presented. Ask the owner to confirm that exact complete revision, request changes or leave it a draft. Approval of a mapping alone, silence, “continue”, a reviewer's pass or confirmation of an old revision is insufficient.
7. **Bind authentic confirmation and review.** Keep confirmation outside the immutable preview. Verify that an actual owner response explicitly confirms the identified complete revision; record a genuine source reference and identity, not a simulated quote. Compare the entire snapshot, then complete manual review. Only resolved conflicts, intact boundaries, approved mapping traces, authentic current-revision confirmation and review `Pass` permit a final wrapper. A digest authenticates no person. This documentation round creates no such final wrapper or approval.
8. **Invalidate on any change.** Any change to a previewed field—including a source reference, unknown, answer excerpt, mapping dependency, rule, workflow control or evidence label—creates `r2`, `r3`, … and clears current confirmation. Preserve prior snapshots and approvals as history, never as approval of the new payload. Show the whole revised preview and obtain new owner confirmation. Approval metadata may be added outside the payload without altering it. If review requires a correction, allow at most one minimal review correction pass and return to complete preview/confirmation; another required correction stops for owner direction. This does not restrict revisions the owner requests during interview.
9. **Reuse in a fresh session.** Provide the complete saved final wrapper, the exact presented preview and the referenced mapping/source dependencies. Read them without earlier chat or prior outputs. Check the approved snapshot, confirmation reference, review result, revision, canonical digest if present, and dependency identity. Apply only approved rules; preserve every unspecified value and all traces/conflicts. Missing, changed, incompatible or unverifiable dependencies block activation; report the exact problem without reconstructing from memory or upgrading versions. A new requested change restarts the revision cycle. Stop after the bounded task; fresh reuse is not permission for a persona inventory or persistence.

## Independent v2 preview contract

The proposed schema identifier is `persona-design-v0.2-mapping-v2`. It is deliberately separate from `persona-design-v0.2` and must not be passed off as accepted by the v1 validator. Its extension validator and compatibility decision are pending. Until implementation is accepted, manually check the full contract; a manual check does not prove behavioral quality or real owner consent.

A complete preview contains exactly the fields illustrated below. `answers` carry unique IDs and minimal faithful text; `origin` distinguishes authentic owner records from handwritten illustrations. `sources` cite the exact human-vocabulary source ledger entries with unchanged provenance. The local source ID `src.project-mapping-v2` identifies the original v2 proposal in `cards.json`, not research support or behavioral evidence. Use `src.project-mapping-v0.2` only for explicitly retained `.v1` mappings; the old ledger entry does not support revised v2 rule text. `mapping_dependencies` identify each selected card by mapping ID, artifact path and exact frozen content identity (a tool-computed file digest or preserved exact text); none are active initially. `mappings` contains only explicitly approved non-unspecified rules. Each mapping contains `id`, `aspect`, `anchor`, `answer_ids`, `behavior_rule`, `boundary`, `mapping_approval_answer_id` and `dependency_ref`. The referenced approval answer must explicitly approve that exact version, anchor, rule and boundary; one active mapping per aspect. Unspecified aspects have no implied rule.

`conflicts` preserve candidates, evidence and resolutions, including withdrawn and superseded rule text. Workflow controls never silently fill aspect targets. `evidence` remains `not_run` with `behavioral_validation: false`; future observations require a separate artifact and new preview if referenced. A source citation, handwritten trace, preference, validator or approval is not behavior evidence.

The following is a **complete handwritten illustration of an initial preview**, not an owner interview, model output, approved spec or performed trial. `ILL01`/`ILL02` and all dialogue below are invented solely to explain structure. They cannot be used as real approval records. Copying this example does not complete an interview.

```json
{
  "schema_version": "persona-design-v0.2-mapping-v2",
  "kind": "preview",
  "revision": "r1",
  "scenario": "HANDWRITTEN ILLUSTRATION ONLY: a fictional paper-craft club wants one advisory session outline; a human organizer makes the final choice. No real-person profiling, high-stakes decisions, panel, persistence or external actions. Stop after one reviewed draft. Scenario evidence: ILL01; boundary evidence: ILL02.",
  "answers": [
    {"id": "ILL01", "origin": "handwritten_illustration", "text": "For a fictional paper-craft club, draft one session outline; I make the final choice."},
    {"id": "ILL02", "origin": "handwritten_illustration", "text": "Retain accuracy, explicit uncertainty, privacy, safety, existing tool permissions and human final judgment; no panel or persistence."}
  ],
  "sources": [
    {"id": "src.deyoung2007", "reference": "../sources.md#srcdeyoung2007", "scope": "Human construct vocabulary only; not agent validation."},
    {"id": "src.ipip.bfas-table", "reference": "../sources.md", "scope": "Human vocabulary/source context only; no questionnaire administration."},
    {"id": "src.project-mapping-v2", "reference": "cards.json", "scope": "Local provenance for original v2 engineering proposals only; not research support, observed behavior or transferred v1 evidence."}
  ],
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
    "boundary_posture": "Preserve accuracy, explicit uncertainty, privacy, safety, existing tool permissions and human final judgment. Evidence: ILL02."
  },
  "mapping_dependencies": [],
  "mappings": [],
  "conflicts": [],
  "unknowns": [
    "All ten aspects are intentionally unspecified.",
    "No owner interview or authentic confirmation occurred in this illustration.",
    "No behavior evaluation or real-owner E2E acceptance has been run.",
    "V2 extension-validator acceptance is pending."
  ],
  "non_claims": ["behavioral_validation", "provider_reliability", "psychometric_validity", "real_person_traits", "real_user_readiness"],
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
  "evidence": {"kind": "not_run", "behavioral_validation": false}
}
```

Only `low`, `middle`, `high`, `unspecified` are allowed aspect values; exactly these ten keys are required. No numbers, domain totals, scores, midpoint defaults or additional aspects. The full preview must preserve the scenario, answers, sources, targets, all eight controls, exact mapping dependencies and active mappings, conflict history, unknowns, non-claims, boundaries and evidence status. Runtime instructions cannot be hidden in surrounding prose or confirmation metadata.

## Exact confirmation binding

For a real accepted final artifact, use an outer record with `kind: spec`, `approved_preview` holding the complete unchanged preview, `approval` and `review`. `approval` records `status: confirmed`, the exact `revision`, `digest` (trusted computed SHA-256 or `null`), `confirmed_by` and `record_ref` pointing to the genuine response and its presented preview. `review` records `Pass` and the actual review reference. This v2 shape is proposed independently; the old validator's wrapper rules do not imply support.

Compare the entire final `approved_preview` with the actual presented JSON, even if `digest` is null. When tools compute a digest, hash canonical JSON as UTF-8 with recursively sorted object keys, compact separators, non-ASCII preserved and no trailing newline. Preserve array order, values and all fields. Canonicalization never licenses changing content after approval. Separately record full-file/dependency hashes for reload identity where computed; distinguish those byte hashes from the preview's canonical digest. Never invent hashes. Markdown-only execution may retain exact snapshots and use a null digest; uncertainty about identity blocks activation.

Owner confirmation should explicitly identify the whole preview, for example a real response confirming “complete preview r3” when that exact r3 was presented. A signature-shaped string authored by the implementer, judge or model is not a real response. Keep confirmation/review metadata outside the immutable design. No final artifact with real confirmation is supplied here because none has occurred.

## Handwritten traces, not execution evidence

These prospective traces show the expected state transitions. They are intentionally **handwritten**, with no model run and no real owner's approval. They cannot pass the [authentic E2E gate](ACCEPTANCE_PROPOSAL.md).

| Trace | Handwritten steps | Required state |
| --- | --- | --- |
| Choice | `ILL03`: owner selects a displayed B08 anchor → interviewer shows exact `map.assertiveness.v2` anchor/rule/boundary and answer trace → `ILL04` explicitly approves that translation | Only then add the selected target and mapping; full new preview still awaits separate confirmation |
| Short answer | `ILL05`: “Let the group decide; show what is supported” → interviewer proposes the precise candidate rule/version and asks approval | Do not infer low Assertiveness, the user's personality or permission from that short reply; keep unspecified until clarified/approved |
| No mapping label | Owner approves concrete wording as a workflow instruction but declines a construct label | Retain the qualitative instruction with evidence; relevant aspect remains unspecified |
| Skip | Owner skips B10 | `bfas.openness` remains unspecified; no middle or breadth rule is added |
| Conflict | Two answers select incompatible B05 rules, even if both say high | Preserve both complete candidates and answer IDs; block finalization until explicit selection or withdrawal |
| Complete preview | Mapping translations are approved; interviewer presents every field of `r2` | Pending confirmation, not final; fragment approval does not bind the whole payload |
| Exact confirmation | A real owner would explicitly confirm complete `r2`, then reviewer would record Pass | Future final wrapper preserves that full snapshot; this hypothetical row supplies no approval |
| Amendment | After an approved snapshot, owner requests changed wording; interviewer produces full `r3` | Clear current confirmation immediately; old `r2` approval remains historical and cannot activate `r3` |
| New confirmation | Owner would explicitly confirm complete `r3`, followed by review | Only a genuine new response can authorize the changed snapshot; not performed here |
| Fresh reuse | A new session would read the exact saved `r3` wrapper and frozen dependencies without prior chat | Preserve approved content and unspecified keys; mismatch or missing approval blocks use; no reuse was executed here |

No state transition in this table counts as evidence that a model follows instructions, that a person approved a design, or that a release is ready. Actual work stops at an unconfirmed draft whenever the required authentic evidence is missing.
