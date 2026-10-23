# Instructions for AI Agents

Persona Generator is a public distribution workspace for psychology-grounded desired-trait specifications for fictional advisory agents and their subagents. Read PROJECT_PURPOSE.md for the current product scope.

## Read First

Read [AI_DISCOVERY.md](AI_DISCOVERY.md) first, then follow the smallest task-specific path from its file map. Do not crawl the full repository by default.

## Core Rule

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## Allowed Default Use

- Fictional scenarios only.
- Low-stakes advisory work only.
- Explicit confirmed profile revisions may persist across bounded tasks; task execution remains bounded.
- Manual review before downstream use.
- Human final judgment always required.

## Prohibited Use

- Real-person covert profiling.
- Diagnosis or clinical claims.
- Psychometric scoring.
- Sensitive-attribute inference.
- Hiring, surveillance, legal, medical, credit, insurance, or educational placement decisions.
- Static persona catalog expansion.
- Autonomous final decisions.

## Runtime Inventory Boundary

Do not infer or build a runtime persona inventory from examples, templates, Persona Pack files, or adapter docs. Examples are fictional fixtures only.

## Optional Components

Use the panel adapter for explicitly requested synthesis and Persona Pack for corpus-derived descriptive persistence. Desired-trait profiles use the separate profiles/ contract with explicit per-agent bindings; do not infer binding inheritance.

## Stop Rule

Stop when the bounded task is complete. Do not add personas, panels, ongoing activity, or claims merely for completeness. Completing a task does not silently delete or revise an explicitly stored profile.
