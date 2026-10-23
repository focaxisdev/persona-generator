# Release-readiness verification — 2026-10-23

This record covers the owner-onboarding, assignment recovery and GitHub-documentation increment based on `ba3fbf5d624ea337499ac34b92d41dbb5b825155`. It adds no runtime mapping, model call, owner answer or scientific observation. The commit containing this record and Draft PR #6 pin the final candidate. See [prospective release acceptance](RELEASE_ACCEPTANCE.md).

## Software checks executed

All **200 tests passed**, including two new synthetic assignment-journey tests. These exercise parent-only use, optional children, catalog upgrade, deliberate child replacement, rollback to a retained revision, exact sibling/parent/store isolation, new-process rendering, stale expectations, missing revisions and tampering. Synthetic receipts remain labeled `synthetic_fixture`; they are not authentic owner decisions.

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`:

| Command | Passed |
| --- | ---: |
| `python -m unittest profiles.test_profiles profiles.test_repair profiles.test_assignment_journey core.test_compiler core.test_cli core.test_envelope -q` | 71 |
| `python -m unittest discover -s adapters/codex -p 'test_*.py' -q` | 10 |
| `python -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q` | 23 |
| `python -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q` | 19 |
| `python -m unittest discover -s validation -p 'test_*.py' -q` | 32 |
| `python -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 |
| `python -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 |

`python evaluation/core-triage-v2/triage.py verify` passed with zero calls. `git diff --check` passed. Local Markdown/llms file-target checks found no missing targets across 389 documents; this is not exhaustive remote URL or heading-anchor validation.

## Clean source-distribution check

A `git archive` of the staged candidate tree was extracted into a disposable directory. The unchanged installer created the 13-file local skill in a separate disposable repository. Its installed `run.py`, invoked from a third working directory, published the two existing full-combination synthetic fixtures and bound a parent plus two children explicitly. Six separate rendering processes (two per binding) reproduced the expected effective digests; the parent and first child matched, while the second child differed. A second installation was rejected without overwriting. No host model, native discovery, account setting or genuine owner confirmation was involved.

Reproduce with a clean archive of the reviewed commit, the [installer](../adapters/codex/README.md), the [synthetic profile commands](../profiles/README.md), and [assignment tests](../profiles/test_assignment_journey.py). Keep all stores and installations disposable; do not install fictional preferences into real agents. All allowlisted runtime and fixture bytes are unchanged from the base commit above.

The installed-file manifest uses SHA-256 of UTF-8 canonical JSON mapping relative file paths to their byte SHA-256, sorted keys with separators `(',', ':')`:

- Installed manifest: `99bb78b55841a544cbcad24fe8c96b90f795d5cf75c9f01068def8178d0deaa5`.
- Synthetic combination A effective payload: `00ee8e9f3c3922caceae601a524f9a42e0b25a086b2e6de86c45ba93089ecba0`.
- Synthetic combination B effective payload: `ef7882fc527d3949f1de21a2711afedec0ca0a412100026beb00e462c7d9fb95`.

## Cumulative candidate and historical integrity

Compared with main `4b533cfb73ba26eb26e319770baa6ca6e776968a`, the candidate contains 808 changed paths: 795 additions, 13 modifications and no deletions. Most additions are preserved evidence: 719 paths under `evaluation`. The rest cover sources/design, validation, core, profiles, adapter and GitHub documentation. This is the cumulative stacked candidate, not a claim that this increment newly implemented every path.

Website PR #3 head `7085df87e38cba873ff32ab1efe042c34b4078b0` is not an ancestor. All 19 `website/` paths introduced there are absent from this candidate. The two original `docs/assets/*.svg` files are unchanged from main; they are existing repository documentation assets. No website branch, preview or hosting action was performed.

A byte comparison against the base commit checked 782 protected files: `core/`, `evaluation/`, `persona-design-v0.2/`, `validation/`, `persona-pack-v0.1/`, old profile fixtures, both catalogs, the profile compiler and existing adapter Markdown records. All were unchanged. The original failed host smoke, explicit-loading reports, frozen studies, invalid ratings and paused six-cell records were not rewritten. No remaining study cell ran, no hidden retry occurred and no private owner transcript was added.

## Independent review

A reviewer separate from implementation inspected the new onboarding/assignment guides against the actual contract and CLI, the synthetic recovery tests, psychology definitions/rights and cumulative README/docs claims. The reviewer independently ran `python -m unittest profiles.test_assignment_journey -v` (2/2 passed), spot-checked the author paper and official IPIP source/provenance pages, and verified protected runtime/evidence paths unchanged. No blocking defect was found. This is a scoped code/documentation review, not a scientific acceptance or release authorization.

## Evidence classes and remaining gates

| Class | State |
| --- | --- |
| Local package and loader | Tested above; synthetic choices only. |
| Actual explicit host/child loading | Two **earlier** retained answers, both using Politeness alone with all other aspects unspecified; not rerun here. |
| Native automatic discovery | Optional and unverified. The failed nested-CLI initialization remains failed; exact failing path unknown. |
| Genuine owner preferences and full-spec confirmation | **PENDING**, privately obtained through questions OR free text, with skipping allowed. |
| Genuine assignments and owner fresh reuse | **PENDING**; children optional, assignment approval separate. No mandatory edit; reconfirm only if content changes. |
| Experimental-package scope and release decision | **PENDING** coordinator adoption, exact-candidate review and separate release authorization. |
| Scientific validation | Original gate **unmet and unwaived**. Composition validity, behavioral stability and human psychometric validity unestablished. |

Next: review the prospective package scope, then conduct the optional private owner journey and exact assignment confirmation. Do not resume paused studies, substitute software checks for scientific acceptance, or infer permission to merge or publish.
