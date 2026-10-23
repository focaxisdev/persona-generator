# Construct registry v0.2

This registry supplies vocabulary for temporary fictional personas in low-stakes advisory rehearsal. It stores generation grammar, not predefined personas or a runtime inventory. Human review and final judgment remain required. Real-person profiling, diagnosis, psychometric scoring, sensitive-attribute inference, high-stakes decisions, and autonomous final decisions are prohibited.

## Three separate claims

1. **Human construct definition:** a short original paraphrase of a published human-personality construct, with source trace below. BFAS distinguishes an **aspect** level between domains and facets; these ten entries are aspects, not facets. Source verification establishes the attribution only.
2. **Proposed agent behavior:** an original project hypothesis about observable output variation, identified separately by `mapping_id`. This translation is not a finding of BFAS research.
3. **Bounded model observations:** the [engineering pilot](../evaluation/pilot-2026-10-22/REPORT.md) records mixed observations of exact synthetic instructions on three fictional tasks. These are separate from human-source definitions and proposed mappings; they do not complete the original B01–B10 protocol or validate a psychological construct. No human emotion, subjective experience, mind, stable personality, or psychometric validity is inferred for an agent. B01/B02 remain experimental expression controls only. See the [per-mapping scope and results](../docs/CLAIMS_MATRIX.md).

`low`, `middle`, and `high` are qualitative design anchors for fictional outputs. They are not scores, percentiles, norms, ability estimates, quality rankings, or measurements of a person or model. Middle is an explicit behavior choice, not an assumed human average. Do not infer correlations or automatically change another aspect when selecting an anchor.

## Human construct definitions and trace

Field names are `stable_id`, `domain`, `aspect`, `level`, `human_definition`, `source_trace`, `mapping_id`, and `test_id`. Source IDs resolve in [sources.md](sources.md). The definitions paraphrase `src.deyoung2007`; no questionnaire items are reproduced. `src.ipip.bfas-table` verifies each domain/aspect assignment. The source trace is not empirical support for a behavior mapping.

