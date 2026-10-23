# Independent documentation and host-smoke evidence review — 2026-10-23

**Verdict: no blocking findings in the reviewed documentation or the reporting
of this failed attempt. Actual host loading remains unverified.** This is a
bounded evidence review, not an experimental rating or release acceptance.

The review used source baseline
`64767190d605bb1d49c4b7a5b03b5c2dfd6d3e3f`, the current documentation diff and
the retained private evidence for the [single host attempt](HOST_SMOKE_2026-10-23.md).
Reviewed documentation comprises the English and Chinese READMEs, project
purpose, profile README/contract/coverage, release acceptance, claims matrix,
Codex adapter README and host-smoke report.

## Independently checked evidence

- The frozen plan, prompt digest and one-attempt reservation agree. The exact
  command requested `gpt-6.1-sol`, `medium`, read-only sandbox, ephemeral JSON
  execution and a 180-second timeout. The bundled catalog lists that model
  and effort; it does not prove backend selection or request acceptance.
- The prompt invokes `$persona-profile` with the explicit synthetic agent and
  store binding and a bounded `LOAD_ACK` task. It supplies no manual skill
  path, command to read the skill, rendered payload or baseline text.
- The manual installed-loader baseline is 6,016 bytes, with SHA-256
  `00ee8e9f3c3922caceae601a524f9a42e0b25a086b2e6de86c45ba93089ecba0`.
  Its digest agrees with the explicit synthetic binding. This is local
  preflight evidence only.
- The recorded CLI process exited with status 1 during in-process app-server
  initialization, reporting a read-only filesystem error. Stdout is empty
  and the final-output file is absent. No skill read, loader execution,
  response or acknowledgment is observable. The error identifies no failing
  path; the accompanying PATH-alias warning does not establish causation.
- The retained launcher reserves one attempt and contains no retry or
  alternate-runtime path. The evidence records one process invocation and
  no timeout. Empty host output cannot establish the number of backend calls
  or hidden transport retries, and the public report makes neither claim.
- Complete installed-file and store manifests match before, after and at
  review time. The twelve substantive installed source files match their
  repository sources byte-for-byte. Public evidence-file digests match the
  retained files. Retained private files have mode `0600`; the enclosing
  private evidence directory has mode `0700` and lies outside this repository.

## Documentation and scope

The revised acceptance document correctly separates ten selectable profile
settings and thirty untested anchors from the legacy core's two operations.
Authentic owner confirmation, actual host loading and model behavior remain
distinct requirements. The historical acceptance section, including the
original 400-response gate, is byte-identical to the baseline and remains
unmet. No paused evaluation is resumed or replaced.

The READMEs, project purpose and profile documents explicitly distinguish
independent selection from statistical independence, zero correlation or a
validated joint distribution. The adapter status, claims matrix and release
checklist consistently report an initialization block without promoting
manual rendering to actual host success. No owner-consent, stable-identity,
child-loading or behavioral-validity result is claimed.

Static review found no whitespace errors, missing local links in the reviewed
documents, or private absolute paths, credentials, thread identifiers or raw
transcripts in the added public prose. The tracked diff contains documentation
changes only. This reviewer performed file, digest, command-record and link
checks; it did not launch a model or host, retry the attempt, alter runtime
configuration, or rerun behavioral evaluation. Broader implementation-test
results are a separate verification record.
