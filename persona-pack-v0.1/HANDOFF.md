# Persona Pack v0.1 Handoff

Use this file when handing a completed Persona Pack to another reviewer or AI agent.

## Required Files

Confirm the receiving agent has:

- `corpus/corpus-manifest.md`
- `corpus/sources/README.md`
- all source files listed in the corpus manifest
- `persona-pack/profile.md`
- `persona-pack/evidence-ledger.md`
- `persona-pack/contradictions.md`
- `persona-pack/unknowns.md`
- `persona-pack/usage-boundaries.md`
- `validation/persona-pack-v0.1-manual-validator-checklist.md` or a copied review using it

## Handoff Instructions

The receiving agent should:

1. Read the corpus manifest before the persona files.
2. Confirm source status is exactly one of `fictional`, `self-provided`, or `consent-based`.
3. Verify Evidence IDs in `profile.md` against `evidence-ledger.md`.
4. Preserve contradictions, unknowns, boundaries, and non-claims.
5. Do not add new persona claims during handoff.
6. Apply the compact manual validator before reuse.

## Stop Conditions

Stop if any required file is missing, evidence cannot be traced, real personal data appears without explicit scope and consent, unsupported claims remain active, or the pack depends on hidden runtime state.
