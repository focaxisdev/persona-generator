# Minimal Ephemeral Persona Panel Adapter v0.1

## Purpose

This adapter describes how to route reviewed ephemeral fictional persona specs into a bounded multi-agent rehearsal without changing the Persona Generator protocol or Persona Pack v0.1 contract.

## Inputs

- One low-stakes fictional scenario brief.
- Two or more ephemeral fictional persona specs.
- Each spec has review status `Pass`.
- Explicit authorization to run a panel-style rehearsal.

## Output

A Markdown panel transcript or synthesis that records:

- scenario
- participating fictional persona specs
- allowed use
- prohibited use
- question or artifact under review
- each persona's bounded contribution
- disagreements and dissent
- unknowns
- human-final-judgment reminder
- stop status

## Adapter Rules

- Do not create new personas inside the adapter.
- Do not use specs with review status `Revise`, `Block`, or `Not reviewed`.
- Preserve each persona's non-claims and boundaries.
- Keep contributions advisory and fictional.
- Preserve disagreement instead of forcing consensus.
- Do not convert output into votes, rankings, suitability scores, or truth claims.
- Do not serialize anything into Persona Pack unless separately authorized.

## Minimal Panel Flow

```text
reviewed ephemeral specs
-> restate scenario and boundaries
-> ask one bounded question
-> collect concise persona responses
-> identify agreement, disagreement, unknowns, and risks
-> produce advisory synthesis
-> stop
```

## Stop Conditions

Stop if:

- a spec lacks `Pass` review status
- real personal data appears
- high-stakes use appears
- diagnosis or scoring appears
- the panel is asked to make the final decision
- a persona boundary conflicts with the requested task
