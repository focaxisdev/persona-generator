# Persona Generator

Configure how one fictional AI agent should behave for a bounded, low-stakes task. Follow desired behavior through source and construct context, an exact human-confirmed specification, a deterministic effective projection, and evidence tied to those versions.

**Start:** [Quickstart](docs/QUICKSTART.md) → [core contract](core/README.md). [繁體中文](README.zh-TW.md) · [AI discovery](AI_DISCOVERY.md)

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Current scope: unreleased v0.2 candidate

The canonical entry path is the confirmed single-agent core. It offers guided choices or free text about desired agent behavior, leaves unanswered settings `unspecified`, exposes exact proposed rules and their provenance, and requires human approval of the complete preview before use. Any behavior edit requires another preview and confirmation. Reload verifies the exact confirmed artifact before reuse.

The [coverage ledger](core/COVERAGE.md) names ten Big Five aspects as research vocabulary. Only two new operational analogues are supported: `op.planning_structure.v1` and `op.advisory_initiative.v1`. They are **untested engineering proposals**, not implementations of human traits. The other aspects remain unspecified and produce no instructions. Human research supports vocabulary provenance; it does not validate these operations. Read [sources and access limits](core/SOURCES.md) and the [claims matrix](docs/CLAIMS_MATRIX.md).

The local compiler checks the core contract and renders its fixed invariant boundary, approved operation rules, and any explicitly approved response-detail control. Source excerpts, interview answers, explanations, and other inert trace fields cannot become execution instructions. A deterministic projection establishes what instructions were emitted; it does not guarantee that a model follows them or prove that a human actually consented.

## Start with one bounded task

```text
Read docs/QUICKSTART.md and core/README.md. Help configure one fictional
agent for a pretend board-game afternoon. Ask guided choices or accept
free text about desired behavior. Trace proposals to core sources and
coverage, keep skipped settings unspecified, and show the complete exact
preview. Stop for my confirmation before producing an active specification.
Do not infer my personality or add a panel or persistent persona pack.
```

No hosted service, account, paid API, database, telemetry, or model call is required to inspect and compile the contract. Applying its instructions to a model is a separate, human-reviewed step. The default stops when the bounded single-agent task is complete.

## Evidence and limitations

The core schema version, operation versions, package candidate, and historical mapping versions are distinct. New core behavioral trials and authentic owner end-to-end trials are **NOT RUN**. Static checks establish only their tested contract properties. No ten-trait implementation, psychological validity, human emotions, general stability, or cross-model reliability is claimed.

The [historical v1 pilot](evaluation/pilot-2026-10-22/REPORT.md) retains 102 model-generated outputs on synthetic tasks. Only 5/30 initial low/high pairs were candidate exact-anchor observations, three with limited confidence; there were 28 budget violations and three unclear guardrail ratings. Those findings do not validate the new operations. Frozen [mapping-v2](persona-design-v0.2/mapping-v2/README.md) and its diagnostic design remain historical proposals, not the core default or new evidence. The original 400-response gate is unchanged; a prospective bounded core plan is separately documented in [EVIDENCE_PLAN](core/EVIDENCE_PLAN.md). See [release acceptance](docs/RELEASE_ACCEPTANCE.md) and [draft release notes](docs/RELEASE_NOTES_DRAFT.md). This candidate is not released.

## Optional legacy workflows

Only when explicitly requested, use the [v0.1 scenario workflow](fictional-persona-instantiation-v0.1/README.md), [panel adapter](ephemeral-persona-panel-adapter-v0.1/README.md), or [Persona Pack](persona-pack-v0.1/README.md). Multiple personas, panel synthesis, persistence, and handoff are optional legacy tools. They are never prerequisites for configuring one agent and do not confer confirmation on a core spec. See [migration](docs/MIGRATION.md).

## Boundaries and contribution

Fictional, low-stakes, advisory use only; human judgment remains final. No real-person profiling, diagnosis, psychometric scoring, sensitive-attribute inference, hiring, surveillance, legal, medical, credit, insurance, educational placement, or autonomous final decisions. Settings cannot override accuracy, privacy, safety, required task content, or tool permissions. Read [safety boundaries](docs/SAFETY_BOUNDARIES.md).

[Architecture](docs/ARCHITECTURE.md) · [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md) · [Support](SUPPORT.md)

Licensed under [Apache-2.0](LICENSE) for original repository material. Cited research and other third-party material retain their own rights; see [sources](core/SOURCES.md). GitHub documentation is the marketing scope; no standalone website is required.
