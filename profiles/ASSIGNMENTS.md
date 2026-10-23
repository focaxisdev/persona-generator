# Explicit assignments, replacement and rollback

Use [ONBOARDING](ONBOARDING.md) for real desired-behavior choices and exact full-preview confirmation first. A stored profile and an assignment are separate decisions. Installation and publication do not activate preferences. Configure only the agents the owner actually needs; parent-only use needs no children. Every configured parent or child has its own agent ID and explicit binding, even when all select the same profile. A child may select a different profile or revision; no inheritance, averaging, merge or implicit latest revision exists.

## Review each intended assignment

Before binding, privately show each intended agent ID with the exact profile ID, revision, snapshot and effective digests. Ask the owner to explicitly confirm that assignment. Confirming a profile alone does not select recipients. Keep a separate local checklist outside the strict profile/binding JSON; it is an optional human record, not a new API or an authentication mechanism:

| Agent ID | Intended exact profile/revision and digests | Assignment confirmation | Actual private record reference |
| --- | --- | --- | --- |
| Owner-supplied ID | Await selection | PENDING | Await actual response |

One real response can explicitly authorize several listed agents, but silence, a synthetic test, an inferred parent choice or a model's statement cannot. Leave unrequested children unconfigured. A confirmed assignment record should identify the actual owner response and exact listed pins; never fabricate one to make a walkthrough pass. Keep real transcripts private. The compiler validates binding integrity, not assignment consent, so the operator must enforce this step.

Requirements: Python 3.9 or newer and the standard library; actual execution tested on Python 3.12.14 only, not Python 3.9. Run all commands below from this checkout. Paths and uppercase values are placeholders to replace with actual private paths, exact validated values and confirmed agent IDs; do not run them unchanged.

```sh
python -m profiles validate /absolute/private/spec.json --presented /absolute/private/preview.json
```

Use the returned `profile_id`, `revision`, `snapshot_sha256` and `effective_sha256` only for that exact validated spec. Publish once if this confirmed revision is not yet stored. Then, after actual assignment confirmation, create each requested binding independently:

```sh
python -m profiles bind --store /absolute/private/profile-store --agent AGENT_ID --profile PROFILE_ID --revision r1 --snapshot SNAPSHOT_SHA --effective EFFECTIVE_SHA
python -m profiles load --store /absolute/private/profile-store --agent AGENT_ID
python -m profiles render --store /absolute/private/profile-store --agent AGENT_ID
```

Repeat for each explicitly confirmed child only. Initial binding is create-only. `load` returns audit data including `binding_sha256`; only successful `render` stdout is the exact trusted instruction payload. A fresh invocation must load its own agent ID again. The [Codex adapter](../adapters/codex/README.md) supplies optional explicit host loading; a different host can use `load_binding` from the same compiler. Keep the bounded task separate and preserve the host's instruction hierarchy, tools and permissions. Stored bytes do not establish that a model followed them.

Missing bindings, wrong digests, stale catalog/source bytes, invalid records or tampered retained artifacts must stop loading. Do not fall back to a parent, another revision, an unbound default or hand-written replacement instructions.

## Deliberately replace one assignment

A persistent content change needs a new revision, complete new preview, genuine owner confirmation and manual review before publication. Catalog v1 to v2 also needs these steps. Publishing r2 does not move any agent from r1. Obtain explicit confirmation for the exact agent-to-r2 assignment, then read the **current validated** binding:

```sh
python -m profiles load --store /absolute/private/profile-store --agent CHILD_ID
```

Validate the retained r2 spec and exact presented preview to get its snapshot/effective pins. Copy `binding_sha256` from the fresh `load` audit into `--expected-current`; never hash the decorated audit JSON or guess an expectation:

```sh
python -m profiles validate /absolute/private/r2-spec.json --presented /absolute/private/r2-preview.json
python -m profiles bind --store /absolute/private/profile-store --agent CHILD_ID --profile PROFILE_ID --revision r2 --snapshot R2_SNAPSHOT_SHA --effective R2_EFFECTIVE_SHA --expected-current CURRENT_BINDING_SHA
python -m profiles render --store /absolute/private/profile-store --agent CHILD_ID
```

An absent expectation cannot replace even an identical existing binding. Stale or malformed expectations, a missing expected binding, or invalid old/new artifacts reject before a binding write. Investigate and reread rather than bypassing the guard. This is deliberate local replacement protection, not owner authentication or an atomic concurrent-writer transaction; coordinate writers externally. Replacing one child's binding leaves its parent, siblings and immutable profile revisions unchanged.

## Roll back by reassigning a retained confirmed revision

Rollback changes an agent binding to a previously confirmed immutable revision. It does not republish an older revision or copy old files over newer ones. First obtain the owner's explicit rollback assignment confirmation for the exact agent and retained revision. Revalidate that retained old spec and its exact presented preview to recover the old pins, and load the current agent binding to obtain a **new** expectation:

```sh
python -m profiles validate /absolute/private/r1-spec.json --presented /absolute/private/r1-preview.json
python -m profiles load --store /absolute/private/profile-store --agent CHILD_ID
python -m profiles bind --store /absolute/private/profile-store --agent CHILD_ID --profile PROFILE_ID --revision r1 --snapshot R1_SNAPSHOT_SHA --effective R1_EFFECTIVE_SHA --expected-current CURRENT_R2_BINDING_SHA
python -m profiles render --store /absolute/private/profile-store --agent CHILD_ID
```

The retained store paths are `versions/PROFILE_ID/r1/spec.json` and `versions/PROFILE_ID/r1/presented.json`; these may be used directly for `validate` instead of separate retained copies. `bind` additionally revalidates the stored revision and manifest. If the earlier version or current binding is missing or tampered, rollback rejects; do not manufacture files, reuse an old expectation or select a fallback. The earlier full-preview confirmation remains attached to that unchanged revision, while the new assignment decision requires its own actual confirmation. Any change to old content needs a new revision instead.

[The assignment journey tests](test_assignment_journey.py) exercise fictional synthetic parent/two-child assignment, catalog upgrade, deliberate single-child replacement and rollback, unchanged sibling/store bytes, fresh-process rendering and rejection paths. They establish software behavior only. Actual owner onboarding, confirmation, assignment and model behavior remain pending until genuinely performed and separately recorded.
