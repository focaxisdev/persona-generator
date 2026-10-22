# Evidence verification — 2026-10-22

Executed in the selected workspace after collection, blind rating lock and receipt-validator repair. These checks establish recorded structural consistency, not provider authentication, psychological validity or release acceptance.

| Command/check | Observed result |
| --- | --- |
| `python3 -m unittest discover -s validation -p 'test_*.py' -q` | 32 passed |
| `python3 -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 passed; includes malformed new/stored receipts, frozen/raw mutations, rating schemas/quotes/lock and summary gate/joins |
| `python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete` | Passed: all 102 receipts and raw outputs, frozen input hashes, exact reload packets, message/model/context consistency |
| `python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22` | Passed: 102 items, 1,020 axes, 918 guardrails, exact response quotes, unchanged lock |
| Fresh temporary copy: remove only the copy's `analysis/`, run `summarize_pilot.py`, compare with committed tables/observations | Tables byte-identical; complete observation content equal after excluding newly generated timestamp |
| Independent recorded-call audit | 76 unique fresh context IDs, requested generator parameters accepted, 26 continuations in the same context; all original recorded completions precede first reload dispatch window |
| `git diff --check` | Passed |
| Relative Markdown link existence check | Passed: 867 local Markdown targets exist |
| Independent review | Original receipt attacks rejected after repair; actual evidence verification and 24 evaluation tests independently rerun successfully |

All synthetic tests use temporary fixtures. They are not extra model observations. The prospective freeze commit is `35b553e908bb41ce9701e8fbbc14a76a1474e71b`; the base protocol is `a11373472832a3ec46a27a870ed484b36eab6cb2`. Frozen inputs and rubric are unchanged. The final evidence commit is identified in the Draft PR and delivery record to avoid a self-referential commit hash in this file.

The [independent review](INDEPENDENT_REVIEW.md) separates resolved verifier defects from unresolved judgment uncertainty and behavior failures. All 28 locked budget violations and three unclear guardrails remain. The full behavior/release gate is **UNMET**; no authentic production preview confirmation, full-protocol coverage, coordinator acceptance, release or website deployment is implied.
