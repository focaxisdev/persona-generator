"""Host-neutral strict profile compiler and immutable local store.

Only parsing/hashing primitives are shared with core; its validator/catalog are not used.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from core.compiler import (CoreError, load_document, canonical_bytes, digest,
                           obj, require, string, strings, array, ASPECTS,
                           TRUSTED_DEPENDENCIES)

ProfileError = CoreError
SCHEMA_VERSION = 'persona-profile-v1'
CATALOG_PATH = 'profiles/catalog-v1.json'
TRUSTED_CATALOG_SHA256 = '52d66e3265567b615cb7230390b5befa8de29e969c4913a6f97fc7230ed67cb5'
ORIGINS = ('owner', 'synthetic_fixture')


def _root(repo_root=None):
    return Path(repo_root) if repo_root is not None else Path(__file__).resolve().parent.parent


def _read(path):
    try:
        return Path(path).read_bytes()
    except OSError as error:
        raise ProfileError('missing or unreadable artifact: ' + str(error)) from error


def load_catalog(repo_root=None):
    root = _root(repo_root)
    raw = _read(root / CATALOG_PATH)
    require(hashlib.sha256(raw).hexdigest() == TRUSTED_CATALOG_SHA256, 'profile catalog differs from trust pin')
    catalog = load_document(raw)
    require(catalog['id'] == 'persona-profile-catalog-v1' and catalog['schema_version'] == SCHEMA_VERSION, 'wrong profile catalog version')
    expected = [{'path': p, 'sha256': h} for p, h in TRUSTED_DEPENDENCIES]
    require(catalog['dependencies'] == expected, 'catalog source declarations differ from pins')
    for path, sha in TRUSTED_DEPENDENCIES:
        require(hashlib.sha256(_read(root / path)).hexdigest() == sha, 'source bytes differ from trust pin: ' + path)
    return catalog


def _id(value, label):
    string(value, label)
    require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,79}', value) is not None, 'invalid ' + label)


def _revision(value):
    string(value, 'revision')
    require(re.fullmatch(r'r[1-9][0-9]*', value) is not None, 'revision must be r followed by positive integer')


def _sha(value, label):
    require(type(value) is str and re.fullmatch('[0-9a-f]{64}', value) is not None, 'invalid ' + label)


def _index(records, keys, label):
    array(records, label)
    result = {}
    for record in records:
        obj(record, keys, label)
        _id(record['id'], label + '.id')
        require(record['id'] not in result, 'duplicate ' + label + ' id')
        result[record['id']] = record
    return result


def candidate(mapping):
    return {key: mapping[key] for key in ('id', 'aspect', 'anchor', 'trigger', 'rule', 'boundary')}


def detect_constraints(constraints):
    """Detect only declared exact-context/action require/forbid pairs, never prose meaning."""
    array(constraints, 'constraints')
    seen = {}
    for constraint in constraints:
        obj(constraint, 'context action effect', 'constraint')
        string(constraint['context'], 'constraint.context')
        string(constraint['action'], 'constraint.action')
        require(type(constraint['effect']) is str and constraint['effect'] in ('require', 'forbid'), 'unknown constraint effect')
        key = (constraint['context'], constraint['action'])
        require(key not in seen or seen[key] == constraint['effect'], 'mutually exclusive catalog constraints in same context')
        seen[key] = constraint['effect']


def validate_preview(preview, repo_root=None, allow_unresolved=False):
    canonical_bytes(preview)
    obj(preview, 'schema_version kind profile_id revision catalog sources targets mappings answers approvals conflicts blocking_issues unknowns history evidence', 'profile preview')
    require(preview['schema_version'] == SCHEMA_VERSION and preview['kind'] == 'preview', 'unsupported profile schema/kind')
    _id(preview['profile_id'], 'profile_id'); _revision(preview['revision'])
    catalog = load_catalog(repo_root)
    obj(preview['catalog'], 'id sha256', 'catalog reference')
    require(preview['catalog'] == {'id': catalog['id'], 'sha256': TRUSTED_CATALOG_SHA256}, 'stale catalog reference')
    require(type(preview['sources']) is list and preview['sources'] == catalog['dependencies'], 'source versions/hashes do not match pinned catalog')
    obj(preview['evidence'], 'status behavioral_validation', 'evidence')
    require(preview['evidence']['status'] == 'untested' and preview['evidence']['behavioral_validation'] is False, 'profile hypotheses remain untested')
    obj(preview['targets'], ' '.join(ASPECTS), 'targets')
    for anchor in preview['targets'].values():
        require(type(anchor) is str and anchor in ('low', 'middle', 'high', 'unspecified'), 'invalid target anchor')
    answers = _index(preview['answers'], 'id origin kind text record_ref', 'answer')
    for answer in answers.values():
        require(type(answer['origin']) is str and answer['origin'] in ORIGINS, 'invalid answer origin')
        require(type(answer['kind']) is str and answer['kind'] in ('choice', 'short-answer'), 'invalid answer kind')
        string(answer['text'], 'answer.text'); string(answer['record_ref'], 'answer.record_ref')
    approvals = _index(preview['approvals'], 'id answer_id aspect anchor candidate_sha256', 'approval')
    for approval in approvals.values():
        require(type(approval['answer_id']) is str and approval['answer_id'] in answers, 'unknown approval answer')
        require(type(approval['aspect']) is str and approval['aspect'] in ASPECTS, 'invalid approval aspect')
        require(type(approval['anchor']) is str and approval['anchor'] in ('low', 'middle', 'high'), 'invalid approval anchor')
        _sha(approval['candidate_sha256'], 'candidate digest')
    mappings = _index(preview['mappings'], 'id aspect anchor trigger rule boundary answer_ids approval_id', 'mapping')
    active = {}; constraints = []; used_approvals = set()
    for mapping in mappings.values():
        for key in ('aspect', 'anchor', 'trigger', 'rule', 'boundary', 'approval_id'):
            string(mapping[key], 'mapping.' + key)
        require(mapping['id'] in catalog['hypotheses'], 'unknown hypothesis')
        hypothesis = catalog['hypotheses'][mapping['id']]
        aspect = mapping['aspect']; anchor = mapping['anchor']
        require(aspect == hypothesis['aspect'] and anchor in ('low', 'middle', 'high'), 'hypothesis aspect/anchor mismatch')
        require(aspect not in active and preview['targets'][aspect] == anchor, 'duplicate or target-mismatched mapping')
        exact = hypothesis['anchors'][anchor]
        require(all(mapping[k] == exact[k] for k in ('trigger', 'rule', 'boundary')), 'custom/stale mapping text')
        strings(mapping['answer_ids'], 'mapping.answer_ids')
        require(all(a in answers for a in mapping['answer_ids']), 'unknown mapping answer')
        require(mapping['approval_id'] in approvals, 'missing candidate approval')
        approval = approvals[mapping['approval_id']]
        require(approval['aspect'] == aspect and approval['anchor'] == anchor and approval['candidate_sha256'] == digest(candidate(mapping)) and approval['answer_id'] in mapping['answer_ids'], 'approval does not bind exact candidate/provenance')
        active[aspect] = mapping
        used_approvals.add(mapping['approval_id'])
        constraints.extend(exact.get('constraints', []))
    require(set(active) == {a for a, v in preview['targets'].items() if v != 'unspecified'}, 'active target lacks exact approved mapping')
    require(set(approvals) == used_approvals, 'unused approval')
    detect_constraints(constraints)
    conflicts = _index(preview['conflicts'], 'id aspect candidates status selected_candidate_id resolution_answer_id', 'conflict')
    conflict_aspects = set()
    for conflict in conflicts.values():
        aspect = conflict['aspect']
        require(type(aspect) is str and aspect in ASPECTS and aspect not in conflict_aspects, 'unknown/duplicate conflict aspect')
        conflict_aspects.add(aspect)
        require(type(conflict['status']) is str and conflict['status'] in ('unresolved', 'selected', 'withdrawn'), 'unknown conflict status')
        alternatives = _index(conflict['candidates'], 'id anchor trigger rule boundary answer_ids', 'conflict candidate')
        require(len(alternatives) >= 2, 'conflict needs competing candidates')
        anchors = set()
        for alternative in alternatives.values():
            anchor = alternative['anchor']
            require(type(anchor) is str and anchor in ('low', 'middle', 'high'), 'unknown conflict anchor')
            require(anchor not in anchors, 'duplicate alternative anchor')
            anchors.add(anchor)
            exact = catalog['hypotheses']['hyp.' + aspect.split('.')[1] + '.v1']['anchors'][anchor]
            require(all(alternative[k] == exact[k] for k in ('trigger', 'rule', 'boundary')), 'conflict candidate differs from catalog')
            strings(alternative['answer_ids'], 'conflict answer_ids')
            require(all(a in answers for a in alternative['answer_ids']), 'unknown conflict answer')
        if conflict['status'] == 'unresolved':
            require(conflict['selected_candidate_id'] is None and conflict['resolution_answer_id'] is None, 'unresolved conflict cannot claim a selection')
            require(allow_unresolved, 'explicit unresolved conflict blocks use')
        elif conflict['status'] == 'withdrawn':
            require(conflict['selected_candidate_id'] is None and preview['targets'][aspect] == 'unspecified', 'withdrawn conflict must leave target unspecified')
            require(type(conflict['resolution_answer_id']) is str and conflict['resolution_answer_id'] in answers, 'missing withdrawal answer')
        else:
            require(type(conflict['selected_candidate_id']) is str and conflict['selected_candidate_id'] in alternatives and aspect in active, 'missing selected active candidate')
            selected = alternatives[conflict['selected_candidate_id']]
            mapping = active[aspect]
            require(all(selected[k] == mapping[k] for k in ('anchor', 'trigger', 'rule', 'boundary', 'answer_ids')), 'selected conflict differs from active mapping')
            require(type(conflict['resolution_answer_id']) is str and conflict['resolution_answer_id'] in answers and approvals[mapping['approval_id']]['answer_id'] == conflict['resolution_answer_id'], 'resolution answer does not approve selected mapping')
    issues = _index(preview['blocking_issues'], 'id description answer_ids status resolution_answer_id resolution', 'blocking issue')
    for issue in issues.values():
        string(issue['description'], 'blocking issue.description')
        strings(issue['answer_ids'], 'blocking issue.answer_ids')
        require(bool(issue['answer_ids']) and all(a in answers for a in issue['answer_ids']), 'blocking issue needs recorded answer provenance')
        require(type(issue['status']) is str and issue['status'] in ('unresolved', 'resolved'), 'unknown blocking issue status')
        if issue['status'] == 'unresolved':
            require(issue['resolution_answer_id'] is None and issue['resolution'] is None, 'unresolved issue cannot claim resolution')
            require(allow_unresolved, 'explicit unresolved blocking issue prevents use')
        else:
            require(type(issue['resolution_answer_id']) is str and issue['resolution_answer_id'] in answers, 'blocking issue resolution needs recorded answer')
            string(issue['resolution'], 'blocking issue.resolution')
    strings(preview['unknowns'], 'unknowns'); strings(preview['history'], 'history')
    return catalog


def _render(preview, catalog):
    lines = [catalog['preamble']]
    for mapping in sorted(preview['mappings'], key=lambda m: m['id']):
        lines.append('When: ' + mapping['trigger'] + '\nPreference: ' + mapping['rule'] + '\nBoundary: ' + mapping['boundary'])
    return '\n\n'.join(lines) + '\n'


def preview_receipt(presented_bytes, repo_root=None, allow_unresolved=False):
    """Return draft review digests, never approval, confirmation or active instructions."""
    require(type(presented_bytes) is bytes, 'preview receipt requires exact presented bytes')
    preview = load_document(presented_bytes)
    catalog = validate_preview(preview, repo_root, allow_unresolved=allow_unresolved)
    blocked = any(item['status'] == 'unresolved' for item in preview['conflicts'] + preview['blocking_issues'])
    return {'profile_id': preview['profile_id'], 'revision': preview['revision'],
            'catalog_sha256': preview['catalog']['sha256'],
            'snapshot_sha256': digest(preview),
            'presented_file_sha256': hashlib.sha256(presented_bytes).hexdigest(),
            'effective_sha256': None if blocked else hashlib.sha256(_render(preview, catalog).encode('utf-8')).hexdigest(),
            'validation_status': 'structural_only', 'confirmation_status': 'NOT_CONFIRMED',
            'blocked_by_unresolved': blocked}


def validate_spec(spec, presented_bytes, repo_root=None):
    canonical_bytes(spec)
    obj(spec, 'schema_version kind approved_preview confirmation review', 'profile spec')
    require(spec['schema_version'] == SCHEMA_VERSION and spec['kind'] == 'spec', 'unsupported profile spec')
    preview = spec['approved_preview']
    catalog = validate_preview(preview, repo_root)
    require(type(presented_bytes) is bytes, 'presented preview requires exact bytes')
    require(load_document(presented_bytes) == preview, 'presented preview differs from full approved snapshot')
    confirmation = spec['confirmation']
    obj(confirmation, 'status profile_id revision snapshot_sha256 presented_file_sha256 effective_sha256 record_ref confirmed_by origin', 'confirmation')
    require(confirmation['status'] == 'confirmed' and confirmation['profile_id'] == preview['profile_id'] and confirmation['revision'] == preview['revision'], 'confirmation identity/revision mismatch')
    effective = _render(preview, catalog)
    require(confirmation['snapshot_sha256'] == digest(preview), 'snapshot digest mismatch')
    require(confirmation['presented_file_sha256'] == hashlib.sha256(presented_bytes).hexdigest(), 'presented byte digest mismatch')
    require(confirmation['effective_sha256'] == hashlib.sha256(effective.encode('utf-8')).hexdigest(), 'effective digest mismatch')
    require(type(confirmation['origin']) is str and confirmation['origin'] in ORIGINS, 'invalid confirmation origin')
    require(confirmation['origin'] != 'owner' or all(a['origin'] == 'owner' for a in preview['answers']), 'synthetic answers cannot establish owner confirmation')
    string(confirmation['record_ref'], 'confirmation.record_ref'); string(confirmation['confirmed_by'], 'confirmed_by')
    obj(spec['review'], 'status record_ref', 'review')
    require(spec['review']['status'] == 'Pass', 'manual review must be Pass')
    string(spec['review']['record_ref'], 'review.record_ref')
    return effective


def validate(spec_path, presented_path, repo_root=None):
    spec = load_document(_read(spec_path)); presented = _read(presented_path)
    return spec, presented, validate_spec(spec, presented, repo_root)


def _pin(spec):
    preview = spec['approved_preview']; confirmation = spec['confirmation']
    return {k: preview[k] for k in ('profile_id', 'revision')} | {
        'snapshot_sha256': confirmation['snapshot_sha256'],
        'effective_sha256': confirmation['effective_sha256'],
        'catalog_sha256': preview['catalog']['sha256'], 'spec_sha256': digest(spec)}


def _safe(store, *parts):
    root = Path(store).absolute()
    target = root.joinpath(*parts)
    for item in (target, *target.parents):
        require(not item.is_symlink(), 'symlink store paths are rejected')
    return target


def _directory(store, profile_id, revision):
    _id(profile_id, 'profile_id'); _revision(revision)
    return _safe(store, 'versions', profile_id, revision)


def publish(spec_path, presented_path, store, repo_root=None):
    """Persist already confirmed artifacts. Never manufacture approval/confirmation."""
    spec, presented, effective = validate(spec_path, presented_path, repo_root)
    pin = _pin(spec); directory = _directory(store, pin['profile_id'], pin['revision'])
    require(not directory.exists(), 'immutable profile revision already exists')
    if directory.parent.exists():
        for existing in directory.parent.iterdir():
            require(not existing.is_symlink(), 'symlink store paths are rejected')
            require(re.fullmatch(r'r[1-9][0-9]*', existing.name) is not None, 'unknown stored revision entry')
            require(int(pin['revision'][1:]) > int(existing.name[1:]), 'new revision must advance monotonically')
    directory.parent.mkdir(parents=True, exist_ok=True)
    try:
        directory.mkdir()
        (directory / 'spec.json').write_bytes(_read(spec_path))
        (directory / 'presented.json').write_bytes(presented)
        (directory / 'manifest.json').write_bytes(canonical_bytes({**pin, 'spec_file_sha256': hashlib.sha256(_read(spec_path)).hexdigest(), 'presented_file_sha256': hashlib.sha256(presented).hexdigest()}))
    except OSError as error:
        raise ProfileError('could not publish immutable revision: ' + str(error)) from error
    return pin


def load_version(store, profile_id, revision, repo_root=None):
    directory = _directory(store, profile_id, revision)
    spec, presented, effective = validate(_safe(store, 'versions', profile_id, revision, 'spec.json'), _safe(store, 'versions', profile_id, revision, 'presented.json'), repo_root)
    pin = _pin(spec)
    require(pin['profile_id'] == profile_id and pin['revision'] == revision, 'stored identity/revision mismatch')
    require(load_document(_read(_safe(store, 'versions', profile_id, revision, 'manifest.json'))) == {**pin, 'spec_file_sha256': hashlib.sha256(_read(_safe(store, 'versions', profile_id, revision, 'spec.json'))).hexdigest(), 'presented_file_sha256': hashlib.sha256(_read(_safe(store, 'versions', profile_id, revision, 'presented.json'))).hexdigest()}, 'stored manifest differs from confirmed revision')
    return spec, effective


def bind(store, agent_id, profile_id, revision, snapshot_sha256, effective_sha256, repo_root=None):
    _id(agent_id, 'agent_id')
    spec, effective = load_version(store, profile_id, revision, repo_root)
    pin = _pin(spec)
    require(pin['snapshot_sha256'] == snapshot_sha256 and pin['effective_sha256'] == effective_sha256, 'binding supplied digests differ from exact revision')
    binding = {'schema_version': 'persona-profile-binding-v1', 'agent_id': agent_id, **pin}
    folder = _safe(store, 'bindings'); folder.mkdir(parents=True, exist_ok=True)
    path = _safe(store, 'bindings', agent_id + '.json'); temporary = _safe(store, 'bindings', agent_id + '.tmp')
    temporary.write_bytes(canonical_bytes(binding)); temporary.replace(path)
    return binding


def load_binding(store, agent_id, repo_root=None):
    _id(agent_id, 'agent_id')
    binding = load_document(_read(_safe(store, 'bindings', agent_id + '.json')))
    obj(binding, 'schema_version agent_id profile_id revision snapshot_sha256 effective_sha256 catalog_sha256 spec_sha256', 'binding')
    require(binding['schema_version'] == 'persona-profile-binding-v1' and binding['agent_id'] == agent_id, 'binding agent identity mismatch')
    spec, effective = load_version(store, binding['profile_id'], binding['revision'], repo_root)
    require({k: binding[k] for k in _pin(spec)} == _pin(spec), 'binding is stale or tampered')
    return binding, effective


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    p = subs.add_parser('validate-preview'); p.add_argument('preview'); p.add_argument('--inspect-unresolved', action='store_true')
    for command in ('validate', 'publish'):
        p = subs.add_parser(command); p.add_argument('spec'); p.add_argument('--presented', required=True)
        if command == 'publish': p.add_argument('--store', required=True)
    p = subs.add_parser('bind')
    for name in ('store', 'agent', 'profile', 'revision', 'snapshot', 'effective'):
        p.add_argument('--' + name, required=True)
    for command in ('load', 'render'):
        p = subs.add_parser(command); p.add_argument('--store', required=True); p.add_argument('--agent', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate-preview':
            result = preview_receipt(_read(args.preview), allow_unresolved=args.inspect_unresolved)
        elif args.command == 'validate':
            spec, _, _ = validate(args.spec, args.presented); result = {**_pin(spec), 'validation_status': 'structural_only'}
        elif args.command == 'publish':
            result = publish(args.spec, args.presented, args.store)
        elif args.command == 'bind':
            result = bind(args.store, args.agent, args.profile, args.revision, args.snapshot, args.effective)
        else:
            binding, effective = load_binding(args.store, args.agent)
            if args.command == 'render':
                sys.stdout.write(effective); return 0
            result = {**binding, 'validation_status': 'structural_only'}
        print(json.dumps(result, ensure_ascii=False, sort_keys=True)); return 0
    except (ProfileError, OSError) as error:
        print('REJECTED: ' + str(error), file=sys.stderr); return 2
