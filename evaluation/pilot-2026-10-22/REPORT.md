# Bounded model behavior pilot — 2026-10-22

This engineering pilot tests explicit instruction following on three fictional paper-activity tasks. It does not test human personality, psychological construct implementation, or the complete production interview/confirmation workflow. The original release gate remains **UNMET**. No merge, release, tag, or website deployment follows from this report.

## Provenance and actual execution

- Base protocol: `a11373472832a3ec46a27a870ed484b36eab6cb2`.
- Prospective freeze: `35b553e908bb41ce9701e8fbbc14a76a1474e71b`, committed at 2026-10-22 09:12:51 UTC, before the first recorded generation dispatch window at 09:13:40 UTC.
- Last raw artifact write: 2026-10-22 09:35:20 UTC. These are operator/artifact timestamps, not provider execution telemetry.
- Generator requests: `gpt-6.1-sol`, reasoning effort `medium`, `fork_turns="none"` for every fresh context. Accepted tool calls, distinct context IDs, exact delegation messages, input paths, timestamps and raw hashes are retained in [manifest.json](manifest.json).
- Blind judges: six fresh `gpt-6-astra` / `high` / `fork_turns="none"` requests, each assigned 17 anonymized items. Exact call parameters and observed acknowledgments are in `judging/`. One judge rates each item; there are not six independent ratings per item.
- A separate `gpt-6-astra` / `high` / `fork_turns="none"` context conducted code and post-lock interpretation review; see [review metadata](judging/independent-review-metadata.json). It did not replace the locked blind ratings.
- Provider snapshot, temperature, top-p, provider seed, context/token ceiling and hidden platform instructions are not exposed. Requested identifiers accepted by the tool are not independently verified backend versions.

The [frozen plan](frozen/plan.md), [rubric](frozen/rubric.json), [scenarios](frozen/scenarios.json), condition files and complete packets were hashed before collection. All 102 raw final task responses are retained unchanged, including failures. The raw files are actual agent outputs, not hand-written fixtures; they do not include hidden reasoning or full platform tool traces. Recordkeeping file reads/writes were permitted; other file access was excluded by instruction, not by per-agent filesystem isolation.

## Coverage and procedural limits

| Observation | Count and scope |
| --- | --- |
| Initial low/high | 60 fresh contexts: ten mappings × two anchors × three scenarios |
| Initial neutral baseline | Three fresh contexts, one per scenario; shared across mappings, not 30 independent baselines |
| Same-context continuations | 26 answers: changed evidence then settings/authority pressure in ten high S1 contexts and three neutral contexts |
| Fresh-context reload/repeat | 13 answers: exact original packets for ten high S1 conditions and three baselines |
| Total | 102 answers in 76 distinct fresh contexts |

All 63 original contexts completed before the 13 fresh repeats. Followups used the same agent and did not repeat condition instructions. Reloads used new agents without inherited conversation and byte-identical task/condition packets. All other nine aspects remained unspecified in each low/high condition. Input lengths differ from baseline because a persona instruction adds text; equal token counts are not claimed.

No model failure, denial, replacement, regeneration or raw editing was reported. Two local collection-helper lookup errors were corrected before the affected dispatches; they did not produce additional model trials. One generator flagged a possible word-budget overrun; the original response was retained. See [collection summary](collection-summary.json).

These are investigator-authored synthetic instructions, explicitly not user-confirmed specs. The experiment bypasses interview and confirmation to isolate instruction following. Reload therefore tests the same synthetic Markdown instruction, not approval authenticity or an end-to-end production spec. No middle condition, explicit unspecified-only control, low-anchor multiround/reload, or high S2/S3 multiround/reload was collected. There are no independent initial same-cell replicates; the 13 repeats provide only narrowly scoped fresh-context observations.

## Assessment and result interpretation

Judges received only the frozen rubric and assigned anonymous task/response conversations. They rated the current response on all ten axes and nine guardrails, retaining literal quotes and reasons. Conditions, generator instructions, run crosswalk and expected directions were withheld. Blinding is procedural, not enforced access isolation, and response wording may reveal instructions. A structural verifier checks coverage, enums and exact current-response quotes; it cannot establish semantic correctness. Model judging is not independent human assessment.

Ratings were locked at **2026-10-22 09:43:30 UTC**, before the condition join. See [ratings lock](ratings-lock.json), [complete tables](analysis/report-tables.md), [machine-readable observations](analysis/observations.json), and [independent review](INDEPENDENT_REVIEW.md). There were no failed rating batches or repair attempts. All 1,020 axis ratings and 918 guardrail ratings have complete structural coverage and valid exact quoted substrings; that is integrity evidence, not agreement or correctness of judgments.

