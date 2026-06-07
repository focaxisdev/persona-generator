# Persona Pack v0.1 Contract

## 1. Purpose

Persona Pack v0.1 defines the smallest portable Markdown contract for creating an auditable operational persona from a bounded fictional, self-provided, or consent-based text corpus.

The public default is fictional use. Self-provided or consent-based use requires explicit scope, consent, and handling rules before any source is included.

## 2. Core Design Principles

- local-first
- Markdown-first
- agent-agnostic
- evidence-linked
- contradiction-aware
- uncertainty-aware
- portable
- explicit-boundary-first
- non-diagnostic
- non-psychometric
- user-controlled

## 3. Minimal Input Contract

The input contract is a corpus folder copied from `persona-pack-v0.1/corpus-template/`.

Required input files:

- `corpus-manifest.md`
- `sources/README.md`
- one or more source Markdown or plain text files in `sources/`, unless the corpus is being prepared before sources are added

The corpus manifest must identify:

- corpus ID and name
- source status: `fictional`, `self-provided`, or `consent-based`
- intended purpose
- allowed and prohibited uses
- analysis scope and excluded scope
- source inventory with Source IDs
- consent and handling notes
- known limitations

## 4. Minimal Output Contract

The output contract is a Persona Pack folder copied from `persona-pack-v0.1/persona-pack-template/`.

Required output files:

- `profile.md`
- `evidence-ledger.md`
- `contradictions.md`
- `unknowns.md`
- `usage-boundaries.md`

The pack is complete only when claims in `profile.md` can be traced to Evidence IDs, contradictions and unknowns remain visible, and usage boundaries explicitly block prohibited uses.

## 5. Required Files

| File | Required Purpose |
| --- | --- |
| `profile.md` | Operational persona summary, dimensions, safe agent usage notes, explicit non-claims, and update history. |
| `evidence-ledger.md` | Evidence records linking observations to Source IDs, source locations, interpretation boundaries, and dimensions. |
| `contradictions.md` | Contradictions, counterevidence, possible context explanations, and resolution status. |
| `unknowns.md` | Missing evidence, unknown dimensions, overclaiming risks, and safe next actions. |
| `usage-boundaries.md` | Allowed uses, prohibited uses, and required interpretation rules. |

## 6. Required Fields

`profile.md` must include:

- profile metadata
- executive summary
- operational persona dimensions
- communication preferences
- decision and collaboration preferences
- context-dependent patterns
- contradictions and unknowns summary
- safe agent usage notes
- explicit non-claims
- update history

`evidence-ledger.md` must include:

- Evidence ID
- Source ID
- Source Location
- Observation
- Interpretation Boundary
- Supports Dimension IDs
- Confidence
- Counterevidence?

`contradictions.md` must include:

- Contradiction ID
- Related Dimension IDs
- Evidence IDs
- Description
- Possible Context Explanation
- Resolution Status

`unknowns.md` must include:

- Unknown ID
- Question or Dimension
- Why It Is Unknown
- Missing Evidence
- Risk of Overclaiming
- Next Safe Action

`usage-boundaries.md` must include allowed uses, prohibited uses, and interpretation rules.

## 7. Confidence Vocabulary

Persona Pack v0.1 uses only these confidence values:

- `high`
- `medium`
- `low`
- `unknown`

Rules:

- `high` requires repeated, direct, context-consistent corpus evidence.
- `medium` requires multiple signals but still has limits.
- `low` indicates weak, narrow, indirect, or context-bound evidence.
- `unknown` is required when evidence is missing, conflicting, insufficient, outside scope, or unsafe to infer.

Do not convert unknowns into numerical scores.

## 8. Evidence ID Linking Rules

- Every meaningful operational claim in `profile.md` must reference at least one Evidence ID from `evidence-ledger.md`.
- Evidence IDs must point to a Source ID and source location.
- Observations must be written separately from interpretation.
- A single sentence is not enough for broad claims about stable personality.
- Counterevidence must remain linked and visible.

