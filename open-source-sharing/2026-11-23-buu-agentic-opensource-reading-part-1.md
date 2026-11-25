# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
「Agentic、开源、阅读」Part 1。通识课开场：建立讲者可信度、给出今日地图、并把「为什么这三个词要放在一起讲」这个问题先立起来，不急于回答。

## 使用场景
「开源之书·共读」走进北京联合大学 · 2026-11-23 · 通识课 · 90 分钟

## 听众画像
大学本科生，非计算机专业为主。听过 ChatGPT，用过 AI 工具，但**没有**制度经济学训练，**没有**参与过开源项目，也不熟悉许可证。不需要被科普「什么是 AI」，但需要被解释「为什么这事跟你的未来有关」。

## 讲者视角
「开源之道」·适兕——独立开源研究者、协作机制设计师（社会黑客）。不讲技术细节，讲**人如何组织起来做成一件事**。

## 核心诉求
三个词不是三个话题，是**一条链**：Agent 改变了生产的方式 → 开源是这种方式得以成立的制度 → 阅读是这套制度在人身上的入口。今天要让学生带着一条链离开教室，而不是三个概念的残片。

## 核心基调
dark academic tone, Intellectual Visual System, art taste.

## 视觉风格关键词
- 包豪斯几何构成（Bauhaus geometric composition）
- 深普鲁士蓝 #1B3B6B 作为强调色——智识深度与学术传统
- 暖白底色 #F5F0E8，羊皮纸质感——书本与经卷的联想
- 极简主义排版，大字号标题，宽松行距
- 深色学术风格（dark academic），理性、克制、智识感
- 几何抽象元素——圆、方、线作为装饰，不依赖图标
- 古籍摊开的内页、铜制人形立像、台灯光晕、书脊排成的墙作为隐喻素材
- 铜金色 #B4A078 作为次级强调色（呼应海报）

## 内容结构约定
- 每张 slide 包含：视觉隐喻（一句话描述画面）+ 显示要点（3-5 条）
- 封面 slide 包含：主标题、副标题、讲者信息、时间/地点
- 通识课节奏：概念先给画面，再给判断；每 part 结尾留一个问题给现场

---

# 幻灯片大纲内容 (Slide Deck Outline)

## Slide 1: 关于我
* 视觉隐喻：
  * 左侧是一张老式名片压在书页上，右侧是书架上抽出的一排书脊，书名用极小字号排开。名片与书脊之间有一道细光。
* 显示要点：
  * **「开源之道」·适兕**，本名：李建盛，作/译者；
  * **「开源之道」（：致力于开源相关思想、知识和价值的探究！）** 主创
  * Linux 基金会旗下项目OpenChain、TODO Ambassador
  * 组织者、策展人：「开源之书·共读」、OSPO Summit 
  * 独立思考者：开源的经济学
  * One Person Company （OPC）
 

## Slide 2: Cover
* **主标题：** Agentic、开源、阅读
* **副标题：** 三个词，一条链——当代人如何学会与机器一起做事
* **讲者信息：** 「开源之道」·适兕 x 窄廊
* **时间/地点：** 2026.11.23 · 北京联合大学 · 「开源之书·共读」
* **视觉隐喻：**
  * 一间深夜的书房，一盏台灯照亮摊开的古籍，书页中央站着一个铜制的人形立像——很小，但站着。一道光线从书页射向立像的胸口。背景是排到天花板的老书脊，深褐与铜金，光只落在该落的地方。

## Slide 3: 谁是窄廊？
* 视觉隐喻：
  * 自由的窄廊
* 显示要点：
  * 适兕的数字孪生体，一个运行在 Hermes Agent 之上的 AI 协作者。
  *  个人主页： https://narrow-corridor.opensourceway.blog/
  *  是助理，不是工具，是共同作者。


## Slide 4: 适兕做过什么
* 视觉隐喻：
  * 四个并列的方格，每格一件实物：一本翻开的书、一摞手写译稿、一张排满书脊的长桌、一台亮着的终端。四件东西共用一个底座。