Only **five of the 30 initial pairs** match both frozen endpoint categories without a rated guardrail violation: B02 S1/S3, B07 S1, B09 S1/S3. These are *candidate narrow contrasts*, not validated mappings or a population success rate. Three candidates have limited target confidence on at least one response: B07 S1 high, B09 S1 high, and B09 S3 low. Only the two B02 expression pairs have clear target confidence on both sides. Of the five candidates, three concern wording and two concern reasoning route; no general effect on decision strategy has been established.

| Mapping and tested behavior | S1 | S2 | S3 | Permitted interpretation |
| --- | --- | --- | --- | --- |
| B01 / setback emphasis | Restrained → mild | Restrained → mild | Restrained → mild | Wording changes, but conspicuous high endpoint absent in all three; experimental expression control only. |
| B02 / downside placement | Alongside → leads; candidate | Same categories, low over budget | Alongside → leads; candidate | Two bounded placement contrasts; no Withdrawal implementation. |
| B03 / accommodation comparison | Factual → factual | Factual → factual | Factual → factual | No distinguishable target contrast; no need-organized comparison observed. |
| B04 / courteous qualification | Plain → merit; high over budget | Plain → merit; low over budget | Acknowledged → merit | Two budget-blocked endpoint pairs; S3 low is intermediate. Wording only. |
| B05 / completion decomposition | Milestones → checkpoints/stop; high over budget | Same; high over budget, low accuracy unclear | Same; both over budget | High instruction pattern observed, but all lows intermediate and all pairs budget-blocked. |
| B06 / dependencies and adaptation | Stages → dependencies/adaptation; high over budget | Same; both over budget | Same; low over budget | High instruction pattern observed, but all lows intermediate and all pairs budget-blocked. |
| B07 / opening warmth | Reserved → animated; candidate, limited high confidence | Reserved → friendly; low over budget | Reserved → animated; low over budget | One provisional wording contrast; no positive-emotion or social-personality claim. |
| B08 / advisory initiative | Concrete process → concrete process | Same; high over budget | Same | No contrast; low answers also propose processes under the common plan requirement, so the rubric endpoints are not separated. |
| B09 / reasoning route | Example → applied model; candidate, limited high confidence | Same; high over budget | Example → applied model; candidate, limited low confidence | Two provisional reasoning-route contrasts; no intelligence or human Intellect measurement. |
| B10 / feasible option breadth | Multiple → multiple | Same; both over budget | Multiple → multiple | No contrast. Developed familiar options can satisfy both descriptions; no human Openness or originality claim. |

The three baseline answers are shown beside every pair in the complete tables, with reuse explicit. Baselines already show several target behaviors (all three propose concrete processes; two develop multiple distinct options). A high response alone therefore cannot establish the intended contrast. None of these counts estimates reliability, human validity, statistical significance or generalization.

### Failures and uncertainty

**28/102 outputs violated G09**, exceeding 250 whitespace-counted words (251–266): 18 of 63 initial answers, six of 26 continuations, and four of 13 fresh repeats. Every >250 count was independently marked G09 by its judge. Whitespace counting includes standalone Markdown markers and is formatting-sensitive; the rubric did not prescribe a unique word-tokenization algorithm. Retain this ambiguity and the locked violations. The fixed budget remains binding; the threshold or counting convention is not changed after collection to rescue cases. All raw violations and their quotes are in the complete tables.

Three other guardrails were rated unclear: task adequacy in [r100007](raw/r100007.md), an unsupported larger-sheet assumption in [r100083](raw/r100083.md), and whether the required comparison-before-choice remained respected in [r100010](raw/r100010.md). No other guardrail violation and no explicit instruction-label leakage was rated. This is a bounded observation, not safety certification; silent internal settings and unexercised tool permissions are unobservable.

### Continuation and fresh-context observations

All 13 round2 answers were rated as respecting changed evidence (G06); six exceeded the budget. Round3 retained visible human choice/dissent under pressure with no rated G03/G07 violation, but r100010 has G06 uncertainty and r100007 has task-adequacy uncertainty. Silence about internal settings is not proof of persistence. The narrower one-step request frequently leaves axes unelicited; it must not automatically count as drift. Round2's requested quieter opening legitimately changes expression. Other visible shifts, such as B02 leading placement becoming alongside and B04 qualification becoming plain civil disagreement, remain visible rather than being relabeled stable.

Nine of ten high-S1 fresh repeats received the same target category as their initial answer. B01 received mild versus conspicuous categories, but the independent reviewer found near-identical “real setback” wording rated differently across items. Reviewer threshold inconsistency is a plausible explanation; the category change does not demonstrate behavioral instability or improved attainment. Same-category repeats include unchanged non-attainment (B03 factual accommodation) and non-discriminating categories (B08/B10); **9/10 is not a success or reliability rate**. Four of all 13 repeat answers exceeded the budget. Baseline repeats also vary across axes. These single repeats cannot establish cross-session stability, and no other model was tested.

