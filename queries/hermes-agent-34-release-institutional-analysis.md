# Hermes Agent 34 Release Institutional Analysis

**对象：** NousResearch/hermes-agent 34 个 release（v2026.3.12 → v2026.9.14）  
**主题：** 来自真实世界的需求、消费、架构重构、issue/PR 解决与制度演化  
**研究立场：** 一个视角，不是定论。本分析基于 release notes 的公开文本，不替代完整 git 考古、维护者访谈或 issue 级抽样。

---

## 0. Source Registry

数据来源：GitHub Releases API / `gh release view`。

- Release list: https://github.com/NousResearch/hermes-agent/releases
- First analyzed release: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.3.12
- Latest analyzed release: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.14
- Key deep-dive release: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31
- Key reliability release: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.11

统计口径：
- 共 34 个 release。
- 时间范围：2026-03-12 至 2026-09-14。
- 部分早期 release notes 长达约 3.2 万到 4.9 万字符；后期多个 patch release notes 很短，但被大型 release 汇总说明。
- 本文优先使用 release notes 中的 H2/H3 章节、highlight bullet、PR/issue 引用、维护者自述和贡献者名单。

---

## 1. Release Cadence: 从高频功能发布到“大型汇总 + patch 标签”

Hermes 的 34 个 release 不是一条线性功能表，而更像一部制度演化史。早期版本密集地把“能做什么”快速展开；中期版本开始处理“如何维护这么大的系统”；后期版本转向“当很多人使用它时，状态、身份、安全、可靠性如何被制度化”。

### 1.1 早期：v2026.3.12–v2026.4.13（v0.2.0–v0.9.0）

特征：
- release notes 体量大，章节完整。
- 从 core agent、gateway、tool system、skills、MCP、browser、CLI、security 全面铺开。
- 每个 release 都是大版本，而不是单点修复。

代表 release：
- `v2026.3.12` v0.2.0：多平台 messaging gateway、ACP、MCP、skills、filesystem checkpoint、3,289 tests。
- `v2026.3.17` v0.3.0：Honcho memory、concurrent tool execution、PII redaction、Vercel AI Gateway、Anthropic native provider。
- `v2026.3.23` v0.4.0：OpenAI-compatible API server、MCP OAuth CLI、更多 messaging adapters、context references。
- `v2026.3.28` v0.5.0：Nous Portal 400+ models、Hugging Face provider、Telegram topics、Modal backend、plugin hooks。
- `v2026.3.30` v0.6.0：Profiles、MCP server mode、Docker、provider fallback chain、Feishu/Lark。
- `v2026.4.3` v0.7.0：pluggable memory provider、credential pools、Camofox browser、inline diffs、API session continuity。
- `v2026.4.8` v0.8.0：background process notifications、live model switching、GPT/Codex tool-use guidance、Gemini native provider。
- `v2026.4.13` v0.9.0：local web dashboard、fast mode、iMessage via BlueBubbles、WeChat/WeCom、Termux/Android。

研究判断：
- 这一阶段的需求主要来自“真实入口”：用户希望 Hermes 不只是 CLI，而是能出现在 Telegram、Discord、Slack、WhatsApp、Signal、Email、Home Assistant、Feishu、WeChat、WeCom、Android/Termux 等场景中。
- 这些入口不是抽象“平台扩展”，而是消费者侧的真实消费面。
- Agent 的“可用性”被需求重新定义：不是能不能回答，而是能不能进入用户已经在用的协作空间。

### 1.2 中期：v2026.4.23–v2026.6.19（v0.11.0–v0.17.0）

特征：
- 开始从“功能扩张”转向“平台化”和“工程复杂度治理”。
- TUI、Transport ABC、Desktop App、Kanban、Curator、插件、安全、Windows、Docker/Nix、Prompt caching 等出现。
- release notes 频繁出现“refactor”“salvage”“community contributors”“P0/P1”等词。

