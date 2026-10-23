# Independent persistent-profile implementation review

Reviewed 2026-10-22 against base `5d046289ff69f2c23e78a0130c1ed884a046c992` on `feat/installable-trait-profiles`. The reviewer worked separately from implementation and edited only this report. Working-tree identities below identify the reviewed files; the uncommitted changes are not attributed to the base commit.

**Disposition: PASS for the bounded static implementation review, with no unresolved blocking findings.** This review is not a model rating, genuine owner confirmation, coordinator acceptance, merge authorization or release approval. All new anchor behavior and authentic owner end-to-end use remain **NOT RUN**.

## Findings and repairs

The initial conflict structure could represent competing exact catalog anchors within one aspect, but not a manually identified cross-aspect or other semantic problem. This contradicted the promised manual blocking gate. The implementation added the separate `blocking_issues` preview collection. Its exact schema retains issue description and answer provenance, blocks unresolved use, requires a recorded resolution answer and explanation, binds every change into full-preview confirmation, and keeps issue prose out of instructions. The repair does not claim natural-language conflict detection or authenticate that a resolution assertion is true.

The coordinator separately identified that manual authoring lacked a public way to obtain the effective digest before confirmation. The reviewed `preview_receipt` API and `validate-preview` command now return exact draft hashes marked `structural_only` and `NOT_CONFIRMED`, emit no instruction payload, and return a null effective digest for inspected unresolved drafts. A digest receipt is never confirmation or activation.

The adapter skill initially described a “revoked” binding although no revocation-state API exists. The wording now says “removed”; a missing binding fails closed without implying a separate revocation mechanism.

## Contract assessment

The ten BFAS aspects each have low/middle/high catalog alternatives, with unspecified inactive. All 30 anchors are explicitly untested engineering hypotheses; source pins support vocabulary and traceability, not validation of agent traits. Separate scoped slots avoid inventing correlations or invalidating unusual combinations. All current anchor `constraints` arrays are empty. The bounded helper only rejects declared exact-context/action require/forbid pairs; manual issue entry and human review remain essential.

The compiler pins catalog bytes and source bytes, accepts only exact catalog rules, checks candidate approvals and full preview/presented-byte/effective digests, and renders only the invariant preamble and active catalog trigger/rule/boundary text. Audit answers, references, history, issues and confirmation text stay inert. Structural provenance cannot authenticate consent, reviewer identity, source-record existence or truthful declarations.

Local publication refuses replacement and backward revisions. Every binding names an exact profile revision and snapshot/effective digests; load revalidates the retained originals, manifest and dependencies. Parent and each child resolve independently, with no inheritance, averaging, latest-version lookup or permission transfer. Temporary task instructions have no accepted profile field; the host must maintain task separation. Static separation and unchanged-store tests do not establish a model's response to overrides.

The installer copies an allowlisted self-contained runtime into the explicit target's `.agents/skills/persona-profile` directory and refuses an existing destination or symlinked target components. The skill requires explicit invocation, absolute store and named agent binding; its adjacent launcher works from unrelated directories. The documented layout and explicit-only metadata match the official host documentation as checked by the coordinator. This reviewer checked the local layout and subprocess behavior, not live Codex discovery. Installation alone neither selects a profile nor changes account settings or a running context.

## Limits retained

Hashes detect drift relative to retained trusted files; they are not signatures or protection against rewriting trusted compiler code and the entire store. The store is not a hostile-filesystem sandbox or transactional database. Concurrent writers or interrupted publication can require manual repair. A new receipt does not authenticate a new human action, and the compiler cannot discover omitted conflicts or prove that the host applied preferences. Host discovery, actual child execution, model adherence, behavioral persistence, psychological validity, private owner confirmation/reconfirmation and release acceptance remain separate work.

No model call, account installation, network mutation, commit, frozen evidence edit or experiment was performed by this reviewer.

## Checks actually performed

