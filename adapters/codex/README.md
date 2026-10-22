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
    profiles/{__init__.py,__main__.py,compiler.py,catalog-v1.json}
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
