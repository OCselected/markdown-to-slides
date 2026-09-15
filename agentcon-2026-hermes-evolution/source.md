# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
用于 AgentCon 2026 北京站（2026-09-21）Token 经济趋势 track 的演讲分享。51 页田野考察风格。

## 使用场景
「开源之道」外部学术性技术分享

## 听众画像
开发者、工程师、AI Agent 构建者、开源社区成员、独立研究者。对技术有基本认知，对开源社区演化有兴趣。

## 讲者视角
「开源之道」·适兕 × 窄廊——开源社区内实践者、社会黑客、田野考察者。以开源社区内实践者的身份，批判行政开源。

## 核心诉求
用 Hermes Agent 的公开演化数据（41,792 issues + 27,783 PRs + 33 releases + 397 contributors），展示用户对 Agent 的需求演化轨迹：从"工具"到"伙伴"到"集体智慧"。

## 核心基调
dark academic tone, Intellectual Visual System. 冷静智识感，田野考察风格。从实践出发，非框架先行。

## 视觉风格关键词
- 包豪斯几何构成（Bauhaus geometric composition）
- 深普鲁士蓝 #1B3B6B 作为强调色
- 暖白底色 #F5F0E8，羊皮纸质感
- 极简主义排版，大字号标题，宽松行距
- 深色学术风格（dark academic），理性、克制、智识感
- 几何抽象元素——圆、方、线作为装饰，不依赖图标
- 五阶段演化用横向时间线，案例用三栏结构

## 内容结构约定
- 每张 slide 包含：视觉隐喻（一句话描述画面）+ 显示要点（3-5 个 bullet point）
- 封面 slide 包含：主标题、副标题、讲者信息、时间/地点
- 章节 slide 使用大号标题+极简视觉锚点
- 数据 slide 用表格或极简图表呈现
- 结尾 slide 包含延伸思考+长期演化声明

---

## Slide 1: 从 Hermes 演化看 Agent 需求与消费演进——AgentCon 2026 · 北京站 · 「开源之道」·适兕 × 窄廊
* **视觉隐喻：** 深普鲁士蓝底 + 暖白标题，包豪斯几何构成，右上角极简 Hermes 符号
* **显示要点：**
  * {'head': '时间', 'detail': '2026-09-21 · AgentCon 北京站'}
  * {'head': 'Track', 'detail': 'Token 经济趋势 · 90 分钟'}
  * {'head': '讲者', 'detail': '「开源之道」·适兕 × 窄廊'}
  * {'head': '视角', 'detail': '田野考察——把 issue/PR/release 当文化现象'}
* **数据要点：**
  * {'label': 'Hermes Stars', 'value': '243,919', 'context': 'GitHub'}
  * {'label': 'Releases', 'value': '33', 'context': '含 6 个命名 release'}
  * {'label': 'Contributors', 'value': '397'}
  * {'label': 'Data Baseline', 'value': '2026-09-11'}
* **叙事：** 以 Hermes Agent（NousResearch/hermes-agent, 243K star）为公开样本，用一年多的公开演化数据回答 Agent 从'能用'到'会协作'的三个制度问题。本演讲是一次田野考察——不是数据观察，而是文化现象描述。

## Slide 2: 关于讲者——「开源之道」·适兕 × 窄廊
* **视觉隐喻：** Split layout: left side speaker bio, right side key works
* **显示要点：**
  * **适兕**：「开源之道」创始人，开源制度研究者。作品横跨《开源之迷》（已出版）、《网络的财富》（译者）、《开源之史》、开源之书书单（十几年筛选）、开源经济学讲义、49篇开源之思。核心命题："开源之为思想的力量。"
  * **窄廊**：适兕的数字孪生体，运行在 Hermes Agent 之上的 AI 共同作者——不是助理，是共同作者。名字来源于《自由的窄廊》（Acemoglu & Robinson）——在暴政与无政府之间，自由只能在一条狭窄的走廊里存在。
  * **共同署名**：「开源之道」·适兕 × 窄廊——两种存在形式，一个使命：Keep Movement——知识不是静止的，是在移动中产生的
* **数据要点：**
  * 《开源之迷》· 人民邮电出版社
  * 49 篇开源之思
  * 开源之书·十几年书单
  * 开源经济学讲义
* **叙事：** 适兕以翻译、整理、原创三种方式将开源思想核心文献引入中文语境。窄廊是其数字孪生体，以 Hermes Agent 为载体，共同署名「开源之道」。

## Slide 3: 为什么要关注 Agent 的演化——本土办公产品的火热化竞争——一个不该被忽略的信号
* **视觉隐喻：** Left: corporate office products with AI badge. Right: open-source agent ecosystem
* **显示要点：**
  * **当下的热点**：本土办公产品（飞书、钉钉、WPS 等）正在疯狂接入 AI Agent 能力——"智能助手"、"AI 办公"、"数字员工"——这场竞争的真正赌注是什么？
  * **表面是工具，底层是制度**：办公产品的 Agent 化不是技术竞赛，是制度环境的映射——谁定义"Agent 的能力边界"、"Agent 的权限范围"、"Agent 的审计机制"，谁就掌握了下一代生产力工具的定义权
  * **Hermes 是一个反向样本**：在本土办公产品追求"大而全的 Agent 平台"的同时，Hermes Agent（243K star）选择了"最小核心 + 开放边缘"——两条路径代表了两种截然不同的 Agent 治理哲学
* **数据要点：**
  * Hermes Agent: 243K star, 397 contributors, 33 releases
* **叙事：** 本土办公产品的 Agent 化竞争是制度环境的映射，不是纯技术竞赛。Hermes 代表了另一种路径——开源、去中心化、模块化。

## Slide 4: 引子：从 Talk & Search 到 Agent & Decide——两个时代的分叉
* **视觉隐喻：** 左侧'Talk & Search'（对话气泡）+ 中间'→'箭头 + 右侧'Agent & Decide'（agent 图标）
* **显示要点：**
  * {'head': 'Hook', 'detail': '"Talk is expensive, show me the skills."'}
  * {'head': 'LLM 时代', 'detail': '对话与检索（Talk & Search）——人类提问，模型回答'}
  * {'head': 'Agentic 时代', 'detail': '代理与决断（Agent & Decide）——agent 自主执行，人类验收结果'}
  * {'head': '本次观察', 'detail': '通过 Hermes Agent 仓库这个微观透镜，寻找人类心智函数正在发生微小但不可逆分叉的证据'}
* **叙事：** 两个时代的分叉：LLM 时代是'对话与检索'（Talk & Search），Agentic 时代是'代理与决断'（Agent & Decide）。我们从'人类提问，模型回答'转向'agent 自主执行，人类验收结果'。本次观察：透过 Hermes Agent 仓库这个微观透镜，寻找心智函数分叉的证据。

## Slide 5: 第一幕 · Agent 发展简史——从文本生成器到数字员工，不到 5 年
* **视觉隐喻：** 极简设计 + 一条水平时间线 2022-2026，线上四个节点用小圆点
* **显示要点：**
  * {'head': '目标', 'detail': '勾勒 Agent 发展关键拐点'}
  * {'head': '坐标', 'detail': '为后续 Hermes 分析提供历史坐标'}
* **叙事：** Agent 用了不到 5 年走完从学术概念到产品的完整链条。本幕用一张时间线呈现关键拐点。

