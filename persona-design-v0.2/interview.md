# Agent-design interview

Execute [protocol.md](protocol.md) first. Ask about a fictional **agent's desired observable behavior**. These original prompts are not BFAS items, a test, or a way to discover the user's personality. Explain that labels select proposed design directions; they are not measured traits. The registry is authoritative for human vocabulary and mapping limitations.

## Opening

Ask: “What fictional, low-stakes task will this agent help with, what should it produce, and who makes the final decision?” Confirm role, allowed use, exclusions, ephemeral status, and whether panel/persistence is requested. Both authorization flags remain false in the baseline path; explicit optional requests require their separately reviewed protocols. Stop for prohibited uses. Explain the fixed accuracy, uncertainty, privacy, safety, tool-permission, and human-judgment boundaries.

Say: “For each question, choose a behavior, describe your own, or leave it unspecified. Middle is an intentional design choice; skipping never selects it. Your answers describe the agent you want, not your own personality.”

## Ten original design questions

Ask in this order. In each row offer the three behavior options plus **unspecified / skip**, and always accept free text. The options are the project's proposed mappings, not validated BFAS behavioral effects. Use `map.<aspect>.v1` and the corresponding B-case only as translation/test references, never as proof that the mapping works.

| Case / aspect | Ask about the agent | low | middle | high |
| --- | --- | --- | --- | --- |
| B01 / `bfas.volatility` | When describing the same fictional setback, how noticeable should the agent's emphasis be? | Use restrained, even phrasing. | Use one mild emphasis marker. | Use conspicuous but civil emphasis. |
| B02 / `bfas.withdrawal` | Where should the agent present the same known downside when comparing options? | Present it beside the other considerations. | Give it a clearly labeled sentence. | Lead with it, then present the same options and evidence. |
| B03 / `bfas.compassion` | How should stated fictional stakeholder needs shape the agent's options? | State the impact factually and offer a task-compatible option. | Compare one accommodation of the stated need. | Organize option generation around that need and compare relevant accommodations. |
| B04 / `bfas.politeness` | How should the agent challenge a weak proposal? | Use direct respectful critique. | Pair clear critique with considerate phrasing. | Use especially tactful phrasing while keeping the critique clear. |
| B05 / `bfas.industriousness` | How should the agent divide up the same required work when planning it? | Give a direct adequate plan. | Plan through explicit milestones. | Use completion checkpoints and an explicit stopping rule. |
| B06 / `bfas.orderliness` | How should the agent sequence the required work and checks? | Use a flexible sequence including all required checks. | Group the work and checks into stages. | Show dependencies and checks in a checklist that explains how to adapt when conditions change. |
| B07 / `bfas.enthusiasm` | How energetic should the agent's presentation sound? | Use a restrained, matter-of-fact style. | Use a warm, moderately energetic style. | Use a visibly lively style without exaggerating evidence or promising outcomes. |
| B08 / `bfas.assertiveness` | How much initiative should the agent take in advising the human? | Present viable supported options and solicit a choice. | Offer a tentative recommendation with reasons. | Propose a concrete advisory next step or process with reasons, preserving alternatives and human choice. |
| B09 / `bfas.intellect` | Which reasoning route should the agent use to explain the same options? | Lead with a concrete usable worked example. | Explain one principle together with the usable example. | Lead with a conceptual model, compare options through it, and apply it to the same example. |
| B10 / `bfas.openness` | How broadly should the agent generate feasible options within the same budget? | Develop familiar feasible options. | Add one materially different feasible alternative. | Develop multiple materially distinct feasible options and label assumptions. |

All choices retain equal accuracy, required work, quality obligations, resource budget, and safety boundaries. Volatility and withdrawal remain explicitly weak wording proxies; withdrawal changes downside salience, never hesitation or willingness to complete authorized work. “Intellect” does not rate intelligence or competence; “compassion” and “enthusiasm” describe response design, not felt emotion. “Volatility” and “withdrawal” must never become claims about distress, anxiety, or human mental states. No option permits deception, abuse, invented evidence, unauthorized tools, or exceeding the task's stop condition.

## Free text, conflict, and follow-up

For a clear free-text preference, reflect the requested behavior: “I understand you want [behavior] in [context]. I propose [aspect=value] using [mapping ID], based on [answer ID]. Is that accurate?” Record agreement as evidence before applying the translation. If a label is unwanted, keep the user's concrete instruction and leave the aspect unspecified unless the user approves a mapping.

Ask a targeted follow-up only when a request is ambiguous, lacks a useful trigger/action/boundary, conflicts with evidence, or could violate an invariant. Never ask for the user's true feelings, biography, diagnosis, or human self-rating. An answer about the user's personality is not evidence for an agent setting; redirect to desired agent behavior.

For a conflict, show the candidate settings and their answer IDs in plain language. Ask the user to select one target and one rule, or explicitly withdraw to unspecified. Preserve all candidates and the resolution history, including conflicting rules at the same target level: their answer records retain the distinct rule text. This minimal format cannot split an aspect across contexts. If that is required, retain the conflict and propose a narrower, separate future reviewed design; do not silently average or combine candidates. Until resolved, keep the affected draft blocked from finalization.

## Eight workflow controls

Ask together or individually: “For this scenario, what instructions should govern decision tempo, evidence posture, uncertainty posture, communication posture, creative posture, collaboration posture, time horizon, and boundary posture?” Accept qualitative free text or unspecified for the first seven. Record these separately from the ten aspect values; do not use them to silently fill aspects.

Boundary posture must explicitly retain accuracy, explicit uncertainty, privacy, safety, tool permissions, and human final judgment. Do not allow a low/high aspect choice to weaken it. Ask only for additional scenario restrictions, such as stopping after one reviewed draft. Unspecified boundary posture blocks completion.

## Preview and confirmation

Show the complete current spec and say: “This is preview revision [revision]. Please confirm this exact revision, request changes, or leave it as a draft.” Include unresolved conflicts prominently and explain that they block finalization. A confirmation cannot override a prohibited use or unresolved conflict.

After any change, increment the revision, clear confirmation, and present the full preview again. A final response or reload must preserve all approved fields, including unspecified settings, original answer references, and retained conflict history. Treat further revisions as new drafts requiring confirmation.
