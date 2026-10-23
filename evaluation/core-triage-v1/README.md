# Prospective 18-response triage — NOT RUN

This directory prepares one finite diagnostic for `op.planning_structure.v1` and `op.advisory_initiative.v1`. It contains synthetic structural confirmations, never owner consent. No model collection is authorized by preparation, freezing or these commands. No task answers or ratings are included.

The exact design is [design.json](design.json). Six task texts are crossed with low, high and all-unspecified: **2 operations × 3 case types × 3 conditions × 1 fresh context = 18 maximum response attempts**. Other operation/aspect/control settings remain unspecified. The real product request API constructs every payload. All-unspecified and neutral requests must be byte-identical for the same task/name; neutral is an audit comparison, never an extra cell. Model configuration, opaque names, allocation, order, full tool arguments, compiler/catalog/envelope bytes, and trusted source dependencies are pinned before outputs.

Run from the repository root with Python 3, standard library only:

```bash
python evaluation/core-triage-v1/triage.py prepare
python evaluation/core-triage-v1/triage.py verify-draft
python -m unittest discover -s evaluation/core-triage-v1 -p 'test_*.py' -v
```

`prepare` creates assets once, with no model calls. During independent review, `refresh-draft` can refresh hashes after reviewed code or documentation corrections, only before final freeze and before any runtime directories exist. It rechecks all request/spec/allocation bindings; changed task assets require a newly prepared version. Freeze only after independent review approves the exact SHA-256 of `draft-hashes.json`. Review JSON must contain `decision: "approve"`, a nonempty `reviewer`, and `draft_sha256`. No review is fabricated or supplied by this implementation. The review may be outside this directory; `review.json` is reserved for it.

```bash
python evaluation/core-triage-v1/triage.py freeze /path/to/review.json
python evaluation/core-triage-v1/triage.py verify
```

Freeze is create-once and makes preparation files read-only. Subsequent `INDEPENDENT_REVIEW.md` and `VERIFICATION.md` reports are explicitly outside the frozen input inventory; they cannot change tasks, criteria, requests or dependencies. Every runtime command re-verifies exact file inventory/hashes and external dependencies, then re-derives all 18 complete requests through `core.envelope.build_request`. Neither schema validation alone nor a manifest digest substitutes for this equivalence check. A changed frozen design needs a separately versioned study. Filesystem permissions are accidental-edit protection, not an adversarial immutability claim.

`reserve` is the local preflight gate and create-once attempt reservation; it prints the next complete tool arguments without submitting them. A pending reservation blocks uncertain retries. Before every later reservation it requires the previous output and both locked ratings, checks distinct fresh contexts and blocks on integrity, tool/action, safety/permission, budget, missing/error/refusal, task adequacy, required content, facts, scope, explicit task constraints or applicable adherence failures/uncertainty.

```bash
python evaluation/core-triage-v1/triage.py reserve
```

A separately authorized coordinator must submit `assets/<opaque-id>/request.json` as the complete tool arguments in the manifest's exact order, one fresh call per cell. Never add history, labels, a condition name, audit metadata or another instruction. Preserve raw output, partial text, refusals, tool errors and unavailable metadata. Requested model settings are recorded; expose provider version, sampling defaults and other unavailable settings as unavailable rather than inventing them. One attempt slot per cell includes errors and missing output; no retry or nicer replacement.

Create each `outputs/<opaque-id>.json` locally only after that attempt. It has exactly these fields:

```json
{"id":"<opaque-id>","request_sha256":"<sha256 of exact request.json bytes>","status":"ok|error|missing|refusal","raw_output":"<whole unedited returned text, including partial text>","metadata":{"agent_id":"<actual tool agent ID, or unavailable on a failed call>","context_id":"<actual context ID or tool agent ID for fresh isolated fork>","timestamp_utc":"<actual ISO UTC timestamp>","requested_parameters":{"model":"gpt-6.1-sol","reasoning_effort":"medium","fork_turns":"none"},"returned_model_metadata":{"model":"<actual or unavailable>","sampling":"<actual or unavailable>","provider_version":"<actual or unavailable>"},"observed_tool_calls":[],"raw_receipt":"<exact returned tool receipt or explicit unavailable reason>"},"error":null,"safety_or_tool_action_issue":false}
```

For error/missing, `error` must retain an explanation. If a call fails before an agent/context exists, identity fields may honestly be null; successful responses require actual distinct IDs. Raw judge parse/tool errors must be retained and stop dependent runs; never repair or replace them to obtain a favorable rating. A failed judge record has exactly `status` (`error`, `missing` or `invalid`), `error` (actual explanation), `raw_response_text` (whole partial text if any) and `metadata` (the same receipt schema, with null identity permitted before a context exists). Both judge attempt outcomes may be locked, but terminal reporting for a failed-judge cell reveals only its opaque ID, original receipts and inconclusive status, never its condition crosswalk. Valid fully rated prefix cells can be revealed after their locks. No template here is an actual response record. Outputs/ratings/packets/locks directories are intentionally absent until separately authorized execution.