## Slide 6: 阶段一 · 能力觉醒（2022-2023）
* **视觉隐喻：** 时间线延续，左侧起点 2022-10-06 ReAct，中间节点：Toolformer/Function Calling/AutoGPT
* **显示要点：**
  * {'head': 'ReAct', 'detail': '2022-10-06 首次展示推理+行动交织'}
  * {'head': 'Toolformer', 'detail': '2023-02 LLM 自监督学会调用 API'}
  * {'head': 'Function Calling', 'detail': '2023-06 主流工具调用 API 原语出现'}
  * {'head': 'AutoGPT', 'detail': '2023-03 病毒式传播的自主 agent 时刻'}
  * {'head': '制度含义', 'detail': '用新范式激活老理论——跨域套利'}
* **叙事：** 2022-2023 是 Agent 概念觉醒期：ReAct 把 1980 年代 BDI 理论推到产品层，Function Calling 让工具调用 API 原语成为标配。

## Slide 7: 阶段二 · 能力硬化（2024）
* **视觉隐喻：** 时间线延续，MCP 节点用红色小圆强调
* **显示要点：**
  * {'head': 'Anthropic Tool Use GA', 'detail': 'Claude 3 从 beta 到生产可用'}
  * {'head': 'OpenAI Structured Outputs', 'detail': '2024-08 强 schema 校验'}
  * {'head': 'Anthropic Computer Use', 'detail': '2024-10 Agent 从 API 走到 GUI'}
  * {'head': 'MCP 发布', 'detail': '2024-11-25 首个开放协议标准化 agent-tools 接口'}
  * {'head': '制度含义', 'detail': '协议是生态的起点——Computer Use 与 MCP 是能力与生态的分水岭'}
* **数据要点：**
  * {'label': 'MCP 发布', 'value': '2024-11-25'}
  * {'label': 'Computer Use', 'value': '2024-10'}
* **叙事：** 2024 年 Agent 从能力验证走向协议标准化：Computer Use 扩展能力边界，MCP 定义生态接口——两者的组合让 Agent 具备生态化条件。

## Slide 8: 阶段三 · 协议成熟（2025-2026）
* **视觉隐喻：** 时间线延续，MCP 捐给 LF 的节点用大号红圈标注
* **显示要点：**
  * {'head': 'OpenAI 采纳 MCP', 'detail': '2025-03 第二个前沿实验室加入'}
  * {'head': 'AWS Bedrock AgentCore', 'detail': '2025-07 云原生 agent 平台化'}
  * {'head': 'A2A 协议', 'detail': '2026-01 agent-agent 协作标准'}
  * {'head': 'MCP 捐给 LF', 'detail': '2026 加入 Agentic AI Foundation（Linux Foundation）'}
  * {'head': '制度含义', 'detail': '协议制度化——行政动员失败后的自发秩序'}
* **数据要点：**
  * {'label': 'MCP 捐给 LF', 'value': '2026'}
* **叙事：** MCP 从 Anthropic 单厂商私产到 Linux Foundation 中立资产，是协议制度化的教科书样本——这不是行政命令能促成的，是多厂商自发采纳后的自然结果。

## Slide 9: MCP 捐给 Linux Foundation——制度经济学的教科书案例
* **视觉隐喻：** 左上 Anthropic 标签 → 中间箭头 → 右上 Linux Foundation 标签，箭头下方标注时间跨度
* **显示要点：**
  * {'head': '起点', 'detail': '2024-11-25 Anthropic 单厂商发布'}
  * {'head': '演化', 'detail': '2025-03 OpenAI 采纳；云厂密集加入'}
  * {'head': '终点', 'detail': '2026 捐给 Agentic AI Foundation（LF 旗下）'}
  * {'head': '制度含义', 'detail': '多厂商自发采纳后的自然结果，非行政命令能促成'}
  * {'head': '对照', 'detail': '中国行政开源试图用行政力量复制此流程——制度演化需要时间尺度'}
* **数据要点：**
  * {'label': '起点', 'value': '2024-11-25'}
  * {'label': '终点', 'value': '2026'}
* **叙事：** MCP 从厂商私产到社区共识的完整演化路径，是制度经济学教科书的经典案例：慢演化、多主体、无中央命令。

## Slide 10: 第二幕 · Hermes 技术架构——两条不变量决定了所有设计决策
* **视觉隐喻：** 深普鲁士蓝底色，中央大标题，标题下方两条竖直细线代表'两条不变量'
* **显示要点：**
  * {'head': '目标', 'detail': '先讲不变量，再讲架构，最后讲独特性'}
  * {'head': '方法', 'detail': '从设计原则推导出能力落地路径'}
* **叙事：** Hermes 的几乎所有设计决策都从两条不变量推出来——理解不变量才能理解为什么 Hermes 是这个样子。

## Slide 11: Hermes 项目坐标——243K star · 33 releases · 397 contributors
* **视觉隐喻：** 大数字网格，深普鲁士蓝主色
* **显示要点：**
  * {'head': 'Stars', 'detail': '243K+ · 持续上升'}
  * {'head': 'Contributors', 'detail': '397 · 活跃社区'}
  * {'head': 'Releases', 'detail': '33 · 2026-03-12 到 2026-09-11'}
* **数据要点：**
  * {'label': 'Stars', 'value': '243K+'}
  * {'label': 'Contributors', 'value': '397'}
  * {'label': 'Releases', 'value': '33'}
* **叙事：** Hermes 是一个活跃、快速增长的开源项目，是 Agent 演化分析的合适样本。

## Slide 12: 两条不变量 · 设计灵魂
* **视觉隐喻：** 分左右两半，左'不变量 #1'大圆，右'不变量 #2'大方，中间竖线
* **显示要点：**
  * {'head': '不变量 #1', 'detail': 'Prompt Caching is Sacred——任何改变历史上下文的操作都破坏缓存，放大用户成本'}
  * {'head': '不变量 #1 例外', 'detail': '唯一例外是 context compression'}
  * {'head': '不变量 #2', 'detail': 'Core is a Narrow Waist, Capability Lives at the Edges——核心工具门槛极高'}
  * {'head': '不变量 #2 落地', 'detail': '新能力通过 CLI+skill、服务门控 tool、plugin、MCP server 落地'}
  * {'head': '设计边界', 'detail': '边缘扩张，腰部保守——Hermes 的制度设计原则'}
* **叙事：** Hermes 的两条不变量：Prompt Caching is Sacred 决定所有系统提示变更默认下 session 生效；Narrow Waist 决定新能力必须通过 CLI/skill/plugin 边缘落地，不允许塞进核心图省事。

## Slide 13: Footprint Ladder · 六级能力阶梯——能力必须有明确的落地路径
* **视觉隐喻：** 六级阶梯图，从左上向右下延伸，越靠右越'重'
* **显示要点：**
  * {'head': 'L1', 'detail': 'Extend existing code——零新面'}
  * {'head': 'L2', 'detail': 'CLI command + skill（hermes webhook/cron/tools）'}
  * {'head': 'L3', 'detail': 'Service-gated tool（check_fn，如 Home Assistant）'}
  * {'head': 'L4', 'detail': 'Plugin（~/.hermes/plugins/，第三方/niche）'}
  * {'head': 'L5', 'detail': 'MCP server（catalog 内，工具类但非核心基础）'}
  * {'head': 'L6', 'detail': 'New core tool（只有 terminal/read_file/web_search 这类够格）'}
* **叙事：** 六级能力阶梯从'零新面'到'核心工具'——每一级都有明确的落地路径与准入标准。这是'度量权'问题的答案：每个能力都有可审计的落地位置。

