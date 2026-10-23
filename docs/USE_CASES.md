# Use cases

All examples describe fictional, low-stakes advisory work. They are possible workflows, not observed model outcomes or owner choices. Start at [Quickstart](QUICKSTART.md); [onboarding](../profiles/ONBOARDING.md) accepts questions **or** free text and optional skipping.

| Workflow | Configuration and boundary |
| --- | --- |
| One advisory agent | Confirm desired behavior and assign an exact profile to one owner-chosen agent ID. No children required. |
| Parent with optional specialist children | Confirm separate assignments; agents can share the exact profile or use different confirmed combinations. A specialist role or tool permission comes from the host, not a trait. |
| Reuse across bounded writing tasks | Load the same exact bound revision afresh; finish each task. Artifact persistence is tested, behavioral stability is not. |
| Try an explicitly revised preference | Confirm a new full preview and publish a new immutable revision. Reassign only selected agents using the current-binding digest. |
| Return to a previous configuration | Confirm the rollback assignment, revalidate the retained revision and replace the current binding with its exact pins. Never overwrite history. |

See [assignment and rollback instructions](../profiles/ASSIGNMENTS.md) and [synthetic software tests](../profiles/test_assignment_journey.py). Two prior live loading answers used Politeness alone; none establishes successful trait composition.

## Separate optional legacy workflows

[Scenario rehearsal](../fictional-persona-instantiation-v0.1/README.md) and [panel synthesis](../ephemeral-persona-panel-adapter-v0.1/README.md) can explore fictional creative alternatives or preserve disagreement within a bounded review. [Persona Pack](../persona-pack-v0.1/README.md) preserves a corpus-derived descriptive persona. These formats do not automatically become desired-trait profiles or carry approval into them.

No workflow authorizes profiling real people, expert claims, high-stakes suitability judgments or autonomous final decisions. [Safety boundaries](SAFETY_BOUNDARIES.md) apply at every setting.
