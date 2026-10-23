# Release status — observed 2026-10-23

This is a dated checkpoint, not a live status feed. **v0.2.0-alpha publication was explicitly approved for the exact source below, but has not happened.** No v0.2 tag or release was visible; only v0.1.0-alpha was visible. Approval and actual publication are separate.

## Exact checkpoints

| Checkpoint | Source commit | Git tree | Observed status |
| --- | --- | --- | --- |
| Approved v0.2.0-alpha source | [`290ede4760f03048ddb8fcc4d613509cc573cb80`](https://github.com/focaxisdev/persona-generator/commit/290ede4760f03048ddb8fcc4d613509cc573cb80) | `79eb58c33a3373e462c1e4a126f88dee6cfa453c` | PR [#6](https://github.com/focaxisdev/persona-generator/pull/6) merged; exact candidate and publication approved; unpublished. |
| Current main | [`69abd2171ef818e3fdba58b041317c40dcb2cadb`](https://github.com/focaxisdev/persona-generator/commit/69abd2171ef818e3fdba58b041317c40dcb2cadb) | `9a2f0b1ae8d0ebc6c58f1477ebce278961c88564` | Includes merged PR [#7](https://github.com/focaxisdev/persona-generator/pull/7), the snapshot fix; differs from the approved alpha. |
| Install-manifest fix | [`fee0b2d919acbfc4912f1cd15b259be4e984ac0e`](https://github.com/focaxisdev/persona-generator/commit/fee0b2d919acbfc4912f1cd15b259be4e984ac0e) | `14cf37fed14134e2b6b1d99bdb9986440567fe36` | PR [#8](https://github.com/focaxisdev/persona-generator/pull/8) is Draft and unmerged; absent from main and the approved alpha. |

Local check totals belong to their exact checkpoints: **201** for the approved alpha, **204** for main above, and **207** for PR #8 above. These are local checks, not hosted CI results, scientific validation or private owner E2E. They are not interchangeable evidence for a later head.

## Publication blocker and remaining work

The last retained release attempt failed with exit code `1`: `Post …/releases: Forbidden`. No HTTP status, request ID or originating layer was retained, so the diagnostic does not establish whether GitHub, a proxy or another platform layer caused it. Publication remains blocked pending platform-log diagnosis. No further retry is authorized by this checkpoint; do not regenerate or substitute assets, move the approved commit, or treat main/PR #8 as the approved alpha.

PR #8 still needs review and a merge decision. This release-status documentation change also needs review. Neither review silently changes the approved v0.2 source or authorizes publication of another artifact. [Source packaging](SOURCE_PACKAGE.md) describes the pinned source and a generic reproducibility procedure; [acceptance](RELEASE_ACCEPTANCE.md) separates distribution from science. [Merge route](MERGE_ROUTE.md) and [draft notes](RELEASE_NOTES_DRAFT.md) are preserved pre-merge snapshots, not current action instructions.

The package remains **UNCONFIGURED experimental source**: no owner profile, store or binding is activated. Genuine private owner confirmation, assignment and fresh reuse/E2E remain unverified and non-gating for this distribution; authentic confirmation and assignment are required before activation. No private owner material belongs in this public status record.

Scientific work remains paused. The original scientific gate is **unmet and unwaived**; no gate or standard changed. Local software checks, approval and an eventual alpha publication cannot establish behavioral composition, stable model identity or human psychometric validity. No experiment, website work or model run resumes from this document.
