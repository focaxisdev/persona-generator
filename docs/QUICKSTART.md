# Quickstart

This quickstart shows how to use Persona Generator in a fictional, low-stakes scenario.

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
