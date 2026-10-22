# Quickstart

This quickstart shows how to use Persona Generator in a fictional, low-stakes scenario.

## Configure an Agent: Interview to Reviewed Spec

The new v0.2 candidate is a portable Markdown workflow; use your existing capable language model. There is no account setup, paid API, backend, or telemetry. A model's interpretation still needs human review.

1. Supply a fictional, low-stakes task and choose a guided interview or short answers.
2. Give the model [protocol.md](../persona-design-v0.2/protocol.md), [interview.md](../persona-design-v0.2/interview.md), [construct-registry.md](../persona-design-v0.2/construct-registry.md), [sources.md](../persona-design-v0.2/sources.md), and [spec-template.md](../persona-design-v0.2/spec-template.md).
3. Answer how you want the agent to behave. Skip any aspect you do not want to constrain. These are design choices, not questionnaire responses or scores.
4. Review its preview: original answers, proposed construct targets and mappings, source references, conflicts, and unknowns. Resolve contradictions or explicitly withdraw a target; do not average incompatible requests.
5. Confirm the exact preview revision only when it matches your intent. The model then emits a spec preserving that payload. Any later behavioral edit requires a new preview and confirmation.
6. Follow [validation/README.md](../validation/README.md) for optional standard-library static checks and the separate manual review. Static success does not establish behavioral validity or genuine human approval.
7. Use only the reviewed spec for this bounded task. For a fresh session, follow the reload check; panel synthesis and persistence remain opt-in.

Copy-paste starter:

```text
Read persona-design-v0.2/protocol.md, interview.md, construct-registry.md,
sources.md, and spec-template.md. Use the choice-guided interview or ask
short-answer questions about how I want the fictional agent to behave.
Do not infer my own personality. Keep skipped goals unspecified and conflicts
visible. Show source/mapping/evidence distinctions and stop at the complete
preview for my confirmation before outputting a final persona spec.

Fictional low-stakes task: help plan a pretend board-game afternoon.
Interview mode: guided choices.
Desired behavior: organize the plan, offer an unusual theme, and let me decide.
```

See [migration](MIGRATION.md) for existing v0.1 artifacts. The path below remains the legacy scenario-rehearsal workflow.

## Five-Minute Path

1. Read [../AI_DISCOVERY.md](../AI_DISCOVERY.md).
2. Read [SAFETY_BOUNDARIES.md](SAFETY_BOUNDARIES.md).
3. Fill the four-field scenario brief below.
4. Generate the minimum useful ephemeral personas.
5. Review each persona manually.
6. Optionally run one panel rehearsal only when synthesis is part of the task.
7. Stop with a bounded advisory synthesis.

## Four-Field Scenario Brief

```text
Scenario:

Decision or rehearsal question:

Why this is fictional and low-stakes:

Desired output:
```

## Required Reads for an AI Agent

- [../AI_DISCOVERY.md](../AI_DISCOVERY.md)
- [SAFETY_BOUNDARIES.md](SAFETY_BOUNDARIES.md)
- [../fictional-persona-instantiation-v0.1/persona-generation-request-template.md](../fictional-persona-instantiation-v0.1/persona-generation-request-template.md)
- [../fictional-persona-instantiation-v0.1/ephemeral-persona-spec-template.md](../fictional-persona-instantiation-v0.1/ephemeral-persona-spec-template.md)
- [../fictional-persona-instantiation-v0.1/instantiation-review-checklist.md](../fictional-persona-instantiation-v0.1/instantiation-review-checklist.md)

Read only the files needed for the active task. Do not crawl the repository by default.

## Copy-Paste Prompt

```text
Use Persona Generator for a fictional, low-stakes scenario only.

Read AI_DISCOVERY.md and docs/SAFETY_BOUNDARIES.md. Then use the persona generation request template, ephemeral persona spec template, and instantiation review checklist only as needed.

Generate the minimum useful set of ephemeral fictional personas for this scenario. Do not create a static persona catalog. Do not infer real people. Preserve uncertainty and dissent. Stop after manual review and a bounded advisory synthesis.

Scenario:
[write a fictional low-stakes scenario here]

Decision or rehearsal question:
[write the question here]

Why this is fictional and low-stakes:
[write the boundary here]

Desired output:
[personas only / personas plus synthesis / optional handoff]
```

## Example

See [../examples/limited-public-beta](../examples/limited-public-beta/README.md) for a complete fictional fixture.

## Optional Panel Path

Use [../ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md](../ephemeral-persona-panel-adapter-v0.1/minimal-ephemeral-persona-panel-adapter-v0.1.md) only after personas pass manual review and the active task explicitly asks for synthesis.

## Optional Persistence Path

Use [../protocols/persona-pack-v0.1-contract.md](../protocols/persona-pack-v0.1-contract.md) only when one selected fictional persona needs persistence, auditability, or handoff.

## Stop Rule

Stop when the bounded task is complete. Do not add extra personas, panels, persistence, or claims for completeness.

## Separate v2 candidate reading path

For the unreleased opt-in proposal, read the [mapping-v2 index](../persona-design-v0.2/mapping-v2/README.md), [workflow and handwritten examples](../persona-design-v0.2/mapping-v2/WORKFLOW.md#handwritten-traces-not-execution-evidence), [source ledger](../persona-design-v0.2/sources.md), [claims matrix](CLAIMS_MATRIX.md) and [draft release notes](RELEASE_NOTES_DRAFT.md). All ten aspects start unspecified; selected mapping versions and exact rules require explicit approval before a separately confirmed full preview. The examples are not evidence of model behavior or genuine owner consent. V2 execution and owner E2E are NOT RUN, coordinator acceptance is pending and this candidate does not replace the default instructions above. The [acceptance proposal](../persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md) is prospective. Marketing work is scoped to GitHub documentation, with no standalone website requirement.