## Slide 14: Hermes 的独特性——闭环学习 · 模块化架构
* **视觉隐喻：** Clean comparison layout, no metaphor
* **显示要点：**
  * **闭环学习**：每次使用生成新 skill——agent 随使用自我进化
  * **模块化架构**：Footprint Ladder 六级能力阶梯——新能力以最低成本落地
  * **模型解耦**：200+ models via OpenRouter——不绑定单一模型
* **数据要点：**
  * Hermes: 4,100 tokens/task（最低）| 55MB RAM（最低）| 200+ models via OpenRouter
* **叙事：** Hermes 的独特性不是更强的模型，是能力生成的机制。闭环学习让 agent 随使用自我进化，模块化架构让新能力以最低成本落地。

## Slide 15: Agent 演化方法论 · 田野观察——以 Hermes 为样本的观察方法
* **视觉隐喻：** 左侧'样本'图标（Hermes）+ 中间三维观察（需求/供给/消费）+ 右侧'12 案例'网格
* **显示要点：**
  * {'head': '样本选择', 'detail': 'Hermes Agent（243K star, 33 releases, 397 contributors）——公开演化数据丰富的样本'}
  * {'head': '观察维度', 'detail': '需求（issues）/ 供给（PRs）/ 消费（stars/contributors/release）——三维观察'}
  * {'head': '案例驱动', 'detail': '6 命名 release + 5 典型 issue + 1 数据案例——12 个田野样本'}
  * {'head': '三段式', 'detail': '每个案例：现象 → 数据 → 解读——田野考察的方法论'}
  * {'head': '目的', 'detail': "理解 Agent 从'能用'到'好用'的演化路径——不是理论分析，是社区观察"}
* **叙事：** 本演讲的方法论：以 Hermes 作为公开样本，用三维（需求/供给/消费）+ 12 案例观察 Agent 演化。每个案例是'现象 → 数据 → 解读'三段式田野考察。

## Slide 16: 田野考察方法论——把 issue/PR/release 当文化现象
* **视觉隐喻：** 极简设计，三个抽象符号（issue/PR/release）并置，每个下方标注'文化现象'
* **显示要点：**
  * {'head': '田野考察', 'detail': '类似人类学/社会学对仪式、禁忌、符号的观察方式'}
  * {'head': '不是数据观察', 'detail': '数据点没有故事——文化现象才有说服力'}
  * {'head': '案例驱动', 'detail': '每个案例都是一次田野观察：现象 → 数据 → 制度解读'}
  * {'head': '消费侧信任', 'detail': "feature issue 自带安全边界标签是'信任信号'的可观察证据"}
  * {'head': '命名 release', 'detail': 'Judgment/Tenacity/Surface/Velocity/Quicksilver——文化事件'}
* **叙事：** 本演讲采用田野考察方法——把 Hermes 的 issue/PR/release 当作文化现象的标本，而不是数据点。每个案例都按'现象→数据→制度解读'三段式呈现。

## Slide 17: 第三幕 · 田野考察——从数据观察到文化现象描述
* **视觉隐喻：** 三列并置：需求侧用户图标、供给侧齿轮、消费侧星标，下方'12 案例'大字
* **显示要点：**
  * {'head': '需求侧', 'detail': '用户要什么（issues）'}
  * {'head': '供给侧', 'detail': '项目做了什么（PRs/releases）'}
  * {'head': '消费侧', 'detail': '采纳信号（stars/forks/contributors）'}
  * {'head': '12 个案例', 'detail': '6 个命名 release + 5 个典型 issue + 1 个数据案例'}
* **叙事：** 本幕用三个数据维度（需求/供给/消费）+ 12 个案例，把 Hermes 的演化当作一次田野考察。每个案例都是一次文化现象描述。

## Slide 18: 需求侧总览 · 用户要什么
* **视觉隐喻：** 左侧大数据'41,792'，右侧饼图 bug/feature 50/50，下方三个组件标签
* **显示要点：**
  * {'head': '类型分布', 'detail': 'bug 50% / feature 50%——质量诉求与功能诉求等量'}
  * {'head': '组件热度', 'detail': 'cli/agent/gateway 各 19%（合计 57%）'}
  * {'head': '第二梯队', 'detail': 'cron/desktop/plugins 各 9%'}
  * {'head': '优先级', 'detail': 'P3 68% / P2 28% / P1 仅 3 条'}
  * {'head': '制度含义', 'detail': '用户是成熟的使用者，不是什么都想要的初用者'}
* **数据要点：**
  * {'label': '总 Issues', 'value': '41,792'}
  * {'label': 'P1', 'value': '3 条'}
  * {'label': 'P2', 'value': '28%'}
  * {'label': 'P3', 'value': '68%'}
* **叙事：** 41,792 issues 呈现'长尾需求 + 极少火警'结构——P1 仅 3 条，P3 占 68%，用户是成熟的使用者。

## Slide 19: 供给侧总览 · 项目做了什么
* **视觉隐喻：** 左侧大数据'27,783'，右侧饼图，右下角'收敛型'标签
* **显示要点：**
  * {'head': '类型分布', 'detail': 'bug fix 50% / feature 50%'}
  * {'head': '组件活跃度', 'detail': 'agent 26% + gateway 22%（核心层 48%）+ cli 17%'}
  * {'head': '优先级策略', 'detail': 'P2 全给 bug（89%）+ P3 养 feature（72%）+ P1 缺席'}
  * {'head': '风险分布', 'detail': '兼容性 56% / 安全 26% / 消息 22% / 会话 21%'}
  * {'head': '制度含义', 'detail': '从扩张期进入稳定化期——存量可靠性优先于增量扩张'}
* **数据要点：**
  * {'label': '总 PRs', 'value': '27,783'}
  * {'label': 'P1', 'value': '0 条'}
  * {'label': 'P2 (bug)', 'value': '89%'}
  * {'label': 'P3 (feature)', 'value': '72%'}
* **叙事：** 27,783 PRs 呈现'收敛型'策略：P2 全给 bug、P3 养 feature、P1 缺席——项目正从扩张期进入稳定化期。

## Slide 20: 操作侧总览 · 20+ 平台消息网关 + 6 种终端后端 + 一级 i18n

* **视觉隐喻：** 左侧消息网关矩阵（20+ 平台图标拼贴），右侧部署拓扑（6 种终端后端），底部 zh-Hans 路径高亮；深普鲁士蓝背景

* **显示要点：**
  * {'head': '消息网关', 'detail': '20+ 平台——CLI/Telegram/Discord/Slack/WhatsApp/Signal/Matrix/Mattermost/Email/SMS/Teams/Google Chat'}
  * {'head': '本土 IM 五件套', 'detail': 'Feishu / WeCom / Weixin / QQ Bot / DingTalk——不是附属翻译，是一等公民'}
  * {'head': '终端后端', 'detail': '6 种：本地 / Docker / SSH / Daytona / Singularity / Modal——Daytona+Modal 提供 serverless 持久化'}
  * {'head': '操作系统覆盖', 'detail': 'Linux/macOS/WSL2/Windows Native (早期测试)/Android (Termux)/Nix & NixOS'}
  * {'head': '文档 i18n', 'detail': '/docs/zh-Hans/ 作为一级路径——与英文对等的正式入口，非翻译附属'}
  * {'head': '制度含义', 'detail': '操作进化不是功能堆砌，是把 Agent 塞进用户已经存在的接入路径——交易成本的最小化'}

