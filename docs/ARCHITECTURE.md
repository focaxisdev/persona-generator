# Architecture: confirmed single-agent core

```text
desired single-agent behavior (choices or free text)
→ construct / source / coverage trace
→ exact operation proposal and complete preview
→ human confirmation of that exact content
→ versioned confirmed core spec
→ deterministic effective projection of approved rules only
→ bounded model use and version-tied evidence
→ stop
```

Canonical reader route: [README](../README.md) → [Quickstart](QUICKSTART.md) → [core contract](../core/README.md).

## Responsibilities and trust boundaries

| Layer | Responsibility | What it cannot establish |
| --- | --- | --- |
| Intent | Record desired agent behavior and skipped/contradictory requests | The owner's human personality or implied consent |
| Source/coverage | Trace human vocabulary, analogy, omissions and confounds | Transfer human research validity to agent behavior |
| Proposal/preview | Expose exact operation versions, settings, rules and complete artifact | Consent before the owner actually confirms |
| Confirmed spec | Bind the exact reviewed contract and its confirmation record | Authenticity merely because a receipt is structurally valid |
| Compiler/projection | Check contract consistency and render approved catalog rules deterministically | Model adherence, semantic safety or behavioral efficacy |
| Evidence | Retain exact input/projection versions, model context, attempts and limitations | General stability or validity beyond observed scope |

The executable rule surface is deliberately small: the new `op.planning_structure.v1` and `op.advisory_initiative.v1`. Alongside the fixed invariant boundary and any explicitly approved response-detail control, only their approved catalog rules may appear in the effective projection. Interview text, source passages, rationale, examples, and provenance are inert trace, including text that resembles instructions. Unsupported targets fail or remain unspecified; they must never be invented during rendering. Unspecified contributes no behavioral instruction.

Ten human aspects remain a vocabulary/coverage inventory. Eight have no active operation, and the two analogues omit human motives, feelings, ability, authority, and stability. [COVERAGE](../core/COVERAGE.md) owns that detail. The compiler is not a general interpreter of the old ten-aspect mapping documents.

## Why this corrects the previous architecture

Earlier entry documents mixed multi-persona rehearsal, a ten-aspect Markdown proposal, and a separate revised-mapping candidate. They did not give one clear boundary from approved intent to emitted instructions. The core makes the confirmed artifact and deterministic projection the shared boundary for interview, use, reload, and evaluation. This prevents an interview answer or citation from silently becoming a rule, avoids filling unspecified aspects, and makes evidence attributable to the exact tested operation versions. It also narrows scope to operations that can be inspected without claiming ten implemented traits.

Approval is a human action outside the compiler. Changing behavior requires a new preview and confirmation; copying a receipt cannot substitute for that action. Fresh reuse verifies the confirmed artifact rather than reconstructing it from a summary. [Owner E2E](../core/OWNER_TEST_PROTOCOL.md) and [behavioral evidence](../core/EVIDENCE_PLAN.md) remain separate prospective checks.

## Versions and optional components

The package's unreleased v0.2 candidate, `persona-core-v1` schema, catalog version, and `.v1` operation versions are separate namespaces. Historical `map.*.v1`/`map.*.v2` identifiers and validators are not aliases. There is no automatic migration or inherited approval/evidence.

[v0.1 instantiation](../fictional-persona-instantiation-v0.1/README.md), [panel rehearsal](../ephemeral-persona-panel-adapter-v0.1/README.md), and [Persona Pack](../persona-pack-v0.1/README.md) remain optional legacy extensions only when explicitly requested. No database, hosted service, model API, telemetry, static persona inventory, or hidden runtime is required for compilation. All model use remains advisory and subject to host permissions and required accuracy, privacy, safety, and task constraints.
