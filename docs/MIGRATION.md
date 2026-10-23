# Migration and historical compatibility

The canonical unreleased candidate now starts at [Quickstart](QUICKSTART.md) → [desired-trait profile](../profiles/README.md). The old core contract remains a separate preserved diagnostic interface. This documentation change does not relabel or rewrite a released package, old spec, old confirmation, mapping, or historical evidence.

| Artifact | Treatment |
| --- | --- |
| v0.1 scenario workflow and Persona Pack | Optional legacy formats; retain original identity. |
| Workflow controls such as decision tempo, evidence posture, and creative posture | Context only; no automatic aspect or operation mapping. |
| `persona-design-v0.2` mapping-v1/v2 documents | Frozen historical proposals; not the new core compiler's rule source. |
| Existing validator or test result | Applies only to its original contract and tested revision. |
| Historical pilot outputs/ratings/failures | Preserve unchanged; no evidence transfer to new operation IDs. |
| Old manual review or preview approval | Does not confirm a new core artifact. |
| Frozen v2 diagnostic design | NOT RUN; neither new core evidence nor a replacement release gate. |

## Preserved two-operation diagnostic migration

This section applies only when deliberately using the old diagnostic interface, not the current profile Quickstart. To configure an old task through the core, retain the old artifact, restate the desired behavior, inspect current [coverage](../core/COVERAGE.md), and create a new proposal using only the two supported operation choices. All other aspects remain unspecified. Resolve contradictions, approve exact proposed rules, and obtain a fresh confirmation of the complete new preview. Do not infer settings from domain labels, questionnaires, roles, or old ratings.

The package candidate is v0.2; the core schema is `persona-core-v1`; operations have separate `.v1` versions. Those names do not denote old mapping-v1 or mapping-v2 compatibility. The core compiler does not validate frozen mapping-v2 artifacts, and the old validator does not validate the new core contract.

A Persona Pack may accompany a core artifact only when persistence or handoff is explicitly requested. Keep the confirmed spec, its identity, and deterministic effective projection intact as companion artifacts. A pack or summary alone does not preserve core confirmation. On reload verify exact content and versions; missing, changed, or unconfirmed content blocks activation. Any behavior edit requires a new preview and reconfirmation.

The [original behavior protocol](../validation/BEHAVIOR_PROTOCOL.md) remains unchanged, including its 400-response minimum. The old 50-response diagnostic remains a separate unexecuted historical proposal. The [new prospective core plan](../core/EVIDENCE_PLAN.md) is separately scoped and cannot silently satisfy or replace that historical gate.

## Desired-trait profiles are a new version, not an upgrade in place

`persona-profile-v1`, explicit `persona-profile-catalog-v1` or `persona-profile-catalog-v2`, and their pinned hypothesis IDs identify specification hypotheses, separate from `persona-core-v1` and every historical mapping. Restate desired agent behavior, inspect all exact new rule semantics, keep unknowns unspecified, resolve conflicts and obtain a new complete confirmation. No old approval or behavioral result transfers. Do not change the old artifacts.

Store the newly confirmed profile as an explicit immutable ID/revision, and bind each parent/child separately. An existing descriptive Persona Pack may be kept alongside it but cannot silently set targets, become a binding or authorize a new profile. Exact-file persistence and fresh-process loader tests do not establish automatic host loading or behavioral persistence.

Catalog v2 changes the high-Politeness fallback (`hyp.politeness.v2`); all other hypothesis IDs remain pinned. Existing v1 profiles stay supported unchanged. Moving to v2 requires a new revision, exact preview and genuine confirmation, followed by separately confirmed assignments. Use [onboarding](../profiles/ONBOARDING.md) and [safe replacement/rollback](../profiles/ASSIGNMENTS.md). Rollback reassigns a retained confirmed revision with the **current** binding digest; it never republishes or edits history. Neither a catalog upgrade nor rollback transfers experimental results.
