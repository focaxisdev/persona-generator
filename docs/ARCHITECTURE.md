# Architecture: confirmed profiles and explicit application

The product purpose is a composable desired-trait specification for agents and subagents. Persistence means preserving an exact confirmed artifact across tasks, not keeping a task running or proving a model has a stable mind. See [purpose and acceptance](../PROJECT_PURPOSE.md).

```text
BFAS source vocabulary + separately versioned AI hypotheses
→ desired agent choices / short answers
→ explicit targets, exact rules, unknowns and conflicts
→ complete preview → genuine owner confirmation
→ profile ID + immutable revision + snapshot/effective digests
→ local store
→ explicit parent binding / explicit child binding / explicit child binding
→ validate exact stored originals → deterministic renderer
→ host-controlled bounded task (host policy/permissions take precedence)
→ task ends; stored profile remains available for explicit reuse
```

## Small modules, different responsibilities

| Layer | Responsibility | Does not establish |
| --- | --- | --- |
| Sources and catalog | Ten BFAS aspect definitions; thirty explicit qualitative hypothesis anchors | Human norms, latent trait scores, psychological validity or measured correlations |
| Preview and confirmation | Trace selected settings to exact rules and full presentation; retain audit data inert | Authenticity of a recorded owner action merely from JSON structure |
| Profile compiler | Strictly validate versions/dependencies and render approved catalog text only | Model adherence, feelings or stable identity |
| Store | Preserve exact original bytes per profile ID/revision and reject mutation | Automatic host discovery or authorization to keep working |
| Binding | Pin each agent's profile ID, revision and digests | Inheritance, averaging, implicit upgrade or transfer of authority |
| Codex adapter | Install an explicit-use local skill that invokes the same loader | Unobserved host activation or automatic child loading |
| Evidence | Tie tests/results to their exact version and distinguish software from behavior | Evidence transfer from another mapping or old diagnostic |

The [profile contract](../profiles/CONTRACT.md) is host-neutral. All ten aspects may be independently specified or left unspecified. A same-domain pair need not match; no random population model or total score exists. Each active rule has a local trigger and boundary. Genuine declared contradictions must be resolved explicitly; arbitrary natural-language conflict detection is not claimed. Separate role, capabilities, values, transient state, goals and permissions remain host/task concerns.

A new profile revision requires renewed confirmation. [Assignments and rollback](../profiles/ASSIGNMENTS.md) require a real assignment decision and the validated current binding digest for replacement; this is neither owner authentication nor a concurrent-writer transaction. Bindings stay pinned until explicitly changed; child changes do not mutate the parent's binding. Current task facts and constraints override preferences temporarily without writing to the profile. Human final judgment, safety, accuracy and privacy remain invariant.

## Version routing and preserved concepts

- [Profiles](../profiles/README.md): new `persona-profile-v1` specification/storage/binding path; explicit catalog v1/v2 pins `hyp.*.v1` and the v2 Politeness repair `hyp.politeness.v2`. Hypotheses have no scientific behavioral validation.
- [Two-operation core](../core/README.md): preserved `persona-core-v1` diagnostic path. Its ephemeral scope and one-answer/no-delegation envelope remain unchanged and apply only to that adapter.
- [Persona Pack](../persona-pack-v0.1/README.md): existing corpus-derived descriptive persistence, distinct from the new desired-trait profile.
- [Scenario rehearsal](../fictional-persona-instantiation-v0.1/README.md) and [panel adapter](../ephemeral-persona-panel-adapter-v0.1/README.md): optional bounded workflows, not the default trait product.

No implicit schema migration, inherited confirmation or inherited behavioral evidence exists. All experiments, including the [six-cell pause](../evaluation/core-triage-v2/records/REPORT.md), remain unchanged. This increment adds no server, model service, orchestration framework, website or experiment.
