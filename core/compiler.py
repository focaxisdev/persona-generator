"""Strict, local, deterministic compiler for the unreleased persona core candidate."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

SCHEMA_VERSION = 'persona-core-v1'
CATALOG_RELATIVE_PATH = 'core/catalog-v1.json'
TRUSTED_CATALOG_SHA256 = '8c616013d572fc6568fe76698f03c5cc41d8aeb130da84a4580090a48d873fc7'
TRUSTED_DEPENDENCIES = (
    ('persona-design-v0.2/construct-registry.md', '47cc2da25549b6cc2e9e49230342f5337f1c79ea01b18b35b85d167cd83976bf'),
    ('persona-design-v0.2/sources.md', '287a435ef7a29778ec91cbc9b680e66128632741356b5e202a7f359294314bd2'),
)
ASPECTS = tuple('bfas.' + x for x in ('volatility', 'withdrawal', 'compassion', 'politeness', 'industriousness', 'orderliness', 'enthusiasm', 'assertiveness', 'intellect', 'openness'))
ANCHORS = ('low', 'middle', 'high')
ORIGINS = ('owner', 'synthetic_fixture')

class CoreError(ValueError):
    """An input failed closed before projection."""

def require(condition, message):
    if not condition:
        raise CoreError(message)

def obj(value, keys, label):
    require(type(value) is dict, label + ' must be an object')
    require(set(value) == set(keys.split()), label + ' has missing or extra fields')

def string(value, label, nonempty=True):
    require(type(value) is str and (bool(value.strip()) or not nonempty), label + ' must be a string' + (' with content' if nonempty else ''))

def array(value, label):
    require(type(value) is list, label + ' must be an array')

def strings(value, label):
    array(value, label)
    for item in value:
        string(item, label)
    require(len(value) == len(set(value)), label + ' contains duplicates')

def canonical_bytes(value):
    try:
        return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')
    except (ValueError, TypeError, UnicodeError, RecursionError) as error:
        raise CoreError('not canonical JSON: ' + str(error)) from error

def digest(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()

def _pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result

def load_document(data):
    """Load a JSON object or exactly one whole-document ```json fence."""
    try:
        if type(data) is bytes:
            data = data.decode('utf-8')
        require(type(data) is str, 'document must be UTF-8 bytes or text')
        if data.lstrip().startswith('```'):
            match = re.fullmatch(r'\s*```json[ \t]*\r?\n([\s\S]*?)\r?\n```\s*', data)
            require(match is not None, 'expected exactly one JSON Markdown fence')
            data = match.group(1)
        result = json.loads(data, object_pairs_hook=_pairs,
                            parse_constant=lambda value: (_ for _ in ()).throw(CoreError('nonfinite JSON number: ' + value)))
        require(type(result) is dict, 'document root must be an object')
        canonical_bytes(result)  # Also rejects overflowing floats and invalid Unicode.
        return result
    except CoreError:
        raise
    except (UnicodeError, ValueError, RecursionError) as error:
        raise CoreError('invalid JSON document: ' + str(error)) from error

def route_document(document):
    """Identify a version route without validating, migrating, or activating it."""
    require(type(document) is dict, 'version routing requires an object')
    outer = document.get('schema_version')
    inner = document.get('approved_preview')
    if inner is not None:
        require(type(inner) is dict, 'approved_preview must be an object')
        nested = inner.get('schema_version')
        require(type(nested) is str, 'missing inner schema version')
        require(outer is None or outer == nested, 'mixed outer/inner schema versions')
        version = nested
    else:
        version = outer
    require(type(version) is str, 'missing schema version')
    if version == SCHEMA_VERSION:
        require(outer == SCHEMA_VERSION, 'core requires an explicit outer schema version')
        require(document.get('kind') == ('spec' if inner is not None else 'preview'), 'inconsistent core kind')
        return 'core-spec' if inner is not None else 'core-preview'
    if version == 'persona-design-v0.2':
        return 'legacy-validation-only'
    if version in ('persona-design-v0.2-mapping-v2', 'mapping-v2'):
        return 'mapping-v2-proposal-only'
    raise CoreError('unknown schema version; no automatic migration')

