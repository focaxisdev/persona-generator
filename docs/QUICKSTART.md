# Quickstart: configure one agent

Start from [README](../README.md), then use the [core contract](../core/README.md). This unreleased v0.2 candidate configures desired behavior for one fictional, low-stakes advisory agent. Multiple personas, panels, and Persona Packs are optional legacy paths.

## Interview → confirmation → effective projection

1. Describe one fictional task and its limits. Read [safety boundaries](SAFETY_BOUNDARIES.md).
2. Choose guided choices or free text about how the agent should behave. Read the [coverage ledger](../core/COVERAGE.md) and [source scope](../core/SOURCES.md). These are design choices, not a test of your personality.
3. Consider only the two supported, untested operation proposals: planning structure and advisory initiative. Keep all other aspects unspecified; do not fill gaps from labels, role stereotypes, or source quotations. Preserve contradictions until the owner resolves or withdraws them.
4. Review the exact proposed versions, settings, literal rules, boundaries, provenance, unresolved items, and full preview. Approve the selected rules and explicitly confirm that exact complete preview. Stop if confirmation is missing.
5. Use the [core compiler instructions](../core/README.md) to validate and deterministically derive the effective projection. Trace fields remain inert; the projection includes only approved operation rules. Structural validation cannot authenticate a human.
6. Keep the spec, presented preview and projection JSON on the compiler/audit side. Use only exact `render` stdout as the persona instruction payload inside the fixed [request envelope](../core/REQUEST_ENVELOPE.md), with the bounded task as a separate component. Do not send projection metadata, aspect/condition labels, interview answers or history to the model. The local envelope builder makes no model call; its documented delegation mechanism is the supported prospective transport.
7. For a fresh session, revalidate the exact confirmed artifact and presented bytes locally, then rebuild the same rendered envelope. Stop if content, versions, or confirmation do not match. Any persistent behavior edit requires a new preview and confirmation. Stop when the task is complete.

```text
Read core/README.md, core/COVERAGE.md, and core/SOURCES.md.
Help me configure one fictional agent for a pretend board-game afternoon.
Interview mode: guided choices [or: free text].
Ask how I want the agent to organize a plan and whether to propose a
supported next step while keeping me in control. Leave skipped settings
unspecified. Show proposed sources, operation versions, exact rules,
conflicts, and the complete preview. Wait for my actual confirmation.
Do not infer my personality. Do not add a panel or persistent pack.
```

## What this demonstrates

The compiler's synthetic fixtures illustrate the artifact contract only. They are not owner consent or behavioral evidence. New operation behavior and authentic owner E2E are **NOT RUN**. Consult [claims](CLAIMS_MATRIX.md), [prospective evidence plan](../core/EVIDENCE_PLAN.md), and [private owner protocol](../core/OWNER_TEST_PROTOCOL.md). No real owner transcript should enter this public repository without specific permission.

## Optional historical tasks

If explicitly requested, follow [v0.1 instantiation](../fictional-persona-instantiation-v0.1/README.md), [panel adapter](../ephemeral-persona-panel-adapter-v0.1/README.md), or [Persona Pack](../persona-pack-v0.1/README.md). Do not silently translate old settings or approvals; see [migration](MIGRATION.md). Historical ten-aspect mapping documents and the frozen v2 diagnostic remain separate from the new core contract.
