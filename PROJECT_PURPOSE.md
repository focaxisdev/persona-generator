# Project purpose and bounded acceptance

Persona Generator defines a psychology-grounded, composable personality specification layer that an owner can install for an agent and explicitly assign to its subagents. It is a grammar for desired traits, not a small catalog of fixed roles. A saved profile can retain its identity and exact confirmed revision across bounded tasks; persistence of that artifact does not prove persistence of model behavior.

The owner selects how the **agent should behave**, through guided choices or short answers. The system traces proposed settings to human constructs and separately identified engineering hypotheses, preserves unknowns and conflicts, presents the complete preview, and waits for actual owner confirmation. It does not diagnose the owner. Unspecified is not middle. The two aspects within a domain need not match, and unusual combinations are not automatically invalid. Independent selection implies neither statistical independence, zero correlation nor a validated joint distribution. No population norms, correlations, total scores, forced balance or natural sampling distribution are inferred.

## Four different claims

| Layer | Deliverable | Limit |
| --- | --- | --- |
| Human theory | Existing BFAS five domains / ten aspects and attributed definitions | Source grounding is not proof of AI traits or human psychometric validity |
| Engineering specification | Versioned, confirmed settings and exact hypothesis rules | Ten renderable settings are not ten validated psychological implementations |
| Engineering persistence | Immutable revision files, exact digests and explicit agent bindings | Saved bytes and deterministic reload are not automatic host discovery or stable model identity |
| Model behavior | Future version-bound observations, including composition and repeated contexts | No new behavioral experiment or genuine owner E2E occurs in this increment |

## This increment's acceptance checklist

- [x] All ten aspects have explicit low/middle/high hypothesis semantics; unspecified emits no active preference. Expression proxies remain visibly limited.
- [x] Full preview and confirmed spec bind profile ID, revision, catalog/source versions, exact presentation bytes and effective instruction digest. Audit text is inert.
- [x] Immutable local storage and exact-version loading reject drift; a change requires a new revision and confirmation.
- [x] Parent and each child have explicit, independently checked bindings. No inheritance, averaging, implicit latest version or permission transfer.
- [x] Task constraints remain outside persistent profile state. Safety, truth, privacy and host permissions are invariants.
- [x] A repository-local Codex adapter installs into a disposable supported layout and loads synthetic profiles without changing account settings.
- [x] Static tests cover two full combinations, parent/two-child isolation, fresh-process reload, task isolation, tampering, unknown values and unresolved conflicts.
- [x] Independent review distinguishes tested installation/loading code from untested host activation and behavioral stability.

Historical implementation evidence belongs in [profile verification](profiles/VERIFICATION.md); current release preparation is tracked in [readiness verification](docs/RELEASE_READINESS_VERIFICATION.md). Checked items above refer to the original bounded implementation and synthetic checks. Later explicit host loading is documented separately and used Politeness alone, not composition. The [prospective release tracks](docs/RELEASE_ACCEPTANCE.md) separate a scoped experimental install/configure/load package from scientific validation. Genuine owner preference, full-spec and assignment confirmation and fresh reuse remain pending; reconfirmation is required only if content changes. Coordinator adoption and exact-candidate review are also pending. The original scientific gate remains unmet and unwaived.

## Deliberately separate paths

The new [desired-trait profile](profiles/README.md) is distinct from [Persona Pack](persona-pack-v0.1/README.md), which already supports corpus-derived descriptive persistence. The existing [two-operation core](core/README.md) and its one-answer/no-delegation evaluation envelope remain unchanged research/diagnostic interfaces. Their restrictions are not a universal product runtime. The [six-cell triage pause](evaluation/core-triage-v2/records/REPORT.md) remains preserved; no remaining cell resumes here.

No website, server, model service, database, autonomous agent framework, paid API, owner-account installation or new behavior experiment is part of this increment. GitHub documentation is the marketing surface. No private owner transcript belongs in the public repository without specific permission.
