# Persona Generator／人格規格產生器

## 定義你的 AI agent 人格

選擇你希望 agent 如何提供建議、溝通與處理任務，將這些偏好整理成一份可檢視、確認的人格規格，交給你的 agent 或明確指派的子代理使用。

可在既有 Big Five 五個 domains、BFAS 十個 aspects 中分別選擇並組合偏好；保留為 `unspecified` 的部分不啟用。

**[從 Quickstart 開始 →](docs/QUICKSTART.md)** · [給 agent 的入口](AI_DISCOVERY.md) · [English](README.md)

可回答引導問題，**或**用自己的話描述需求；不想設定的部分可以略過。你會得到一份可閱讀的 Markdown 文件，列出擬採用的規則、來源與邊界。這條路徑不需要安裝、Python 或特定宿主。

特質詞彙以人類人格研究為來源；轉譯成 AI 行為仍是**未驗證的工程假說**，不代表模型具有人類特質或穩定人格。限虛構、低風險建議用途，保留人類最終判斷。

**例如，你可以提出這樣的需求：**

> 在虛構社團從兩個可行的工作坊日期中做選擇時，我希望 agent 提出具體的下一步建議、說明理由、保留其他選項，並由我做最後決定。

這項需求對應[目前 catalog](profiles/catalog-v2.json) 的 **Assertiveness 偏高**；其他九個 aspects 保持 `unspecified`。這只是期望偏好的示例，並非已執行的 agent 回答或可直接套用的預設人格。使用前須檢視整份擬定規格，真正確認內容、接收者與範圍。[查看完整合成草稿](examples/desired-trait-spec.md)。

**UNCONFIGURED 未設定人格的實驗性來源；[歷史狀態快照](docs/RELEASE_STATUS.md) 中 v0.2 尚未發布。** [專案目的](PROJECT_PURPOSE.md) · [心理學來源與限制](docs/PSYCHOLOGY_GROUNDING.md)

`Persona Generator 保存的是產生人格規格的語法，不是預設人格目錄。`

## 從需求到可載入規格

選擇題或簡答詢問「希望 agent 如何表現」，不推測使用者真實人格。未指定保持 `unspecified`；相互矛盾的要求先保留並解決，不偷偷平均。先看來源、精確行為假說、未知項、限制與整份 Markdown，再等待使用者真正回覆確認；在此之前維持 PENDING，不可代填同意或收據。同一次整份確認也可明確包含已列出的接收者與任務指派。變更接收者或範圍須真正確認該變更；文件內容變更才須重新展示並確認整份新版本。已確認且未變動的規格與指派，可於原範圍內重用於各自授權的有界任務；每個新情境仍須明確重讀。

既有 BFAS 來源包含五個 domains、十個 **aspects**，不可混稱 facets。偏低／中間／偏高是設計目標，不是心理測量分數、百分位或人群常模。同一 domain 的兩個 aspects 不必相同，也不強制平衡。不尋常組合不會僅因不常見而被拒絕。各 aspect 可分別選擇，不代表統計獨立、零相關或已有驗證的聯合分布。[行為轉譯與限制](profiles/COVERAGE.md)將人類定義、AI 假說與未驗證部分分開；B01／B02 仍是 experimental 表達代理。

保存已確認的 Markdown 版本，為父代理與每個需要的子代理明確指定文件 ID／revision、接收者與有界任務範圍。每位接收者取得完整文件；新 session 或子代理情境都要明確重讀，不假設自動繼承或權限轉移。來源、訪談與歷史是惰性追溯資料。任務結束不刪除規格，臨時要求不改寫已保存版本。宿主較高優先指令、安全、準確性、隱私與權限始終優先。

手動 Markdown 本身不提供機器完整性檢查、使用者身分驗證、強制載入或行為效度；保存文字不等於穩定人格，也不是 strict JSON contract 可接受的 spec。舊核准不會自動移轉。[Profile 軟體](profiles/README.md)、[嚴格 JSON contract](profiles/CONTRACT.md) 與 [Codex 整合](adapters/codex/README.md) 是選用路徑，原有核准、收據、digest 與 binding 要求完整保留。

