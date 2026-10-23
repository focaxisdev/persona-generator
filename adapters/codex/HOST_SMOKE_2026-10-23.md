# Bounded synthetic Codex host smoke — 2026-10-23

**Outcome: BLOCKED at host initialization.** One Codex CLI process was started;
the in-process app-server client failed before any host skill loading could be
observed. This is not a successful host-loading check.

## Scope and preflight

- Source checkout HEAD: `64767190d605bb1d49c4b7a5b03b5c2dfd6d3e3f`.
- Existing CLI: Codex `0.163.0`; existing authentication and runtime unchanged.
- Bundled local model catalog explicitly listed `gpt-6.1-sol` and supported
  reasoning effort `medium`. Catalog support does not establish backend use.
- A fresh disposable Git repository received the unchanged adapter through
  `install.py`. Every installed source file was checked byte-for-byte against
  its corresponding source. A separate private synthetic store received the
  unchanged `combination-a` spec and preview fixtures.
- Explicit binding: agent `synthetic-host-smoke`, profile
  `synthetic-combination-a`, revision `r1`. Synthetic fixture confirmation
  records demonstrate format only; they are not owner consent.
- Installed-loader manual preflight emitted exactly 6,016 bytes. Its SHA-256
  matched the binding's effective digest. This preflight is separate from
  actual host execution.

## Frozen attempt

Before invocation, the private evidence captured the exact prompt, command
arguments, one-attempt reservation, plan, source hashes, installed-file hashes,
store hashes and manual baseline. The prompt explicitly invoked
`$persona-profile` and supplied only the selected agent ID and absolute
synthetic-store location, followed by the bounded loading task and `LOAD_ACK`
request. No manual skill path, rendered profile text or baseline was injected
into the prompt.

Requested command parameters were `codex exec -m gpt-6.1-sol -c
'model_reasoning_effort="medium"' -s read-only --ephemeral --json`, with the
fresh repository selected by `-C`, private final output selected by `-o`, and
prompt input supplied through stdin (`-`). The fixed timeout was 180 seconds.
No permissions, account settings, authentication, environment-variable homes,
model choice or runtime were changed.

- Start UTC: `2026-10-23T01:03:26.141237+00:00`.
- End UTC: `2026-10-23T01:03:26.206552+00:00`.
- Process exit: `1`; timeout: no.
- Failure: `failed to initialize in-process app-server client: Read-only file system (os error 30)`.
- The failing read-only path is **UNAVAILABLE**: stderr does not identify it.
  A read-only filesystem warning about PATH aliases also appeared; no causal
  attribution between that warning and initialization failure is established.
- JSONL stdout: empty; final output file: absent.
- Native process invocation attempts: one. Observed model turns, skill reads and
  loader calls: zero. Empty event output cannot establish a backend call count.
- No retry, resume, repair, permission expansion, alternate runtime
  or model substitution followed the filesystem denial. No internal transport
  retry was observable.

## Acceptance observations

| Check | Observation |
| --- | --- |
| CLI invocation | Process started, then exited during host initialization |
| Successful actual host launch | Not established |
| Initial host skill inventory/discovery | Unobservable |
| Host read of the installed skill | No event observed |
| Host execution of installed `run.py render` for the bound agent/store | No event observed |
| Exact host tool stdout equals manual baseline | Not testable; no host tool stdout |
| `LOAD_ACK` | Not produced |
| Installed files unchanged | Complete file-content before/after manifests match |
| Stored files unchanged | Complete file-content before/after manifests match |

Requested model and reasoning effort are known from the captured command.
Actual backend model, effective backend reasoning settings and request
acceptance are unknown because initialization failed before host events.
An acknowledgment alone would not have established successful loading.

## Sanitized synthetic digests

| Artifact | SHA-256 |
| --- | --- |
| Bound snapshot | `7aa973faf8e12acaf8eb09e02f2a5b39aeb4cf63793fa5cbca40447623c8af22` |
| Bound effective text / manual baseline | `00ee8e9f3c3922caceae601a524f9a42e0b25a086b2e6de86c45ba93089ecba0` |
| Bound canonical spec | `8fc7b40e78f268356d3db78b1a0913d2a51d736b40f884a02c51a9730de97fcf` |
| Catalog | `52d66e3265567b615cb7230390b5befa8de29e969c4913a6f97fc7230ed67cb5` |
| Frozen prompt | `b655c17bbe52b61cf485a90853c6bbfe338b8e4558fb34067f5112228c0feb2d` |
| Plan | `20324db38d9909044953601d461397f81addbeb85425724f4febb79905425c85` |
| Empty host JSONL stdout | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Host stderr | `8e3330eeb312ddb37b9da73c3ece4a8aa7e2ade4b7bb255573aa487bc89f0f58` |
| Installed complete-file hash manifest, before and after | `1c71b331d7b13422f6cfe59927e0fbc4b45d4bbb049cadf817ea7b37315e0f04` |
| Store complete-file hash manifest, before and after | `4c9e25e4f8be51b1d8d02d2efa31c6b9f26bd33bcaef8aaa82c6f98d0234ab54` |

Private evidence remains outside the public repository. This report contains
manually inspected synthetic facts and digests, with no absolute private paths,
thread identifiers, raw traces, transcripts or private policy. No product code,
fixtures, previous reports, core or evaluation records were changed for this
smoke. The smoke collector performed no commit or push.

This attempt supplies no owner E2E, behavioral validity, stable identity,
automatic activation, implicit discovery success, child-loading or inheritance
claim. Successful actual host loading remains unverified. The [independent review](HOST_SMOKE_REVIEW_2026-10-23.md) separately checks this report and the retained private evidence; review cannot turn initialization failure into host-loading success.