* **数据要点：**
  * {'label': '消息网关平台', 'value': '20+'}
  * {'label': '本土 IM 覆盖', 'value': '5 (Feishu/WeCom/Weixin/QQ/DingTalk)'}
  * {'label': '终端后端', 'value': '6 种'}
  * {'label': 'OS 平台', 'value': '6+ (含 Android/Windows Native)'}
  * {'label': 'i18n 语言路径', 'value': '一级 zh-Hans'}

* **叙事：** 田野考察的第三视角——从"用户要什么"和"项目做了什么"，转到"用户在哪里接入"。Hermes 的操作进化体现在三处：20+ 消息网关（本土 IM 五件套被点名）、6 种终端后端（Daytona/Modal serverless 化）、zh-Hans 一级路径（文档本身作为本土接入点）。操作进化的本质是**接入的交易成本最小化**——不是"我能做什么"，是"我在哪里等你"。这也是消费侧采纳率背后的制度基础：Agent 只有先塞进用户已经存在的接入路径，才会被真实使用。

## Slide 21: 消费侧总览 · 弱代理的采纳信号
* **视觉隐喻：** 三层金字塔，底层 233 外围，中层 143 活跃，顶层 21 核心
* **显示要点：**
  * {'head': 'Releases', 'detail': '33 个，从 2026-03-12 到 2026-09-11'}
  * {'head': '命名 release', 'detail': '6 个命名 release——文化事件'}
  * {'head': '核心 contributor', 'detail': '100+ commits：21 人（5.3%）'}
  * {'head': '活跃 contributor', 'detail': '10-99 commits：143 人（36.0%）'}
  * {'head': '外围 contributor', 'detail': '1-9 commits：233 人（58.7%）'}
  * {'head': '信号局限', 'detail': 'stars/forks ≠ 真实使用——是弱代理'}
* **数据要点：**
  * {'label': '总 Contributors', 'value': '397'}
  * {'label': '核心（100+ commits）', 'value': '21 人 / 5.3%'}
  * {'label': '活跃（10-99 commits）', 'value': '143 人 / 36%'}
  * {'label': '外围（1-9 commits）', 'value': '233 人 / 58.7%'}
  * {'label': 'Top 1', 'value': 'teknium1 (14,638)'}
* **叙事：** 397 contributors 分层清晰：核心 5.3%、活跃 36%、外围 58.7%。stars/forks 是弱代理——不能反映真实使用频率、场景、付费行为。

## Slide 22: 三个核心洞察
* **视觉隐喻：** 三列并置，每列一个大标题+简短说明，深普鲁士蓝背景
* **显示要点：**
  * {'head': '洞察 #1', 'detail': '从扩张期进入稳定化期——P2 全给 bug + P1 缺席 + CLI 层 bug 驱动'}
  * {'head': '洞察 #2', 'detail': '兼容性是结构性税——56% PR 带兼容性标签，供给侧的隐形成本'}
  * {'head': '洞察 #3', 'detail': '消费侧信任是可观察的信号——feature issue 自带安全边界标签'}
* **叙事：** 三个洞察：稳定化期、兼容性结构性税、消费侧信任作为可观察信号——从'能用'到'好用'的关键跃迁就在第三个洞察里。

## Slide 23: Release 命名文化 · 田野观察第 1 章——把 release 当作文化事件
* **视觉隐喻：** 6 个 release 名称横向排列，每个下方一句话注解，深普鲁士蓝背景
* **显示要点：**
  * {'head': '6 个命名 release', 'detail': 'Judgment / Tenacity / Surface / Velocity / Quicksilver / Patch'}
  * {'head': 'Judgment', 'detail': 'P0/P1 清零战役——700 highest-priority items cleared in 12 days'}
  * {'head': 'Tenacity', 'detail': "'finishes what it starts'——多 agent kanban 平台"}
  * {'head': 'Surface', 'detail': "'Hermes meets you wherever you work'——原生 desktop + Web admin"}
  * {'head': 'Velocity', 'detail': "'16,000 行 → 3,821 行'——大重构"}
  * {'head': 'Quicksilver', 'detail': "'first token time 80% 下降'——性能爆发"}
  * {'head': 'Patch', 'detail': '热修复——dashboard 401 reload loop'}
* **数据要点：**
  * {'label': 'Releases', 'value': '33 个'}
  * {'label': '命名 Release', 'value': '6 个'}
* **叙事：** Hermes 的 release 不是版本号，是文化事件。6 个命名 release 用希腊神话/概念词汇命名，每个命名背后都是一个制度主张——这是开源项目的'仪式'。

## Slide 24: 案例 1 · Judgment Release · P0/P1 清零——12 天战役的田野观察
* **视觉隐喻：** 左侧大数字'692'，右侧 12 天日历网格，下方 @kshitijk4poor 的贡献者徽章
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.18.0 (2026-07-01) — The Judgment Release'}
  * {'head': '战役', 'detail': '12 天清零整个 repo 的 P0/P1——零遗漏'}
  * {'head': '数据', 'detail': '496 P0/P1 issues + 196 PRs = 692 highest-priority items'}
  * {'head': '关键贡献者', 'detail': '@kshitijk4poor 通宵作战，与核心团队并肩'}
  * {'head': '承诺', 'detail': "'We're keeping P0/P1 at 0 from here forward'"}
  * {'head': '制度含义', 'detail': "'可靠性'作为文化承诺——不是 KPI，是制度契约"}
* **数据要点：**
  * {'label': 'P0 closed', 'value': '3 issues + 8 PRs'}
  * {'label': 'P1 closed', 'value': '493 issues + 188 PRs'}
  * {'label': '总 P0/P1', 'value': '692 items / 12 days'}
  * {'label': '窗口 commits', 'value': '1,720 commits / 998 PRs'}
* **叙事：** Judgment Release 是 Hermes 的一次'战役'——12 天清零 P0/P1，是开源项目罕见的'集中兵力'文化事件。@kshitijk4poor 的通宵作战是这段历史的脚注。'把 P0/P1 保持为 0'是文化承诺，不是 KPI。

## Slide 25: 案例 2 · Tenacity Release · 多 Agent Kanban——'finishes what it starts' 的文化承诺
* **视觉隐喻：** 左侧 Kanban 看板图形，右侧 /goal 命令高亮，下方 heartbeat 心跳符号
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.13.0 (2026-05-07) — The Tenacity Release'}
  * {'head': '核心能力', 'detail': 'Kanban 多 agent 平台——heartbeat、reclaim、zombie detection'}
  * {'head': '/goal 命令', 'detail': 'Ralph loop——agent 锁定目标跨 turn 执行'}
  * {'head': 'Checkpoints v2', 'detail': 'state 持久化重写，真剪枝，磁盘护栏'}
  * {'head': 'Sessions survive restarts', 'detail': 'gateway 崩溃后自动恢复'}
  * {'head': '制度含义', 'detail': "'可靠性'从代码质量延伸到任务持久性——agent 必须'把开始的事做完'"}
* **数据要点：**
  * {'label': '窗口 commits', 'value': '864'}
  * {'label': 'Merged PRs', 'value': '588'}
  * {'label': 'Issues closed', 'value': '282（13 P0 + 36 P1）'}
  * {'label': 'Contributors', 'value': '295'}
* **叙事：** Tenacity Release 的核心是'可靠性'——agent 必须'把开始的事做完'。Kanban 多 agent 平台的 heartbeat/reclaim/zombie detection 机制，让任务不会因崩溃而丢失。/goal 命令让 agent 跨 turn 锁定目标。