代表 release：
- `v2026.4.23` v0.11.0：Ink-based TUI、Transport ABC、Native AWS Bedrock、QQBot、WeCom/Weixin、DingTalk、Mattermost、Feishu、BlueBubbles。
- `v2026.4.30` v0.12.0：Autonomous Curator、self-improvement loop、ComfyUI、LM Studio provider、Gateway pluggability。
- `v2026.5.7` v0.13.0 Tenacity：durable multi-agent Kanban、persistent goals、checkpoints、video analyze、voice cloning、多语言静态消息。
- `v2026.5.16` v0.14.0：Windows native early beta、PyPI/supply-chain/Nix/Docker/ACP、xAI Grok OAuth、OpenAI-compatible local proxy、x_search、Microsoft Teams、debloating。
- `v2026.5.28` v0.15.0 Velocity：`run_agent.py` 16,000 行到 3,821 行、Kanban swarm、cold-start performance、session_search rebuild、promptware defense。
- `v2026.5.29` v0.15.1 Patch：dashboard 401 loop、Docker MCP command resolution、skills sidebar、Kanban worker kill。
- `v2026.6.5` v0.16.0 Surface：Hermes Desktop App、remote-gateway/multi-profile、web admin panel、简体中文 desktop、leaner skill set。
- `v2026.6.19` v0.17.0：iMessage Photon Spectrum、Raft agent network、background subagents、image-to-image、desktop 深化。

研究判断：
- 中期最大变化不是“功能更多”，而是“消费者变多”。
- 当消费面扩大到桌面、浏览器、IDE、移动端、网关、远程 gateway、multi-profile、Docker/Nix 时，单一 agent 文件/单一进程/单一 profile 的隐含假设开始失效。
- 于是出现 Kanban、Desktop、Dashboard、Transport ABC、Profiles、Plugin、MCP server/client 等制度容器。

### 1.3 后期：v2026.7.1–v2026.9.14（v0.18.0–v0.21.3）

特征：
- 从“功能扩张”转向“判断、可靠性、状态一致性、安全、消费侧体验”。
- release notes 出现 P0/P1 clean sweep、verification、self-improvement、performance spine、state.db reliability campaign。
- patch release 变多，且后续大版本会明确“roll up patch tags”。

代表 release：
- `v2026.7.1` v0.18.0 Judgment：P0/P1 clean sweep、Mixture-of-Agents、verification、`/learn`、`/journey`、coding cockpit、scale-to-zero、relay。
- `v2026.7.20` v0.19.0 Quicksilver：first-turn latency 从约 4.3 秒降到约 0.9 秒、desktop speed wave、smart approvals default、Bitwarden/1Password secret sources、performance。
- `v2026.8.3` v0.20.0：streaming conversational voice、wake words、voice on every platform、grounded citations、outbound webhooks、desktop performance。
- `v2026.8.31` v0.21.0 Pantheon：Bot Mode、`hermes peer`、cron jobs that remember、steerable subagents、MCP command center、desktop browser、provider/model wave、security hardening。release notes 自述 since v0.20.0: ~5,800 commits、~2,475 merged PRs、~2,100 issues closed、760+ contributors。
- `v2026.9.11` v0.21.2 state.db patch：state.db reliability campaign、six PRs、44 issues closed、multi-profile isolation hardening、password-blind credential vault。
- `v2026.9.14` v0.21.3：remote Desktop/Cloud patch，dashboard session expiry、duplicate state.db writer handles 等。

研究判断：
- 后期 release 的制度主题是“真实规模”。
- 真实规模不是 feature count，而是：多个 profile、多个 gateway、多个 desktop backend、多个 MCP server、多个 cron、多个 subagent、多个 remote users 同时触碰同一状态库。
- 因此 release 必须回答：谁写状态？谁能读什么？凭证如何不泄露？agent 出错时谁负责？session 如何延续？

---

## 2. 功能演化：从单 agent 到 agent 社会

### 2.1 阶段一：单 agent 的基础设施化

早期需求来自基础能力缺口：
- provider/model routing
- tool calling
- file operations
- terminal execution
- browser
- memory/session
- skills
- MCP
- messaging gateway

代表：v0.2.0–v0.9.0。

关键变化：
- Hermes 从“一个 agent loop”变成“一个可接入多平台和多工具的 runtime”。
- 需求不来自抽象 AI roadmap，而来自真实消费者入口：聊天平台、IDE、API、browser、terminal、Docker、手机终端、远程控制等。

制度意义：
- 功能演化的起点不是“更强模型”，而是“可被不同用户场景消费”。
- Messaging gateway 不是附加项，而是 Hermes 成为公共表面（public surface）的制度入口。

### 2.2 阶段二：多 agent 与可编排

中期出现：
- Kanban
- durable goals
- checkpoints
- delegation/subagents
- curator/self-improvement
- background review fork
- swarm/graph decomposition

代表：v0.12.0–v0.17.0。

