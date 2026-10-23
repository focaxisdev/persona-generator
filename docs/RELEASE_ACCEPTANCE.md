# Release acceptance — two prospective tracks

**Unreleased; neither track authorizes merging, tagging, publishing or experiments.** The candidate is an installable, source-grounded desired-trait specification layer for an agent and optional subagents. It is not a scientifically validated personality system. Package version, profile schema, catalog version and individual hypothesis versions are distinct.

The original behavioral release gate remains **unmet and unwaived**. This document proposes a separately scoped **experimental package** decision for inspectable software with explicitly unvalidated AI mappings. Adopting that narrower distribution scope requires coordinator review of the exact candidate and an explicit release decision; it is not implied by passing tests. No prior failed or paused study is reclassified as successful.

## Track A: experimental package readiness (prospective)

Permitted package claim: users can author and inspect desired-trait specifications, preserve exact confirmed revisions, explicitly assign each agent, and invoke a local validated loader through repository guidance. Thirty rule anchors per catalog are engineering hypotheses. “Experimental” must remain prominent in README, release title and notes; it cannot disguise a claim of psychological validation.

| Gate | Acceptance evidence | Current state / remaining action |
| --- | --- | --- |
| A1 Scope decision | Exact version/tree and explicit acceptance of this experimental software scope, separate from scientific claims. | **PENDING coordinator decision**. Draft PR is not release authorization. |
| A2 Install and portable loading | Clean source-tree installation, no credentials/account changes, validated version-pinned loading, deterministic bytes, missing/tampered inputs rejected. | Existing installer/loader checks plus the current [readiness verification](RELEASE_READINESS_VERIFICATION.md); no native-discovery requirement. |
| A3 Optional onboarding | Choice questions **or** free text; skipped aspects remain unspecified; readable construct definitions, exact engineering rules, limits, complete preview and genuine confirmation. | [Owner guide](../profiles/ONBOARDING.md) prepared. **Genuine owner preference/spec confirmation PENDING**; synthetic receipts never satisfy it. |
| A4 Explicit assignments and recovery | Owner approves each intended agent ID/profile/revision; no implicit child inheritance. Review current binding before deliberate replacement or rollback; preserve old revisions. | [Assignment guide](../profiles/ASSIGNMENTS.md) and synthetic regression checks. **Genuine owner assignment confirmation PENDING**. Children are optional. |
| A5 Actual explicit host use | Host reads installed skill, invokes its own binding loader, then uses stdout for a separately bounded task; a participating child loads independently. | [One parent and one child](../adapters/codex/EXPLICIT_LOADING_2026-10-23.md) observed. Only Politeness was specified; this is loading evidence, not composition validity or real owner use. No new live run in this increment. |
| A6 Genuine owner reuse | Load the owner's actually approved profile and assignment in the declared supported path. | **PENDING**. Owner may accept the first complete preview unchanged. Reconfirmation is required only if content changes; no correction is manufactured. Test conditional edit paths with synthetic software tests. |
| A7 Distribution and review | Cumulative tree against main excludes website PR #3; affected/aggregate tests, local links, historical integrity and independent exact-candidate review pass. | Review [verification](RELEASE_READINESS_VERIFICATION.md); final adoption/merge/release decision remains separate. |
| A8 Claims and rights | GitHub README/Quickstart/examples explain sources, exclusions, experimental status, Apache-2.0 scope and third-party rights. | [Grounding](PSYCHOLOGY_GROUNDING.md), [claims](CLAIMS_MATRIX.md), [draft notes](RELEASE_NOTES_DRAFT.md). No full questionnaire or invented certification. |

For this owner's intended use, A3/A4/A6 stay open until real private evidence exists. The software can be installed without selecting a profile; that fact does not complete owner onboarding. An unconfigured-tool distribution before owner use would require a separate explicit scope decision, not a silent waiver of these open rows.

Automatic native skill discovery is optional for this explicit-loading product. The retained nested-CLI Error 30 attempt is still failed, its exact failing path unknown, and native discovery unverified. No retry or executor change is required by Track A. A host permission or policy denial remains a stop, not a reason to paste a replacement payload or widen access.

## Track B: scientific validation (unmet; no execution authorized)

Source-grounded names and definitions are not empirical evidence that an AI has human traits. The original [behavior protocol](../validation/BEHAVIOR_PROTOCOL.md), including its `10 × 5 × 2 × (3 rounds + reload) = 400` minimum, remains unchanged and incomplete. Those historical requirements are not satisfied by Track A, static tests, two explicit-loading answers, or a smaller diagnostic. Meeting a response count alone would not establish human psychometric validity either.

Any future scientific proposal must name the exact mapping versions and claims, prospectively align tasks/rubrics, separate adherence, discriminability, usefulness and safety, retain baseline/unspecified and non-trigger/override cases, assess transfer, repetition, composition and persistence, and retain every outcome and disagreement. Independently review the proposal before any collection. New hypotheses cannot inherit old ratings. This increment neither replaces the historical protocol nor adopts a new threshold.

| Preserved record | Status retained |
| --- | --- |
| [v1 pilot](../evaluation/pilot-2026-10-22/REPORT.md) | 102 outputs; 5/30 candidate contrasts, three limited-confidence; 28 word-budget violations. Not validation of the current profile catalog. |
| [Core triage v1](../evaluation/core-triage-v1/records/REPORT.md) | Stopped after one generator and two invalid judge outcomes; zero accepted ratings. |
| [Core triage v2](../evaluation/core-triage-v2/records/REPORT.md) | Paused at six answers (one carried, five new), twelve locked ratings, seventeen diagnostic calls. No remaining cell resumed. |
| [Frozen 50-response design](../persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md) | NOT RUN; no automatic execution. |
| [132-response proposal](../core/EVIDENCE_PLAN.md) | Unadopted, not a release gate. |

B01/B02 remain experimental expression proxies. Ten independently selectable settings do not establish ten implemented human psychological traits, statistical independence, stable model identity, feelings, cross-model reliability or human personality validity. Composition of serialized rules is implemented; behavioral composition validity is unverified.

## Next bounded decision

Review this exact experimental-package proposal and the current code/docs checkpoint. Then offer the owner the optional [choices OR free-text journey](../profiles/ONBOARDING.md), keep all actual preferences and assignment review private, present the complete spec, and wait for real confirmation. Do not require both input modes or an unnecessary edit. Only after remaining Track A gates and an explicit decision can merge/tag/release preparation proceed. Track B remains separately open.

Marketing is GitHub documentation only. The standalone website was a coordinator misunderstanding, not the user's requested deliverable. PR #3 and its private preview remain untouched, unmerged, unshared and excluded from the candidate. The released v0.1.0-alpha is not overwritten.
