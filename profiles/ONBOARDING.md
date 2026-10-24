# Optional desired-behavior onboarding

> **Optional strict JSON route.** For the primary read-and-follow Markdown workflow, with no installation or Python prerequisite, start at the [Quickstart](../docs/QUICKSTART.md). The requirements below apply to this separate software contract and remain unchanged; Markdown is not an accepted strict JSON spec.

Use this guide with [CONTRACT](CONTRACT.md) and [COVERAGE](COVERAGE.md) to prepare a fictional, low-stakes advisory agent's desired behavior. Python 3.9 or newer and the standard library are required; the tested interpreter is Python 3.12.14. Python 3.9 execution has not been verified in this check. No model call, questionnaire service or new authoring framework is required. A person or an LLM following the exact contract can assemble the JSON; the compiler validates it but cannot establish that a person agreed.

## Choose either starting route, or skip

Offer one optional opening: “Would you prefer a few guided choices, describe how the agent should behave in your own words, or skip preferences for now?” Do not require both routes. Start all ten targets at `unspecified`. A skipped question, unknown preference or absent answer stays unspecified; `middle` requires an explicit choice. Do not diagnose the owner or infer traits from their writing, job or identity.

For guided onboarding, ask one or a few relevant questions in ordinary language, such as “When an answer needs a correction, how would you like the agent to present it?” Show the selected catalog's exact alternatives before accepting a mapping, and allow skip or withdrawal. Corrections remain conditional on an actual need: do not invent a mandatory correction, disagreement, praise or greeting just to express a preference.

For free text, invite “Describe how you want this agent to behave; you can leave anything undecided.” Preserve the actual answer and privately retained record reference. Suggest only catalog anchors that plausibly express that request, identify the suggestion as an interpretation, and ask whether the exact wording fits. An ambiguity is a question or an unknown, never an inferred choice. Do not force paired aspects to agree, average them, or invent missing preferences.

No children need to be configured if the owner does not need them. Ask about assignments only after the profile is ready; [ASSIGNMENTS](ASSIGNMENTS.md) covers optional parent and child bindings.

## From a proposal to a complete preview

Keep unapproved proposals in a private human-readable worksheet outside the strict compiler JSON. For each candidate show its aspect/anchor, exact catalog `id`, `trigger`, `rule`, `boundary`, original answer reference and candidate digest. Explain the construct source and the separate untested engineering interpretation using [COVERAGE](COVERAGE.md). The source vocabulary is not evidence of AI psychological validity or stable behavior.

Record a candidate approval only after the owner actually accepts that exact candidate. Preserve that actual acceptance as an answer with its real record reference; the approval must name that answer and the mapping must include its ID in `answer_ids`. Retain the original preference answer as well when it is a separate event. It is narrower than confirmation of the whole profile. Use the exact `candidate_sha256 = digest(candidate(mapping))` operation from `profiles.compiler`; do not hash explanatory prose. Do not put a guessed approval, pending placeholder, or synthetic receipt into an owner preview. Unapproved targets may stay unspecified. Preserve real conflicts and blocking issues and obtain explicit selection, withdrawal or resolution; do not silently resolve them. An unresolved draft can be inspected but cannot be confirmed or used.

Assemble `preview.json` with exactly the [contract's preview fields](CONTRACT.md#exact-preview-and-confirmation). Use the actual owner answers (`origin: "owner"`), their truthful `choice` or `short-answer` kind and private `record_ref`; keep any supplemental worksheet outside JSON. A free-text answer uses `short-answer`. Copy mappings literally from the explicitly selected catalog, including hypothesis IDs. Fill all ten targets; emit no mapping for an unspecified target. Empty `answers` and `approvals` are allowed when everything is unspecified. Keep `evidence` exactly `{"status":"untested","behavioral_validation":false}`. Do not add role, tools, permissions, task or owner-psychology fields.

Read trusted catalog data using the existing public API rather than transcribing or rewriting rules:

```python
from profiles import compiler as c
catalog_id = 'persona-profile-catalog-v2'  # an explicit choice, never implicit latest
catalog = c.load_catalog(catalog_id=catalog_id)
# catalog['id'], c.TRUSTED_CATALOGS[catalog_id][1], catalog['dependencies']
# supply preview.catalog and preview.sources exactly.
# c.hypothesis_for_aspect(catalog, aspect) supplies each hypothesis and its anchors.
# c.digest(c.candidate(mapping)) supplies an exact candidate approval digest.
```

Catalog v1 remains supported. Moving a confirmed v1 profile to v2 changes the profile: use a new revision and new confirmation. The synthetic fixture builder is for tests only; it must never supply owner answers, approvals, confirmation or review.

## Read the whole preview and stop for actual confirmation

Make `preview.json` an indented UTF-8 document that the owner can read in full in an editor or a complete, untruncated attachment. Retain those exact bytes; a summary alone is insufficient. Accompany it with the selected catalog's full invariant `preamble` (available through `load_catalog`) and an explanation of source limitations. A usable review includes every target, exact active trigger/rule/boundary and approval, all answers and record references, conflicts and their resolutions, unknowns, blocking issues, history, evidence, catalog/source versions and hashes. Provide access to the exact source files identified there. Audit text is retained but never becomes instructions. Keep private records outside this public repository.

Run from this checkout before requesting full-preview confirmation:

```sh
python -m profiles validate-preview /absolute/private/preview.json
```

This returns the snapshot, exact presented-byte and effective-text digests with `confirmation_status: NOT_CONFIRMED`. It establishes structural validity only, even when every candidate already has an approval. It neither creates consent nor prints an active instruction payload. `--inspect-unresolved` permits blocked draft inspection, returning a null effective digest; resolve and re-preview before proceeding. Any edit, including whitespace in the presented file, requires a fresh receipt and a renewed presentation of the exact file.

Ask the owner to confirm the complete profile ID/revision, the unchanged full preview and its digests. Wait for their actual response and manual review. Until then the real full-preview confirmation and downstream assignment remain **PENDING**. Do not fill `confirmed_by`, `origin`, a private record reference or review `Pass` on their behalf. This guide supplies no real owner answer or confirmation.

Only after those events, prepare `spec.json` with exactly `schema_version`, `kind: "spec"`, the unchanged full `approved_preview`, `confirmation` and `review` as specified in the contract. Copy the three receipt hashes into confirmation without recomputing them from an edited presentation. Record the actual confirmer and confirmation reference with `origin: "owner"`, and the actual manual review reference. Do not put worksheet statuses or assignment fields in the spec.

```sh
python -m profiles validate /absolute/private/spec.json --presented /absolute/private/preview.json
python -m profiles publish /absolute/private/spec.json --presented /absolute/private/preview.json --store /absolute/private/profile-store
```

Retain the exact spec, presented preview and actual private confirmation/review records. Successful commands validate recorded assertions; they do not authenticate the people or prove model behavior. Publication stores an immutable revision; it does not assign or activate an agent. Continue with [explicit assignments](ASSIGNMENTS.md) only when requested.
