#!/usr/bin/env python3
"""Optional structural checks for the Markdown interview protocol; no runtime."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


class ValidationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path):
    """Read exactly one JSON fence. Prose remains for human review."""
    text = Path(path).read_text(encoding="utf-8")
    blocks = re.findall(r"^```json\s*\n(.*?)^```\s*$", text, re.M | re.S)
    require(len(blocks) == 1, "expected exactly one fenced json payload")
    try:
        result = json.loads(blocks[0], object_pairs_hook=unique_object)
    except (ValueError, TypeError) as exc:
        raise ValidationError(f"invalid JSON: {exc}") from exc
    require(isinstance(result, dict), "payload must be an object")
    return result


def digest(preview):
    """SHA-256 over UTF-8 canonical JSON, not the surrounding Markdown."""
    canonical = json.dumps(preview, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def keys(value, expected, where):
    require(isinstance(value, dict), f"{where} must be an object")
    require(set(value) == set(expected), f"{where} fields must be exactly: {', '.join(expected)}")


def strings(value, where, minimum=0):
    require(isinstance(value, list) and len(value) >= minimum and all(nonempty(x) for x in value), f"{where} must contain nonempty strings")


def records(value, fields, where):
    require(isinstance(value, list), f"{where} must be a list")
    indexed = {}
    for row in value:
        keys(row, fields, where)
        require(all(nonempty(row[f]) for f in fields), f"{where} values must be nonempty strings")
        require(row["id"] not in indexed, f"duplicate {where} id")
        indexed[row["id"]] = row
    return indexed


ASPECTS = (
    "bfas.volatility", "bfas.withdrawal", "bfas.compassion", "bfas.politeness",
    "bfas.industriousness", "bfas.orderliness", "bfas.enthusiasm",
    "bfas.assertiveness", "bfas.intellect", "bfas.openness",
)
SOURCE_IDS = {"src.deyoung2007", "src.ipip.bfas-table", "src.project-mapping-v0.2"}
WORKFLOW = ("decision_tempo", "evidence_posture", "uncertainty_posture", "communication_posture", "creative_posture", "collaboration_posture", "time_horizon", "boundary_posture")
BOUNDARY_POSTURE = "Preserve accuracy, explicit uncertainty, privacy, safety, tool permissions, and human final judgment."
TARGETS = {"low", "middle", "high", "unspecified"}
NON_CLAIMS = {"psychometric_validity", "real_person_traits", "behavioral_validation", "provider_reliability", "real_user_readiness"}
BOUNDARIES = {
    "fictional": True, "low_stakes": True, "ephemeral": True,
    "accuracy": True, "explicit_uncertainty": True, "privacy": True,
    "safety": True, "tool_permissions": True,
    "human_final_judgment": True, "panel_authorized": False,
    "persistence_authorized": False,
}
PREVIEW_FIELDS = ("schema_version", "kind", "revision", "scenario", "answers", "sources", "targets", "mappings", "conflicts", "unknowns", "non_claims", "boundaries", "evidence", "workflow_controls")


def validate_preview(preview, final=False):
    keys(preview, PREVIEW_FIELDS, "preview")
    require(preview["schema_version"] == "persona-design-v0.2", "unsupported schema_version")
    require(preview["kind"] == "preview", "kind must be preview")
    require(isinstance(preview["revision"], str) and re.fullmatch(r"r[1-9][0-9]*", preview["revision"]) and nonempty(preview["scenario"]), "revision rN and scenario required")
    answers = records(preview["answers"], ("id", "text"), "answers")
    sources = records(preview["sources"], ("id", "citation"), "sources")
    require(set(sources) == SOURCE_IDS, "sources must cite the three required registry source IDs")
    keys(preview["workflow_controls"], WORKFLOW, "workflow_controls")
    require(all(nonempty(v) for v in preview["workflow_controls"].values()), "workflow controls must be text or unspecified")
    require(preview["workflow_controls"]["boundary_posture"] == BOUNDARY_POSTURE, "boundary_posture must preserve fixed invariants")
    keys(preview["targets"], ASPECTS, "targets")
    require(all(isinstance(v, str) and v in TARGETS for v in preview["targets"].values()), "targets use only qualitative low|middle|high|unspecified; no scores")
    strings(preview["unknowns"], "unknowns")
    strings(preview["non_claims"], "non_claims")
    require(set(preview["non_claims"]) == NON_CLAIMS, "required non_claims missing or unsupported claim added")
    keys(preview["boundaries"], BOUNDARIES, "boundaries")
    require(all(type(preview["boundaries"][k]) is bool and preview["boundaries"][k] is v for k, v in BOUNDARIES.items()), "baseline boundary invariant violated")
    keys(preview["evidence"], ("kind", "behavioral_validation"), "evidence")
    require(preview["evidence"]["kind"] in ("not_run", "synthetic_protocol_fixture"), "unsupported behavioral evidence claim; observed runs require separate evidence records")
    require(preview["evidence"]["behavioral_validation"] is False, "static validation cannot claim behavioral validation")
    mappings = records(preview["mappings"], ("id", "answer_id", "source_id", "aspect", "target", "behavior_rule", "boundary"), "mappings")
    mapped = set()
    for mapping in mappings.values():
        aspect = mapping["aspect"]
        require(aspect in ASPECTS, "mapping references unknown aspect")
        require(aspect not in mapped, "conflicting or duplicate mappings for aspect")
        mapped.add(aspect)
        require(mapping["id"] == f"map.{aspect.split('.')[1]}.v1", "mapping id must be map.<aspect>.v1")
        require(mapping["answer_id"] in answers, "dangling mapping answer_id")
        require(mapping["source_id"] in sources, "dangling mapping source_id")
        require(mapping["source_id"] == "src.project-mapping-v0.2", "agent mapping must cite project hypothesis, not human construct evidence")
        require(mapping["target"] != "unspecified" and mapping["target"] == preview["targets"][aspect], "mapping target conflicts with final target or constrains unspecified")
    requested = {a for a, t in preview["targets"].items() if t != "unspecified"}
    require(mapped == requested, "every requested target needs one mapping; unspecified must stay unconstrained")
    require(isinstance(preview["conflicts"], list), "conflicts must be a list")
    conflict_ids = set()
    for conflict in preview["conflicts"]:
        keys(conflict, ("id", "aspect", "candidates", "status", "resolution", "resolution_answer_id"), "conflict")
        require(nonempty(conflict["id"]) and conflict["id"] not in conflict_ids, "conflict id missing or duplicate")
        conflict_ids.add(conflict["id"])
        require(nonempty(conflict["aspect"]) and (conflict["aspect"] in ASPECTS or conflict["aspect"] in {"workflow_controls." + k for k in WORKFLOW}), "conflict references unknown aspect or workflow control")
        require(isinstance(conflict["candidates"], list) and len(conflict["candidates"]) >= 2, "retain at least two conflict candidates")
        candidate_records = set()
        for candidate in conflict["candidates"]:
            keys(candidate, ("target", "answer_ids"), "conflict candidate")
            require(nonempty(candidate["target"]) and (conflict["aspect"].startswith("workflow_controls.") or candidate["target"] in TARGETS), "invalid candidate target")
            strings(candidate["answer_ids"], "candidate answer_ids", 1)
            require(all(a in answers for a in candidate["answer_ids"]), "dangling candidate answer ref")
            identity = (candidate["target"], tuple(candidate["answer_ids"]))
            require(identity not in candidate_records, "exact duplicate conflict candidate")
            candidate_records.add(identity)
        require(conflict["status"] in ("resolved", "unresolved"), "invalid conflict status")
        require(isinstance(conflict["resolution"], str), "conflict resolution must be text")
        if conflict["status"] == "resolved":
            require(nonempty(conflict["resolution"]) and nonempty(conflict["resolution_answer_id"]) and conflict["resolution_answer_id"] in answers, "resolved conflict needs resolution and answer record")
        if final:
            require(conflict["status"] == "resolved", "final spec has unresolved conflict")
    return preview


def validate_spec(spec, preview):
    keys(spec, ("kind", "approved_preview", "approval", "review"), "spec")
    require(spec["kind"] == "spec", "kind must be spec")
    validate_preview(preview, final=True)
    validate_preview(spec["approved_preview"], final=True)
    require(spec["approved_preview"] == preview, "spec changed from supplied approved preview")
    keys(spec["approval"], ("status", "revision", "digest", "confirmed_by", "record_ref"), "approval")
    approval = spec["approval"]
    require(approval["status"] == "confirmed", "final spec requires explicit confirmed approval")
    require(approval["revision"] == preview["revision"], "approval revision mismatch")
    require(approval["digest"] is None or approval["digest"] == digest(preview), "approval digest mismatch")
    require(nonempty(approval["confirmed_by"]) and nonempty(approval["record_ref"]), "approval provenance record required")
    require(spec["review"] == "Pass", "final spec requires independent manual review Pass")
    return spec


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    preview_parser = sub.add_parser("preview", help="check a preview and print its canonical digest")
    preview_parser.add_argument("path")
    spec_parser = sub.add_parser("spec", help="check a final spec against a separately supplied preview")
    spec_parser.add_argument("path")
    spec_parser.add_argument("--preview", required=True)
    spec_parser.add_argument("--reload", help="also compare a saved/reloaded spec JSON payload")
    args = parser.parse_args(argv)
    try:
        payload = load(args.path)
        if args.command == "preview":
            validate_preview(payload)
            print(f"PASS structural preview: {digest(payload)}")
        else:
            preview = load(args.preview)
            validate_spec(payload, preview)
            if args.reload:
                reloaded = load(args.reload)
                validate_spec(reloaded, preview)
                require(reloaded == payload, "saved/reloaded spec differs from original")
            print("PASS structural spec; human confirmation and behavior remain unverified")
    except (ValidationError, OSError, ValueError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
