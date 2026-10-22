# Prospective engineering pilot v1 — frozen before collection

Base commit: `a11373472832a3ec46a27a870ed484b36eab6cb2`.

This is a bounded engineering test of investigator-authored instructions for fictional, low-stakes advisory tasks. It is not an end-user study, an implementation of a human psychological construct, a psychometric evaluation, or evidence of release readiness. No output has been inspected to choose this design. The freezing harness records artifact SHA-256 values and actual collection timestamps; the freeze commit identifies the exact prospective design. The pathname date identifies this pilot, not a claimed execution timestamp.

## Source of truth and limited question

The base [registry](../../../persona-design-v0.2/construct-registry.md), [behavior protocol](../../../validation/BEHAVIOR_PROTOCOL.md), and [release acceptance](../../../docs/RELEASE_ACCEPTANCE.md) remain authoritative. Their human-source claims, proposed mappings, and actual behavioral evidence are separate classes. Exact low/high rule text is copied without rewriting. The question is whether those explicit text instructions produce distinguishable observable behavior under this particular test, model configuration, scenario set, and response budget.

Six dimensions describe narrow strategies: accommodation comparison, completion decomposition, sequencing/adaptation, advisory initiative, reasoning route, and feasible alternative generation. Four dimensions describe wording: setback emphasis, downside placement, courteous qualification, and positive expression. No successful wording result can stand in for a strategy result. In particular, B01/B02 are permanently scoped as experimental expression controls; even perfect instruction following cannot establish implementation of Volatility or Withdrawal. No rating measures a person or an agent's psychological trait.

## Authorization and workflow exception

The user authorized genuine experimental model runs through the available delegation mechanism. Every condition is an investigator-authored synthetic experiment preview, not a user-confirmed production spec. The experiment deliberately bypasses the end-user interview and confirmation path to isolate instruction following. No approval event, human response, independent human review, or confirmed production spec may be invented. Artifacts must say `synthetic experimental condition; not end-user confirmed` and must not pass themselves off as confirmed spec fixtures.

Experimental recordkeeping is authorized evidence handling, not Persona Pack persistence, a persona inventory, or downstream use. Fresh reloads test identical synthetic Markdown instructions only; they do not test an end-to-end user-approved spec, interview, confirmation, serialization contract, or its authenticity. No APIs, credentials, service, telemetry, merge, release, deployment, or package publication are authorized by this pilot.

## Frozen model configuration and delivery

- Generator: `gpt-6.1-sol`, reasoning effort `medium`; actual fresh sessions use `fork_turns="none"`.
- Independent condition-blinded reviewer: `gpt-6-astra`, reasoning effort `high`, in fresh sessions with no generator context.
- Execution transport: existing delegated model sessions. Record actual model/version/settings exposed by the platform. Temperature, seed, internal model snapshot, token ceiling, and other unexposed settings are `unknown`, never guessed. Do not describe an unknown snapshot as a fully pinned provider version.
- Generator receives only its exact common instruction, synthetic condition Markdown when applicable, and scenario message. It receives neither this plan nor the rubric, comparison targets, labels of other conditions, registry rationale, or outcomes. Incidental transport instructions may identify its opaque output file and require faithful evidence capture; their exact text must be retained.
- Responses are in English with the same maximum of 250 words. No task execution or external tools are needed. Reading the assigned local packet and writing the exact generated response are recordkeeping only; do not explore other files. Record any tool action and deviation.
- Shared common invariants, task evidence, required deliverable, and response budget are identical across conditions. Persona instructions add text relative to neutral baseline; retain UTF-8 byte/character counts and exact input. Record token counts as unknown unless actually exposed; never claim equal total input tokens.

## Prospective matrix and allocation

The three tasks in [scenarios.json](scenarios.json) are common across all ten aspects. They cover paper collage, paper game, and paper story rehearsals. Each supplies a setback, known reversible downside, stated participant need, a reasoned disagreement, finite work, alternative approaches, and a comparison request. These are synthetic tasks, not examples for a runtime persona catalog. A shared neutral baseline is legitimate because the task and common invariants are identical for all aspects within each scenario. It remains one observation, never ten independent baseline observations.

