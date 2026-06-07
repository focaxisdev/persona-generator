# Persona Generator / 人格產生器

Persona Generator（人格產生器）是一套 protocol-first、Markdown-first 的 AI 多代理人格生成框架。它不儲存預製人格目錄，而是依照情境即時產生受學術邊界約束的虛構人格。

公開 tagline：

`Generate academically bounded fictional personas on demand for multi-agent rehearsal.`

核心原則：

`Persona Generator stores the grammar for generating personas, not a catalog of predefined personas.`

[Read the English README](README.md)

## 一句話說明

當你需要 AI Agent 為一個虛構、低風險情境產生幾個臨時觀點，用來做 brainstorming、風險檢查或交接演練時，Persona Generator 提供一套可檢查、可停止、可移交的 Markdown protocol。

## 這是什麼 / 不是什麼

| Persona Generator 是 | Persona Generator 不是 |
| --- | --- |
| 本地優先的 Markdown protocol 套件 | Hosted service |
| 依情境產生臨時虛構人格的 grammar | 靜態人格目錄 |
| 用於低風險演練的受限 construct vocabulary | 人格測驗或心理計量工具 |
| 需要人工審查的 advisory workflow | 診斷工具 |
| 保留異議與少數觀點的合成輔助 | 自動決策系統 |
| 可選的 Persona Pack 交接格式 | 真人側寫基礎建設 |

## 五分鐘開始

1. 讀 [docs/QUICKSTART.md](docs/QUICKSTART.md)。
2. 讓 AI Agent 讀 [AI_DISCOVERY.md](AI_DISCOVERY.md)，並只走最小必要路徑。
3. 提供一個虛構、低風險的 scenario brief。
4. 產生最小必要的 ephemeral personas（臨時虛構人格）。
5. 執行人工 review checklist。
6. 只有在任務明確需要時，才使用 panel rehearsal（多觀點合成）或 Persona Pack handoff（Markdown 交接包）。
7. 產出 bounded advisory synthesis（受限建議性合成）後停止。

複製起始 prompt：

```text
Read AI_DISCOVERY.md and docs/QUICKSTART.md. Use Persona Generator only for a fictional, low-stakes scenario. Generate the minimum useful set of ephemeral fictional personas, review them manually, preserve dissent, avoid static persona catalogs, and stop after a bounded advisory synthesis.

Scenario: [描述一個虛構、低風險情境]
Decision or rehearsal question: [臨時觀點要檢查什麼問題？]
Why this is fictional and low-stakes: [簡短說明邊界]
Desired output: [只要 personas / personas plus synthesis / optional handoff]
```

## 架構概覽

![Architecture overview](docs/assets/architecture-overview.svg)

```text
虛構低風險情境
-> 受邊界約束的 construct vocabulary
-> LLM-native on-demand ephemeral personas
-> 人工審查
-> 可選 panel rehearsal
-> 保留異議的 advisory synthesis
-> 可選 Persona Pack v0.1 serialization
-> 可選 handoff
-> stop
```

## 公開範例

請看 [examples/limited-public-beta](examples/limited-public-beta/README.md)。這是一個虛構的志工知識分享場景，示範多個臨時人格、可見異議、少數觀點保留，以及受限的建議性合成。

範例只是 public fixture：用來示範格式與安全邊界，不是資料集、runtime inventory、可重用 preset，也不是靜態人格目錄。

## 安全邊界

Persona Generator 預設只用於虛構、低風險、建議性情境。不要用於真人側寫、診斷、心理計量評分、招聘、監控、法律、醫療、信用、保險、教育分配或其他高風險決策。

使用前請讀 [docs/SAFETY_BOUNDARIES.md](docs/SAFETY_BOUNDARIES.md)。

## 學術邊界與證據限制

這裡的 construct 只是受邊界約束的描述詞彙，用來幫助情境設計；它不是心理測量、臨床驗證、診斷、人格真相或行為預測。

請讀 [docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md) 與 [docs/EVIDENCE_SUMMARY.md](docs/EVIDENCE_SUMMARY.md)。

## 文件導覽

- [Quickstart](docs/QUICKSTART.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Academic Boundaries and Source Notes](docs/ACADEMIC_BOUNDARIES_AND_SOURCE_NOTES.md)
- [Why Persona Generator](docs/WHY_PERSONA_GENERATOR.md)
- [Use Cases](docs/USE_CASES.md)
- [FAQ](docs/FAQ.md)
- [Safety Boundaries](docs/SAFETY_BOUNDARIES.md)
- [AI Discovery Guide](AI_DISCOVERY.md)
- [Experimental llms.txt](llms.txt)

## Contributing

貢獻前請讀 [CONTRIBUTING.md](CONTRIBUTING.md)、[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md) 與 [SUPPORT.md](SUPPORT.md)。

請不要提交個人資料、敏感資料、秘密側寫需求、靜態人格目錄、心理計量評分或高風險使用案例。

## License

Persona Generator 使用 [Apache-2.0](LICENSE) 授權。除非個別檔案另有說明，授權範圍包含本公開 repository 的文件、protocols、templates、examples、visual assets，以及未來程式碼。

## Star

如果這種 protocol-first 的做法對你有幫助，歡迎 Star 這個 repository，讓更多 builders 找得到它。
