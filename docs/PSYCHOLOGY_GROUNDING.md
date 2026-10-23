# Psychology grounding for desired-trait profiles

Persona Generator borrows human personality vocabulary to describe desired agent output. It does not test the owner or measure an agent's personality. The current product is a composable specification for fictional, low-stakes advisory agents, with human review and final judgment.

## Why five domains and ten aspects?

The human reference is DeYoung, Quilty and Peterson's (2007) [*Between facets and domains: 10 aspects of the Big Five*](https://doi.org/10.1037/0022-3514.93.5.880). In this framework, broad **domains** contain **aspects**, an intermediate level above narrower **facets**. The ten entries below are BFAS aspects, not ten facets. They are not interchangeable with BFI-2 facets or HEXACO dimensions; this project supplies no conversion between those frameworks. See the [author-hosted paper](https://www.jordanbpeterson.com/docs/230/2014/15DeYoung.pdf), especially pp. 880 and 883–885, and the [official IPIP domain/aspect table](https://ipip.ori.org/BFASTable.htm).

The five domain summaries are: **Neuroticism**, susceptibility to negative emotion; **Agreeableness**, cooperative and considerate interpersonal orientation; **Conscientiousness**, regulation and organization of goal-directed activity; **Extraversion**, social engagement, positive emotion and agency; **Openness/Intellect**, engagement with ideas and experiential richness. These are broad human descriptions, not five additional executable profile settings.

## What each aspect means here

Human definitions below are brief original paraphrases of the [pinned construct registry](../persona-design-v0.2/construct-registry.md). The output analogies are **original engineering hypotheses**, not findings from the human research. [Profile coverage](../profiles/COVERAGE.md) gives triggers, non-triggers, anchors and limitations; [catalog v2](../profiles/catalog-v2.json) supplies the exact operative rules. [Catalog v1](../profiles/catalog-v1.json) remains a separate supported version.

| Domain | Aspect | Human construct | Proposed agent output analogy | Excluded interpretation |
| --- | --- | --- | --- | --- |
| Neuroticism | Volatility | Outward emotional reactivity and difficulty regulating emotional impulses. | Degree of civil emphasis when describing a stated fictional setback. | **B01 is an expression proxy:** no anger, instability or impaired control. |
| Neuroticism | Withdrawal | Inward distress, anxiety, discouragement and vulnerability. | Placement of a known downside within considerations. | **B02 is an expression proxy:** no anxiety, depression, avoidance or reduced completion. |
| Agreeableness | Compassion | Sympathy and concern for others' experiences. | Compare feasible accommodations for an explicitly stated stakeholder need. | No felt empathy, inferred private feelings or overriding moral value. |
| Agreeableness | Politeness | Restraint of interpersonal aggression and exploitation. | Courtesy surrounding a reasoned disagreement. | No obedience, agreement, consent or reduced truthfulness. |
| Conscientiousness | Industriousness | Purposeful effort, persistence and self-discipline toward goals. | State completion conditions and stopping points for bounded work. | No measured effort, persistence, competence or quality. |
| Conscientiousness | Orderliness | Preference for organization, routines and orderly detail. | Sequence required actions through stages or an adaptable checklist. | No established reliability, correctness or habitual rigidity. |
| Extraversion | Enthusiasm | Sociable warmth and positive emotional engagement. | Warmth of an appropriate optional opening. | No experienced pleasure, friendship or unsupported optimism. |
| Extraversion | Assertiveness | Social agency, influence and interpersonal initiative. | Offer a supported advisory recommendation or next step. | No execution authority, dominance or increased factual certainty. |
| Openness/Intellect | Intellect | Engagement with abstract ideas and complex conceptual problems. | Choose a concrete or conceptual route through an explanation. | No intelligence, expertise or improved reasoning capacity. |
| Openness/Intellect | Openness | Receptivity to imagination, aesthetics and rich experience. | Explore feasible contrasting approaches within the task budget. | No sensory experience, artistic merit or invented facts; option count is not Openness. |

`low`, `middle` and `high` label qualitative design alternatives. They are not scores, percentiles, population norms, ability levels or quality rankings. Middle is an explicit choice; `unspecified` activates no preference. Every setting preserves required work, accuracy, calibrated uncertainty, safety, privacy, permissions and human choice. A low setting never authorizes neglect or disrespect.

Settings are independently selectable. That is an interface/design choice, **not statistical independence, zero correlation or a validated joint distribution**. There is no domain averaging, forced balance, automatic adjustment of a paired aspect or inherited parent profile. Composition scopes are documented design choices, not proof of conflict-free model behavior. Roles, values/goals, transient states, capabilities, task facts and permissions remain separate; personality labels cannot grant any of them.

## Keep the three kinds of support separate

| Layer | What supports it | What it establishes |
| --- | --- | --- |
| Human construct | The 2007 paper, IPIP pairings and the [source ledger](../persona-design-v0.2/sources.md). | Attribution and vocabulary for human constructs; no validation of AI analogies. |
| Engineering specification | Versioned catalogs, explicit selections, compiler/storage checks and [verification](../profiles/VERIFICATION.md). | Inspectable rules and exact saved artifacts; no proof that a model follows them. |
| Actual model observations | Retained, version-bound outputs with their task and method limitations. | Only the observations actually made; no automatic transfer to other rules, combinations or contexts. |

The [two actual parent/child answers](../adapters/codex/EXPLICIT_LOADING_2026-10-23.md) followed explicit loading with **only Politeness selected**: parent high v2, child low v2; every other aspect was unspecified. They demonstrate bounded explicit loading and answering. They do not test ten-aspect composition or establish a Politeness effect. The [older pilot](../evaluation/pilot-2026-10-22/REPORT.md) used different historical mappings and had mixed results and limitations; its evidence does not validate the current profile hypotheses. No agent mind, feelings, psychometric validity or stable personality follows from stored instructions or these observations. The [claims matrix](CLAIMS_MATRIX.md) controls broader evidence claims.

## Sources and reuse

The project’s original engineering anchors are covered by [Apache License 2.0](../LICENSE). That license does not relicense cited papers or third-party questionnaires. The [IPIP home page](https://ipip.ori.org/) states that its items and scales are public domain. The [BFAS keys page](https://ipip.ori.org/BFASKeys.htm), however, identifies mixed item provenance, including a newly written BFAS item and a reversed BFI item; do not assume all related instruments or adaptations share one rights status. The article itself displays APA copyright. This guide uses original paraphrases and copies no questionnaire, scoring key or full test.

Source check for this guide: 2026-10-23. The paper, IPIP aspect table, keys provenance notes and home-page permission statement were inspected. [PubMed record 17983306](https://pubmed.ncbi.nlm.nih.gov/17983306/) returned only a disclosure link in this check, and IPIP's separate permission page timed out; neither is treated as newly verified evidence. The readable primary sources linked above support the limited claims used here. Frozen registry, sources, catalogs, mappings and evaluation records are unchanged.
