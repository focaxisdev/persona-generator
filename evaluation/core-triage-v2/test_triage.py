"""Offline synthetic integrity fixtures only; no experimental model calls."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location('v2_test_subject', HERE / 'triage.py')
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
TEXT = 'Amber lantern glows.'
CASE = {'observables': [{'id': 'feature', 'values': ['true', 'false', 'unclear', 'not_applicable']}]}


def rating(value='true', quote=TEXT):
    return {'packet_sha256': 'a' * 64, 'observations': [{'id': 'feature', 'value': value, 'quote': quote}],
            'safety': 'clear', 'permission': 'clear', 'task_adequacy': 'adequate', 'leakage': 'none',
            'notes': '' if value == 'true' else 'feature: Synthetic explanation only.'}


class ContractTests(unittest.TestCase):
    def validate(self, value):
        return t.validate_rating(value, CASE, TEXT, 'a' * 64)

    def test_complete_matrix_and_no_mutation(self):
        for value, quote in [('true', TEXT), ('false', None), ('false', TEXT), ('unclear', None), ('unclear', TEXT), ('not_applicable', None)]:
            with self.subTest(value=value, quote=quote):
                obj = rating(value, quote)
                before = copy.deepcopy(obj)
                self.validate(obj)
                self.assertEqual(obj, before)

    def test_reject_invalid_quote_types_empty_missing_and_contradictions(self):
        for value, quotes in [('true', [None, '', ' ', 'amber', 'null', 1, False, [], {}]),
                              ('false', ['', ' ', 'not present', 'null', 1, False, [], {}]),
                              ('unclear', ['', ' ', 'not present', 'null', 1, False, [], {}]),
                              ('not_applicable', [TEXT, '', ' ', 'null', 1, False, [], {}])]:
            for quote in quotes:
                with self.subTest(value=value, quote=quote), self.assertRaises(ValueError):
                    self.validate(rating(value, quote))
        obj = rating()
        del obj['observations'][0]['quote']
        with self.assertRaises(ValueError): self.validate(obj)

    def test_reject_missing_extra_duplicate_and_wrong_types(self):
        for field in rating():
            obj = rating(); del obj[field]
            with self.subTest(missing=field), self.assertRaises(ValueError): self.validate(obj)
        mutations = [lambda x: x.update(extra=1), lambda x: x.update(observations={}),
                     lambda x: x.update(observations=[None]), lambda x: x.update(observations=[]),
                     lambda x: x['observations'].append(copy.deepcopy(x['observations'][0])),
                     lambda x: x['observations'][0].update(extra=1),
                     lambda x: x['observations'][0].update(id='unknown'),
                     lambda x: x['observations'][0].update(value=True),
                     lambda x: x.update(notes=None), lambda x: x.update(safety=False),
                     lambda x: x.update(permission='safe'), lambda x: x.update(task_adequacy=True),
                     lambda x: x.update(leakage='invalid'), lambda x: x.update(packet_sha256='b' * 64)]
        for mutate in mutations:
            obj=rating(); mutate(obj)
            with self.subTest(obj=obj), self.assertRaises(ValueError): self.validate(obj)

    def test_null_string_is_not_a_sentinel_even_if_present_in_output(self):
        for value in ('true','false','unclear','not_applicable'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                t.validate_rating(rating(value, 'null'), CASE, 'null', 'a' * 64)

    def test_nontrue_explanations_are_explicit_id_lines(self):
        for notes in ['', 'some reason', 'other: explanation', 'feature:   ']:
            obj=rating('false', None); obj['notes']=notes
            with self.subTest(notes=notes), self.assertRaises(ValueError): self.validate(obj)

    def test_packet_contains_actual_contract_schema_and_synthetic_examples(self):
        contract=t.read(HERE/'rating-contract.json')
        payload=t.packet_payload('opaque', {'task':'Synthetic color question', **CASE}, {'raw_output':TEXT}, 'a')
        embedded=payload['message'][len(contract['instructions']) + 1:].rsplit('\nPacket hash: ', 1)[0]
        data=json.loads(embedded)
        self.assertEqual(data['rating_schema'], contract['schema'])
        self.assertEqual(data['synthetic_examples'], contract['synthetic_examples'])
        for example in contract['synthetic_examples']:
            obj=rating(); obj['observations']=[example['observation']]; obj['notes']=example['notes']
            case={'observables':[{'id':'example_observable','values':CASE['observables'][0]['values']}]}
            t.validate_rating(obj, case, example['synthetic_raw_output'], 'a'*64)
        self.assertNotEqual(payload['task_name'], t.original.packet_payload('opaque', {'task':'Synthetic color question', **CASE}, {'raw_output':TEXT}, 'a')['task_name'])
        for case in t.read(t.SOURCE/'design.json')['cases']:
            self.assertNotIn(case['task'], json.dumps(contract['synthetic_examples']))

    def test_read_only_historical_collect_all_audit(self):
        result=subprocess.run([sys.executable,str(HERE/'diagnose.py')],cwd=ROOT,capture_output=True,text=True,timeout=30,check=True)
        audit=json.loads(result.stdout)
        for outcome in audit['judges'].values():
            self.assertEqual(outcome['all_failed_checks'],['invalid anchored observation']*13)
            self.assertEqual(outcome['null_quotes_by_value'],{'true':0,'false':3,'unclear':0,'not_applicable':10})
            self.assertEqual(outcome['other_masked_failures'],[])
            self.assertIs(outcome['new_v2_evidence'],False)

    def test_schema_golden_matrix_when_jsonschema_available(self):
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            self.skipTest('optional independent JSON Schema checker unavailable; production uses standard library only')
        schema=t.read(HERE/'rating-contract.json')['schema']
        Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema)
        for value in ('true','false','unclear','not_applicable'):
            for quote in [TEXT,None,'',' ','null',False,1,[],{}]:
                with self.subTest(value=value,quote=quote):
                    expected=(isinstance(quote,str) and quote==TEXT and value!='not_applicable') or (quote is None and value!='true')
                    self.assertEqual(validator.is_valid(rating(value,quote)),expected)
        for example in t.read(HERE/'rating-contract.json')['synthetic_examples']:
            obj=rating(); obj['observations']=[example['observation']];obj['notes']=example['notes']
            self.assertTrue(validator.is_valid(obj))

    def test_original_judge_candidates_remain_rejected_by_new_packet_binding(self):
        manifest,cases=t.original.verify(); cell=manifest['cells'][0]
        output=t.read(t.SOURCE/'outputs'/(cell['id']+'.json'))
        packet=t.packet_payload(cell['id'], cases[cell['case']], output, 'a')
        digest=t.sha(packet['message'].rsplit('\nPacket hash: ',1)[0].encode())
        for judge in 'ab':
            candidate=t.read(t.SOURCE/'records'/(cell['id']+'-'+judge+'.invalid-original.json'))['rating']
            with self.assertRaisesRegex(ValueError,'packet identity'):
                t.validate_rating(candidate,cases[cell['case']],output['raw_output'],digest)


class ProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template_dir=tempfile.TemporaryDirectory(); cls.template=Path(cls.template_dir.name)
        shutil.copytree(t.SOURCE,cls.template/'evaluation/core-triage-v1',ignore=shutil.ignore_patterns('__pycache__'))
        for relative in t.original.dependencies():
            target=cls.template/relative; target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/relative,target)
        cls.here=cls.template/'evaluation/core-triage-v2'; cls.here.mkdir()
        for source in HERE.iterdir():
            if source.is_file() and source.name not in t.EXCLUDED and source.name!='manifest.json': shutil.copyfile(source,cls.here/source.name)
        cls.cli_at(cls.template,'prepare')
        (cls.template/'synthetic-review.json').write_text(json.dumps({'decision':'approve','reviewer':'SYNTHETIC LOCAL TEST ONLY; not independent approval','draft_sha256':t.sha((cls.here/'draft-hashes.json').read_bytes())}))
        cls.cli_at(cls.template,'freeze',str(cls.template/'synthetic-review.json'))

    @classmethod
    def tearDownClass(cls): cls.template_dir.cleanup()

    @staticmethod
    def cli_at(root,*args,ok=True):
        result=subprocess.run([sys.executable,str(root/'evaluation/core-triage-v2/triage.py'),*args],cwd=root,capture_output=True,text=True,timeout=60)
        if ok and result.returncode: raise AssertionError(result.stdout+result.stderr)
        if not ok and not result.returncode: raise AssertionError('unexpected acceptance '+str(args))
        return result

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'repo'; shutil.copytree(self.template,self.root)
        self.here=self.root/'evaluation/core-triage-v2'

    def cli(self,*args,ok=True): return self.cli_at(self.root,*args,ok=ok)

    def test_real_builder_and_frozen_allocation_and_no_runtime_preparation(self):
        self.cli('verify')
        for name in t.MUTABLE: self.assertFalse((self.here/name).exists())
        old=t.read(self.root/'evaluation/core-triage-v1/manifest.json')
        new=t.read(self.here/'manifest.json')
        self.assertEqual([x['id'] for x in old['cells']],[x['id'] for x in new['cells']])
        self.assertEqual(new['new_generator_maximum'],17); self.assertEqual(new['new_judge_maximum'],36)
        self.assertEqual(new['new_call_maximum'],53)

    def test_import_carried_exact_once_and_block_first_regeneration(self):
        self.cli('reserve',ok=False)
        self.cli('import-carried')
        path=self.here/'outputs'/(t.CARRIED_ID+'.json')
        self.assertEqual(path.read_bytes(),(self.root/'evaluation/core-triage-v1/outputs'/path.name).read_bytes())
        self.cli('import-carried',ok=False)
        self.cli('reserve',ok=False)  # no two new locked ratings yet
        self.cli('packet',t.CARRIED_ID)
        self.cli('packet',t.CARRIED_ID,ok=False) # no repeated prospective judge slots
        self.assertFalse((self.here/'ratings').exists()); self.assertFalse((self.here/'locks').exists())
        self.cli('reserve',ok=False)

    def test_source_terminal_report_and_carried_bytes_are_dependencies(self):
        for rel in ['records/REPORT.md','outputs/'+t.CARRIED_ID+'.json']:
            path=self.root/'evaluation/core-triage-v1'/rel; data=path.read_bytes(); path.chmod(0o644); path.write_bytes(data+b' ')
            self.cli('verify',ok=False)
            path.write_bytes(data)
        self.cli('verify')

    def test_historical_ratings_cannot_be_imported_or_locked_as_new(self):
        self.cli('import-carried'); self.cli('packet',t.CARRIED_ID)
        target=self.here/'ratings'; target.mkdir()
        for judge in 'ab':
            shutil.copyfile(self.root/'evaluation/core-triage-v1/records'/(t.CARRIED_ID+'-'+judge+'.invalid-original.json'),target/(t.CARRIED_ID+'-'+judge+'.json'))
        result=self.cli('lock-ratings',t.CARRIED_ID,ok=False)
        self.assertIn('packet identity',result.stderr)
        self.assertFalse((self.here/'locks').exists())

    def retain_pair(self,cell_id,failed=False,lock=True):
        """Synthetic bookkeeping fixtures, never semantic ratings or actual calls."""
        output=t.read(self.here/'outputs'/(cell_id+'.json'))
        manifest=t.read(self.here/'manifest.json'); cell=next(x for x in manifest['cells'] if x['id']==cell_id)
        case=next(x for x in t.read(self.root/'evaluation/core-triage-v1/design.json')['cases'] if x['id']==cell['case'])
        target=self.here/'ratings';target.mkdir(exist_ok=True)
        for judge in 'ab':
            packet=t.read(self.here/'packets'/(cell_id+'-'+judge+'.json'))
            meta=copy.deepcopy(output['metadata'])
            meta.update(agent_id='SYNTHETIC-'+cell_id+'-'+judge,context_id='SYNTHETIC-context-'+cell_id+'-'+judge,
                        requested_parameters={k:packet[k] for k in ('model','reasoning_effort','fork_turns')},
                        raw_receipt='SYNTHETIC local integrity fixture; no model call')
            observations=[{'id':o['id'],'value':'false' if o['id'] in ('invented_dependencies','unauthorized_action_claim') else 'true',
                           'quote':None if o['id'] in ('invented_dependencies','unauthorized_action_claim') else output['raw_output']} for o in case['observables']]
            obj={'packet_sha256':t.sha(packet['message'].rsplit('\nPacket hash: ',1)[0].encode()),'observations':observations,
                 'safety':'clear','permission':'clear','task_adequacy':'adequate','leakage':'none',
                 'notes':'invented_dependencies: Synthetic absence.\nunauthorized_action_claim: Synthetic absence.'}
            record={'raw_response_text':json.dumps(obj),'rating':obj,'metadata':meta}
            if failed and judge=='a': record={'status':'invalid','error':'SYNTHETIC invalid attempt','raw_response_text':'{truncated','metadata':meta}
            (target/(cell_id+'-'+judge+'.json')).write_text(json.dumps(record))
        if lock: self.cli('lock-ratings',cell_id)

    def add_output(self,cell,raw_output):
        obj=t.read(self.here/'outputs'/(t.CARRIED_ID+'.json'))
        obj['id']=cell['id'];obj['raw_output']=raw_output
        obj['request_sha256']=t.sha((self.here/cell['asset']/'request.json').read_bytes())
        obj['metadata']['agent_id']='SYNTHETIC-generator-'+cell['id'];obj['metadata']['context_id']='SYNTHETIC-generation-context-'+cell['id']
        obj['metadata']['raw_receipt']='SYNTHETIC local fixture; no call'
        (self.here/'outputs'/(cell['id']+'.json')).write_text(json.dumps(obj))

    def test_two_new_locked_judges_gate_continuation_budget_stop_and_provenance(self):
        self.cli('import-carried');self.cli('packet',t.CARRIED_ID)
        self.retain_pair(t.CARRIED_ID)
        manifest=t.read(self.here/'manifest.json');second=manifest['cells'][1]
        request=self.cli('reserve').stdout
        self.assertEqual(json.loads(request),t.read(self.here/second['asset']/'request.json'))
        self.cli('reserve',ok=False) # pending new generator cannot be retried
        self.add_output(second,'word '*251)
        self.cli('packet',second['id']);self.retain_pair(second['id'])
        self.assertTrue(json.loads(self.cli('validate-output',second['id']).stdout)['stop_dependent_runs'])
        self.cli('reserve',ok=False)
        self.cli('terminate','SYNTHETIC budget failure; no actual calls')
        result=json.loads(self.cli('reveal').stdout)
        rows=result['crosswalk_and_original_ratings']
        self.assertEqual(rows[0]['response_origin'],'carried_exact_prior_response')
        self.assertEqual(rows[1]['response_origin'],'new_generation')
        self.assertEqual(rows[1]['response_classification'],'budget_failure')
        self.assertEqual(result['v2_attempt_accounting']['new_generator_attempts'],1)
        self.assertEqual(len(result['termination']['unattempted']),16)

    def test_failed_new_judge_stops_and_terminal_reveal_keeps_condition_hidden(self):
        self.cli('import-carried');self.cli('packet',t.CARRIED_ID);self.retain_pair(t.CARRIED_ID,failed=True)
        self.cli('reserve',ok=False)
        self.cli('terminate','SYNTHETIC judge failure; no calls')
        result=json.loads(self.cli('reveal').stdout)
        row=result['crosswalk_and_original_ratings'][0]
        self.assertNotIn('condition',row);self.assertNotIn('case',row)
        self.assertEqual(row['response_origin'],'carried_exact_prior_response')
        self.assertEqual(result['v2_attempt_accounting']['new_generator_attempts'],0)

    def test_actual_rating_record_requires_bare_strict_json_object(self):
        self.cli('import-carried');self.cli('packet',t.CARRIED_ID);self.retain_pair(t.CARRIED_ID,lock=False)
        path=self.here/'ratings'/(t.CARRIED_ID+'-a.json')
        original=t.read(path)
        raw=original['raw_response_text']
        malformed=['```json\n'+raw+'\n```', '```\n'+raw+'\n```',raw+' trailing text',
                   '{"notes":"duplicate",'+raw[1:],raw[:-1], '['+raw+']']
        for text in malformed:
            record=copy.deepcopy(original);record['raw_response_text']=text;path.write_text(json.dumps(record))
            self.cli('lock-ratings',t.CARRIED_ID,ok=False)
            self.assertFalse((self.here/'locks').exists())
        # Surrounding JSON whitespace is permitted without changing retained text.
        original['raw_response_text']='  \n'+raw+'\n  '
        path.write_text(json.dumps(original))
        self.cli('lock-ratings',t.CARRIED_ID)
        self.assertTrue((self.here/'locks'/(t.CARRIED_ID+'.json')).exists())

    def test_complete_synthetic_prefix_stops_after_exactly_seventeen_new_generator_slots(self):
        self.cli('import-carried')
        manifest=t.read(self.here/'manifest.json')
        for index,cell in enumerate(manifest['cells']):
            if index:
                request=json.loads(self.cli('reserve').stdout)
                self.assertEqual(request,t.read(self.here/cell['asset']/'request.json'))
                self.add_output(cell,TEXT)
            self.cli('packet',cell['id']);self.retain_pair(cell['id'])
        result=self.cli('reserve')
        self.assertIn('All 18 attempt slots consumed',result.stdout)
        records=list((self.here/'records').glob('*.reservation.json'))
        self.assertEqual(len(records),18)
        self.assertEqual(sum(t.read(path).get('mode')!='carried_exact_prior_response' for path in records),17)
        result=json.loads(self.cli('reveal').stdout)
        self.assertEqual(result['v2_attempt_accounting']['carried_responses'],1)
        self.assertEqual(result['v2_attempt_accounting']['new_generator_attempts'],17)
        self.assertEqual(result['v2_attempt_accounting']['new_judge_attempt_slots_reserved'],36)

    def test_new_generator_cannot_reuse_a_historical_judge_context(self):
        self.cli('import-carried');self.cli('packet',t.CARRIED_ID);self.retain_pair(t.CARRIED_ID)
        self.cli('reserve');cell=t.read(self.here/'manifest.json')['cells'][1]
        self.add_output(cell,TEXT)
        output_path=self.here/'outputs'/(cell['id']+'.json');obj=t.read(output_path)
        old=t.read(self.root/'evaluation/core-triage-v1/ratings'/(t.CARRIED_ID+'-a.json'))['metadata']
        obj['metadata'].update(agent_id=old['agent_id'],context_id=old['context_id']);output_path.write_text(json.dumps(obj))
        result=self.cli('validate-output',cell['id'],ok=False)
        self.assertIn('reused',result.stderr)

    def test_truncated_and_extra_key_raw_judge_responses_stop(self):
        self.cli('import-carried'); self.cli('packet',t.CARRIED_ID)
        target=self.here/'ratings'; target.mkdir()
        archive=t.read(self.root/'evaluation/core-triage-v1/records'/(t.CARRIED_ID+'-a.invalid-original.json'))
        for text in ['{"observations":', '{"extra":1}']:
            record=copy.deepcopy(archive); record['raw_response_text']=text
            (target/(t.CARRIED_ID+'-a.json')).write_text(json.dumps(record))
            self.cli('lock-ratings',t.CARRIED_ID,ok=False)
        self.assertFalse((self.here/'locks').exists())

if __name__=='__main__': unittest.main()
