# Persona Generator marketing preview

Traditional Chinese, buildless static page based on protocol/evidence commit `9aa9ff2534c4d1593f07386ad8b99250ea25e72c`. This website increment changes no core mapping, rubric, rating or pilot output. It is a review candidate, not a release announcement.

## Run locally

From the repository root:

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory website
```

Open `http://127.0.0.1:4173/` on that machine. A remote workspace's loopback address is not a user-facing preview URL. Stop the server when finished. The deployed review copy uses a separate owner-only Sites project; no public deployment or repository-main merge is part of this increment.

## Files and behavior

- `index.html`, `styles.css` and local SVG assets: presentation, sources, scope, evidence and FAQ.
- `demo.js`: browser-memory-only educational workflow; no live LLM, inferred personality, API, analytics, cookies or local storage.
- `demo.test.cjs`: state and rendering-boundary checks.
- `qa/`: reproducible browser checks, actual results, screenshots and independent review.

The demo records explicit choices or verbatim unknown text, retains contradictory choices, requires explicit resolution and review, and invalidates confirmation when content changes. It exports a **demo-only Markdown draft**, not a production Persona Spec or a manual-review Pass. The full protocol still requires its own confirmation and review. Download/copy actions occur only when requested; downloaded files and clipboard contents remain outside the page after reset.

All ten mappings are copied from the pinned registry; no questionnaire is administered. The page keeps human research definitions, project-authored mappings and bounded model observations distinct. The five candidate contrasts among 30 pairs are not a success rate; three have limited rating confidence. All 28 budget failures among 102 outputs remain visible. See the pinned claims matrix and pilot report linked on the page.

## Checks

```sh
node website/demo.test.cjs
python3 website/qa/browser_checks.py
```

Browser checks use an already available Python Playwright installation and Chromium, not a runtime dependency of the website. Read `qa/QA.md` for the actual environment, viewports, commands, outcomes and limits. Screenshots are observations of the local static page, not proof of hosted access control. The native Sites access response establishes the hosted audience.

## Hosting boundary

Only the presentation files are copied into the private Site's `dist/` directory. Its `.openai/hosting.json` and Site source repository are kept separate from this public project repository. No private credentials, account identifiers or Site URL belong in this repository. Private access must be enforced by Sites owner-only policy; `noindex` is only a crawler hint.

The current environment lacks the Sites source-helper scripts. The supported native source/version contract can be fulfilled with Git using the returned repository credential in process memory, a pushed source commit, and a tar archive containing `.openai/hosting.json` plus `dist/`. Credentials must enter via hidden stdin and must never be written to disk, command arguments, logs or commits. The owner-private save/deploy operation is used only after local QA and confirmed owner-only access. Do not opt into automatic publish-on-push before QA, and do not broaden access.

## License and use

Original repository code, copy and SVG/CSS assets follow the root Apache-2.0 license. Cited papers and questionnaire materials retain their own rights; this page reproduces no questionnaire. The project's fictional, low-stakes advisory scope excludes profiling, diagnosis, psychometric scoring, sensitive inference and high-stakes or autonomous final decisions. These scope rules are distinct from claims about third-party intellectual-property licenses.