| Check | Observed result |
| --- | --- |
| `python -m unittest profiles.test_profiles -v` | **14 tests passed** after final implementation changes. Covers full combinations, exact approvals and digests, immutable revisions, fresh-process reload, parent/two-child independence, child revision isolation, inert audit text, manual and same-aspect conflict gates, task/store separation, and draft receipt boundaries. |
| `python -m unittest discover -s adapters/codex -p 'test_*.py' -v` | **9 tests passed** after final implementation changes. Covers exact portable installation layout, no overwrite, symlink refusal, explicit destination, unrelated working directory, unbound failure, copied dependency tamper rejection, and independent parent/child loads in fresh processes. |
| Independent malformed-value sweep | Across **258 preview paths**, **1,543 mutations rejected**, two valid changes to empty unknown/history arrays accepted, and three identical values skipped. No unexpected exception. This is an inline synthetic probe, not an additional repository test count. |
| Independent manual-issue probes | **11** malformed provenance/status/resolution mutations rejected. Unresolved CLI inspection reported blocked; publication exited 2 with no stdout and no store created. |
| Independent audit and settings probes | Resealed synthetic imperative text in answers, references, unknowns, history, confirmation and review did not change rendered bytes. **40** single-aspect setting cases emitted exactly one rule for active settings and none for unspecified. These are deterministic software outputs, not model behavior. |
| Frozen paths | `git diff 5d046289ff69f2c23e78a0130c1ed884a046c992 -- core evaluation persona-design-v0.2 validation` had no changes. No claim of new behavioral evidence follows. |
| Installation claim review | Local file layout and launcher verified; official host references were checked separately by the coordinator. Live discovery, session activation and child model execution were **NOT RUN**. |

An initial reviewer command mistakenly passed `discover` as a module name; that invocation failed on its own nonexistent module. Corrected explicit suite invocations above passed. No product defect was inferred from that command error.

## Reviewed file identities

The following manifest excludes this report, verification summaries and generated Python caches. Records are `{path,sha256}` objects sorted by path, serialized with `json.dumps(rows, sort_keys=True, separators=(",", ":"))`, then UTF-8 encoded. Entry/discovery documentation was also read for scope consistency; its ongoing edits are outside this file-identity manifest.

Manifest SHA-256: `38e454fb57d1b3a962cfd99bd1fde439baf4a1d5166e331eae329c167ca05b3b`.

| File | SHA-256 |
| --- | --- |
| `adapters/codex/README.md` | `c460b7fa3939cd66b5b7ed5625091f7256785eed7152595186d4968b14f2f168` |
| `adapters/codex/install.py` | `f49c6a1489082faf8a0c3337d1d39e53559376f48e81a508d4e0312c1aa117db` |
| `adapters/codex/run.py` | `d517b30241c07ddb4d860bd9ff6eb94d8ae905256e03c9fe62633c7717aea8db` |
| `adapters/codex/skill/SKILL.md` | `43e971e74cf36e0709fcbea09bfd19efd412329c97ff2b8237a9c88c0dc0483e` |
| `adapters/codex/skill/agents/openai.yaml` | `5c540389e6f174d5dcf65f46a39d5e9e578b5522f54006ac91b37cf7496f9ba6` |
| `adapters/codex/test_install.py` | `e42cd0429100ff8ba49c46c755d84189d20f4605b94a2dca501f4dcd53d8bfea` |
| `profiles/CONTRACT.md` | `aadca08b81de162a6e5144d5d36cc606947abcfdb681d8445366bf1545a52938` |
| `profiles/COVERAGE.md` | `87bbd6ef5b9533a99288ae2e1e3c352677eae17ed4a3613944ad32ab45948a03` |
| `profiles/README.md` | `c67da32b16aa97e1385ab60d64cbe16b42cd66826a8e8158641dc8c9bd71b089` |
| `profiles/__init__.py` | `dd4d65cb529743572887e5fdadb3966a4e82188984109e77e3f5a5fba23e8d5b` |
| `profiles/__main__.py` | `f02ee84d775e0809210dbec5b1597774a88915a01bc3e2989848b2125f0ee7cd` |
| `profiles/catalog-v1.json` | `52d66e3265567b615cb7230390b5befa8de29e969c4913a6f97fc7230ed67cb5` |
| `profiles/compiler.py` | `e0544e0ec5838b640ccb23695e1f9608f69e6b764846c3f4efbecba3b08e8c7a` |
| `profiles/fixtures/build_fixtures.py` | `a52eff5e9d24b22c5788c38c1d6c029b05729d2d19970958c6d4af4a00ac5da0` |
| `profiles/fixtures/combination-a-preview.json` | `257604e4f89e91c08d180e2be10c427bcb3da0ed0727f5886607ed1e5f841471` |
| `profiles/fixtures/combination-a-spec.json` | `55c9b4f731edcd15b89bc7a33a1bf0f0ce0dec9616a415f565c34e5c24d6aac6` |
| `profiles/fixtures/combination-b-preview.json` | `f5cb0bf8430c025cde771d000ebde16b6e57f2e91511ab36f91010e94877a1d0` |
| `profiles/fixtures/combination-b-spec.json` | `a965963c9d1cb2e77ee3f8035044ce0edf24133cc75e61c10f257442e4685b91` |
| `profiles/test_profiles.py` | `9fac28a756136de00c9036ec4bdbda85c99ce553aeaad15c3a911b6276d9234b` |
