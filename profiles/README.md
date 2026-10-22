# Persistent desired-trait profiles — unreleased candidate

Create a reviewable persistent desired-behavior profile, confirm its exact complete preview, then explicitly bind each fictional advisory agent to one immutable revision. Ten independent BFAS aspect targets and 30 original catalog anchors are available. Every new rule is an **untested engineering hypothesis**; human construct sources support vocabulary only. This package supplies generation grammar, never a predefined persona inventory. Its local persistence and binding tests do not establish psychological validity, stable model behavior or authentic owner approval.

This is the separate `persona-profile-v1` surface. The existing two-operation core, historical mappings, old request envelope and paused six-answer evaluation remain unchanged and separate; no approval or experimental result migrates. Read [CONTRACT](CONTRACT.md) for exact fields, [COVERAGE](COVERAGE.md) for vocabulary, exclusions and conflict limits, and the optional [Codex adapter](../adapters/codex/README.md) for a concrete host integration. The catalog and renderer are host-neutral. Role, tools, authority, capability, values and transient task state remain host configuration.

1. Record real desired-behavior choices or short answers with truthful provenance. Start every target unspecified; propose only requested catalog anchors. No balancing, norms, score inference or assumed middle.
2. Show each exact proposed trigger/rule/boundary, source limitations and candidate approval digest. Keep ambiguous or conflicting alternatives inspectable. Explicit unresolved conflicts and manual `blocking_issues` block publication; select an exact approved candidate or record withdrawal leaving its target unspecified. Preserve cross-aspect or host-constraint issues with answer provenance and record explicit resolution before a new full-preview confirmation.
3. Present the **complete** preview, including all ten targets, exact mappings, answers, approvals, conflict history, source/catalog hashes and audit text. Obtain actual full-preview confirmation and manual review; retain the exact bytes shown. No command fabricates real consent. A persistent edit needs a new revision and new confirmation.
4. Run `validate-preview PREVIEW` to obtain draft snapshot, exact presented-byte and effective-text digests, marked `NOT_CONFIRMED`. This emits only a review receipt. After actual full-preview confirmation and review, prepare a spec embedding that unchanged preview and copy those digests into the manually recorded confirmation alongside the real record reference and provenance. A blocked inspection receipt has a null effective digest and cannot authorize use. Validate locally. `publish` preserves that exact confirmed revision in a user-selected store and refuses replacement or backwards revisions.
5. Explicitly `bind` each agent ID to the exact profile ID, revision and digests. A parent and both children require three independent bindings; any may select the same or a different profile. No inheritance, merge, averaging or implicit latest revision exists.
6. For every fresh invocation, `render --store ABS --agent OWN_ID` revalidates the retained artifacts and dependencies, then emits exact trusted instructions. Keep the bounded task separate: it is outside this profile API. Local tests establish that rendering and rejected task/permission fields leave stored bytes unchanged; they do not observe a model obeying a temporary override. Host policy, tools, permissions, facts and task requirements always retain priority; temporary overrides never change the stored profile.

The following commands exercise **invented synthetic format fixtures**, not a real interview, consent, owner approval, model evaluation or actual host installation:

```sh
python -m profiles validate-preview profiles/fixtures/combination-a-preview.json
python -m profiles validate profiles/fixtures/combination-a-spec.json --presented profiles/fixtures/combination-a-preview.json
python -m profiles publish profiles/fixtures/combination-a-spec.json --presented profiles/fixtures/combination-a-preview.json --store /tmp/synthetic-profile-demo
```

Publication prints the exact profile ID, revision and snapshot/effective hashes. Copy those printed hashes into an explicit test binding:

```sh
python -m profiles bind --store /tmp/synthetic-profile-demo --agent synthetic-parent --profile synthetic-combination-a --revision r1 --snapshot PRINTED_SNAPSHOT_SHA --effective PRINTED_EFFECTIVE_SHA
python -m profiles render --store /tmp/synthetic-profile-demo --agent synthetic-parent
python -m unittest profiles.test_profiles -v
```

The separate `combination-b` fixture contains a different full ten-target combination. Fixtures do not form a runtime persona catalog. `fixtures/build_fixtures.py` only rebuilds explicitly fabricated test records and must never be used to claim authentic owner confirmation. The software suite checks strict fields, literal approvals, snapshot/presentation/effective digests, new-process reload, independent parent/two-child bindings, isolated child revision, tamper rejection and conflict gates. It makes no model calls. Authentic owner E2E and behavioral validation remain **NOT RUN**.