## 9. Contradiction Handling Rules

- Contradictions are valid output.
- Do not delete counterevidence to make the persona cleaner.
- Do not force conflicting evidence into one stable trait.
- Use lower confidence when contradictions materially weaken a claim.
- Allowed resolution statuses are:
  - `unresolved`
  - `context-dependent`
  - `insufficient-evidence`
  - `revised`
  - `not-a-contradiction`

## 10. Unknown Handling Rules

- Unknowns are valid output.
- Missing evidence must remain unknown.
- Unknowns must not become default tags, neutral scores, or medium-confidence claims.
- Unknowns should identify what evidence would be needed and what overclaiming risk exists.

## 11. Source Status Rules

The corpus must use exactly one source status:

- `fictional`
- `self-provided`
- `consent-based`

Rules:

- Fictional sources must be clearly marked fictional.
- Self-provided sources must be scoped by the provider.
- Consent-based sources require consent and handling notes.
- Non-consented third-party private material is not allowed.
- Public examples should use fictional sources.

## 12. Theory Mapping Boundaries

Theory mappings and source notes may support:

- vocabulary
- construct family labels
- inference boundaries
- unsafe-overreach warnings
- optional theory references

Theory mappings and source notes must not be treated as:

- text-only inference validity
- psychometric measurement
- clinical validation
- real-world behavior prediction
- proof of hidden traits
- proof of honesty, deception, trustworthiness, morality, or protected attributes

Operational claims in Persona Pack v0.1 must be supported by corpus evidence, not by theory mapping alone.

## 13. Unsupported Claims Rules

Unsupported claims must be removed, downgraded to `unknown`, or recorded as prohibited non-claims.

Persona Pack v0.1 must not claim:

- psychological diagnosis
- clinical assessment
- psychometric score
- objective personality truth
- hidden true self
- hidden motives
- honesty, deception, trustworthiness, or morality scoring
- protected or sensitive attribute inference
- hiring, employment, credit, insurance, policing, immigration, education placement, legal, medical, surveillance, or manipulation suitability

## 14. Real-Person Use Gate

Persona Pack v0.1 does not approve real-person deployment.

Before any workflow uses real personal data, the proposed use must have explicit consent, source inventory, storage, retention, deletion, correction, review, sensitive-attribute handling, prohibited-use exclusion, and owner approval.

Until then, use the contract for fictional examples, self-provided text with explicit scope, or governance simulations.

## 15. Agent Portability Expectations

A completed Persona Pack must be usable by another agent by reading only Markdown files.

The receiving agent should be able to identify:

- source status
- intended use
- Evidence IDs
- operational patterns
- counterevidence
- unknowns
- usage boundaries
- explicit non-claims
- update history

No receiving agent should need a database, API, package install, UI, vector index, embedding store, or hidden prompt state to understand the pack.

## 16. Intentional Exclusions

Persona Pack v0.1 intentionally does not include:

- automated scoring
- psychometric claims
- hidden-trait detection
- personality truth claims
- database storage
- API services
- embeddings
- vector search
- Web UI
- viewer implementation
- CLI tooling
- automated validators
- real-person deployment
- public-release workflow
- multi-agent voting
- brainstorming panels
- decision panels
- fictional persona batch generation

These items may exist as downstream layers elsewhere, but they are not part of the Persona Pack v0.1 kernel.

## 17. Completion Criteria

A Persona Pack v0.1 is complete when:

- the corpus manifest is filled
- every included source has a Source ID
- all five required output files exist
- every meaningful claim links to Evidence IDs
- confidence values use only `high`, `medium`, `low`, or `unknown`
- contradictions and counterevidence are preserved
- unknowns and insufficient evidence are recorded
- unsupported claims are blocked or downgraded
- usage boundaries include allowed and prohibited uses
- theory mapping is optional and bounded
- real-person governance is respected
- the pack can be copied and understood as Markdown without tooling
