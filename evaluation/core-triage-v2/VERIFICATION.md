# Rating-contract repair verification — 2026-10-22

Baseline: `511517e616f7cb6e908a70ca41e4ee92a8b8d222`. The delivery PR records the exact final commit and rerun results. This document is outside the frozen input inventory and cannot change the contract, tasks, stop rules or call budget.

Independent [targeted review](INDEPENDENT_REVIEW.md) approved draft SHA-256 `2b7686d577689be737225be4816494e680c9ebdc4849a933d5e1533916e127cd` before local freeze. The resulting [freeze manifest](frozen-hashes.json) SHA-256 is **`eec76d8a00ff5f468dbf1930df40e5097a7c98e7a773d07dee83086343ac15f2`**. Verification succeeds after freeze. Preparation made **zero experimental generator or judge calls**, and the actual v2 tree has no runtime output, rating, packet, lock or reservation directories. No carried import was performed.

The implementation and independent reviewer each ran all **19 v2 tests** successfully, including actual packet/schema/examples, strict raw JSON, quote/value/type negatives, original-rating rejection, source drift, context reuse, pending attempts, two-judge locks, stop/terminal provenance and a full 18-cell synthetic flow in temporary directories. The installed JSON Schema checker ran the golden schema matrix; it was not skipped. It adds no runtime dependency. The independent review also checked the schema metaschema and additional adversarial cases. An inherited Markdown-fence parsing mismatch was found, corrected only at the v2 rating-record entry point, and retested before approval.

The other relevant suites passed on the unchanged core/historical implementation: 48 core/CLI/envelope, 23 v1 triage, 32 historical validation, 24 pilot tooling and 21 frozen diagnostic tests. Together these are **167 software tests**, not 167 model responses. Synthetic receipts, confirmations, ratings and temporary review records are explicitly test fixtures, not owner actions, live ratings or empirical evidence. Final delivery reruns the six suites below on the exact committed head.

```sh
python3 -m unittest core.test_compiler core.test_cli core.test_envelope -q
python3 -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -q
python3 -m unittest discover -s validation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation -p 'test_*.py' -q
python3 -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -q
python3 evaluation/core-triage-v2/triage.py verify
python3 evaluation/core-triage-v2/diagnose.py
python3 evaluation/core-triage-v1/triage.py verify
python3 evaluation/core-triage-v1/triage.py reveal
python3 evaluation/diagnostic-v2/validate_design.py verify
python3 evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete
python3 evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22
git diff --check
```

The collect-all historical diagnosis reports exactly 13 original quote-type failures per judge (three false and ten not applicable), with no additional masked checks failing. It never accepts or repairs those records. V1 remains stopped with one actual generator response, two invalid judge outcomes and zero accepted ratings. Its original terminal report reproduces unchanged.

All 136 tracked v1 files, including its 120 preparation files and all raw records, locks, STOP and reports, retain their baseline bytes. The older 541 evidence/source/validation files remain unchanged. Compiler, catalog, generator envelope, tasks, conditions and behavioral rubric meanings are unchanged. The new freeze pins the whole v1 tree and original core dependencies; the pristine source verifier rederives the original 18 requests through the real renderer. Final delivery checks local Markdown/llms file targets (excluding remote URLs and fragments), historical bytes, freeze hashes and clean Git state.

Only a later separate execution decision can activate the [prospective plan](PLAN.md): one disclosed exact carried observation, at most 17 new generator calls and 36 new judge calls (53 new calls maximum). The prior three calls remain historical and outside those new-call counts. All 18 observations would require new-contract judging; old invalid ratings never count. The contract was designed after seeing the stopped prefix, so this is not an unseen replication. No release gate, owner confirmation, behavioral validity or execution approval follows from this verification.
