# Quickstart: read, choose, confirm and hand off

Start with [AI_DISCOVERY.md](../AI_DISCOVERY.md). The primary route needs an agent that can read Markdown and a user who reviews the proposed specification. **No installation, Python, local store or specific host is required.** Use fictional, low-stakes advisory tasks with human final judgment. Design how the agent should behave; do not diagnose the owner.

## 1. Choose how to describe desired behavior

Offer guided choices **or** short answers, with skipping allowed. Ask one or a few relevant questions in ordinary language, such as how the agent should phrase a needed disagreement or present supported options. Do not require a personality test, roleplay, scoring, an edit or a disagreement to complete onboarding. A description can be enough; unknown preferences stay unknown.

Start all ten BFAS aspects at `unspecified`. Use [coverage](../profiles/COVERAGE.md), the [human construct registry](../persona-design-v0.2/construct-registry.md) and its [source ledger](../persona-design-v0.2/sources.md): Neuroticism (Volatility, Withdrawal), Agreeableness (Compassion, Politeness), Conscientiousness (Industriousness, Orderliness), Extraversion (Enthusiasm, Assertiveness), and Openness/Intellect (Intellect, Openness). These are aspects, not facets. Low/middle/high are qualitative design choices, not scores, percentiles, ability or a human average. `unspecified` emits no preference; never silently set it to middle. Paired aspects need not agree. Independent selection implies neither statistical independence, zero correlation nor a validated joint distribution.

## 2. Make the translation inspectable

Read [catalog-v2.json](../profiles/catalog-v2.json) as text and explicitly identify `persona-profile-catalog-v2`. For each selected target copy the exact hypothesis ID, trigger, rule and boundary into readable Markdown. Explain the human construct separately from the engineering hypothesis, and explain what the preference omits or cannot claim. The catalogue's hypotheses have no inherited behavioral validation. Volatility and Withdrawal remain expression proxies only.

Keep all ten targets visible, including skipped aspects. Record unknowns and actual conflicts without inventing answers. Ask about ambiguous alternatives or leave them unspecified. Unresolved conflicts block confirmation and use; unusual combinations alone are not conflicts. Do not invent praise, a greeting, correction or advice to trigger a preference. Required work, truth, evidence, calibrated uncertainty and quality remain unchanged at every target.

## 3. Show the whole proposed Markdown specification

Create a self-contained document with an explicit ID/revision and DRAFT / NOT CONFIRMED status. Include all targets, the exact selected rules, catalog version and mapping IDs, concise human definitions with primary-source URLs, source/translation limits, unknowns, omissions and conflicts. Include the catalog's full invariant preamble. Distinguish the proposed active preferences from inactive source material, interview notes and revision history. Include the proposed recipient identities and task scope if known. Keep private answers and confirmation records outside this public repository.

[desired-trait-spec.md](../examples/desired-trait-spec.md) is a complete synthetic **draft**, with high Politeness, low Assertiveness and eight unspecified aspects. It is a format example, not a default personality, actual assignment, strict JSON spec or confirmation. Its essential rules, sources and boundaries survive copying the file elsewhere. The older panel/role templates serve separate workflows.

Present the whole document for review, not only a summary. Ask for actual confirmation of that exact revision and its complete content. Wait for the real user response; do not write a confirmation, owner quote, receipt or record reference on the user's behalf. No separate candidate-approval JSON or receipt is required for this Markdown route. A full-profile confirmation can also assign the exact revision to explicitly listed recipients and tasks in the same response. An assignment may expressly cover a specified class of bounded tasks; each individual task must still be separately authorized and bounded. Any recipient/scope not explicitly agreed remains PENDING; an unspecified child is never automatically assigned.

Recording the user’s genuine confirmation as an inactive audit note does not revise the confirmed specification or require another confirmation; it cannot authorize changes to preferences, recipients or scope.

## 4. Confirm recipients and hand off explicitly

