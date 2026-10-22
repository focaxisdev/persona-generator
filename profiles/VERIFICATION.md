# Profile increment verification

Base checkpoint: `5d046289ff69f2c23e78a0130c1ed884a046c992`. This increment contains no experimental model generation or judging. All owner choices, approvals and revisions used in tests are explicitly synthetic. See [independent review](INDEPENDENT_REVIEW.md) for separately performed contract and installation review.

## Executed local checks

The full existing 167-test suite and 23 new tests pass (190 total):

```bash
python3 -m unittest profiles.test_profiles -v
python3 -m unittest discover -s adapters/codex -p 'test_*.py' -v
python3 -m unittest core.test_compiler core.test_cli core.test_envelope -q
python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q
python3 -m unittest discover -s validation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q
```

The suites contain 14, 9, 48, 23, 19, 32, 24 and 21 tests respectively. Synthetic fixtures do not count as behavioral observations.

New checks exercise:

- Two distinct full ten-aspect combinations, including different anchors within a domain; all-unspecified rendering emits only invariants.
- Candidate approvals, exact preview/snapshot/presentation/effective digests, pinned sources/catalog and immutable revision publication.
- Public preconfirmation draft receipts: `NOT_CONFIRMED`, with no effective digest for unresolved inspected drafts; no automatic approval action.
- Parent/two-child explicit assignments, shared and different profiles, a new confirmed child revision, unchanged parent/sibling, and rejection of an unbound child.
- Exact-version rendering in separate local Python processes from a different working directory.
- Stored artifacts/bindings/source tamper rejection; wrong revisions, unknown values/fields, malformed JSON, duplicate keys, unsupported types, custom rules and path/symlink refusal.
- Real-catalog competing-anchor conflicts and manual cross-aspect blocking issues; no use until explicit recorded resolution and new full confirmation. Synthetic declared require/forbid checks are mechanical, not a natural-language semantic solver.
- Audit/issue text exclusion. Task/permission/tool fields cannot enter the profile, and repeated loads leave all stored bytes unchanged. Actual model obedience to overrides was not tested.
- Installation into disposable directories of the complete `.agents/skills/persona-profile` layout; explicit destination, no overwrite, pinned dependencies, no copied profiles, independent installed-loader execution and tamper refusal.

## Preservation and host boundary

All 767 existing files under `evaluation/`, `core/`, `persona-design-v0.2/`, `validation/` and `persona-pack-v0.1/` remain byte-identical to the base checkpoint. Old pilot output/rating integrity, the frozen 50-slot design and core triage verification pass. Core-triage-v2 remains paused after six locked cells with no new reservation or model call; its freeze SHA-256 remains `eec76d8a00ff5f468dbf1930df40e5097a7c98e7a773d07dee83086343ac15f2`.

The local Codex binary reports `codex-cli 0.163.0`; only `--version` and help were inspected. Its version invocation reported inability to create PATH aliases on a read-only path; no permission change was attempted or needed for local Python installation tests. The official skill/instruction references were checked on 2026-10-22 and are linked in the [adapter guide](../adapters/codex/README.md). No live Codex session, model behavior trial, owner-account installation, account setting, credential or paid service was used. Repository-local file layout and loader execution are tested; actual Codex skill discovery, prompt activation, automatic reload and child behavior are **not tested**.

Local Markdown/llms relative file targets and Git whitespace checks pass. External websites are not part of the local link check. Installation and artifact persistence are engineering results only. They do not establish genuine owner consent, stable psychological personality, reliability, cross-model portability, composition effects or release readiness.

## Remaining acceptance

The implemented acceptance slice is in [PROJECT_PURPOSE](../PROJECT_PURPOSE.md). Real private owner choice/short-answer journeys, revisions/reconfirmation, actual host loading and separately reviewed prospective behavior/combination/persistence studies remain pending. The original release gate is unchanged. No automatic study, merge, release or website action follows.
