# Stopped-run verification — 2026-10-22

Execution base: `fb376222dc73faa366546a034bc7437b294b17d9`. The delivery PR identifies the final results commit. The [result report](REPORT.md), [call ledger](call-ledger.json), [terminal report](terminal-report.json), and separate [post-run review](RESULTS_REVIEW.md) distinguish actual diagnostic observations from static fixtures and review work.

The frozen manifest remains SHA-256 `d90178dc49665fe46f2c61dc291c73f27a4f16cf4d2e3524c468c3b5197a3198`. All 115 frozen inputs and 8 external dependencies verify; all 120 triage files tracked at the execution base retain their bytes. All 541 older evidence/source/validation files also remain unchanged. No mapping, task, rubric, request, scoring rule or stop criterion was edited.

## Actual evidence checks

- One generation reservation, one raw response, two judge packet reservations/calls and two failed judge outcomes exist. There are no replacements. The 17 remaining generator cells and their 34 judge slots are NOT RUN.
- The raw generator response has 9 words under the frozen whole-response `str.split()` rule; no budget failure occurred.
- Each original judge response parses as JSON and contains 13 `quote: null` observations. Both original candidates reproduce the frozen `invalid anchored observation` rejection. The preserved originals and failed-attempt wrappers retain identical raw text and metadata; no null-to-string repair or rerating occurred.
- Both original attempt outcomes are hash-locked. Terminal reveal exactly reproduces [terminal-report.json](terminal-report.json), reports the attempted opaque ID as inconclusive and emits no condition join or accepted rating for it.
- `reserve` after termination rejects with `STOP: study terminated; no more attempts`, without creating another reservation.
- Requested model/effort/fork parameters and distinct returned canonical task identities are retained. Backend identity/version, sampling settings, provider thread/turn IDs and internal tool traces were not exposed; these limits are recorded rather than inferred.

The original rating-shaped records under `records/*invalid-original.json` are archives of actual returned judge text and its parsed JSON, not accepted ratings. The failed wrappers under `ratings/` encode the observed validation outcome while retaining that text. The original lock and terminal ledger preserve their failure status.

## Reproducible read-only checks

From the repository root:

```sh
python3 evaluation/core-triage-v1/triage.py verify
python3 evaluation/core-triage-v1/triage.py validate-output req_259d3a551dbfe17bbfa8f342
python3 evaluation/core-triage-v1/triage.py reveal
python3 -m unittest core.test_compiler core.test_cli core.test_envelope -q
python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q
python3 -m unittest discover -s validation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q
python3 evaluation/diagnostic-v2/validate_design.py verify
python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete
python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22
git diff --check
```

The five named suites pass **148 software tests** (48 + 23 + 32 + 24 + 21). These include synthetic temporary integrity fixtures; they are not additional diagnostic calls or empirical samples. The old 50-output design remains NOT RUN and its freeze verifies. Repository Markdown/llms relative file targets resolve; remote URLs and fragments are excluded from that link check. Final delivery reruns these checks at the exact results commit.

No accepted semantic score, operation contrast, reliability estimate, owner confirmation, psychological validity or release acceptance follows from this stopped prefix. The next decision is a prospective, separately versioned judge-packet/schema alignment review; no new study or repair is performed here.
