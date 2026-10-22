/* Buildless, local-only educational workflow demo. Registry snapshot at source_base_sha. */
(function () {
  "use strict";
  const REGISTRY = [
  {
    "id": "bfas.volatility",
    "name": "Volatility",
    "mapping_id": "map.volatility.v1",
    "test_id": "B01",
    "dimension": "Expressive response to a stated fictional setback",
    "rules": {
      "low": "Describe the setback in restrained, even phrasing.",
      "middle": "Use one mild emphasis marker when describing the setback.",
      "high": "Use conspicuous but civil emphasis when describing the setback."
    },
    "limitation": "Weak translation: expressive wording is only a proxy; it does not simulate anger, emotional instability, insults, or impaired control.",
    "source_trace": "src.deyoung2007, p. 885; src.ipip.bfas-table",
    "explanation_zh": "挫折描述的強調程度；不是情緒或易怒程度。"
  },
  {
    "id": "bfas.withdrawal",
    "name": "Withdrawal",
    "mapping_id": "map.withdrawal.v1",
    "test_id": "B02",
    "dimension": "Presentation salience of the same known downside",
    "rules": {
      "low": "Present the required downside beside the other considerations.",
      "middle": "Give the downside its own clearly labeled sentence.",
      "high": "Lead with the downside, then present the same options and evidence."
    },
    "limitation": "Weak translation: downside salience is only a proxy; it does not simulate anxiety, depression, avoidance, extra doubt, or reduced willingness to complete authorized work.",
    "source_trace": "src.deyoung2007, p. 885; src.ipip.bfas-table",
    "explanation_zh": "已知缺點的位置；不是焦慮或逃避。"
  },
  {
    "id": "bfas.compassion",
    "name": "Compassion",
    "mapping_id": "map.compassion.v1",
    "test_id": "B03",
    "dimension": "How stated stakeholder needs shape options",
    "rules": {
      "low": "Present the stakeholder impact factually and offer a task-compatible option.",
      "middle": "Explicitly compare one accommodation of the stated stakeholder need.",
      "high": "Organize option generation around the stated stakeholder need, comparing relevant accommodations."
    },
    "limitation": "This is a strategy hypothesis; do not claim felt empathy, infer unstated emotions, or override consent.",
    "source_trace": "src.deyoung2007, pp. 885, 891; src.ipip.bfas-table",
    "explanation_zh": "以已述利害關係人需求比較可行安排；不是感受同理心。"
  },
  {
    "id": "bfas.politeness",
    "name": "Politeness",
    "mapping_id": "map.politeness.v1",
    "test_id": "B04",
    "dimension": "Courtesy around reasoned disagreement",
    "rules": {
      "low": "State the disagreement plainly and civilly.",
      "middle": "Add a short courteous acknowledgment before disagreement.",
      "high": "Acknowledge the alternative's merit, then express disagreement with courteous qualification."
    },
    "limitation": "Courtesy wording is narrower than the human construct; it cannot alter consent, obedience, truth, or respect.",
    "source_trace": "src.deyoung2007, pp. 885, 891; src.ipip.bfas-table",
    "explanation_zh": "表達不同意見時的禮貌措辭；不改變尊重與事實。"
  },
  {
    "id": "bfas.industriousness",
    "name": "Industriousness",
    "mapping_id": "map.industriousness.v1",
    "test_id": "B05",
    "dimension": "Planning decomposition for the same bounded task",
    "rules": {
      "low": "Give a direct adequate plan for completing the required work.",
      "middle": "Plan the required work through explicit milestones.",
      "high": "Decompose the same required work into completion checkpoints with an explicit stopping rule."
    },
    "limitation": "Plan decomposition is narrower than human persistence; required work, actual effort, quality, and stopping scope remain invariant.",
    "source_trace": "src.deyoung2007, Table 3, pp. 884–885; src.ipip.bfas-table",
    "explanation_zh": "同一必要工作的計畫分解；不改變努力、品質或範圍。"
  },
  {
    "id": "bfas.orderliness",
    "name": "Orderliness",
    "mapping_id": "map.orderliness.v1",
    "test_id": "B06",
    "dimension": "Sequencing and adaptation of the same required work",
    "rules": {
      "low": "Use a flexible sequence that includes all required checks.",
      "middle": "Group the required work and checks into stages.",
      "high": "Make dependencies and checks explicit in a checklist, including how to adapt the sequence when conditions change."
    },
    "limitation": "Structure is a limited strategy proxy; it does not establish correctness, compliance, or greater reliability.",
    "source_trace": "src.deyoung2007, Table 3, pp. 884–885; src.ipip.bfas-table",
    "explanation_zh": "同一必要工作的順序與檢查；不代表更可靠。"
  },
  {
    "id": "bfas.enthusiasm",
    "name": "Enthusiasm",
    "mapping_id": "map.enthusiasm.v1",
    "test_id": "B07",
    "dimension": "Warmth and upbeat expression",
    "rules": {
      "low": "Use a reserved, neutral greeting or opening.",
      "middle": "Use a friendly opening and modest positive wording.",
      "high": "Use a warmly animated opening and explicit encouragement appropriate to the facts."
    },
    "limitation": "Expressive tone does not imply pleasure, friendship, optimism about unsupported outcomes, or personal feelings.",
    "source_trace": "src.deyoung2007, pp. 883–885; src.ipip.bfas-table",
    "explanation_zh": "開場的溫暖與鼓勵措辭；不是情感或樂觀預測。"
  },
  {
    "id": "bfas.assertiveness",
    "name": "Assertiveness",
    "mapping_id": "map.assertiveness.v1",
    "test_id": "B08",
    "dimension": "Initiative in an advisory process",
    "rules": {
      "low": "Present viable supported options and solicit the human's choice.",
      "middle": "Offer a tentative recommendation with reasons.",
      "high": "Propose a concrete advisory next step or process with reasons, preserving viable alternatives and human choice."
    },
    "limitation": "Advisory initiative does not confer leadership authority, permission to act, dominance, or factual confidence.",
    "source_trace": "src.deyoung2007, pp. 883–884; src.ipip.bfas-table",
    "explanation_zh": "建議流程的主動程度；不增加權限，保留人的選擇。"
  },
  {
    "id": "bfas.intellect",
    "name": "Intellect",
    "mapping_id": "map.intellect.v1",
    "test_id": "B09",
    "dimension": "Concrete versus conceptual reasoning route",
    "rules": {
      "low": "Lead the reasoning with a concrete usable worked example.",
      "middle": "Explain one general principle together with the usable example.",
      "high": "Lead with a conceptual model, use it to compare options, and apply it to the same usable example."
    },
    "limitation": "Reasoning route is not intelligence, expertise, reasoning quality, or permission to omit needed explanation; correctness remains constant.",
    "source_trace": "src.deyoung2007, pp. 883–884; src.ipip.bfas-table",
    "explanation_zh": "具體範例與概念模型的推理順序；不是智力或能力。"
  },
  {
    "id": "bfas.openness",
    "name": "Openness",
    "mapping_id": "map.openness.v1",
    "test_id": "B10",
    "dimension": "Breadth of feasible option generation",
    "rules": {
      "low": "Develop familiar feasible options under the task's budget.",
      "middle": "Develop one materially different feasible alternative alongside the familiar approach.",
      "high": "Develop multiple materially distinct feasible options under the same budget, labeling assumptions."
    },
    "limitation": "Option breadth is a strategy hypothesis, not originality, sensory experience, artistic merit, or permission to invent facts or expand scope.",
    "source_trace": "src.deyoung2007, pp. 883–884; src.ipip.bfas-table",
    "explanation_zh": "相同預算下可行方案的廣度；不允許捏造或擴張範圍。"
  }
];
  const SOURCE_SHA = '9aa9ff2534c4d1593f07386ad8b99250ea25e72c';
  const ANCHOR_LABELS = {unspecified: '未指定', low: '低', middle: '中間', high: '高'};
  const ASPECT_LABELS = Object.fromEntries(['易變性','退縮性','同情心','禮貌','勤勉性','條理性','熱情','主張性','智性','開放性'].map((name, i) => [REGISTRY[i].id, name]));
  const ANCHORS = ['unspecified', 'low', 'middle', 'high'];
  const RULE_ZH = [
    ['以平穩、克制的措辭描述挫折。','描述挫折時使用一個輕微強調。','描述挫折時使用明顯但文明的強調。'],
    ['將已知缺點與其他考量並列。','用一句明確標示的句子說明缺點。','先說明缺點，再呈現相同選項與證據。'],
    ['客觀呈現影響，並提供符合任務的選項。','明確比較一項對已述需求的調整。','以已述需求組織方案，並比較相關調整。'],
    ['平實、文明地表達不同意見。','先簡短禮貌回應，再表達不同意見。','承認替代方案的優點，再以禮貌限定語表達不同意見。'],
    ['直接提供足以完成必要工作的計畫。','以明確里程碑安排必要工作。','將相同必要工作拆為完成檢查點，並明訂停止規則。'],
    ['採彈性順序，包含所有必要檢查。','將必要工作與檢查分為階段。','以清單明示依賴與檢查，說明條件改變時如何調整。'],
    ['以保留、中性的方式開場。','友善開場，使用適度正面措辭。','以溫暖活潑的方式開場，提供符合事實的鼓勵。'],
    ['提出有支持的可行選項，請人選擇。','提出附理由的暫定建議。','提出附理由的具體建議步驟或流程，保留可行替代方案與人的選擇。'],
    ['先用可實作的具體範例展開推理。','結合一項通則與同一可用範例。','先以概念模型比較選項，再套用於同一可用範例。'],
    ['在任務預算內發展熟悉的可行方案。','在熟悉方案外，加入一項實質不同的可行替代方案。','在相同預算內發展多項實質不同的可行方案，並標明假設。']
  ];
  const ruleZh = (id, target) => RULE_ZH[REGISTRY.findIndex(r => r.id === id)][['low','middle','high'].indexOf(target)];
  const BOUNDARIES = Object.freeze({fictional_low_stakes_advisory_only: true, accuracy: true, explicit_uncertainty: true, privacy: true, safety: true, tool_permissions: true, human_choice: true, human_final_judgment: true, no_real_person_profiling: true, no_diagnosis_or_psychometric_scoring: true, no_sensitive_attribute_inference: true, no_high_stakes_or_autonomous_decisions: true, panel_authorized: false, persistence_authorized: false});
  const clone = value => JSON.parse(JSON.stringify(value));
  function createModel() {
    let revision = 1, sequence = 0, answers = [], conflicts = [], resolutions = [], preview = null, confirmed = null;
    const targets = Object.fromEntries(REGISTRY.map(row => [row.id, 'unspecified']));
    const activeAnswers = Object.fromEntries(REGISTRY.map(row => [row.id, []]));
    function change() { revision++; preview = null; confirmed = null; }
    function record(type, data) { const answer = {id: 'A' + String(++sequence).padStart(3, '0'), type, ...data}; answers.push(answer); return answer; }
    function validateText(text, required) {
      if (typeof text !== 'string' || text.length > 2000 || (required && !text.trim())) throw new Error('請輸入 1–2000 字；原文會完整保留，請勿包含個人資料。');
    }
    function choice(aspect, target, rationale = '', rawId = '') {
      if (!REGISTRY.some(row => row.id === aspect) || !ANCHORS.includes(target)) throw new Error('請選擇清單中的面向與目標。');
      validateText(rationale, false);
      const raw = rawId ? answers.find(a => a.id === rawId && a.type === 'free_text') : null;
      if (rawId && !raw) throw new Error('找不到所連結的未知回答，請重新選擇。');
      change();
      const previous = activeAnswers[aspect].length > 0;
      const a = record('explicit_choice', {aspect, target, rationale, raw_answer_id: rawId || null});
      activeAnswers[aspect].push(a.id);
      let conflict = conflicts.find(c => c.aspect === aspect && c.status === 'unresolved' && c.type === 'choice');
      if (conflict || (previous && targets[aspect] !== target)) {
        if (!conflict) { conflict = {id: 'C' + (conflicts.length + 1), type: 'choice', aspect, candidates: [], status: 'unresolved'}; conflicts.push(conflict); }
        conflict.candidates = answers.filter(item => item.type === 'explicit_choice' && item.aspect === aspect).map(item => ({target: item.target, answer_id: item.id}));
        targets[aspect] = 'unspecified';
      } else targets[aspect] = target;
      if (raw) raw.review = 'explicit_choice_added_raw_remains_unknown';
      return a.id;
    }
    function freeText(text) { validateText(text, true); change(); return record('free_text', {text, interpretation: 'unknown', review: 'pending'}).id; }
    function keepUnknown(id) {
      const answer = answers.find(a => a.id === id && a.type === 'free_text');
      if (!answer) throw new Error('請選擇已記錄的未知回答。');
      change(); answer.review = 'explicitly_keep_unknown'; record('unknown_review', {answer_id: id, decision: 'keep_unknown'});
    }
    function flag(text) { validateText(text, true); change(); const a = record('manual_conflict_flag', {text}); conflicts.push({id: 'C' + (conflicts.length + 1), type: 'manual', aspect: null, candidates: [{answer_id: a.id, text}], status: 'unresolved'}); }
    function resolve(id, target) {
      const c = conflicts.find(c => c.id === id && c.status === 'unresolved');
      if (!c) throw new Error('此衝突已解決，或目前無法取得。');
      if (c.type === 'choice' && !ANCHORS.includes(target)) throw new Error('請明確選擇要保留的目標，或撤回為未指定。');
      change(); const answer = record('conflict_resolution', {conflict_id: id, target: c.type === 'choice' ? target : null, decision: c.type === 'choice' ? 'explicit_anchor_selection' : 'manually_reviewed_flag_resolved'});
      c.status = 'resolved'; c.resolution_answer_id = answer.id;
      c.resolution = c.type === 'choice' ? target : 'User explicitly marked the manually flagged conflict resolved; no text was analyzed or mapped.';
      resolutions.push({conflict_id: id, answer_id: answer.id, resolution: c.resolution, revision});
      if (c.type === 'choice') { targets[c.aspect] = target; activeAnswers[c.aspect].push(answer.id); }
    }
    function snapshot() {
      return {demo_only: true, artifact_type: 'educational_workflow_draft', revision: 'r' + revision, source_base_sha: SOURCE_SHA, registry_path: 'persona-design-v0.2/construct-registry.md', targets: clone(targets), goals: REGISTRY.map(row => ({aspect: row.id, target: targets[row.id], answer_ids: clone(activeAnswers[row.id]), mapping_id: row.mapping_id, mapping_source: 'src.project-mapping-v0.2', human_definition_sources: row.source_trace, mapping_status: 'unvalidated-hypothesis', rule: targets[row.id] === 'unspecified' ? null : row.rules[targets[row.id]], explanation_zh: row.explanation_zh, limitation: row.limitation})), answers: clone(answers), unknown_answers: clone(answers.filter(a => a.type === 'free_text')), conflicts: clone(conflicts), conflict_resolution_history: clone(resolutions), invariants: clone(BOUNDARIES), behavioral_evidence: 'not_run', boundaries: 'Temporary fictional low-stakes advisory educational draft only. Human final judgment required. No psychology, real-user validity, production review, behavioral reliability, or completed protocol claim. Unknown is not middle. Raw free text is never analyzed or automatically mapped. No agent or LLM runs here.', sources: [{id: 'src.deyoung2007', citation: 'DeYoung, Quilty, & Peterson (2007), Between facets and domains: 10 aspects of the Big Five. DOI: 10.1037/0022-3514.93.5.880. Human vocabulary only.'}, {id: 'src.ipip.bfas-table', citation: 'https://ipip.ori.org/BFASTable.htm — human domain/aspect assignments only.'}, {id: 'src.project-mapping-v0.2', citation: 'Original proposed project mappings in the registry. Unvalidated hypotheses; source attribution is not behavioral evidence.'}]};
    }
    function blockers() { return conflicts.some(c => c.status === 'unresolved') ? '請先明確解決所有尚未解決的衝突。' : answers.some(a => a.type === 'free_text' && a.review === 'pending') ? '請逐一檢視未知回答：明確保留未知，或加入連結的明確選擇。' : ''; }
    function makePreview() { preview = snapshot(); confirmed = null; return clone(preview); }
    function confirm(checked) { if (!checked || !preview || preview.revision !== 'r' + revision) throw new Error('請先顯示目前完整預覽，並勾選此修訂的檢視確認方塊。'); if (blockers()) throw new Error(blockers()); confirmed = revision; }
    function exportText() {
      if (confirmed !== revision || !preview || blockers()) throw new Error('匯出尚未開放；請先顯示並明確確認目前無未解衝突的預覽。');
      return '# Persona design demo — educational workflow draft\n\nDemo only. Local review acknowledgment is not a production manual review or validated spec. Behavioral evidence for this draft: not_run.\n\nThe JSON below preserves exactly the displayed draft.\n\n```json\n' + JSON.stringify(preview, null, 2) + '\n```\n';
    }
    return {choice, freeText, keepUnknown, flag, resolve, snapshot, blockers, makePreview, confirm, exportText, invalidate: change, revokeConfirmation() { confirmed = null; }, get revision() { return revision; }, get hasPreview() {return !!preview;}, get isConfirmed() {return confirmed === revision;}};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {createModel, REGISTRY, SOURCE_SHA};
  if (typeof document === 'undefined') return;
  const mount = document.getElementById('persona-demo');
  if (!mount) return;
  let model = createModel();
  function node(tag, text, className) { const n = document.createElement(tag); if (text !== undefined) n.textContent = text; if (className) n.className = className; return n; }
  function button(text, action, parent = mount) { const b = node('button', text, 'button'); b.type = 'button'; b.addEventListener('click', () => {try { action(); } catch (e) { announce(e.message, true); }}); parent.append(b); return b; }
  function label(text, input, parent) { const l = node('label', text, 'field'); l.append(input); parent.append(l); return input; }
  function select(items) { const s = node('select'); items.forEach(([value, text]) => {const o = node('option', text); o.value = value; s.append(o);}); return s; }
  function detail(title, value) { const d = node('details'); d.append(node('summary', title)); if (value !== undefined) { const pre = node('pre', JSON.stringify(value, null, 2)); pre.tabIndex = 0; d.append(pre); } return d; }
  mount.append(node('p', '這是教學用流程草稿。你選擇的是虛構代理應如何回應，不是評估任何人的特質。十個目標起初皆為「未指定」。此示範不使用文字分析、語言模型、網路請求、Cookie 或瀏覽器儲存；內容只留在頁面記憶體，重設或重載即清除。僅由你主動複製或下載。', 'demo-notice'));
  mount.append(node('p', '固定界線：僅供虛構、低風險的建議用途；準確性、明示不確定性、隱私、安全、既有工具權限、人的選擇與最終判斷始終不變。禁止診斷、心理計分、敏感屬性推斷、真人側寫、高風險或自主最終決策。此簡化示範不會完成正式協定，也不能驗證人工審查身分。'));
  const status = node('p', '', 'demo-status'); status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite'); mount.append(status);
  const controls = node('div', undefined, 'demo-controls'); mount.append(controls);
  const mode = label('輸入模式', select([['choice', '明確選擇'], ['free', '自由簡答，保留未知']]), controls);
  const choicePane = node('div', undefined, 'demo-grid'); controls.append(choicePane);
  const aspect = label('選擇面向', select(REGISTRY.map(r => [r.id, ASPECT_LABELS[r.id] + ' · ' + r.name])), choicePane);
  const anchor = label('選擇目標（中間值須明選；未指定不產生規則）', select(ANCHORS.map(a => [a, ANCHOR_LABELS[a]])), choicePane);
  const optionsText = node('div', undefined, 'demo-card'); choicePane.append(optionsText);
  function showOptions() { optionsText.replaceChildren(); const row = REGISTRY.find(r => r.id === aspect.value); optionsText.append(node('p', row.explanation_zh)); for (const a of ['low', 'middle', 'high']) optionsText.append(node('p', ANCHOR_LABELS[a] + '：' + ruleZh(row.id, a))); const d = detail('三個目標的英文規則與來源'); for (const a of ['low', 'middle', 'high']) d.append(node('p', ANCHOR_LABELS[a] + '：' + row.rules[a])); d.append(node('p', row.mapping_id + ' · ' + row.limitation)); optionsText.append(d); }
  showOptions(); aspect.addEventListener('change', showOptions);
  const rationaleInput = node('textarea'); rationaleInput.maxLength = 2000; rationaleInput.rows = 2; const rationale = label('選填理由（最多 2000 字；請勿填個人資料）', rationaleInput, choicePane);
  const rawRef = label('選填：明確連結一則未知回答', select([['', '不連結回答']]), choicePane);
  button('加入選擇', () => {const id = model.choice(aspect.value, anchor.value, rationale.value, rawRef.value); rationale.value = ''; refresh('已記錄 ' + id + '。');}, choicePane);
  const freePane = node('div', undefined, 'demo-grid'); controls.append(freePane); freePane.hidden = true;
  const rawInput = node('textarea'); rawInput.maxLength = 2000; rawInput.rows = 4;
  const raw = label('描述虛構代理應有的行為（保留原文，最多 2000 字）', rawInput, freePane);
  freePane.append(node('p', '簡答不會被解讀、分類或自動對應。即使之後加入連結的明確選擇，原文仍保留為未知；請於下方明確檢視。'));
  button('保留簡答為未知', () => {const id = model.freeText(raw.value); raw.value = ''; refresh('已記錄未知回答 ' + id + '。');}, freePane);
  mode.addEventListener('change', () => {choicePane.hidden = mode.value !== 'choice'; freePane.hidden = mode.value !== 'free';});
  const manualInput = node('textarea'); manualInput.maxLength = 2000; manualInput.rows = 2;
  const manual = label('手動描述矛盾（不會自動分析文字）', manualInput, controls);
  button('標記衝突', () => {model.flag(manual.value); manual.value = ''; refresh('已保留手動衝突。');}, controls);
  const history = node('div', undefined, 'demo-history'); mount.append(history);
  const conflictsPane = node('div', undefined, 'demo-conflicts'); mount.append(conflictsPane);
  const previewTrigger = node('div', undefined, 'demo-actions'); mount.append(previewTrigger);
  const previewArea = node('div', undefined, 'demo-preview'); mount.append(previewArea);
  const actions = node('div', undefined, 'demo-actions'); mount.append(actions);
  const review = node('input'); review.type = 'checkbox'; review.disabled = true;
  let previewButton;
  previewButton = button('顯示完整預覽', () => { const p = model.makePreview(); renderPreview(p); review.checked = false; review.disabled = !!model.blockers(); confirmButton.disabled = !!model.blockers(); copyButton.disabled = true; downloadButton.disabled = true; announce('已顯示預覽 ' + p.revision + '。' + (model.blockers() || '請檢視完整草稿，再明確確認此修訂。')); previewArea.focus(); }, previewTrigger);
  const reviewLabel = label('我已檢視此修訂的完整示範預覽，包括未知回答、衝突與固定界線；此勾選只代表示範確認，並非正式人工審查。', review, actions);
  const confirmButton = button('確認此示範修訂', () => {model.confirm(review.checked); copyButton.disabled = false; downloadButton.disabled = false; announce('示範修訂 r' + model.revision + ' 已確認；匯出將保留此次顯示的完整草稿。');}, actions); confirmButton.disabled = true;
  const copyButton = button('複製 Markdown', async () => {
    const text = model.exportText(); const copyRevision = model.revision;
    try { if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('無法使用剪貼簿'); await navigator.clipboard.writeText(text); announce('已依你的操作複製草稿。'); }
    catch (_) {if (model.revision !== copyRevision || !model.isConfirmed) return; fallback.value = text; fallback.hidden = false; fallback.focus(); fallback.select(); announce('剪貼簿不可用；請從下方文字框選取並複製完整草稿。');}
  }, actions); copyButton.disabled = true;
  const downloadButton = button('下載 Markdown', () => { const text = model.exportText(); try {const blob = new Blob([text], {type: 'text/markdown;charset=utf-8'}); const url = URL.createObjectURL(blob); const a = node('a'); a.href = url; a.download = 'persona-design-demo.md'; mount.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000); announce('已要求下載草稿；若瀏覽器未開始下載，可使用下方可讀文字備援。');} catch (_) {announce('無法下載；請從下方可讀文字備援複製。');} fallback.value = text; fallback.hidden = false; }, actions); downloadButton.disabled = true;
  review.addEventListener('change', () => { if (!review.checked) { model.revokeConfirmation(); copyButton.disabled = true; downloadButton.disabled = true; fallback.value = ''; fallback.hidden = true; announce('已撤回檢視確認；匯出前請重新確認目前預覽。'); } });
  const fallback = node('textarea', undefined, 'demo-fallback'); fallback.readOnly = true; fallback.rows = 12; fallback.hidden = true; fallback.setAttribute('aria-label', '完整教學草稿匯出文字，可選取並複製'); mount.append(fallback);
  button('重設：清除頁面記憶', () => {model = createModel(); raw.value = ''; rationale.value = ''; manual.value = ''; aspect.selectedIndex = 0; anchor.selectedIndex = 0; mode.value = 'choice'; choicePane.hidden = false; freePane.hidden = true; showOptions(); refresh('已清除此頁記憶體中的回答、預覽與確認；先前複製或下載的內容不受此重設影響。');}, actions);
  function announce(text, error = false) {status.textContent = text; status.className = error ? 'demo-status demo-error' : 'demo-status'; status.setAttribute('role', error ? 'alert' : 'status');}
  function dirty() {model.invalidate(); review.checked = false; review.disabled = true; confirmButton.disabled = true; copyButton.disabled = true; downloadButton.disabled = true; previewArea.replaceChildren(node('p', '內容已改變；確認或匯出前，請重新顯示完整預覽。')); fallback.value = ''; fallback.hidden = true; announce('修訂 r' + model.revision + '：先前預覽與確認已失效。');}
  [aspect, anchor, rationale, rawRef, raw, manual].forEach(input => input.addEventListener('input', dirty));
  function renderPreview(p) {
    previewArea.replaceChildren(node('h3', '完整教學預覽 · ' + p.revision)); previewArea.tabIndex = -1;
    for (const goal of p.goals) {
      const card = node('section', undefined, 'demo-card');
      card.append(node('h4', ASPECT_LABELS[goal.aspect] + ' → ' + ANCHOR_LABELS[goal.target]), node('p', goal.explanation_zh), node('p', goal.rule ? ruleZh(goal.aspect, goal.target) : '未指定：不產生此面向的規則，也不代表中間值。'));
      const d = detail('來源、英文規則與回答依據', goal); card.append(d); previewArea.append(card);
    }
    previewArea.append(node('h4', '未知回答與固定界線'));
    if (!p.unknown_answers.length) previewArea.append(node('p', '沒有簡答未知回答；未指定目標仍保留未指定。'));
    for (const a of p.unknown_answers) previewArea.append(node('p', a.id + '：' + a.text + '（原文仍為未知；' + (a.review === 'pending' ? '待明確檢視' : '已明確檢視') + '）'));
    previewArea.append(node('p', '行為證據：未執行（not_run）。準確性、明示不確定性、隱私、安全、工具權限、人的選擇與最終判斷不變。僅限虛構低風險建議；不主張心理效度、正式審查完成或正式規格。'));
    previewArea.append(detail('完整資料與回答追溯', p));
  }
  function refresh(message) {
    const p = model.snapshot(); history.replaceChildren(node('h3', '保留的回答紀錄'));
    if (!p.answers.length) history.append(node('p', '尚無回答，十個目標皆為未指定。'));
    const typeNames = {free_text: '簡答原文（未知）', explicit_choice: '明確選擇', unknown_review: '未知回答檢視', manual_conflict_flag: '手動衝突標記', conflict_resolution: '明確解決紀錄'};
    p.answers.forEach(a => {const card = node('div', undefined, 'demo-card'); card.append(node('p', a.id + ' · ' + typeNames[a.type])); if (a.text) card.append(node('p', a.text)); if (a.aspect) card.append(node('p', ASPECT_LABELS[a.aspect] + '：' + ANCHOR_LABELS[a.target])); if (a.rationale) card.append(node('p', '理由：' + a.rationale)); card.append(detail('此回答的完整追溯資料', a)); if (a.type === 'free_text') button('明確保留 ' + a.id + ' 為未知', () => {model.keepUnknown(a.id); refresh(a.id + ' 已明確保留為未知。');}, card); history.append(card);});
    const priorRef = rawRef.value; rawRef.replaceChildren(); [['', '不連結回答'], ...p.unknown_answers.map(a => [a.id, a.id + ' · 未知'])].forEach(([v,t]) => {const o=node('option',t);o.value=v;rawRef.append(o);}); if (p.unknown_answers.some(a => a.id === priorRef)) rawRef.value = priorRef;
    conflictsPane.replaceChildren(node('h3', '衝突與明確解決紀錄'));
    if (!p.conflicts.length) conflictsPane.append(node('p', '目前沒有已標記衝突。簡答矛盾不會自動偵測；若有矛盾，請使用手動標記。'));
    p.conflicts.forEach(c => {const card = node('div', undefined, 'demo-card'); card.append(node('p', c.id + ' · ' + (c.status === 'unresolved' ? '尚未解決：會阻擋確認' : '已明確解決') + (c.aspect ? ' · ' + ASPECT_LABELS[c.aspect] : ' · 手動標記'))); c.candidates.forEach(candidate => card.append(node('p', '保留候選：' + (candidate.target ? ANCHOR_LABELS[candidate.target] : candidate.text) + ' · ' + (candidate.answer_id || '')))); card.append(detail('衝突與解決的完整追溯資料', c)); if (c.status === 'unresolved') {if (c.type === 'choice') {const s = label('解決衝突 ' + c.id + '：選擇一個目標，或撤回為未指定', select([['', '請選擇解決方式'], ...ANCHORS.map(a => [a,ANCHOR_LABELS[a]])]), card); button('明確解決 ' + c.id + '', () => {model.resolve(c.id, s.value); refresh(c.id + ' 已明確解決。');}, card);} else button('我已檢視此手動標記，明確標為已解決', () => {model.resolve(c.id); refresh(c.id + ' 已由你明確解決；系統未解讀或對應原文。');}, card);} conflictsPane.append(card);});
    previewArea.replaceChildren(node('p', '目前草稿：r' + model.revision + '。請顯示完整預覽以進行檢視。')); review.checked = false; review.disabled = true; confirmButton.disabled = true; copyButton.disabled = true; downloadButton.disabled = true; fallback.value = ''; fallback.hidden = true;
    announce(message + ' 目前草稿 r' + model.revision + '。' + model.blockers());
  }
  refresh('已就緒，僅供教學示範。');
})();
