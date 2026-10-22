# Independent post-run evidence review

Reviewed 2026-10-22 against run base `fb376222dc73faa366546a034bc7437b294b17d9`. This reviewer is separate from the generator, both experimental judges, and the results-document author. This is post-run artifact review, outside the three diagnostic calls. It supplies no experimental rating, owner approval, behavioral acceptance, release approval, or authorization for further collection. Only this report was written by this reviewer; frozen inputs and runtime evidence were not edited.

## Finding

No blocking inconsistency was found between the retained evidence, [REPORT.md](REPORT.md), and the ten updated current-status documents. The supported conclusion is a stopped, inconclusive prefix: **one generator call, two schema-invalid judge outcomes, zero accepted ratings, 17 generator cells and 34 judge slots NOT RUN**. The rejected observations cannot establish semantic safety, task adequacy, adherence, contrast, an operation effect, or personality success/failure.

The nine-word raw generator response is retained exactly. The mechanical word count is below 250; the stop is not a budget failure. Both original judge texts parse as JSON, but each contains 13 `quote: null` values. Frozen `triage.py` requires `type(item['quote']) is str` in `rating_record`; its exact rejection is `invalid anchored observation`.

The judge packet asks for observation objects with `id,value,quote` and exact evidence for true values, but does not expressly state the string-only representation for absence. The frozen design separately says an empty quote means absence. This supports describing the incident as a packet/schema interface failure and proposing prospective alignment. It does not establish a causal explanation for either model response or license accepting the rejected observations.

## Evidence checks

- Each archived `*.invalid-original.json` contains a parsed candidate equal to parsing its original raw text. Its raw text and metadata equal the corresponding invalid failure wrapper. The completion payload nested in each receipt equals the retained raw text. Both wrappers preserve `status: invalid`, the actual schema error, and the absence of correction/retry/replacement.
- Read-only, in-memory substitution of each archived candidate into the unchanged frozen validator reproduced `invalid anchored observation`. No candidate field was repaired and no rating was reevaluated semantically. Ordinary validation of the retained failure wrappers returns `rating: null`.
- The lock's exact inventory and all six file digests verify: output, two packets, two failed outcomes, and reservation. The archival originals and validator-error file remain separate retained evidence; the lock does not falsely claim to bind those additional files.
- The call ledger's payload-file, canonical-argument and message SHA-256 values match the actual files. Generator parameters are `gpt-6.1-sol` / `medium` / `fork_turns: none`; both judge parameters are `gpt-6-astra` / `high` / `fork_turns: none`.
- The three canonical returned task names are distinct and agree with the result metadata and receipt captures. These names are context-identity surrogates, not independently exposed provider thread IDs. The receipts do not attest submitted hashes or actual backend model/version. Sampling values, temperature, model sampling seed, provider thread/turn IDs and backend identity are unavailable, not fabricated. The fixed allocation seed in the manifest is a separate local ordering control.
- Empty observed-tool lists describe delivered-message observation only. Hidden traces were unavailable; no tools-off or enforced-sandbox conclusion follows. Fresh-fork requests and packet instructions do not remove inherited host instructions, tools or workspace access.
- The frozen terminal-report function reproduces [terminal-report.json](terminal-report.json) exactly as parsed JSON. Its sole result row has only the opaque ID, inconclusive status and original judge-attempt records; no condition, case, applicability, adherence or contrast fields are joined. Its termination suffix contains all 17 remaining opaque IDs in the frozen order.
- Actual runtime inventory is one output, two packets, two failed rating wrappers, one lock and one reservation. There are no remaining-cell outputs or ratings in the retained run. No retry, repair or replacement is represented in the ledger. This artifact review cannot independently attest unexposed provider history.

## Integrity and local verification

The freeze-manifest SHA-256 remains `d90178dc49665fe46f2c61dc291c73f27a4f16cf4d2e3524c468c3b5197a3198`. Frozen verification checked all **115 input files and 8 dependencies**, rederived all 18 real-envelope requests, and retained neutral/all-unspecified equality. All **120 tracked triage files** from the run base remain byte-identical, including prospective preparation and review reports. All **541 historical tracked files** under `evaluation/`, `persona-design-v0.2/` and `validation/` remain byte-identical to integration base `6604bec9617a49d3cf6e4af852515b2a41aaca80`.

The reviewer independently ran these suites with `PYTHONDONTWRITEBYTECODE=1`; all passed. Tests use their existing isolated temporary fixtures and do not constitute new experimental calls.

| Command | Actual result |
| --- | --- |
| `python3 -m unittest core.test_compiler core.test_cli core.test_envelope -q` | 48 tests passed |
| `python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q` | 23 tests passed |
| `python3 -m unittest discover -s validation -p 'test_*.py' -q` | 32 tests passed |
| `python3 -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 tests passed |
| `python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 tests passed |

Additional read-only checks invoked the frozen verification, output-record, locked-record and terminal-report functions, compared archived candidates and receipts, recalculated hashes, checked runtime counts and compared historical bytes with Git objects. Their results are reported above; no reserve, packet, freeze, lock, termination or repair operation was performed by this reviewer.

## Claims and next decision

The final result report and current English/Chinese README, AI discovery guide, core README, evidence plan, claims matrix, release acceptance, draft release notes, Quickstart and `llms.txt` correctly distinguish attempted collection from accepted behavioral evidence. The frozen preparation-time NOT RUN statements remain historical and are explicitly contextualized by the current result report. Authentic owner E2E remains NOT RUN; no private owner transcript or policy is introduced by these changes. The original 400-response gate remains unchanged and unmet; the older 50-response diagnostic remains NOT RUN and the 132-response proposal remains unadopted.

The next bounded decision is whether to commission a separately versioned judge-packet/schema alignment proposal, independently reviewed and frozen before any new study. This review does not authorize editing the present freeze, converting null quotes, accepting the invalid ratings, rerunning this cell, or starting another study automatically.
