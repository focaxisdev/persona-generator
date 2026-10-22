# Persona Generator

用 Markdown 定義臨時、虛構、低風險的 AI 觀點與行為，讓不同看法能被檢視，最後由人做決定。本專案提供生成與審閱的規則；不建立固定人格庫，也不測量使用者人格或宣稱 AI 擁有人類特質。

**從這裡開始：**[Quickstart](docs/QUICKSTART.md) → 提供虛構情境 → 產生最少必要的觀點 → 人工審閱後停止。若要指定代理行為，可用選項或短答提出需求，再審閱規則並確認完整預覽。先看[來源](persona-design-v0.2/sources.md)與[主張／限制](docs/CLAIMS_MATRIX.md)；[v2 提案](persona-design-v0.2/mapping-v2/README.md)仍是 **NOT RUN、未發布**，不會自動取代既有流程。

[v1 試行](evaluation/pilot-2026-10-22/REPORT.md)保留 102 份合成任務輸出：30 組初始低／高對照中，僅 5 組是符合端點且無已評定違規的候選對照，其中 3 組仍有信心限制；全部輸出有 28 次超出字數預算。這些有限觀察不代表十個人格面向已實現或通過驗證。完整門檻仍未完成；詳見[發布說明草稿](docs/RELEASE_NOTES_DRAFT.md)。專案介紹與行銷範圍為 GitHub 文件。

Generate academically bounded fictional personas on demand for multi-agent rehearsal.

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

Persona Generator is a local-first, Markdown-first protocol package for creating temporary fictional personas for bounded, low-stakes scenarios. Use this when you want an AI agent to generate a few temporary fictional viewpoints for a low-stakes rehearsal, then stop with an auditable advisory summary.

**Start here:** [Quickstart](docs/QUICKSTART.md) -> [AI discovery guide](AI_DISCOVERY.md) -> [Safety boundaries](docs/SAFETY_BOUNDARIES.md).

## Traceable agent design (unreleased v0.2 candidate)

Configure **how a fictional agent should behave**, using a choice-guided or short-answer interview. The new [design protocol](persona-design-v0.2/protocol.md) names the ten Big Five **aspects** described by DeYoung, Quilty, and Peterson (2007). It separates cited human constructs from this project's proposed behavior mappings and from actual model observations.

Answers become `low`, `middle`, `high`, or `unspecified` design goals, never personality scores. Review the source trace, proposed rules, conflicts, and unknowns, then confirm the exact preview before generating a spec. Unanswered goals remain unconstrained. Accuracy, privacy, safety, and tool permissions are never personality options.

Start with the [new quickstart](docs/QUICKSTART.md). Existing v0.1 workflows remain available; see [migration](docs/MIGRATION.md). A [bounded engineering pilot](evaluation/pilot-2026-10-22/REPORT.md) retained 102 synthetic task responses in 76 fresh contexts with separate condition-blinded model ratings. Its mixed, task-specific observations do not fulfill the original behavior protocol; this increment is **not released**. See [claims](docs/CLAIMS_MATRIX.md), [evaluation protocol](validation/BEHAVIOR_PROTOCOL.md), and [release acceptance](docs/RELEASE_ACCEPTANCE.md).

## What This Is

| Persona Generator is | Persona Generator is not |
| --- | --- |
| A protocol-first Markdown workspace | A hosted service |
| A grammar for on-demand fictional personas | A static persona catalog |
| A bounded construct vocabulary for scenario design | A psychometric instrument |
| A manual-review workflow | A diagnosis tool |
| A dissent-preserving advisory aid | An autonomous decision maker |
| Optional Persona Pack handoff files | Real-person profiling infrastructure |

## Try It in Five Minutes

1. Read [docs/QUICKSTART.md](docs/QUICKSTART.md).
2. Ask your AI agent to read [AI_DISCOVERY.md](AI_DISCOVERY.md) for the smallest task-specific path.
3. Provide one fictional, low-stakes scenario brief.
4. Generate the minimum useful set of ephemeral personas.
5. Run the manual review checklist.
6. Optionally use the minimal panel adapter only when the task explicitly calls for synthesis.
7. Stop with a bounded advisory synthesis.

