# Persona Generator

**Traceable personality design for an agent and its subagents.** Configure a combination of desired traits, inspect their psychological sources and proposed AI behavior, confirm the complete specification, and load the same explicit profile revision again.

**UNCONFIGURED experimental source candidate (unreleased):** ten BFAS aspects now have versioned specification semantics, not demonstrated human personality or psychometric validity. New behavioral hypotheses have no inherited results from earlier experiments. [繁體中文](README.zh-TW.md) · [Project purpose and acceptance](PROJECT_PURPOSE.md)

**Choose questions OR free text, or skip:** [owner onboarding](profiles/ONBOARDING.md) · [parent/optional-child assignments and rollback](profiles/ASSIGNMENTS.md) · [readable psychology definitions](docs/PSYCHOLOGY_GROUNDING.md).

**Start:** [Quickstart](docs/QUICKSTART.md) → [desired-trait profiles](profiles/README.md) → [Codex installation](adapters/codex/README.md).

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Choose behavior, review, confirm, load

Guided choices or short answers ask how the agent should behave—not what personality the owner has. Unanswered aspects stay `unspecified`; contradictory requests remain visible until resolved. Preview exact sources, hypothesis rules, unknowns, exclusions and the complete artifact before actual confirmation. Edits require a new revision and confirmation.

The profile layer covers the existing five Big Five domains and ten BFAS **aspects**, not facets. Low, middle and high are design targets, not scores or percentiles. Each aspect is independently selectable; this implies neither statistical independence, zero correlation nor a validated joint distribution. Each selected hypothesis renders explicit bounded preferences; no balancing or population correlations are invented. B01/B02 remain experimental expression proxies. Read [coverage](profiles/COVERAGE.md) and [source limits](core/SOURCES.md).

A local store preserves exact confirmed profile revisions. Parent and child agents each bind an explicit profile ID, revision and digests; they may share a profile or use different ones. A child change does not silently change its parent. Task completion ends the task, not the saved profile. Tools, capabilities, role, values and transient states are separate host concerns. Safety, accuracy, privacy and permissions cannot become personality sliders.

## What can be checked locally

The profile tooling and Codex adapter require **Python 3.9 or newer** and the standard library; the tested interpreter is **Python 3.12.14**. Python 3.9 is the implementation minimum, not an execution-tested interpreter in this check.

Standard-library Python validates the confirmed artifact, saves immutable revisions and deterministically renders catalog rules. Interview/source/history text remains inert. The Codex adapter installs a repository-local explicit-invocation skill; it does not change account settings or automatically assign a persona. Fresh sessions and spawned agents must explicitly load and verify their binding. See [verification](profiles/VERIFICATION.md) for tested versus manual/unverified steps.

File persistence does not establish automatic host reload, consistent model behavior, felt emotion, human psychometric validity, or cross-model stability. Structural confirmation receipts cannot prove that a real owner approved. Public examples use synthetic choices and synthetic receipts only.

One [repository-guided explicit-loading demonstration](adapters/codex/EXPLICIT_LOADING_2026-10-23.md) now records an actual parent and independently delegated child reading the installed skill, running their own validated loader and answering a bounded synthetic task. Both live answers used **Politeness alone**, with every other aspect unspecified. They establish explicit loading, not composition validity. Native discovery remains unverified and optional for explicit loading; this integration is not behavioral validation. Catalog v2 adds a neutral Politeness fallback, while existing v1 specs remain unchanged; deliberate binding replacement requires an expected-current digest.

## Evidence stays tied to its version

This increment runs **zero behavior experiments**. [Core triage v2 remains paused](evaluation/core-triage-v2/records/REPORT.md) at six answers (one carried, five new) and twelve locked new ratings: seventeen diagnostic calls. Remaining cells do not resume automatically. The earlier [v1 pilot](evaluation/pilot-2026-10-22/REPORT.md) retains 102 outputs, 5/30 candidate contrasts (three limited-confidence) and 28 word-budget violations. These results do not validate the new ten-aspect hypotheses.

The **UNCONFIGURED experimental source-package** candidate covers inspectable install/configure/load software separately from scientific validation. It activates no persona. Genuine private owner preference/spec/assignment confirmation and fresh reuse remain unverified and non-gating for this distribution; authentic confirmation is still required before later activation. [Exact packaging and checklist](docs/SOURCE_PACKAGE.md) await coordinator artifact review and separate release authorization. The original scientific gate remains unmet and unwaived. Authentic owner E2E, composition behavior, persistent identity and general behavioral stability remain unverified. [Claims](docs/CLAIMS_MATRIX.md) · [Release acceptance](docs/RELEASE_ACCEPTANCE.md) · [Draft release notes](docs/RELEASE_NOTES_DRAFT.md).

## Other supported concepts

[Persona Pack](persona-pack-v0.1/README.md) supports corpus-derived descriptive persistence; it is not the desired-trait profile. [Two-operation core](core/README.md) remains an unchanged limited diagnostic implementation, and its one-answer evaluation adapter is not the universal product runtime. [Scenario rehearsal](fictional-persona-instantiation-v0.1/README.md) and [panel synthesis](ephemeral-persona-panel-adapter-v0.1/README.md) remain optional. No automatic migration or inherited approval/evidence is implied. [Architecture](docs/ARCHITECTURE.md) · [Migration](docs/MIGRATION.md).

Fictional, low-stakes advisory use; human final judgment. No real-person covert profiling, diagnosis, psychometric scoring, sensitive inference, high-stakes placement or autonomous final decisions. [Safety](docs/SAFETY_BOUNDARIES.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md).

Original repository material is [Apache-2.0](LICENSE). Research, questionnaires and third-party text retain their own rights; no complete instrument is redistributed or relicensed. GitHub documentation is the marketing surface; no standalone website is required.