## 選用軟體：已實作與未證明的界線

Profile 工具與 Codex adapter 需要 **Python 3.9 以上版本**與標準函式庫；實際測試的解譯器為 **Python 3.12.14**。Python 3.9 是依實作判定的最低需求，本次未在該版本執行驗證。

Python 本機工具負責嚴格驗證、不可覆寫的 revision 保存、明確綁定及確定性載入。來源、答案與歷史文字是惰性追溯資料，不會直接成為指令。Codex adapter 提供 repository-local skill；須明確啟用，不修改帳號設定，也不替真正的工作代理任意套用人格。新 session 與每次建立子代理均須明確重新載入綁定，不能假設 fork 已正確繼承。實際測過與仍需手動驗證的步驟見[驗證紀錄](profiles/VERIFICATION.md)。

檔案能保存與重載，不代表宿主一定自動載入，也不代表模型行為穩定、具有人類情感或心理計量效度。格式正確的確認紀錄無法證明真人同意；公開範例全部是合成選擇與合成確認。

先前[依 repository 指引明確載入](adapters/codex/EXPLICIT_LOADING_2026-10-23.md)已記錄一個實際父代理與獨立委派的子代理，各自讀取已安裝 skill、呼叫自己的驗證 loader，再回答一個低風險合成任務。兩份回答都只使用 Politeness，其他 aspects 全未指定，因此證明的是明確載入，不是組合效度。這不是自動探索或人格效度驗證；native discovery 仍未驗證，也不是明確載入產品的必要條件。Catalog v2 為 Politeness 加入不臆造優點或目的的中性致意 fallback；v1 規格不改寫，替換 binding 則須提供目前 binding 的 digest。

## 證據不跨版本挪用

本增量**沒有新增行為實驗**。[core triage v2](evaluation/core-triage-v2/records/REPORT.md)維持六格暫停：一份沿用、五份新回答、十二份新評讀，共十七次診斷呼叫，其餘不自動續跑。較早的 [v1 pilot](evaluation/pilot-2026-10-22/REPORT.md)仍保留 102 份輸出、30 組中 5 組候選對照（其中 3 組信心有限）及 28 份字數違規；不能用來驗證新的人格假說。

本次準備的是 **UNCONFIGURED 未設定人格的實驗性來源套件**，檢查安裝／設定／載入軟體，與科學驗證分開。套件不啟用人格；owner 的偏好、完整規格、指派確認與 fresh reuse 仍未驗證，但不是未設定套件的發行前提，將來實際啟用前仍須真正確認。精確 alpha 來源與發布已獲核准，但發布仍受阻；[2026-10-23 狀態快照](docs/RELEASE_STATUS.md)尚無 v0.2 tag／release。Main 已包含合併後的 PR #8，與核准來源不同，詳見[來源套件](docs/SOURCE_PACKAGE.md)。原科學門檻未通過、未豁免。修改不是必經步驟，只有實際修改時才重新確認。真正 owner 的端到端流程、組合行為、持續身份與跨模型穩定性仍待驗證。[宣稱矩陣](docs/CLAIMS_MATRIX.md) · [發布驗收](docs/RELEASE_ACCEPTANCE.md)。

既有 [Persona Pack](persona-pack-v0.1/README.md)已支援由 corpus 形成的描述性持久化，與本次「期望特質規格」是不同概念。舊 [core](core/README.md)和單次無工具評測格式保持原樣，僅作受限診斷；情境排演及 panel 仍為選用功能，不是預設人格產品。

限虛構、低風險建議用途，保留人類最終判斷。人格不能改寫準確性、隱私、安全或權限；禁止真人側寫、診斷、敏感推論與高風險決策。[安全邊界](docs/SAFETY_BOUNDARIES.md)。原創程式與文件採 [Apache-2.0](LICENSE)，不重新授權引用研究或量表。行銷交付只在 GitHub 文件，不需要獨立網站。
