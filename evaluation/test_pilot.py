import json
import copy
import tempfile
import unittest
from pathlib import Path

from pilot import blind, digest, prepare, read_json, record, verify, write_json


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        write_json(self.root / "frozen/scenarios.json", {"output_budget_words": 250,
            "scenarios": [{"id": f"S{i}", "round1": f"Task {i}", "round2": f"Changed {i}"} for i in range(1, 4)],
            "round3": "Pressure"})
        write_json(self.root / "frozen/rubric.json", {"axes": []})
        self.registry = Path(__file__).resolve().parents[1] / "persona-design-v0.2/construct-registry.md"
        prepare(self.root, self.registry, 20261022)

    def metadata(self, output, manifest=None):
        manifest = manifest or read_json(self.root / "manifest.json")
        agent = "/root/synthetic_" + output["session_id"]
        return {"agent_id": agent,
            "started_at": "2026-10-22T09:00:00Z", "ended_at": "2026-10-22T09:00:01+00:00",
            "requested_tool": "collaboration.spawn_agent" if output["turn"] == 1 else "collaboration.followup_task",
            "requested_parameters": {"message": (self.root / output["message"]).read_text(),
                **({"task_name": "synthetic_" + output["session_id"], **manifest["tested_requested"]}
                   if output["turn"] == 1 else {"target": agent})},
            "returned_metadata": {"task_name": agent, "acknowledged": True},
            "limitations": "SYNTHETIC fixture; acknowledgment is not completion proof"}

    def seal(self, output):
        (self.root / output["raw"]).write_text("SYNTHETIC response\n")
        record(self.root, output["run_id"], self.metadata(output))

    def test_coverage_order_and_frozen_inputs(self):
        manifest = verify(self.root)
        self.assertEqual(len(manifest["sessions"]), 76)
        self.assertEqual(len(manifest["outputs"]), 102)
        self.assertEqual(sum(s["reload"] for s in manifest["sessions"]), 13)
        self.assertEqual(sum(s["rounds"] == 3 for s in manifest["sessions"]), 13)
        self.assertEqual(len({o["run_id"] for o in manifest["outputs"]}), 102)
        (self.root / "frozen/scenarios.json").write_text("mutated")
        with self.assertRaisesRegex(ValueError, "Frozen input"):
            verify(self.root)

    def test_followups_do_not_reinforce_condition(self):
        manifest = verify(self.root)
        for output in manifest["outputs"]:
            packet = (self.root / output["packet"]).read_text()
            if output["turn"] > 1:
                self.assertNotIn("engineering condition", packet)
                self.assertNotIn("Accuracy, explicit uncertainty", packet)
                self.assertTrue(packet.startswith("Keep this response"))
    def test_reload_phase_and_byte_identity(self):
        manifest = verify(self.root)
        self.assertTrue(all(not s["reload"] for s in manifest["sessions"][:63]))
        self.assertTrue(all(s["reload"] for s in manifest["sessions"][63:]))
        for session in manifest["sessions"][63:]:
            original = next(s for s in manifest["sessions"][:63]
                            if (s["condition"], s["scenario"]) == (session["condition"], session["scenario"]))
            def packet_bytes(s):
                output = next(o for o in manifest["outputs"] if o["run_id"] == s["runs"][0])
                return (self.root / output["packet"]).read_bytes()
            self.assertEqual(packet_bytes(original), packet_bytes(session))

    def test_receipts_and_blinding(self):
        manifest = read_json(self.root / "manifest.json")
        for output in manifest["outputs"]:
            self.seal(output)
        verify(self.root, complete=True)
        blind(self.root)
        packets = list((self.root / "blind").glob("*.json"))
        self.assertEqual(len(packets), 102)
        for packet in packets:
            doc = read_json(packet)
            self.assertEqual(set(doc), {"item_id", "conversation"})
            self.assertNotIn("condition", packet.read_text())
        first = manifest["outputs"][0]
        with self.assertRaisesRegex(ValueError, "already sealed"):
            record(self.root, first["run_id"], {})
        (self.root / first["raw"]).write_text("edited")
        with self.assertRaisesRegex(ValueError, "Raw output"):
            verify(self.root)

    def test_invalid_receipts_rejected_by_record_and_verify(self):
        manifest = read_json(self.root / "manifest.json")
        output = manifest["outputs"][0]
        (self.root / output["raw"]).write_text("SYNTHETIC response\n")
        cases = [
            ("wrong tool", lambda r: r.update(requested_tool="collaboration.send_message")),
            ("invalid date", lambda r: r.update(started_at="invalid timestamp")),
            ("naive date", lambda r: r.update(started_at="2026-10-22T09:00:00")),
            ("non UTC", lambda r: r.update(started_at="2026-10-22T09:00:00+01:00")),
            ("end before start", lambda r: r.update(ended_at="2026-10-22T08:59:59Z")),
            ("wrong message", lambda r: r["requested_parameters"].update(message="SYNTHETIC replacement")),
            ("wrong model", lambda r: r["requested_parameters"].update(model="SYNTHETIC wrong model")),
            ("wrong effort", lambda r: r["requested_parameters"].update(reasoning_effort="low")),
            ("inherited context", lambda r: r["requested_parameters"].update(fork_turns="all")),
            ("wrong spawn identity", lambda r: r["requested_parameters"].update(task_name="wrong")),
            ("false ack", lambda r: r["returned_metadata"].update(acknowledged=False)),
            ("numeric ack", lambda r: r["returned_metadata"].update(acknowledged=1)),
            ("failure status", lambda r: r["returned_metadata"].update(status="failed")),
            ("explicit error", lambda r: r["returned_metadata"].update(error="SYNTHETIC failure")),
            ("false success", lambda r: r["returned_metadata"].update(success=False)),
            ("no ack", lambda r: r.update(returned_metadata={})),
            ("wrong returned identity", lambda r: r["returned_metadata"].update(task_name="/root/wrong")),
        ]
        for label, mutate in cases:
            with self.subTest(label=label):
                metadata = self.metadata(output)
                mutate(metadata)
                with self.assertRaises(ValueError):
                    record(self.root, output["run_id"], metadata)
                self.assertIsNone(read_json(self.root / "manifest.json")["outputs"][0]["receipt"])
                tampered = copy.deepcopy(manifest)
                tampered["outputs"][0]["receipt"] = {**metadata, "sha256": digest(self.root / output["raw"])}
                write_json(self.root / "manifest.json", tampered)
                with self.assertRaisesRegex(ValueError, output["run_id"]):
                    verify(self.root)
                write_json(self.root / "manifest.json", manifest)

    def test_continuity_targets_and_fresh_identity_revalidated(self):
        manifest = read_json(self.root / "manifest.json")
        session = next(s for s in manifest["sessions"] if s["rounds"] == 3)
        first, followup = [next(o for o in manifest["outputs"] if o["run_id"] == r) for r in session["runs"][:2]]
        self.seal(first)
        (self.root / followup["raw"]).write_text("SYNTHETIC followup\n")
        metadata = self.metadata(followup)
        metadata["requested_parameters"]["target"] = "/root/wrong"
        with self.assertRaisesRegex(ValueError, "target"):
            record(self.root, followup["run_id"], metadata)
        # Relative names are accepted when they identify exactly one known agent.
        metadata["requested_parameters"]["target"] = metadata["agent_id"].rsplit("/", 1)[1]
        metadata["returned_metadata"] = {"task_name": metadata["agent_id"], "status": "followup accepted"}
        record(self.root, followup["run_id"], metadata)
        original = read_json(self.root / "manifest.json")
        for field in ("target", "agent_id"):
            with self.subTest(field=field):
                tampered = copy.deepcopy(original)
                receipt = next(o for o in tampered["outputs"] if o["run_id"] == followup["run_id"])["receipt"]
                if field == "target":
                    receipt["requested_parameters"][field] = "/root/wrong"
                else:
                    receipt[field] = "/root/wrong"
                    receipt["requested_parameters"]["target"] = "/root/wrong"
                    receipt["returned_metadata"]["task_name"] = "/root/wrong"
                write_json(self.root / "manifest.json", tampered)
                with self.assertRaises(ValueError):
                    verify(self.root)
        write_json(self.root / "manifest.json", original)
        another = next(o for o in manifest["outputs"] if o["turn"] == 1 and o["run_id"] != first["run_id"])
        (self.root / another["raw"]).write_text("SYNTHETIC response\n")
        metadata = self.metadata(another)
        metadata["agent_id"] = self.metadata(first)["agent_id"]
        metadata["requested_parameters"]["task_name"] = metadata["agent_id"]
        metadata["returned_metadata"]["task_name"] = metadata["agent_id"]
        with self.assertRaisesRegex(ValueError, "reused"):
            record(self.root, another["run_id"], metadata)
        tampered = copy.deepcopy(original)
        next(o for o in tampered["outputs"] if o["run_id"] == another["run_id"])["receipt"] = {
            **metadata, "sha256": digest(self.root / another["raw"])}
        write_json(self.root / "manifest.json", tampered)
        with self.assertRaisesRegex(ValueError, "reused"):
            verify(self.root)

    def test_ambiguous_relative_target_rejected(self):
        manifest = read_json(self.root / "manifest.json")
        session = next(s for s in manifest["sessions"] if s["rounds"] == 3)
        first, followup = [next(o for o in manifest["outputs"] if o["run_id"] == r) for r in session["runs"][:2]]
        another = next(o for o in manifest["outputs"] if o["turn"] == 1 and o["run_id"] != first["run_id"])
        for output, agent in [(first, "/root/a/shared"), (another, "/root/b/shared")]:
            metadata = self.metadata(output)
            metadata["agent_id"] = agent
            metadata["requested_parameters"]["task_name"] = agent
            metadata["returned_metadata"]["task_name"] = agent
            (self.root / output["raw"]).write_text("SYNTHETIC response\n")
            record(self.root, output["run_id"], metadata)
        metadata = self.metadata(followup)
        metadata["agent_id"] = "/root/a/shared"
        metadata["returned_metadata"]["task_name"] = "/root/a/shared"
        metadata["requested_parameters"]["target"] = "shared"
        (self.root / followup["raw"]).write_text("SYNTHETIC response\n")
        with self.assertRaisesRegex(ValueError, "target"):
            record(self.root, followup["run_id"], metadata)

    def test_manifest_design_cannot_be_relabelled(self):
        manifest = read_json(self.root / "manifest.json")
        manifest["sessions"][0]["condition"] = "baseline"
        manifest["sessions"][1]["condition"] = "tampered"
        write_json(self.root / "manifest.json", manifest)
        with self.assertRaisesRegex(ValueError, "manifest design"):
            verify(self.root)


if __name__ == "__main__":
    unittest.main()