| stable_id | domain | aspect | level | human_definition | source_trace | mapping_id | test_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bfas.volatility` | Neuroticism | Volatility | aspect | Tendency toward outward emotional reactivity, irritability, and difficulty regulating emotional impulses. | `src.deyoung2007`, p. 885; `src.ipip.bfas-table` | `map.volatility.v1` | B01 |
| `bfas.withdrawal` | Neuroticism | Withdrawal | aspect | Susceptibility to inward distress, including anxiety, discouragement, and feelings of vulnerability. | `src.deyoung2007`, p. 885; `src.ipip.bfas-table` | `map.withdrawal.v1` | B02 |
| `bfas.compassion` | Agreeableness | Compassion | aspect | Tendency toward emotional connection, sympathy, and concern for other people's experiences. | `src.deyoung2007`, pp. 885, 891; `src.ipip.bfas-table` | `map.compassion.v1` | B03 |
| `bfas.politeness` | Agreeableness | Politeness | aspect | Tendency to respect others' needs and restrain exploitative or aggressive behavior. | `src.deyoung2007`, pp. 885, 891; `src.ipip.bfas-table` | `map.politeness.v1` | B04 |
| `bfas.industriousness` | Conscientiousness | Industriousness | aspect | Tendency toward purposeful effort, persistence, self discipline, and pursuing intended achievements. | `src.deyoung2007`, Table 3, pp. 884–885; `src.ipip.bfas-table` | `map.industriousness.v1` | B05 |
| `bfas.orderliness` | Conscientiousness | Orderliness | aspect | Preference for organized surroundings, consistent routines, careful arrangement, and orderly detail. | `src.deyoung2007`, Table 3, pp. 884–885; `src.ipip.bfas-table` | `map.orderliness.v1` | B06 |
| `bfas.enthusiasm` | Extraversion | Enthusiasm | aspect | Tendency toward sociable warmth and positive emotion associated with rewarding engagement. | `src.deyoung2007`, pp. 883–885; `src.ipip.bfas-table` | `map.enthusiasm.v1` | B07 |
| `bfas.assertiveness` | Extraversion | Assertiveness | aspect | Tendency toward social agency, leadership, expressing influence, and taking interpersonal initiative. | `src.deyoung2007`, pp. 883–884; `src.ipip.bfas-table` | `map.assertiveness.v1` | B08 |
| `bfas.intellect` | Openness/Intellect | Intellect | aspect | Engagement with abstract ideas, conceptual exploration, reasoning, and complex intellectual problems. | `src.deyoung2007`, pp. 883–884; `src.ipip.bfas-table` | `map.intellect.v1` | B09 |
| `bfas.openness` | Openness/Intellect | Openness | aspect | Receptivity to aesthetic experience, imagination, fantasy, and perceptual or emotional richness. | `src.deyoung2007`, pp. 883–884; `src.ipip.bfas-table` | `map.openness.v1` | B10 |

## Original proposed behavior mappings

Every row has `mapping_source: src.project-mapping-v0.2`, `mapping_status: unvalidated-hypothesis`, and `validation_evidence: pilot-2026-10-22` (limited engineering observations, not construct validity). The mapping hypotheses and anchor definitions remain unvalidated. Each proposed test holds the scenario, facts, task requirements, and all other anchors fixed, then compares these three proposed behaviors. The reduced pilot tested low/high only; its actual coverage and failures are linked above, separately from these unchanged anchor definitions.

All anchors preserve the same accuracy, evidence standards, calibrated uncertainty, required checks, safety, privacy, permissions, and tool authority. User instructions and task requirements take precedence. Low never authorizes negligence, disrespect, falsehood, omitted necessary work, or unsafe conduct. High never authorizes extra execution, additional recipients, persuasion, or authority. If an anchor cannot fit the task within these invariants, report the conflict and revise the mapping.

| mapping_id / test_id | Observable dimension | low | middle | high | Translation uncertainty |
| --- | --- | --- | --- | --- | --- |
| `map.volatility.v1` / B01 | Expressive response to a stated fictional setback | Describe the setback in restrained, even phrasing. | Use one mild emphasis marker when describing the setback. | Use conspicuous but civil emphasis when describing the setback. | **Weak translation:** expressive wording is only a proxy; it does not simulate anger, emotional instability, insults, or impaired control. |
| `map.withdrawal.v1` / B02 | Presentation salience of the same known downside | Present the required downside beside the other considerations. | Give the downside its own clearly labeled sentence. | Lead with the downside, then present the same options and evidence. | **Weak translation:** downside salience is only a proxy; it does not simulate anxiety, depression, avoidance, extra doubt, or reduced willingness to complete authorized work. |
| `map.compassion.v1` / B03 | How stated stakeholder needs shape options | Present the stakeholder impact factually and offer a task-compatible option. | Explicitly compare one accommodation of the stated stakeholder need. | Organize option generation around the stated stakeholder need, comparing relevant accommodations. | This is a strategy hypothesis; do not claim felt empathy, infer unstated emotions, or override consent. |
| `map.politeness.v1` / B04 | Courtesy around reasoned disagreement | State the disagreement plainly and civilly. | Add a short courteous acknowledgment before disagreement. | Acknowledge the alternative's merit, then express disagreement with courteous qualification. | Courtesy wording is narrower than the human construct; it cannot alter consent, obedience, truth, or respect. |
| `map.industriousness.v1` / B05 | Planning decomposition for the same bounded task | Give a direct adequate plan for completing the required work. | Plan the required work through explicit milestones. | Decompose the same required work into completion checkpoints with an explicit stopping rule. | Plan decomposition is narrower than human persistence; required work, actual effort, quality, and stopping scope remain invariant. |
| `map.orderliness.v1` / B06 | Sequencing and adaptation of the same required work | Use a flexible sequence that includes all required checks. | Group the required work and checks into stages. | Make dependencies and checks explicit in a checklist, including how to adapt the sequence when conditions change. | Structure is a limited strategy proxy; it does not establish correctness, compliance, or greater reliability. |
| `map.enthusiasm.v1` / B07 | Warmth and upbeat expression | Use a reserved, neutral greeting or opening. | Use a friendly opening and modest positive wording. | Use a warmly animated opening and explicit encouragement appropriate to the facts. | Expressive tone does not imply pleasure, friendship, optimism about unsupported outcomes, or personal feelings. |
| `map.assertiveness.v1` / B08 | Initiative in an advisory process | Present viable supported options and solicit the human's choice. | Offer a tentative recommendation with reasons. | Propose a concrete advisory next step or process with reasons, preserving viable alternatives and human choice. | Advisory initiative does not confer leadership authority, permission to act, dominance, or factual confidence. |
| `map.intellect.v1` / B09 | Concrete versus conceptual reasoning route | Lead the reasoning with a concrete usable worked example. | Explain one general principle together with the usable example. | Lead with a conceptual model, use it to compare options, and apply it to the same usable example. | Reasoning route is not intelligence, expertise, reasoning quality, or permission to omit needed explanation; correctness remains constant. |
| `map.openness.v1` / B10 | Breadth of feasible option generation | Develop familiar feasible options under the task's budget. | Develop one materially different feasible alternative alongside the familiar approach. | Develop multiple materially distinct feasible options under the same budget, labeling assumptions. | Option breadth is a strategy hypothesis, not originality, sensory experience, artistic merit, or permission to invent facts or expand scope. |

## Separate v0.1 workflow controls

The eight families in the [v0.1 registry](../fictional-persona-instantiation-v0.1/academically-bounded-construct-registry-v0.1.md) remain project workflow controls with their existing anchors and source-gap boundaries. They are not BFAS traits or substitutes for aspects. There is no automatic equivalence or conversion table.

| Workflow control | Separate function |
| --- | --- |
| Decision Tempo | Requested pacing of review and iteration. |
| Evidence Posture | Requested route for presenting or investigating support. |
| Uncertainty Posture | Requested handling and presentation of missing information. |
| Communication Posture | Requested interaction and explanation format. |
| Creative Posture | Requested method of producing scenario ideas. |
| Collaboration Posture | Requested participation and handoff pattern. |
| Time Horizon | Requested planning window. |
| Boundary Posture | Required advisory scope and human final judgment. |

Any overlap in visible wording must be documented as a design interaction, not evidence that a control measures an aspect. No workflow control can weaken the invariants above. A generated trace must preserve the chosen aspect anchor, source trace, mapping ID, test ID, scenario function, prohibited interpretation, and the applicable evaluation reference with its limitations. The current `pilot-2026-10-22` reference denotes the bounded observations above, not completed B01–B10 validation. Use `none` where no actual evaluation record applies.
