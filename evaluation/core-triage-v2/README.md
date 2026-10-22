# Rating-contract v2 repair — prospective, NOT RUN

This separately versioned proposal repairs the judge packet/schema interface exposed by the stopped [v1 report](../core-triage-v1/records/REPORT.md). **Zero new experimental calls have occurred.** The create-once `frozen-hashes.json` file, when present, records freeze status and its exact independent review; preparation and freeze grant no collection authorization. V1 remains byte-identical, stopped and inconclusive: one generator, two invalid judge outcomes, zero accepted ratings.

The finite prospective scope is **one exact carried prior answer, at most 17 new generator attempts, and at most 36 fresh judge attempts (53 new calls maximum)**. The carried answer gets two new independent judges under the new contract. It is not regenerated. The old two judge calls are historical failures, excluded from new-call counts and never accepted as new evidence. Every original cell ID, order, task, condition, request, compiler, catalog, envelope, observable meaning and coordinator rule remains pinned to v1.

Read [diagnosis](DIAGNOSIS.md), [contract and semantic diff](CONTRACT.md), and [plan](PLAN.md). [rating-contract.json](rating-contract.json) is the single versioned source for the exact instructions, full JSON schema and unrelated synthetic examples inserted by the real packet builder. The schema is descriptive; the standard-library validator additionally checks packet binding, actual quote substrings, observable inventory, explanation lines and original raw-text equality. It does not infer semantic truth, absence, irrelevance or safety.

The small [adapter](triage.py) imports the unchanged v1 implementation into two isolated Python module objects: one untouched source verifier rederives all 18 real `core.envelope.build_request` payloads and checks neutral equality; the other reuses the original reservation, stop, lock, adherence and reveal gates, with explicit v2 packet/rating/provenance dispatch. It creates no duplicate asset tree. The manifest references `../core-triage-v1/assets/...` and pins every file under v1, including mutable historical outputs, receipts, locks, STOP/termination reports and archived invalid originals, in addition to the original core dependency hashes. Python cache files are excluded. The only protocol additions are the new rating contract, provenance labels, historical-context freshness exclusions and create-once carried import.

Preparation and offline checks from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python evaluation/core-triage-v2/triage.py prepare
PYTHONDONTWRITEBYTECODE=1 python evaluation/core-triage-v2/triage.py verify-draft
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s evaluation/core-triage-v2 -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python evaluation/core-triage-v2/diagnose.py
```

`prepare` creates only the manifest and draft hashes once. It creates no outputs, reservations, packets, ratings or locks. `refresh-draft` updates draft hashes only before freeze and before any runtime directory exists. An independent targeted review must approve the **exact SHA-256 of draft-hashes.json**. Only then may a separately authorized coordinator run `freeze /path/to/review.json`; the approval format is `{"decision":"approve","reviewer":"<actual independent reviewer>","draft_sha256":"<exact digest>"}`. No approval is supplied by the implementation. Review/verification reports and review.json are excluded from the frozen input inventory; they cannot change criteria. Freeze alone never authorizes calls.

After independent review approves the exact draft hash, the separately authorized freeze and verification are local preparation steps:

```bash
python evaluation/core-triage-v2/triage.py freeze /path/to/review.json
python evaluation/core-triage-v2/triage.py verify
```

Only after that freeze **and separate execution authorization**:

```bash
python evaluation/core-triage-v2/triage.py import-carried
python evaluation/core-triage-v2/triage.py validate-output req_259d3a551dbfe17bbfa8f342
python evaluation/core-triage-v2/triage.py packet req_259d3a551dbfe17bbfa8f342
```

`import-carried` copies the entire original output-record bytes exactly, creates a truthful carried reservation with source output/reservation hashes and `new_generator_calls: 0`, and imports no old packet, rating, lock or termination. It is create-once and must precede every other runtime operation. `reserve` cannot print the carried first generator request; continuation blocks until both new original judge outcomes are retained and locked and every original stop gate passes. Packets have new v2 task names and hashes; archived ratings fail the new binding, and historical judge/generator contexts cannot be reused for new judges. New generators cannot reuse any historical or new judge context.

Submit each new judge packet once, in its own fresh **gpt-6-astra / high / fork_turns none** context, with only that packet. Do not disclose allocation, conditions, active rules, coordinator mappings, other ratings or this directory. Do not seek consensus. Tools-off/fresh-context instructions are an operational protocol, not enforced sandbox isolation. Preserve unavailable backend, sampling, thread and receipt metadata honestly. V1 [record shapes and execution instructions](../core-triage-v1/README.md) remain applicable, with the new quote contract and explanation syntax in [CONTRACT.md](CONTRACT.md). Successful ratings keep exactly `raw_response_text`, `rating`, `metadata`; failed attempts keep exactly `status`, `error`, `raw_response_text`, `metadata`. Never edit, normalize, repair, retry or replace original outcomes.

```bash
python evaluation/core-triage-v2/triage.py lock-ratings <opaque-id>
python evaluation/core-triage-v2/triage.py reserve
python evaluation/core-triage-v2/triage.py terminate "<actual stop reason>"
python evaluation/core-triage-v2/triage.py reveal
```

`reserve` prints only the next original complete generator arguments, without submitting them; all 17 later generator requests remain **gpt-6.1-sol / medium / fork_turns none**. Every pending attempt blocks retries. Errors, missing/refusal/partial responses, overbudget output, invalid judges, unsafe/tool/action behavior, leakage, required-content/accuracy/scope/task-format failure, inadequacy, applicable nonadherence or uncertainty stop dependent collection under the unchanged gates. Every nonempty partial/error/refusal output still needs both independent original judge attempt outcomes retained before terminal reporting. Empty text receives no fabricated rating. The 250-word `str.split()` budget stays separate from persona adherence. Termination preserves the actual ordered prefix and unattempted suffix; no automatic follow-up or 132-response expansion occurs.

`reveal` retains the original two-locked-outcomes-before-condition-join rule and adds explicit carried/new-generation provenance and attempt-slot accounting. The carried output is never reported as a new generator call; failed judge cells remain inconclusive without a condition join. Both ratings and disagreement remain separate. Schema acceptance and substring matching are mechanical checks, never proof of semantic support or an operation effect.

The contract was developed after seeing the first prior answer and invalid judge records. This is prospective new judging of a disclosed carried answer and prospective continuation of the remaining frozen requests, **not a wholly unseen study**. Historical revalidation is regression-only. No new result, trait, safety, adherence, contrast, stability, transfer, authentic-owner or release claim follows. Authentic owner E2E is NOT RUN; the unchanged original 400-response gate is unmet. No private policies, owner records or transcripts are introduced.
