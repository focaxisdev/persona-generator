# Compact Manual Persona Pack Validator Checklist

Purpose: decide whether one completed Persona Pack folder satisfies the Persona Pack v0.1 contract without code, tools, databases, or automated validators.

Use this as a compact quality gate:

```text
Persona Pack folder
-> compact checklist review
-> Pass / Revise / Block
```

## Review Inputs

- One Persona Pack folder containing the five required output files.
- The related corpus manifest and source files, when available.
- The Persona Pack v0.1 contract: `protocols/persona-pack-v0.1-contract.md`.

Do not add new persona claims during review. Check only whether the pack is structured, traceable, bounded, and safe to reuse as Markdown.

## Decision Rule

- **Pass**: every checklist item is Pass, with no unresolved safety or traceability issue.
- **Revise**: one or more items need correction, but the pack is still reviewable and no blocker is present.
- **Block**: any blocker is present. Do not reuse the pack until the blocker is resolved and the pack is reviewed again.

## Checklist

| # | Check | Pass | Revise | Block |
| --- | --- | --- | --- | --- |
| 1 | Required files | `profile.md`, `evidence-ledger.md`, `contradictions.md`, `unknowns.md`, and `usage-boundaries.md` all exist. | A required file exists but is clearly incomplete or placeholder-heavy. | Any required output file is missing. |
| 2 | Source status | The corpus uses exactly one status: `fictional`, `self-provided`, or `consent-based`. | Status is present but wording is ambiguous. | Status is missing, mixed, or includes non-consented third-party private material. |
| 3 | Corpus scope | Intended purpose, allowed uses, prohibited uses, analysis scope, excluded scope, and known limitations are visible. | Scope exists but leaves important ambiguity. | No usable corpus scope is provided. |
| 4 | Source inventory | Each included source has a Source ID and location reference. | Minor source-location gaps exist but evidence can still be checked. | Evidence cannot be traced back to sources. |
| 5 | Evidence ledger | Evidence records separate observation from interpretation and include Evidence ID, Source ID, source location, confidence, supported dimension, and counterevidence status. | Some records need cleanup but the ledger remains auditable. | Evidence ledger is missing, opaque, or mostly unsupported by sources. |
| 6 | Profile traceability | Every meaningful operational claim in `profile.md` cites one or more Evidence IDs. | A few claims need Evidence IDs, downgrade, or removal. | Major claims are uncited, broad, or impossible to audit. |
| 7 | Confidence vocabulary | Confidence uses only `high`, `medium`, `low`, or `unknown`, with weaker evidence assigned lower confidence. | A few confidence labels need correction. | Numeric scores, psychometric ratings, or unsupported high-confidence claims are used. |
| 8 | Contradictions | Contradictions and counterevidence remain visible with status: `unresolved`, `context-dependent`, `insufficient-evidence`, `revised`, or `not-a-contradiction`. | Contradictions are present but need clearer links or status. | Counterevidence is hidden, deleted, or forced into a clean trait claim. |
| 9 | Unknowns | Missing evidence stays unknown, with overclaiming risk and next safe action recorded. | Unknowns are present but incomplete. | Unknowns are converted into claims, default traits, or medium-confidence assumptions. |
| 10 | Usage boundaries | Allowed uses, prohibited uses, and interpretation rules are explicit. | Boundaries are present but need clearer wording. | Prohibited or high-stakes use is allowed or left unblocked. |
| 11 | Unsupported claims | The pack blocks diagnosis, clinical assessment, psychometric scoring, hidden-trait truth claims, honesty/deception/morality scoring, protected or sensitive attribute inference, and high-stakes suitability claims. | A borderline claim needs downgrade, removal, or explicit non-claim wording. | Any unsupported or prohibited claim remains active. |
| 12 | Markdown portability | Another agent can understand source status, Evidence IDs, claims, counterevidence, unknowns, boundaries, explicit non-claims, and update history by reading only Markdown files. | Minor navigation or wording improvements are needed. | The pack depends on hidden prompt state, app/runtime behavior, database, API, embeddings, or non-Markdown tooling to be understood. |

## Reviewer Result

```text
Pack path:
Review date:
Reviewer:
Source status:

Decision: Pass / Revise / Block

Required revisions:
-

Blockers:
-

Notes:
-
```
