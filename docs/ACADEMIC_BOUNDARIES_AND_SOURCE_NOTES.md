# Academic Boundaries and Source Notes

Persona Generator uses academically bounded vocabulary to make fictional persona generation more disciplined. The vocabulary helps describe scenario-relevant variation, but it is not a measurement system.

## What "Academically Bounded" Means

In this repository, academically bounded means:

- construct names are treated as cautious vocabulary, not truth claims
- source coverage is tracked explicitly
- missing support is labeled as `source-gap`
- qualitative anchors remain qualitative
- generated personas remain fictional, temporary, and advisory

## What Constructs Are For

Construct families help an AI agent create useful contrast in a fictional rehearsal. Examples include:

- decision tempo
- evidence posture
- uncertainty posture
- communication posture
- creative posture
- collaboration posture
- time horizon
- boundary posture

These families are design vocabulary for low-stakes fictional scenarios. They are not psychometric dimensions, clinical categories, validated scales, or hidden traits.

## What Constructs Are Not

Constructs must not be used as:

- psychometric measurements
- personality scores
- diagnosis
- clinical validation
- real-world behavior prediction
- proof of hidden traits
- evidence of honesty, deception, trustworthiness, morality, or suitability
- protected or sensitive attribute inference

## Source-Note Status

Use these statuses when discussing source support:

| Status | Meaning | Public Use |
| --- | --- | --- |
| `verified` | A source note has been individually checked against a stable public source. | Use narrowly and cite the checked source. |
| `partial` | A source note supports vocabulary or caution only in a limited way. | Use as boundary language, not validation. |
| `source-gap` | No reliable public source note is included in this package. | Mark the gap; do not invent or inflate support. |

## Current Public Source Coverage

This public alpha package intentionally ships a conservative source-status table rather than a broad bibliography.

| Construct Area | Public Status | Boundary |
| --- | --- | --- |
| Qualitative variation anchors | `partial` | Useful for scenario design, not measurement. |
| Manual review and traceability | `partial` | Useful as audit discipline, not proof of correctness. |
| Persona Pack portability | `partial` | Supported by bounded local dry-runs, not universal portability. |
| Real-person inference | `source-gap` | Not supported and not allowed. |
| Psychometric validity | `source-gap` | Not claimed. |
| High-stakes suitability | `source-gap` | Not claimed and not allowed. |

## Representative Source Notes

No broad external bibliography is bundled in this public alpha. This is intentional. The public package prefers honest `partial` and `source-gap` labels over decorative citations.

Future source-note contributions should include exact bibliographic details, stable URLs or identifiers where available, access status, relevance notes, and explicit claim boundaries. Citation placeholders are not academic proof.

## Practical Rule

If a generated persona needs a claim that would require psychometric validation, clinical expertise, real-person evidence, protected-attribute inference, or high-stakes suitability assessment, stop. Do not create the claim.