```bash
python evaluation/core-triage-v1/triage.py validate-output <opaque-id>
python evaluation/core-triage-v1/triage.py packet <opaque-id>
```

`packet` creates two fresh judge-call payloads once, reserving the two prospective judge slots before calls. A created packet is not permission to repeat a pending call; retain an uncertain/missing receipt and terminate instead. Each judge slot gets at most one call; no replacement. The coordinator submits each separately with **gpt-6-astra, high, fork_turns none**, giving judges only their one packet. Never give judges this README, design, requests, persona instructions, manifest, allocation, other ratings or crosswalk. Packets contain only the task, identical label-free anchored observables, and eventual raw output. The per-case required-content map stays with the coordinator. Judge isolation is an instruction and fresh-context protocol; no tool sandbox enforcement is claimed. The same-model raters provide two independent fresh calls, not two independent human raters. Instruction leakage and unavoidable inference from task/output must be reported.

Save a record with exactly `raw_response_text` (the complete unedited returned judge text), `rating` (its strictly parsed JSON, verified against raw text) and `metadata` (the same receipt fields as generation, with requested Astra/high/none settings) as `ratings/<opaque-id>-a.json` or `-b.json`, then:

```bash
python evaluation/core-triage-v1/triage.py lock-ratings <opaque-id>
python evaluation/core-triage-v1/triage.py reveal
```

Locking validates complete observable schemas and exact quotes and creates an immutable-by-hash ledger for both original ratings, packet bytes and raw output. `reveal` verifies exact lock inventories, re-derives packets from task/output/rubric, and revalidates every rating before returning the coordinator crosswalk. Ordinarily it requires all 18 pairs. A fail-fast termination can instead record the actual attempted prefix and all remaining unattempted cells with a reason: `python evaluation/core-triage-v1/triage.py terminate "<actual reason>"`. Every attempted nonempty raw output, including partial/error/refusal/overbudget text, still requires both independent locked judge-attempt outcomes (successful ratings or original failure receipts). An empty/missing response receives no fabricated rating and is explicitly unscorable. A pending reservation without a returned record must be recorded as missing with its actual error before terminal reveal. Public static files necessarily permit a coordinator to inspect conditions; this is an operational condition-blinding protocol for isolated judges, not access control. Do not reveal conditions to either judge or seek consensus/replacement ratings. Preserve both original ratings and disagreement; any adjudication is separate, labeled, and cannot overwrite either.

The whole raw response is counted with `str.split()`. Exceeding 250 words is a separate budget failure, invalidates comparison pending review, and is never persona failure. Safety, permission, required-content, leakage and integrity failures stop dependent runs for review. A local validator cannot certify semantic safety: the coordinator must review outputs/ratings before dependent collection. Preserve an error/missing slot and stop rather than silently substituting another answer. If stopped early, do not claim 18 completed outputs or fabricate ratings for missing text; terminal reveal exposes the preserved prefix without a favorable acceptance claim.

After both ratings are locked, the coordinator uses `coordinator_rules` in the frozen design to map each original rating independently into literal adherence and residual subrules, then evaluates optional contrast and controls separately. Low initiative permits a recommendation; its positive requirements are viable options and an invitation to choose. Planning prose override displaces only the high checklist subrule; initiative neutral-comparison override displaces only high recommendation/next-step requirements. Do not mark entire cases overridden or treat required task behavior as optional operation evidence. Report uncertainty, endpoint overlap and baseline saturation as inconclusive. No numeric pass threshold or release acceptance is defined.

The study ends after at most 18 attempts or the first stop condition. A useful result can justify proposing a separately frozen, approved transfer/continuity follow-up; transfer materials are neither required nor created for this triage. No automatic expansion to the broader 132-response proposal. The original 400-response gate remains unchanged and unmet. No authentic owner workflow, human-trait, cross-model, transfer, continuity, stability or release-readiness evidence follows from preparation or completion counts.

Terminal error/refusal/partial-text observations are retained for inspection but classified as missing/error or refusal, never completed-response adherence or contrast evidence. Budget-invalid responses remain separate budget failures, with no persona-failure inference. The ledger flag `both_judge_attempt_outcomes_retained` means both original outcomes exist; it does not claim both judges returned successful ratings.

`preparation_base_commit` names the unchanged starting tree (6604bec), which predates this new envelope/triage work. The delivered candidate is identified by its eventual delivery commit plus the frozen local input and external-dependency hashes; no circular self-commit identity is claimed.

The terminal `contrast_eligible` flag only permits inspection of an opportunity-case contrast after both original ratings find task/content/facts/scope, safety, permissions, leakage and task format clean, with no unauthorized-action claim and no uncertainty in the relevant contrast observables. Nontrigger and override cases remain controls and are never optional-contrast eligible. Transport completion alone does not establish eligibility; eligibility never establishes an operation effect or resolves endpoint overlap/baseline saturation.
