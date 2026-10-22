# Independent review — private marketing preview

Date: 2026-10-22. Reviewer: separate model agent, not the designer or demo implementer. Model review is not independent human approval, coordinator acceptance or release authorization.

**Outcome:** no unresolved high- or medium-severity issue was found within the local static-page scope. This is a candidate for an owner-only review preview. Hosted access control must still be verified separately by the coordinator; local screenshots and `noindex` cannot prove it.

## Material and actual checks

Read `AGENTS.md`, `AI_DISCOVERY.md`, claims matrix, pilot REPORT, website README, HTML/CSS, demo model/rendering code, state tests, browser-check implementation, QA.md and final results. The controlling baseline is `9aa9ff2534c4d1593f07386ad8b99250ea25e72c`.

Independently ran `node website/demo.test.cjs` successfully. Inspected exact registry rule checks, unknown preservation, contradiction history, explicit resolution, immutable preview export, invalidation and input bounds. Additional installed Python Playwright/Chromium checks against the loopback server confirmed five domains, ten aspects, `zh-Hant`, preview focus, final DOM order, 14px mobile evidence limitations and 16px mobile input text.

Visually inspected desktop hero, mobile hero/workbench and final mobile-preview screenshots, plus independent 390px domain/pilot captures. Controls are contained and the Traditional Chinese hierarchy is readable. Canonical English names, identifiers and source rules remain alongside Chinese descriptions; full JSON is expandable.

Final [browser evidence](results.json) records **55 passed, 0 failed**, executed at 2026-10-22T10:17:13.140228+00:00. Its application hashes match current files. Coverage includes skip focus, labels, forward keyboard traversal, clipboard/download and fallback, contradictions, raw HTML-like text, unknown-answer linking, reset/reload, no storage/cookie writes or external requests during interactions, and responsive overflow checks. See [QA.md](QA.md) for exact viewports and limits.

## Claims and behavior

- Human definitions, original proposed engineering mappings and bounded observations remain distinct. All five domains and ten aspects appear. B01/B02 are expressly experimental expression controls.
- Counts match the controlling evidence: 30 initial pairs; five candidate contrasts, three with limited target confidence; 102 outputs; all 28 budget violations. The page rejects success-rate interpretation, retains no-contrast mappings and B05/B06 overlap, and exposes shared baselines, missing controls, unknown settings and the incomplete release gate.
- Markdown portability is separated from behavioral stability. No claim of validated psychological traits, real emotion or cross-model reliability was found. The license FAQ separates original Apache-2.0 material from external papers/questionnaires and does not extend IPIP rights to all BFAS materials.
- Ten targets start unspecified; unknown never defaults to middle. Free text remains verbatim unknown with no NLP/model classification. Contradictions retain candidates and require explicit resolution; manual flags and history remain visible.
- Confirmation applies to a displayed revision; edits and unchecking review revoke export. Exports are explicitly demo-only, with behavioral evidence `not_run`, not a production review Pass. Text-node rendering, input bounds, CSP and observed network/storage checks support the stated local-only behavior. Clipboard/download copies surviving reset are documented.

## Resolved findings

1. **Medium, resolved:** the initial skip link did not focus main. `tabindex="-1"` and final keyboard evidence resolve it.
2. **Low, resolved:** confirmation controls preceded the preview. The final DOM order is trigger → preview → confirmation/export; forward Tab traversal passes.
3. **Low, resolved:** mobile evidence caveats were 10–11px. Final computed values are 14px for important evidence text and 16px for inputs.

A detected source-hash mismatch after an implementation change was reported to QA. The final frozen-source rerun supersedes intermediate results. No remaining local implementation blocker was found.

## Scope and limits

Baseline diff and untracked-file inspection showed additions only under `website/`; no core mappings, frozen prompts, rubric, ratings or pilot outputs changed. The reviewer edited only this report and did not publish, merge, release or change hosting access.

No screen-reader, real-device, cross-browser, complete WCAG, live external-link availability or authenticated hosting review was performed. Links were structurally checked against anchors and pinned repository paths. Hosted owner-only enforcement remains a separate coordinator check. This report contains no private policy, account identifier or Site URL. The full behavior protocol and product release remain incomplete as stated in the evidence.

Reviewed source hashes:

- `index.html`: `504fc2aaead2fde7d432e6d4ce0836385491e5dc8a7a4827611556d669baac08`
- `styles.css`: `948df23b6d3317c111aa06e9e1559e8176f99acdf8fc984769d27e5a13451860`
- `demo.js`: `0a66ab38a56bc53ae4e43cea8f7ccaae6caacf08c9aac33172443589f1a6a1f8`
- `favicon.svg`: `b45a525318b59c6489475f66301b86a5fcc90010c07166525b128f153fbc933c`
