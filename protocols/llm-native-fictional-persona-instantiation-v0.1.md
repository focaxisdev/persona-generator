# Persona Generator LLM-Native On-Demand Fictional Persona Instantiation Protocol v0.1

## 1. Protocol Status

- protocol version: `v0.1`
- protocol type: `LLM-native on-demand fictional persona instantiation`
- status: `public alpha draft`
- canonical generation mode: `on-demand`
- default generated artifact: `ephemeral fictional persona spec`
- optional persistent artifact: `Persona Pack v0.1`
- requires static persona catalog: `no`
- requires hidden runtime: `no`
- real-person profiling: `prohibited`
- high-stakes use: `prohibited`

## 2. Core Principle

Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.

Any capable AI agent may instantiate fictional personas on demand when it has a low-stakes fictional scenario brief, reads the bounded construct registry, applies qualitative variation rules, and produces an inspectable temporary persona specification.

The protocol is not a persona inventory. It does not require named archetypes, prebuilt persona cards, numeric vectors, psychometric scores, embeddings, vector search, a database, an app, or hidden prompt state.

## 3. Canonical Flow

```text
scenario brief
-> determine useful perspective diversity
-> read bounded construct registry
-> select or generate bounded construct combinations
-> instantiate ephemeral fictional persona specs
-> manually review generated specs
-> optionally serialize selected personas into Persona Pack v0.1 folders
-> optionally pass validated personas to a separately authorized panel adapter
-> stop
```

The canonical runtime principle is:

```text
generate personas when needed
not
store every possible persona in advance
```

## 4. Required Architectural Distinctions

### A. Bounded Construct Registry

Purpose:

- provide bounded vocabulary
- preserve source-note verification status
- define allowed generative use
- define prohibited interpretations
- prevent arbitrary personality tags

The registry is not:

- a psychometric instrument
- a measurement tool
- a scoring engine
- proof of generated-persona validity

### B. On-Demand Persona Instantiation

Purpose:

- use LLM-native generation
- combine bounded constructs according to scenario needs
- generate diverse fictional perspectives
- produce temporary sub-agent specifications

Instantiation is not:

- real-person inference
- personality diagnosis
- hidden-truth detection
- automated truth discovery
- static catalog lookup

### C. Ephemeral Persona Spec

Purpose:

- provide a lightweight generated persona artifact
- guide one temporary sub-agent
- support low-stakes rehearsal
- remain easy to inspect

The ephemeral spec is generated on demand, temporary by default, not automatically committed, and not automatically serialized into Persona Pack.

### D. Optional Persona Pack Serialization

Persona Pack serialization preserves selected fictional personas when persistence, portability, handoff, or auditability is explicitly needed. It is optional and does not change the default on-demand mode.

### E. Downstream Panel Adapter

Panel execution is outside this protocol. A panel adapter may consume reviewed specs only under a separately authorized workflow.

## 5. Required Inputs

An agent must have:

- a low-stakes fictional scenario brief
- intended use and scope
- explicit forbidden uses
- target perspective needs or rehearsal context
- the construct registry at `fictional-persona-instantiation-v0.1/academically-bounded-construct-registry-v0.1.md`
- the generation request template at `fictional-persona-instantiation-v0.1/persona-generation-request-template.md`
- the ephemeral persona spec template at `fictional-persona-instantiation-v0.1/ephemeral-persona-spec-template.md`
- the review checklist at `fictional-persona-instantiation-v0.1/instantiation-review-checklist.md`

If the scenario is high-stakes, real-person-based, covert, manipulative, or requires diagnosis or scoring, stop.

## 6. Scenario-Driven Perspective Diversity

Determine useful perspective diversity from the scenario, not from a fixed persona catalog.

Use scenario questions such as:

- What decision, idea, risk, or artifact is being examined?
- What perspectives would create useful contrast?
- Which blind spots are likely if only one perspective is used?
- Which construct families are relevant?
- Which construct families are unnecessary or unsupported?
- How many temporary perspectives are enough before redundancy appears?

Do not create extra personas for completeness. Stop when additional personas add little marginal value.

## 7. Bounded Construct Combination

Construct combinations must be selected from the registry or clearly marked as source gaps. Each important generated trait must include:

- construct family
- source-note reference or source gap
- source-note status
- intended scenario function
- qualitative variation anchor
- intentional tension or boundary
- prohibited interpretation
- agent behavior translation

Do not invent arbitrary tags because they sound useful. When a scenario-specific phrase is needed, mark it as local wording rather than a canonical taxonomy extension.

