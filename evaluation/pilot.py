#!/usr/bin/env python3
"""Offline preparation and integrity checks for the bounded engineering pilot."""
import argparse
import hashlib
import json
import random
from pathlib import Path

BASELINE = """Help with this fictional, low-stakes rehearsal. Give advisory suggestions only. Preserve uncertainty, dissent, and human final judgment. Accuracy, explicit uncertainty, privacy, safety, existing tool permissions, and human final judgment are invariant. Do not profile real people, diagnose, score personality, infer sensitive attributes, manipulate, or make high-stakes or autonomous final decisions. Do not use a persona or infer personality traits. Do not persist artifacts or run a panel. Stop after the requested bounded answer."""
LIMITS = {"model_version": "unknown", "temperature": "unknown", "top_p": "unknown", "context_budget": "unknown", "provider_seed": "unknown", "limitations": "Requested model and effort are tool parameters; backend version, sampling settings and context budget are not exposed. Session history includes platform instructions."}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def read_json(path):
    return json.loads(path.read_text())


def anchors(registry):
    rows = []
    for line in registry.read_text().splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) == 6 and cells[0].startswith("`map."):
            mapping = cells[0].split("`")[1]
            rows.append((mapping, cells[2], cells[4]))
    if len(rows) != 10:
        raise ValueError("Expected exactly ten registry mapping rows")
    return rows


def message(packet, raw):
    return (f"Read only the assigned standalone instruction packet at {packet}. "
            "Do not inspect other files, repository documents, outputs, manifests, or evaluation rubrics. "
            "Answer its current task as the assistant. Use no external tools or sources for the task. "
            f"Save your complete actual task response verbatim as UTF-8 Markdown to {raw}, "
            "using a local file-write tool solely for this authorized evaluation recordkeeping. "
            "Do not overwrite an existing output. Do not add commentary, analysis, wrappers, or metadata "
            "to the saved response. Return that same complete response in your final answer. "
            "The sole permitted file operations are reading the assigned packet and creating the assigned raw output.\n")


