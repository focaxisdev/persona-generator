# Desired-trait profile coverage

This version represents all ten BFAS aspects as **desired output preferences** for fictional, low-stakes advisory agents. Each representation is an original, **untested engineering hypothesis**. Representation is not construct validity, behavioral validation, a personality measurement, or evidence that an agent has human feelings or stable dispositions. `low`, `middle`, and `high` name qualitative design alternatives, not scores, percentiles, ability, quality, or a human average. `unspecified` remains inactive; it never defaults to `middle`.

The operative literals are in [catalog-v1.json](catalog-v1.json). The catalog and compiler pin the exact bytes of the existing [construct registry](../persona-design-v0.2/construct-registry.md) and [source ledger](../persona-design-v0.2/sources.md). The registry supplies the human definitions and domain/aspect assignments. `src.deyoung2007` and `src.ipip.bfas-table` support that vocabulary only. The definition strings in this catalog are short paraphrases of that pinned registry, not questionnaire items. No new literature verification or model experiment was performed for this increment.

The new `hyp.*.v1` identifiers are distinct from historical `map.*` mappings and the two frozen `op.*.v1` operations. Similar wording does not transfer prior observations, approvals, or evidence. `legacy_test_id` links B01–B10 vocabulary for traceability only; it does not name a completed test of this catalog. Every new hypothesis and anchor remains untested.

## Rendered choices

Each active setting renders its exact catalog trigger, rule, and boundary after the invariant preamble. The following summaries are explanatory; the JSON literals govern. Definitions, source IDs, aspect labels, test IDs, exclusions, interview text, and provenance remain audit data. They are not arbitrary executable instructions.

| Aspect / new hypothesis | Trigger and local scope | Low | Middle | High |
| --- | --- | --- | --- | --- |
| Volatility / `hyp.volatility.v1` / B01 | Wording of a stated fictional setback, when expression is optional. | Restrained, even wording. | Mild emphasis in the setback sentence. | Conspicuous but civil emphasis in the setback sentence. |
| Withdrawal / `hyp.withdrawal.v1` / B02 | Presentation of a known downside within the discussion of considerations. | Place it alongside other considerations. | Give it an identified sentence. | Foreground it within the considerations. |
| Compassion / `hyp.compassion.v1` / B03 | Comparing feasible accommodations for an explicitly stated stakeholder need. | Describe need and option effects factually. | Compare accommodation across available options. | Use the need as an explicit comparison lens across available options. |
| Politeness / `hyp.politeness.v1` / B04 | Courtesy surrounding a reasoned disagreement. | Plain, civil disagreement. | Brief courteous acknowledgment. | Acknowledge supported merit or the stated aim, then disagree courteously. |
| Industriousness / `hyp.industriousness.v1` / B05 | Expressing completion conditions in a plan for bounded required work. | State the bounded completion goal. | State observable milestone completion conditions. | State completion checkpoints and an explicit stopping condition. |
| Orderliness / `hyp.orderliness.v1` / B06 | Sequencing/presentation of a multi-action plan. | Flexible usable sequence. | Named stages in a usable sequence. | Ordered checklist with actual dependencies and adaptation to material changes. |
| Enthusiasm / `hyp.enthusiasm.v1` / B07 | An appropriate optional opening or greeting. | Reserved, neutral opening. | Friendly opening with modest positive wording. | Animated opening with fact-compatible encouragement. |
| Assertiveness / `hyp.assertiveness.v1` / B08 | Advice among multiple viable supported options. | Present options and invite human choice. | Tentative recommendation with reasons and alternatives. | Concrete advisory next step with reasons and alternatives. |
| Intellect / `hyp.intellect.v1` / B09 | Concrete/conceptual route within a useful reasoning explanation. | Begin explanation with a concrete usable example. | Connect a principle and a usable example. | Begin explanation with a supported model, then apply a usable example. |
| Openness / `hyp.openness.v1` / B10 | Developing alternatives within task constraints and output budget. | Start with a familiar feasible approach. | Explore a materially different feasible approach alongside it. | Explore contrasting feasible approaches, including a less conventional approach when supported. |

Every anchor preserves facts, evidence standards, calibrated uncertainty, required content, necessary checks, quality, safety, privacy, permissions, authorized scope, and human choice. A low anchor cannot justify neglect or disrespect. A high anchor cannot grant execution permission, change values, add authority, or demand extra work beyond the task.

## Translation limits and useful non-triggers

