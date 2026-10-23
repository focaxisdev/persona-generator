"""Rebuild handwritten SYNTHETIC format fixtures; never authentic owner choices.

This script invents test receipts explicitly marked synthetic_fixture. It is not
an interview, approval, confirmation, review or production authoring workflow.
"""
import hashlib
import json
from pathlib import Path
from profiles import compiler as c


def make(profile_id, anchors, revision='r1', audit='Synthetic format fixture; not authentic owner input.', *, catalog_id='persona-profile-catalog-v1'):
    catalog = c.load_catalog(catalog_id=catalog_id)
    preview = {
        'schema_version': c.SCHEMA_VERSION, 'kind': 'preview',
        'profile_id': profile_id, 'revision': revision,
        'catalog': {'id': catalog['id'], 'sha256': c.TRUSTED_CATALOGS[catalog_id][1]},
        'sources': catalog['dependencies'], 'targets': dict(zip(c.ASPECTS, anchors)),
        'mappings': [], 'answers': [], 'approvals': [], 'conflicts': [], 'blocking_issues': [],
        'unknowns': [audit], 'history': ['SYNTHETIC FIXTURE ONLY: no owner interview or model observation.'],
        'evidence': {'status': 'untested', 'behavioral_validation': False},
    }
    for aspect, anchor in preview['targets'].items():
        if anchor == 'unspecified':
            continue
        name = aspect.split('.')[1]; hypothesis_id = c.hypothesis_for_aspect(catalog, aspect)[0]
        mapping = {'id': hypothesis_id, 'aspect': aspect, 'anchor': anchor,
                   **{k: catalog['hypotheses'][hypothesis_id]['anchors'][anchor][k] for k in ('trigger', 'rule', 'boundary')},
                   'answer_ids': ['answer-' + name], 'approval_id': 'approval-' + name}
        preview['mappings'].append(mapping)
        preview['answers'].append({'id': 'answer-' + name, 'origin': 'synthetic_fixture', 'kind': 'choice',
                                   'text': 'Invented example chooses ' + anchor + ' for ' + aspect,
                                   'record_ref': 'synthetic://fixture/choice/' + name})
        preview['approvals'].append({'id': 'approval-' + name, 'answer_id': 'answer-' + name,
                                    'aspect': aspect, 'anchor': anchor, 'candidate_sha256': c.digest(c.candidate(mapping))})
    presented = (json.dumps(preview, indent=2, ensure_ascii=False) + '\n').encode()
    effective = c._render(preview, catalog)
    spec = {'schema_version': c.SCHEMA_VERSION, 'kind': 'spec', 'approved_preview': preview,
            'confirmation': {'status': 'confirmed', 'profile_id': profile_id, 'revision': revision,
                             'snapshot_sha256': c.digest(preview), 'presented_file_sha256': hashlib.sha256(presented).hexdigest(),
                             'effective_sha256': hashlib.sha256(effective.encode()).hexdigest(),
                             'record_ref': 'synthetic://fixture/not-owner-confirmation',
                             'confirmed_by': 'synthetic-format-writer', 'origin': 'synthetic_fixture'},
            'review': {'status': 'Pass', 'record_ref': 'synthetic://fixture/not-authentic-review'}}
    c.validate_spec(spec, presented)
    return preview, presented, spec


def main():
    for name, anchors in (
        ('combination-a', ('low', 'high', 'middle', 'low', 'high', 'low', 'middle', 'high', 'low', 'high')),
        ('combination-b', ('high', 'low', 'high', 'middle', 'low', 'high', 'low', 'middle', 'high', 'low')),
    ):
        _, presented, spec = make('synthetic-' + name, anchors)
        folder = Path(__file__).resolve().parent
        (folder / (name + '-preview.json')).write_bytes(presented)
        (folder / (name + '-spec.json')).write_text(json.dumps(spec, indent=2, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    main()
