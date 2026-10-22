# Independent core integration review

Reviewed 2026-10-22 against base `8e55a4046b5fdc8870a4a16ad2b5f46e984afa54` on `feat/confirmed-core-integration`. This review was performed separately from implementation; the reviewer changed only this report. The reviewed working-tree file identities are recorded below, rather than attributing uncommitted work to the base commit.

**Disposition: PASS for the bounded static candidate review, with no unresolved blocking findings.** This is not owner confirmation, behavioral validation, coordinator acceptance, merge authorization, or release approval. New operation behavior and authentic owner E2E remain **NOT RUN**.

## Findings and corrections

1. The initially emitted invariant preamble did not explicitly carry all scope/privacy/safety/human-review constraints claimed in the contract. This was reported and corrected in the pinned catalog. The reviewed output now carries fictional, low-stakes, ephemeral advisory scope, human review/final judgment, accuracy, calibrated uncertainty, privacy, safety, permissions and authorized scope. Current task requirements override preferences without changing the confirmed spec; non-trigger, override and nonadherence are distinguished as instructions, not claimed classifier results.
2. An intermediate 33-test run failed with 10 errors after the public renderer changed from accepting projections to requiring spec/presented-preview paths, and after the control gained its visible literal rule. The tests were synchronized with that contract. The final independent rerun executed 40 tests successfully. The public renderer validates source artifacts before rendering; arbitrary typed projections are not an alternative public approval route.

## Checks actually performed

| Check | Observed result |
| --- | --- |
| `python -m unittest core.test_compiler core.test_cli -v` | **40 tests passed** on the recorded files. Includes exact snapshot/byte binding, stale confirmation, nested types/keys, trusted dependencies, custom-rule rejection, conflicts, unspecified fields, version routing, inert text and fresh-process comparison. |
| Independent wrong-type and key mutations of the valid choice preview | **636 wrong-type mutations** and **109 missing/extra-key mutations** rejected; no unexpected exceptions. These were exploratory inline standard-library probes, not additional named repository unit tests. |
| Independent parser/router probes | Overflowing float, lone surrogate, oversized integer, nested duplicate key and prose outside the single JSON fence rejected; three mixed/missing core version cases rejected; four explicit current/historical routes checked. |
| Independent synthetic audit injection | Imperative sentinel text in answers, record references, unknowns, history, source IDs and rejected conflict candidates did not enter emitted instructions. Resealed synthetic audit changes changed snapshot identity while leaving rendered bytes identical. Confirmation/review metadata remained absent from instructions. |
| Independent conflict checks | Selected candidate anchor/trigger/rule/boundary/answer mismatches rejected. Withdrawal required unspecified and removed the operation while retaining inert audit candidates. |
| Complete supported setting grid | All **64** combinations of two four-valued operation settings and four response-detail settings compiled; public API render and a fresh CLI process produced identical text for every combination. These are software checks, not model responses. |
| Frozen historical identity | All **541** tracked files under `evaluation/`, `persona-design-v0.2/`, and `validation/` were byte-identical to the base commit. Independently checked all **61** v2 SHA-256 entries and **470** protected v1 Git blobs: no mismatches. |
| `python evaluation/diagnostic-v2/validate_design.py verify` | Structural design PASS; generated outputs **0**, human confirmation **not_obtained**, semantic validation **false**. No diagnostic execution occurred. |
| Documentation paths | **178** relative Markdown link paths in changed docs, core Markdown and `llms.txt` resolved. This checks local destinations, not every remote page or fragment. |

## Trust boundary and coverage assessment

The compiler anchors catalog bytes and dependency paths/hashes in its own code. A known operation ID, a spec-supplied digest, a modified local dependency, or a fresh self-hash cannot authorize custom executable text. Complete preview content and actual presented file bytes are separately bound. Active operations and the response-detail control require exact candidate approvals; unsupported aspects cannot become active. The emitted surface is the invariant preamble plus catalog-derived approved operations and control wording in deterministic order. Source, answer, history and rejected-candidate text is excluded, including after reload. Legacy and mapping-v2 routes remain non-executable in this core and mixed/unknown core schemas fail closed.