def prepare(root, registry, seed):
    manifest_path = root / "manifest.json"
    if manifest_path.exists() or (root / "frozen-hashes.json").exists():
        raise ValueError("Already prepared; never regenerate a frozen trial")
    scenarios_doc = read_json(root / "frozen/scenarios.json")
    scenarios = scenarios_doc["scenarios"]
    if [s["id"] for s in scenarios] != ["S1", "S2", "S3"]:
        raise ValueError("Exactly S1, S2, S3 required")
    registry_rows = anchors(registry)
    frozen = root / "frozen"
    for folder in ["conditions", "packets", "messages"]:
        (frozen / folder).mkdir(parents=True, exist_ok=True)
    (root / "raw").mkdir(exist_ok=True)
    conditions = {"baseline": BASELINE}
    for mapping, low, high in registry_rows:
        for target, rule in [("low", low), ("high", high)]:
            name = mapping.removeprefix("map.").removesuffix(".v1") + "_" + target
            conditions[name] = (BASELINE.replace("Do not use a persona or infer personality traits. ", "") +
                "\n\nInvestigator-authored engineering condition preview; not a user-confirmed final spec. "
                "Apply only this proposed observable behavior rule; all other nine aspects are unspecified "
                "and unconstrained. This qualitative target is not a measurement or a claim of human feelings. "
                "Task evidence may change advice but does not authorize changing the stated behavior rule.\n\n" + rule)
    condition_files = {}
    for condition, text in conditions.items():
        path = frozen / "conditions" / (condition + ".md")
        path.write_text(text + "\n")
        condition_files[condition] = str(path.relative_to(root))
    sessions = []
    for condition in conditions:
        for scenario in scenarios:
            extended = condition == "baseline" or (scenario["id"] == "S1" and condition.endswith("_high"))
            sessions.append({"condition": condition, "scenario": scenario["id"], "reload": False,
                             "rounds": 3 if extended else 1})
    # Three common baselines plus ten high S1 repeats = thirteen fresh reloads.
    reloads = []
    for condition in ["baseline"] + [c for c in conditions if c.endswith("_high")]:
        for scenario in scenarios if condition == "baseline" else scenarios[:1]:
            reloads.append({"condition": condition, "scenario": scenario["id"], "reload": True, "rounds": 1})
    rng = random.Random(seed)
    rng.shuffle(sessions)
    rng.shuffle(reloads)
    sessions.extend(reloads)
    identifiers = list(range(100001, 100001 + 102))
    rng.shuffle(identifiers)
    session_ids = list(range(200001, 200001 + len(sessions)))
    rng.shuffle(session_ids)
    outputs = []
    for index, session in enumerate(sessions):
        session["session_id"] = f"s{session_ids[index]}"
        session["order"] = index + 1
        session["runs"] = []
        session["execution"] = None
        scenario = next(s for s in scenarios if s["id"] == session["scenario"])
        for turn in range(1, session["rounds"] + 1):
            run_id = f"r{identifiers.pop()}"
            task = scenario["round1"] if turn == 1 else scenario["round2"] if turn == 2 else scenarios_doc["round3"]
            packet = frozen / "packets" / (run_id + ".md")
            instruction = conditions[session["condition"]] + "\n\n" if turn == 1 else ""
            packet.write_text(instruction + f"Keep this response within {scenarios_doc['output_budget_words']} words.\n\nCurrent task:\n" + task + "\n")
            raw = root / "raw" / (run_id + ".md")
            msg = frozen / "messages" / (run_id + ".txt")
            msg.write_text(message(packet.resolve(), raw.resolve()))
            session["runs"].append(run_id)
            outputs.append({"run_id": run_id, "session_id": session["session_id"], "turn": turn,
                            "packet": str(packet.relative_to(root)), "message": str(msg.relative_to(root)),
                            "raw": str(raw.relative_to(root)), "task": task, "receipt": None})
    manifest = {"schema_version": "engineering-pilot-v1", "seed": seed,
                "source_registry_sha256": digest(registry), "base_commit": "a11373472832a3ec46a27a870ed484b36eab6cb2",
                "date": "2026-10-22", "human_confirmation": "not obtained; original protocol acceptance gate incomplete",
                "tested_requested": {"model": "gpt-6.1-sol", "reasoning_effort": "medium", "fork_turns": "none"},
                "judge_requested": {"model": "gpt-6-astra", "reasoning_effort": "high", "fork_turns": "none"},
                "unexposed_settings": LIMITS, "condition_files": condition_files, "sessions": sessions, "outputs": outputs}
    if len(sessions) != 76 or len(outputs) != 102:
        raise ValueError("Unexpected design coverage")
    write_json(manifest_path, manifest)
    hashes = {str(p.relative_to(root)): digest(p) for p in sorted(frozen.rglob("*")) if p.is_file()}
    write_json(root / "frozen-hashes.json", {"files": hashes, "design_sha256": design_digest(manifest)})


