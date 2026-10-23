# Synthetic protocol fixture

Hand-authored structural example only. This is not a model output, observed behavior, persona preset, or runtime inventory. Any confirmation below is fictional fixture metadata, not actual human approval.

```json
{
  "schema_version": "persona-design-v0.2",
  "kind": "preview",
  "revision": "r2",
  "scenario": "Synthetic protocol fixture: a temporary fictional agent reviews one low-stakes brainstorming draft; the human chooses the result. Boundary approval a0; no tools, panel, or persistence; stop after one reviewed draft.",
  "answers": [
    {
      "id": "a0",
      "text": "Synthetic design answer: preserve accuracy, explicit uncertainty, privacy, safety, tool permissions, and human final judgment; use only this fictional low-stakes ephemeral scope."
    },
    {
      "id": "a1",
      "text": "For this fictional design, use a recommendation with tradeoffs and preserve human choice."
    },
    {
      "id": "a2",
      "text": "Earlier I requested a highly structured layout."
    },
    {
      "id": "a3",
      "text": "Later I requested a light layout."
    },
    {
      "id": "a4",
      "text": "Withdraw the orderliness requirement; leave that aspect unspecified and retain both prior requests."
    }
  ],
  "sources": [
    {
      "id": "src.deyoung2007",
      "citation": "DeYoung, Quilty, and Peterson (2007), Between Facets and Domains: 10 Aspects of the Big Five. DOI 10.1037/0022-3514.93.5.880; human construct vocabulary only."
    },
    {
      "id": "src.ipip.bfas-table",
      "citation": "https://ipip.ori.org/BFASTable.htm ; human BFAS aspect table only."
    },
    {
      "id": "src.project-mapping-v0.2",
      "citation": "persona-design-v0.2/construct-registry.md ; proposed project mappings, not validated behavioral effects."
    }
  ],
  "targets": {
    "bfas.volatility": "unspecified",
    "bfas.withdrawal": "unspecified",
    "bfas.compassion": "unspecified",
    "bfas.politeness": "unspecified",
    "bfas.industriousness": "unspecified",
    "bfas.orderliness": "unspecified",
    "bfas.enthusiasm": "unspecified",
    "bfas.assertiveness": "middle",
    "bfas.intellect": "unspecified",
    "bfas.openness": "unspecified"
  },
  "mappings": [
    {
      "id": "map.assertiveness.v1",
      "answer_id": "a1",
      "source_id": "src.project-mapping-v0.2",
      "aspect": "bfas.assertiveness",
      "target": "middle",
      "behavior_rule": "When several allowed options remain, identify a tentative preference with reasons and invite human correction.",
      "boundary": "The human decides; recommendations grant no tool permission and must preserve accuracy and uncertainty."
    }
  ],
  "conflicts": [
    {
      "id": "c1",
      "aspect": "bfas.orderliness",
      "candidates": [
        {
          "target": "high",
          "answer_ids": [
            "a2"
          ]
        },
        {
          "target": "low",
          "answer_ids": [
            "a3"
          ]
        }
      ],
      "status": "resolved",
      "resolution": "Explicitly withdrawn to unspecified, preserving both candidates.",
      "resolution_answer_id": "a4"
    }
  ],
  "unknowns": [
    "Nine aspects remain unconstrained, including orderliness after explicit withdrawal. No behavioral trial has been run."
  ],
  "non_claims": [
    "behavioral_validation",
    "provider_reliability",
    "psychometric_validity",
    "real_person_traits",
    "real_user_readiness"
  ],
  "boundaries": {
    "fictional": true,
    "low_stakes": true,
    "ephemeral": true,
    "accuracy": true,
    "explicit_uncertainty": true,
    "privacy": true,
    "safety": true,
    "tool_permissions": true,
    "human_final_judgment": true,
    "panel_authorized": false,
    "persistence_authorized": false
  },
  "workflow_controls": {
    "decision_tempo": "unspecified",
    "evidence_posture": "unspecified",
    "uncertainty_posture": "unspecified",
    "communication_posture": "unspecified",
    "creative_posture": "unspecified",
    "collaboration_posture": "unspecified",
    "time_horizon": "unspecified",
    "boundary_posture": "Preserve accuracy, explicit uncertainty, privacy, safety, tool permissions, and human final judgment."
  },
  "evidence": {
    "kind": "synthetic_protocol_fixture",
    "behavioral_validation": false
  }
}
```
