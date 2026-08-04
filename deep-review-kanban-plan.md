# 论文阅读 Deep Review — Hermes Kanban 工程方案

> 日期：2026-08-04
> 产出：窄廊
> Board：`deep-review-wiki`
> 主参考文件：`论文阅读-folder-inventory.md` / `论文阅读-deep-review-plan.md`

---

## 1. 工程全景

**总任务量：** 204 件物品 -> 5 级分类 -> 8 个 Phase -> 40+ 张 Kanban 卡片
**执行模型：** 窄廊（AI worker profile = `default`），单 worker 串行+批次执行
**每篇耗时估计：** 完整 Deep Review ~ 8-12 分钟，快速评估 ~ 2-3 分钟
**总耗时：** 约 7.5-9.5 小时（AI 执行时间，不含等待）

---

## 2. 任务依赖关系

```
Phase 1 (NIE基石) --> Phase 2 (开源经济学) --> Phase 3 (大分流)
        |                     |                      |
        +----------------------+----------------------+
                               v
                        Phase 4 (OSPO)
                               v
                        Phase 5 (AI+制度)
                               v
                        Phase 6 (B级快速评估)
                               v
                        Phase 7 (C级标记归档)
                               v
                        Phase 8 (综合产出)
```

Phase 1-8 是依赖链，Phase 4-6 是 Phase 2-3 完成后才可做的派生任务。

---

## 3. 每篇 Deep Review 的产出规范

每张卡片执行时产出以下文件：

| 产出文件 | 路径 | 说明 |
|---------|------|------|
| 书卡/论文卡 | `wiki/raw/articles/paper_or_book_reading/<slug>.md` | frontmatter + 5段结构化内容 |
| 桥接概念页 | `wiki/raw/articles/concepts/<bridge-name>.md` | 与适兕思想体系的交叉连接 |
| 札记 | `wiki/raw/articles/issues-musings/<日期>-<主题>.md` | 可选，如有值得记录的观点 |

**每篇 Deep Review 的标准 frontmatter：**
```yaml
title: ""
author: ""
year: 
source: ""
source_name: ""
language: ""
type: paper|book
ISBN: TBD
douban_rating: 
ai_judgement: "窄廊独立产出 Deep Review，桥接概念：XXX"
```

**每篇 Deep Review 的正文结构：**
1. 作者与出版信息
2. 核心框架（论文/书籍的核心论证）
3. 关键概念（提取 3-5 个核心概念）
4. 桥接概念（与适兕思想体系的交叉，必须有来源标注）
5. 与其他文献的连接（已有 book/paper 列表）

---

## 4. 8 个 Phase 的完整任务清单

### Phase 1 — NIE 基石（5篇）
*依赖：无 | 优先级：最高*

| 卡片 | 文献 | 预计产出 |
|------|------|---------|
| P1-1 | Acemoglu and Robinson 2025: Culture Institutions Social Equilibria (JEL) | bridge concept: 文化均衡 |
| P1-2 | Acemoglu 2026: AI Human Cognition Knowledge Collapse | bridge concept: AI知识崩塌 |
| P1-3 | Acemoglu 2024: The Simple Macroeconomics of AI | bridge concept: AI宏观经济学 |
| P1-4 | Greif-Tabellini 2010: Cultural and Institutional Bifurcation (AER) | bridge concept: 文化-制度分叉 |
| P1-5 | Williamson 2000: Taking Stock（已有deep review，标记为done） | 无需重复 |

### Phase 2 — 开源经济学核心（10篇）
*依赖：Phase 1 完成*

| 卡片 | 文献 | 预计产出 |
|------|------|---------|
| P2-1 | Lerner and Tirole 2006: Economics of Technology Sharing: Open Source and Beyond | bridge: 技术共享经济学 |
| P2-2 | Gehring 2006: Institutionalization of Open Source | 已有书卡，需补 deep review |
| P2-3 | Akşulu and Wade 2010: Open Source Research Review | bridge: OSS研究综述 |
| P2-4 | Dahlander and Magnusson 2005 | bridge: OSS企业-社区二元性 |
| P2-5 | Engelhardt and Freytag 2010 | bridge: OSS制度与文化 |
| P2-6 | Bessen 2006: Open Source Complex Public Goods | bridge: 复杂公共品 |
| P2-7 | Bitzer and Schröder 2006 | bridge: OSS开发经济学 |
| P2-8 | Ciesielska 2010: Hybrid Organisations | bridge: OSS混合组织 |
| P2-9 | Baldwin-von Hippel 2011: Modeling a Paradigm Shift | bridge: 范式转换 |
| P2-10 | What Economists Know about OSS | 综述文章 |

### Phase 3 — 大分流制度演化（8篇）
*依赖：Phase 1 完成*

| 卡片 | 文献 | 预计产出 |
|------|------|---------|
| P3-1 | Greif: Institutions and the Path to the Modern Economy（大裂变英文版） | bridge: 中世纪贸易制度 |
| P3-2 | 彭慕兰: 大分流（中文版） | bridge: 大分流2.0理论底座 |
| P3-3 | 秦晖: 传统十论 | bridge: 本土制度 |
| P3-4 | March and Olsen: 重新发现制度 | bridge: 制度重新发现 |
| P3-5 | Mary Douglas: 制度如何思考 | bridge: 制度的心智模型 |
| P3-6 | Powell and DiMaggio: 组织分析的新制度主义 | bridge: 制度同构 |
| P3-7 | Nelson and Winter: 经济变迁的演化理论 | bridge: 演化经济学 |
| P3-8 | Williamson: 资本主义经济制度（中文版） | 已有book卡，需补deep review |