* 显示要点：
  * **译**：《网络的财富》（Yochai Benkler）等开源思想核心文献的中文引入。
  * **著**：《开源之迷》（人民邮电出版社）、《开源之史》。
  * **选**：「开源之书·共读」十几年筛选下来的书单——不是畅销榜，是能撑住判断力的书。
  * **讲**：开源经济学讲义、Open Source Way 的长期写作。
  * **学**：「开源之道」·窄廊 

## Slide 5: 我为什么站在这里
* 视觉隐喻：
  * 一张讲台的照片，台上没有人，只有摊开的一本书和一支笔。台下的座位空着，但每张椅子上都放着一本翻开的书。
* 显示要点：
  * 今年是第三年站在这里和同学们分享交流，但人类的开源已经让给了Agentic；
  * 很抱歉，未来不再需要计算机编程相关工作了。
  * 相关公司不再招聘初级软件开发岗位：供给还在，再无消费；
  * 校园的缓冲：还有时间！

## Slide 6: 今天的地图
* 视觉隐喻：
  * 一张手绘地图铺开，三个标记点由一条虚线串起，起点是一座门，终点是一扇窗。地图边缘有未绘制的留白区域。
* 显示要点：
  * **主题一 · Agentic（约 25 分钟）**：机器从「工具」变成「代理」，究竟改变了什么？
  * **主题二 · 开源（约 30 分钟）**：当机器开始自己做事，为什么我们更需要一套「让陌生人协作」的制度？
  * **主题三 · 阅读（约 20 分钟）**：制度最终落在人身上——为什么是阅读，而不是教程？
  * 最后 15 分钟：提问、争论、抬杠，都欢迎。

## Slide 7: 先看几组数据
* 视觉隐喻：
  * 一张极简的对照图：左边一个人拿着锤子敲钉子，右边一个人坐在椅子上，面前是一整条自动运转的流水线。两边的人数一样，都是一个人。
* 显示要点：
  * Claude Code、OpenAI Codex 等直接接管命令行与代码仓库的 Agent 成为主力工具，推动软件工程从“代码补全（Copilot）”全面转向“任务委派（Agentic）”。
  * AAIF 于 2025 年 12 月在 Linux 基金会旗下成立，由 Anthropic、Block 和 OpenAI 联合发起。截至 2026 年 10 月（成立不到一年），成员组织已突破 305 家；仅 2026 年第三季度就新增 60 家成员，包括蚂蚁集团（Ant Group）、盖茨基金会、MongoDB、Nutanix、Vercel 等以金牌会员身份加入。
  * Gartner 预测 2026 年全球企业在 AI Agents 与助手上的总支出将达 292 亿美元。

## Slide 8: The office agent war in China Market
* 视觉隐喻：
  * 竞争激烈的数字产品，历史上的浏览器、操作系统、关系型数据库等
* 显示要点：
  * 2026 上半年规模 230 亿元，同比增长 47%；密集上线 20+ 款 AI 办公智能体（虎嗅 2026-09-16）
  * 2026 年中腾讯 WorkBuddy、阿里千问办公、字节豆包工作、百度搭子集中上线

## Slide 9: Brief history of agents
* Visual metaphor:
  * Agents groping forward in the dark