关键变化：
- Agent 从“一个人做事”变成“团队做事”。
- 任务需要拆解、分派、回收、失败重领、heartbeat、durable state、worker lifecycle。

制度意义：
- 多 agent 本质上是协作制度，不是并行调用技巧。
- Kanban 是任务分配机制；subagent 是代理机制；checkpoint 是退出/恢复机制；curator 是知识治理机制。

### 2.3 阶段三：agent 社会与 bot mode

后期出现：
- Bot Mode
- named agents
- deterministic avatars
- group chats
- `hermes peer`
- bot-to-bot DM
- cron jobs with memory
- cron continuity
- steerable subagents
- MCP command center

代表：v0.21.0。

关键变化：
- Agent 不再只是执行者，而是可以被命名、寻址、组织成群聊、被 @mention、互相 DM 的社会单元。
- Cron job 也不再是一次性脚本，而是能记住历史、连续学习的定时行动者。

制度意义：
- 这是 agent 从 tool 到 institution 的关键跃迁。
- 当一个 agent 有名字、有 profile、有记忆、有 session、有 cron、有可审计对话记录，它已经接近“组织成员”而不是“工具”。

---

## 3. 架构重构：当消费面扩大，架构必须制度化为分层

### 3.1 Messaging Gateway：从平台适配到公共表面

早期：
- Telegram、Discord、Slack、WhatsApp、Signal、Email、Home Assistant。

中期：
- Mattermost、Matrix、Feishu/Lark、WeChat/WeCom、DingTalk、QQBot、iMessage/BlueBubbles、Microsoft Teams、Webhook、SMS/Twilio、Raft。

后期：
- voice on every platform
- outbound webhooks
- gateway/dashboard/desktop/backend 联动
- remote gateway / multi-profile

研究判断：
- Gateway 的价值不是“支持更多平台”，而是把 agent 暴露给真实消费者。
- 每个平台都是一个不同的权限、上下文、消息生命周期和身份边界。
- Gateway 最终成为“agent 的公共入口制度”，而不是消息转发层。

### 3.2 Profiles / Multi-instance：从单一用户到组织隔离

代表：
- v0.6.0 Profiles — Multi-Instance Hermes
- v0.16.0 remote-gateway & multi-profile
- v0.21.2 multi-profile isolation hardening
- v0.21.3 duplicate state.db writer handles

研究判断：
- Profile 不是配置目录，而是身份边界。
- 每个 profile 有 config、memory、sessions、skills、gateway service。
- 当多个 profile 共享机器、gateway、dashboard、Desktop backend 时，状态写入、session 读取、credential 获取都必须防止跨 profile 污染。
- 后期的 state.db reliability campaign 正是对早期“单用户本地工具”假设的修正。

### 3.3 Transport ABC / Provider Layer：模型市场制度

早期：
- centralized provider router
- provider fallback
- credential pools

中期：
- Anthropic native provider
- Gemini native provider
- Hugging Face
- Bedrock
- Codex / Responses API
- OpenAI-compatible proxy
- OAuth provider local proxy

后期：
- provider/model catalog wave
- model_overrides
- MoA
- model picker / reasoning mode / cache hit / latency / tokens per second

研究判断：
- Provider layer 是开源 agent 项目的“模型市场接口”。
- 它解决的不是单纯 API 调用，而是认证、计费、配额、缓存、流式、reasoning、fallback、prompt formatting 和成本可见性。
- 对开源而言，provider 多样化降低供应商锁定，提高消费者选择权。

### 3.4 Memory / Honcho / Session Search：从上下文到可治理知识

代表：
- Honcho Memory Integration
- Pluggable Memory Provider Interface
- Sessions & memory
- session_search rebuilt
- cron jobs that remember
- multi-user isolation

研究判断：
- Memory 是 agent 的长期记忆制度。
- 它不是缓存，而是跨 session、跨 profile、跨时间的知识产权和召回机制。
- 当 cron 有 memory，agent 才有持续性；当 memory provider 可插拔，agent 才允许外部知识系统进入治理边界。

### 3.5 MCP：从外部协议到 command center

代表：
- v0.2.0 MCP client
- v0.4.0 MCP server management CLI + OAuth 2.1 PKCE
- v0.6.0 MCP server mode
- v0.21.0 MCP command center
- v0.21.2/v0.21.3 MCP / dashboard / desktop backend 修复

