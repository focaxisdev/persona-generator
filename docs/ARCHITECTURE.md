# Architecture

Persona Generator uses a small protocol-first architecture:

```text
fictional low-stakes scenario
-> academically bounded construct vocabulary
-> LLM-native on-demand ephemeral personas
-> manual review
-> optional minimal panel rehearsal
-> dissent-preserving advisory synthesis
-> optional Persona Pack v0.1 serialization
-> optional handoff
-> stop
```

## Layer Summary

| Layer | Role | Required? |
| --- | --- | --- |
| Scenario brief | Defines the fictional low-stakes situation. | yes |
| Construct vocabulary | Provides bounded descriptive vocabulary. | yes |
| Ephemeral personas | Temporary fictional perspectives generated on demand. | yes |
| Manual review | Blocks unsafe, redundant, or overclaimed personas. | yes |
| Panel rehearsal | Optional advisory synthesis across reviewed personas. | no |
| Persona Pack v0.1 | Optional Markdown handoff format. | no |
| Stop rule | Prevents scope creep and overclaiming. | yes |

## Non-Architecture

Persona Generator does not require an app, hosted service, database, API, embeddings, vector search, telemetry, analytics, or hidden runtime.
