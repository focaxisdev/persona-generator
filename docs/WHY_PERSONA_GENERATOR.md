# Why Persona Generator

The goal is an inspectable, installable personality specification that an owner can compose for an agent and explicitly assign to optional subagents. The repository supplies a grammar and versioned choices, not a catalog of fixed characters.

## Trace decisions before applying them

[BFAS sources](PSYCHOLOGY_GROUNDING.md) define human constructs. Separate engineering hypotheses state the proposed observable AI behavior and what they omit. Owner choices or free text become exact candidate rules, then a complete preview. Unknowns and conflicts stay visible; real confirmation is required. Citation alone is not behavioral validation.

## Preserve the artifact deliberately

Immutable revisions and digest-pinned bindings make a prior confirmed specification reloadable and auditable. Parent and child agents can share or differ without implicit inheritance. [Replacement and rollback](../profiles/ASSIGNMENTS.md) change explicit assignments rather than rewriting old profiles. Stored bytes do not establish consistent model behavior or a human-like mind.

## Keep the interface portable and bounded

Markdown explains the process; small standard-library Python tools validate and render the exact version. The [Codex adapter](../adapters/codex/README.md) provides explicit loading without a new service. Tasks remain bounded, while confirmed profiles can be deliberately reused. Host policy, facts, safety and permissions take precedence.

Begin with [Quickstart](QUICKSTART.md) or [optional questions OR free text](../profiles/ONBOARDING.md). The [release tracks](RELEASE_ACCEPTANCE.md) distinguish useful experimental software from the still-unmet scientific validation. Optional legacy rehearsal can retain dissent, but it does not define this persistent-profile product.
