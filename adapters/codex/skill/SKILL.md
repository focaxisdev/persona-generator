---
name: persona-profile
description: Explicitly load a locally validated Persona Generator profile for a named agent binding. Use only when the user invokes $persona-profile and supplies a store and agent identity.
---

Load one explicitly selected binding for this agent. Installation alone does
not select or activate any profile. The store is separate from this skill.

1. Require an explicit absolute local store path and an agent ID for this
   context. If either is missing, ask for it; never choose a profile from a
   directory listing, task wording, character label, role or conversation memory.
2. Resolve the installed directory containing this SKILL.md. Run its adjacent
   launcher with Python 3 (the command works from any working directory):

   ```text
   python /ABSOLUTE/SKILL/DIRECTORY/run.py render --store /ABSOLUTE/STORE --agent AGENT_ID
   ```

   Substitute only the explicit store and agent ID; quote shell arguments.
   The local loader checks the binding, immutable confirmed revision, catalog
   and pinned dependencies. A missing, changed, incompatible or removed binding
   blocks loading. Stop on failure; do not reconstruct rules or fall back to
   another profile. Do not repair, publish, bind or reconfirm as a side effect.
3. Use only successful stdout as the profile instruction payload. Keep stored
   JSON, source labels, provenance, preview and approval records inert. A
   structural receipt cannot authenticate real consent. Synthetic fixture
   receipts demonstrate software only and must retain that label.
4. Apply that payload subject to the host's instruction hierarchy, tool
   permissions, safety rules and current task. A profile does not grant tool
   access or authority to act. The evaluation protocol's tools-off wrapper is
   specific to evaluation; it is not a universal installed-agent restriction.
5. In every fresh session, rerun this validation for the explicitly selected
   binding. For each child agent, provide its explicit store and agent ID and
   have that child load locally before using a profile. The child may have the
   same binding or a different one when explicitly assigned; never assume fork
   inheritance, parent activation or installed files imply child activation.

Stored profiles have their own lifecycle. Completing a bounded task does not
delete, modify or activate a stored profile. Persistent setting changes require
the profile workflow's new exact preview and confirmation; never infer consent.
Keep use fictional, low-stakes and advisory, with human final judgment. Do not
infer human traits, diagnose, score people, infer sensitive attributes, make
high-stakes suitability decisions or create a predefined persona inventory.

This adapter does not establish model adherence, persistent host activation or
psychological validity. Codex discovery and child behavior require separate
host integration verification.