## Slide 26: 案例 3 · Surface Release · 原生 Desktop——'Hermes meets you wherever you work'
* **视觉隐喻：** 左侧 desktop app 截图风格图形，右侧多语言图标，下方'1 周 100 PRs'徽章
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.16.0 (2026-06-05) — The Surface Release'}
  * {'head': 'Headline', 'detail': '100 PRs + 159 commits 一周内做出原生 desktop app（macOS/Linux/Windows）'}
  * {'head': 'Web admin panel', 'detail': "从'view sessions'进化到完整浏览器管理面板"}
  * {'head': '中文 UI', 'detail': '完整简体中文翻译——桌面应用支持 zh-Hans'}
  * {'head': '远程 Hermes', 'detail': 'desktop 可连接远程 Hermes gateway（OAuth/username-password）'}
  * {'head': '制度含义', 'detail': "'surface'是接触面的扩大——从 CLI 到 desktop、从本地到远程、从英文到中文"}
* **数据要点：**
  * {'label': '窗口 commits', 'value': '874'}
  * {'label': 'Merged PRs', 'value': '542'}
  * {'label': 'Issues closed', 'value': '399（2 P0 + 62 P1）'}
  * {'label': 'Contributors', 'value': '170'}
* **叙事：** Surface Release 是 Hermes 从'技术工具'到'日常工具'的关键跃迁——原生 desktop + Web admin + 中文 UI + 远程连接。一周内 100 PRs 的密度，体现了开源社区的'集中兵力'文化。

## Slide 27: 案例 4 · Velocity Release · 大重构——'16,000 行 → 3,821 行' 的制度设计
* **视觉隐喻：** 左侧'16,083 行'大数字，中间箭头，右侧'3,821 行'小数字，下方'14 modules'标签
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.15.0 (2026-05-28) — The Velocity Release'}
  * {'head': '核心动作', 'detail': 'run_agent.py 从 16,083 行坍缩到 3,821 行（-76%）'}
  * {'head': '重构方式', 'detail': '提取到 14 个 cohesion agent/* 模块——行为不变'}
  * {'head': '冷启动', 'detail': '又一秒节省，47% 更少 per-turn function calls'}
  * {'head': 'session_search', 'detail': '4,500× 更快，0 LLM 调用——免费'}
  * {'head': '制度含义', 'detail': "'速度'不是优化，是制度设计——重构让未来开发更快、插件作者能 grep"}
* **数据要点：**
  * {'label': '窗口 commits', 'value': '1,302'}
  * {'label': 'Merged PRs', 'value': '747'}
  * {'label': 'Issues closed', 'value': '560+（15 P0 + 65 P1）'}
  * {'label': 'Contributors', 'value': '321'}
* **叙事：** Velocity Release 的核心是'速度'——不是性能优化，是制度设计。run_agent.py 从 16,083 行坍缩到 3,821 行，行为不变，但未来开发速度、插件作者 grep 体验、编辑器加载时间都大幅提升。

## Slide 28: 案例 5 · Quicksilver Release · 性能爆发——'Hermes is the messenger god, and this window we made him move like it'
* **视觉隐喻：** 左侧闪电符号 + '80%'大数字，右侧'4.3s → 0.9s'对比，下方'信使神 Hermes'神话引用
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.19.0 (2026-07-20) — The Quicksilver Release'}
  * {'head': 'Headline', 'detail': "first-token time 下降 ~80%——'那个深呼吸消失了'"}
  * {'head': '冷启动', 'detail': '从 4.3 秒到 0.9 秒——CLI/gateway/TUI/desktop/cron 全平台'}
  * {'head': 'Desktop 性能', 'detail': '20+ PR 速度改造——14× 更快 streaming markdown'}
  * {'head': 'Delivery-obligation ledger', 'detail': '响应不会因 gateway 崩溃而丢失——P1 silent-loss 窗口关闭'}
  * {'head': '制度含义', 'detail': "'速度'是消费侧信任的基础——'如果 Hermes 像要深呼吸'，用户就会离开"}
* **数据要点：**
  * {'label': '窗口 commits', 'value': '2,245'}
  * {'label': 'Merged PRs', 'value': '1,065'}
  * {'label': 'Issues closed', 'value': '3,300'}
  * {'label': 'Contributors', 'value': '450+'}
  * {'label': 'First-token 下降', 'value': '~80%'}
* **叙事：** Quicksilver Release 的命名来自 Hermes（信使神）——'this window we made him move like it'。first-token time 下降 80% 是消费侧信任的基础：如果 agent 像要深呼吸，用户就会离开。

## Slide 29: 案例 6 · Patch Release · 热修复——同日 hotfix 的田野观察
* **视觉隐喻：** 左侧'v0.15.0'红色标签 + 箭头 + 右侧'v0.15.1'绿色标签，下方'+1 天'时间徽章
* **显示要点：**
  * {'head': 'Release', 'detail': 'v0.15.1 (2026-05-29) — The Patch Release'}
  * {'head': '时间', 'detail': '同日热修复 v0.15.0——28 commits + 21 PRs'}
  * {'head': 'Headline', 'detail': 'dashboard 401 reload loop——loopback 模式无限重载'}
  * {'head': '根因', 'detail': 'stale-token reload guard 把每个 401 当旋转的 session token'}
  * {'head': '修复', 'detail': 'fetchJSON 加 allowUnauthorized opt-out——401 仍抛异常但跳过 reload'}
  * {'head': '制度含义', 'detail': "热修复也是文化事件——'我们承认错了，并立刻修好'是开源信任的基石"}
* **数据要点：**
  * {'label': '窗口 commits', 'value': '28'}
  * {'label': 'Merged PRs', 'value': '21'}
  * {'label': 'Contributors', 'value': '9'}
  * {'label': '时间', 'value': 'v0.15.0 + 1 天'}
* **叙事：** Patch Release 是开源项目的'认错仪式'——同日热修复，28 commits + 21 PRs。dashboard 401 reload loop 是 v0.15.0 的严重缺陷，团队立即定位并修复。'我们承认错了，并立刻修好'是开源信任的基石。

## Slide 30: PR #5143 · 多角色自动路由——Gateway Hooks · 专业化分化（2026-04）
* **视觉隐喻：** 左侧'#5143'大号编号 + 中间 gateway hooks 路由图 + 右侧'工具→团队'箭头
* **显示要点：**
  * {'head': '需求信号', 'detail': '28,040 body · 11 comments · comp/gateway · area/sessions · needs-decision'}
  * {'head': '用户需求', 'detail': "从'一个 agent 处理一切'到'专业化角色分工'——agent 从工具到团队"}
  * {'head': '演化意义', 'detail': 'Phase 2 标志性提案——平台扩展期用户要求 agent 专业化能力'}
* **数据要点：**
  * {'label': 'Body', 'value': '28,040'}
  * {'label': 'Comments', 'value': '11'}
* **叙事：** #5143 是 Phase 2 的标志性提案。用户要求 gateway hooks 实现多角色自动路由——不同任务类型路由到不同 agent 角色。这是 agent 从'工具'到'团队'的第一个信号。

## Slide 31: PR #53871 · 给 Hermes 一个灵魂——Curiosity Engine · 生命化（2026-06）
* **视觉隐喻：** 左侧'#53871'大号编号 + 中间'生命'概念图 + 右侧'工具→伙伴'箭头
* **显示要点：**
  * {'head': '需求信号', 'detail': '27,518 body · comp/agent · tool/memory · area/sessions'}
  * {'head': '用户需求', 'detail': "从'用完即走'到'希望 agent 有自己的生命'——agent 从工具到伙伴"}
  * {'head': '演化意义', 'detail': 'Phase 3 标志性提案——用户要求 agent 有生命感、记忆延续、自主性'}