Copy-paste starter prompt:

```text
Read AI_DISCOVERY.md and docs/QUICKSTART.md. Use Persona Generator only for a fictional, low-stakes scenario. Generate the minimum useful set of ephemeral fictional personas, review them manually, preserve dissent, avoid static persona catalogs, and stop after a bounded advisory synthesis.

Scenario: [describe your fictional low-stakes scenario here]
Decision or rehearsal question: [what should the temporary perspectives examine?]
Why this is fictional and low-stakes: [brief boundary statement]
Desired output: [personas only / personas plus synthesis / optional handoff]
```

## How It Works

![Architecture overview](docs/assets/architecture-overview.svg)

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

Optional panel rehearsal and Persona Pack serialization are task-triggered components. They are not default runtime inventory and they do not create reusable persona presets.

## Public Example

See [examples/limited-public-beta](examples/limited-public-beta/README.md) for a fictional volunteer knowledge-sharing scenario with multiple ephemeral personas, visible dissent, a preserved minority view, and an advisory synthesis.

## Use Cases

- Product decision rehearsal for a fictional beta.
- Social-conflict perspective exploration using fictional roles.
- Creative brainstorming without permanent persona inventory.
- Pre-mortem review for reversible decisions.
- Advisory review for low-stakes plans.
- Optional handoff of one selected fictional persona through Persona Pack v0.1.

All examples are fictional fixtures for format and safety demonstration only. They are not datasets, runtime inventory, reusable presets, or a static persona catalog.

## Safety Boundaries

Persona Generator is not for real-person profiling, diagnosis, hiring, surveillance, legal, medical, credit, insurance, educational placement, or other high-stakes decisions.

Read [docs/SAFETY_BOUNDARIES.md](docs/SAFETY_BOUNDARIES.md) before adapting the workflow.

## Academic Boundaries and Evidence

Academic constructs are bounded vocabulary for scenario design. They are not psychometric measurements, validation proof, diagnosis, or real-world behavior prediction.

Read [docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md) and [docs/EVIDENCE_SUMMARY.md](docs/EVIDENCE_SUMMARY.md).

## Documentation

- [Quickstart](docs/QUICKSTART.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Academic Boundaries and Source Notes](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md)
- [Why Persona Generator](docs/WHY_PERSONA_GENERATOR.md)
- [Use Cases](docs/USE_CASES.md)
- [FAQ](docs/FAQ.md)
- [Safety Boundaries](docs/SAFETY_BOUNDARIES.md)
- [AI Discovery Guide](AI_DISCOVERY.md)
- [Experimental llms.txt](llms.txt)

## Contributing

Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), and [SUPPORT.md](SUPPORT.md).

Do not submit personal data, sensitive data, covert profiling requests, static persona catalog proposals, psychometric scoring, or high-stakes use cases.

## License

Persona Generator is licensed under [Apache-2.0](LICENSE). The license applies to this public repository's docs, protocols, templates, examples, visual assets, and future code unless a file states otherwise.

This covers the project's original material; it does not relicense cited external papers, questionnaires or other third-party materials. Their respective terms and attribution limits remain in force; consult the [source ledger](persona-design-v0.2/sources.md). 本專案授權不涵蓋外部論文或其他第三方素材的再授權。

## Star the Project

If this protocol-first approach is useful to you, consider starring the repository so other builders can find it.

## Separate v2 candidate — not released

The [mapping-v2 proposal](persona-design-v0.2/mapping-v2/README.md) offers a separate opt-in design path with [handwritten workflow illustrations](persona-design-v0.2/mapping-v2/WORKFLOW.md#handwritten-traces-not-execution-evidence). These are explanations, not model observations or owner approvals. V2 behavior and authentic owner E2E are NOT RUN; coordinator acceptance is pending and the existing workflow remains the default. Read the [sources](persona-design-v0.2/sources.md), [claims and limits](docs/CLAIMS_MATRIX.md), [acceptance proposal](persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md) and [draft release notes](docs/RELEASE_NOTES_DRAFT.md). Marketing scope is this GitHub repository and its documentation; a standalone website is not required.