研究判断：
- MCP 最初是工具接入协议，后来变成 agent 社会的互操作层。
- 当 MCP 数量增加，核心问题变成：发现、认证、健康检查、成本估算、schema token、usage、deep link install、failure recovery。
- MCP 不是“插件市场”，而是 agent 与外部世界之间的协议口岸。

### 3.6 Desktop / Dashboard / TUI：消费面决定架构

代表：
- Ink-based TUI
- Web Dashboard
- Local admin panel
- Hermes Desktop App
- Desktop drives browser
- desktop performance 60fps waves
- remote dashboard sessions

研究判断：
- UI 不是功能的包装层。
- 当 agent 被桌面、浏览器、CLI、远端 gateway、手机平台消费时，UX 会反向要求状态、认证、流式、通知、审批、session continuity 和 performance。
- Desktop App 的出现标志着 Hermes 从开发者 CLI 工具进入“日常办公/科研/管理入口”。

### 3.7 God-file Refactor：维护制度被规模逼出来

代表：
- v0.15.0 `run_agent.py` 16,083 到 3,821 行
- v0.17.0 god-file refactor wave (`run_agent.py` / `cli.py` / `gateway/run.py`)
- v0.18.0 composer / god-file de-entangle
- v0.21.0+ state/db writer handle 治理

研究判断：
- God file 不是代码品味问题，而是制度信号。
- 当单一文件承载太多职责，说明系统边界还没有制度化。
- Refactor 是把隐性耦合转成显性模块，是让多人贡献可继续发生的条件。

---

## 4. Issue / PR 解决：从 bug fix 到制度修复

release notes 中的 issue/PR 引用并不只是补丁列表，而是需求与风险的证据链。

### 4.1 需求侧 issue：来自消费面

常见需求来源：
- 平台接入：Discord、Telegram、Slack、WhatsApp、Signal、Feishu、WeChat、WeCom、DingTalk、QQBot、iMessage、Matrix、Mattermost、Teams、SMS、Webhook。
- Provider：Claude、GPT/Codex、Gemini、xAI、Nous、Hugging Face、Bedrock、LM Studio、MiniMax、Azure、Tencent、Meta、Nebius、CommandCode、Ramp、Actual Computer。
- UI：TUI、Dashboard、Desktop、ACP、browser、voice。
- Memory/session：search、compression、continuity、multi-profile。
- Security：redaction、credential、approval、prompt injection、secret leak、permission persistence。

研究判断：
- 真实需求不是抽象功能 wishlist，而是用户在具体入口中遇到的摩擦。
- 每个 issue 都是一次消费者侧的成本暴露。

### 4.2 供给侧 PR：来自社区与 maintainer 的治理

release notes 中频繁出现：
- salvage
- community contributors
- merged PR count
- top community contributors
- core team
- all contributors
- PR/issue links

代表：
- v0.21.0 since v0.20.0: ~2,475 merged PRs、~2,100 issues closed、760+ contributors。

研究判断：
- PR 是供给侧制度运行证据。
- Salvage 表明维护者需要把社区散落的贡献重新纳入可发布状态。
- Contributor 名单表明项目不是单人维护，而是一个贡献者治理系统。

### 4.3 Patch release：规模之后的可靠性压力

代表：
- v0.15.1 dashboard 401 reload loop
- v0.15.2 小修复
- v0.18.1/v0.18.2 patch
- v0.19.1 patch
- v0.20.1–v0.20.6 patch tags
- v0.21.1 patch
- v0.21.2 state.db reliability campaign
- v0.21.3 remote desktop/cloud patch

研究判断：
- patch release 是系统从“开发期”进入“部署期”的标志。
- 用户开始把 agent 当作长驻服务/日常工具，而不是一次性命令。
- 因此小 bug 会产生大制度成本：state.db、dashboard、credential、session、gateway、Desktop backend 都会影响持续信任。

---

## 5. 安全、审批、凭证：从“能做事”到“被允许做事”

### 5.1 安全边界的演化

早期：
- security & reliability
- PII redaction
- file safety
- credentials
- approval

中期：
- P0/P1 hardening
- promptware defense
- protected agent-instruction files
- Windows destructive command approval
- macOS TCC signing identity
- redaction sweep

后期：
- password-blind credential vault
- multi-profile isolation
- duplicate state.db writer handles
- remote dashboard session expiry
- MCP health/re-auth

研究判断：
- 安全问题不是附加检查，而是 agent 被授权参与现实的边界。
- 当 agent 能读写文件、运行命令、发消息、调 MCP、访问 memory、处理凭证，安全制度就是它的“行动许可”。