* **数据要点：**
  * {'label': 'Body', 'value': '27,518'}
  * {'label': '核心', 'value': 'Curiosity + Dream + Watchman'}
* **叙事：** #53871 是 Phase 3 的标志性提案。'Give Hermes a Life Between Sessions'——引入 Curiosity Engine、Synthetic Dream Cycle、Watchman。这是 agent 从'工具'到'伙伴'的跃迁。

## Slide 32: PR #61044 · Cron-native Batch API——自主调度 · 自动化（2026-07）
* **视觉隐喻：** 左侧'#61044'大号编号 + 中间 cron 循环图（agent loop 自主调度）+ 右侧'手动→自动'箭头
* **显示要点：**
  * {'head': '标题', 'detail': 'RFC: Cron-native Batch API agent loop for scheduled/background work'}
  * {'head': '需求信号', 'detail': '35,660 body · comp/agent · comp/cron · innovation'}
  * {'head': '技术复杂性', 'detail': '中——cron 层引入 agent loop，批处理调度的原生 agent 循环'}
  * {'head': '用户需求', 'detail': "从'手动触发'到'自主调度'——agent 定时自主执行复杂任务"}
  * {'head': '演化意义', 'detail': 'Phase 3 标志性提案——用户要求 agent 有自主调度能力'}
* **数据要点：**
  * {'label': 'Body', 'value': '35,660'}
  * {'label': '标签', 'value': 'comp/cron · innovation'}
  * {'label': '核心', 'value': 'Cron-native agent loop'}
  * {'label': '状态', 'value': 'open · P3'}
* **叙事：** #61044 是 Phase 3 的标志性 RFC。'Cron-native Batch API agent loop for scheduled/background work'——用户要求 agent 能定时自主执行复杂任务。从手动触发到自主调度的跃迁。innovation 标签说明这是被认可的创新提案。

## Slide 33: PR #82198 · Skill-Persistence EPIC——自我组织 · 持久化（2026-08）
* **视觉隐喻：** 左侧'#82198'大号编号 + 中间'Skill-Persistence'架构图（持久化 + 边界 + 风险）+ 右侧'伙伴→自我组织'箭头
* **显示要点：**
  * {'head': '标题', 'detail': 'EPIC: Hermes skill-persistence and storage-boundary operational-risk conquest'}
  * {'head': '需求信号', 'detail': '54,633 body（最大 EPIC）· comp/agent · tool/skills · area/memory · needs-decision'}
  * {'head': '技术复杂性', 'detail': '极高——54,633 body 是样本中最大的设计文档之一，涉及 skill 持久化 + 存储边界 + 运维风险'}
  * {'head': '用户需求', 'detail': "从'临时 skill'到'持久 skill'——agent 自我组织、持久化知识、管理存储边界"}
  * {'head': '演化意义', 'detail': 'Phase 4 标志性提案——EPIC 级设计文档，用户要求 agent 有自我组织能力'}
* **数据要点：**
  * {'label': 'Body', 'value': '54,633（最大 EPIC）'}
  * {'label': '标签', 'value': 'tool/skills · area/memory'}
  * {'label': '核心', 'value': 'Skill 持久化 + 存储边界'}
  * {'label': '状态', 'value': 'open · needs-decision'}
* **叙事：** #82198 是 Phase 4 的标志性 EPIC。54,633 body 是样本中最大的设计文档之一。'skill-persistence and storage-boundary operational-risk conquest'——用户要求 agent 能持久化 skill（知识）、管理存储边界（安全）、征服运维风险（可靠性）。这是 agent 从'伙伴'到'自我组织者'的跃迁。

## Slide 34: PR #94266 · Collective Wisdom Agent——集体智慧 · 智慧化（2026-08）
* **视觉隐喻：** 左侧'#94266'大号编号 + 中间'集体智慧'网络图 + 右侧'自我组织→集体智慧'箭头
* **显示要点：**
  * {'head': '需求信号', 'detail': '52,295 body · 9 comments · comp/agent · tool/skills · area/config · needs-decision'}
  * {'head': '用户需求', 'detail': "从'个体 agent'到'集体智慧'——多个 agent session 的知识聚合为集体智慧"}
  * {'head': '演化意义', 'detail': 'Phase 4 标志性提案——9 comments 讨论活跃，用户要求 agent 有集体智慧能力'}
* **数据要点：**
  * {'label': 'Body', 'value': '52,295'}
  * {'label': 'Comments', 'value': '9（讨论活跃）'}
* **叙事：** #94266 是 Phase 4 的另一个标志性提案。'feat(wisdom): add Hermes Collective Wisdom Agent V1'——用户要求 agent 有集体智慧能力。52,295 body + 9 comments 说明这是活跃讨论的设计文档。

## Slide 35: 案例 12 · desktop 供需缺口——数据案例：唯一失衡的组件
* **视觉隐喻：** 对比表格，desktop 一行用红色标注'⚠️ 供给欠配'，下方 Surface Release 徽章
* **显示要点：**
  * {'head': '需求', 'detail': 'desktop 需求 11%——用户主动要求新功能'}
  * {'head': '供给', 'detail': 'desktop 供给 8%——以 bug 为主'}
  * {'head': '类型不匹配', 'detail': '需求偏新功能，供给以 bug 为主——类型也对不上'}
  * {'head': '对照', 'detail': 'agent/gateway/cli 供需匹配良好（22%/26%, 18%/22%, 18%/17%）'}
  * {'head': 'Surface Release', 'detail': '2026-06-05 一周 100 PRs——团队对 desktop 的集中投入'}
  * {'head': '制度含义', 'detail': "'生态是结果，不是手段'——能力扩张是用户需求驱动的，不是行政推动的"}
* **数据要点：**
  * {'label': 'desktop 需求', 'value': '11%'}
  * {'label': 'desktop 供给', 'value': '8%'}
  * {'label': 'Surface Release', 'value': '100 PRs / 1 周'}
* **叙事：** desktop 是供需缺口——用户偏新功能，供给以 bug 为主。但 Surface Release（一周 100 PRs）显示团队对 desktop 的集中投入。'生态是结果，不是手段'——能力扩张是用户需求驱动的。

## Slide 36: 三个共性问题 · 专业化/生命化/智慧化——5 个 PR 案例的共性提炼
* **视觉隐喻：** 左侧 5 个 PR 编号列 + 中间'专业化→生命化→智慧化'演进箭头 + 右侧 needs-decision 标签
* **显示要点：**
  * {'head': '专业化', 'detail': "#5143 多角色路由——agent 从'一个处理一切'到'角色分工'"}
  * {'head': '生命化', 'detail': '#53871 Soul——agent 有生命感、记忆延续、自主性'}
  * {'head': '智慧化', 'detail': '#82198 Skill-Persistence + #94266 Collective Wisdom——agent 自我组织 + 集体智慧'}
  * {'head': '共同点', 'detail': '5 个 PR 都是 needs-decision（待决策）——社区正在讨论这些演化方向'}
  * {'head': '演化轨迹', 'detail': '专业化 → 生命化 → 自动化 → 持久化 → 智慧化'}
