# Persona Generator／人格規格產生器

**為 agent 與子代理設計可追溯、可組合的人格規格。** 選擇希望 agent 表現的特質組合，檢查心理學來源與工程轉譯，確認完整規格，再於新任務載入同一個明確版本。

目前是**尚未發布的候選版**。十個 BFAS aspects 有版本化的設定與指令語義，不等於模型已實現十種人類心理特質。[English](README.md) · [專案目的與驗收](PROJECT_PURPOSE.md)

**可選擇題或自由文字，也可略過：**[owner 入門](profiles/ONBOARDING.md) · [父／選用子代理指派與回復](profiles/ASSIGNMENTS.md) · [心理學定義與排除範圍](docs/PSYCHOLOGY_GROUNDING.md)。

**開始使用：**[Quickstart](docs/QUICKSTART.md) → [持久人格規格](profiles/README.md) → [Codex 安裝方式](adapters/codex/README.md)。

## 從需求到可載入規格

選擇題或簡答詢問「希望 agent 如何表現」，不推測使用者真實人格。未指定保持 `unspecified`；相互矛盾的要求先保留並解決，不偷偷平均。先看來源、精確行為假說、未知項、限制與完整 preview，再由真正的 owner 確認；修改後必須建立新 revision 並重新確認。

既有 BFAS 來源包含五個 domains、十個 **aspects**，不可混稱 facets。偏低／中間／偏高是設計目標，不是心理測量分數、百分位或人群常模。同一 domain 的兩個 aspects 不必相同，也不強制平衡。不尋常組合不會僅因不常見而被拒絕。各 aspect 可分別選擇，不代表統計獨立、零相關或已有驗證的聯合分布。[行為轉譯與限制](profiles/COVERAGE.md)將人類定義、AI 假說與未驗證部分分開；B01／B02 仍是 experimental 表達代理。

本機 store 保存完整確認過的版本；父代理與每個子代理各自綁定 profile ID、revision 與 digest，可共用或不同。子代理的修改不會自動改動父代理。任務結束不刪除人格規格；臨時任務要求也不改寫持久 profile。角色、能力、價值／目標、暫時狀態與工具權限是另外的設定，不能混成人格滑桿。

## 已實作與未證明的界線

Python 本機工具負責嚴格驗證、不可覆寫的 revision 保存、明確綁定及確定性載入。來源、答案與歷史文字是惰性追溯資料，不會直接成為指令。Codex adapter 提供 repository-local skill；須明確啟用，不修改帳號設定，也不替真正的工作代理任意套用人格。新 session 與每次建立子代理均須明確重新載入綁定，不能假設 fork 已正確繼承。實際測過與仍需手動驗證的步驟見[驗證紀錄](profiles/VERIFICATION.md)。

檔案能保存與重載，不代表宿主一定自動載入，也不代表模型行為穩定、具有人類情感或心理計量效度。格式正確的確認紀錄無法證明真人同意；公開範例全部是合成選擇與合成確認。

先前[依 repository 指引明確載入](adapters/codex/EXPLICIT_LOADING_2026-10-23.md)已記錄一個實際父代理與獨立委派的子代理，各自讀取已安裝 skill、呼叫自己的驗證 loader，再回答一個低風險合成任務。兩份回答都只使用 Politeness，其他 aspects 全未指定，因此證明的是明確載入，不是組合效度。這不是自動探索或人格效度驗證；native discovery 仍未驗證，也不是明確載入產品的必要條件。Catalog v2 為 Politeness 加入不臆造優點或目的的中性致意 fallback；v1 規格不改寫，替換 binding 則須提供目前 binding 的 digest。

## 證據不跨版本挪用

本增量**沒有新增行為實驗**。[core triage v2](evaluation/core-triage-v2/records/REPORT.md)維持六格暫停：一份沿用、五份新回答、十二份新評讀，共十七次診斷呼叫，其餘不自動續跑。較早的 [v1 pilot](evaluation/pilot-2026-10-22/REPORT.md)仍保留 102 份輸出、30 組中 5 組候選對照（其中 3 組信心有限）及 28 份字數違規；不能用來驗證新的人格假說。

另提出「實驗性套件」驗收，檢查安裝／設定／載入的可用性，與科學驗證分開；仍待真正 owner 私下確認偏好、完整規格、指派與 fresh reuse，以及協調者採納範圍和審查。原科學門檻未通過、未豁免。修改不是必經步驟，只有實際修改時才重新確認。真正 owner 的端到端流程、組合行為、持續身份與跨模型穩定性仍待驗證。[宣稱矩陣](docs/CLAIMS_MATRIX.md) · [發布驗收](docs/RELEASE_ACCEPTANCE.md)。

既有 [Persona Pack](persona-pack-v0.1/README.md)已支援由 corpus 形成的描述性持久化，與本次「期望特質規格」是不同概念。舊 [core](core/README.md)和單次無工具評測格式保持原樣，僅作受限診斷；情境排演及 panel 仍為選用功能，不是預設人格產品。

限虛構、低風險建議用途，保留人類最終判斷。人格不能改寫準確性、隱私、安全或權限；禁止真人側寫、診斷、敏感推論與高風險決策。[安全邊界](docs/SAFETY_BOUNDARIES.md)。原創程式與文件採 [Apache-2.0](LICENSE)，不重新授權引用研究或量表。行銷交付只在 GitHub 文件，不需要獨立網站。