def _root(repo_root):
    return Path(repo_root) if repo_root is not None else Path(__file__).resolve().parent.parent

def load_catalog(repo_root=None):
    root = _root(repo_root)
    try:
        raw = (root / CATALOG_RELATIVE_PATH).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == TRUSTED_CATALOG_SHA256, 'catalog bytes differ from compiler trust pin')
        catalog = load_document(raw)
        expected = [{'path': p, 'sha256': h} for p, h in TRUSTED_DEPENDENCIES]
        require(catalog['dependencies'] == expected, 'catalog dependency declarations differ from trusted paths/hashes')
        for path, sha in TRUSTED_DEPENDENCIES:
            require(hashlib.sha256((root / path).read_bytes()).hexdigest() == sha, 'dependency bytes differ from trust pin: ' + path)
        return catalog
    except OSError as error:
        raise CoreError('missing or unreadable pinned dependency: ' + str(error)) from error

def _index(records, keys, label):
    array(records, label)
    result = {}
    for record in records:
        obj(record, keys, label)
        string(record['id'], label + '.id')
        require(record['id'] not in result, 'duplicate ' + label + ' id')
        result[record['id']] = record
    return result

def validate_preview(preview, repo_root=None):
    """Validate structural approvals only; this does not authenticate any human."""
    canonical_bytes(preview)
    require(route_document(preview) == 'core-preview', 'non-core route cannot be compiled')
    obj(preview, 'schema_version kind revision catalog scope answers targets mappings approvals controls conflicts unknowns sources history evidence', 'preview')
    require(preview['schema_version'] == SCHEMA_VERSION and preview['kind'] == 'preview', 'unsupported schema/kind; legacy specs are validation-only and cannot be projected')
    string(preview['revision'], 'revision')
    require(re.fullmatch(r'r[1-9][0-9]*', preview['revision']) is not None, 'revision must be r followed by a positive integer')
    catalog = load_catalog(repo_root)
    obj(preview['catalog'], 'id sha256', 'catalog')
    require(preview['catalog'] == {'id': catalog['id'], 'sha256': TRUSTED_CATALOG_SHA256}, 'unknown catalog identity/hash')
    obj(preview['scope'], 'fictional low_stakes ephemeral', 'scope')
    require(all(type(v) is bool and v for v in preview['scope'].values()), 'scope must remain fictional, low-stakes, ephemeral')
    obj(preview['evidence'], 'status behavioral_validation', 'evidence')
    require(preview['evidence']['status'] == 'untested' and preview['evidence']['behavioral_validation'] is False, 'core operation evidence must remain untested')
    answers = _index(preview['answers'], 'id origin kind text record_ref', 'answer')
    for answer in answers.values():
        require(answer['origin'] in ORIGINS, 'unknown answer origin')
        require(answer['kind'] in ('choice', 'short-answer'), 'unknown answer kind')
        string(answer['text'], 'answer.text'); string(answer['record_ref'], 'answer.record_ref')
    approvals = _index(preview['approvals'], 'id answer_id kind setting target candidate_sha256', 'approval')
    for approval in approvals.values():
        for key in ('answer_id', 'kind', 'setting', 'target', 'candidate_sha256'):
            string(approval[key], 'approval.' + key)
        require(approval['answer_id'] in answers, 'approval references unknown answer')
        require(approval['kind'] in ('mapping', 'control'), 'unknown approval kind')
        require(re.fullmatch('[0-9a-f]{64}', approval['candidate_sha256']) is not None, 'invalid approval digest')
    def answer_ids(ids):
        strings(ids, 'answer_ids')
        require(all(a in answers for a in ids), 'unknown answer reference')
    def approved(approval_id, kind, setting, target, candidate, ids):
        string(approval_id, 'approval_id')
        require(approval_id in approvals, 'missing structural approval')
        approval = approvals[approval_id]
        require(approval['kind'] == kind and approval['setting'] == setting and approval['target'] == target and approval['candidate_sha256'] == digest(candidate), 'approval does not bind this exact candidate')
        require(approval['answer_id'] in ids, 'approval answer not in exact answer provenance')
    obj(preview['targets'], ' '.join(ASPECTS), 'targets')
    for aspect, anchor in preview['targets'].items():
        require(type(anchor) is str and anchor in ('unspecified',) + ANCHORS, 'invalid target anchor')
        require(aspect in ('bfas.orderliness', 'bfas.assertiveness') or anchor == 'unspecified', 'unsupported aspect must remain unspecified')
    mappings = _index(preview['mappings'], 'id aspect anchor trigger rule boundary answer_ids approval_id', 'mapping')
    mapped = {}
    for mapping in mappings.values():
        for key in ('aspect', 'anchor', 'trigger', 'rule', 'boundary'):
            string(mapping[key], 'mapping.' + key)
        require(mapping['id'] in catalog['operations'], 'unknown operation id')
        operation = catalog['operations'][mapping['id']]
        require(mapping['aspect'] == operation['aspect'] and mapping['anchor'] in ANCHORS, 'operation aspect/anchor mismatch')
        require(mapping['aspect'] not in mapped, 'duplicate active aspect')
        require({k: mapping[k] for k in ('trigger', 'rule', 'boundary')} == operation['anchors'][mapping['anchor']], 'custom or stale rule is not the exact catalog operation')
        require(preview['targets'][mapping['aspect']] == mapping['anchor'], 'mapping inconsistent with selected target')
        answer_ids(mapping['answer_ids'])
        approved(mapping['approval_id'], 'mapping', mapping['aspect'], mapping['anchor'], {k: mapping[k] for k in ('id', 'aspect', 'anchor', 'trigger', 'rule', 'boundary')}, mapping['answer_ids'])
        mapped[mapping['aspect']] = mapping
    require(set(mapped) == {a for a, v in preview['targets'].items() if v != 'unspecified'}, 'active target missing exact approved mapping')
    obj(preview['controls'], 'response_detail', 'controls')
    control = preview['controls']['response_detail']
    obj(control, 'value rule answer_ids approval_id', 'response_detail')
    require(type(control['value']) is str and control['value'] in ('unspecified', 'concise', 'standard', 'detailed'), 'unsupported response_detail')
    answer_ids(control['answer_ids'])
    if control['value'] == 'unspecified':
        require(control['rule'] is None and control['answer_ids'] == [] and control['approval_id'] is None, 'unspecified control cannot carry an active rule or approval')
    else:
        require(control['rule'] == catalog['response_detail'][control['value']], 'custom response_detail rule is not the exact catalog template')
        approved(control['approval_id'], 'control', 'response_detail', control['value'], {'name': 'response_detail', 'value': control['value'], 'rule': control['rule']}, control['answer_ids'])
    conflicts = _index(preview['conflicts'], 'id aspect candidates status selected_candidate_id resolution_answer_id', 'conflict')
    conflict_aspects = set()
    for conflict in conflicts.values():
        require(type(conflict['aspect']) is str and conflict['aspect'] in ASPECTS and conflict['aspect'] not in conflict_aspects, 'unknown/duplicate conflict aspect')
        conflict_aspects.add(conflict['aspect'])
        candidates = _index(conflict['candidates'], 'id anchor trigger rule boundary answer_ids', 'candidate')
        require(len(candidates) >= 2, 'conflict needs at least two candidates')
        for candidate in candidates.values():
            require(type(candidate['anchor']) is str and candidate['anchor'] in ANCHORS, 'invalid candidate anchor')
            for key in ('trigger', 'rule', 'boundary'):
                string(candidate[key], 'candidate.' + key)
            answer_ids(candidate['answer_ids'])
        require(type(conflict['status']) is str and conflict['status'] in ('selected', 'withdrawn'), 'unresolved conflict blocks compilation')
        require(type(conflict['resolution_answer_id']) is str and conflict['resolution_answer_id'] in answers, 'missing conflict resolution answer')
        if conflict['status'] == 'withdrawn':
            require(conflict['selected_candidate_id'] is None and preview['targets'][conflict['aspect']] == 'unspecified', 'withdrawn conflict must leave target unspecified')
        else:
            require(type(conflict['selected_candidate_id']) is str and conflict['selected_candidate_id'] in candidates, 'unknown selected candidate')
            require(conflict['aspect'] in mapped, 'selected conflict has no active mapping')
            selected = candidates[conflict['selected_candidate_id']]; active = mapped[conflict['aspect']]
            require(all(selected[k] == active[k] for k in ('anchor', 'trigger', 'rule', 'boundary', 'answer_ids')), 'resolved candidate inconsistent with active mapping')
            require(approvals[active['approval_id']]['answer_id'] == conflict['resolution_answer_id'], 'selected candidate not bound to resolution approval')
    strings(preview['unknowns'], 'unknowns')
    strings(preview['history'], 'history')
    sources = _index(preview['sources'], 'id path sha256', 'source')
    for source in sources.values():
        string(source['path'], 'source.path')
        string(source['sha256'], 'source.sha256')
    require(len(sources) == len(TRUSTED_DEPENDENCIES), 'source dependency count mismatch')
    require(sorted((s['path'], s['sha256']) for s in sources.values()) == sorted(TRUSTED_DEPENDENCIES), 'unknown/missing/mutated source dependency')
    return preview

