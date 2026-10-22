# Persona Generator AI Discovery Guide

**Current status:** [Core triage v2 is paused for scope alignment](evaluation/core-triage-v2/records/REPORT.md): six retained answers (one byte-identical carried answer and five new), 12 fresh locked schema-valid ratings, and 17 new diagnostic calls. Frozen v2 preparation **NOT RUN** text is historical; no continuation is automatically authorized. The two operations are limited diagnostics. The intended final product remains an installable, composable, psychology-grounded specification for agents and subagents; persistence and composition remain unverified.

Canonical route: [README](README.md) → [Quickstart](docs/QUICKSTART.md) → [core contract](core/README.md). The default configures **one fictional agent's desired behavior** for a bounded, low-stakes task. Do not start by generating several personas, a panel, or a pack.

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Smallest task path

1. Read [Quickstart](docs/QUICKSTART.md), [core contract](core/README.md), and [safety boundaries](docs/SAFETY_BOUNDARIES.md).
2. Consult [coverage](core/COVERAGE.md) and [sources](core/SOURCES.md) for the proposed behavior's provenance and exclusions.
3. Collect guided choices or free text about desired agent behavior. Preserve skipped settings as unspecified and conflicts as unresolved.
4. Present exact proposed operations/rules and the complete preview for human confirmation. Do not manufacture approval or use a synthetic receipt as consent.
5. Validate the confirmed core artifact and derive its deterministic effective projection. Only approved catalog rules may become instructions; trace text stays inert.
6. Keep projection JSON as audit data. Send only exact `render` stdout plus the separate bounded task through the fixed [request envelope](core/REQUEST_ENVELOPE.md). Spec, preview, trace and aspect/condition labels never go to the evaluated model. Reconfirm edits; verify original artifacts locally before fresh-session reuse. Stop when complete.

## Contract boundaries

The unreleased v0.2 package candidate uses the new core schema and separately versioned `op.planning_structure.v1` and `op.advisory_initiative.v1`. Ten human aspects are vocabulary; only these two operational analogues are supported, and neither is behaviorally validated. Other aspects remain unspecified. Never infer a user's personality, treat settings as human scores, or fill unsupported goals from a role, source excerpt, or neighboring aspect.

Static validation cannot prove human approval, model adherence, safety, psychological validity, or stability. Read the [claims matrix](docs/CLAIMS_MATRIX.md) before describing evidence. The [core triage](evaluation/core-triage-v1/records/REPORT.md) stopped after one generator and two judge calls, both schema-invalid; zero ratings were accepted. New core behavior remains unvalidated; authentic owner E2E is NOT RUN. At preparation, the separate [rating-contract v2 repair](evaluation/core-triage-v2/README.md) was prospective NOT RUN; partial execution is now [paused](evaluation/core-triage-v2/records/REPORT.md). Its preparation maximum was: one disclosed carried answer, at most 17 new generators and 36 new judges; no old rating becomes valid and no execution follows automatically. The [evidence plan](core/EVIDENCE_PLAN.md) is prospective; the [private owner protocol](core/OWNER_TEST_PROTOCOL.md) must not be simulated into a claim of genuine consent.

## Optional historical paths

| Explicit task | Optional path | Boundary |
| --- | --- | --- |
| Rehearse multiple fictional perspectives | [v0.1 instantiation](fictional-persona-instantiation-v0.1/README.md) | Only minimum requested perspectives; manual review. |
| Synthesize reviewed perspectives | [panel adapter](ephemeral-persona-panel-adapter-v0.1/README.md) | One bounded advisory synthesis; preserve dissent. |
| Persist or hand off one selected persona | [Persona Pack](persona-pack-v0.1/README.md) | Keep core artifact and confirmation identity intact; pack alone cannot activate it. |
| Understand old design and evidence | [migration](docs/MIGRATION.md), [historical pilot](evaluation/pilot-2026-10-22/REPORT.md) | No automatic upgrades or evidence/approval transfer. |

Frozen `persona-design-v0.2` mapping-v1/v2 documents and `evaluation/diagnostic-v2` are historical research/design material, not current core runtime instructions. No v1 validator result validates a new core artifact or frozen v2 proposal. The original 400-response gate is unchanged; the old 50-response diagnostic is NOT RUN and is not a release gate.

## Stop and safety rules

Fictional, low-stakes, advisory only; human final judgment. No real-person profiling, diagnosis, psychometric scoring, sensitive-attribute inference, high-stakes decisions, static persona inventory, or autonomous final decisions. Accuracy, privacy, safety, required task content, and permissions are invariants. Stop on unresolved contradiction, missing exact confirmation, invalid or changed artifact, or completion of the bounded task. Do not crawl the repository by default. Examples are fictional fixtures, never reusable persona inventory or authentic owner evidence.