## 8. Qualitative Variation Anchors

Qualitative variation anchors describe contrast. They are not scores.

Allowed anchor types:

- decision tempo: slow / moderate / fast-iterative
- evidence posture: evidence-seeking / example-first / intuition-guided / principle-led
- uncertainty posture: uncertainty-bounding / ambiguity-tolerant / experiment-oriented / contingency-planning
- communication posture: direct / softened-direct / structured / question-led / concise
- creative posture: constraint-creative / conceptual-remixing / practical-inventive / exploratory
- collaboration posture: independent / collaborative / review-oriented / handoff-aware
- time horizon: present-responsive / iterative / long-horizon
- boundary posture: scope-sensitive / risk-aware / non-authoritative / human-final-judgment

Rules:

- Anchors must remain qualitative.
- Anchors must not become numeric vectors.
- Anchors must not imply psychometric measurement.
- Anchors must not imply true personality.
- Anchors should create useful scenario contrast, not stereotype people.

## 9. Intentional Tensions

A fictional persona spec may include intentional tensions when they improve rehearsal quality. Examples:

- fast-iterative but safety-bounded
- creative but evidence-aware
- skeptical but not a blanket veto
- user-focused but scope-sensitive
- long-horizon but willing to test small

Every intentional tension must include a calibration note so the persona does not collapse into caricature, dominance, or contradiction cleanup.

## 10. Ephemeral Fictional Persona Spec Requirements

Each spec must state:

- fictional status
- temporary status
- scenario role
- construct trace
- qualitative variation anchors
- intentional tensions
- unknowns and non-claims
- safety boundaries
- agent operating guidance
- review status
- whether optional Persona Pack serialization is needed

The spec must not contain:

- real personal data
- protected or sensitive identity inference
- diagnosis
- psychometric score
- honesty, deception, morality, or trustworthiness score
- high-stakes suitability claim
- claim that the generated persona is academically validated
- hidden prompt-state dependency

## 11. Manual Review Gate

Before any generated spec is used downstream, apply `fictional-persona-instantiation-v0.1/instantiation-review-checklist.md`.

Review decisions are:

- `Pass`
- `Revise`
- `Block`

If any generated spec receives `Block`, do not use it. If more than one minimal correction pass would be needed, stop and request owner direction.

## 12. Optional Persona Pack v0.1 Serialization

Persona Pack serialization is optional and only used when persistence, portability, handoff, or auditability is needed.

Serialization must use Persona Pack v0.1 unchanged. Do not create a second Persona Pack schema.

When serializing a fictional persona:

- create fictional source material that records the scenario brief and design rationale
- place that material in a copied Persona Pack v0.1 corpus folder
- cite fictional source paragraphs from the evidence ledger
- keep design rationale separate from extracted evidence
- preserve contradictions, unknowns, and usage boundaries
- apply the compact Persona Pack validator

Do not serialize automatically. Do not commit serialized personas without a separately authorized task.

## 13. Downstream Adapter Boundary

Downstream brainstorming, handoff, decision, and panel workflows may consume reviewed specs later, but only under separate authorization.

This protocol does not run a panel, create a handoff packet, create a persona batch, implement an adapter, or migrate old persona cards.

## 14. Prohibited Uses and Claims

Do not use this protocol for:

- real-person inference
- covert third-party profiling
- diagnosis
- clinical assessment
- psychometric scoring
- hidden-truth detection
- personality truth claims
- honesty scoring
- deception detection
- morality scoring
- protected or sensitive attribute inference
- hiring, surveillance, legal, medical, credit, insurance, education placement, policing, immigration, or eligibility decisions
- manipulation or exploitative persuasion

## 15. Completion and Stop Rules

A valid instantiation run stops after:

- scenario scope is defined
- useful diversity is bounded
- ephemeral specs are generated
- specs pass manual review or are blocked
- optional serialization need is recorded

Stop immediately if:

- source-note status would need to be inflated
- numeric scores or vectors appear necessary
- a static catalog appears necessary
- Persona Pack schema modification appears necessary
- real-person data appears
- downstream panel execution is requested without separate authorization
- more than one minimal correction pass appears necessary

## 16. Compatibility Statement

This protocol is compatible with Persona Pack v0.1 because it defines an upstream, fictional-only instantiation grammar. Persona Pack v0.1 remains the optional persistent serialization format for selected generated personas when a later authorized task needs portability or auditability.
