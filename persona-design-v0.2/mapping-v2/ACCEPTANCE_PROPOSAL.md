# Prospective limited alpha acceptance proposal

Status: **PROPOSAL ONLY; coordinator decision PENDING; all v2 behavioral collection NOT RUN; real-owner E2E NOT RUN; release BLOCKED.** This file cannot amend the existing release gate by itself. It must be reviewed and accepted prospectively, before collection, as a separate and explicitly limited v2 path. No current evidence is relabeled passing, and no owner consent is fabricated.

The user-facing marketing surface is GitHub README, Quickstart, examples, source/claim limitations and [draft release notes](../../docs/RELEASE_NOTES_DRAFT.md). A standalone website was a coordinator misunderstanding, not a user requirement. PR #3 is excluded from this work and is not merged; any existing private preview remains private without sharing or deletion. Website work and deployment are outside this proposal, and no website gate is required. This independent core-v2 PR remains a reviewable candidate with no release authorization.

## Explicit difference from the existing gate

| Requirement | Existing repository protocol | Separate v2 proposal |
| --- | --- | --- |
| Mapping scope | Ten original cases B01–B10 with `.v1` mappings | Five revised mappings B03/B05/B06/B08/B10; other five remain opt-in v1 hypotheses outside the revised-mapping diagnostic |
| Initial conditions and independent repeats | Ten cases × five conditions (neutral, low, middle, high, unspecified) × two independent fresh replicates | Five revised mappings × five conditions × two independent fresh replicates |
| Responses per condition/replicate | Three conversational rounds plus one fresh-session round-1 reload | One fresh-context response only |
| Minimum task responses | `10 × 5 × 2 × (3 + 1) = 400` | `5 × 5 × 2 = 50` diagnostic responses; not 50 confirmations, not a reliability sample |
| Authentic workflow | Interview, exact preview, authentic user confirmation and manual review required | Diagnostic synthetic instructions cannot substitute; authentic owner E2E is a separate additional prospective requirement |
| Continuity | All-round/reload coverage required | Absent from the 50; repeat/multiround/reload coverage must be specified and performed separately before any continuity claim or limited alpha acceptance |
| Present result | NOT COMPLETED, release BLOCKED | NOT RUN, proposal PENDING, release BLOCKED |

The [original protocol](../../validation/BEHAVIOR_PROTOCOL.md) remains intact. The [v1 pilot](../../evaluation/pilot-2026-10-22/REPORT.md) is 102 responses under a different design, not a partial v2 pass. Its 28 G09 failures and all unclear and non-contrast findings remain in their original denominator. No threshold, counting convention, rubric endpoint or old failure is changed to rescue either version.

## Proposed decision process, before collection

1. Obtain a recorded coordinator decision on the exact scope and limitations of this proposal. Until then it is not an operative acceptance gate. Freeze the revised cards, [diagnostic design](../../evaluation/diagnostic-v2/design.json), [PLAN](../../evaluation/diagnostic-v2/PLAN.md), prompts, full condition packets, word-count convention, rubric, randomization/order, exposed model settings and file digests. Unknown provider settings stay unknown. No paid API or experiment execution is authorized by this document.
2. Collect the 50 diagnostic responses only under separately granted execution authorization. Retain complete inputs, outputs, attempts, failures, refusals, errors and metadata. A new mapping or task after inspection needs a new prospective version; it does not overwrite earlier failures. Synthetic instruction packets are explicitly not owner-confirmed specs.
3. Have two separate judges assess every claimed contrast and its task usefulness and invariant adherence. Use condition-blinded outputs where feasible; record leaked/unblinded conditions. Each judge retains exact quotations, category, rationale and ambiguity before the condition join. Do not treat two judges as independent human assessors unless they actually are human, or claim statistical agreement without an appropriate analysis. Retain disagreements; unresolved relevant ambiguity blocks the positive claim rather than being voted away.
4. Require bounded observed contrasts for **all required intended anchors** in the frozen design, task-useful outputs, and safe adherence to the fixed boundaries, with two-judge agreement and no unresolved relevant ambiguity. Compare low/middle/high against the specified rule, neutral, unspecified and each other; high behavior alone is insufficient. A middle rule is a concrete instruction, not a numeric midpoint. Merely satisfying coverage, echoing a rule, being verbose, or sharing a category between indistinguishable endpoints is insufficient. Do not invent a numeric pass percentage. If a task fails to elicit an anchor, record it as not elicited and preserve the failure; resolve it through a separately versioned prospective study, not a retrospective reinterpretation.
5. Before any proposed limited alpha acceptance, freeze and execute a **separate later continuity protocol** with independent repeats, same-context changed-evidence and authority-pressure rounds, and fresh-session reload comparisons for the intended released scope. State the required cases/conditions/coverage and decision rule before running it. The 50-response diagnostic supplies no such observations. Until that protocol exists and its requirements are met, continuity and alpha acceptance remain blocked.
6. Also complete the real-owner E2E requirement below, independent review and a new coordinator decision on the exact candidate artifacts and permitted claims. A diagnostic result cannot authorize merge, release, tag or external publication. Those remain separate later decisions under the existing release requirements. GitHub documentation is the marketing scope; no standalone website is part of this proposal.

This proposal narrows what a future alpha might claim; it does not lower the old gate in place. Even a favorable diagnostic would support only bounded observations for the tested literal instructions, tasks, model and settings. It cannot establish BFAS construct implementation, psychometric validity, general reliability, cross-model portability, real-person profiling, experienced emotion or broad real-user readiness. B01/B02 remain expression controls regardless of later diagnostic outcomes.

## Additional authentic owner E2E requirement

Current status: **NOT RUN.** The owner must actually participate; a developer-written quote, fixture, model role-play, structural test or hash is not owner consent. Use [WORKFLOW.md](WORKFLOW.md) and retain a minimal, authorized record showing:

- A real choice or short free-text request for desired fictional agent behavior, faithfully assigned answer IDs; no inference about the person's own traits.
- Explicit approval of the specific mapping version, anchor, exact rule and boundary, followed by presentation of the complete preview revision and a separate authentic confirmation bound to that revision.
- Manual review and final artifact preserving the entire confirmed snapshot; changes create a new revision and invalidate confirmation immediately.
- An actual owner-requested change, a full new preview, and an actual new confirmation; an old approval or “continue” does not substitute.
- A fresh session reading the saved final artifact and its referenced exact mapping dependencies, checking identity and preserving unspecified fields, approved rules, answers, conflicts, boundaries and approval records. Fresh-session behavior observations additionally belong to the separate continuity protocol.

Record the exact presented snapshots, genuine confirmation references, review outcome, relevant file identities and limitations. Collect only necessary design evidence; do not publish private confirmation records without authorization. Missing, denied, stale or ambiguous approval leaves a draft and a concrete blocker. No actual owner approval is claimed or requested as a side effect of authoring these documents.

## Reviewable outcomes

The coordinator may reject this proposal, request a new prospective version, or later accept a narrowly scoped evidence statement after all separately required work. Record each decision and its exact artifact identity. A no-contrast mapping stays proposed/unverified; it cannot support a claim that all revised mappings work. Scope exclusions must be explicit before a later release decision, with negative evidence visible. No partial result silently turns the 50 responses into the original 400-response gate.
