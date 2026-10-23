# Codex local skill adapter

This adapter copies a self-contained local loader into an explicitly requested
repository. It provides an explicit `$persona-profile` skill, not automatic
profile activation. The host-neutral [profiles package](../../profiles/README.md)
owns storage, immutable revisions, confirmation and agent bindings. Installation
copies no profiles, private records or example personas.

From the Persona Generator checkout, with Python 3 and the standard library:

```bash
python adapters/codex/install.py --target-repo /absolute/path/to/disposable-repo
```

The target must already be a directory. The installer refuses an existing
`.agents/skills/persona-profile` path and symlinked installation paths. It makes
no network requests, starts no model session, changes no account settings, and
does not install into a user's home, global agent configuration or running
agent by default. There is no implicit destination or overwrite switch.

The resulting layout is:

```text
target-repo/.agents/skills/persona-profile/
  SKILL.md
  agents/openai.yaml
  run.py
  runtime/
    LICENSE
    profiles/{__init__.py,__main__.py,compiler.py,catalog-v1.json,catalog-v2.json}
    core/{__init__.py,compiler.py}
    persona-design-v0.2/{construct-registry.md,sources.md}
```

`core.compiler` supplies strict JSON/hash helpers; the installed profiles package
uses its own versioned catalog. Both catalog and pinned source bytes travel
with the loader. No dependency download is needed. To update, review the new
version and install into a new target; this installer never merges or silently
upgrades an existing skill.

Create and confirm profiles and explicitly bind agent IDs using the profiles
workflow. Keep the store outside the installed skill. Then invoke in Codex:

```text
$persona-profile Load my explicitly bound agent ID EXAMPLE_AGENT from the local
store /absolute/path/to/store for this fictional, low-stakes advisory task: ...
```

For local validation without a host or model:

```bash
python /absolute/path/to/disposable-repo/.agents/skills/persona-profile/run.py render --store /absolute/path/to/store --agent EXAMPLE_AGENT
```

The command revalidates the binding and exact confirmed revision and emits only
trusted instructions on success. A fresh session must explicitly load again.
A parent and child can use the same or different explicit bindings, but each
context must load and validate its own binding. Stored profile lifecycle is
independent of a bounded task's completion. Host permissions remain host-owned.

## Repository-guided explicit loading

Automatic discovery is optional. A host with ordinary local file-reading and
command-execution tools can follow this explicit integration path without
starting another Codex CLI or changing account settings:

1. Supply the installed `SKILL.md` path, the absolute store path, the current
   agent's explicit ID, and one bounded fictional task. Explicitly request
   `$persona-profile` through these repository instructions.
2. Have the actual host read that installed `SKILL.md` and follow its adjacent
   `run.py render` command for the supplied binding. Stop on validation failure.
3. Have the host consume the successful loader stdout as preferences subject to
   its existing instruction hierarchy, then answer the separately supplied task.
   Do not paste a hand-rendered equivalent into the request or claim discovery.
4. If supported delegation is used, explicitly supply each child its own skill
   path, store and binding ID. The child must read the installed instructions and
   invoke its loader independently; inherited parent text does not count.

Record actual file-read and loader events, exact output digests, host/model
parameters exposed by the tools, failures, and task responses. Distinguish this
**repository-guided explicit loading** from native skill discovery, installation
tests, owner consent and behavioral evaluation. A bounded demonstration does
not measure personality efficacy, stable behavior or psychological validity.
The [explicit-loading record](EXPLICIT_LOADING_2026-10-23.md) reports this path
separately from the unchanged failed nested-CLI attempt.

## Evidence boundary and official host references

The [official Codex skills documentation](https://developers.openai.com/codex/skills)
describes repository `.agents/skills` discovery from the current directory to
the repository root, `SKILL.md` name/description metadata, and optional
`agents/openai.yaml` with `policy.allow_implicit_invocation: false` for explicit
invocation. A new skill may require restarting Codex before it appears. This
adapter includes that explicit-only metadata.

The [official AGENTS.md documentation](https://developers.openai.com/codex/guides/agents-md)
describes instructions assembled once per run from root downward. Accordingly,
this adapter does not rewrite AGENTS.md or claim that installing files changes
a running context. These official documentation URLs currently redirect to
ChatGPT developer documentation.

Local tests cover copied layout, byte identity, refusal to overwrite, and
portable validation in separate processes. They do **not** verify Codex skill
discovery, live model adherence, automatic fresh-session activation, child
inheritance or psychological validity. No live Codex session or paid service is
part of the adapter test. Structural synthetic fixtures are not genuine owner
consent or behavioral evidence.

Run the adapter tests from the repository root:

```bash
python -m unittest discover -s adapters/codex -p 'test_*.py' -v
```

## Actual-host smoke status

A [single synthetic nested-CLI attempt on 2026-10-23](HOST_SMOKE_2026-10-23.md) was blocked during Codex app-server initialization by a read-only filesystem error. The process did not expose a skill-read or loader-execution event. Its record remains unchanged and no retry or permission change followed. Native discovery remains unverified. The separately authorized repository-guided path above does not repair or reclassify that failed attempt. Raw traces remain private.