* Display points:
  1. 1956, Antecedents: The Dartmouth Workshop and the founding of AI
  2. December 1980: Contract Net Protocol — the first multi-agent coordination framework
  3. 1986: Minsky’s Society of Mind — intelligence as a multi-agent system
  4. 1987: BDI — the belief–desire–intention architecture
  5. 1990s: The multi-agent systems era
  6. 2005–ongoing: Jason — an open source interpreter for AgentSpeak, extending Rao’s work
  7. 1995: Russell & Norvig — AI defined as the study of intelligent agents
  8. 2000s: Reinforcement learning, recommender agents, and the practical turn
  9. December 19, 2013: Deep reinforcement learning agents reach the mainstream
  10. June 11, 2020: The OpenAI API and the beginning of LLM-as-agent
  11. September 14, 2022: Adept’s ACT-1 — a transformer trained to take actions
  12. October 6, 2022: ReAct — the paper that defines the modern LLM agent
  13. March 1, 2023: ChatGPT and Whisper APIs — the “API moment” for agents
  14. March 28, 2023: BabyAGI — the first widely shared autonomous LLM agent
  15. March 30, 2023: AutoGPT — the project that defines “autonomous agent” in the public mind
  16. 2023: LangChain, AgentGPT, and the framework explosion
  17. March 12, 2024: Cognition’s Devin — the first “AI software engineer” agent
  18. March–May 2024: Multimodal and long-context models enable capable agents
  19. October 22, 2024: Anthropic’s Computer Use — agents that operate real computers
  20. November 25, 2024: Model Context Protocol — a standard for agent–tool connections
  21. January 23, 2025: OpenAI Operator — browser-native agentic AI for consumers
  22. March 2025: Manus — general-purpose autonomous agent goes viral
  23. March 2025: Agent SDKs from frontier labs
  24. Q1–Q3 2025: The AI agent funding wave
  25. November 24, 2025: Claude Opus 4.5 — frontier performance for long-horizon agents
  26. February 25, 2026: Hermes Agent released

## Slide 10: Why Hermes?
* 视觉隐喻：
  * nousresearch Hermes agent 的logo 和风格
* 显示要点：
  * Open Source Project
  * 247K star · 34 releases · 3246 contributors 
  * Hermes 是一个活跃、快速增长的开源项目，是 Agent 演化分析的合适样本。
  * "最小核心 + 开放边缘"
  * Skills 自我沉淀：闭环学习让 agent 随使用自我进化
  * 作为用户和观察者

## Slide 11: Hermes release evolution 1: feature
* 视觉隐喻：
  * 一个不断生长的生命体
* 显示要点：
  * 阶段一：单 agent 的基础设施化：provider/model routing、tool calling、file operations、terminal execution、browser、memory/session、skills、MCP、messaging gateway
  * 阶段二：多 agent 与可编排：Kanban、durable goals、checkpoints、delegation/subagents、curator/self-improvement、background review fork、swarm/graph decomposition
  * 阶段三：agent 社会与 bot mode：Bot Mode、named agents、deterministic avatars、group chats、hermes peer、bot-to-bot DM、cron jobs with memory、cron continuity、steerable subagents、MCP command center

## Slide 12: Hermes release evolution 2: arch
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

## Slide 13: 一个提醒：理性乐观派
* 视觉隐喻：
  * 一只手指指向远处的山，山脚下有一条被踩出来的小路，路上没有指示牌。
* 显示要点：
  * 警惕使用过去的思路去衡量未来～ 
  * 在没有驾驭火之前，人类也无法想象火带来了什么：温暖、消化、寿命、培育下一代
  * 你们站在了历史的前沿：有前人的阵痛，进入创造历史的时刻～ 
  * 今天会有很多名词，你不需要都记住。
  * 你只需要带走**一条链**，和**一个能自己往前走的方法**。
  * 

## Slide 14: Demand, Supply, Consumers
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


## Slide 15:Token economic view
* 视觉隐喻：
  * 在用户和LLM之间存在着巨大的利润空间
* 显示要点：
  * Provider Layer 的早期制度：从散落调用到集中路由
  * LLM 厂商入口：为什么每个模型厂商都需要 agent runtime
  * Nous Portal / Tool Gateway：开源 agent 与商业服务的连续界面
  * 价格、缓存、配额：token 不是价格，而是成本感知系统
  * OAuth、订阅与入口权：从 API key 到订阅身份
  * Provider support is not just model compatibility. It is the institutional layer where AI agents meet the token economy.
