# Quickstart: choose, confirm, bind and reload

Start with the [project purpose](../PROJECT_PURPOSE.md), [profile guide](../profiles/README.md) and [coverage](../profiles/COVERAGE.md). This candidate configures desired agent traits for fictional, low-stakes advisory work. It does not diagnose you or grant the agent tools.

1. Choose guided questions or short answers about how you want the agent to behave. Consult the ten BFAS aspects and their separate AI hypotheses. Keep skipped settings unspecified; choose middle only explicitly.
2. Inspect each proposed rule, its trigger, source, omissions and uncertainty. Do not derive scores, force paired aspects to match, or silently resolve contradictory preferences.
3. Review the complete versioned preview. Resolve conflicts or leave the profile inactive. Confirm the exact content only after you understand it. A change creates a new revision and needs confirmation again.
4. Follow the [profile CLI examples](../profiles/README.md) to validate and publish the exact spec and presented preview to a local store. Public fixtures are synthetic demonstrations, never your approval.
5. Explicitly bind the parent and each child agent to a profile ID/revision/digest. They may share or differ. A new child context must load its own binding; conversation inheritance is insufficient.
6. Install the [Codex local skill](../adapters/codex/README.md) into an explicitly chosen repository. Invoke it explicitly with the agent ID and store location. No profile is installed or activated by default.
7. In each fresh session, validate and render the exact bound revision before applying preferences. Keep task instructions separate; temporary overrides never modify the stored profile. End the task when complete while retaining the confirmed profile for deliberate reuse.

Suggested interview request:

```text
Read PROJECT_PURPOSE.md and profiles/README.md. Help me design a desired
personality specification for my fictional advisory agent. Use guided
choices or short answers about how I want the agent to behave. Explain
source definitions separately from proposed AI behavior. Keep skipped
aspects unspecified, show conflicts and the complete preview, and wait
for my real confirmation. Do not infer my personality or create approval
on my behalf. Keep parent and child assignments explicit.
```

No paid API, model service, telemetry or account settings are needed for local validation and installation. Actual Codex discovery/use, model behavior, persistent identity and genuine owner E2E remain separate verification steps; [verification](../profiles/VERIFICATION.md) records their status.

For the unchanged two-operation experiment interface, read [core/README](../core/README.md) and its [fixed envelope](../core/REQUEST_ENVELOPE.md). That envelope is not the universal product runtime. [Persona Pack](../persona-pack-v0.1/README.md) remains a separate descriptive-persistence format. No old spec, approval or rating automatically migrates. The [paused diagnostic](../evaluation/core-triage-v2/records/REPORT.md) does not resume through this quickstart.
