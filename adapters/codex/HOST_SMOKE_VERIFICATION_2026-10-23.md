# Host-smoke follow-up verification — 2026-10-23

Source checkpoint: `64767190d605bb1d49c4b7a5b03b5c2dfd6d3e3f` on the existing PR #6 branch. This follow-up changes documentation and records one blocked native-host attempt; product code, fixtures, catalog and historical evidence remain unchanged.

The [smoke report](HOST_SMOKE_2026-10-23.md) separates successful disposable installation and manual synthetic loader preflight from the actual Codex process, which exited during app-server initialization. The [independent review](HOST_SMOKE_REVIEW_2026-10-23.md) checks the retained private first-attempt artifacts. No retry, model fallback or permission change occurred. A failed initialization is not a trait or adapter-behavior failure and does not establish host activation.

All **190 existing tests pass** on the follow-up tree: 14 profile + 9 adapter + 48 core/CLI/envelope + 23 legacy triage + 19 rating-contract repair + 32 validation + 24 pilot tooling + 21 historical diagnostic design. Reproducible commands:

```bash
python3 -m unittest profiles.test_profiles core.test_compiler core.test_cli core.test_envelope -q
python3 -m unittest discover -s adapters/codex -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q
python3 -m unittest discover -s validation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q
python3 evaluation/core-triage-v2/triage.py verify
```

All 767 protected files under `core/`, `evaluation/`, `persona-design-v0.2/`, `validation/` and `persona-pack-v0.1/` are byte-identical to the source checkpoint. The six-cell pause, reservations, raw responses, ratings and locks remain unchanged. The v2 freeze SHA-256 remains `eec76d8a00ff5f468dbf1930df40e5097a7c98e7a773d07dee83086343ac15f2`. Static test fixtures are not additional model responses.

Local Markdown/llms file-target checks and Git whitespace checks pass. Release acceptance now routes to the active profile contract and separates its ten settings from the legacy two-operation diagnostic. Independently selectable settings imply neither statistical independence, zero correlation nor a validated joint distribution. The original 400-response gate is unchanged and unmet.

Actual host discovery/application, automatic reload, child model loading, private genuine owner confirmation and behavioral stability remain unverified. The environmental initialization blocker must be resolved through a supported runtime before a separately authorized new host attempt; this report grants no retry or wider permissions. Raw traces stay outside the public repository; no account settings, main merge, release or website were changed.
