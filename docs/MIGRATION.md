# Migration from v0.1 to the v0.2 candidate

The v0.1 directories, protocol contracts, example fixtures, and published release are not rewritten. The new `persona-design-v0.2` directory is an unreleased opt-in path for configuring desired agent behavior. This does not add a permanent persona inventory.

| Existing item | Treatment |
| --- | --- |
| Decision tempo, evidence posture, uncertainty posture, communication posture | Preserve as workflow controls; no automatic BFAS mapping. |
| Creative posture, collaboration posture, time horizon, boundary posture | Preserve as workflow controls; boundary obligations remain mandatory. |
| Missing psychological construct goals | Record all ten as `unspecified` until the user requests and confirms a target. |
| Old spec or Persona Pack | Still v0.1; do not relabel it as a confirmed v0.2 spec. |
| Old manual review Pass | Does not confirm a new preview or validate its mappings. |
| Legacy dry-run summary | Does not establish new behavior evidence. |

To migrate one bounded task, retain the original artifact, run the new interview, and cite the old workflow controls as context rather than evidence of traits. Ask the user to review any proposed new construct target and its rationale. Preserve contradictions and uncertainty. Require explicit confirmation of the new preview and a new manual review before use.

For optional Persona Pack handoff, keep the reviewed v0.2 Markdown spec intact as a companion artifact with its identity/digest. Record that companion in the existing evidence ledger and handoff notes without changing the v0.1 schema or pretending the pack alone preserves the new contract. On reload provide the exact companion and validate it against the approved preview. Missing companion, changed content, or missing confirmation blocks v0.2 activation.

There is no automatic conversion, score conversion, domain-to-aspect inference, or mapping of BFI-2/HEXACO facets. A desire for a fast workflow is not evidence of Extraversion, and evidence-seeking is not a measurement of Intellect.

## Separate mapping-v2 proposal

The [mapping-v2 workflow](../persona-design-v0.2/mapping-v2/WORKFLOW.md) is a separate opt-in proposal, not an automatic migration or the default path. Coordinator acceptance of its [acceptance proposal](../persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md) is pending; v2 behavior and authentic owner E2E are NOT RUN. Begin all ten aspect keys unspecified. Explicitly approve each selected version, anchor, rule and boundary, then separately confirm the complete new preview. B03/B05/B06/B08/B10 use revised `.v2` IDs; B01/B02/B04/B07/B09 retain `.v1` only by explicit opt-in. B01/B02 remain experimental expression controls. Existing specs, confirmations, reviews and evidence remain historical and do not transfer. A separate extension contract is proposed; v1 validator acceptance must not be assumed. See the [v2 index](../persona-design-v0.2/mapping-v2/README.md) for scope and current blockers.
