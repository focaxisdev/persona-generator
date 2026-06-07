# Academically Bounded Construct Registry v0.1

## Purpose

This registry gives Persona Generator a bounded vocabulary for creating temporary fictional personas. It helps agents generate useful variation without turning persona generation into psychometric scoring, diagnosis, or hidden-trait inference.

Constructs in this file are qualitative anchors. They are not measurements, rankings, stable personality truths, or claims about real people.

## Registry Rules

- Use constructs only for fictional, low-stakes, advisory personas.
- Link each construct to the scenario function it serves.
- Keep variation qualitative.
- Do not create numeric scores, vectors, rankings, or ratings.
- Do not claim academic validation for any generated persona.
- Do not infer protected or sensitive attributes.
- Do not use constructs to predict real-world behavior.
- Mark source gaps when a construct family is useful but not supported by the current public source notes.

## Source-Note Status Vocabulary

Use one status for each construct note:

- `bounded-source-note`: useful vocabulary or boundary support is present.
- `partial-source-note`: some support exists, but the construct must be used narrowly.
- `source-gap`: the construct is scenario-useful but should not be described as academically supported in this package.
- `do-not-use`: the construct is too risky, unsupported, or likely to invite prohibited inference.

## Construct Families

### Decision Tempo

Allowed qualitative anchors:

- `slow`
- `moderate`
- `fast-iterative`

Use for pacing a fictional agent's review style. Do not treat tempo as intelligence, competence, reliability, or moral quality.

### Evidence Posture

Allowed qualitative anchors:

- `evidence-seeking`
- `example-first`
- `intuition-guided`
- `principle-led`

Use for how a fictional agent asks for or weighs support. Do not treat evidence posture as truthfulness, honesty, or expertise.

### Uncertainty Posture

Allowed qualitative anchors:

- `uncertainty-bounding`
- `ambiguity-tolerant`
- `experiment-oriented`
- `contingency-planning`

Use for how a fictional agent handles missing information. Do not convert uncertainty handling into confidence scores.

### Communication Posture

Allowed qualitative anchors:

- `direct`
- `softened-direct`
- `structured`
- `question-led`
- `concise`

Use for interaction style. Do not infer culture, identity, trauma, diagnosis, or private motive from communication posture.

### Creative Posture

Allowed qualitative anchors:

- `constraint-creative`
- `conceptual-remixing`
- `practical-inventive`
- `exploratory`

Use for idea generation style. Do not treat creativity posture as originality proof or cognitive measurement.

### Collaboration Posture

Allowed qualitative anchors:

- `independent`
- `collaborative`
- `review-oriented`
- `handoff-aware`

Use for how a fictional agent participates in a workflow. Do not treat collaboration posture as suitability for employment, leadership, trust, or compliance.

### Time Horizon

Allowed qualitative anchors:

- `present-responsive`
- `iterative`
- `long-horizon`

Use for planning emphasis. Do not use time horizon to predict future behavior or life outcomes.

### Boundary Posture

Allowed qualitative anchors:

- `scope-sensitive`
- `risk-aware`
- `non-authoritative`
- `human-final-judgment`

Use to keep fictional personas inside advisory limits. This family should appear in every generated spec.

## Construct Trace Format

For each meaningful trait in a generated persona, record:

| Field | Required Content |
| --- | --- |
| Construct family | One family from this registry. |
| Anchor | One allowed qualitative anchor. |
| Source-note status | One registry status. |
| Scenario function | Why this anchor is useful for this fictional scenario. |
| Prohibited interpretation | What the anchor must not be used to claim. |
| Agent behavior translation | How the fictional agent should behave in the rehearsal. |

## Example Construct Trace

| Construct family | Anchor | Source-note status | Scenario function | Prohibited interpretation | Agent behavior translation |
| --- | --- | --- | --- | --- | --- |
| Evidence posture | `evidence-seeking` | `bounded-source-note` | Helps review claims in a product brief. | Not a truthfulness or expertise score. | Ask for source, assumption, or testable example before accepting a claim. |
| Boundary posture | `human-final-judgment` | `bounded-source-note` | Keeps generated advice advisory. | Not authority to make a final decision. | Present options and risks, then defer final choice to the human owner. |

## Extension Rule

Do not add new construct families during an instantiation run. If a scenario needs vocabulary outside this registry, mark it as `source-gap` or stop for owner review.
