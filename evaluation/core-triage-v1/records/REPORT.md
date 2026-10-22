# Core triage v1 — stopped prefix, inconclusive

The separately authorized diagnostic stopped on its first cell after **three diagnostic calls: one generator and two independent judge calls**. There are **zero accepted ratings** and no scored adherence or contrast result. This is a judge packet/schema interface failure, not a personality failure or evidence of an operation effect. The unreleased candidate remains behaviorally unvalidated; authentic owner E2E is **NOT RUN**.

This report describes the retained execution against baseline `fb376222dc73faa366546a034bc7437b294b17d9`. The [frozen protocol](../README.md), design, rubric, requests, and preparation reports retain their original bytes and prospective status. Their preparation-time “NOT RUN” language is not the current execution status; this report is the current result. No condition crosswalk is disclosed for the failed cell.

## Attempt accounting

| Item | Attempted | NOT RUN | Result |
| --- | --- | --- | --- |
| Generator cells (18 maximum) | 1 | 17 | One raw response retained; no scored result. |
| Judge calls (36 maximum) | 2 | 34 | Both original outcomes invalid; zero accepted ratings. |
| All diagnostic calls | 3 | 51 | Stopped; no repair, retry, replacement or further experimental calls. |

The attempted cell is `req_259d3a551dbfe17bbfa8f342`. Its complete [raw output](../outputs/req_259d3a551dbfe17bbfa8f342.json) is:

> There are eight scorecards in the eight welcome kits.

The frozen `str.split()` counter gives **9 words**, below the 250-word maximum. This was **not a word-budget failure**. No accepted semantic rating supports a task-quality, safety, literal-adherence or optional-contrast conclusion.

Both judges returned syntactically valid JSON, but each supplied **13 JSON null observation quote values**. The frozen validator requires string quotes and rejected each with the exact error `invalid anchored observation`. JSON parsing success did not establish schema validity. No null-to-string conversion, quote repair, rubric change, rerating or consensus replacement occurred. The original responses remain in [judge A original](req_259d3a551dbfe17bbfa8f342-a.invalid-original.json) and [judge B original](req_259d3a551dbfe17bbfa8f342-b.invalid-original.json). Their failure receipts are [judge A outcome](../ratings/req_259d3a551dbfe17bbfa8f342-a.json) and [judge B outcome](../ratings/req_259d3a551dbfe17bbfa8f342-b.json); the actual validator errors are in [judge-validation-errors.json](judge-validation-errors.json).

The [lock](../locks/req_259d3a551dbfe17bbfa8f342.json) retains both judge attempt outcomes and binds output, packets, failure receipts and reservation by hash. `both_judge_attempt_outcomes_retained: true` does not mean either rating succeeded. The [termination record](termination.json) stops all remaining cells. Terminal reveal classified the sole attempted opaque ID as `inconclusive: judge attempt error/missing/invalid` and exposed original receipts without a condition join. No trait, adherence or contrast positive is inferred from the rejected JSON.

All 17 remaining generator cells are **NOT RUN**; each also has two judge calls **NOT RUN** (34 total):

- `req_57f68112f863daa5d9e8f1a6`
- `req_3dfb50eb9c415d2b6a7b30fb`
- `req_09314e39fcf919f5cbcb87b1`
- `req_967d3f5b1f8ddce304178382`
- `req_cc85a6edf2b6b47feaffde0c`
- `req_7b6e7dcd185fd75809cae2e9`
- `req_db19e8aea26548f0625ec7ca`
- `req_12b8a3402e98aaa33f791e64`
- `req_e09de582d152a48e7de3506c`
- `req_8f84fadec986611ec57c9b95`
- `req_a03bb249a2de40f151e78951`
- `req_f22d1fc8501d03dfc314ba74`
- `req_9130a48e4c9eb1ee3f8db994`
- `req_e8fde78a84a536d326a19793`
- `req_2959668825e6c9e4ba28a3a1`
- `req_f33032616b42be7c0b64a0b7`
- `req_620840a7ff8a53101c6b050e`

## Model and observability limits

The generator request explicitly specified `gpt-6.1-sol`, reasoning `medium`, `fork_turns: none`. Each judge request explicitly specified `gpt-6-astra`, reasoning `high`, `fork_turns: none`. The two judges were separate fresh calls with only their own packet; they are same-model raters, not independent human raters. The tool accepted these explicit requests but returned canonical task names only. Actual backend model/version, sampling defaults, temperature, seed, provider thread IDs and turn IDs were unavailable. The retained canonical task names serve as the fresh-context identity surrogates allowed by the protocol; they are not provider context IDs.

Record timestamps are UTC capture timestamps, not provider generation timestamps. `observed_tool_calls: []` means no tool activity appeared in delivered messages. Internal traces were not exposed; neither tools-off enforcement nor sandbox isolation is established. Public protocol files permit coordinator condition inspection, and task/output content can enable inference; condition blinding is an operational judge instruction, not access control. Task/spec inputs are synthetic; the retained execution records contain actual delivered model responses, not handwritten answers or owner evidence. No private user conversation or authentic owner consent is published.

The [call ledger](call-ledger.json) records the three accepted tool calls, submitted payload hashes and metadata limitations. The [terminal report](terminal-report.json) preserves the frozen reporting command's output. Preparation and result-review work are separate from these three diagnostic calls.

Read [result verification](RESULTS_VERIFICATION.md) and the separate [post-run review](RESULTS_REVIEW.md) for integrity checks and their limits.

## Next bounded decision

Review a **separately versioned judge-packet/schema alignment proposal**, then independently review and freeze its exact instructions, examples, schema, validator behavior and stopping rules before any new study. The current frozen rubric and original outcomes must remain unchanged. This report authorizes no new collection and no retry of this cell.

The earlier 132-response proposal is unadopted, the old 50-response diagnostic is NOT RUN, and the unchanged original 400-response gate remains unmet. Middle settings, repetition, transfer, continuity, composition, cross-model reliability and authentic owner E2E remain untested. Three completed calls do not establish psychological validity, personality success or failure, release acceptance, or stability.
