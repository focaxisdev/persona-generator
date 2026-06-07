# Ephemeral Persona Panel Adapter v0.1

This folder defines a minimal optional bridge from reviewed ephemeral fictional persona specs into a panel-style rehearsal.

The adapter is not the default Persona Generator runtime. Use it only when a task explicitly authorizes panel rehearsal after generated specs have passed manual review.

## Files

- `minimal-ephemeral-persona-panel-adapter-v0.1.md`: minimal adapter contract.

## Boundary

The adapter may route reviewed fictional persona specs into a bounded conversation format. It must not:

- generate new personas from a static catalog
- bypass manual review
- create scores or votes as truth
- make final decisions
- infer real-person traits
- run high-stakes workflows
- require a database, API, app, embeddings, or hidden runtime

## Default Stop

If panel execution is not explicitly authorized, stop after the reviewed ephemeral persona specs.
