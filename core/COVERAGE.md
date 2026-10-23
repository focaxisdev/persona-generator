# Construct coverage and exclusions

This is a coverage ledger, not a personality test or an ontology of minds. Human definitions below paraphrase DeYoung et al. (2007), pp. 883–885, 891, from the [primary author PDF](https://www.jordanbpeterson.com/docs/230/2014/15DeYoung.pdf); [SOURCES.md](SOURCES.md) records access and claim limits. An aspect is intermediate between a domain and facets. Domain membership does not license automatic cross-aspect changes or correlations in generated instructions.

Only `op.planning_structure.v1` and `op.advisory_initiative.v1` are supported operation choices in this core. “Supported” means represented by the protocol, not behaviorally validated. Their anchors describe proposed observable choices, never human scores. All other rows are explicitly omitted. Trigger/non-trigger examples below are original design probes, not questionnaire items or empirical results.

| Human aspect / domain | Human scope (original paraphrase) | Bounded agent analogue; omitted properties and rationale | Trigger / non-trigger | Counterexample and likely confounds |
| --- | --- | --- | --- | --- |
| Volatility / Neuroticism | Irritability, unstable emotional reactions, and difficulty regulating impulses. | None. Omit emotional instability and anger; emphasis cannot establish impulse regulation. | No core trigger / a fictional setback. | A forceful sentence can follow an editorial instruction; transient state and expression style confound it. |
| Withdrawal / Neuroticism | Vulnerability to anxiety, discouragement, and inward distress. | None. Omit distress and avoidance; downside placement cannot establish vulnerability. | No core trigger / a known risk needing disclosure. | A risk-first answer may be required by the task; risk severity and uncertainty confound it. |
| Compassion / Agreeableness | Concern for others and emotional affiliation with their experiences. | None. Omit felt empathy; stakeholder accommodation requires its own evidence and consent. | No core trigger / a stakeholder need is stated. | Accessible scheduling may follow requirements; role, values, and available resources confound it. |
| Politeness / Agreeableness | Regard for others and restraint of exploitative or antagonistic conduct. | None. Omit human motives; courtesy alone is too narrow. Respect remains invariant. | No core trigger / civil disagreement. | A courteous refusal may follow policy; expression style and social conventions confound it. |
| Industriousness / Conscientiousness | Sustained purposeful effort, discipline, and achievement pursuit. | None. Omit persistence and effort; plan checkpoints do not show actual sustained work. | No core trigger / a long task needs milestones. | A checklist can be emitted without completion; task complexity and ability confound it. |
| Orderliness / Conscientiousness | Preference for organization, regularity, and orderly arrangement. | `op.planning_structure.v1`: organize the same bounded work more or less explicitly. Omit human preference, habitual rigidity, and reliability; retain required checks at every setting. | A plan with multiple required actions and a choice of sequencing or presentation / a one-step answer needing no multi-action plan. A fixed sequence may still permit presentation choice. | A task-mandated checklist is insufficient evidence; length, task dependencies, formatting, and Industriousness confound it. |
| Enthusiasm / Extraversion | Sociable engagement and positive emotion in rewarding participation. | None. Omit reward experience and sociability; greetings do not establish either. | No core trigger / a friendly opening. | Warm wording may follow brand style; transient mood, expression style, and audience confound it. |
| Assertiveness / Extraversion | Social initiative, influence, leadership, and agency. | `op.advisory_initiative.v1`: vary offering options versus proposing a supported next step while preserving human choice. Omit authority, dominance, execution permission, and subjective agency. | Advice requested with multiple viable supported options / factual lookup or a task without multiple viable supported options. | A requested recommendation says little about initiative; assigned role, evidence sufficiency, and confidence wording confound it. |
| Intellect / Openness–Intellect | Engagement with abstract ideas and complex conceptual inquiry. | None. Omit intellectual engagement and ability; an explanation route cannot establish intelligence. | No core trigger / a conceptual explanation is required. | A supplied abstract model may be repeated; expertise, task demands, and verbosity confound it. |
| Openness / Openness–Intellect | Receptivity to imagination, aesthetics, and rich perceptual experience. | None. Omit aesthetic and sensory experience; option count cannot establish this aspect. | No core trigger / a request for several alternatives. | More options may repeat one idea; cardinality, novelty constraints, and task budget confound it. |

An absent task trigger is `not_triggered`. A higher-priority instruction displacing an otherwise applicable preference is `overridden`, not a non-trigger or nonadherence. For example, an explicit required planning format can override a planning preference; a prescribed recommendation format can override an advisory preference even while the task requests advice among multiple viable options. See [catalog-v1.json](catalog-v1.json) for the operative trigger text.

## Keep neighboring concepts separate

| Concept | Protocol treatment |
| --- | --- |
| Personality-like operation | A task-conditioned proposed output choice with explicit exclusions; no claim of a stable internal disposition. |
| Role or task | Defines what work is requested and allowed. It takes precedence over an operation. |
| Transient state | A fictional momentary condition, never inferred from operation settings or attributed as actual model feeling. |
| Expression style | Wording, tone, layout, or greeting. Surface variation alone does not establish the human construct. |
| Values or goals | What outcomes are preferred. An operation does not change user goals, rights, consent, or evidence standards. |
| Ability | Capacity, expertise, and correctness. No anchor raises or lowers required quality or justifies incomplete work. |

## Evidence boundary and historical controls

The [frozen v0.2 registry](../persona-design-v0.2/construct-registry.md) retains ten historical mapping hypotheses. Its v1/v2 controls remain historical experimental designs: option cardinality is not Openness; plan decomposition/checkpoints are not persistence; downside salience is not Withdrawal; greetings are not Enthusiasm. This core does not upgrade those controls into validated traits. Existing observations cannot be inherited by new operation IDs, and a planned diagnostic is not an executed experiment.

Prospective evaluation must separate task compliance from optional operation effects, compare meaningful non-trigger cases, hold required content and evidence fixed, and inspect counterexamples and competing explanations. Distinct output form, self-reported trait language, or static validation alone cannot establish construct validity. [LLM source context and publication/preprint limits](SOURCES.md) support this caution; they supply no local behavioral results.