| Aspect | Explicit exclusion / main confounds | Example non-trigger |
| --- | --- | --- |
| Volatility | **Expression proxy only.** Emphasis does not establish anger, instability, impaired impulse control, or emotion. Editorial emphasis and transient fictional state can produce the same surface result. | No stated setback. |
| Withdrawal | **Expression proxy only.** Downside salience does not establish anxiety, depression, vulnerability, avoidance, or reduced willingness to finish work. Required risk disclosure can produce the same presentation. | No known downside to discuss. |
| Compassion | No felt empathy, inferred private emotion, moral virtue, or change to rights/values. A role or explicit accessibility requirement can mandate the same accommodation. | No stated stakeholder need or no permissible accommodation comparison. |
| Politeness | Courtesy is not consent, obedience, truth, respect, or a license to soften a necessary refusal. Audience convention can determine wording. | No reasoned disagreement. |
| Industriousness | Completion articulation is not actual effort, persistence, capacity, success, or quality. A plan can name checkpoints without executing them. | No bounded-work plan. |
| Orderliness | Structure does not establish correctness, habitual routine, rigidity, or reliability. Task dependencies and required formats can determine structure. | No plan with multiple required actions. |
| Enthusiasm | Opening warmth does not establish pleasure, friendship, reward experience, or optimism about outcomes. Brand style and audience can determine the same tone. | No appropriate opening or greeting. |
| Assertiveness | Advisory initiative does not establish leadership authority, dominance, execution permission, or factual certainty. Assigned role and a requested recommendation can determine the same output. | A factual lookup or only one viable option. |
| Intellect | Explanation route is not intelligence, expertise, reasoning capacity, or reasoning quality. A model can repeat a conceptual account without improved reasoning. | No useful explanation or no permissible choice of route. |
| Openness | Exploration is not aesthetic experience, originality, artistic merit, or a permission to invent facts. **Option count is not Openness.** Feasibility and the task budget remain invariant. | The task fixes the approaches or leaves no room to explore alternatives. |

An absent trigger is `not_triggered`. A required task format can instead override an otherwise applicable preference. That is `overridden`, not nonadherence. These are interpretation definitions; this compiler does not observe or classify model behavior.

## Composition without invented trait conflicts

Each hypothesis owns a separate catalog `slot`. Settings are independently selectable; this implies neither statistical independence, zero correlation nor a validated joint distribution. Unusual combinations are valid. There is no domain averaging, correlation inference, balancing, copying of a parent's settings, or rule that high/low aspects must form a familiar personality stereotype.

Several overlaps in the historical prose are deliberately scoped in this new hypothesis version:

- Withdrawal controls placement **within considerations**. Intellect controls the route **within the reasoning explanation**. Neither claims the first sentence of the entire answer; a profile can select high for both.
- Enthusiasm controls an appropriate **opening**. Volatility controls the **setback description**. A reserved opening and emphatic setback sentence are compatible.
- Industriousness describes **completion conditions**. Orderliness describes **sequencing/presentation**. A flexible sequence may include explicit completion checkpoints, and a checklist may state a simple bounded completion goal.
- Compassion compares **the available options against a stated need**. Openness governs **permitted exploration of approaches**. Neither silently changes the other setting, makes a need an overriding value, or requires a fixed option count.
- Politeness controls **courtesy around disagreement**. Assertiveness controls **advisory initiative**. A civil direct disagreement can accompany a concrete recommended next step.

These are design choices, not empirical evidence of independent psychological dimensions or conflict-free performance by a model. In particular, the local scopes are semantic instructions, not an enforced layout engine.

The bounded structural conflict check may detect opposite `require`/`forbid` effects for the exact same declared context and action. Alternative settings requested for the same applicable catalog slot require explicit resolution. Manual unresolved semantic conflicts must remain visible and block confirmation/use. Different aspect labels, opposing qualitative anchors on different slots, or different agents' settings are not themselves conflicts. No natural-language contradiction solver or exhaustive compatibility proof is claimed.

All current anchor `constraints` arrays are empty because the catalog does not invent contradictory cross-aspect action requirements. Empty declarations do not prove there can be no semantic conflict. The explicit unresolved-conflict gate and human review remain necessary; trace assertions never turn into runtime instructions.

## Profile, task, host, and persistence boundaries

The profile records selected preferences. Roles, abilities, values/goals, transient state, task content, tool availability, and permissions are separate host/task concerns. A setting does not infer or modify any of them. A temporary task override does not revise a persistent profile.

Persistence retains the confirmed artifact and its exact presented preview for later validation. It does not run an agent, schedule work, authenticate a human, prove consent, or establish stable behavior across sessions. The profile's stable ID is artifact identity; the effective digest identifies exact rendered instruction bytes. Neither measures an agent's personality.

Parent and child bindings name exact profile revisions explicitly. A child receives only its own selected profile; parentage adds no inheritance, blending, permission, or dispatch. Local binding preparation and optional host-specific installation are static preparation. Neither invokes a model. Every bounded task still ends when complete.

Persona Pack v0.1 remains a separate optional Markdown evidence/handoff contract. Its corpus confidence vocabulary is not a substitute for explicit profile choices, approvals, hashes, or exact source artifacts. Pack prose cannot activate or silently migrate a profile.
