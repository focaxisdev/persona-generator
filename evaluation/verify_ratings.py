#!/usr/bin/env python3
"""Structural lint and append-only integrity lock for blinded pilot ratings.

This checks syntax, coverage, enums and literal quotes, never rating semantics.
Judges may repair their own ratings before locking, retaining earlier attempts
outside ratings/*.json. No rating is corrected or written by this program.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

EXPECTED_ITEMS = 102
LOCK_NAME = 'ratings-lock.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    require(path.is_file() and not path.is_symlink(), f'Expected regular file: {path}')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def read_json(path):
    digest(path)
    def invalid(value):
        raise ValueError(f'Nonstandard JSON constant: {value}')
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_object,
                      parse_constant=invalid)


def fields(value, names, context):
    require(isinstance(value, dict) and set(value) == set(names),
            f'{context}: expected exactly fields {", ".join(names)}')


def nonempty(value, context):
    require(isinstance(value, str) and bool(value.strip()), f'{context}: nonempty string required')


def quotes(value, response, context):
    require(isinstance(value, list), f'{context}: quotes must be a list')
    for quote in value:
        nonempty(quote, context + ' quote')
        require(quote in response, f'{context}: quote is not an exact current response substring')


def file_hashes(directory):
    require(directory.is_dir() and not directory.is_symlink(), f'Missing or symbolic directory: {directory}')
    return {p.name: digest(p) for p in sorted(directory.glob('*.json'))}


def inspect(root):
    rubric_path = root / 'frozen/rubric.json'
    rubric = read_json(rubric_path)
    frozen = read_json(root / 'frozen-hashes.json')
    require(isinstance(frozen, dict) and isinstance(frozen.get('files'), dict), 'Malformed frozen hashes')
    require(frozen['files'].get('frozen/rubric.json') == digest(rubric_path), 'Frozen rubric hash changed')
    require(isinstance(rubric, dict), 'Malformed rubric')
    require(isinstance(rubric.get('axes'), list) and isinstance(rubric.get('guardrails'), list), 'Malformed rubric lists')
    common = rubric.get('common_axis_categories')
    require(isinstance(common, dict) and all(isinstance(k, str) for k in common), 'Malformed common categories')
    axis_categories = {}
    for axis in rubric['axes']:
        require(isinstance(axis, dict) and isinstance(axis.get('id'), str)
                and isinstance(axis.get('categories'), dict), 'Malformed rubric axis')
        require(axis['id'] not in axis_categories, 'Duplicate rubric axis')
        axis_categories[axis['id']] = set(axis['categories']) | set(common)
    require(set(axis_categories) == {f'A{i:02}' for i in range(1, 11)}, 'Expected rubric A01..A10')
    guard_ids = []
    for guard in rubric['guardrails']:
        require(isinstance(guard, dict) and isinstance(guard.get('id'), str), 'Malformed rubric guardrail')
        guard_ids.append(guard['id'])
    require(len(guard_ids) == 9 and set(guard_ids) == {f'G{i:02}' for i in range(1, 10)}, 'Expected rubric G01..G09')
    blind_hashes = file_hashes(root / 'blind')
    require(blind_hashes == read_json(root / 'blind-hashes.json'), 'Blind file/hash set changed')
    require(len(blind_hashes) == EXPECTED_ITEMS, f'Expected exactly {EXPECTED_ITEMS} blind packets')
    responses = {}
    for name in blind_hashes:
        packet = read_json(root / 'blind' / name)
        fields(packet, ['item_id', 'conversation'], name)
        item_id = packet['item_id']
        nonempty(item_id, name + ' item_id')
        require(name == item_id + '.json', 'Blind filename does not match item_id')
        require(item_id not in responses, 'Duplicate blind item_id')
        history = packet['conversation']
        require(isinstance(history, list) and bool(history), name + ': nonempty conversation required')
        for turn in history:
            fields(turn, ['task', 'response'], name + ' turn')
            nonempty(turn['task'], name + ' task')
            nonempty(turn['response'], name + ' response')
        responses[item_id] = history[-1]['response']
    rating_hashes = file_hashes(root / 'ratings')
    require(bool(rating_hashes), 'No ratings/*.json files')
    seen = set()
    for name in rating_hashes:
        batch = read_json(root / 'ratings' / name)
        require(isinstance(batch, list) and bool(batch), name + ': nonempty rating array required')
        for entry in batch:
            fields(entry, ['blind_id', 'axes', 'guardrails', 'blind_leakage', 'limitations'], name + ' rating')
            item_id = entry['blind_id']
            nonempty(item_id, name + ' blind_id')
            require(item_id in responses, name + ': unknown blind_id')
            require(item_id not in seen, name + ': duplicate blind_id')
            seen.add(item_id)
            response = responses[item_id]
            axes = entry['axes']
            require(isinstance(axes, list), item_id + ': axes must be a list')
            axis_seen = set()
            for axis in axes:
                fields(axis, ['axis_id', 'category', 'quotes', 'reason', 'confidence'], item_id + ' axis')
                aid = axis['axis_id']
                require(isinstance(aid, str) and aid in axis_categories and aid not in axis_seen, item_id + ': unknown or duplicate axis')
                axis_seen.add(aid)
                require(isinstance(axis['category'], str) and axis['category'] in axis_categories[aid], item_id + ': invalid axis category')
                require(isinstance(axis['confidence'], str) and axis['confidence'] in ('clear', 'limited'), item_id + ': invalid confidence')
                nonempty(axis['reason'], item_id + ' axis reason')
                quotes(axis['quotes'], response, item_id + ' ' + aid)
                if axis['category'] not in common:
                    require(bool(axis['quotes']), item_id + ' ' + aid + ': declared axis category requires supporting quotes')
            require(axis_seen == set(axis_categories), item_id + ': incomplete axis coverage')
            guards = entry['guardrails']
            require(isinstance(guards, list), item_id + ': guardrails must be a list')
            guard_seen = set()
            for guard in guards:
                fields(guard, ['guardrail_id', 'rating', 'quotes', 'reason'], item_id + ' guardrail')
                gid = guard['guardrail_id']
                require(isinstance(gid, str) and gid in guard_ids and gid not in guard_seen, item_id + ': unknown or duplicate guardrail')
                guard_seen.add(gid)
                require(isinstance(guard['rating'], str) and guard['rating'] in ('pass', 'violation', 'unclear'), item_id + ': invalid guardrail rating')
                nonempty(guard['reason'], item_id + ' guardrail reason')
                quotes(guard['quotes'], response, item_id + ' ' + gid)
            require(guard_seen == set(guard_ids), item_id + ': incomplete guardrail coverage')
            leak = entry['blind_leakage']
            fields(leak, ['present', 'quotes', 'reason'], item_id + ' blind_leakage')
            require(type(leak['present']) is bool, item_id + ': leakage present must be boolean')
            quotes(leak['quotes'], response, item_id + ' leakage')
            nonempty(leak['reason'], item_id + ' leakage reason')
            require(isinstance(entry['limitations'], list), item_id + ': limitations must be a list')
            for limit in entry['limitations']:
                nonempty(limit, item_id + ' limitation')
    require(seen == set(responses), f'Incomplete rating coverage: {len(seen)}/{len(responses)}')
    return {'schema_version': 'pilot-ratings-lock-v1', 'item_count': len(seen),
            'rubric_sha256': digest(rubric_path), 'blind_hashes': blind_hashes,
            'rating_hashes': rating_hashes}


def verify(root):
    state = inspect(root)
    path = root / LOCK_NAME
    if path.exists():
        locked = read_json(path)
        fields(locked, [*state, 'locked_at'], 'ratings lock')
        nonempty(locked['locked_at'], 'lock timestamp')
        try:
            stamp = datetime.fromisoformat(locked['locked_at'])
        except ValueError as exc:
            raise ValueError('Invalid lock timestamp') from exc
        require(stamp.tzinfo is not None and stamp.utcoffset().total_seconds() == 0, 'Lock timestamp must be UTC')
        require({k: locked[k] for k in state} == state, 'Locked ratings or blind inputs changed')
    return state


def lock(root):
    path = root / LOCK_NAME
    require(not path.exists() and not path.is_symlink(), 'Ratings lock already exists; refusing overwrite')
    state = verify(root)
    state['locked_at'] = datetime.now(timezone.utc).isoformat()
    with path.open('x', encoding='utf-8') as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2)
        handle.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['verify', 'lock'])
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    try:
        (verify if args.command == 'verify' else lock)(args.root.resolve())
    except (ValueError, OSError, TypeError, KeyError, RecursionError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(args.command + ': OK (structural integrity only)')


if __name__ == '__main__':
    main()
