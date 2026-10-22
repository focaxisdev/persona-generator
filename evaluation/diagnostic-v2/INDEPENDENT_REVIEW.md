# Independent review of the core-v2 design

Date: 2026-10-22. Disposition: **No remaining blocking discrepancy found in the reviewed design-only package.** This is an independent model review of documents, code and structural checks, not human approval, behavioral validation, experiment authorization or release acceptance. No v2 model generation or judging was performed. The reviewer did not implement the mapping or harness; review findings were returned to the implementers before the one-time freeze.

## Reviewed identity and actual checks

Baseline: `9aa9ff2534c4d1593f07386ad8b99250ea25e72c`. The reviewed [freeze manifest](frozen-hashes.json) has SHA-256:

```text
e3c7bd044cf7927a26fea97aaf6aa25106ba49b64c2bd519496b892ee5c46d8a
```

All 61 listed input hashes were independently recomputed and matched. The prepared manifest has exactly 25 case/condition cells with two repeats each, 50 unique planned context slots, 50 exact packets and zero actual receipts. The validator confirms zero generated outputs, no owner confirmation and 470 unchanged protected v1 files. Planned slots do not prove actual fresh sessions. This review is intentionally outside the prospective input manifest.

The following commands were actually run by this reviewer and passed:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s evaluation/diagnostic-v2 -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python evaluation/diagnostic-v2/validate_design.py verify
PYTHONDONTWRITEBYTECODE=1 python evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete
PYTHONDONTWRITEBYTECODE=1 python evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22
```

All **21 diagnostic tests passed**. The existing 102-response pilot and locked ratings also passed their integrity checks. An independent Git diff check found no changes to the original registry, validation directory or pilot evidence against the baseline. A file-existence check of 166 local Markdown link targets across 11 reviewed documentation files found none missing; this did not validate heading anchors, external links or rendered presentation. Tests use temporary synthetic structural fixtures and are not model observations.

## Mapping, task and rubric assessment

The five `.v2` mappings are separate prospective hypotheses. Human definitions, v1 instructions, raw responses, rubric, locked judgments and failure classifications remain historical evidence. The B01 r100034/r100077 threshold inconsistency is acknowledged without rerating. B01/B02 remain experimental expression controls outside this diagnostic.

- **B03:** The focused task permits comparing accommodations without requiring every response to compare or prescribing a particular example. Low can compare spontaneously; kind wording alone cannot satisfy the strategy features.
- **B05:** Usable planning, at least one intermediate completed outcome and checkpoint-recognition criteria are distinct predicates. A useful low answer may contain milestones. The final stopping scope is common to every condition.
- **B06:** Flexible ordering may coexist with stages, dependency explanations and adaptation. High does not silently require middle's stages. The task itself supplies precedence and possible table unavailability, so baseline saturation remains a material, explicitly retained risk.
- **B08:** The final recommendation feature matches the generic recommendation clause. Low is not forbidden to recommend, and high does not acquire execution or decision authority. Recommendation and process features may overlap.
- **B10:** Exact one/two/three developed approaches are a new, narrower instruction design, not a retrospective reinterpretation of familiar v1 options. Familiarity is unscored. Whole-answer total and usable/feasible counts must both match; undeveloped or infeasible extra candidates cannot disappear from the count. Ambiguous grouping remains unclear. This tests literal breadth instructions, not human Openness or creativity.

Earlier draft issues concerning B08 recommendation scope, B05/B06 literal specificity, judge-path resolution, freeze coverage and repeated condition ordering were resolved before preparation. The final order uses the prospectively specified SHA-256 sorting procedure. The freeze includes the mapping workflow and acceptance proposal as well as tasks, cards, code, plan, order and packets.

## Prospective assessment controls

The frozen PLAN separates assigned-rule adherence, directed target-feature contrasts, task adequacy, safety/boundaries, language and the complete-answer budget. Its declared contrast sets match the cards. A difference on an unrelated axis cannot substitute for the intended contrast; partial observations, nonelicitation, uncertainty and judge disputes remain visible. No forbidden-feature predicate is invented to force low/high separation.

Two separate blind judges are planned to assess all 50 slots independently, with missing-observation envelopes where evidence is unavailable. Both complete ledgers must lock before either judge receives labels, pairings or expectations. The fixed judge template covers all 19 feature predicates, task requirements, common checks, exact quotes, confidence, leakage and count ambiguity. These are prospective procedures, not executed judging or enforced filesystem isolation.

The 250-word ceiling uses the complete decoded answer and Python `len(text.split())`, without section exemptions. An overrun remains a budget violation; it does not automatically become a personality or safety failure. Each planned slot has one attempt maximum. Missing outputs, errors, refusals, truncation and contamination remain in the finite ledger; no regeneration-until-pass or silent substitution is permitted. Unknown backend settings remain unknown, and synthetic condition packets are not owner-confirmed specs.

## Documentation scope and remaining gates

The README, Quickstart, source/claim links and draft release notes clearly describe GitHub documentation as the marketing scope. The updated acceptance document removes the standalone website requirement and excludes PR #3. No website action was performed by this review. Historical website statements inside preserved v1 reports remain historical rather than operative requirements.

The 50-response design does not replace the original 400-response protocol. The limited alpha proposal remains pending a prospective coordinator decision. V2 collection, genuine owner interview/preview confirmation, an actual requested amendment and reconfirmation, fresh reuse, and the later continuity protocol are **NOT RUN**. The separate v2 workflow extension validator and compatibility acceptance are not implemented or established by these tests. Exact-candidate coordinator review, release packaging and any later merge/tag/release authorization remain outstanding.

Even successful future execution could support only bounded observations of the literal instructions on these tasks and requested settings. Task differences confound between-aspect comparisons; nested features can remain indistinguishable; two replicates do not establish reliability; model judges are not independent human raters. Local hashes establish consistency with this recorded freeze, not provider identity, authorship or authentic owner consent. Release remains **BLOCKED**.