### Phase 4 — OSPO体系（7篇）
*依赖：Phase 2 完成*

| 卡片 | 文献 | 预计产出 |
|------|------|---------|
| P4-1 | OSPO Book (2026-07 完整版) | bridge: OSPO全书 |
| P4-2 | The Rise of the OSPO | bridge: OSPO兴起 |
| P4-3 | The Business Value of the OSPO | bridge: OSPO商业价值 |
| P4-4 | Evolution of OSPO Report | bridge: OSPO演化 |
| P4-5 | SR Issue Brief: Operating OSPOs at System Level | bridge: 系统级OSPO |
| P4-6 | 2023 The Business Value of OSPO | 可能重复，需比对 |
| P4-7 | Institutional Complexity in OSS Ecosystems (Moradi 2024) | bridge: OSS生态制度复杂性 |

### Phase 5 — AI+制度交叉（10篇）
*依赖：Phase 3 完成*

| 卡片 | 文献 | 预计产出 |
|------|------|---------|
| P5-1 | NBER w34468: Coasean Singularity | bridge: 科斯奇点 |
| P5-2 | Ghosts of Electricity | bridge: 稀缺的未来 |
| P5-3 | 202605.00224v1 (arXiv) | 待定 |
| P5-4 | Agents Economics 2509-01063 (arXiv) | bridge: Agent经济 |
| P5-5 | Agents Markets 2509-10147 (arXiv) | bridge: Agent市场 |
| P5-6 | Markets Agency Trust AI Knowledge Problem | bridge: 代理-信任问题 |
| P5-7 | 面向设备/企业/国家/生命的AI操作系统 | bridge: AI操作系统 |
| P5-8 | Open Source and the Future of AI: Report 2026 | bridge: 开源+AI未来 |
| P5-9 | How Open Source ML Shapes AI | bridge: OSS塑造AI |
| P5-10 | 一个词是怎么死的 | 已有深读，归档链接 |

### Phase 6 — B级快速评估（约30篇）
*依赖：Phase 4-5 完成*

先做快速摘要（2-3分钟/篇），再决定是否需要完整 Deep Review：
- Innovation Commons (Potts)
- General Theory of Economic Evolution (Dopfer and Potts)
- Bourgeois Equality (McCloskey)
- Against Intellectual Monopoly (Boldrin and Levine)
- What We Owe the Future (MacAskill)
- Politicizing Business (Ning Leng)
- The Company of Strangers (Seabright)
- 抛弃版权 / 谁害怕亚当斯密 / 陌生人群
- 经济运行的逻辑 / 基层中国
- 食人资本主义 / 天朝的崩溃
- 制度是如何形成的 / 观念史研究
- 大侦探经济学
- 芯片战争 / 创新跃迁 / 可复制的成功
- 中国 OSS Stakeholders Report
- Innovation Blowback
- Open at Core
- 中国Stakeholders Report

### Phase 7 — C级标记归档（约130件）
*依赖：无（可并行执行）*

纯个人阅读/时事/营养类/管理类/非学术。不纳入知识图谱。
标记方式：在 inventory 中标注 "[C-ARCHIVED]" 前缀，不创建书卡。

### Phase 8 — 综合产出
*依赖：Phase 1-7 全部完成*

1. Bridge Concept 总目录（wiki/raw/articles/concepts/index.md）
2. 与适兕思想体系的交叉索引
3. 知识图谱总览
4. 每日推荐 cron 更新（将新的 bridge concept 加入推荐序列）
5. 给适兕一份最终报告

---

## 5. 执行模式

**窄廊的工作方式：**
- 不在当前对话中逐篇执行（context 太大，效率低）
- 使用 Hermes Kanban 系统：每篇卡片是一个独立 worker
- 当前对话只做"策划 + 启动 Phase 1"
- 后续 Phase 可在独立 session 中启动，或由 cron 定时触发

**推荐的执行频率：**
- 每天 1-2 篇 Deep Review（不贪多，保证质量）
- 2-3 周完成全部 40 篇 A 级
- B 级评估穿插在 A 级之间

**质量门槛（每张卡片完成标准）：**
- frontmatter 完整（作者/年份/出处/ISBN/评分）
- 至少 1 个 bridge concept 命名+定义
- 至少 1 个与适兕思想体系的交叉连接
- 至少 1 条与其他文献的连接

---

## 6. 启动指令

在 Hermes 中执行：

```
hermes kanban boards switch deep-review-wiki
hermes kanban list
```

然后选择 Phase 1 的卡片开始执行。

---

## 7. Board 结构

Board slug: `deep-review-wiki`
Display name: "Deep Review Wiki 工程"
DB path: `/home/lee/.hermes/kanban/boards/deep-review-wiki/kanban.db`

8 个 Phase 任务（已创建）：
- t_67b069b6: Phase 1 — NIE 基石 (5篇)
- t_e148f222: Phase 2 — 开源经济学核心 (10篇)
- t_f6f3ceee: Phase 3 — 大分流制度演化 (8篇)
- t_038ba9ec: Phase 4 — OSPO体系 (7篇)
- t_cca9e8ad: Phase 5 — AI+制度交叉 (10篇)
- t_24ecd077: Phase 6 — B级快速评估 (约30篇)
- t_0c6f2522: Phase 7 — C级标记归档 (约130件)
- t_a5a1790a: Phase 8 — 综合产出

---

## 8. 与适兕书摘的对读关系

适兕录入自己的书摘和感悟后，窄廊的 deep review 应与之对读：
- 适兕读"原文"的触动（主读）
- 窄廊读"制度分析"的骨架（辅读）
- 两者在同一个概念上交汇，形成 bridge concept 的双层结构

这是**对读**，不是**拼接**。
