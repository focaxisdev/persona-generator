# FAQ

## What is the current product?

An unreleased desired-trait specification and explicit loading layer for a fictional advisory agent and optional subagents. Choose a combination, inspect its sources and proposed behavior, confirm the full profile, then explicitly assign exact revisions. Start at [Quickstart](QUICKSTART.md), [optional onboarding](../profiles/ONBOARDING.md) and [assignments](../profiles/ASSIGNMENTS.md).

## Must I answer a questionnaire and write an essay?

No. Choose guided questions **or** free text, or skip preferences. Skipped aspects remain unspecified. No correction, edit, child agent or particular setting is mandatory. A change that you actually request needs a new preview and confirmation.

## Is this a personality test or a collection of fixed roles?

Neither. It configures desired agent behavior, not the owner's personality. The ten BFAS aspects provide source-grounded vocabulary; their qualitative AI rules are engineering hypotheses, not human scores or validated traits. See [readable definitions and exclusions](PSYCHOLOGY_GROUNDING.md). Role, capability, values and permissions are separate.

## Are combinations validated?

No. Traits are independently selectable, which does not imply statistical independence or a validated joint distribution. Synthetic tests check composition of exact rules and isolation of bindings. The two previous live answers used Politeness alone with every other aspect unspecified; they establish explicit loading, not composition validity or stable identity.

## What persists, and what activates it?

Only deliberately published confirmed revisions and explicit bindings persist in the local store. Installation assigns nothing. Fresh sessions and children must explicitly validate and load their own binding. Ending a task does not delete its profile or authorize ongoing work. Follow [replacement and rollback](../profiles/ASSIGNMENTS.md); the current-binding guard is not owner authentication.

## Is automatic discovery required?

No. The [Codex adapter](../adapters/codex/README.md) supports repository-guided explicit loading: the host reads installed skill instructions and invokes its validated loader. Native discovery remains unverified; the separate failed nested-CLI attempt remains unchanged. Copying profile prose into a prompt is not evidence that the host loaded it.

## What are Persona Pack and panels?

[Persona Pack](../persona-pack-v0.1/README.md) is a separate corpus-derived descriptive persistence format. [Scenario rehearsal](../fictional-persona-instantiation-v0.1/README.md) and panels are optional legacy workflows. The preserved two-operation core is a diagnostic interface, not the scope of the current profile product.

## Does this require an account, server or paid model API?

No new service is required for local validation, installation and rendering: Markdown, JSON and standard-library Python 3.9+ suffice; actual execution was tested on Python 3.12.14 only. Using a model still requires an already available host. The package grants no tools or permissions and changes no owner account settings.

## What would an experimental alpha mean?

A clearly labeled, scoped install/configure/load package, not scientific validation. The [UNCONFIGURED source-package track](RELEASE_ACCEPTANCE.md) is separate from the original unmet scientific gate and awaits exact-artifact review and release authorization. Personal confirmation/assignment/reuse remains unverified and non-gating for unconfigured distribution; genuine confirmation is required before later profile activation. No v0.2 release has occurred.

## What uses are excluded?

Real-person profiling, diagnosis, psychometric scoring, sensitive inference, high-stakes placement and autonomous final decisions. Human judgment remains final; read [safety boundaries](SAFETY_BOUNDARIES.md).

## Where should an agent start?

[AI Discovery](../AI_DISCOVERY.md). `llms.txt` is navigation metadata, not a guarantee of crawler support or host discovery. Original repository material is [Apache-2.0](../LICENSE); cited research and questionnaires retain their own rights.