### 5.2 Smart approvals：从人工逐条确认到制度化判断

代表：
- v0.3.0 smart approvals / `/stop`
- v0.19.0 smart approvals default
- v0.21.0 protected agent-instruction files require write approval

研究判断：
- 审批不是摩擦，而是责任分配。
- 问题不是“要不要批准所有动作”，而是哪些动作允许 agent 自主，哪些必须人类确认。
- Smart approval 是风险判断机制，不是效率优化。

---

## 6. 真实世界的需求与消费：Hermes 的需求从哪里来？

### 6.1 消费者画像

从 release notes 可以反推出几类消费者：

1. **开发者 / 维护者**
   - 使用 CLI/TUI/Desktop。
   - 关注 terminal、file ops、git、code review、debug、MCP、subagent。

2. **平台用户**
   - 在 Telegram、Discord、Slack、Feishu、WeChat、WeCom、Teams、WhatsApp、Signal、iMessage 等环境中使用。
   - 关注消息、附件、session、@mention、group chat、voice note。

3. **远程/团队用户**
   - 使用 remote gateway、dashboard、multi-profile、Bot Mode、Bot Chat。
   - 关注权限、审计、多用户隔离、持续运行。

4. **研究者 / 自动化用户**
   - 使用 cron、delegation、Kanban、curator、grounded citations、MCP、subagents。
   - 关注持久任务、记忆、可验证结果、自我改进。

5. **部署者 / 运维者**
   - 使用 Docker、Nix、PyPI、installer、remote dashboard、Hermes Cloud。
   - 关注 build、state.db、service、upgrade、reliability。

### 6.2 需求如何驱动架构

Hermes 的架构演化不是从模型能力倒推出来的，而是被消费面反向牵引：

- 消费面扩展到消息平台 → gateway 制度。
- 消费面扩展到多人 → profile / multi-user / auth。
- 消费面扩展到长任务 → cron / goals / checkpoints / Kanban。
- 消费面扩展到桌面和远端 → Desktop / Dashboard / admin panel。
- 消费面扩展到外部工具 → MCP / plugin / skills。
- 消费面扩展到真实组织 → security / approval / state consistency / observability。

研究判断：
- Agent 的“能力”不是自足目标；能力必须被真实场景消费，才会变成产品制度。
- release 是需求的显影液：需求不一定写在 issue 里，但会在 release notes 的修复、重构和性能改进中显形。

---

## 7. 制度演化：从工具到制度

### 7.1 阶段模型

1. **Tool 阶段**
   - 单 agent、CLI、文件、terminal、tool use。
   - 制度问题弱，个人效率强。

2. **Gateway 阶段**
   - 多平台消息入口、session、media、approval。
   - 出现公共表面和权限边界。

3. **Platform 阶段**
   - profiles、dashboard、desktop、TUI、Docker、Nix、provider layer。
   - 系统需要安装、部署、升级、迁移、隔离。

4. **Organization 阶段**
   - Kanban、subagents、Bot Mode、cron memory、peer messaging、MCP command center。
   - 开始有角色、任务分配、沟通、记忆、责任。

5. **Institution 阶段**
   - state.db reliability、credential vault、approval、security hardening、observability、contributor governance。
   - 重点从“能做什么”变成“谁可以做什么、谁负责、如何恢复、如何审计”。

### 7.2 理论解释

用新制度经济学看：

- **科斯**：交易成本从代码提交/命令执行扩散到 approval、memory、state.db、MCP、session、credential、dashboard 等多个制度摩擦点。
- **威廉姆森 L1→L4**：
  - L1：agent 的价值观/文化：Keep Movement、开源协作、社区贡献。
  - L2：治理规则：license、approval、security、profile isolation。
  - L3：机制：gateway、cron、Kanban、MCP、subagent、dashboard。
  - L4：资源配置：PR、contributors、commits、issues、providers、tools。
- **奥斯特罗姆**：多 agent、多用户、多平台系统需要共享池治理：谁能改 skill、谁能写 memory、谁能调用 MCP、谁能批准命令。
- **阿西莫格鲁**：Hermes 的演化更像包容性制度：上游贡献、社区 salvage、多 profile、开放 provider、可插拔 memory/plugin；其成熟取决于这些机制是否继续开放，而非变成锁定。

---

## 8. 对 AgentCon Slide 的可复用结论

