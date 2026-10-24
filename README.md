# Persona Generator

## Define your AI agent’s personality

Choose how you want your agent to advise, communicate and approach a task. Turn those preferences into a personality specification you can review, confirm and give to your agent or explicitly assigned subagents.

Choose and combine preferences separately across the existing five Big Five domains and ten BFAS aspects; anything left `unspecified` stays inactive.

**[Start with the Quickstart →](docs/QUICKSTART.md)** · [Entry point for agents](AI_DISCOVERY.md) · [繁體中文](README.zh-TW.md)

Answer guided questions **or** describe what you want in your own words; skip anything you do not want to specify. You get a readable Markdown document with proposed rules, sources and boundaries. No installation, Python or particular host is required for this route.

The vocabulary draws on human personality research; translating it into AI behavior remains an **unvalidated engineering hypothesis**, not evidence that a model has human traits or a stable personality. Intended for fictional, low-stakes advisory use, with human final judgment.

**An example of what you could ask for:**

> For a fictional club choosing between two feasible workshop dates, I want my agent to recommend a concrete next step, explain its reasons, keep the alternatives visible and leave the decision to me.

This request targets **high Assertiveness** in the [current catalog](profiles/catalog-v2.json); the other nine aspects stay `unspecified`. It illustrates a desired preference, not an executed agent response or a ready-made persona. Review and genuinely confirm the whole proposed specification, its recipients and scope before use. [See a complete synthetic draft](examples/desired-trait-spec.md).

**UNCONFIGURED experimental source; v0.2 unreleased at the [dated checkpoint](docs/RELEASE_STATUS.md).** [Project purpose](PROJECT_PURPOSE.md) · [Psychology sources and limits](docs/PSYCHOLOGY_GROUNDING.md)

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Choose behavior, review, confirm, load

Guided choices or short answers ask how the agent should behave—not what personality the owner has. Unanswered aspects stay `unspecified`; contradictory requests remain visible until resolved. Preview exact sources, hypothesis rules, unknowns, exclusions and the complete Markdown artifact before the user actually confirms. Confirmation stays PENDING until a real response; never fabricate consent or receipts. Whole-profile confirmation may also explicitly assign listed recipients and tasks in that same response. Changed assignments or scope need actual confirmation of that change; changed document content needs review and confirmation of the whole changed revision. Unchanged confirmed profiles and assignments can be reused within their agreed scope for separately authorized bounded tasks, with explicit reading in each fresh context.

The profile layer covers the existing five Big Five domains and ten BFAS **aspects**, not facets. Low, middle and high are design targets, not scores or percentiles. Each aspect is independently selectable; this implies neither statistical independence, zero correlation nor a validated joint distribution. Each selected hypothesis renders explicit bounded preferences; no balancing or population correlations are invented. B01/B02 remain experimental expression proxies. Read [coverage](profiles/COVERAGE.md) and [source limits](core/SOURCES.md).

Save the confirmed Markdown revision and explicitly assign each parent or requested child to its exact document and bounded task scope. Give each recipient the complete document; require explicit reading again in fresh contexts. No automatic inheritance or permission transfer follows from parentage. Source notes and history stay inactive; task completion ends the task, not the saved document. Higher-priority host instructions, safety, accuracy, privacy and permissions govern. Tools, capabilities, role, values and transient states are separate host concerns.

Manual Markdown does not supply machine-checked integrity, user authentication, enforced loading or behavioral validation. Saved text does not prove stable personality. It is not an accepted strict JSON profile; no old approval migrates. The separate [profiles software guide](profiles/README.md), [strict contract](profiles/CONTRACT.md) and [Codex integration](adapters/codex/README.md) remain optional routes with their full existing requirements.

## Optional software: what can be checked locally

The profile tooling and Codex adapter require **Python 3.9 or newer** and the standard library; the tested interpreter is **Python 3.12.14**. Python 3.9 is the implementation minimum, not an execution-tested interpreter in this check.

Standard-library Python validates the confirmed artifact, saves immutable revisions and deterministically renders catalog rules. Interview/source/history text remains inert. The Codex adapter installs a repository-local explicit-invocation skill; it does not change account settings or automatically assign a persona. Fresh sessions and spawned agents must explicitly load and verify their binding. See [verification](profiles/VERIFICATION.md) for tested versus manual/unverified steps.

File persistence does not establish automatic host reload, consistent model behavior, felt emotion, human psychometric validity, or cross-model stability. Structural confirmation receipts cannot prove that a real owner approved. Public examples use synthetic choices and synthetic receipts only.

One [repository-guided explicit-loading demonstration](adapters/codex/EXPLICIT_LOADING_2026-10-23.md) now records an actual parent and independently delegated child reading the installed skill, running their own validated loader and answering a bounded synthetic task. Both live answers used **Politeness alone**, with every other aspect unspecified. They establish explicit loading, not composition validity. Native discovery remains unverified and optional for explicit loading; this integration is not behavioral validation. Catalog v2 adds a neutral Politeness fallback, while existing v1 specs remain unchanged; deliberate binding replacement requires an expected-current digest.

## Evidence stays tied to its version

This increment runs **zero behavior experiments**. [Core triage v2 remains paused](evaluation/core-triage-v2/records/REPORT.md) at six answers (one carried, five new) and twelve locked new ratings: seventeen diagnostic calls. Remaining cells do not resume automatically. The earlier [v1 pilot](evaluation/pilot-2026-10-22/REPORT.md) retains 102 outputs, 5/30 candidate contrasts (three limited-confidence) and 28 word-budget violations. These results do not validate the new ten-aspect hypotheses.

The **UNCONFIGURED experimental source-package** candidate covers inspectable install/configure/load software separately from scientific validation. It activates no persona. Genuine private owner preference/spec/assignment confirmation and fresh reuse remain unverified and non-gating for this distribution; authentic confirmation is still required before later activation. The exact alpha source and publication were approved, but publication remains blocked and no v0.2 tag/release exists at the [2026-10-23 checkpoint](docs/RELEASE_STATUS.md). Main now includes merged PR #8 and differs from that approved source; see [packaging](docs/SOURCE_PACKAGE.md). The original scientific gate remains unmet and unwaived. Authentic owner E2E, composition behavior, persistent identity and general behavioral stability remain unverified. [Claims](docs/CLAIMS_MATRIX.md) · [Release acceptance](docs/RELEASE_ACCEPTANCE.md) · [Draft release notes](docs/RELEASE_NOTES_DRAFT.md).

## Other supported concepts

[Persona Pack](persona-pack-v0.1/README.md) supports corpus-derived descriptive persistence; it is not the desired-trait profile. [Two-operation core](core/README.md) remains an unchanged limited diagnostic implementation, and its one-answer evaluation adapter is not the universal product runtime. [Scenario rehearsal](fictional-persona-instantiation-v0.1/README.md) and [panel synthesis](ephemeral-persona-panel-adapter-v0.1/README.md) remain optional. No automatic migration or inherited approval/evidence is implied. [Architecture](docs/ARCHITECTURE.md) · [Migration](docs/MIGRATION.md).

Fictional, low-stakes advisory use; human final judgment. No real-person covert profiling, diagnosis, psychometric scoring, sensitive inference, high-stakes placement or autonomous final decisions. [Safety](docs/SAFETY_BOUNDARIES.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md).

Original repository material is [Apache-2.0](LICENSE). Research, questionnaires and third-party text retain their own rights; no complete instrument is redistributed or relicensed. GitHub documentation is the marketing surface; no standalone website is required.
