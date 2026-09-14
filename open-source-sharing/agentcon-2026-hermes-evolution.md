# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
用于 AgentCon 2026 北京站（2026-09-21）Token 经济趋势 track 的演讲分享。50 页田野考察风格。

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

# 幻灯片大纲内容 (Slide Deck Outline)

## Slide 1: 封面 (Cover)
* **主标题：** 从 Hermes 演化看 Agent 需求与消费演进
* **副标题：** Talk & Search → Agent & Decide——两个时代的分叉
* **讲者信息：** 「开源之道」·适兕 × 窄廊
* **英文署名：** Open Source Way · Kuosi × Narrow Corridor
* **时间/地点：** AgentCon 2026 · 北京 · 2026-09-21
* **Track：** Token 经济趋势
* **视觉隐喻：** 深普鲁士蓝底色封面，中央大号标题。标题下方"Talk & Search → Agent & Decide"横向箭头。底部小字："Talk is expensive, show me the skills."

## Slide 2: 引子——从 Talk & Search 到 Agent & Decide
* **视觉隐喻：** 左侧"对话气泡"（Talk & Search），中间"→"箭头，右侧"agent 图标"（Agent & Decide）。顶部一句 Hook："Talk is expensive, show me the skills."
* **显示要点：**
  * **Hook**："Talk is expensive, show me the skills."
  * **LLM 时代**：对话与检索（Talk & Search）——人类提问，模型回答
  * **Agentic 时代**：代理与决断（Agent & Decide）——agent 自主执行，人类验收结果
  * **本次观察**：透过 Hermes Agent 仓库这个微观透镜，寻找人类心智函数正在发生微小但不可逆分叉的证据

## Slide 3: 章节过渡——Agent 发展简史
* **视觉隐喻：** 深普鲁士蓝底色。中央大字"Agent 发展简史"。下方时间线 2022 → 2026。
* **显示要点：**
  * 从"文本生成器"到"数字员工"，Agent 用了不到 5 年
  * 本部分目标：勾勒 Agent 发展的关键拐点

## Slide 4: 阶段一——能力觉醒（2022-2023）
* **显示要点：**
  * **ReAct**：首次展示"推理 + 行动"交织的 agent 模式
  * **Toolformer**：LLM 自监督学会调用 API
  * **OpenAI Function Calling**：主流"函数调用"API 原语首次出现
  * **AutoGPT / BabyAGI**：病毒式传播的"自主 agent"时刻
  * **跨域套利**：从学术（1980s BDI）到产品（LLM tool use）

## Slide 5: 阶段二——能力硬化（2024）
* **显示要点：**
  * **Anthropic Tool Use GA**：从 beta 到生产可用
  * **OpenAI Structured Outputs**：强 schema 校验
  * **Anthropic Computer Use**：Agent 从 API 走到 GUI
  * **MCP 发布（2024-11-25）**：首个开放协议标准化 agent-tools 接口
  * **协议是生态的起点**：Computer Use 扩展能力边界，MCP 定义协议

## Slide 6: 阶段三——协议成熟（2025-2026）
* **显示要点：**
  * **OpenAI 采纳 MCP**（2025-03）：第二个前沿实验室加入
  * **AWS Bedrock AgentCore**（2025-07）：云原生 agent 平台化
  * **A2A 协议**（2026-01）：agent-agent 协作标准
  * **MCP 捐给 Agentic AI Foundation**（2026）
  * **协议制度化**：从"一家厂商的设计"到"中立基金会资产"

## Slide 7: MCP 捐给 Linux Foundation
* **显示要点：**
  * **起点**：2024-11-25，Anthropic 单厂商发布 MCP
  * **演化**：2025-03 OpenAI 采纳；2025 云厂密集加入
  * **终点**：2026，MCP 捐给 Agentic AI Foundation（Linux Foundation 旗下）
  * **制度含义**：多厂商自发采纳后的自然结果——不是行政命令能促成的

## Slide 8: 章节过渡——Hermes 技术架构
* **视觉隐喻：** 深普鲁士蓝底色。中央大字"Hermes 技术架构"。下方两条竖线（两条不变量）。
* **显示要点：**
  * Hermes 的几乎所有设计决策都从两条不变量推出来
  * 本部分目标：先讲不变量，再讲架构，最后讲独特性