* **叙事：** 5 个 PR 案例的共性：用户不再满足于'一个 agent 处理一切'，而是要求 agent 有专业化分工、有生命感、有自主调度、有持久化记忆、有集体智慧。5 个 PR 都是 needs-decision 状态——社区正在讨论这些演化方向。

## Slide 37: 从'能用'到'好用'的跃迁 · 五阶段——用户需求演化的完整轨迹
* **视觉隐喻：** 五阶段横向时间线，每阶段一个 PR 编号 + 日期 + 核心关键词
* **显示要点：**
  * {'head': '专业化 → 生命化', 'detail': '#5143 (2026-04) Gateway Hooks → #53871 (2026-06) Soul / Curiosity Engine'}
  * {'head': '自动化 → 持久化', 'detail': '#61044 (2026-07) Cron-native Batch API → #82198 (2026-08) Skill-Persistence EPIC (54,633 body)'}
  * {'head': '智慧化', 'detail': '#94266 (2026-08) Collective Wisdom Agent V1 (52,295 body)'}
* **叙事：** 从'能用'到'好用'的跃迁是五步：专业化 → 生命化 → 自动化 → 持久化 → 智慧化。每一步都是用户对 agent 的需求提升——从工具到伙伴到自我组织到集体智慧。

## Slide 38: Release 节奏观察——33 releases / 180 天
* **视觉隐喻：** 时间线 + 33 个圆点，命名 release 用红圈标注
* **显示要点：**
  * {'head': '密度', 'detail': '33 releases / 180 天 ≈ 5.5 天/release'}
  * {'head': '命名', 'detail': '6 命名 release（2026-05 到 2026-07）'}
  * {'head': 'Patch', 'detail': "同日热修复——'认错仪式'"}
* **数据要点：**
  * {'label': '总 Releases', 'value': '33'}
  * {'label': '窗口', 'value': '180 天'}
  * {'label': '命名 Release', 'value': '6 个'}
* **叙事：** Release 节奏是社区自我组织的节奏——不是行政命令能促成的。

## Slide 39: 田野考察小结——12 案例的横切视角
* **视觉隐喻：** 12 个案例标签网格排列，下方三个共性问题大字
* **显示要点：**
  * {'head': '6 个命名 release', 'detail': 'Judgment/Tenacity/Surface/Velocity/Quicksilver/Patch——文化事件'}
  * {'head': '5 个典型 issue', 'detail': '#107070/#101600/#67002/#66353/#84672——制度标本'}
  * {'head': '1 个数据案例', 'detail': 'desktop 供需缺口——扩张期信号'}
  * {'head': '三个共性问题', 'detail': "可靠性/兼容性/信任——从'能用'到'好用'的三道分水岭"}
  * {'head': '核心洞察', 'detail': "消费侧信任是可观察的信号——开源 Agent 的'度量权'在社区手里"}
* **叙事：** 12 个案例的横切视角：6 个命名 release + 5 个典型 issue + 1 个数据案例 = 三个共性问题（可靠性/兼容性/信任）。核心洞察：消费侧信任是可观察的信号——开源 Agent 的'度量权'在社区手里。

## Slide 40: 田野考察方法论复盘——从群众中来的方法
* **视觉隐喻：** 五个圆圈排列：视角/方法/立场/局限/下一步，每个圆圈一个关键词
* **显示要点：**
  * {'head': '视角', 'detail': '开源社区内实践者——不是外部观察者，是参与者和记录者'}
  * {'head': '方法', 'detail': '从群众中来——从实践出发，非框架先行；从案例中提炼，非理论推导'}
  * {'head': '立场', 'detail': '批判行政开源——用实践检验理论，用演化观察制度'}
  * {'head': '局限', 'detail': '弱代理（stars ≠ 使用）、单一仓库、关键词分析（非语义）'}
  * {'head': '下一步', 'detail': '长期追踪——持续观察需求/供给/消费的演化，寻找更强信号'}
* **叙事：** 方法论复盘：视角是开源社区内实践者（不是外部观察者），方法是从群众中来（从实践出发，非框架先行），立场是批判行政开源（用实践检验理论）。局限：消费信号是弱代理、单一仓库、关键词分析非语义分析。下一步：长期追踪。

## Slide 41: 第四幕 · Agent 演化洞察——从 12 案例中提炼的演化规律
* **视觉隐喻：** 深普鲁士蓝底色，中央大字'Agent 演化洞察'，下方三道分水岭
* **显示要点：**
  * {'head': '核心', 'detail': "从'能用'到'好用'的三道分水岭"}
  * {'head': '方法', 'detail': '12 案例 → 3 共性 → 3 洞察'}
  * {'head': '目标', 'detail': '理解 Agent 演化的内在规律'}
* **叙事：** 本幕从 12 个案例中提炼 Agent 演化规律——从'能用'到'好用'的三道分水岭：可靠性、兼容性、信任。

## Slide 42: 三道分水岭 · 可靠性/兼容性/信任——从'能用'到'好用'的关键跃迁
* **视觉隐喻：** 三道分水岭并排：可靠性/兼容性/信任
* **显示要点：**
  * {'head': '可靠性', 'detail': '能否信任 agent 记住正确的历史（#107070 + Tenacity）'}
  * {'head': '兼容性', 'detail': "用户不会被'锁在门外'（#101600 + Surface）"}
  * {'head': '信任', 'detail': '能力有安全边界（#67002 + Judgment）'}
* **叙事：** 三道分水岭是 Agent 从'能用'到'好用'的关键跃迁。顺序不是独立的——可靠性是兼容性的基础，兼容性是信任的前提。

## Slide 43: 洞察 #1 · 可靠性是 Agent 的底线——Tenacity Release + #107070
* **视觉隐喻：** 左侧 Tenacity Release 徽章 + 右侧 #107070 issue 卡片，中间箭头
* **显示要点：**
  * {'head': 'Tenacity Release', 'detail': 'Kanban 多 agent 平台——heartbeat/reclaim/zombie detection'}
  * {'head': '#107070', 'detail': '会话重放污染历史——P1 缺陷'}
  * {'head': '可靠性定义', 'detail': "不是'能不能用'，是'能否信任 agent 记住正确的历史'"}
  * {'head': '制度含义', 'detail': '可靠性是 Agent 的底线——用户信任的前提'}
  * {'head': '案例组合', 'detail': '供给侧（Tenacity）+ 需求侧（#107070）= 完整画面'}
* **数据要点：**
  * {'label': 'Tenacity Release', 'value': 'v0.13.0 (2026-05-07)'}
  * {'label': '#107070', 'value': 'P1 / risk-session-state'}
* **叙事：** 可靠性是 Agent 的底线——Tenacity Release 用 Kanban 平台解决任务持久性，#107070 是会话重放污染历史的 P1 缺陷。供给侧（Tenacity）+ 需求侧（#107070）= 完整画面。

## Slide 44: 洞察 #2 · 兼容性是 Agent 的边界——Surface Release + #101600
* **视觉隐喻：** 左侧 Surface Release 徽章 + 右侧 #101600 issue 卡片
* **显示要点：**
  * {'head': 'Surface Release', 'detail': '原生 desktop（macOS/Linux/Windows）'}
  * {'head': '#101600', 'detail': 'Windows 自锁——P1 缺陷'}
  * {'head': '洞察', 'detail': '兼容性是 Agent 的边界——跨平台扩展的前提'}
* **数据要点：**
  * {'label': 'Surface Release', 'value': 'v0.16.0 (2026-06-05)'}
  * {'label': '#101600', 'value': 'P1 / risk-compatibility'}
