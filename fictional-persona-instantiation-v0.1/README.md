# Fictional Persona Instantiation v0.1

This folder contains the default on-demand Persona Generator workflow.

Use it when a fictional, low-stakes scenario needs temporary AI-agent perspectives for brainstorming, risk finding, tradeoff review, or rehearsal.

## Files

- `academically-bounded-construct-registry-v0.1.md`: bounded construct vocabulary and source-note rules.
- `persona-generation-request-template.md`: request template for scenario-driven generation.
- `ephemeral-persona-spec-template.md`: output format for one temporary fictional persona.
- `instantiation-review-checklist.md`: manual Pass / Revise / Block quality gate.

## Default Flow

```text
scenario brief
-> request template
-> construct registry
-> ephemeral persona specs
-> manual review
-> stop
```

Persona Pack serialization and panel adapter use are optional downstream steps. Do not perform them unless the task explicitly authorizes them.

## Safety Baseline

- fictional only by default
- low-stakes only
- advisory only
- no real-person profiling
- no diagnosis
- no psychometric scoring
- no protected or sensitive attribute inference
- no high-stakes suitability claims
- no hidden runtime dependency

## Stop Rule

Stop if the scenario needs real personal data, a static persona catalog, numeric scoring, diagnosis, eligibility decisions, or more than one minimal correction pass.
