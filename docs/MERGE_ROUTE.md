> **Historical pre-merge snapshot.** The original body below is preserved unchanged. For the approved source, merged changes, unpublished release and remaining blockers, read [current release status](RELEASE_STATUS.md). Do not repeat this snapshot’s merge or candidate-selection instructions.

# Reviewed merge route — instructions only

No retarget, merge, tag or publication has been executed. The source candidate is **v0.2.0-alpha UNCONFIGURED experimental**, not a scientifically validated persona. [Package acceptance](RELEASE_ACCEPTANCE.md) and explicit maintainer decisions govern any future action.

## Observed stack

Read-only GitHub inspection on 2026-10-23 found all listed PRs open, draft and unmerged. Main was `4b533cfb73ba26eb26e319770baa6ca6e776968a`.

| PR | Head checkpoint | Current base |
| --- | --- | --- |
| #1 | `a11373472832a3ec46a27a870ed484b36eab6cb2` | main |
| #2 | `9aa9ff2534c4d1593f07386ad8b99250ea25e72c` | #1 branch |
| #4 | `8e55a4046b5fdc8870a4a16ad2b5f46e984afa54` | #2 branch |
| #5 | `5d046289ff69f2c23e78a0130c1ed884a046c992` | #4 branch |
| #6 | Current exact reviewed candidate pinned in PR body/sidecar manifest | #5 branch |

Website #3 at `7085df87e38cba873ff32ab1efe042c34b4078b0` is a separate branch from #2. It is not an ancestor of #6 and its 19 `website/` paths are excluded. Do not merge #3 or alter/share its preview.

## Preferred economical route: cumulative PR #6 review

After explicit authorization, retarget #6 to main and review its **full cumulative** diff. This includes #1/#2/#4/#5 source and retained evidence, not just the profile increment. Confirm that main still matches the recorded base, required repository rules/checks are satisfied, and the candidate tree/archive match the reviewed hashes. Do not infer merge authorization from `mergeable: true`.

Use an ancestry-preserving merge commit if that is permitted by repository policy and explicitly selected. With unchanged main as an ancestor of the candidate, the resulting merge's source tree should equal the reviewed candidate tree. If there is any delta, conflict, required update or policy restriction, stop for review and re-run affected checks; do not bypass protections. Keep #1/#2/#4/#5 until a separately authorized disposition avoids duplicate work. Merging #6 into its **current #5 branch** alone does not put it on main.

## Alternative: merge the stack in order

After separate authorization, merge **#1 → #2 → #4 → #5 → #6**. After each predecessor reaches main, explicitly retarget the next PR to main and review its remaining delta, ancestry and checks. Do not assume GitHub automatically moves the next base. Prefer ancestry-preserving merge commits; squash/rebase rewrites ancestry and requires an explicitly reviewed new route and hashes, not blind continuation of this sequence.

## Final decision checklist

- [ ] Coordinator accepts the exact unconfigured scope, source commit/tree, archive/manifest checksums, changelog and draft notes.
- [ ] Maintainer selects and authorizes the route; current main and PR heads are read back before changes.
- [ ] Required branch protections, approvals and checks are identified and satisfied through permitted tools/UI. They have not been asserted absent or bypassed.
- [ ] Full cumulative main diff excludes website work and preserves scientific records; resulting main tree matches the reviewed tree or changed content is reviewed/retested.
- [ ] Only after separate authorization, choose the actual tag commit and create the new prerelease without overwriting v0.1.0-alpha.
- [ ] If the tag points to a new merge commit, rebuild and reverify the archive/manifest for that **commit** even if its tree matches: Git archive metadata and hashes can change. Attach only the newly verified files after publication authorization.

No hosted CI workflow/check result is implied by local tests. At the initial head `13e95a0383d1d498574c6aabb1767e7adfd67b23`, GitHub reported zero Actions runs, zero check runs and an empty status list (`pending` aggregate). Final-head status must be read again and included in PR coordination. Branch-rule visibility is distinct from CI status; maintainers must confirm required approvals before merging.

Personal owner confirmation, assignment and reuse remain unverified and **non-gating for unconfigured distribution**. Authentic full-spec and assignment confirmation are required before actual activation; fresh reuse/E2E may be evaluated afterward. The original scientific gate remains unmet and unwaived; no merge route or alpha label converts it into a pass.