面向 20 分钟英文分享，可压缩为 6–8 个核心判断：

1. **Agent evolution is driven by real consumption, not model claims.**
   - Hermes 的需求来自 CLI、gateway、desktop、mobile、browser、IDE、cron、team chat，而不是抽象 benchmark。

2. **Gateway made Hermes public.**
   - 平台接入让 agent 从个人工具变成公共表面。

3. **Profiles turned Hermes into a multi-user institution.**
   - 每个 profile 是身份、记忆、session、skill、gateway 的边界。

4. **Kanban and subagents made agent work organizational.**
   - 多 agent 不是并行执行，而是任务分配、交接、回收和治理。

5. **MCP became a protocol port, not just a tool list.**
   - MCP 数量增长后，问题变成认证、发现、健康检查、成本、审计和 deep link。

6. **Refactoring is institutional work.**
   - God-file refactor、Transport ABC、provider layer、state.db governance 都是制度重构。

7. **Reliability is the new feature.**
   - state.db、duplicate writers、session expiry、dashboard auth、credential vault 是规模之后的真实需求。

8. **Agent is becoming a participant, not only a tool.**
   - Bot Mode、named agents、group chats、cron memory、peer messaging 指向 agent 社会。

---

## 9. 后续研究 TODO

若要深化，不应再停留在 release notes 摘要，而应做三类证据：

1. **Issue 级抽样**
   - 抽取每个大版本中关闭的 P0/P1、state.db、gateway、desktop、MCP、memory、security 相关 issue。
   - 标记需求类型：用户摩擦、部署问题、安全漏洞、平台适配、消费体验、维护者治理。

2. **PR 级抽样**
   - 抽取 salvage PR、community PR、maintainer PR。
   - 观察贡献者进入路径和收益分配。

3. **代码边界抽样**
   - 对比 v0.2.0、v0.12.0、v0.18.0、v0.21.0 的目录结构。
   - 验证 release notes 中的架构重构是否在代码边界中真实发生。

研究立场保持：这是开放观察，不是企业评价。

---

## 10. Token Economy 视角：模型支持演变是入口经济与平台治理

### 10.1 核心判断

Hermes Agent 对 model/provider 的支持演变，不是一般意义的“接入更多模型”。它更像是围绕 token 经济建立的一套入口、路由、认证、计费、缓存、降级和用户选择制度。

可以从三个方向理解：

1. **LLM 厂商希望获得更多入口**
   - ChatGPT/Codex、Claude、Gemini、Grok、Nous Portal、Hugging Face、Bedrock、LM Studio、OpenRouter、Vercel AI Gateway 等都需要一个能触达 agent 工作流的入口。
   - Hermes 不是单纯“调用 API”的工具，而是把模型选择变成用户每日工作流的一部分。

2. **Nous Research 也把 Hermes 变成商业模型与工具入口**
   - Nous Portal、Nous Tool Gateway、Nous free tier、subscription/topup、pricing display、recommended models、model catalog、tool entitlement 等，说明开源 agent 与商业服务之间有连续界面。
   - Hermes 的 provider 层不是只服务第三方厂商，也服务 Nous 自己的 Portal/Tool Gateway 生态。

3. **Token economy 的核心是交易界面**
   - token 不是孤立的 API 计费单位，而是由入口、身份、认证、路由、缓存、配额、价格显示、模型目录、fallback、用量反馈共同构成的交易界面。
   - 谁掌握入口，谁就影响用户消费 token 的路径、成本感知和厂商选择。

---

### 10.2 Provider Layer 的早期制度：从散落调用到集中路由

早期 release 中 provider 支持的变化，重点不是“多一个模型”，而是建立统一入口。

代表节点：
- `v2026.3.12` v0.2.0：Centralized provider router、`resolve_provider_client()`、`call_llm()` API、Nous Portal first-class provider、OpenAI Codex Responses API、OpenRouter routing。
- `v2026.3.17` v0.3.0：Vercel AI Gateway、Anthropic native auxiliary vision、Anthropic OAuth flow、direct endpoint overrides。
- `v2026.3.23` v0.4.0：GitHub Copilot、Alibaba Cloud / DashScope、Kilo Code、OpenCode Zen/Go 等 new providers。
- `v2026.3.28` v0.5.0：Hugging Face first-class provider、Nous Portal 400+ models、Nous Portal model slugs align with OpenRouter naming。
- `v2026.3.30` v0.6.0：ordered fallback provider chain、Gemini preview models、stop silent OpenRouter fallback。