## Slide 9: Hermes 项目坐标
* **显示要点：**
  * **Stars**：243K+ · 持续上升
  * **Contributors**：397 · 活跃社区
  * **Releases**：33 · 2026-03-12 到 2026-09-11
  * **Issues**：41,792 · PRs：27,783
  * **创建**：2025-07-22

## Slide 10: 两条不变量——设计灵魂
* **显示要点：**
  * **不变量 #1：Prompt Caching is Sacred**
    - 任何改变历史上下文的操作都会破坏缓存、放大用户成本
    - 结果：所有修改系统提示状态的命令默认"下 session 生效"
  * **不变量 #2：Core is a Narrow Waist, Capability Lives at the Edges**
    - 新能力通过"CLI + skill"、"plugin"、"MCP server"落地
    - "边缘扩张，腰部保守"——Hermes 的制度设计原则

## Slide 11: Footprint Ladder——六级能力阶梯
* **显示要点：**
  * **Level 1**：Extend existing code（零新面）
  * **Level 2**：CLI command + skill
  * **Level 3**：Service-gated tool（check_fn）
  * **Level 4**：Plugin（第三方/niche/用户特定）
  * **Level 5**：MCP server（catalog 内）
  * **Level 6**：New core tool（只有普适工具够格）
  * **度量权**：每个能力都有可审计的落地位置

## Slide 12: Hermes 的独特性——大教堂的瓦解
* **视觉隐喻：** 左侧"大教堂"（单体建筑），右侧"集市"（多个小摊位），中间"瓦解"箭头。
* **显示要点：**
  * **大教堂 vs 集市**：Monolithic（大教堂思维）→ Modular（集市涌现）——模块化降低新 skill 的"交易成本"
  * **闭环学习**：每次使用生成新 skill——agent 随使用自我进化
  * **对比四个框架**：Hermes 4,100 tokens/task（最低）/ 55MB RAM（最低）/ 200+ models via OpenRouter
  * **消费重构**：从"对标准产品的依赖"到"对个性化技能编排（Composition）的投入"

## Slide 13: Agent 演化方法论——田野观察
* **显示要点：**
  * **样本选择**：Hermes Agent（243K star, 33 releases, 397 contributors）——公开演化数据丰富的样本
  * **观察维度**：需求（issues）/ 供给（PRs）/ 消费（stars/contributors/release）
  * **案例驱动**：6 命名 release + 5 典型 PR + 1 数据案例——12 个田野样本
  * **三段式**：现象 → 数据 → 解读
  * **目的**：理解 Agent 从"能用"到"好用"的演化路径

## Slide 14: 田野考察方法论
* **显示要点：**
  * **视角**：开源社区内实践者——不是外部观察者
  * **方法**：从群众中来——从实践出发，非框架先行
  * **立场**：批判行政开源——用实践检验理论
  * **局限**：弱代理、单一仓库、关键词分析（非语义）
  * **下一步**：长期追踪

## Slide 15: 章节过渡——田野考察
* **视觉隐喻：** 深普鲁士蓝底色。中央大字"第三幕 · 田野考察"。下方"12 案例"网格。
* **显示要点：**
  * 6 命名 Release + 5 PR 演化案例 + 1 数据案例
  * 每个案例：现象 → 数据 → 解读

## Slide 16: 需求侧总览——用户要什么
* **显示要点：**
  * **类型**：bug 50% / feature 50%
  * **组件**：cli / agent / gateway 各 19%（57%）
  * **优先级**：P3 68% / P2 28% / P1 3%
  * **风险谱**：兼容性 > 消息投递 > 安全边界 ≈ 会话状态
  * **特征**：长尾需求 + 极少火警

## Slide 17: 供给侧总览——项目做了什么
* **显示要点：**
  * **类型**：bug fix 50% / feature 50%
  * **组件**：agent 26% + gateway 22%（48%）
  * **收敛型策略**：P2 全给 bug（89%）+ P1 缺席
  * **风险**：兼容性 56%（结构性负担）
  * **含义**：从扩张期进入稳定化期

