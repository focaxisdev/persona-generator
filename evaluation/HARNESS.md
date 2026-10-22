# Offline pilot harness

`pilot.py` uses Python's standard library and makes no model or network calls. It prepares bounded engineering trial inputs, seals genuine outputs supplied by the operator, and builds condition-blinded review packets. It does not create model responses or authenticate human approval. Investigator-authored previews do not satisfy the original behavior protocol's user-confirmation gate.

Finalize `pilot-2026-10-22/frozen/plan.md`, `scenarios.json`, and `rubric.json` before preparing. From the repository root:

```sh
python evaluation/pilot.py prepare --root evaluation/pilot-2026-10-22
python evaluation/pilot.py verify --root evaluation/pilot-2026-10-22
python -m unittest discover -s evaluation -p 'test_*.py' -v
```

Preparation freezes the complete input file set and immutable design portion of the manifest by SHA-256 before any outputs exist. It refuses a second preparation. The seeded session order is `manifest.json.sessions`; each session lists its sequential run IDs. The initial 63 sessions are shuffled separately from the 13 fresh reloads that follow them. Only the first turn receives the condition instruction; subsequent packets contain the changed task and shared word budget, without condition reminders. Matched original and reload packets must be byte-identical. Execute a session's turns in order, preserving its agent, and start each new session (including reloads) with a fresh agent. Read the exact stored `frozen/messages/<run_id>.txt` into the delegation tool's `message` parameter. Use the frozen tested-model parameters for new sessions. Do not substitute investigator-written answers, regenerate unsuccessful outputs in place, or edit original raw files. Failures and missing outputs remain missing observations; record their errors in the experiment ledger.

For each actual tool call, retain an external metadata JSON containing `agent_id`, UTC `started_at` and `ended_at`, `requested_tool`, complete `requested_parameters` (including exact message), `returned_metadata` (tool result and completion status), and `limitations` (errors, truncation, hidden settings, or other caveats). Never store private staffing policies or credentials. Tool-requested model identifiers are not proof of a provider's internal backend version.

```sh
python evaluation/pilot.py record --root evaluation/pilot-2026-10-22 --run r123456 --metadata /tmp/actual-call.json
python evaluation/pilot.py verify --root evaluation/pilot-2026-10-22 --complete
python evaluation/pilot.py blind --root evaluation/pilot-2026-10-22
```

`record` and `verify` share receipt validation: exact frozen delegation message, fresh model parameters, correct spawn/followup tool, timezone-aware UTC start/end with end no earlier than start, affirmative tool acknowledgment without conflicting failure metadata, exposed returned task identity, independent-session canonical agent IDs, and within-session followup continuity and target identity. Relative task names must resolve unambiguously among recorded canonical identities. Accepted acknowledgment fields are literal `acknowledged: true` or the operation-specific `status: "spawn accepted"` / `"followup accepted"`; these establish recorded tool acceptance, not model completion or backend verification. Raw-file presence is checked separately. Receipts are append-only through `record`, which seals the nonempty raw file hash. The output hash detects later edits; it does not authenticate authorship or the operator-supplied metadata. `verify` revalidates stored receipts and checks frozen design, input hashes, recorded raw hashes, unexpected raw files, and (once built) blind packet hashes. `--complete` also requires every planned output to have a receipt. Atomic recovery after an interrupted filesystem write is outside this minimal harness.

Give the judge only the frozen rubric, the standalone judge instructions, and `blind/*.json`, with a narrow assigned read scope. Keep `manifest.json`, `blind-crosswalk.json`, condition packets, messages, and source plans withheld until all blind ratings are frozen. Blind packets carry only an anonymous item ID and task/response conversation content; neither run filenames nor condition labels are passed through. Responses can reveal their instructions or style, so blinding is limited rather than guaranteed. Preserve that limitation in judging records. The crosswalk is an audit artifact and may be published after the rating lock.

Judges save JSON rating arrays to `ratings/batch01.json`, etc., using the exact frozen rubric schema. Every blind ID must appear exactly once across the active `ratings/*.json` files. Before locking, judges may repair their own records while retaining previous attempts outside that active glob. The verifier checks structure, category enums, coverage, and literal quotes against only the current (last) response. It does not assess rating semantics or correct ratings. Keep actual judge tool/model/call metadata separately, and keep private staffing policies out of the repository.

```sh
python evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22
python evaluation/verify_ratings.py lock --root evaluation/pilot-2026-10-22
python evaluation/verify_ratings.py verify --root evaluation/pilot-2026-10-22
python evaluation/summarize_pilot.py --root evaluation/pilot-2026-10-22
```

`lock` exclusively creates `ratings-lock.json` with a UTC timestamp and rubric, blind-packet, and rating hashes; it refuses overwrite. Subsequent verification rejects changed hashes or file sets. Do not unblind or join conditions before locking. `summarize_pilot.py` requires that lock, verifies unchanged ratings and the complete pilot, and checks crosswalk conversations against the recorded runs before joining. It creates `analysis/observations.json` and `analysis/report-tables.md`, refusing an existing analysis directory. These contain all 30 initial category pairs and actual shared baselines, 13 repeats, 13 multiround sequences, guardrail violations, leakage, diagnostic whitespace word counts, and B05/A05 versus B06/A06 cross-axis records. They preserve categories and flags for review without semantic adjudication, validity claims, release decisions, p-values, or population estimates. Summary file creation is not an atomic two-file transaction; preserve and inspect any partial analysis after interruption.

Tests use explicitly marked synthetic strings in temporary directories only. They verify design coverage (76 sessions, 102 output files, 13 multiround sessions and 13 fresh reloads), frozen-input mutation detection, receipt immutability, raw mutation detection, and blind-packet field boundaries. They provide structural evidence only.