def validate_spec(spec, presented_preview, presented_file_bytes, repo_root=None):
    canonical_bytes(spec)
    require(route_document(spec) == 'core-spec', 'non-core route cannot be compiled')
    obj(spec, 'schema_version kind approved_preview confirmation review', 'spec')
    require(spec['schema_version'] == SCHEMA_VERSION and spec['kind'] == 'spec', 'unsupported spec schema/kind; no automatic migration')
    validate_preview(spec['approved_preview'], repo_root)
    require(type(presented_file_bytes) is bytes, 'presented file bytes are required')
    actual = load_document(presented_file_bytes)
    require(canonical_bytes(actual) == canonical_bytes(presented_preview) == canonical_bytes(spec['approved_preview']), 'presented file/snapshot differs from approved preview')
    confirmation = spec['confirmation']
    obj(confirmation, 'status revision snapshot_sha256 presented_file_sha256 record_ref confirmed_by origin', 'confirmation')
    require(confirmation['status'] == 'confirmed', 'explicit confirmation is required')
    require(confirmation['revision'] == spec['approved_preview']['revision'], 'stale confirmation revision')
    require(confirmation['snapshot_sha256'] == digest(spec['approved_preview']), 'stale confirmation snapshot hash')
    require(confirmation['presented_file_sha256'] == hashlib.sha256(presented_file_bytes).hexdigest(), 'presented file byte hash mismatch')
    for key in ('record_ref', 'confirmed_by'):
        string(confirmation[key], 'confirmation.' + key)
    require(confirmation['origin'] in ORIGINS, 'unknown confirmation origin')
    require(confirmation['origin'] == 'synthetic_fixture' or all(a['origin'] == 'owner' for a in spec['approved_preview']['answers']), 'synthetic answers cannot claim owner confirmation')
    obj(spec['review'], 'status record_ref', 'review')
    require(spec['review']['status'] == 'Pass', 'review must Pass before projection')
    string(spec['review']['record_ref'], 'review.record_ref')
    return spec

