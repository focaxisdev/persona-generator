# Independent prospective triage review

Reviewed 2026-10-22 against preparation baseline `6604bec9617a49d3cf6e4af852515b2a41aaca80`. This reviewer was separate from the design and implementation agents and changed only this report. The report is explicitly outside the frozen design inventory.

**Decision: APPROVE the exact draft below for the bounded static freeze. No unresolved blocking findings remain.** This decision is not permission to collect model responses, authentic owner consent, evidence of model behavior, release acceptance, or merge authorization.

Approved `draft-hashes.json` SHA-256:

```text
6ea7779970b0b8101d47368f269036221b1c27fbab6677f0bc74dd5de67b1e68
```

The draft binds the actual preparation files and external compiler/catalog/envelope dependencies. Approval applies to those exact bytes, not merely the baseline commit or a future edited design. The coordinator must perform the create-once freeze and verify it separately.

## Findings resolved during review

- The initial mutable lock reader trusted an empty file inventory, and rating locking did not independently rebuild a packet from its frozen task/rubric and exact output. The final implementation requires the exact lock inventory, verifies hashes, re-derives packets, and checks original raw judge JSON against the stored parsed rating. Forged empty locks, altered packets, changed outputs and changed locked ratings are rejected by static tests.
- Independent review/verification reports initially participated in the preparation snapshot. They are now explicitly excluded, so writing this report cannot alter frozen tasks, rules, requests or criteria.
- Judges now receive an explicit prohibition on tools, files, network and delegation. Receipt checks retain actual observed calls and reject judge tool use. This is an instruction and record protocol, not an enforced tool sandbox.
- An unclear invented-dependency observation could initially become favorable high-planning adherence, and partial/error output could receive ordinary completed-response labels. Uncertainty now remains unclear; partial/error/refusal and budget-invalid text retain original observations but are explicitly ineligible for completed-response evidence.
- A terminal report initially marked inadequate task output as contrast eligible. An independent temporary-fixture probe reproduced that issue. The corrected eligibility requires an opportunity case, both judges' clear task/content/facts/scope/safety/permission/leakage checks and determinate contrast observations. Nontrigger and override cases remain controls. The same independent probe now rejects contrast eligibility.

## Checks actually performed

| Check | Result |
| --- | --- |
| `python -m unittest core.test_compiler core.test_cli core.test_envelope -q` | 48 tests passed. |
| `python -m unittest discover -s validation -p 'test_*.py' -q` | 32 tests passed. |
| `python -m unittest discover -s evaluation -p 'test_*.py' -q` | 24 historical tooling tests passed. |
| `python -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q` | 21 frozen diagnostic tests passed. |
| `python -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q` | Final 23 tests passed, including synthetic temporary-directory execution-record and stopping tests. |
| `python evaluation/core-triage-v1/triage.py verify-draft` | Passed for the approved exact draft digest. |
| Independent examination of all 18 actual prepared payloads | Each message equaled fresh compiler CLI stdout, including its newline, inside the fixed wrapper with the exact separate task. Request argument keys and audit-label exclusion were checked. All six unspecified requests were byte-identical to their neutral construction with the same opaque ID. |
| Independent temporary-fixture attacks | Empty-lock terminal reveal, modified packet, and raw/parsed judge disagreement rejected. A null precontext error was retained, blocked the next attempt, and reported without fabricated ratings. The previously failing inadequate-task terminal-report probe now passes. |
| Historical file identity | All 541 baseline-tracked files under `evaluation/`, `persona-design-v0.2/` and `validation/` were byte-identical to the preparation baseline. |
| Historical verifiers | Frozen diagnostic verification, complete pilot verification, and original rating-integrity verification passed. Diagnostic generated outputs remained zero. |
| `git diff --check` | Passed. |

The named suites total **148 software tests**, not behavioral trials. Synthetic temporary records, approvals and ratings test bookkeeping only; they are not experimental observations, real reviewer identities or owner evidence. The actual triage directory had no `outputs`, `ratings`, `packets`, `locks` or `records` runtime directories at final review.

## Scope and design assessment

The prepared allocation contains exactly six tasks and eighteen requests: two operations, three settings, three task categories and one fresh context. Other operations/aspects and response detail remain unspecified. Neutral equivalence is a static check, not another response cell. Future generation requests use the actual exposed `collaboration.spawn_agent` arguments with `gpt-6.1-sol`, medium effort and `fork_turns='none'`. No role, temperature, seed, token-limit or tool-permission control is fabricated. The manifest allocation seed controls only local order.

The prospective judging mechanism uses two fresh `gpt-6-astra` high-effort calls per scorable output. Their packets contain the task, identical observable anchors and raw text; condition/operation/aspect labels, active instructions, allocation and coordinator crosswalk stay outside. The coordinator obtains condition mappings only after both original valid ratings are locked. Failed judge attempts and missing generation text stay visible without fabricated favorable ratings or revealed failed-cell conditions.

The reservation mechanism consumes one slot, prevents an uncertain pending attempt from silently becoming a retry, and checks prior locked results before dependent generation. Error, refusal, missing/partial output, tool use, safety, content, budget and uncertainty remain visible. The plan preserves literal adherence, optional contrast, controls, adequacy and budget as distinct assessments; partial overrides retain their remaining obligations. Low initiative does not forbid a recommendation. Overlap and baseline saturation remain inconclusive.

## Limits

Fresh forks omit parent turns but retain host instructions, tools and the shared filesystem. Hashes and declared receipts do not authenticate consent, truthful execution metadata, unseen tool activity or genuine independence against a malicious coordinator. Public audit files are accessible; blinding is an operational protocol, not access control. Static tests cannot establish semantic judge accuracy, generator adherence or safety.

Generation and judging calls for this preparation remain **zero**. Both operation behaviors and authentic owner E2E remain **NOT RUN**. The maximum prospective cost is 18 generation plus 36 judging calls, with earlier stopping possible. The original 400-response gate is unchanged; no automatic 132-response expansion, transfer/continuity evidence, psychometric validity, release, publication or merge follows from this review.
