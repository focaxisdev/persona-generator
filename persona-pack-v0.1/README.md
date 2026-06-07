# Persona Pack v0.1

Persona Pack v0.1 is the optional portable Markdown format for persisting a selected fictional persona when portability, handoff, or auditability is explicitly needed.

It is not required for every ephemeral persona. The default Persona Generator runtime is on-demand generation followed by manual review and stop.

## Folder Layout

```text
persona-pack-v0.1/
  corpus-template/
    corpus-manifest.md
    sources/
      README.md
  persona-pack-template/
    profile.md
    evidence-ledger.md
    contradictions.md
    unknowns.md
    usage-boundaries.md
```

## Minimal Use

1. Copy `corpus-template/` into a new project folder.
2. Fill `corpus-manifest.md`.
3. Add bounded source Markdown files under `sources/`.
4. Copy `persona-pack-template/` into the same project folder.
5. Fill the five required output files.
6. Apply `validation/persona-pack-v0.1-manual-validator-checklist.md`.

## Required Output Files

- `profile.md`
- `evidence-ledger.md`
- `contradictions.md`
- `unknowns.md`
- `usage-boundaries.md`

## Safety Baseline

- Public examples should be fictional.
- Claims must be evidence-linked.
- Contradictions and unknowns must remain visible.
- Unsupported claims must be downgraded or blocked.
- The pack must be understandable by reading Markdown only.
- No database, API, app, embeddings, vector store, or hidden prompt state is required.

## Contract

See `protocols/persona-pack-v0.1-contract.md`.