def compile_spec(spec, presented_preview, presented_file_bytes, repo_root=None):
    validate_spec(spec, presented_preview, presented_file_bytes, repo_root)
    catalog = load_catalog(repo_root)
    preview = spec['approved_preview']
    instructions = [{'kind': 'boundary', 'instruction': catalog['preamble']}]
    for mapping in sorted(preview['mappings'], key=lambda m: m['id']):
        operation = catalog['operations'][mapping['id']]
        instructions.append({'kind': 'operation', 'operation_id': mapping['id'], 'aspect': operation['aspect'], 'anchor': mapping['anchor'], **operation['anchors'][mapping['anchor']]})
    value = preview['controls']['response_detail']['value']
    if value != 'unspecified':
        instructions.append({'kind': 'control', 'name': 'response_detail', 'value': value, 'instruction': catalog['response_detail'][value]})
    return {'schema_version': 'persona-core-projection-v1', 'source_schema_version': SCHEMA_VERSION, 'revision': preview['revision'], 'snapshot_sha256': digest(preview), 'catalog_sha256': TRUSTED_CATALOG_SHA256, 'confirmation_origin': spec['confirmation']['origin'], 'validation_status': 'structural_only', 'instructions': instructions}

def project(spec_path, presented_path, repo_root=None):
    require(isinstance(spec_path, (str, Path)) and isinstance(presented_path, (str, Path)), 'spec and presented inputs must be local file paths, not a projection')
    try:
        spec = load_document(Path(spec_path).read_bytes())
        raw = Path(presented_path).read_bytes()
        return compile_spec(spec, load_document(raw), raw, repo_root)
    except OSError as error:
        raise CoreError('unreadable input: ' + str(error)) from error

