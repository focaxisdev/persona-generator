# Static check report — unreleased v0.2 candidate

Date: 2026-10-22. Environment: Python 3.12.14, standard library only. Base checkout: `4b533cfb73ba26eb26e319770baa6ca6e776968a`. This report accompanies the candidate changes in the same commit; the Draft PR identifies the exact resulting commit.

## Executed checks

From the repository root:

```sh
python3 -m unittest discover -s validation -p 'test_*.py' -v
python3 validation/validate_spec.py preview validation/fixtures/all-unspecified-preview.md
python3 validation/validate_spec.py preview validation/fixtures/mixed-preview.md
python3 validation/validate_spec.py spec validation/fixtures/mixed-spec.md --preview validation/fixtures/mixed-preview.md --reload validation/fixtures/mixed-spec.md
git diff --check
```

Results: **32 tests passed**; both preview checks passed; spec and unchanged-reload comparison passed; whitespace check passed. The reload command uses the same synthetic file as a positive identity check; a separate regression mutates a copied file and verifies rejection. None of these checks runs an agent in a fresh session.

The suite includes rejection of unknown or missing aspects, numerical targets, unrequested middle defaults, dangling traces, human-source substitution for mapping evidence, unresolved conflicts, erased candidates, duplicate candidates, missing/stale confirmation, altered approved payloads even with recomputed hashes, changed reload metadata, weakened boundary controls, and fabricated behavioral validation. Positive cases include explicit middle, all-unspecified, same-level rule conflicts with distinct evidence, resolved workflow conflicts, and Markdown-only confirmation with a null digest.

Observed canonical preview digests:

- All unspecified: `sha256:bc563446457fa2a7e8fc820e881f8d65ed9956edfb951e6afd35624abde5d70a`
- Mixed synthetic fixture: `sha256:32b3af6c4d42babebecd719e079bfb1474b10f9ad60ab4f195a17e6e6f468314`

Local Markdown link targets were checked for filesystem existence: no missing targets. This checks paths only, not external availability or fragment anchors. Reproduce with:

```sh
python3 - <<'PY'
from pathlib import Path
import re
root = Path('.')
missing = []
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for raw in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        target = raw.split('#', 1)[0].split(' "', 1)[0]
        if target and '://' not in target and not target.startswith('mailto:'):
            if not (path.parent / target).exists():
                missing.append((str(path), target))
print(missing)
raise SystemExit(bool(missing))
PY
```

The existing v0.1 protocol, templates, adapter, Persona Pack, examples, and license have no content changes. No runtime, dependency, CI workflow, hosted site, or release was added.

## Review corrections and evidence limits

Review was performed separately from implementation. Initial review found that same-level conflicting rules could not be preserved, fixtures lacked a required boundary-answer reference, and one fixture source URL differed from the canonical source ledger. These were corrected and regression-tested. Documentation was also aligned with the validator's limited context model and optional digest path. Source interpretation, proposed mapping, interview choices, and prospective behavioral cases were reviewed as separate evidence layers.

The fixtures are hand-authored fictional protocol records. Their answer and confirmation metadata are synthetic; they do not represent actual user approval or observed model behavior. Structural success cannot authenticate consent, prove semantic safety, or establish behavioral adherence. No behavioral pilot was executed. The baseline, multi-round, and fresh-session reload trials remain **NOT RUN**. Release acceptance remains **BLOCKED** pending genuine model evidence and coordinator review.
