# Request-envelope and triage verification — 2026-10-22

This follow-up stays on PR #5, based on exact integration commit `6604bec9617a49d3cf6e4af852515b2a41aaca80`. The delivery PR records the final commit. This report is outside the frozen input inventory and cannot change requests or criteria. [Independent review](INDEPENDENT_REVIEW.md) records the separate review and exact approved draft hash; [frozen-hashes.json](frozen-hashes.json) binds the preparation files and external dependencies.

The create-once freeze completed after independent approval, followed by a successful read-only verification. Approved draft SHA-256: `6ea7779970b0b8101d47368f269036221b1c27fbab6677f0bc74dd5de67b1e68`. Final freeze manifest SHA-256: `d90178dc49665fe46f2c61dc291c73f27a4f16cf4d2e3524c468c3b5197a3198`.

## Static checks

Run from the repository root with Python 3 and its standard library:

| Command | Result |
| --- | --- |
| `python3 -m unittest core.test_compiler core.test_cli core.test_envelope -q` | 48 tests pass: 40 existing core/CLI and 8 new envelope tests. |
| `python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q` | 23 triage tests pass, including isolated CLI protocol tests and semantic reporting regressions. |
| `python3 -m unittest discover -s validation -p 'test_*.py' -q` | 32 historical contract tests pass. |
| `python3 -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 historical pilot tooling tests pass. |
| `python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 historical frozen-design tests pass. |
| `python3 evaluation/core-triage-v1/triage.py verify` | All 18 exact requests rederive from their source artifacts; six neutral/all-unspecified route comparisons are byte-identical. |
| `python3 evaluation/diagnostic-v2/validate_design.py verify` | Original 50-output design intact, zero outputs and no human confirmation. |
| `python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete` | Historical pilot manifest integrity passes. |
| `python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22` | Historical rating integrity passes; no rerating. |
| `git diff --check` | Pass. |

Total: **148 software tests**, including 31 new envelope/triage tests and the 117 previously existing tests rerun. These are not behavioral observations. Test execution records and rating-shaped records are explicitly synthetic integrity fixtures created only in temporary isolated repository copies; they are neither actual task answers nor empirical ratings.

Checks cover exact render CLI stdout and terminal newline preservation, identical product/evaluation builder use, metadata exclusion, neutral equivalence, frozen/dependency mutation, wrong condition/spec binding, pending reservations, errors/missingness/budget/tools, both original judge outcomes, edited packets/outputs/ratings, global context reuse, and terminal incomplete prefixes. Contrast eligibility regressions reject non-trigger/override controls and inadequate or unclear assessments rather than relabeling them successful contrasts. Eligibility itself is not a contrast finding.

All 541 baseline files under historical `evaluation/`, `persona-design-v0.2/`, and `validation/` are byte-identical to the integration base. Original compiler, catalog, fixture pairs, integration tests and earlier review/verification records remain unchanged. The v2 freeze manifest remains SHA-256 `e3c7bd044cf7927a26fea97aaf6aa25106ba49b64c2bd519496b892ee5c46d8a`.

Repository Markdown/llms relative file destinations are checked locally; remote URLs and fragments are excluded. The final delivery reports the exact scan count. All relevant tests, freeze checks and local links must be rerun against the final commit before delivery.

## What has not happened

This turn generated **zero experimental model responses and zero experimental judge ratings**. No runtime reservations, outputs, judge packets, ratings or locks were created in this study directory. The future ceiling is 18 generator attempts plus at most 36 judge calls, not 54 completed observations. Neither static fixture confirmations nor design-review approval is genuine owner approval.

Actual private owner intent, complete-preview confirmation, owner edits/reconfirmation and fresh reuse remain pending. Model behavior, middle settings, repetition, held-out transfer, continuity and composition remain NOT RUN. The 18-cell triage only detects gross problems; the 132-response coverage proposal is unadopted and the original 400-response gate is unchanged. No website work, merge, release, new paid API, or private transcript publication occurred.
