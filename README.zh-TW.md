# Persona Generator / 人格產生器

為一個虛構、低風險任務設定單一 AI agent 的行為。主流程是：希望 agent 如何表現 → 來源與構念脈絡 → 人工確認的完整 spec → 確定性的有效指令投影 → 綁定版本的證據。

**從這裡開始：**[Quickstart](docs/QUICKSTART.md) → [core 合約](core/README.md)。[English README](README.md) · [AI 導覽](AI_DISCOVERY.md)

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## 目前範圍：尚未發布的 v0.2 候選版

核心流程透過選項或自由短答詢問「希望 agent 如何表現」，不推測使用者人格。未回答的設定保持 `unspecified`。使用者先檢查來源、轉譯理由、精確規則、衝突與完整預覽，再明確確認。行為變更必須重新預覽與確認；新 session 使用前須核對原確認內容。

[涵蓋表](core/COVERAGE.md)將十個 Big Five aspects 作為研究詞彙。核心只支援兩個新的操作類比：`op.planning_structure.v1` 與 `op.advisory_initiative.v1`。兩者都是**尚未經行為試驗的工程提案**，不代表已實現人類特質；其餘面向保持未指定，不產生指令。[來源與存取限制](core/SOURCES.md)支持詞彙脈絡，不證明本專案的 agent 行為有效。請讀[主張邊界](docs/CLAIMS_MATRIX.md)。

本機 compiler 檢查 core 合約，從固定邊界、已核准的 operation 規則與明確核准的回答詳略控制產生有效指令。訪談原文、來源摘錄、解釋與其他追溯欄位都是惰性資料，不能被拼進執行指令。確定性輸出能說明產生了什麼，不保證模型遵守，也無法自行證明真正的人已同意。

## 以一個任務開始

```text
讀 docs/QUICKSTART.md 與 core/README.md，協助設定一個為虛構桌遊下午
提供建議的 agent。可用選項或自由短答，詢問我希望 agent 如何表現。
把提案連到 core 的來源與涵蓋表，略過的設定保持未指定。顯示完整且
精確的預覽，等我確認後才能產生可使用的 spec。不要推測我的人格，
也不要自行增加 panel 或持久化 Persona Pack。
```

檢查與編譯合約不需要 hosted service、帳號、付費 API、資料庫、遙測或模型呼叫。把指令交給模型是另一個需人工審閱的步驟：只使用[固定請求格式](core/REQUEST_ENVELOPE.md)中的精確 renderer stdout，不能傳入 projection JSON、spec 或訪談歷史。完成受限的單一 agent 任務後停止。

## 證據與限制

套件 v0.2 候選版、core schema 版本、operation 版本，以及舊 mapping 版本各自獨立。新 core 行為試驗與真正 owner 的端到端試驗均為 **NOT RUN**；靜態測試只支持實際測過的合約性質。不宣稱十個特質已實現、心理計量有效、人類心智／情緒、通用穩定性或跨模型可靠性。

[舊 v1 試行](evaluation/pilot-2026-10-22/REPORT.md)保留 102 份模型對合成任務的實際輸出；30 組初始低／高對照中，只有 5 組是符合端點的候選觀察，其中 3 組信心受限；另有 28 次字數違規與三項不明確的 guardrail 評分。這些結果不能轉作新 operation 的證據。凍結的 [mapping-v2](persona-design-v0.2/mapping-v2/README.md) 與其診斷設計仍為歷史提案，不是預設路徑或新證據。原 400 回答門檻不變；[core 證據計畫](core/EVIDENCE_PLAN.md)是另立的前瞻計畫，不是替代門檻。詳見[發布驗收](docs/RELEASE_ACCEPTANCE.md)與[發布說明草稿](docs/RELEASE_NOTES_DRAFT.md)。下一個凍結診斷最多 18 份輸出，仍為 NOT RUN；先前 132 份的涵蓋提案未被採納。兩個類比是實作里程碑，不是將心理學導向的專案目標縮減成兩種人格。候選版尚未發布。

## 僅在明確要求時使用的舊流程

[v0.1 情境流程](fictional-persona-instantiation-v0.1/README.md)、[panel adapter](ephemeral-persona-panel-adapter-v0.1/README.md) 與 [Persona Pack](persona-pack-v0.1/README.md)仍可選用。多個 persona、panel 合成、持久化與交接都不是設定單一 agent 的必要步驟，也不構成 core spec 的確認。見[遷移說明](docs/MIGRATION.md)。

僅供虛構、低風險、建議性任務，最終由人判斷。禁止真人側寫、診斷、人格評分、敏感屬性推論，以及招聘、監控、法律、醫療、信用、保險、教育分配等高風險用途與自動最終決策。人格設定不得改寫準確性、隱私、安全、任務必要內容或工具權限。[安全邊界](docs/SAFETY_BOUNDARIES.md) · [架構](docs/ARCHITECTURE.md) · [貢獻](CONTRIBUTING.md) · [安全通報](SECURITY.md)

原創 repository 素材採 [Apache-2.0](LICENSE)；外部論文與第三方素材保留原權利。行銷範圍為 GitHub 文件，不需要獨立網站。
