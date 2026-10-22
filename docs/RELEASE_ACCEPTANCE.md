# Release and Marketing Acceptance — proposed v0.2.0-alpha

This is an acceptance plan, not a release announcement. No release, tag or main merge is authorized by this increment. Preserve v0.1.0-alpha without modification. The coordinator must review the Draft PR before any later public action. Marketing scope is the GitHub repository: README, Quickstart, examples, source/claim limitations and release notes.

| Gate | Reproducible acceptance | Current disposition |
| --- | --- | --- |
| Source and taxonomy | Ten aspect/domain pairs checked against named primary sources; original summaries; source locators and license scope recorded; no imported questionnaire | Review source ledger and registry in Draft PR. |
| Configuration contract | Both interview paths reach an explicit preview; unspecified remains unconstrained; contradictions preserved; exact preview confirmation; independent manual review | Implemented contract; review required. |
| Static verification | Run documented validator and negative tests at the exact candidate commit; retain commands and results; no broken local links | [32 original tests and CLI checks passed](../validation/STATIC_CHECK_REPORT.md); the pilot adds [24 passing integrity tests and reproducibility checks](../evaluation/pilot-2026-10-22/VERIFICATION.md). Neither test suite is behavioral evidence. |
| Behavior pilot | Execute [BEHAVIOR_PROTOCOL](../validation/BEHAVIOR_PROTOCOL.md), retain exact inputs/raw outputs/model metadata, baseline and qualitative contrasts, repeat/multiround/reload results, invariants and failures | **BLOCKED: full protocol NOT COMPLETED.** The [bounded pilot](../evaluation/pilot-2026-10-22/REPORT.md) records 102 synthetic responses, mixed contrasts, 28 budget violations and three unclear guardrail ratings; it does not meet the original coverage/confirmation requirements. |
| Independent review | Reviewer separate from implementation checks source/mapping boundary, artifacts and tests; all blocking findings resolved; coordinator accepts exact commit | Separate condition-blinded ratings and [independent model review](../evaluation/pilot-2026-10-22/INDEPENDENT_REVIEW.md) are recorded; receipt-validation findings were repaired and rechecked. Rating ambiguities and behavior failures remain visible; coordinator acceptance is pending. |
| Claims and migration | README, quickstart, migration, and marketing copy obey [claims matrix](CLAIMS_MATRIX.md); legacy artifacts not silently upgraded | Draft PR review required. |
| Release packaging | Exact accepted commit, changelog distinguishing source/static/model evidence, license/source attribution, versioned Markdown bundle, tested instructions, new alpha tag only | Not performed; requires later authorization after gates. |
| GitHub marketing documentation | README and Quickstart give a clear start path; examples distinguish handwritten fixtures from observations; sources, claim limits and draft release notes distinguish human vocabulary, proposed behavior and actual evidence; no validation badge, invented benchmark, testimonials or human-mind claim | Candidate documentation is reviewable in the independent core-v2 PR; acceptance pending. No standalone website is required. |

## Behavior decision rule

Before trials, freeze the cases, conditions, rubric, and run matrix from the protocol. Retain all attempts; a missing baseline, missing raw output, unresolved invariant failure, missing repeat/multiround/reload trial, or merely hand-written example fails the gate. A negative or not-elicited contrast must be reported and either narrowed out of the release's claimed behavior scope or investigated and rerun under a versioned protocol. Do not quietly discard failures or change success criteria after seeing outputs. Passing permits only the scoped claims supported by the recorded observations, never psychometric validity or universal stability.

## GitHub documentation review

Review the repository's [README](../README.md), [Quickstart](QUICKSTART.md), [handwritten workflow illustrations](../persona-design-v0.2/mapping-v2/WORKFLOW.md#handwritten-traces-not-execution-evidence), [source ledger](../persona-design-v0.2/sources.md), [claims matrix](CLAIMS_MATRIX.md) and [draft release notes](RELEASE_NOTES_DRAFT.md). Check that links and copyable instructions work, the default path remains clear, pending candidate status is visible and examples cannot be mistaken for model observations or authentic owner approvals. Review the exact candidate diff before any later merge or release decision.

## Scope correction

The user requested clear GitHub marketing. The independent website plan came from a coordinator misunderstanding and was outside that requested scope. PR #3 is excluded from this core-v2 work and is not merged. Any existing private preview stays private; it is neither shared nor deleted by this correction. No website creation, deployment or standalone website acceptance gate forms part of this plan. Historical v1 evidence and recorded outcomes remain unchanged.

## Separate v2 proposal; original gate unchanged

The [mapping-v2 index](../persona-design-v0.2/mapping-v2/README.md) and [prospective limited alpha proposal](../persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md) describe a separate path awaiting coordinator acceptance. They do not replace this gate or authorize release. Their 50-response fresh-only diagnostic is NOT RUN and cannot satisfy the original `10 × 5 × 2 × (3 rounds + reload) = 400` response minimum. Separate later multiround/reload coverage and authentic owner confirmation, amendment, reconfirmation and fresh reuse remain additional prospective requirements. Historical v1 budget failures and all locked observations remain intact; no evidence is inherited by revised rules. The existing workflow remains the default and release remains BLOCKED.
