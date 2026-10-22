# Source notes v0.2

These notes separate checked human-construct sources from original project behavior hypotheses. Checked on 2026-10-22. `verified` means the stated source content was inspected, not that a generated persona or mapping is validated. The registry contains short original paraphrases and original mapping instructions; no questionnaire item text, scoring keys, or full instrument is reproduced.

## Source records

### `src.deyoung2007`

DeYoung, C. G., Quilty, L. C., & Peterson, J. B. (2007). Between facets and domains: 10 aspects of the Big Five. *Journal of Personality and Social Psychology, 93*(5), 880–896. DOI: [10.1037/0022-3514.93.5.880](https://doi.org/10.1037/0022-3514.93.5.880). [Author-hosted PDF](https://www.jordanbpeterson.com/docs/230/2014/15DeYoung.pdf).

- Access: `verified`; the PDF rendered with 17 pages. Inspected the hierarchy statement on p. 880, aspect interpretations on pp. 883–885, Table 3, and the relevant discussion on p. 891.
- Supports: human aspect terminology and the short construct paraphrases in [construct-registry.md](construct-registry.md).
- Limit: human research does not establish agent traits or validate project mappings. No psychometric scoring, human inference, or biological claim is imported.
- Rights: the PDF displays American Psychological Association copyright. Availability online does not establish an open license. Citation and short original paraphrase do not relicense the article, its instruments, or adaptations.

### `src.ipip.bfas-table`

International Personality Item Pool, [Characteristics of the IPIP Scales to Measure Two Aspects of Each Big Five Domain](https://ipip.ori.org/BFASTable.htm).

- Access: `verified`; inspected the domain/aspect table and its DeYoung et al. citation.
- Supports: exact pairings: Neuroticism—Volatility/Withdrawal; Agreeableness—Compassion/Politeness; Conscientiousness—Industriousness/Orderliness; Extraversion—Enthusiasm/Assertiveness; Openness/Intellect—Intellect/Openness.
- Limit: reported human scale statistics are not evidence of agent reliability, validity, effect size, or useful qualitative anchors. None are used as project thresholds.

### `src.ipip.bfas-keys`

International Personality Item Pool, [The Items in the Big Five Aspects Scales](https://ipip.ori.org/BFASKeys.htm).

- Access: `verified`; inspected headings, provenance footnotes, and reference attribution. Items and keys are intentionally not copied into this package.
- Supports: a provenance caution. Footnotes **a** and **b** identify reversed wording of IPIP items; **c** identifies an item newly written for BFAS; **d** identifies reversed wording of a BFI item rather than an IPIP item. The notes state these items were not administered to the ESCS.
- Limit: this mixed provenance prevents assuming that every BFAS-related text, adaptation, or article has the same rights status solely because it appears beside IPIP material. No permission for third-party instruments is inferred here.

### `src.ipip.home`

International Personality Item Pool, [official home page](https://ipip.ori.org/).

- Access: `verified`; inspected the site's public-domain statement for IPIP items and scales.
- Supports: the IPIP site's stated permission to copy, edit, translate, and use its public-domain items and scales without a fee or permission request.
- Limit: this statement is not a universal license for all linked publications, other instruments, BFAS adaptations, or material with separate provenance. This project does not need to reproduce instrument items to define fictional behavior anchors.

### `src.pubmed17983306`

National Library of Medicine, [PubMed record 17983306](https://pubmed.ncbi.nlm.nih.gov/17983306/).

- Access: `verified`; the web rendering exposed bibliographic metadata and the Abstract section, both inspected on 2026-10-22.
- Supports: metadata cross-check for title, authors, year, journal, pages, DOI, and PMID; the abstract independently identifies aspects as intermediate between domains and facets. Detailed definitions rely on the author-hosted PDF above.
- Limit: no agent-mapping claim or full-text rights is established by this record.

### `src.project-mapping-v0.2`

Persona Generator, [Construct registry v0.2: original proposed behavior mappings](construct-registry.md#original-proposed-behavior-mappings).

- Provenance: original project design, not an external academic source. `mapping_status: unvalidated-hypothesis`; `validation_evidence: none` for all ten mappings.
- Supports: attribution of the proposed low/middle/high output instructions and their B01–B10 evaluation targets.
- Limit: documentation checks and proposed test cases do not establish actual behavior, effect size, robustness, cross-provider portability, or human psychometric validity. Any future evidence must identify the tested mapping version and actual observed outputs; it cannot be backfilled from citations.
- Rights: original project prompt/mapping instructions are covered by this repository's [Apache License 2.0](../LICENSE). Cited sources retain their own rights; citing or linking them does not relicense them.

## Use boundary

The ten BFAS aspects are the core human-construct vocabulary. The eight v0.1 workflow controls remain separate project controls, not additional BFAS traits and not academic equivalents. Preserve source provenance, translation uncertainty, and the lack of validation evidence in generated specifications. No source in this file supports real-person profiling, diagnosis, sensitive-attribute inference, high-stakes decisions, or claims that an agent has human emotions or a mind.