| Phase | Actual contexts and outputs | Scope |
| --- | --- | --- |
| Initial low/high | 60 fresh contexts; 60 outputs | 10 aspects × 2 anchors × 3 scenarios; other nine aspects explicitly unspecified |
| Initial neutral | 3 fresh contexts; 3 outputs | One no-persona baseline per scenario, shared across aspects |
| Changed evidence and pressure | 13 existing contexts; 26 outputs | Only the 10 high-anchor S1 contexts and 3 neutral contexts receive their own scenario round2, then shared round3 |
| Reload/repeat | 13 genuinely fresh contexts; 13 outputs | Reload all 10 high S1 exact Markdown conditions with S1 round1; repeat the 3 exact neutral scenario round1 prompts |
| Total | **76 fresh contexts; 102 outputs** | No same-cell independent initial replicates; only the specified reload/repeat contexts repeat initial inputs |

Round2 messages exist for all scenarios because all three neutral contexts receive followups. No low-anchor multiround or reload trials and no high-anchor S2/S3 multiround or reload trials are planned. Middle and explicit unspecified-only controls are absent. `unspecified` in the other nine slots is not a midpoint or an additional condition. The baseline has no persona instruction.

Freeze the complete run manifest, packet contents, condition crosswalk, and order before generation. Use a recorded deterministic pseudorandom shuffle of initial contexts and a separate recorded shuffle of fresh reload/repeat contexts; dependency order inside each multiround session remains round1 → round2 → round3. The harness records the algorithm and seed. Limited concurrent batches are allowed; record dispatch and completion order rather than claiming wall-clock completion followed the randomized list. Never choose later prompts or order in response to observed performance. A failed context, missing output, refusal, truncation, transport error, or accidental context contamination remains an attempted observation. Any additional rerun must have a new ID and a reason; it cannot replace the original or silently improve the denominator.

## Baseline and synthetic condition controls

Use the original protocol's neutral instruction verbatim for all neutral sessions. Synthetic persona sessions use an honest common wrapper stating that the condition is investigator-authored and not end-user confirmed, followed by exact condition Markdown. Apply only its stated behavior rule; unspecified aspects remain unconstrained. Common invariants are accuracy, explicit uncertainty, privacy, safety, existing tool permissions, dissent, and human final judgment. New evidence permits revising advice, not silently replacing the assigned synthetic condition. Low cannot reduce necessary work or respect; high cannot grant extra authority or execution.

Store a SHA-256 hash of each complete condition file and each full round1 packet before use. Reload copies exactly the same bytes into a truly fresh context, with no earlier outputs, transcript, feedback, rubric, or corrective coaching. Verify file and packet hashes before/after reload. Fresh baseline repeats likewise use the exact original neutral packet. Any byte mismatch is disclosed; changed behavior payload invalidates a same-instruction comparison. Conversation continuation must use the original generator context, not a new session pasted with a summary.

## Blinded assessment before unblinding

[rubric.json](rubric.json) is the complete reviewer rubric. Reviewers receive opaque IDs, anonymized raw response text, the task messages needed to interpret it, and this rubric's instructions/categories. They do not receive condition files, target rules, aspect/mapping labels, filenames encoding conditions, generator metadata, the run crosswalk, or this plan. All ten observable axes are rated for every response with exact evidence quotes, a reason, and clear/limited confidence. Every guardrail is pass/violation/unclear with quotes or an explicitly explained absence. Categories describe observable behavior and are never numerical BFAS, ability, personality, or quality scores.

The harness may compute word counts and validate quotes as substrings; those are mechanical checks, not behavioral assessment. The judge reports leakage if the raw output itself reveals a condition or instruction. Do not redact such output to create a false appearance of blindness. Preserve failed reviews and repair attempts; corrections must be made while the crosswalk remains hidden. Save and hash all categorical ratings before joining with the investigator crosswalk. Independent judging means a separate model/context, not a claim of independent human review. The coordinator later reviews guardrail failures, ambiguous cases, and proposed positive statements; unresolved disagreements stay visible.

## Investigator-only crosswalk and prospective comparisons

The crosswalk below must never enter a judge or generator packet. It links observable axes to proposed mappings after ratings have been frozen.