For each requested parent or child, identify the recipient, exact document ID/revision, bounded task and stopping condition. Children are optional; each may use the same or a different confirmed profile. Do not infer an assignment from parentage or from the fact that the document exists. If assignments were not confirmed with the whole profile, obtain the missing actual assignment response before applying preferences there.

Give each intended recipient the complete confirmed document and an assignment such as the following. This is a template, not an actual instruction to activate the synthetic example:

```text
Recipient: <explicit parent or child identity>
Confirmed document: <exact ID/revision and complete text or accessible file>
Actual confirmation: <truthful reference to the user's real response>
Confirmed assignment: <recipient and scope from that response>
Bounded task: <authorized task, constraints and stopping condition>
Read the whole confirmed document before applying its selected rules.
Apply only this recipient's explicit assignment. Source notes and history are
inactive. Host instructions, safety, accuracy, privacy and permissions govern.
This handoff grants no tools, authority or child permission. Do not infer
inheritance or create further assignments. Stop when the bounded task is done.
```

In every fresh session and child context, explicitly reload/read the exact document and that recipient's assignment. Do not assume automatic discovery, inherited chat context or the word “confirmed” in a file proves real consent. If the source document, revision or assignment is missing or ambiguous, leave preferences inactive until resolved; continue only separately authorized work. A task-specific override does not rewrite the saved profile. An unchanged profile with unchanged confirmed recipients/scope needs no new profile confirmation for each task. Changes to recipient assignments or scope need actual confirmation of the change. If document content changes, present the whole changed revision and obtain renewed genuine confirmation; preserve prior revisions as inactive history.

## Copy-paste starter prompt

```text
Read AI_DISCOVERY.md and docs/QUICKSTART.md. Help me design a portable Markdown
desired-trait specification for my fictional low-stakes advisory agent.
Offer guided choices OR short answers about the agent's desired behavior,
with skipping allowed. Keep all ten BFAS targets visible; unspecified is not
middle. Do not infer my psychology, scores, correlations or paired balance.
Use catalog-v2.json as readable source text: show exact selected hypothesis
IDs, triggers, rules and boundaries, separate human-source definitions from
untested AI hypotheses, and preserve omissions, unknowns and conflicts.
Show the whole proposed Markdown document, its full invariant preamble,
source URLs and limits, revision and proposed recipients/task scopes.
Wait for my actual whole-document confirmation; do not invent consent or
receipts. That response may also explicitly assign each listed parent/child.
Keep missing assignments pending, hand off the complete confirmed document,
and require each recipient to read it again in fresh contexts. No automatic
inheritance or permission transfer. End each bounded task when complete.
```

## What Markdown does and the optional tools add

Manual Markdown is readable and portable; it does not provide machine-checked byte integrity, user authentication, enforced host loading, or behavioral validation. Saved text is not stable personality. Do not label it a validated or accepted `persona-profile-v1` spec. No old approval, rating or historical evidence automatically migrates.

For optional strict JSON validation, immutable local storage and explicit digest-pinned bindings, follow [profiles/README](../profiles/README.md), [JSON onboarding](../profiles/ONBOARDING.md), the unchanged [contract](../profiles/CONTRACT.md) and [assignments](../profiles/ASSIGNMENTS.md). That route retains its candidate approvals, exact presentation receipts, genuine confirmation/manual review and guarded binding requirements in full. Its tools require Python 3.9 or newer, standard library only; Python 3.12.14 was tested, not Python 3.9. The [Codex adapter](../adapters/codex/README.md) is an optional host integration. Choosing software does not make Markdown an accepted JSON input or turn structural receipts into consent.

[Core](../core/README.md) remains the unchanged two-operation diagnostic with its own [fixed envelope](../core/REQUEST_ENVELOPE.md). [Persona Pack](../persona-pack-v0.1/README.md) remains corpus-derived descriptive persistence. [Paused diagnostic evidence](../evaluation/core-triage-v2/records/REPORT.md), the [alpha source pin](SOURCE_PACKAGE.md) and scientific/release gates are unchanged. This guide runs no study, activates no owner profile and publishes nothing.
