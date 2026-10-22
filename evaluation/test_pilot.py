import json
import tempfile
import unittest
from pathlib import Path

from pilot import blind, prepare, read_json, record, verify, write_json


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
            (self.root / output["raw"]).write_text("TEST FIXTURE response\n")
            record(self.root, output["run_id"], {"agent_id": output["session_id"], "started_at": "test", "ended_at": "test",
                "requested_tool": "test-only", "requested_parameters": {
                    "message": (self.root / output["message"]).read_text(),
                    **(manifest["tested_requested"] if output["turn"] == 1 else {"target": output["session_id"]})},
                "returned_metadata": {}, "limitations": "fixture"})
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

    def test_manifest_design_cannot_be_relabelled(self):
        manifest = read_json(self.root / "manifest.json")
        manifest["sessions"][0]["condition"] = "baseline"
        manifest["sessions"][1]["condition"] = "tampered"
        write_json(self.root / "manifest.json", manifest)
        with self.assertRaisesRegex(ValueError, "manifest design"):
            verify(self.root)


if __name__ == "__main__":
    unittest.main()
