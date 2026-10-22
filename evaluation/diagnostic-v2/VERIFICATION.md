# Core v2 design verification — 2026-10-22

This record reports **static design verification, not an experiment**. The branch starts at `9aa9ff2534c4d1593f07386ad8b99250ea25e72c`. No new generator output, experimental judge rating, owner confirmation or fresh-reuse observation was created.

## Frozen design identity

The one-time `prepare` command completed, followed by `verify`. The freeze contains 61 input/control files: the mapping cards, workflow and acceptance proposal, diagnostic plan and design, validator/tests, manifest/order and 50 exact input packets. The freeze file's SHA-256 is:

```text
e3c7bd044cf7927a26fea97aaf6aa25106ba49b64c2bd519496b892ee5c46d8a
```

The external identity above binds [frozen-hashes.json](frozen-hashes.json); the file does not hash itself. Review and verification reports are deliberately outside the prospective input set. The final PR commit supplies the full reviewable repository identity. Any future change to frozen inputs requires a new prospective version, not replacement of these hashes.

## Executed checks

Commands were executed from the repository root on 2026-10-22; the final new-suite run completed at approximately 10:41 UTC.

| Command | Actual result |
| --- | --- |
| `python3 -m unittest discover -s validation -p 'test_*.py' -v` | 32 original contract tests passed. |
| `python3 -m unittest discover -s evaluation -p 'test_*.py' -v` | 24 original pilot integrity tests passed. |
| `python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -v` | 21 new design tests passed after final freeze. |
| `python3 evaluation/diagnostic-v2/validate_design.py prepare` | Prepared once; 50 planned fresh slots, two planned judges, zero outputs, no owner confirmation. Do not rerun preparation on this directory. |
| `python3 evaluation/diagnostic-v2/validate_design.py verify` | All 61 frozen file hashes and 470 protected v1 files verified; exact packet rendering and allocation verified. |
| `python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete` | Existing v1 input/output/receipt integrity passed. |
| `python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22` | Existing locked v1 ratings passed structural integrity checks. |
| `git diff --check` | Passed. |

The original 56 tests were run during this increment and their unchanged files were subsequently verified against the baseline; the final new suite was rerun after its fixes. A local Markdown target-existence check covered 168 links in the changed documentation and design files with no missing target. This is not a remote-link or full anchor-rendering test.

New negative tests reject missing/duplicated cells, reused planned context slots, nonfocal constraints, invented receipts, false execution/confirmation/release states, mismatched mapping versions, rubric references absent from the literal clauses, invented absence bans, additional task requirements, missing ambiguity/count/stop declarations, shared judge paths, unblinded declarations, changed order or packet text, duplicate JSON keys, path traversal, changed/added/deleted frozen inputs and unexpected evidence files. Real baseline-copy tests also reject mutation, addition and deletion of protected v1 files. Synthetic temporary fixtures used by tests are not model observations.

## Review and scope

See the separate [independent review](INDEPENDENT_REVIEW.md) for semantic and methodological inspection. Static IDs and hashes cannot prove that a criterion faithfully interprets language, a future context is fresh, judges are independent, a model is the advertised backend, or an owner genuinely confirmed a preview.

No website directory is present on this branch. The latest scope correction limits marketing to GitHub documentation; PR #3 is excluded, and no Site action belongs to this increment. Existing v1 frozen inputs, raw outputs, ratings, reports and failures remain unchanged.

## Gates still unresolved

- Coordinator acceptance of the new mappings and prospective acceptance proposal.
- Actual 50-slot diagnostic collection and two independently locked blind reviews: **NOT RUN**.
- Full v2 preview-contract implementation/validation: proposed Markdown workflow only; the design validator does not validate final owner specs.
- Genuine choice/short-answer interview, complete owner preview confirmation, amendment/reconfirmation and fresh reuse: **NOT RUN**.
- A separately specified continuity protocol and its actual evidence; the existing 400-response protocol remains incomplete.
- Product release acceptance and release packaging: **BLOCKED / NOT PERFORMED**.

No test count or design freeze completes those gates. No main merge, release, tag change, paid API or new service was performed.