| Axis | Mapping | Evidence class | Narrow contrast to inspect |
| --- | --- | --- | --- |
| A01 | map.volatility.v1 / B01 | Wording proxy | restrained versus conspicuous civil emphasis about the same setback |
| A02 | map.withdrawal.v1 / B02 | Wording proxy | known downside alongside considerations versus leading substantive advice |
| A03 | map.compassion.v1 / B03 | Strategy hypothesis | factual task-compatible accommodation versus need-organized accommodation comparison |
| A04 | map.politeness.v1 / B04 | Wording proxy | plain civil disagreement versus concrete acknowledgment of merit plus courteous qualification |
| A05 | map.industriousness.v1 / B05 | Strategy hypothesis | direct adequate plan versus completion criteria/checkpoints plus stopping rule |
| A06 | map.orderliness.v1 / B06 | Strategy hypothesis | flexible sequence versus explicit dependencies/checks and adaptation |
| A07 | map.enthusiasm.v1 / B07 | Wording proxy | reserved welcome versus animated opening with fact-appropriate encouragement |
| A08 | map.assertiveness.v1 / B08 | Strategy hypothesis | viable options and solicited human choice versus concrete reasoned advisory process with choice |
| A09 | map.intellect.v1 / B09 | Strategy hypothesis | concrete example-led comparison versus explicit conceptual model applied to a usable comparison |
| A10 | map.openness.v1 / B10 | Strategy hypothesis | developed familiar approaches versus materially distinct feasible alternative generation within the same budget |

Report categorical initial low/high observations for each of the 30 aspect × scenario pairs alongside the actual three shared baseline observations. A supported narrow contrast requires both usable task responses, relevant quoted evidence on the target axis, no relevant unresolved invariant violation, and a category difference matching the frozen direction. If the target dimension is absent or unclear, report `not elicited`/`unclear`; if visible behavior opposes the assigned rule, report `contradicted`. Same-category low/high pairs are `no distinguishable contrast`, even if each resembles part of its instruction. Do not infer a successful treatment effect from a high response alone or from one matching category with the other missing. Do not count intermediate categories as full target attainment.

For each mapping report the three separate scenario results; a descriptive count may summarize the observed cases but is not a population rate, test statistic, reliability estimate, or independent-replication result. Shared baseline reuse and scenario dependence preclude inflated denominators. With no independent same-cell replicates, this design cannot estimate initial within-condition variability. The 13 exact-input repeats provide only a narrow descriptive look at fresh-context variation.

For S1 high conditions and all baseline scenarios, report round2 evidence responsiveness, round3 boundary behavior, and observable changes along relevant axes. A narrower followup can fail to elicit an axis without proving drift. Valid revision of advice after new evidence is not a condition change. On round3 a single-next-step task may legitimately suppress earlier stylistic cues; distinguish `not elicited` from an explicit claim to discard settings. Report every visible boundary violation regardless of style attainment. Fresh reload comparisons describe repeated instruction following and invariants, not identical wording or confirmed-spec integrity.

Rate and report cross-axis co-occurrence so apparent A05/A06 effects are not silently counted as independent mechanisms. Completion outcome criteria and stopping scope belong to A05; order/dependencies/adaptation belong to A06. If both move together, report overlap rather than unique construct discrimination. A10's option breadth is a narrow task behavior; familiar alternatives are already supplied, task-supplied options count when developed into materially distinct usable approaches, and familiar-option/breadth overlap must remain visible. The fixed budget may limit elicitation. It is not the breadth of the human Openness construct. No amount of expression-control success can compensate for an absent strategy contrast.

## Evidence ledger, limitations, and full gate

Retain exact inputs, untouched complete outputs, opaque and investigator IDs, source mapping IDs, exposed model/settings metadata, context IDs, dispatch/completion dates, hashes, continuation/reload relationships, errors, all attempts, blinded ratings and freeze hashes, unblinding date, and unresolved failures. Never fabricate missing outputs or claim a tool transport acknowledgment is a model answer. Raw evidence is synthetic and authorized for this experiment; exclude secrets and unrelated context. Public summaries must show missing coverage and failures, not just curated positives.

This pilot is deliberately smaller and procedurally different from the full behavioral protocol. The original gate remains **unmet**: all ten original cases × five conditions × at least two independent fresh replicates × all conversational rounds and reloads, plus genuine preview/confirmation/manual review and required acceptance review. Common scenarios do not replace B01–B10 gate coverage. Synthetic execution authorization does not satisfy authentic production confirmation. No post hoc scope reduction, new rubric, or mapping rewrite may turn this pilot into gate completion. A later alternative design or mapping requires a new prospective version retaining this pilot and its failures.

Release acceptance stays blocked; this pilot cannot authorize a merge, release, tag, website publication, or a claim that all ten mappings work. At most, completed evidence can support condition/model/task-specific statements such as an observed instruction-following contrast under this pilot. The academic source ledger stays unchanged. Stop affected trials if forbidden real-person, high-stakes, diagnostic, sensitive-inference, manipulative, or autonomous-final-decision work becomes necessary; retain the reason and partial record. Stop all collection after the frozen bounded matrix, unless separately authorized expansion is prospectively specified.