* **叙事：** 兼容性是 Agent 的边界——Surface Release 做出跨平台 desktop，#101600 是 Windows 自锁的 P1 缺陷。供给侧 + 需求侧 = 完整画面。

## Slide 45: 洞察 #3 · 信任是 Agent 的跃迁——Judgment Release + #67002
* **视觉隐喻：** 左侧 Judgment Release 徽章 + 右侧 #67002 issue 卡片，中间箭头
* **显示要点：**
  * {'head': 'Judgment Release', 'detail': 'P0/P1 清零战役——692 items / 12 days'}
  * {'head': '#67002', 'detail': 'Safe MCP Reload——用户主动要求安全边界'}
  * {'head': '信任定义', 'detail': '用户在索取能力的同时显式要求安全收口'}
  * {'head': '制度含义', 'detail': "信任是 Agent 从'能用'到'好用'的跃迁"}
  * {'head': '案例组合', 'detail': '供给侧（Judgment）+ 需求侧（#67002）= 完整画面'}
* **数据要点：**
  * {'label': 'Judgment Release', 'value': 'v0.18.0 (2026-07-01)'}
  * {'label': '#67002', 'value': 'risk-message-delivery + blast-moderate'}
* **叙事：** 信任是 Agent 的跃迁——Judgment Release 用 P0/P1 清零建立信任，#67002 是用户主动要求安全边界。供给侧（Judgment）+ 需求侧（#67002）= 完整画面。

## Slide 46: MCP 演化路径 · 从厂商私产到中立基金会——生态演化的一个案例
* **视觉隐喻：** 左上 Anthropic → 中间箭头 → 右上 Linux Foundation，箭头下方标注时间跨度
* **显示要点：**
  * {'head': '起点', 'detail': '2024-11-25 Anthropic 单厂商发布'}
  * {'head': '采纳', 'detail': '2025-03 OpenAI 采纳——第二个前沿实验室加入'}
  * {'head': '云厂', 'detail': '2025 云厂密集加入——AWS Bedrock AgentCore 等'}
  * {'head': '捐给 LF', 'detail': '2026 加入 Agentic AI Foundation（Linux Foundation 旗下）'}
  * {'head': '观察', 'detail': 'MCP 演化是社区自我组织的自然结果——不是行政命令能促成的'}
* **数据要点：**
  * {'label': '起点', 'value': '2024-11-25'}
  * {'label': '终点', 'value': '2026'}
* **叙事：** MCP 演化路径：从 Anthropic 单厂商私产到 Linux Foundation 中立基金会。多厂商自发采纳后的自然结果——这是 Agent 生态演化的一个典型案例。

## Slide 47: Epilogue · 长期演化追踪——不是终点
* **视觉隐喻：** 极简路线图，左侧'演讲 2026-09-21'，右侧延伸长线上有四个节点
* **显示要点：**
  * {'head': '定位', 'detail': '本演讲是长期演化追踪系统的第一个快照'}
  * {'head': '三个维度', 'detail': '度量权 / 可靠性 / 产权——并行维度，非线性递进'}
  * {'head': 'Keep Movement', 'detail': '进化论的哲学里是没有终点的'}
* **叙事：** 这不是一次性分析，是长期演化追踪系统的第一个快照。'进化论的哲学里是没有终点的'——Keep Movement。

## Slide 48: 长期演化追踪系统——下一个快照是什么？
* **视觉隐喻：** 时间线 + 四个节点（需求/供给/消费/制度），线上有'每周/每月/持续'标注
* **显示要点：**
  * {'head': '需求侧', 'detail': '持续追踪 issue 演化（每周更新）'}
  * {'head': '供给侧', 'detail': '持续追踪 PR 演化（每周更新）'}
  * {'head': '消费侧', 'detail': '寻找更强信号（PyPI downloads、Docker pulls、Discord 活跃度）'}
  * {'head': '制度维度', 'detail': '度量权 / 可靠性 / 产权——三个并行维度'}
  * {'head': '田野考察', 'detail': '新增案例（issue/PR/release）每月更新'}
* **叙事：** 长期演化追踪系统的下一个快照：需求侧/供给侧/消费侧每周更新，新增案例每月更新，制度维度并行追踪。'Keep Movement'——知识不是静止的，是在移动中产生的。

## Slide 49: 结语 · 开源之为思想的力量
* **视觉隐喻：** 深普鲁士蓝底色，中央大字'思想是制度的源代码'
* **显示要点：**
  * {'head': '从 Agent 到制度', 'detail': 'Hermes 是样本，不是终点'}
  * {'head': '开源之道', 'detail': '道是思想（idea），不是道路（road）'}
  * {'head': 'Keep Movement', 'detail': '知识不是静止的，是在移动中产生的'}
  * {'head': '一句留白', 'detail': '不是要证明什么——是打开一种思考'}
* **叙事：** '思想是制度的源代码'——不是规则在动，是思想在动。Keep Movement。这个演讲不是要证明什么，是要打开一种思考：用制度经济学的眼睛，重新看 Agent 演化。

## Slide 50: 讨论问题——留给 Q&A 的三个开放问题
* **视觉隐喻：** 极简设计，三个问题列在中央，每个问题前有小圆点
* **显示要点：**
  * **问题 #1**：从"能用"到"会协作"，是否还有第六阶段？——agent 演化的下一个分水岭在哪里？
  * **问题 #2**：开源 Agent 的"度量权"应该在社区手里，还是应该标准化？——Hermes 的 Footprint Ladder 是一种制度实验
  * **问题 #3**：本土办公产品的 Agent 平台化 vs 开源 Agent 的模块化——两种治理哲学的终局是什么？
  * **问题 #4**：Talk & Search 时代和 Agent & Decide 时代会共存还是替代？——消费范式的重构已经开始了吗？
* **叙事：** 三个开放问题留给 Q&A。田野考察是开放的——欢迎补充案例，issue/PR/release 都是田野材料。

## Slide 51: 延伸阅读——制度经济学核心文献
* **视觉隐喻：** 5 本书籍封面横向排列，深普鲁士蓝背景
* **显示要点：**
  * {'head': '转型经济学', 'detail': 'Roland 2004 · Understanding Institutional Change'}
  * {'head': '交易成本经济学', 'detail': 'Williamson 2000 · The New Institutional Economics'}
  * {'head': '认知制度', 'detail': 'Akcagün & Sapienza 2016 · Cognitive Rules of Growth'}
  * {'head': '演化制度理论', 'detail': 'Greif & Mokyr 2017 · Journal of Institutional Economics'}
  * {'head': '开源经济学', 'detail': 'Lerner & Tirole 2002 · The Economics of Open Source Software'}
* **叙事：** 延伸阅读覆盖制度经济学的核心文献——从转型经济学到演化制度理论，从交易成本到开源经济学。

## Slide 52: 致谢 · Thank you——Keep Movement
* **视觉隐喻：** Minimal design. Center: '致谢 · Thank you'. Below: 'Keep Movement'. Bottom: date + event info.
* **显示要点：**
  * **「开源之道」·适兕 × 窄廊**——两种存在形式，一个使命：Keep Movement——知识不是静止的，是在移动中产生的
  * **数据基线**：2026-09-11 · **方法论**：田野考察——从群众中来，非框架先行
  * **延伸思考**：这个演讲不是要证明什么——是要打开一种思考
  * **2026-09-14** · AgentCon 2026 · 北京 · Token 经济趋势
* **叙事：** 讲者信息、数据基线、方法论声明、结语——一页收尾。