def design_digest(manifest):
    copy = json.loads(json.dumps(manifest))
    for session in copy["sessions"]:
        session["execution"] = None
    for output in copy["outputs"]:
        output["receipt"] = None
    return hashlib.sha256(json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify(root, complete=False):
    manifest = read_json(root / "manifest.json")
    frozen = read_json(root / "frozen-hashes.json")
    if design_digest(manifest) != frozen["design_sha256"]:
        raise ValueError("Frozen manifest design changed")
    initial = {}
    reload_seen = False
    for session in manifest["sessions"]:
        first = next(o for o in manifest["outputs"] if o["run_id"] == session["runs"][0])
        key = (session["condition"], session["scenario"])
        if session["reload"]:
            reload_seen = True
            if key not in initial or digest(root / first["packet"]) != initial[key]:
                raise ValueError("Reload packet differs from original or precedes it")
        else:
            if reload_seen:
                raise ValueError("Initial session occurs after reload phase")
            initial[key] = digest(root / first["packet"])
    current = {str(p.relative_to(root)): digest(p) for p in (root / "frozen").rglob("*") if p.is_file()}
    if current != frozen["files"]:
        raise ValueError("Frozen input file/hash set changed")
    expected = set()
    for output in manifest["outputs"]:
        path = root / output["raw"]
        if path in expected:
            raise ValueError("Overlapping raw paths")
        expected.add(path)
        receipt = output["receipt"]
        if receipt and (not path.is_file() or digest(path) != receipt["sha256"]):
            raise ValueError("Raw output missing or changed: " + output["run_id"])
        if complete and (not receipt or not path.is_file()):
            raise ValueError("Missing output receipt: " + output["run_id"])
    if set((root / "raw").glob("*.md")) - expected:
        raise ValueError("Unexpected raw outputs")
    blind_hashes = root / "blind-hashes.json"
    if blind_hashes.exists():
        actual = {p.name: digest(p) for p in (root / "blind").glob("*.json")}
        if actual != read_json(blind_hashes):
            raise ValueError("Blind packet missing or changed")
    return manifest


def record(root, run_id, metadata):
    manifest = verify(root)
    output = next(o for o in manifest["outputs"] if o["run_id"] == run_id)
    if output["receipt"] is not None:
        raise ValueError("Output already sealed; original records are immutable")
    for key in ["agent_id", "started_at", "ended_at", "requested_tool", "requested_parameters", "returned_metadata", "limitations"]:
        if key not in metadata:
            raise ValueError("Missing metadata field: " + key)
    params = metadata["requested_parameters"]
    if params.get("message") != (root / output["message"]).read_text():
        raise ValueError("Delegation message differs from frozen message")
    session = next(s for s in manifest["sessions"] if s["session_id"] == output["session_id"])
    if output["turn"] == 1:
        for key, value in manifest["tested_requested"].items():
            if params.get(key) != value:
                raise ValueError("Fresh-session parameter mismatch: " + key)
        used = {o["receipt"]["agent_id"] for o in manifest["outputs"] if o["receipt"]}
        if metadata["agent_id"] in used:
            raise ValueError("Fresh session reused an agent ID")
    else:
        previous = next(o for o in manifest["outputs"] if o["run_id"] == session["runs"][output["turn"] - 2])
        if not previous["receipt"] or previous["receipt"]["agent_id"] != metadata["agent_id"]:
            raise ValueError("Followup must retain the preceding session agent")
    path = root / output["raw"]
    if not path.is_file() or not path.read_text().strip():
        raise ValueError("Actual nonempty raw output required")
    output["receipt"] = {**metadata, "sha256": digest(path)}
    write_json(root / "manifest.json", manifest)


def blind(root):
    manifest = verify(root, complete=True)
    destination = root / "blind"
    if destination.exists():
        raise ValueError("Blind packets already exist")
    destination.mkdir()
    rng = random.Random(manifest["seed"] + 1)
    outputs = list(manifest["outputs"])
    rng.shuffle(outputs)
    crosswalk = {}
    for index, output in enumerate(outputs, 1):
        item_id = f"item{index:03}"
        session = next(s for s in manifest["sessions"] if s["session_id"] == output["session_id"])
        history = [next(o for o in manifest["outputs"] if o["run_id"] == r) for r in session["runs"][:output["turn"]]]
        write_json(destination / (item_id + ".json"), {"item_id": item_id,
            "conversation": [{"task": h["task"], "response": (root / h["raw"]).read_text()} for h in history]})
        crosswalk[item_id] = output["run_id"]
    write_json(root / "blind-crosswalk.json", crosswalk)
    write_json(root / "blind-hashes.json", {p.name: digest(p) for p in sorted(destination.glob("*.json"))})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "verify", "record", "blind"])
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--registry", type=Path, default=Path("persona-design-v0.2/construct-registry.md"))
    parser.add_argument("--seed", type=int, default=20261022)
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--run")
    parser.add_argument("--metadata", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(args.root.resolve(), args.registry, args.seed)
        elif args.command == "verify":
            verify(args.root.resolve(), args.complete)
        elif args.command == "record":
            record(args.root.resolve(), args.run, read_json(args.metadata))
        else:
            blind(args.root.resolve())
    except (ValueError, KeyError, StopIteration, OSError) as exc:
        parser.exit(1, str(exc) + "\n")
    print(args.command + ": OK")


if __name__ == "__main__":
    main()
