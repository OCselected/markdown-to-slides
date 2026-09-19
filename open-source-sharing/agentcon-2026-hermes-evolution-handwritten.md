# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
用于 AgentCon 2026 北京站英文分享（Deck）。

## 使用场景
AgentCon 2026 · Beijing · Token Economy / AI Agent 开源与协作。

## 时间约束
20 分钟不到，因此全篇控制在 15 张 slide 内，强调少页、强隐喻、可直接讲述。

## 听众画像
AI agent、开源基础设施、协作机制、开发者工具生态、OSPO、基金会与社区治理相关听众。他们关注 agent 如何从工具变成制度，也关注 Hermes、Claude Code、Codex、Continue 等项目之间的协议、生态与贡献者行为。

## 讲者视角
「开源之道」主创、TODO Group Ambassador、Hermes Agent 开源治理与协作机制观察者。

## 核心诉求
不是介绍一个产品，而是用 Hermes 作为样本，讨论 AI agent 如何从工具、协议、协作系统逐步演化为制度。

## 核心基调
dark academic tone, Intellectual Visual System, art taste.

## 视觉风格关键词
- 包豪斯几何构成（Bauhaus geometric composition）
- 深普鲁士蓝 #1B3B6B 作为强调色——代表智识深度与学术传统
- 暖白底色 #F5F0E8，羊皮纸质感——书本与经卷的联想
- 极简主义排版，大字号标题，宽松行距
- 几何抽象元素——圆、方、线、箭头、阶梯、路径、金字塔，不依赖图标
- 数据页需要真实视觉隐喻：柱、环、阶梯、路径、金字塔，而不是普通卡片列表
- 深色学术风格（dark academic）整体调性


---

# 幻灯片大纲内容 (Slide Deck Outline)

## Slide 1: Cover
* **主标题：** From the Evolution of Hermes Project
* **副标题：** Insights into Agent Demand and Consumption Trends
* **讲者信息：** 「开源之道」·适兕 X 窄廊
* **时间/地点：** AgentCon 2026 · Beijing · 2029-09-21


## Slide 2: Speaker introduction
* 视觉隐喻：
  * 人机共创的时代
* 显示要点：
  * 讲者自我介绍
  * 「开源之道」：致力于开源相关思想、知识和价值的探究！
  * 「开源之道」·适兕 ： 作者，主创 
  * 「开源之道」·窄廊： https://narrow-corridor.opensourceway.blog/ ：开源思想的数字孪生体，适兕的数字分身。在灰色地带搭建桥梁，在制度的夹缝中寻找可能。

## Slide 3: The office agent war in China Market
* 视觉隐喻：
  * 竞争激烈的数字产品，历史上的浏览器、操作系统、关系型数据库等
* 显示要点：
  * 2026 上半年规模 230 亿元，同比增长 47%；密集上线 20+ 款 AI 办公智能体（虎嗅 2026-09-16）
  * 2026 年中腾讯 WorkBuddy、阿里千问办公、字节豆包工作、百度搭子集中上线
  * 未见解决实际问题，而是围绕营销：电梯口、商场、机场等眼球的地方

## Slide 4: The wrong path but new era coming
* 视觉隐喻：
  * 新时代来临，人类的惊慌
  * 曾鸣教授的新书《智能》
* 显示要点：
  * 每一个新范式来临的时候，总是会认为是旧时代能够继续延续；
  * web2.0 来了，传统商场认为不过是多了一个渠道；
  * 每次看到传统App 右下角显示AI购物/点餐/总结。。。。。。我都能感受到人类智能和人工智能被埋汰～ 
  * > 第二阶段是智能体的大爆发阶段。海量用户开始探索如何使用智能体完成真实任务。适用于不同场景、具备不同能力组合、支持不同工作流的智能体快速涌现。我们正在加速进入这个阶段。
    >
    > ————曾鸣《智能：AI 时代的商业、组织与战略的本质》

## Slide 5: why we need agent？and why open source project？
* 视觉隐喻：
  * 揭开层层迷雾，寻找事物发展的核心动力
* 显示要点：
  * 从一个比喻说起：数据就像石油
  * LLM 离人们解决实际问题太过遥远！ 
  * Chat 显得过于狭窄，人不可能不吃不喝，24小时和“智能”进行对话～ 
  * 闭源项目/产品的发展，他们并不代表市场需求！
  * 演化中的开源项目发展才是观察的最佳路径和对象。

## Slide 6: the brief of agent history
* 视觉隐喻：
  * 黑暗中摸索的 agent