制度意义：
- provider router 是 token economy 的“交易中介”。
- 它把模型调用从分散的脚本/API key 行为，变成可配置、可切换、可回退、可观察的资源路由。
- 当 Hermes 能自动识别 provider、切换 model、保留 custom endpoint、清除 stale `api_mode`、阻止 silent OpenRouter fallback，它就在建立一种“不误导用户”的交易透明度。

---

### 10.3 LLM 厂商入口：为什么每个模型厂商都需要 agent runtime

Hermes 的 provider 演变显示，LLM 厂商并不只想被 API 调用，而是希望进入 agent 的日常行动环境。

主要厂商/入口：
- OpenAI / Codex：Responses API、Codex OAuth、GPT/Codex tool-use guidance、Fast Mode、developer role、Codex runtime。
- Anthropic / Claude：native Anthropic provider、Claude Code credential auto-discovery、OAuth PKCE、prompt caching、native auxiliary vision。
- Google / Gemini：Google AI Studio native provider、Gemini CLI OAuth、models.dev integration、Gemini routed through AI Studio API。
- xAI / Grok：xAI native provider、xAI Grok prompt caching、SuperGrok OAuth。
- Nous Research：Nous Portal、Nous Tool Gateway、Nous recommended models、Nous free tier。
- Hugging Face：first-class inference provider、agentic model picker。
- AWS Bedrock：native Bedrock provider。
- OpenRouter：routing、catalog、pricing、fallback、provider_preferences。
- Vercel AI Gateway：dynamic discovery、pricing、attribution。
- 其他：DashScope、Qwen OAuth、LM Studio、MiniMax、Tencent Tokenhub/TokenPlan、Azure AI Foundry、Meta Model API、CommandCode、Nebius Token Factory、Ramp Router、Actual Computer。

研究判断：
- LLM 厂商需要的不是“被列表收录”，而是进入 agent runtime 的执行环境。
- Agent runtime 决定模型如何被调用、如何显示价格、如何处理 OAuth、如何缓存、如何 fallback、如何被用户中途切换。
- 因此 provider 支持是入口战，不是技术兼容列表。

---

### 10.4 Nous Portal / Tool Gateway：开源 agent 与商业服务的连续界面

Nous 相关入口在 release 中逐渐变清晰：
- v0.2.0：Nous Portal as first-class provider。
- v0.5.0：Nous Portal supports 400+ models。
- v0.8.0：Nous Portal free-tier model gating、pricing display。
- v0.10.0：Nous Tool Gateway for paid Nous Portal subscribers: web search、image generation、TTS、vision etc.
- v0.12.0：remote model catalog manifest from OpenRouter + Nous Portal catalogs。
- v0.16.0：Always show Nous Tool Gateway backends、login on select、surface Nous free tool pool、route FAL video gen through managed Nous gateway。
- v0.17.0：persist Nous recommended-models to disk、fall back on Portal failure。
- v0.21.2：Nous free tier and guided first launch。

制度意义：
- Nous Portal 是模型供给入口。
- Nous Tool Gateway 是工具供给入口。
- free tier、subscription、topup、pricing display 是消费制度。
- Hermes 不是单纯开源项目，而是 Nous 商业生态与开源 agent 用户之间的连续界面。

关键问题：
- 开源入口如何吸引用户？
- 免费层如何降低首次消费门槛？
- 付费订阅如何获得工具权益？
- Nous 推荐模型如何影响用户选择？
- OpenRouter/第三方模型与 Nous Portal 模型之间如何显示价格与缓存优势？

这些不是 UI 问题，而是 token economy 的制度设计。

---

### 10.5 价格、缓存、配额：token 不是价格，而是成本感知系统

release notes 中多次出现 pricing、prompt caching、rate limit、usage、topup、subscription。

代表节点：
- v0.8.0：Model pricing display for OpenRouter and Nous Portal、xAI Grok prompt caching。
- v0.9.0：Fast Mode、rate limit header capture shown in `/usage`。
- v0.14.0：OpenRouter Pareto Code router、Codex runtime、OpenAI-compatible local proxy for OAuth providers。
- v0.17.0：Anthropic adaptive models、expensive selection confirmation。
- v0.19.0：`/subscription` and `/topup`、smart approvals default。
- v0.21.0：model catalog wave、model_overrides lets users patch context window or pricing themselves。

