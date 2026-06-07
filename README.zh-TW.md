# 人格產生器

`人格產生器`是一套 protocol-first、Markdown-first 的 AI 多代理人格生成框架。它不儲存預製人格目錄，而是依照情境即時產生受學術定義約束的虛構人格。

英文名稱：`Persona Generator`

公開 tagline：

`Generate academically bounded fictional personas on demand for multi-agent rehearsal.`

核心原則：

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

## 這是什麼

- 本地優先的 Markdown protocol 套件。
- 用於虛構、低風險情境。
- 協助 AI Agent 依照當前情境產生最小必要的臨時虛構人格。
- 保留不確定性、反對意見與人工最終判斷。
- 需要持久化或交接時，可選擇 Persona Pack v0.1。

## 這不是什麼

- 不是人格測驗。
- 不是心理計量工具。
- 不是真人側寫工具。
- 不是診斷工具。
- 不是監控、招聘、醫療、法律、信用、保險或教育分配工具。
- 不是自動決策系統。
- 不是靜態人格目錄。

## 最短使用路徑

1. 閱讀 [docs/QUICKSTART.md](docs/QUICKSTART.md)。
2. 讓 AI Agent 閱讀 [AI_DISCOVERY.md](AI_DISCOVERY.md) 或 [AGENTS.md](AGENTS.md)。
3. 提供一個虛構、低風險情境。
4. 產生最小必要的臨時虛構人格。
5. 執行人工審查。
6. 視需要使用 panel rehearsal 或 Persona Pack handoff。
7. 在 bounded advisory synthesis 後停止。

## 安全邊界

所有使用都必須維持在虛構、低風險、建議性場景內。請先閱讀 [docs/SAFETY_BOUNDARIES.md](docs/SAFETY_BOUNDARIES.md)。