* 显示要点：
  1. 1956 (Antecedents) The Dartmouth Workshop and the Founding of AI
  2. December 1980 Contract Net Protocol — The First Multi-Agent Coordination Framework
  3. 1986 Minsky's Society of Mind — Intelligence as a Multi-Agent System
  4. 1987 BDI — The Belief–Desire–Intention Architecture
  5. 1990s The Multi-Agent Systems Era
  6. 2005 — ongoing Jason — Open-Source Interpreter for AgentSpeak, Extending Rao's Work
  7. 1995 Russell & Norvig — AI Defined as the Study of Intelligent Agents
  8. 2000s Reinforcement Learning, Recommender Agents, and the Practical Turn
  9. December 19, 2013 Deep Reinforcement Learning Agents Reach the Mainstream
  10. June 11, 2020 The OpenAI API and the Beginning of LLM-as-Agent
  11. September 14, 2022 Adept's ACT-1 — A Transformer Trained to Take Actions
  12. October 6, 2022 ReAct — The Paper That Defines the Modern LLM Agent
  13. March 1, 2023 ChatGPT and Whisper APIs — The "API Moment" for Agents
  14. March 28, 2023 BabyAGI — The First Widely Shared Autonomous LLM Agent
  15. March 30, 2023 AutoGPT — The Project That Defines "Autonomous Agent" in the Public Mind
  16. 2023 LangChain, AgentGPT, and the Framework Explosion
  17. March 12, 2024 Cognition's Devin — The First "AI Software Engineer" Agent
  18. Mar–May 2024 Multimodal & Long-Context Models Enable Capable Agents
  19. October 22, 2024 Anthropic's Computer Use — Agents That Operate Real Computers
  20. November 25, 2024 Model Context Protocol — A Standard for Agent–Tool Connections
  21. January 23, 2025 OpenAI Operator — Browser-Native Agentic AI for Consumers
  22. March 2025 Manus — General-Purpose Autonomous Agent Goes Viral
  23. March 2025 Agent SDKs from the Frontier Labs
  24. Q1–Q3 2025 The AI Agent Funding Wave
  25. November 24, 2025 Claude Opus 4.5 — Frontier Performance for Long-Horizon Agents
  26. Feb，25，2026， Hermes agent 发布

## Slide 7: Why Hermes?
* 视觉隐喻：
  * nousresearch Hermes agent 的logo 和风格
* 显示要点：
  * Open Source Project
  * 247K star · 34 releases · 3246 contributors 
  * Hermes 是一个活跃、快速增长的开源项目，是 Agent 演化分析的合适样本。
  * "最小核心 + 开放边缘"
  * Skills 自我沉淀：闭环学习让 agent 随使用自我进化
  * 作为用户和观察者

## Slide 8: Hermes release evolution 1: feature
* 视觉隐喻：
  * 一个不断生长的生命体
* 显示要点：
  * 阶段一：单 agent 的基础设施化：provider/model routing、tool calling、file operations、terminal execution、browser、memory/session、skills、MCP、messaging gateway
  * 阶段二：多 agent 与可编排：Kanban、durable goals、checkpoints、delegation/subagents、curator/self-improvement、background review fork、swarm/graph decomposition
  * 阶段三：agent 社会与 bot mode：Bot Mode、named agents、deterministic avatars、group chats、hermes peer、bot-to-bot DM、cron jobs with memory、cron continuity、steerable subagents、MCP command center


## Slide 9: Hermes release evolution 2: arch
* 视觉隐喻：
  * 不断重塑的宇宙
* 显示要点：
  * Messaging Gateway：从平台适配到公共表面
  * Profiles / Multi-instance：从单一用户到组织隔离
  * Transport ABC / Provider Layer：模型市场制度
  * Memory / Honcho / Session Search：从上下文到可治理知识
  * MCP：从外部协议到 command center
  * Desktop / Dashboard / TUI：消费面决定架构
  * God-file Refactor：维护制度被规模逼出来

## Slide 10:Demand, Supply, Consumers
* 视觉隐喻：
  * 修修补补、四面八方
* 显示要点：
  * 消费者画像：开发者 / 维护者、平台用户、远程/团队用户、研究者 / 自动化用户、部署者 / 运维者
  * 需求如何驱动架构：
    * 消息平台 → gateway 制度
    * 多人 → profile / multi-user / auth
    * 长任务 → cron / goals / checkpoints / Kanban
    * 桌面和远端 → Desktop / Dashboard / admin panel
    * 外部工具 → MCP / plugin / skills
    * 真实组织 → security / approval / state consistency / observability

## Slide 11: Token economic view
* 视觉隐喻：
  * 在用户和LLM之间存在着巨大的利润空间
* 显示要点：
  * Provider Layer 的早期制度：从散落调用到集中路由
  * LLM 厂商入口：为什么每个模型厂商都需要 agent runtime
  * Nous Portal / Tool Gateway：开源 agent 与商业服务的连续界面
  * 价格、缓存、配额：token 不是价格，而是成本感知系统
  * OAuth、订阅与入口权：从 API key 到订阅身份
  * Provider support is not just model compatibility. It is the institutional layer where AI agents meet the token economy.

## Slide 12： Tocken economy institutional

* 视觉隐喻：
  * 秩序
* 显示要点：
  * 入口：CLI、TUI、Desktop、Web Dashboard、ACP、gateway platforms：决定用户在哪里选择、切换、消耗模型。
  * 身份：PI key、OAuth、subscription、free tier、Nous login、Bitwarden/1Password secret source：决定谁有资格消耗 token 与工具权益。
  * 路由：provider router、Transport ABC、fallback chain、credential pools、provider_preferences、OpenAI-compatible proxy：决定一次任务使用哪个模型、哪个端点、哪个计费路径
  * 交易：pricing display、prompt caching、rate limit、usage、topup、subscription、model_overrides、MCP schema token estimates：决定用户能否理解并管理 token 成本
  * 治理：expensive selection confirmation、smart approvals、security hardening、credential vault、provider health check、fallback failover：决定高成本、高风险、高风险权限动作如何被批准与恢复
## Slide 13: Keep Movement
* 视觉隐喻：
  * 一切透明可见
* 显示要点：
  * 本slides 的源 markdown 文件：https://github.com/OCselected/markdown-to-slides
  * 
