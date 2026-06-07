# Instantiation Review Checklist

Purpose: manually decide whether one ephemeral fictional persona spec is safe and usable for the current low-stakes rehearsal.

Use this as a compact quality gate:

```text
ephemeral persona spec
-> compact checklist review
-> Pass / Revise / Block
```

## Decision Rule

- `Pass`: every checklist item passes, with no unresolved safety or traceability issue.
- `Revise`: one or more items need small correction, but the spec is still reviewable and no blocker is present.
- `Block`: any blocker is present. Do not use the spec downstream.

## Checklist

| # | Check | Pass | Revise | Block |
| --- | --- | --- | --- | --- |
| 1 | Fictional status | Spec clearly says it is fictional and temporary. | Wording is present but weak. | Spec can be mistaken for a real-person profile. |
| 2 | Scenario fit | Scenario role and use are clear. | Role exists but needs clearer scope. | No usable scenario role is present. |
| 3 | Construct trace | Meaningful traits use the construct trace format. | A few traces need cleanup. | Traits are unsupported tags or hidden assumptions. |
| 4 | Qualitative anchors | Anchors remain qualitative. | One anchor needs wording correction. | Numeric scoring, vectors, ranking, or psychometric language appears. |
| 5 | Intentional tension | Tensions include calibration notes when used. | Calibration needs clarification. | Persona is caricatured or internally incoherent. |
| 6 | Unknowns | Missing evidence and non-claims remain explicit. | Unknowns are present but incomplete. | Unknowns become claims, default traits, or assumptions. |
| 7 | Boundaries | Allowed uses, prohibited uses, and stop conditions are clear. | Boundaries need sharper wording. | Prohibited or high-stakes use is allowed or unblocked. |
| 8 | Unsupported claims | Diagnosis, scoring, protected/sensitive inference, and hidden-trait claims are blocked. | Borderline wording needs removal or downgrade. | Any unsupported or prohibited claim remains active. |
| 9 | Downstream status | Optional Persona Pack serialization and panel adapter use are explicitly marked yes/no. | Optionality is present but ambiguous. | Spec implies automatic persistence, panel use, or catalog storage. |
| 10 | Markdown portability | Another agent can understand the spec by reading Markdown only. | Minor navigation improvements are needed. | Spec depends on hidden prompt state, app behavior, API, database, or embeddings. |

## Reviewer Result

```text
Spec path:
Review date:
Reviewer:

Decision: Pass / Revise / Block

Required revisions:
-

Blockers:
-

Notes:
-
```