def _format_projection(projection, repo_root=None):
    """Private formatter: caller must first validate through compile_spec/project."""
    obj(projection, 'schema_version source_schema_version revision snapshot_sha256 catalog_sha256 confirmation_origin validation_status instructions', 'projection')
    require(projection['confirmation_origin'] in ORIGINS and projection['validation_status'] == 'structural_only', 'invalid structural provenance')
    require(projection['schema_version'] == 'persona-core-projection-v1' and projection['source_schema_version'] == SCHEMA_VERSION and projection['catalog_sha256'] == TRUSTED_CATALOG_SHA256, 'unsupported projection')
    string(projection['revision'], 'projection.revision')
    require(re.fullmatch(r'r[1-9][0-9]*', projection['revision']) is not None, 'invalid projection revision')
    require(type(projection['snapshot_sha256']) is str and re.fullmatch('[0-9a-f]{64}', projection['snapshot_sha256']) is not None, 'invalid projection snapshot hash')
    catalog = load_catalog(repo_root)
    array(projection['instructions'], 'instructions')
    require(bool(projection['instructions']) and projection['instructions'][0] == {'kind': 'boundary', 'instruction': catalog['preamble']}, 'missing trusted boundary')
    lines = [catalog['preamble']]; seen = set(); previous = ''; control_seen = False
    for instruction in projection['instructions'][1:]:
        require(type(instruction) is dict, 'instruction must be object')
        if instruction.get('kind') == 'operation':
            obj(instruction, 'kind operation_id aspect anchor trigger rule boundary', 'operation instruction')
            opid = instruction['operation_id']; anchor = instruction['anchor']
            require(type(opid) is str and opid in catalog['operations'] and opid not in seen and opid > previous and not control_seen, 'unknown/duplicate/unordered operation')
            operation = catalog['operations'][opid]
            require(type(anchor) is str and anchor in ANCHORS and instruction == {'kind': 'operation', 'operation_id': opid, 'aspect': operation['aspect'], 'anchor': anchor, **operation['anchors'][anchor]}, 'custom projection operation')
            lines.extend([instruction['trigger'], instruction['rule'], instruction['boundary']]); seen.add(opid); previous = opid
        else:
            obj(instruction, 'kind name value instruction', 'control instruction')
            value = instruction['value']
            require(not control_seen and type(value) is str and value in catalog['response_detail'] and instruction == {'kind': 'control', 'name': 'response_detail', 'value': value, 'instruction': catalog['response_detail'][value]}, 'custom/duplicate projection control')
            lines.append(instruction['instruction']); control_seen = True
    return '\n\n'.join(lines) + '\n'

def render(spec_path, presented_path, repo_root=None):
    """Public renderer: validate exact confirmation and presentation before formatting."""
    return _format_projection(project(spec_path, presented_path, repo_root), repo_root)

render_text = render

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('validate-preview'); p.add_argument('preview')
    for command in ('validate', 'project', 'render'):
        p = sub.add_parser(command); p.add_argument('spec'); p.add_argument('--presented', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate-preview':
            validate_preview(load_document(Path(args.preview).read_bytes()))
            print('STRUCTURAL PASS: preview; no owner identity authenticated; operations untested.')
        else:
            projection = project(args.spec, args.presented)
            if args.command == 'validate':
                print('STRUCTURAL PASS: exact snapshot, presented bytes, approvals and review; no owner identity authenticated; operations untested.')
            elif args.command == 'project':
                print(json.dumps(projection, ensure_ascii=False, sort_keys=True, indent=2))
            else:
                print('PROVENANCE: ' + projection['confirmation_origin'] + '; structural_only; operations untested.', file=sys.stderr)
                print(_format_projection(projection), end='')
        return 0
    except (CoreError, OSError) as error:
        print('REJECTED: ' + str(error), file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