研究判断：
- token economy 的核心不是 token 单价，而是用户对成本的可感知性和可控制性。
- Hermes 通过 pricing display、prompt caching、rate limit、usage、model_overrides、fallback 与 expensive selection confirmation，把 token 从“看不见的水电”变成“可管理的资源配置”。
- 这也解释了为什么性能、prompt caching、model picker、latency、tokens/sec、cache-hit% 都是 token economy 的一部分。

---

### 10.6 OAuth、订阅与入口权：从 API key 到订阅身份

provider 演化中有一类重要变化：从 API key 到 OAuth / subscription / identity。

代表：
- Codex OAuth、ChatGPT subscription support。
- Anthropic OAuth flow / Claude Code credential auto-discovery。
- GitHub Copilot OAuth。
- Google Gemini CLI OAuth。
- xAI SuperGrok OAuth。
- MiniMax OAuth PKCE。
- Nous Portal / Nous Tool Gateway login、free tier、subscription、topup。

研究判断：
- API key 是机器凭证，OAuth/subscription 是用户身份和权益系统。
- 厂商通过 OAuth/subscription 不只是完成认证，还把用户订阅、权益、免费层、模型推荐和工具入口绑定起来。
- Hermes 作为开源 agent，天然成为这些身份系统进入 agent 工作流的入口。

这带来两个制度问题：
- 用户选择模型时，是在选择技术能力，还是在选择厂商订阅身份？
- agent 的开放性是否会转化为模型/工具厂商的渠道优势？

---

### 10.7 Token Economy 的制度框架

可以把 Hermes 的 model/provider 演化整理为五层：

1. **入口层**
   - CLI、TUI、Desktop、Web Dashboard、ACP、gateway platforms。
   - 决定用户在哪里选择、切换、消耗模型。

2. **身份层**
   - API key、OAuth、subscription、free tier、Nous login、Bitwarden/1Password secret source。
   - 决定谁有资格消耗 token 与工具权益。

3. **路由层**
   - provider router、Transport ABC、fallback chain、credential pools、provider_preferences、OpenAI-compatible proxy。
   - 决定一次任务使用哪个模型、哪个端点、哪个计费路径。

4. **交易层**
   - pricing display、prompt caching、rate limit、usage、topup、subscription、model_overrides、MCP schema token estimates。
   - 决定用户能否理解并管理 token 成本。

5. **治理层**
   - expensive selection confirmation、smart approvals、security hardening、credential vault、provider health check、fallback failover。
   - 决定高成本、高风险、高风险权限动作如何被批准与恢复。

---

### 10.8 对 AgentCon 分享的可复用表达

可以这样表达：

> Provider support is not just model compatibility. It is the institutional layer where AI agents meet the token economy.

中文解释：
- provider support 不是“模型兼容”。
- 它是 agent 与 token 经济相遇的制度层。
- LLM 厂商需要入口；Nous 需要商业模型与工具入口；用户需要可理解的价格、可切换的模型、可回退的路由；开源社区需要保持开放与选择权。

一句话结论：
> Hermes 的 model/provider 演化，展示了开源 agent runtime 如何成为 LLM 厂商、工具厂商和用户之间的 token 交易界面。

---

### 10.9 后续深挖方向

如果要继续深入，建议围绕以下证据做专项分析：

1. **Provider timeline**
   - 统计每个 provider 首次出现、后续增强、成为 first-class provider、支持 OAuth、支持 pricing、支持 prompt caching 的时间点。

2. **Nous Portal vs third-party providers**
   - 比较 Nous Portal、OpenRouter、Codex、Claude、Gemini、xAI 在 release notes 中的入口位置。
   - 观察 Nous recommended models、free tier、Tool Gateway 与第三方模型并置时，Hermes 如何呈现选择权。

3. **Token cost visibility**
   - 抽取 pricing display、prompt caching、usage、topup、subscription、model_overrides、cache-hit、tokens/sec、latency 等证据。
   - 做一张“成本可见性演化图”。

4. **OAuth and identity**
   - 统计 OAuth provider 数量与认证路径。
   - 分析 API key、OAuth、subscription、credential pool、secret source 的治理差异。

5. **Entry power**
   - 讨论开源 agent runtime 是否成为模型厂商的分发渠道。
   - 如果 Hermes 用户增长，LLM 厂商会怎样理解这个入口？Nous 的商业模型又怎样通过 Portal/Tool Gateway 反哺开源用户？

