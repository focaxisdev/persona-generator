# Release and Marketing Acceptance — proposed v0.2.0-alpha

This is an acceptance plan, not a release announcement. No release, tag, main merge, or website deployment is authorized by this increment. Preserve v0.1.0-alpha without modification. The coordinator must review the Draft PR before any later public action.

| Gate | Reproducible acceptance | Current disposition |
| --- | --- | --- |
| Source and taxonomy | Ten aspect/domain pairs checked against named primary sources; original summaries; source locators and license scope recorded; no imported questionnaire | Review source ledger and registry in Draft PR. |
| Configuration contract | Both interview paths reach an explicit preview; unspecified remains unconstrained; contradictions preserved; exact preview confirmation; independent manual review | Implemented contract; review required. |
| Static verification | Run documented validator and negative tests at the exact candidate commit; retain commands and results; no broken local links | [32 tests and CLI checks passed](../validation/STATIC_CHECK_REPORT.md); not behavioral evidence. |
| Behavior pilot | Execute [BEHAVIOR_PROTOCOL](../validation/BEHAVIOR_PROTOCOL.md), retain exact inputs/raw outputs/model metadata, baseline and qualitative contrasts, repeat/multiround/reload results, invariants and failures | **BLOCKED: not run.** No model runtime evidence captured for this increment. |
| Independent review | Reviewer separate from implementation checks source/mapping boundary, artifacts and tests; all blocking findings resolved; coordinator accepts exact commit | Coordinator acceptance pending. |
| Claims and migration | README, quickstart, migration, and marketing copy obey [claims matrix](CLAIMS_MATRIX.md); legacy artifacts not silently upgraded | Draft PR review required. |
| Release packaging | Exact accepted commit, changelog distinguishing source/static/model evidence, license/source attribution, versioned Markdown bundle, tested instructions, new alpha tag only | Not performed; requires later authorization after gates. |
| Marketing page | Clear purpose and start path; construct → proposed behavior → evidence illustration; explicit pending/limited evidence; no validation badge, invented benchmark, testimonials, or human-mind claim | Not built or deployed this round. |

## Behavior decision rule

Before trials, freeze the cases, conditions, rubric, and run matrix from the protocol. Retain all attempts; a missing baseline, missing raw output, unresolved invariant failure, missing repeat/multiround/reload trial, or merely hand-written example fails the gate. A negative or not-elicited contrast must be reported and either narrowed out of the release's claimed behavior scope or investigated and rerun under a versioned protocol. Do not quietly discard failures or change success criteria after seeing outputs. Passing permits only the scoped claims supported by the recorded observations, never psychometric validity or universal stability.

## Next-round marketing review

Prepare a reviewable page before publication. Include an honest headline such as “Design agent behavior with traceable psychological constructs,” a short design-intent example, a source/mapping/evidence diagram, the confirmation step, scope restrictions, and links to the source ledger and evidence. Test small-screen layout, keyboard navigation, contrast, links, and any copy/paste interaction. Use original or explicitly licensed assets; ornamental images are optional. Record the preview and acceptance results before requesting any deployment action.