## Slide 18: 消费侧总览——弱代理的采纳信号
* **显示要点：**
  * **Releases 节奏**：33 个 release，8 月 5 个
  * **Contributor 分布**：核心 21 / 活跃 143 / 外围 233
  * **Top 3**：teknium1 > OutThisLife > kshitijk4poor
  * **消费信号局限**：stars/forks ≠ 真实使用——是弱代理

## Slide 19: 三个核心洞察
* **显示要点：**
  * **洞察 #1：项目正从扩张期进入稳定化期**
  * **洞察 #2：兼容性是结构性税**
  * **洞察 #3：消费侧信任是可观察的信号**

## Slide 20: Release 命名文化——田野观察第 1 章
* **显示要点：**
  * **6 命名 release**：Judgment / Tenacity / Surface / Velocity / Quicksilver / Patch
  * **命名不是版本**：是社区自我命名的文化事件
  * **田野意义**：每个命名 release 是一个制度演化节点

## Slide 21: 案例 1 · Judgment Release · P0/P1 清零
* **显示要点：**
  * **版本**：v2026.7.20 "Judgment"
  * **内容**：P0/P1 清零战役——692 items / 12 days
  * **Feature 改进**：项目自我修复的"认错仪式"
  * **信任分水岭**：用户在要能力的同时要求安全边界
  * **演化意义**：从扩张期进入稳定化期的标志

## Slide 22: 案例 2 · Tenacity Release · 多 Agent Kanban
* **显示要点：**
  * **版本**：v2026.7.1 "Tenacity"
  * **内容**：Kanban 多 agent 平台
  * **Feature 改进**：heartbeat / reclaim / zombie detection——任务持久性保障
  * **可靠性分水岭**：能否信任 agent 记住正确的历史
  * **演化意义**：从单 agent 到多 agent 协作

## Slide 23: 案例 3 · Surface Release · 原生 Desktop
* **显示要点：**
  * **版本**：v2026.6.5 "Surface"
  * **内容**：原生 desktop（macOS/Linux/Windows）
  * **Feature 改进**："Hermes meets you wherever you work"
  * **兼容性分水岭**：用户不会被"锁在门外"
  * **演化意义**：跨平台扩展的前提

## Slide 24: 案例 4 · Velocity Release · 大重构
* **显示要点：**
  * **版本**：v2026.5.29 "Velocity"
  * **内容**：性能优化、异步处理
  * **Feature 改进**：能力硬化阶段的速度跃迁
  * **演化意义**：从"能用"到"快用"

## Slide 25: 案例 5 · Quicksilver Release · 性能爆发
* **显示要点：**
  * **版本**：v2026.5.28 "Quicksilver"
  * **内容**：快速迭代版本
  * **Feature 改进**：扩张期的迭代节奏
  * **演化意义**：快速试错、快速迭代

## Slide 26: 案例 6 · Patch Release · 热修复
* **显示要点：**
  * **版本**：v2026.5.7 "Patch"
  * **内容**：同日热修复
  * **Feature 改进**：快速响应模式
  * **演化意义**："认错仪式"——承认错误并快速修复

## Slide 27: PR #5143 · 多角色自动路由
* **显示要点：**
  * **需求信号**：28,040 body · 11 comments · comp/gateway · area/sessions · needs-decision
  * **用户需求**：从"一个 agent 处理一切"到"专业化角色分工"——agent 从工具到团队
  * **演化意义**：Phase 2 标志性提案——平台扩展期用户要求 agent 专业化能力

## Slide 28: PR #53871 · 给 Hermes 一个灵魂
* **显示要点：**
  * **需求信号**：27,518 body · comp/agent · tool/memory · area/sessions
  * **用户需求**：从"用完即走"到"希望 agent 有自己的生命"——agent 从工具到伙伴
  * **演化意义**：Phase 3 标志性提案——用户要求 agent 有生命感、记忆延续、自主性

## Slide 29: PR #61044 · Cron-native Batch API
* **显示要点：**
  * **需求信号**：35,660 body · comp/agent · comp/cron · innovation
  * **用户需求**：从"手动触发"到"自主调度"——agent 定时自主执行复杂任务
  * **演化意义**：Phase 3 标志性提案——用户要求 agent 有自主调度能力

