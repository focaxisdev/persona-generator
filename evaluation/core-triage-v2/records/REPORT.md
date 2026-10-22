# Core triage v2 — paused for scope alignment

Current status: **PAUSED**, at the completed sixth-cell boundary. This administrative pause is not a frozen failure, STOP or termination. No seventh cell is reserved and no call is pending. The remaining 12 cells and at most 36 potential calls are unattempted; they are **not authorized to resume automatically**. See [PAUSE.json](PAUSE.json) and the [actual call ledger](call-ledger.json).

## Retained prefix and accounting

The run base is `246a1177d21b487edae97b111a6b3329e8706604`; the SHA-256 of `frozen-hashes.json` is `eec76d8a00ff5f468dbf1930df40e5097a7c98e7a773d07dee83086343ac15f2`. The last completed cell is `req_cc85a6edf2b6b47feaffde0c`. The six answers comprise one byte-identical carried v1 output record and five newly generated answers. The carried answer consumed zero new generator calls. Twelve fresh, schema-valid original judge ratings are retained across six locked cells. The actual diagnostic-call total is **17: five generators and twelve judges**. Historical v1 judge failures remain invalid and excluded from these new-call counts. The 17-call diagnostic sample count also excludes nonexperimental bookkeeping delegation to two execution coordinators and independent checkpoint review. Those administrative calls supplied neither sampled answers nor judge ratings; 17 is not a count of all model-tool invocations.

All six retained cells pass the unchanged frozen `prior_gate` checks. No retries, replacements or consensus judgments were introduced. No termination or reveal command was used for this pause; no condition crosswalk is disclosed here. The frozen preparation files remain unchanged. Their prospective **NOT RUN** wording describes the preparation stage, not this current paused execution status.

## Requested parameters and provenance limits

The five new generator calls requested and were accepted by the tool with `model=gpt-6.1-sol`, `reasoning_effort=medium`, `fork_turns=none`. The twelve fresh judge calls requested and were accepted with `model=gpt-6-astra`, `reasoning_effort=high`, `fork_turns=none`. The call ledger records each actual returned canonical task name, submitted payload hashes and capture metadata. The carried answer retains its original record rather than a new generation receipt.

Tool acceptance does not attest backend model identity. Backend model/version, sampling values, thread/turn identifiers and internal tool traces were unavailable. Distinct canonical task names with `fork_turns=none` are context surrogates. Tools-off and blindness instructions are an operational protocol, not enforced sandbox isolation. No sampled-model tool activity appeared in delivered messages; empty observed-tool lists do not prove that an inaccessible internal trace is empty. Hashes identify coordinator-submitted payload files, not server attestations. UTC timestamps are receipt-capture times, not provider generation times.

## Preserved disagreements

Both independent ratings, original raw text, quotes and notes remain separately retained. The following observation-value differences are preserved without adjudication; quote and note wording also varies in the original records.

| Opaque cell ID | Observable | Judge A | Judge B |
| --- | --- | --- | --- |
| `req_3dfb50eb9c415d2b6a7b30fb` | `ordered_checklist` | `false` | `not_applicable` |
| `req_3dfb50eb9c415d2b6a7b30fb` | `named_stages` | `false` | `not_applicable` |
| `req_3dfb50eb9c415d2b6a7b30fb` | `explicit_task_format_followed` | `not_applicable` | `true` |
| `req_967d3f5b1f8ddce304178382` | `adjustment_for_changed_conditions_or_explicit_none_needed` | `not_applicable` | `false` |
| `req_cc85a6edf2b6b47feaffde0c` | `explicit_task_format_followed` | `true` | `not_applicable` |

These differences do not trigger a frozen stop for the retained prefix. Schema and substring checks establish only mechanical acceptance, not semantic support or an operation effect.

## Scope and claim boundaries

The two current operations are limited diagnostics, not the intended final product scope. The intended product remains an installable, composable, psychology-grounded specification for agents and subagents. Persistence and composition remain unverified; this pause adds no architecture implementation.

The v2 rating contract was developed after viewing the carried answer and invalid original v1 ratings. New judging and continuation therefore do not constitute a wholly unseen study. This prefix supports no efficacy, psychological validity, reliability, stability, transfer, persistence, composition or release claim. Authentic owner E2E is **NOT RUN** and the original 400-response gate remains unmet. Candidate release status is unchanged.

Any resumption requires a separate explicit decision and the unchanged frozen gates. This report grants no further experimental calls or automatic expansion.
