# Persona Generator AI Discovery Guide

Persona Generator is a local-first Markdown protocol package for generating academically bounded fictional personas on demand for multi-agent rehearsal.

Core principle:

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Intended Use

- Generate temporary fictional personas for bounded low-stakes scenarios.
- Review generated personas manually before downstream use.
- Preserve uncertainty, dissent, and safety boundaries.
- Use optional panel rehearsal only when the task explicitly asks for synthesis.
- Use optional Persona Pack serialization only when the task explicitly needs persistence, auditability, or handoff.

## Prohibited Use

- No real-person profiling.
- No diagnosis.
- No psychometric scoring.
- No sensitive-attribute inference.
- No high-stakes decisions.
- No static persona catalog.
- No autonomous final decision.

## Configure Desired Agent Behavior (unreleased v0.2)

For a request to configure the agent's personality or to run a choice/short-answer interview, use this path instead of the legacy generation path below:

1. [Safety boundaries](docs/SAFETY_BOUNDARIES.md).
2. [Design protocol](persona-design-v0.2/protocol.md) and [interview](persona-design-v0.2/interview.md).
3. [Named aspect registry](persona-design-v0.2/construct-registry.md) and [source ledger](persona-design-v0.2/sources.md).
4. [Spec template](persona-design-v0.2/spec-template.md) and [static validation](validation/README.md).

Stop at a preview until the user confirms it. Missing answers stay `unspecified`; unresolved contradictions block the final spec. Ask about desired agent behavior, never infer a user's personality. Keep legacy workflow controls separate from BFAS aspects. All mappings remain proposed. The [bounded engineering pilot](evaluation/pilot-2026-10-22/REPORT.md) records 102 synthetic responses with mixed instruction-following observations; the full behavior protocol remains NOT COMPLETED and release remains BLOCKED. The [claims matrix](docs/CLAIMS_MATRIX.md) controls descriptions of this increment.

## Shortest Canonical Reading Path

1. [docs/QUICKSTART.md](docs/QUICKSTART.md)
2. [docs/SAFETY_BOUNDARIES.md](docs/SAFETY_BOUNDARIES.md)
3. [docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md)
4. [fictional-persona-instantiation-v0.1/persona-generation-request-template.md](fictional-persona-instantiation-v0.1/persona-generation-request-template.md)
5. [fictional-persona-instantiation-v0.1/ephemeral-persona-spec-template.md](fictional-persona-instantiation-v0.1/ephemeral-persona-spec-template.md)
6. [fictional-persona-instantiation-v0.1/instantiation-review-checklist.md](fictional-persona-instantiation-v0.1/instantiation-review-checklist.md)
7. Optional, only when task-triggered: [ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md](ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md)
8. Optional, only when task-triggered: [protocols/persona-pack-v0.1-contract.md](protocols/persona-pack-v0.1-contract.md)

## Machine-Readable Architecture Summary

```text
fictional_low_stakes_scenario
-> bounded_construct_vocabulary
-> on_demand_ephemeral_personas
-> manual_review
-> optional_panel_rehearsal
-> dissent_preserving_synthesis
-> optional_persona_pack_handoff
-> stop
```

## Task-Based File Map

| Task | Start Here | Stop Condition |
| --- | --- | --- |
| Understand the project | [README.md](README.md) | You understand the core principle and safety boundary. |
| Generate personas | [fictional-persona-instantiation-v0.1/persona-generation-request-template.md](fictional-persona-instantiation-v0.1/persona-generation-request-template.md) | Minimum useful personas are reviewed. |
| Review personas | [fictional-persona-instantiation-v0.1/instantiation-review-checklist.md](fictional-persona-instantiation-v0.1/instantiation-review-checklist.md) | Pass, Revise, or Block is recorded. |
| Run optional panel rehearsal | [ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md](ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md) | One bounded synthesis is complete. |
| Serialize for handoff | [protocols/persona-pack-v0.1-contract.md](protocols/persona-pack-v0.1-contract.md) | Persona Pack files are complete and manually reviewed. |
| Audit or discover boundaries | [docs/SAFETY_BOUNDARIES.md](docs/SAFETY_BOUNDARIES.md) + [docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md) | Boundary summary complete; no generation performed. |

## Examples

Examples are fictional fixtures for format and safety demonstration only. They are not runtime inventory, datasets, reusable presets, or a static persona catalog.

## Bounded Claims

- Bounded fictional dry-runs support this package as an inspectable protocol foundation.
- The evidence does not establish general reliability or real-user readiness.
- Academic constructs are vocabulary for description and generation, not scores.

## Unsupported Claims

No psychometric validity, personality truth detection, diagnosis, real-user readiness, high-stakes suitability, cross-provider reliability, or autonomous decision suitability is claimed.

## Stable Terms

- `ephemeral persona`: a temporary fictional perspective generated for one bounded scenario.
- `Persona Pack v0.1`: optional Markdown handoff format.
- `panel rehearsal`: optional advisory synthesis across reviewed fictional personas.
- `bounded construct vocabulary`: descriptive vocabulary, not measurement.

## Stop Conditions

- Stop if the scenario is real-person, high-stakes, covert, diagnostic, or surveillance-oriented.
- Stop if more personas would only create redundancy.
- Stop after one bounded advisory synthesis unless a new task is explicitly authorized.
- Do not scan the entire repository by default.