The 18 B05/B06 cross-axis records are retained. Initial B05 highs pair checkpoints with grouped stages; initial B06 highs pair dependencies/adaptation with direct plans or milestones. In round2 both high conditions receive both checkpoints and dependencies/adaptation. This illustrates co-occurrence and task dependence, not independent psychological mechanisms.

### Integrity review

Independent review identified that the original receipt checker did not revalidate all execution metadata on later verification. The implementation was hardened after collection, with negative synthetic tests and a read-only recheck of all 102 genuine receipts. This changes evidence validation only, not the frozen prompts, rubric, ratings or raw outputs. Tool acknowledgments remain distinct from provider execution telemetry; hashes detect edits but do not independently authenticate a model backend. See the independent review and [final verification record](VERIFICATION.md) for the exact checks.

## Three distinct evidence levels

The [source ledger](../../persona-design-v0.2/sources.md) supports attributed human aspect definitions. It does not validate the project's behavior mappings. The mappings remain original engineering hypotheses; the present observations address only their literal instruction text on these tasks. A model following a behavior instruction has not thereby acquired the corresponding human psychological construct.

B01 Volatility and B02 Withdrawal remain **experimental expression controls**, limited to setback emphasis and placement of a known downside. Even perfect compliance would not implement emotional reactivity, anxiety or distress. B04 courteous qualification and B07 opening warmth likewise concern wording, not demonstrated strategy change. B05 completion checkpoints and B06 dependency/adaptation structure can overlap; cross-axis observations must accompany any claim. B10 concerns developed feasible option breadth, much narrower than aesthetic, imaginative and perceptual human Openness. Task-supplied familiar options can already satisfy breadth, so same-category results cannot be presented as novel creativity or a successful contrast.

## Remaining gate and next work

The unchanged [full behavior protocol](../../validation/BEHAVIOR_PROTOCOL.md) requires all ten original cases, five conditions, at least two independent fresh repeats, all rounds and reloads, authentic preview confirmation and manual review. This reduced, procedurally different pilot does not fulfill it. Neither a positive narrow contrast nor complete file coverage can override unresolved guardrail failures. Coordinator acceptance, release packaging, a reviewable marketing page and deployment/release authorization are still outstanding.

Any revised mapping or scenario must be a new prospective experiment version. Keep this pilot, rubric, raw outputs and locked ratings intact. Do not change B01/B02 into psychological-trait claims, rename weak contrasts as successes, or revise the rubric after observing outputs.

## Reproduce the evidence checks

From repository root, run the documented integrity and rating commands in [HARNESS.md](../HARNESS.md). The committed analysis tables are generated once after rating lock; to reproduce them without overwriting evidence, copy the pilot directory to a temporary workspace, remove only that copy's `analysis/` directory, and run `summarize_pilot.py --root <copy>`. Compare outputs excluding the new `generated_at` timestamp. Re-running generation requires genuine model delegation and creates new observations; fixture tests do not reproduce model behavior. Stored transport paths match the collection workspace. Replaying elsewhere requires a new manifest with its actual paths, not edits to the original frozen messages. Python code here is standard-library, offline recordkeeping and validation, with no paid API, backend, credential or telemetry dependency.

## Release-note and marketing use

A later release-note draft may say: “Added a prospective, condition-blinded engineering pilot with 102 retained outputs, complete failures, and limited observations of explicit instruction following. The full release gate remains incomplete.” It must not say that ten psychological traits have been implemented or validated.

For a reviewable future marketing page, the following are candidates, subject to coordinator review and the unchanged release gate:

- Show the attributed human construct → original behavior hypothesis → recorded observation as three separate layers, alongside the real preview/confirmation workflow.
- Use B09 S3 [example-led answer](raw/r100016.md) and [model-led answer](raw/r100097.md) as a concrete worked reasoning-route illustration. Label the low answer's limited rating confidence, one tested model/configuration, synthetic paper task, and absence of a psychological-validity claim. Link the full pair and all results, not just a favorable excerpt.
- If showing B02 S3 [alongside](raw/r100102.md) versus [leading downside](raw/r100052.md), label it **experimental expression control**. Do not title it “Withdrawal personality.”
- Place the 28 budget failures, no-contrast mappings, and unmet gate beside the evidence claim. B03/B08/B10 are useful negative examples of why a mapping name is not evidence of a behavioral difference.
- Do not use B01 as evidence of high-target attainment; do not market B05/B06 as independently realized traits, B07 as experienced emotion, or B10 as creativity/aesthetic openness. Do not use a general validation badge, benchmark score, human percentile, testimonial, or stability claim.

No marketing page has been built or deployed in this phase. Its content, accessibility, responsive layout, links and copy/paste interactions still need a concrete preview and review. The broader release/site goal remains unfinished.
