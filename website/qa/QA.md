# Browser QA — 2026-10-22

Final actual Chromium run: **55 checks passed, 0 failed**. The machine-readable evidence is [results.json](results.json), including browser version, execution timestamp, start/end SHA-256 hashes of index, styles, demo, and favicon, exact checks, network requests, and computed color samples. The implementation was frozen before this final run; its four asset hashes match at the start and end.

## Reproduce

From `website/`, start a local server:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

In another terminal, with Python Playwright installed and Chromium at `/usr/bin/chromium`:

```sh
python3 qa/browser_checks.py
```

The script uses an isolated browser context with reduced motion for stable screenshots, real clipboard permission, real downloads, intercepted storage-write attempts, and console/network event collection. It changes only QA outputs. Its base URL can be changed with `--url`. The server must already be running. The runner creates its screenshot directory when absent and exits 1 if any check fails, otherwise 0.

## Executed coverage

- Desktop 1440×1000; responsive widths 768, 760, 390, 375, and 320 at height 844. Initial states and opened full JSON previews have no horizontal page overflow. Visible controls stay inside each viewport. Mobile computed evidence body text is at least 14px and native input controls are at least 16px.
- All ten defaults remain unspecified with no generated aspect rules. One explicit anchor changes only its selected aspect.
- Preview is required; an unchecked acknowledgment blocks confirmation. Confirmation enables exports; unchecking it or editing an input revokes export permission and stale preview/confirmation.
- Copy and downloaded Markdown contain the exact JSON displayed by the preview. Clipboard rejection exposes the same complete readable fallback. Actual downloaded fixture is [downloaded-demo.md](downloaded-demo.md).
- Contradictory same-aspect choices retain both answers, clear the target to unspecified, and block confirmation. An explicit resolution restores a chosen target and retains resolution history. Manual conflict flags also block until explicitly resolved.
- Free text remains verbatim and unknown without inferring targets. Explicit keep-unknown permits review without mapping. A linked explicit choice preserves the original unknown answer and its provenance.
- HTML payload is visibly literal; no injected image or script execution occurs. Reset and reload clear page memory.
- No external requests, cookie/storage writes, console errors, uncaught page errors, or failed asset responses occurred during these interactions. Local loading requests are recorded in results.json.
- Nineteen links have nonempty valid in-page anchors or pinned GitHub paths that correspond to actual repository files. Remote destinations were not fetched.
- Every form control has a native or accessible label. Keyboard skip link focuses main; preview focus advances through all eleven closed detail summaries to the review checkbox, then confirm and copy. Focused skip link is visible.

## Visual evidence

- [Desktop hero viewport, 1440×1000](screenshots/desktop-hero-viewport.png)
- [Desktop full page](screenshots/desktop-full.png)
- [Mobile hero, 390×844](screenshots/mobile-hero.png)
- [Mobile full page](screenshots/mobile-full.png)
- [Mobile workbench](screenshots/mobile-workbench.png)
- [Mobile preview](screenshots/mobile-preview.png)
- [Retained conflict and blocked confirmation](screenshots/conflict-review.png)

Screenshots are actual browser captures of the final localized interface. Mobile hero, preview, and conflict crops were visually inspected. The root reviewer independently inspects final design.

## Contrast and practical limits

Computed opaque color pairs measured 12.90:1 for primary body text on paper, 6.11:1 for normal primary-control text on teal, 5.29:1 for muted text on paper, and 4.94:1 for demo status text. Full samples appear in results.json. These checks do not model disabled-control opacity, all hover states, or every rendered text node.

This is targeted automated QA, not accessibility certification. No screen-reader, Safari/Firefox, real mobile-device, production-hosting, or externally fetched-link test was executed. Mobile decorative microcopy remains smaller than body text. Live clipboard/download behavior can differ with browser permissions; readable fallback was tested.

## Resolved findings and reruns

The initial keyboard check found that the skip target did not receive focus. The implementation added `tabindex="-1"` to main; the final actual keyboard check passes. A later DOM-order improvement places complete preview content before its review controls; the full forward-Tab traversal passes.

An intermediate harness assertion expected raw HTML text inside JSON-only history, where quotes were escaped; it was a test assertion mismatch rather than script execution. The final localized history renders the raw answer literally, and both literal text and non-execution checks pass. An intermediate run also crossed a localization source update and timed out against the obsolete English button label; all selectors now use observed final Traditional Chinese controls.

Mobile evidence body text and controls were enlarged after review. Screenshots and responsive checks were rerun against the frozen stylesheet. Earlier exploratory English screenshots were removed from final deliverables. No remaining blockers were found within the tested scope.