## Slide 30: PR #82198 · Skill-Persistence EPIC
* **显示要点：**
  * **需求信号**：54,633 body（最大 EPIC）· comp/agent · tool/skills · area/memory · needs-decision
  * **用户需求**：从"临时 skill"到"持久 skill"——agent 自我组织、持久化知识、管理存储边界
  * **演化意义**：Phase 4 标志性提案——EPIC 级设计文档，用户要求 agent 有自我组织能力

## Slide 31: PR #94266 · Collective Wisdom Agent
* **显示要点：**
  * **需求信号**：52,295 body · 9 comments · comp/agent · tool/skills · area/config · needs-decision
  * **用户需求**：从"个体 agent"到"集体智慧"——多个 agent session 的知识聚合为集体智慧
  * **演化意义**：Phase 4 标志性提案——9 comments 讨论活跃，用户要求 agent 有集体智慧能力

## Slide 32: 案例 12 · desktop 供需缺口
* **显示要点：**
  * **需求**：desktop 需求 11%（并列第三）
  * **供给**：desktop 供给仅 8%
  * **类型也对不上**：需求偏新功能，供给以 bug 为主
  * **含义**："生态是结果，不是手段"——desktop 是用户主动要求扩张的方向

## Slide 33: 三个共性问题——专业化/生命化/智慧化
* **显示要点：**
  * **专业化**：#5143 多角色路由——agent 从"一个处理一切"到"角色分工"
  * **生命化**：#53871 Soul——agent 有生命感、记忆延续、自主性
  * **智慧化**：#82198 + #94266——agent 自我组织 + 集体智慧
  * **共同点**：5 个 PR 都是 needs-decision（待决策）——社区正在讨论这些演化方向
  * **演化轨迹**：专业化 → 生命化 → 自动化 → 持久化 → 智慧化

## Slide 34: 从"能用"到"好用"的跃迁·五阶段
* **显示要点：**
  * **专业化 → 生命化**：#5143 (2026-04) Gateway Hooks → #53871 (2026-06) Soul / Curiosity Engine
  * **自动化 → 持久化**：#61044 (2026-07) Cron-native Batch API → #82198 (2026-08) Skill-Persistence EPIC (54,633 body)
  * **智慧化**：#94266 (2026-08) Collective Wisdom Agent V1 (52,295 body)

## Slide 35: Release 节奏观察
* **显示要点：**
  * **密度**：33 releases / 180 天 ≈ 5.5 天/release
  * **命名**：6 命名 release（2026-05 到 2026-07）
  * **Patch**：同日热修复——"认错仪式"
  * **含义**：Release 节奏是社区自我组织的节奏

## Slide 36: 田野考察小结
* **显示要点：**
  * **6 命名 Release**：Tenacity / Surface / Judgment / Velocity / Quicksilver / Patch——供给侧的叙事化
  * **5 PR 案例**：#5143 / #53871 / #61044 / #82198 / #94266——需求侧的演化轨迹
  * **1 数据案例**：desktop 供需缺口
  * **核心发现**：用户对 agent 的需求从"工具"演化为"伙伴"再演化为"集体智慧"
  * **方法**：田野考察——从实践中观察，非框架先行

## Slide 37: 田野考察方法论复盘
* **显示要点：**
  * **视角**：开源社区内实践者
  * **方法**：从群众中来
  * **立场**：批判行政开源
  * **局限**：弱代理、单一仓库、关键词分析
  * **下一步**：长期追踪

## Slide 38: 章节过渡——Agent 演化洞察
* **视觉隐喻：** 深普鲁士蓝底色。中央大字"第四幕 · Agent 演化洞察"。下方三道分水岭。
* **显示要点：**
  * 从 12 案例中提炼的演化规律
  * 从"能用"到"好用"的三道分水岭

## Slide 39: 三道分水岭——可靠性/兼容性/信任
* **显示要点：**
  * **可靠性**：能否信任 agent 记住正确的历史（#107070 + Tenacity）
  * **兼容性**：用户不会被"锁在门外"（#101600 + Surface）
  * **信任**：能力有安全边界（#67002 + Judgment）

