# Integration verification — 2026-10-22

This record concerns local software and document checks, not model behavior, genuine owner approval, or release acceptance. The candidate is based on exact PR #4 commit `8e55a4046b5fdc8870a4a16ad2b5f46e984afa54`. The delivery PR identifies the exact final commit; these commands must also pass against that head. See the separate [independent review](INDEPENDENT_REVIEW.md).

## Executed checks

From the repository root, using Python 3 and its standard library:

| Command | Observed result |
| --- | --- |
| `python3 -m unittest core.test_compiler core.test_cli -q` | 40 tests passed; new contract and actual CLI checks. |
| `python3 -m unittest discover -s validation -p 'test_*.py' -q` | 32 historical contract tests passed. |
| `python3 -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 historical pilot tooling tests passed. |
| `python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 frozen diagnostic design tests passed. |
| `python3 evaluation/diagnostic-v2/validate_design.py verify` | Structural design passed; zero generated outputs and no human confirmation. |
| `python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete` | Historical pilot manifest passed. |
| `python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22` | Historical rating integrity passed; no rerating performed. |
| `git diff --check` | Passed. |

The 117 tests comprise 40 new core tests and 77 historical tests rerun on this candidate. They are not 117 behavioral trials. The CLI suite actually validates, projects and renders both synthetic fixture pairs; compares with the public API; checks changed presentation bytes; and rejects invalid versions and malformed documents. Core tests cover fresh-process deterministic reload, canonical round trips, version and dependency binding, explicit control rules, stale confirmation, changed/deleted mappings, inactive data, unspecified/conflict cases and invalid input.

All 541 tracked files under `evaluation/`, `persona-design-v0.2/`, and `validation/` were byte-compared against the PR #4 baseline and remain identical. The v2 freeze manifest SHA-256 remains `e3c7bd044cf7927a26fea97aaf6aa25106ba49b64c2bd519496b892ee5c46d8a`; its verifier also checks 61 frozen hashes and 470 protected historical blobs. The frozen 50-output diagnostic was not executed.

A repository Markdown scan resolved relative file-link targets, excluding external URLs and in-page anchors, with no missing paths. This checks local navigation only: it is not an external-site availability, rendered UI, or anchor-validation claim. Publisher access limitations are recorded separately in [SOURCES](SOURCES.md).

## Remaining gates

The fixtures are handwritten synthetic input records, not model outputs or owner transcripts. Fresh Python subprocesses establish deterministic software reload only, not fresh model-context behavior. Authentic choice/short-answer confirmation, a real owner edit and reconfirmation, and model fresh reuse are **NOT RUN**. The two new operations are behaviorally **UNTESTED** and inherit no v1/v2 evidence.

The [private owner protocol](OWNER_TEST_PROTOCOL.md) and [prospective evidence plan](EVIDENCE_PLAN.md) require later review and execution. The 132-response proposal is bounded research planning, not an approved replacement for the unchanged 400-response gate. No release readiness, psychometric validity, general stability or cross-model reliability is established.
