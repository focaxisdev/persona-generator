"""Read-only historical failure audit; regression evidence, never new ratings."""
import json
from pathlib import Path
import triage


def diagnose():
    manifest, cases = triage.original.verify()
    cell = manifest['cells'][0]
    case = cases[cell['case']]
    output = triage.read(triage.SOURCE / 'outputs' / (cell['id'] + '.json'))
    report = {'purpose': 'historical structural regression only; no acceptance, conversion or semantic rerating', 'judges': {}}
    for judge in ('a', 'b'):
        historical = triage.read(triage.SOURCE / 'records' / (cell['id'] + '-' + judge + '.invalid-original.json'))
        module = triage.load_v1('v1_read_only_audit_' + judge)
        original_read, original_require = module.read, module.require
        failures = []
        target = triage.SOURCE / 'ratings' / (cell['id'] + '-' + judge + '.json')
        def redirected_read(path):
            return historical if Path(path) == target else original_read(path)
        def collect_require(ok, message):
            if not ok:
                failures.append(message)
        module.read, module.require = redirected_read, collect_require
        # All subsequent checks remain the unchanged v1 function body. The
        # in-memory candidate substitution never writes/repairs a source file.
        module.rating_record(cell['id'], judge, case, output)
        observations = historical['rating']['observations']
        report['judges'][judge] = {'all_failed_checks': failures,
            'null_quotes_by_value': {value: sum(item['value'] == value and item['quote'] is None for item in observations) for value in ('true', 'false', 'unclear', 'not_applicable')},
            'other_masked_failures': [failure for failure in failures if failure != 'invalid anchored observation'],
            'historical_packet_binding_retained': True,
            'new_v2_evidence': False}
    return report

if __name__ == '__main__':
    print(json.dumps(diagnose(), indent=2))