## Slide 40: 洞察 #1 · 可靠性是 Agent 的底线
* **显示要点：**
  * **Tenacity Release**：Kanban 多 agent 平台——heartbeat/reclaim/zombie detection
  * **#107070**：会话重放污染历史——P1 缺陷
  * **可靠性定义**：不是"能不能用"，是"能否信任 agent 记住正确的历史"
  * **案例组合**：供给侧（Tenacity）+ 需求侧（#107070）= 完整画面

## Slide 41: 洞察 #2 · 兼容性是 Agent 的边界
* **显示要点：**
  * **Surface Release**：原生 desktop（macOS/Linux/Windows）
  * **#101600**：Windows 自锁——P1 缺陷
  * **兼容性定义**：不是"次要的技术债"，是"用户不被锁在门外"
  * **案例组合**：供给侧（Surface）+ 需求侧（#101600）= 完整画面

## Slide 42: 洞察 #3 · 信任是 Agent 的跃迁
* **显示要点：**
  * **Judgment Release**：P0/P1 清零战役——692 items / 12 days
  * **#67002**：Safe MCP Reload——用户主动要求安全边界
  * **信任定义**：用户在索取能力的同时显式要求安全收口
  * **案例组合**：供给侧（Judgment）+ 需求侧（#67002）= 完整画面

## Slide 43: MCP 演化路径——从厂商私产到中立基金会
* **显示要点：**
  * **起点**：2024-11-25 Anthropic 单厂商发布
  * **采纳**：2025-03 OpenAI 采纳
  * **云厂**：2025 云厂密集加入
  * **捐给 LF**：2026 加入 Agentic AI Foundation（Linux Foundation 旗下）
  * **观察**：MCP 演化是社区自我组织的自然结果

## Slide 44: 章节过渡——Epilogue
* **视觉隐喻：** 深普鲁士蓝底色。中央大字"Epilogue · 长期演化追踪"。
* **显示要点：**
  * 不是终点，是起点

## Slide 45: 长期演化追踪系统
* **显示要点：**
  * **需求侧**：持续追踪 issue 演化（月度）
  * **供给侧**：持续追踪 PR 演化（月度）
  * **消费侧**：寻找更强信号（PyPI downloads、Docker pulls、Discord 活跃度）
  * **制度维度**：度量权 / 可靠性 / 产权（长期制度演化追踪）
  * **核心声明**：进化论的哲学里是没有终点的

## Slide 46: 结语——开源之为思想的力量
* **显示要点：**
  * **从 Agent 演化到制度演化**：Hermes 是一个样本，但不是终点
  * **开源的"道"是思想（idea）**："开源之为思想的力量"
  * **Keep Movement**：知识不是静止的，是在移动中产生的
  * **一句留白**：这个演讲不是要证明什么——是要打开一种思考

## Slide 47: 讨论问题
* **显示要点：**
  * **问题 #1**：从"能用"到"会协作"，是否还有第六阶段？
  * **问题 #2**：开源 Agent 的"度量权"应该在社区手里，还是应该标准化？
  * **问题 #3**：5 个 needs-decision PR 最终会走向什么？
  * **问题 #4**：Talk & Search 时代和 Agent & Decide 时代会共存还是替代？

## Slide 48: 延伸阅读
* **显示要点：**
  * Hermes Agent 仓库：github.com/NousResearch/hermes-agent
  * AgentCon 2026 北京站：2026-09-21
  * MCP 规范：modelcontextprotocol.io
  * Linux Foundation Agentic AI Foundation
  * 本项目分析报告：Google Drive osw 账户

## Slide 49: 致谢
* **显示要点：**
  * **讲者**：「开源之道」·适兕 × 窄廊
  * **数据基线**：2026-09-11
  * **方法论**：田野考察——从群众中来
  * **立场**：开源社区内实践者

## Slide 50: Thank you
* **视觉隐喻：** 极简设计。页面中央"Thank you"。下方"Keep Movement"。
* **显示要点：**
  * **Thank you**
  * **Keep Movement**
  * **「开源之道」·适兕 × 窄廊**
  * **2026-09-14**