Only `op.planning_structure.v1` and `op.advisory_initiative.v1` are supported, both explicitly untested. The other eight aspects remain vocabulary without runtime operations. Coverage distinguishes human definitions, bounded analogues, omitted properties, triggers, counterexamples and confounds. The review independently retrieved the [BFAS author PDF](https://www.jordanbpeterson.com/docs/230/2014/15DeYoung.pdf) and exact [Serapio-García arXiv v4](https://arxiv.org/abs/2307.00184v4) and [Salecha arXiv v2](https://arxiv.org/abs/2405.06058v2) abstract/version pages. The [source ledger](SOURCES.md) correctly keeps preprints separate from final publications and discloses unavailable publisher full-text verification. This review does not add verification of inaccessible final methods or borrow empirical results as local evidence.

README, Chinese README, discovery, Quickstart and architecture now agree on one default single-agent path. Version identities are separate from package and historical mappings; multi-persona/panel/pack work remains optional. Historical mixed results and failures remain visible. The private owner protocol requires actual choice/free-text participation, exact confirmation, a real edit, reconfirmation and fresh reuse without publishing private records. The bounded prospective evidence plan uses the same renderer, unprompted opportunities, non-triggers/overrides, held-out cases, continuation/reload, limited composition and two condition-blind raters. It requires prospective freezing and does not change the historical 400-response gate or execute the old 50-response diagnostic.

## Remaining limits

Structural receipts cannot authenticate consent, reviewer identity or truthful provenance. The compiler cannot infer whether free text expresses the claimed intent, detect an omitted semantic conflict, authenticate historical revision order, or establish model compliance. The artifact protocol still requires actual human review and confirmation. Hashes anchor local bytes; they are not signatures or protection against modification of trusted compiler code. New behavioral/owner evidence and any later release decision remain separate work. No model collection, owner simulation, website publication, release/tag, PR #3 action, or historical evidence change was performed by this review.

## Reviewed file identities

The table excludes this report and generated Python caches. Its ordered records are `{path,sha256}` objects sorted by path, serialized with Python `json.dumps(rows, sort_keys=True, separators=(",", ":"))`, UTF-8 encoded. Manifest SHA-256: `662c58a5f43a11bcc09ea554ce88511176a8981876e95dd8a9af8759be0ffb26`.

| File | SHA-256 |
| --- | --- |
| `AI_DISCOVERY.md` | `7acd7f161c419c2d715a908259acd8f78e1724383dc17f9311107313b16fbdc5` |
| `README.md` | `003fcdb3bc1d6cad37a1511c6dde49666e9ceade884a8fb26174983696a7fa4a` |
| `README.zh-TW.md` | `ad336b3ec3ef5a4b1bf5657becd42ca59f9b1e775f65a81f97dcbecbe3979477` |
| `core/CONTRACT.md` | `e4dd84ef45e1db8c3160d40a859faa7d403e4cf269a95c289b97246798c385b4` |
| `core/COVERAGE.md` | `db5d152b34e2b39313a4a6df4606759f068fc58798f5bcdcd73901b9a3783237` |
| `core/EVIDENCE_PLAN.md` | `dcc407f3fc0c095b8e1063598d03219a5f108fd8c1d09ed0f1e8aae302a97791` |
| `core/OWNER_TEST_PROTOCOL.md` | `d3592e1e24db60c9b7825730e0df1642821e248d6133bbf3fa0b322306ada903` |
| `core/README.md` | `a5dc62edc6369fc1636628962cb53c02f07960991abb57d1f3314725a4f1990f` |
| `core/SOURCES.md` | `583f4671b7b67f2c77a5b1c8a3c34cd50107067c1611dd5d03dafa349a9166dc` |
| `core/VERIFICATION.md` | `89f8b4ffeb1b219d0b1ddb58d13791b465a4d2d87fefde4f482e00884e42bb9a` |
| `core/__init__.py` | `a27f6c37be4fa235db534a2151eea9195b4290acc105212bd0de19613ce49cd1` |
| `core/catalog-v1.json` | `8c616013d572fc6568fe76698f03c5cc41d8aeb130da84a4580090a48d873fc7` |
| `core/compiler.py` | `06c00e79add152b44d5f2c685c690920344413dc85d0dc7b1be4201e901f4eeb` |
| `core/fixtures/choice-preview.json` | `0f9c19a7ede560bbcc12174a8f4ca81bcb0bed347f2ecbb1b446f058fc4ef001` |
| `core/fixtures/choice-spec.json` | `6810e22aa99af13a2366ceb82481d34aea01fa9761b5f7e4c01192cc5d55d034` |
| `core/fixtures/short-answer-preview.json` | `ed81dfd8f7c883f9dfce04dd883938ccee3a8869c0e51c2d147702aa82b035e7` |
| `core/fixtures/short-answer-spec.json` | `9b028eb68e8f04da3fdfaa9e86b130c4aa286e181f55de4d26093a718850e5de` |
| `core/test_cli.py` | `659cc70ae0b773d5b0a3850ca169cbae7c1cd407f34ad220d2d530f9c2060105` |
| `core/test_compiler.py` | `df63a40c7208ec54c7514f2706a29901101de9e32665b538c8e28537c87d89c5` |
| `docs/ARCHITECTURE.md` | `3d3d5e890319996c3e6e9a81eed4b56e618c7c67e96991a6a12185c5266a8dd0` |
| `docs/CLAIMS_MATRIX.md` | `f639965ac035baae0b45988ace6e438ee9ed0ff682fc354594c8607fd06dca0d` |
| `docs/FAQ.md` | `972e9e0274a22417b043e0842d5c0804c0e96c374b8d334c6127e6c2c4a575b4` |
| `docs/MIGRATION.md` | `da4d9e53a71834999ce5290d11c73bcf616a96fd0c8d72c866cd0912dc6a8611` |
| `docs/QUICKSTART.md` | `1c9a6942285d4fe1afd3f7c734123e4d1f605043d5a3033f14c6f31bc9ff0357` |
| `docs/RELEASE_ACCEPTANCE.md` | `b51941e00ea464d2811c3f7b4a76e5837dd7348d36ee1d76a2785ec8e8018fad` |
| `docs/RELEASE_NOTES_DRAFT.md` | `3fdb776855c81cf8631ce1bc4d6c320a4203bc73b35553099744b66ae4bb1ecb` |
| `docs/USE_CASES.md` | `ca3899c120365e5204a3053903f61aede96f846da2b17acc81fa9a5fa882c5af` |
| `docs/WHY_PERSONA_GENERATOR.md` | `30a0add6b5249bcb0ea5231b7ab4c9f3a2adef51c52cef9348b81cf9fa2ae93d` |
| `llms.txt` | `550832f085cfbe6688bccf1643975d14d06a76f7b784dda84c2537e75dc0a3a0` |
