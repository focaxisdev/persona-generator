#!/usr/bin/env python3
"""Offline structural checks only; never generate responses or judge semantics."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
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


def read_json(path):
    def reject_constant(value):
        raise ValidationError(f"non-finite JSON constant: {value}")
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"),
                          object_pairs_hook=unique_object, parse_constant=reject_constant)
    except (ValueError, TypeError) as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def keys(value, expected, where):
    require(isinstance(value, dict), f"{where} must be an object")
    require(set(value) == set(expected), f"{where} fields must be exactly {sorted(expected)}")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def local_path(root, name):
    require(nonempty(name), "file reference must be nonempty text")
    relative = Path(name)
    require(not relative.is_absolute() and ".." not in relative.parts,
            "file references must stay within the design directory")
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), "file reference escapes design directory")
    return path


ASPECTS = ('B03', 'B05', 'B06', 'B08', 'B10')
ALL_ASPECTS = tuple(f'B{i:02}' for i in range(1, 11))
CASE_TO_ASPECT = dict(zip(ALL_ASPECTS, (
    'bfas.volatility', 'bfas.withdrawal', 'bfas.compassion', 'bfas.politeness',
    'bfas.industriousness', 'bfas.orderliness', 'bfas.enthusiasm',
    'bfas.assertiveness', 'bfas.intellect', 'bfas.openness')))
CONDITIONS = ('neutral', 'low', 'middle', 'high', 'unspecified')
ORDER_SEED = 'diagnostic-v2-2026-10-22'
BASE_COMMIT = '9aa9ff2534c4d1593f07386ad8b99250ea25e72c'
DESIGN_DIR = 'evaluation/diagnostic-v2'
CARDS = 'persona-design-v0.2/mapping-v2/cards.json'
PROTECTED = ('persona-design-v0.2', 'validation', 'evaluation/pilot-2026-10-22')
COMMON = ('Help with this fictional, low-stakes rehearsal. Give advisory suggestions only. '
          'Preserve accuracy, explicit uncertainty, privacy, safety, existing tool permissions, '
          'dissent, and human final judgment. Do not profile real people, diagnose, score '
          'personality, infer sensitive attributes, manipulate, or make high-stakes or '
          'autonomous final decisions. Do not execute actions, use external tools, persist '
          'personas, or run a panel. Remain civil and proportionate; do not assume unstated '
          'vulnerability, claim personal feelings, or give unsupported guarantees. '
          'Respond in English in at most 250 whitespace-delimited '
          'words; stop after one bounded answer.')


def string_ids(value, where, minimum=0):
    require(isinstance(value, list) and len(value) >= minimum and
            all(nonempty(x) for x in value), f'{where} must contain nonempty strings')
    require(len(value) == len(set(value)), f'{where} contains duplicate IDs')
    return set(value)


def rows_by_id(rows, fields, where, id_field='id'):
    require(isinstance(rows, list), f'{where} must be a list')
    indexed = {}
    for row in rows:
        keys(row, fields, where)
        require(nonempty(row[id_field]), f'{where} ID must be nonempty')
        require(row[id_field] not in indexed, f'duplicate {where} ID')
        indexed[row[id_field]] = row
    return indexed


def validate_inputs(design, cards):
    keys(design, ('schema_version', 'status', 'human_confirmation', 'release_status',
                 'generated_output_count', 'tasks', 'judges', 'rating_policy'), 'design')
    require(design['schema_version'] == 'diagnostic-v2-design', 'unsupported design schema')
    require(design['status'] == 'design_only' and design['human_confirmation'] == 'not_obtained'
            and design['release_status'] == 'blocked', 'design-only and unconfirmed status required')
    require(type(design['generated_output_count']) is int and design['generated_output_count'] == 0,
            'design must record zero generated outputs')
    tasks = rows_by_id(design['tasks'], ('id', 'aspect_id', 'prompt', 'requirements',
        'rubric_required_ids', 'ambiguity_policy', 'word_limit', 'word_count_method', 'stop_rule'), 'task')
    require(len(tasks) == 5 and {t['aspect_id'] for t in tasks.values()} == set(ASPECTS),
            'exactly one task per five selected aspects required')
    for task in tasks.values():
        require(nonempty(task['prompt']), 'task prompt required')
        requirements = rows_by_id(task['requirements'], ('id', 'text'), 'requirement')
        require(requirements and all(nonempty(r['text']) for r in requirements.values()),
                'explicit task requirements required')
        require(string_ids(task['rubric_required_ids'], 'rubric requirement IDs') == set(requirements),
                'rubric must match task requirements exactly; no added requirements')
        require(task['ambiguity_policy'] == 'clarify_or_state_assumption', 'explicit ambiguity policy required')
        require(type(task['word_limit']) is int and task['word_limit'] == 250,
                'word limit must be the predefined 250')
        require(task['word_count_method'] == 'unicode_whitespace_split_complete_answer',
                'word count must cover complete answer with Python whitespace split')
        require(task['stop_rule'] == 'one_bounded_answer', 'explicit stop rule required')
    judges = rows_by_id(design['judges'], ('id', 'ratings_path', 'lock_path', 'blind_to',
                                         'independent_before_comparison'), 'judge')
    require(len(judges) == 2, 'exactly two distinct planned judges required')
    paths = []
    for judge in judges.values():
        require(string_ids(judge['blind_to'], 'judge blind fields') ==
                {'condition', 'target', 'expected_features'}, 'judge must be blinded to condition and expectations')
        require(judge['independent_before_comparison'] is True, 'independent judging declaration required')
        for field in ('ratings_path', 'lock_path'):
            require(nonempty(judge[field]), 'judge rating and lock paths required')
            paths.append(judge[field])
    require(len(set(paths)) == 4, 'each judge must have a separate rating and lock path')
    keys(design['rating_policy'], ('feature_values', 'comparison_gate'), 'rating policy')
    require(string_ids(design['rating_policy']['feature_values'], 'feature values') ==
            {'present', 'absent', 'unclear'}, 'feature values must include explicit unclear')
    require(design['rating_policy']['comparison_gate'] == 'both_judge_locks',
            'comparison must wait for both separate judge locks')
    keys(cards, ('schema_version', 'mappings'), 'cards')
    require(cards['schema_version'] == 'mapping-v2', 'unsupported cards schema')
    mappings = rows_by_id(cards['mappings'], ('mapping_id', 'aspect_id', 'test_id', 'task_id',
        'rubric_axis_id', 'dimension', 'common_requirements', 'rule_clauses', 'features',
        'anchors', 'nonclaims'), 'mapping', 'mapping_id')
    require(len(mappings) == 5 and {m['aspect_id'] for m in mappings.values()} == set(ASPECTS),
            'exactly five selected aspect mappings required')
    for field in ('test_id', 'task_id', 'rubric_axis_id'):
        require(all(nonempty(m[field]) for m in mappings.values()) and
                len({m[field] for m in mappings.values()}) == 5, f'{field} must be unique')
    for mapping in mappings.values():
        require(mapping['mapping_id'] == f"map.{CASE_TO_ASPECT[mapping['aspect_id']].split('.')[1]}.v2",
                'mapping ID/version must match its case aspect exactly')
        require(nonempty(mapping['dimension']), 'mapping dimension required')
        require(mapping['task_id'] in tasks, 'mapping references unknown task')
        task = tasks[mapping['task_id']]
        require(task['aspect_id'] == mapping['aspect_id'], 'mapping/task aspect mismatch')
        require(string_ids(mapping['common_requirements'], 'mapping common requirements') ==
                {r['id'] for r in task['requirements']}, 'mapping requirements must match task exactly')
        string_ids(mapping['nonclaims'], 'mapping nonclaims', 1)
        clauses = rows_by_id(mapping['rule_clauses'], ('id', 'text'), 'rule clause')
        require(clauses and all(nonempty(c['text']) for c in clauses.values()), 'rule clause text required')
        features = rows_by_id(mapping['features'], ('id', 'criterion', 'rule_clause_ids'), 'feature')
        require(features, 'observable features required')
        for feature in features.values():
            require(nonempty(feature['criterion']), 'feature criterion required')
            require(string_ids(feature['rule_clause_ids'], 'feature clause trace', 1) <= set(clauses),
                    'feature references undefined rule clause')
        keys(mapping['anchors'], ('low', 'middle', 'high'), 'anchors')
        for anchor in mapping['anchors'].values():
            keys(anchor, ('rule_clause_ids', 'expected_present', 'expected_absent'), 'anchor')
            clause_ids = string_ids(anchor['rule_clause_ids'], 'anchor rule clauses', 1)
            require(clause_ids <= set(clauses), 'anchor references undefined rule clause')
            present = string_ids(anchor['expected_present'], 'expected present features')
            absent = string_ids(anchor['expected_absent'], 'expected absent features')
            require(not absent, 'v2 defines no feature-absence bans; preserve allowed co-occurrence')
            require(present | absent and (present | absent) <= set(features) and not present & absent,
                    'anchor needs consistent defined feature predicates')
            for feature_id in present | absent:
                require(set(features[feature_id]['rule_clause_ids']) <= clause_ids,
                        'anchor rubric feature adds a requirement absent from its rule clauses')
    return tasks, mappings


def render_packet(task, mapping, condition):
    sections = [COMMON]
    if condition == 'neutral':
        sections.append('Do not use a persona packet or infer personality traits.')
    else:
        sections.append('Synthetic experimental persona packet; not an end-user-confirmed spec.')
        targets = {CASE_TO_ASPECT[a]: condition if a == mapping['aspect_id'] and condition != 'unspecified'
                   else 'unspecified' for a in ALL_ASPECTS}
        sections.append('Qualitative targets (not scores): ' + json.dumps(targets, sort_keys=True) +
                        '\nEvery unspecified aspect is explicitly unconstrained; never substitute middle.')
        if condition != 'unspecified':
            clauses = {c['id']: c['text'] for c in mapping['rule_clauses']}
            sections.append('\n'.join(clauses[c] for c in mapping['anchors'][condition]['rule_clause_ids']))
    sections.append('Task requirements:\n' + '\n'.join(r['text'] for r in task['requirements']))
    sections.append('If ambiguous, ask for clarification or state your assumption explicitly. '
                    'Count every word of the complete answer with Python len(answer.split()); no exemptions.')
    sections.append('Current task:\n' + task['prompt'])
    return '\n\n'.join(sections) + '\n'


def planned_runs(tasks, mappings):
    runs, packets = [], {}
    by_aspect = {m['aspect_id']: m for m in mappings.values()}
    for aspect in ASPECTS:
        mapping = by_aspect[aspect]
        for condition in CONDITIONS:
            for repeat in (1, 2):
                run_id = f'{aspect.lower()}-{condition}-{repeat}'
                path = f'{DESIGN_DIR}/packets/{run_id}.md'
                runs.append({'run_id': run_id, 'aspect_id': aspect, 'condition': condition,
                    'repeat': repeat, 'context_slot': f'planned-fresh-{run_id}', 'packet_path': path,
                    'targets': {CASE_TO_ASPECT[a]: condition if a == aspect and condition not in ('neutral', 'unspecified')
                                else 'unspecified' for a in ALL_ASPECTS},
                    'persona_packet': condition != 'neutral', 'actual_receipt': None})
                packets[path] = render_packet(tasks[mapping['task_id']], mapping, condition)
    return {'schema_version': 'diagnostic-v2-slots', 'runs': runs}, packets


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def protected_blobs(root):
    command = ['git', 'ls-tree', '-r', '-z', BASE_COMMIT, '--', *PROTECTED]
    result = subprocess.run(command, cwd=root, capture_output=True, check=True).stdout
    blobs = {}
    for record in result.split(b'\0'):
        if not record:
            continue
        metadata, name = record.split(b'\t', 1)
        mode, kind, blob = metadata.decode().split()
        require(kind == 'blob' and mode == '100644', 'unsupported protected baseline file mode')
        blobs[name.decode()] = blob
    require(blobs, 'protected baseline tree missing')
    return blobs


def verify_protected(root):
    blobs = protected_blobs(root)
    actual_files = set()
    for directory in PROTECTED:
        for path in (root / directory).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts:
                name = str(path.relative_to(root))
                if not name.startswith('persona-design-v0.2/mapping-v2/'):
                    actual_files.add(name)
    require(actual_files == set(blobs), 'protected v1 file set changed')
    for name, expected in blobs.items():
        path = local_path(root, name)
        require(path.is_file() and not path.is_symlink(), f'protected v1 file missing: {name}')
        content = path.read_bytes()
        actual = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
        require(actual == expected, f'protected v1 file changed: {name}')
    return blobs


def input_files(root):
    fixed = [CARDS, 'persona-design-v0.2/mapping-v2/cards.md', f'{DESIGN_DIR}/design.json',
             f'{DESIGN_DIR}/PLAN.md', 'persona-design-v0.2/mapping-v2/WORKFLOW.md',
             'persona-design-v0.2/mapping-v2/README.md',
             'persona-design-v0.2/mapping-v2/ACCEPTANCE_PROPOSAL.md', f'{DESIGN_DIR}/manifest.json',
             f'{DESIGN_DIR}/order.json', f'{DESIGN_DIR}/validate_design.py', f'{DESIGN_DIR}/test_design.py']
    packet_dir = local_path(root, f'{DESIGN_DIR}/packets')
    require(packet_dir.is_dir(), 'prepared packets directory missing')
    packet_files = sorted(str(p.relative_to(root)) for p in packet_dir.rglob('*') if p.is_file())
    return fixed + packet_files


def verify_hashes(root):
    frozen = read_json(root / DESIGN_DIR / 'frozen-hashes.json')
    keys(frozen, ('schema_version', 'base_commit', 'files', 'protected_v1_blobs'), 'frozen hashes')
    require(frozen['schema_version'] == 'diagnostic-v2-freeze' and frozen['base_commit'] == BASE_COMMIT,
            'unsupported freeze baseline')
    require(frozen['protected_v1_blobs'] == verify_protected(root), 'protected baseline snapshot changed')
    require(isinstance(frozen['files'], dict) and set(frozen['files']) == set(input_files(root)),
            'frozen input file set changed')
    for name, expected in frozen['files'].items():
        path = local_path(root, name)
        require(path.is_file() and not path.is_symlink() and digest(path) == expected,
                f'frozen input hash changed: {name}')


def verify(root, check_hashes=True):
    root = Path(root).resolve()
    if check_hashes:
        verify_hashes(root)
    else:
        verify_protected(root)
    directory = root / DESIGN_DIR
    design = read_json(directory / 'design.json')
    cards = read_json(root / CARDS)
    tasks, mappings = validate_inputs(design, cards)
    for judge in design['judges']:
        for field in ('ratings_path', 'lock_path'):
            path = local_path(directory, judge[field])
            require(not path.exists(), 'design-only package must not contain ratings or judge locks')
    manifest = read_json(directory / 'manifest.json')
    expected, packets = planned_runs(tasks, mappings)
    require(manifest == expected, 'planned slots changed: coverage, context, targets, packet, or receipt mismatch')
    order = read_json(directory / 'order.json')
    require(isinstance(order, list) and len(order) == 50 and all(nonempty(x) for x in order) and
            len(set(order)) == 50 and set(order) == {r['run_id'] for r in manifest['runs']},
            'execution order must cover all 50 unique slots')
    require(order == planned_order(manifest), 'prospective order differs from fixed hash-sort algorithm')
    actual_packet_paths = {str(p.relative_to(root)) for p in (directory / 'packets').rglob('*') if p.is_file()}
    require(actual_packet_paths == set(packets), 'packet file set must contain exactly 50 planned packets')
    for name, content in packets.items():
        path = local_path(root, name)
        require(not path.is_symlink() and path.read_text(encoding='utf-8') == content,
                f'packet differs from exact task and referenced rule clauses: {name}')
    for name in ('raw', 'outputs', 'ratings', 'blind', 'analysis'):
        path = directory / name
        require(not path.exists() or (path.is_dir() and not any(path.iterdir())),
                f'design-only package contains generated evidence: {name}')
    if check_hashes:
        verify_hashes(root)
    else:
        verify_protected(root)
    return {'planned_slots': 50, 'planned_fresh_context_slots': 50,
            'generated_outputs': 0, 'planned_independent_judges': 2,
            'human_confirmation': 'not_obtained', 'semantic_validation': False}


def planned_order(manifest):
    return sorted((r['run_id'] for r in manifest['runs']),
                  key=lambda run_id: hashlib.sha256((ORDER_SEED + '\n' + run_id).encode('utf-8')).hexdigest())


def prepare(root):
    root = Path(root).resolve()
    directory = root / DESIGN_DIR
    generated = [directory / name for name in ('manifest.json', 'order.json', 'packets', 'frozen-hashes.json')]
    require(not any(p.exists() for p in generated), 'refusing overwrite of prepared design')
    tasks, mappings = validate_inputs(read_json(directory / 'design.json'), read_json(root / CARDS))
    verify_protected(root)
    manifest, packets = planned_runs(tasks, mappings)
    (directory / 'packets').mkdir()
    for name, content in packets.items():
        local_path(root, name).write_text(content, encoding='utf-8')
    write_json(directory / 'manifest.json', manifest)
    # Prospective hash-sort; actual dispatch and completion order remain unobserved.
    order = planned_order(manifest)
    write_json(directory / 'order.json', order)
    verify(root, check_hashes=False)
    frozen = {'schema_version': 'diagnostic-v2-freeze', 'base_commit': BASE_COMMIT,
              'files': {name: digest(local_path(root, name)) for name in input_files(root)},
              'protected_v1_blobs': verify_protected(root)}
    with (directory / 'frozen-hashes.json').open('x', encoding='utf-8') as handle:
        handle.write(json.dumps(frozen, ensure_ascii=False, indent=2) + '\n')
    return verify(root)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('prepare', 'verify'))
    parser.add_argument('--repo-root', default=str(Path(__file__).resolve().parents[2]))
    args = parser.parse_args(argv)
    try:
        result = prepare(args.repo_root) if args.command == 'prepare' else verify(args.repo_root)
        print('PASS structural design only: ' + json.dumps(result, sort_keys=True))
        print('Planned slots do not prove actual fresh contexts, judge independence, human confirmation, '
              'semantic alignment, or behavioral validity.')
    except (ValueError, OSError, TypeError, KeyError, subprocess.CalledProcessError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
