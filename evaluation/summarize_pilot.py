#!/usr/bin/env python3
"""Join frozen pilot conditions to locked ratings; report mechanical observations only."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import pilot
import verify_ratings as vr


def mapping_rows(plan):
    rows = re.findall(r'^\| (A\d{2}) \| (map\.([a-z]+)\.v1) / (B\d{2}) \|', plan, re.MULTILINE)
    vr.require(len(rows) == 10 and {r[0] for r in rows} == {f'A{i:02}' for i in range(1, 11)},
               'Expected ten axis/mapping rows in frozen plan')
    vr.require(len({r[2] for r in rows}) == 10, 'Duplicate mapping names in frozen plan')
    return sorted(rows)


def collect(root):
    # This gate precedes every condition/crosswalk read and all raw-output reads.
    vr.require((root / vr.LOCK_NAME).is_file(), 'Ratings lock required before any unblinding join')
    integrity = vr.verify(root)
    manifest = pilot.verify(root, complete=True)
    plan = (root / 'frozen/plan.md').read_text(encoding='utf-8')
    mappings = mapping_rows(plan)
    rubric = vr.read_json(root / 'frozen/rubric.json')
    crosswalk = vr.read_json(root / 'blind-crosswalk.json')
    runs = {o['run_id']: o for o in manifest['outputs']}
    vr.require(len(runs) == 102 and isinstance(crosswalk, dict)
               and set(crosswalk) == {p[:-5] for p in integrity['blind_hashes']}, 'Crosswalk blind coverage mismatch')
    vr.require(all(isinstance(v, str) for v in crosswalk.values())
               and len(set(crosswalk.values())) == 102 and set(crosswalk.values()) == set(runs),
               'Crosswalk must be a bijection onto all 102 runs')
    sessions = {s['session_id']: s for s in manifest['sessions']}
    ratings = {}
    for filename in integrity['rating_hashes']:
        for row in vr.read_json(root / 'ratings' / filename):
            ratings[row['blind_id']] = row
    records = []
    for blind_id, run_id in sorted(crosswalk.items()):
        run = runs[run_id]
        session = sessions[run['session_id']]
        packet = vr.read_json(root / 'blind' / (blind_id + '.json'))
        history = [runs[r] for r in session['runs'][:run['turn']]]
        expected = [{'task': h['task'], 'response': (root / h['raw']).read_text(encoding='utf-8')} for h in history]
        vr.require(packet['conversation'] == expected, 'Crosswalk conversation mismatch: ' + blind_id)
        rating = ratings[blind_id]
        records.append({'blind_id': blind_id, 'run_id': run_id, 'session_id': session['session_id'],
            'condition': session['condition'], 'scenario': session['scenario'], 'reload': session['reload'],
            'turn': run['turn'], 'blind_path': 'blind/' + blind_id + '.json', 'raw_path': run['raw'],
            'word_count_whitespace': len(packet['conversation'][-1]['response'].split()),
            'axes': rating['axes'], 'guardrails': rating['guardrails'],
            'guardrail_violations': [g['guardrail_id'] for g in rating['guardrails'] if g['rating'] == 'violation'],
            'guardrail_unclear': [g['guardrail_id'] for g in rating['guardrails'] if g['rating'] == 'unclear'],
            'blind_leakage': rating['blind_leakage'], 'limitations': rating['limitations']})
    def select(condition, scenario, reload=False, turn=1):
        found = [r for r in records if (r['condition'], r['scenario'], r['reload'], r['turn']) ==
                 (condition, scenario, reload, turn)]
        vr.require(len(found) == 1, 'Missing or duplicated comparison cell')
        return found[0]
    def view(record, axis=None):
        return {'blind_id': record['blind_id'], 'run_id': record['run_id'],
            'blind_path': record['blind_path'], 'raw_path': record['raw_path'],
            'categories': {a['axis_id']: a['category'] for a in record['axes'] if axis is None or a['axis_id'] == axis},
            'guardrail_violations': record['guardrail_violations'], 'guardrail_unclear': record['guardrail_unclear']}
    initial = []
    repeats = []
    for axis, mapping, name, case in mappings:
        for scenario in ('S1', 'S2', 'S3'):
            initial.append({'axis_id': axis, 'mapping_id': mapping, 'case_id': case, 'scenario': scenario,
                'low': view(select(name + '_low', scenario), axis),
                'high': view(select(name + '_high', scenario), axis),
                'shared_baseline': view(select('baseline', scenario), axis)})
        repeats.append({'condition': name + '_high', 'scenario': 'S1', 'target_axis': axis,
            'original': view(select(name + '_high', 'S1')), 'repeat': view(select(name + '_high', 'S1', True))})
    for scenario in ('S1', 'S2', 'S3'):
        repeats.append({'condition': 'baseline', 'scenario': scenario, 'target_axis': None,
            'original': view(select('baseline', scenario)), 'repeat': view(select('baseline', scenario, True))})
    multi = []
    for session in sorted(manifest['sessions'], key=lambda s: s['order']):
        if session['rounds'] == 3:
            multi.append({'session_id': session['session_id'], 'condition': session['condition'], 'scenario': session['scenario'],
                'rounds': [view(select(session['condition'], session['scenario'], False, turn)) for turn in (1, 2, 3)]})
    vr.require(len(initial) == 30 and len(repeats) == 13 and len(multi) == 13, 'Comparison coverage mismatch')
    cross_axes = []
    overlap_names = {name: (axis, mapping, case) for axis, mapping, name, case in mappings if axis in ('A05', 'A06')}
    for record in records:
        name = record['condition'].rsplit('_', 1)[0]
        if name in overlap_names:
            item = view(record)
            item['categories'] = {k: v for k, v in item['categories'].items() if k in ('A05', 'A06')}
            item.update(condition=record['condition'], scenario=record['scenario'], turn=record['turn'], reload=record['reload'])
            item.update(zip(('target_axis', 'mapping_id', 'case_id'), overlap_names[name]))
            cross_axes.append(item)
    violations = [{'blind_id': r['blind_id'], 'run_id': r['run_id'], 'condition': r['condition'],
                   'scenario': r['scenario'], 'turn': r['turn'], 'guardrail': g}
                  for r in records for g in r['guardrails'] if g['rating'] == 'violation']
    leakage = [{'blind_id': r['blind_id'], 'run_id': r['run_id'], **r['blind_leakage']}
               for r in records if r['blind_leakage']['present']]
    return {'schema_version': 'pilot-mechanical-observations-v1',
        'generated_at': datetime.now(timezone.utc).isoformat(), 'ratings_lock_sha256': vr.digest(root / vr.LOCK_NAME),
        'scope': 'Mechanical joins of locked descriptive ratings; no semantic adjudication, psychological validity, release pass, population estimates or p-values.',
        'baseline_note': 'Three shared initial baseline observations are reused across the 30 comparisons; they are not 30 independent baseline observations.',
        'word_count_note': 'Whitespace split is diagnostic only; no language or strategy assessment is computed.',
        'rubric_evidence_classes': {a['id']: a.get('evidence_class', 'unspecified') for a in rubric['axes']},
        'initial_pairs': initial, 'repeat_comparisons': repeats, 'multi_round': multi,
        'a05_a06_cross_axis': cross_axes, 'guardrail_violations': violations,
        'blind_leakage_present': leakage, 'outputs': records}


def render(doc):
    lines = ['# Locked pilot observations', '', doc['scope'], '', doc['baseline_note'], '', doc['word_count_note'], '',
             'All categories and flags below are the locked judge records. Empty violation lists mean no violation was rated; unclear flags remain separate for review.', '']
    def escape(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    def table(headers, rows):
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('| ' + ' | '.join('---' for _ in headers) + ' |')
        for row in rows:
            lines.append('| ' + ' | '.join(escape(v) for v in row) + ' |')
        lines.append('')
    def ref(record):
        return f"[{record['blind_id']}](../{record['blind_path']}) / [{record['run_id']}](../{record['raw_path']})"
    def cats(record):
        return ', '.join(k + '=' + v for k, v in record['categories'].items())
    def flags(record):
        return 'violations=' + ','.join(record['guardrail_violations']) + '; unclear=' + ','.join(record['guardrail_unclear'])
    lines.extend(['## Initial low/high pairs and actual shared baseline', ''])
    table(['Case / axis / scenario', 'Low', 'High', 'Shared baseline', 'Low flags', 'High flags', 'Baseline flags'],
          [(f"{p['case_id']} / {p['axis_id']} / {p['scenario']}", ref(p['low']) + ' ' + cats(p['low']),
            ref(p['high']) + ' ' + cats(p['high']), ref(p['shared_baseline']) + ' ' + cats(p['shared_baseline']),
            flags(p['low']), flags(p['high']), flags(p['shared_baseline'])) for p in doc['initial_pairs']])
    lines.extend(['## Fresh-context repeat comparisons', ''])
    table(['Condition / scenario', 'Original', 'Repeat', 'Original flags', 'Repeat flags'],
          [(p['condition'] + ' / ' + p['scenario'], ref(p['original']) + ' ' + cats(p['original']),
            ref(p['repeat']) + ' ' + cats(p['repeat']), flags(p['original']), flags(p['repeat'])) for p in doc['repeat_comparisons']])
    lines.extend(['## Multi-round categories and guardrails', ''])
    table(['Condition / scenario', 'Round', 'Output / categories', 'Flags'],
          [(p['condition'] + ' / ' + p['scenario'], i, ref(r) + ' ' + cats(r), flags(r))
           for p in doc['multi_round'] for i, r in enumerate(p['rounds'], 1)])
    lines.extend(['## B05/A05 and B06/A06 cross-axis records', '',
                  'Co-occurrence is reported for review; it does not establish independent mechanisms.', ''])
    table(['Condition / scenario / turn / reload', 'Output / categories', 'Flags'],
          [(f"{r['condition']} / {r['scenario']} / {r['turn']} / {r['reload']}", ref(r) + ' ' + cats(r), flags(r)) for r in doc['a05_a06_cross_axis']])
    lines.extend(['## Every rated guardrail violation', ''])
    table(['Blind / run', 'Condition / scenario / turn', 'Guardrail', 'Quotes', 'Reason'],
          [(r['blind_id'] + ' / ' + r['run_id'], f"{r['condition']} / {r['scenario']} / {r['turn']}",
            r['guardrail']['guardrail_id'], json.dumps(r['guardrail']['quotes'], ensure_ascii=False), r['guardrail']['reason'])
           for r in doc['guardrail_violations']])
    lines.extend(['## Blind leakage rated present', ''])
    table(['Blind / run', 'Quotes', 'Reason'], [(r['blind_id'] + ' / ' + r['run_id'],
          json.dumps(r['quotes'], ensure_ascii=False), r['reason']) for r in doc['blind_leakage_present']])
    lines.extend(['## Per-output whitespace word counts and flags', ''])
    table(['Output', 'Condition / scenario / turn / reload', 'Words', 'Flags', 'Leakage present'],
          [(ref(r), f"{r['condition']} / {r['scenario']} / {r['turn']} / {r['reload']}",
            r['word_count_whitespace'], flags(r), r['blind_leakage']['present']) for r in doc['outputs']])
    return '\n'.join(lines)


def summarize(root):
    doc = collect(root)
    report = render(doc)
    destination = root / 'analysis'
    vr.require(not destination.exists() and not destination.is_symlink(), 'Analysis destination exists; refusing overwrite')
    destination.mkdir()
    with (destination / 'observations.json').open('x', encoding='utf-8') as handle:
        json.dump(doc, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    with (destination / 'report-tables.md').open('x', encoding='utf-8') as handle:
        handle.write(report)
    return doc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    try:
        summarize(args.root.resolve())
    except (ValueError, OSError, TypeError, KeyError, StopIteration, RecursionError) as exc:
        parser.exit(1, str(exc) + '\n')
    print('summary: OK (mechanical observations only)')


if __name__ == '__main__':
    main()
