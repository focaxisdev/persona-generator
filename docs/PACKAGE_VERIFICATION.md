# UNCONFIGURED source-package verification — 2026-10-23

This release-packaging increment starts at `13e95a0383d1d498574c6aabb1767e7adfd67b23`. It prepares **v0.2.0-alpha UNCONFIGURED experimental source**, not a configured persona or scientific acceptance. The exact final commit/tree, external archive/manifest hashes and post-commit readback are pinned in Draft PR #6. Those external artifacts are not part of their own source hash domain.

## Python requirement and executed checks

Runtime dictionary union in `profiles/compiler.py` requires Python 3.9+. Source inspection and Python 3.9 grammar parsing of the shipped entrypoint/runtime files found no higher requirement. Actual execution used **CPython 3.12.14**, not Python 3.9. Installer, installed launcher and `python -m profiles` check the reported version before normal work. Very old interpreters may reject syntax before reaching the guard; no universal older-interpreter exit-code claim is made.

The new guard test simulates 3.8 rejection and the 3.9 acceptance boundary using the current interpreter. It checks an untouched installation target, empty loader output and no compiler/installation work. This tests branching, not execution compatibility with those Python versions.

All **201 local tests passed**. Commands use `PYTHONDONTWRITEBYTECODE=1` from the source root:

| Command | Passed |
| --- | ---: |
| `python -m unittest profiles.test_profiles profiles.test_repair profiles.test_assignment_journey core.test_compiler core.test_cli core.test_envelope -q` | 71 |
| `python -m unittest discover -s adapters/codex -p 'test_*.py' -q` | 11 |
| `python -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q` | 23 |
| `python -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q` | 19 |
| `python -m unittest discover -s validation -p 'test_*.py' -q` | 32 |
| `python -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 |
| `python -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 |

Frozen-triage integrity verification (`python evaluation/core-triage-v2/triage.py verify`) and Git whitespace checks passed with zero model calls. Local Markdown/navigation file-target checks passed; this does not promise exhaustive external URL or heading validation.

## Source package, installation and attribution

Using Git 2.52.0, the staged source package preflight verified all 856 tracked files and their executable classification against Git blobs, with no extra/missing files, symlinks, submodules or archive path escapes. Repeated archives were byte-identical. Independent artifact review then found Git’s default tar umask yielded group-writable regular-file permissions (0664), although payloads and executable classification matched. That first archive is retained unchanged outside Git. Packaging now explicitly uses `git -c tar.umask=0022 archive`, and the final check additionally requires exact regular-file permission bits 0644/0755. It rebuilds from the corrected committed revision and records both commit and tree in the external manifest. [Packaging instructions](SOURCE_PACKAGE.md) define the artifact boundaries and reproduction steps.

The extracted package's installer created only 13 allowlisted skill/runtime files in a disposable repository. It installed no profile fixture, active store or binding. Attempting to render an unconfigured agent failed with empty stdout and did not create a store. Separate synthetic checks then published two existing full-combination fixtures into a different disposable store, created three explicit bindings, and verified six fresh-process renders against their exact effective digests. A tampered binding and a second installation were rejected. All extracted source bytes and installed files remained intact.

These are local software checks, not actual host/model observations. The two earlier live answers used Politeness alone and establish loading, not composition validity. No new live answer, native-discovery test or nested-CLI retry occurred.

The full source retains Apache-2.0, the source ledger/registry, original construct paraphrases, third-party-rights notes, changelog and draft release notes. No complete research paper or questionnaire is added. Historical fixtures and authorized evidence remain inert. No private owner transcript, active assignment/store or private raw host trace is introduced.

## Cumulative tree and integrity

Compared with main `4b533cfb73ba26eb26e319770baa6ca6e776968a`, the candidate has **812 changed paths: 799 additions, 13 modifications, no deletions**. Of those, 719 paths are preserved evaluation evidence. Website #3 at `7085df87e38cba873ff32ab1efe042c34b4078b0` is not an ancestor, and all 19 website paths are absent. Original documentation SVG assets remain unchanged from main.

Against the starting head, **780 protected files** were checked unchanged: core, evaluation, frozen source/mappings, validation, Persona Pack, profile compiler/catalogs/old fixtures and historical adapter reports. Current install instructions, entrypoints and their tests are intentionally changed; historical smoke/readiness records are not rewritten. The original scientific 400 gate remains unmet and unwaived, the six-cell study remains paused, old 50 remains NOT RUN and 132 remains unadopted.

## Independent review and remaining decisions

A reviewer independent of implementation ran all 11 adapter tests and checked version guards, runtime API floor, unconfigured distribution boundaries, source/manifest design and stack route. Review found two documentation issues: pre-activation confirmation was conflated with later reuse, and unsupported-interpreter exit behavior was too broad. Both were corrected; the refusal test was also strengthened to assert an untouched installation target. Final readback and exact artifact verification are reported with the PR checkpoint.

Local tests are distinct from hosted CI. Read-only GitHub inspection at the starting head found no Actions runs, check runs or status entries; its empty aggregate `pending` is not a failed test or a CI pass. Final-head CI/check state is read again for coordination. Required branch protections/approvals must be confirmed by a maintainer; this record does not claim they are absent or bypass them.

Remaining distribution decisions: exact-artifact/coordinator acceptance, an explicitly authorized [merge route](MERGE_ROUTE.md), satisfaction of repository rules, and separate tag/prerelease authorization. **Personal E2E is unverified and non-gating for UNCONFIGURED distribution**. Authentic full-spec and assignment confirmation remain mandatory before later activation. Scientific validation remains unmet. No retarget, merge, tag, release, website or owner activation is performed here.
