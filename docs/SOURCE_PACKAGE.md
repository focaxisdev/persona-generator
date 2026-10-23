# v0.2.0-alpha UNCONFIGURED experimental source candidate

This is a source distribution for inspection and optional local installation, not a configured persona or scientific certification. No profile/store/binding is activated or shipped as a default. Tracked synthetic fixtures and historical outputs remain inert examples and evidence. Personal owner E2E is unverified and non-gating for this unconfigured scope; actual profile use requires real confirmation and assignment.

## Requirements and scope

The profile runtime and adapter require **Python 3.9+**, standard library only. Actual execution is tested on **Python 3.12.14 only**. Dictionary merge `|` is a Python 3.9 addition ([official Python documentation](https://docs.python.org/3.9/whatsnew/3.9.html#dictionary-merge-update-operators)) and is used at runtime. Source inspection finds no later required runtime API; postponed type annotations do not imply Python 3.10 execution is necessary. Grammar/version-guard simulations do not establish successful execution on untested versions. Use a maintained interpreter; the implementation minimum is not a recommendation to install an obsolete interpreter.

Building the candidate additionally uses Git and a SHA-256 utility. There is no pip dependency, wheel, new model service, credential or background process. Historical evidence documents keep the interpreter requirements/status they originally recorded; current install instructions govern the current profile package.

## Approved alpha source

At the [2026-10-23 checkpoint](RELEASE_STATUS.md), the approved v0.2.0-alpha source is exactly commit [`290ede4760f03048ddb8fcc4d613509cc573cb80`](https://github.com/focaxisdev/persona-generator/commit/290ede4760f03048ddb8fcc4d613509cc573cb80), tree `79eb58c33a3373e462c1e4a126f88dee6cfa453c`. Publication was approved but failed; no v0.2 tag/release exists. Current main includes PR #7; the install-manifest fix in Draft PR #8 is absent from both main and this approved alpha. Neither is a replacement release source.

The procedure below documents reproducibility, not an instruction to regenerate approved assets, upload them or retry publication. Existing approved artifacts remain bound to their recorded commit and hashes. A different source requires a new review and decision. Never substitute `HEAD`, a moving branch, current main or PR #8 for this alpha.

## Generic exact-source reproduction, outside the repository

For a separately requested reproduction, use the reviewed full 40-character commit ID, never a moving branch name. For this alpha, `CANDIDATE_SHA` must be `290ede4760f03048ddb8fcc4d613509cc573cb80`. Resolve and record `git rev-parse CANDIDATE_SHA^{tree}`. Do not put the generated archive, manifest or private records into this Git tree: that would create self-hash recursion or change the reviewed source.

```sh
# For the approved v0.2 alpha, use only 290ede4760f03048ddb8fcc4d613509cc573cb80.
# Use a fresh empty output directory, outside the checkout.
mkdir /tmp/persona-v0.2.0-alpha-candidate
git -c tar.umask=0022 archive --format=tar --prefix=persona-generator-v0.2.0-alpha/ --output=/tmp/persona-v0.2.0-alpha-candidate/persona-generator-v0.2.0-alpha-unconfigured-source.tar 290ede4760f03048ddb8fcc4d613509cc573cb80
sha256sum /tmp/persona-v0.2.0-alpha-candidate/persona-generator-v0.2.0-alpha-unconfigured-source.tar
```

The tar contains the full reviewed tracked source tree, including preserved failure/paused evidence. No working-tree/untracked files are added. Verify every extracted regular file byte-for-byte against that commit's Git blobs, plus file inventory and mode; reject symlinks, submodules, path traversal, duplicate names, missing or extra files. Do not rely on an archive filename alone. Current `.gitattributes` has no export-ignore/substitution transformations. The explicit archive-only `tar.umask=0022` makes regular-file permission bits match Git modes (0644/0755); do not rely on Git’s default archive umask. Repeated archives at the same commit and explicit setting must produce identical bytes under the recorded Git version.

Create `manifest.json` as a sidecar, recording:

- `version: v0.2.0-alpha`, `distribution: experimental-source`, `configuration: UNCONFIGURED`;
- exact source commit and tree; Git/Python versions used for packaging and tests;
- archive name, bytes and SHA-256;
- all tracked source paths, Git modes, byte lengths and SHA-256 values;
- implementation minimum `3.9`, actual tested interpreter `3.12.14`, no execution evidence for other versions;
- protected-history comparison, website exclusion, source/rights documentation and check results.

Write indented UTF-8 JSON with sorted keys and a final newline, then SHA-256 the actual manifest bytes. The source file hash domain excludes the manifest, archive and test outputs: these are external evidence. Retain archive and manifest hashes, full commit/tree and test results with the corresponding review record; the approved alpha review is no longer an open Draft PR. An archive checksum verifies bytes, not signatures or publisher identity. No release asset upload is performed by these instructions.

## Clean installation and synthetic reload acceptance

Extract the exact verified archive into a disposable directory. With the actually tested interpreter:

1. Run the aggregate local suites in [packaging verification](PACKAGE_VERIFICATION.md).
2. Run `python adapters/codex/install.py --target-repo /absolute/disposable/repo`. Confirm only the allowlisted skill/runtime files were copied and **no profile, fixture, store or binding** was installed. No live host is launched.
3. Separately use the existing labeled synthetic fixtures in another disposable store to test publish/bind/render. Check two different full combinations, explicit parent/two-child pins, fresh-process exact digests, rejected missing/tampered binding and refusal to overwrite the installed skill. Do not use these receipts as real consent.
4. Retain the source/package hashes and results. This verifies unconfigured installation and local software loading, not owner E2E, automatic discovery or model behavior.

For real optional configuration later, read [onboarding](../profiles/ONBOARDING.md), [assignments](../profiles/ASSIGNMENTS.md) and [explicit Codex loading](../adapters/codex/README.md). No personal journey is invented to complete packaging.

## Source attribution and licensing

| Material | Treatment in the archive |
| --- | --- |
| Original project code, protocols, engineering rules and documentation | Retain [Apache-2.0](../LICENSE); do not remove existing attribution. |
| BFAS human-construct sources | Retain the [source ledger](../persona-design-v0.2/sources.md), [registry](../persona-design-v0.2/construct-registry.md) and [grounding/rights notes](PSYCHOLOGY_GROUNDING.md). Definitions are original paraphrases. No complete questionnaire or paper is included. |
| IPIP and separately sourced/adapted items | Existing notes distinguish IPIP's statement from individual item provenance; the project license does not relicense all related instruments. |
| Historical synthetic outputs and evidence | Retain authorized public records, limitations and failure reports byte-for-byte. These are not active profiles or scientific certification. |
| Private owner material and raw host traces | Outside the source tree; not included. |
| Website PR #3 | Excluded; existing original README SVG assets are separate and retained. |

[Current release status](RELEASE_STATUS.md) and [acceptance tracks](RELEASE_ACCEPTANCE.md) distinguish the exact artifact from later changes. [Changelog](../CHANGELOG.md), [draft notes](RELEASE_NOTES_DRAFT.md) and [merge route](MERGE_ROUTE.md) retain historical preparation context; the latter two are pre-merge snapshots. No new academic endorsement or expanded validation claim is licensed by packaging.
