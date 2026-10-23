# Explicit-loading repair verification — 2026-10-23

Published runtime implementation commit: `1ef40d4365acb2dc2983beb740dce23421aac9ca`.
Its source tree is identical to the tested pre-execution local commit `520d203e1dddf626b6c4d5f05842dd19dc8c23ca`; the latter remains in the unchanged private plan.
The final documentation/evidence follow-up does not change those runtime bytes.
This record complements, and does not rewrite, the historical verification.

## Software checks actually executed

All commands ran with `PYTHONDONTWRITEBYTECODE=1` from the repository root:

```sh
python -m unittest profiles.test_profiles profiles.test_repair core.test_compiler core.test_cli core.test_envelope -q
python -m unittest discover -s adapters/codex -p 'test_*.py' -q
python -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q
python -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q
python -m unittest discover -s validation -p 'test_*.py' -q
python -m unittest discover -s evaluation -p 'test_*.py' -q
python -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q
python evaluation/core-triage-v2/triage.py verify
git diff --check
```

The seven suites passed **69 + 10 + 23 + 19 + 32 + 24 + 21 = 198 tests**.
Freeze verification passed with zero experimental calls. These are software
regressions; the paused six-cell study did not resume.

New checks cover exact v1 fixture/render compatibility; allowlisted v1/v2
catalog selection; changed Politeness meaning under a new ID; version-correct
conflicts; unknown/malformed IDs and pins; stale wording and catalog tampering;
missing/stale/malformed expectations; missing or corrupt current bindings;
rejection without rewriting; valid explicit child replacement; parent isolation;
and portable installed loading of both catalog versions. Local guard checks
are not owner authentication or concurrent transaction tests.

## Evidence classes

| Class | Result and limit |
| --- | --- |
| Unit / static | 198 passed; synthetic records only, no genuine consent |
| Installed local loader | Both catalogs revalidate through the installed package; no model needed for these tests |
| Actual explicitly guided parent | Installed skill read, own loader exit 0, exact stdout, one retained synthetic answer |
| Actual explicitly guided child | Fresh independent delegation; installed skill read, own loader exit 0, exact stdout, one retained answer |
| Native discovery | UNVERIFIED; old nested-CLI failure unchanged, no retry |
| Behavioral efficacy / stability / composition | UNVALIDATED; two integration answers are not a personality study |
| Genuine private owner journey | NOT RUN; synthetic receipts do not count |

The actual integration's source pin, task, digests and limits are in the
[separate execution record](EXPLICIT_LOADING_2026-10-23.md). Direct host steps
are evidenced by the live delegation/tool flow and retained per-agent execution
records. Backend provenance and a separately exported full platform-event
transcript were not available; local status JSON alone is not independent
attestation of a model service.

## Independent review and preservation

A separate reviewer inspected the implementation and final retained artifacts.
The reviewer independently ran 21 profile and 10 adapter tests, recomputed all
reported plan/request/stdout/answer digests, checked exact installed skill and
runtime bytes against the identical implementation source tree, and checked all 13 installed
files, eight store files and 68 old private-smoke files were unchanged. It found
no blocking issues. The 198-test full-suite run was performed separately by the
coordinator. The reviewer verified retained artifacts, not a direct replay of
the parent/child tool-event transcript; that distinction remains explicit.

The v1 catalog, four existing fixture JSON files, all old public smoke reports,
and protected core/evaluation/source/validation/Persona Pack files remain
unchanged. Historical failures, ratings, stopped/paused records and original
release gates remain intact. Raw integration records stay private and no owner
transcript or private execution policy is published.

Local Markdown/llms checks passed: 1,085 relative file targets across 385
documents resolve. Git whitespace checks passed. No merge, release, standalone website,
credentials, permissions, protected-state relocation or alternate executor is
part of this increment.
