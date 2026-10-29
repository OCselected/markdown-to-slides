# 「开源之书·共读」Quote 海报提示词 v2 — 李录 1+1>4（三要素齐备版）

## 版本说明

v1（`poster-prompt-2026-10-28-li-lu-1plus1.md`）只把作者与书名压成底部一行小字，**没有做到 quote 海报的基本要求**。v2 依检索到的 quote card 通行规范重做。

## 检索所得的五条硬规范（v2 的设计依据）

来源：Gradiently《Quote cards: a layout for podcast, book and speaker quotes》、bestquotes.biz《Designing Viral Quote Images》、thebetteredit《How to verify and cite quotations》、arrowupz《Epigraph Formatting》。

| # | 规范 | 出处要点 | v2 如何落实 |
|---|------|---------|------------|
| 1 | **署名与出处不是可选项** | "Name and source are not optional. A quote without them looks invented, and it gives the person no reason to share it." | 原文、作者、书名三者各自成行，独立成块，不压在底栏 |
| 2 | **署名独立成行，不用破折号** | "Set the name on its own line beneath the quote rather than putting a dash in front of it." | 弃用 `————`，改为换行＋字重/颜色区分 |
| 3 | **三层信息：引文 → 人 → 出处** | book quote card 的范本是"书名与章节作为出处"，放在引文下方独立一行 | 引文最大 → 作者次之 → 书名与章节更小 |
| 4 | **字号跟引文长度走；宁可剪短，不要缩小** | "cut before you shrink: a smaller quote is almost always a better quote"；每行 20–35 字符，3–6 行 | 引文只留核心三句，行宽控制在 20–28 字 |
| 5 | **品牌不得与引文争夺视觉** | "A large logo competing with the quote" 属应避免项 | 品牌与 slogan 缩小、压边角，做「系列识别」而非主张 |

**来源可信度分级（决定要不要印章节）**：Tier 1 是原始出处。本书引文已核到原书第十一讲「现代化的本质和铁律」第 37 页，**属 Tier 1，故章节应该在海报上出现**——这是 v1 也漏掉的。

---

## 海报信息

| 字段 | 内容 |
|------|------|
| **品牌** | 「开源之书·共读」 |
| **Slogan** | We are what we read！人如其读！ |
| **原文** | 知识思想交换时出现的情况是 1+1〉4。不同的思想进行交换的时候，交换双方不仅保留了自己的思想，获得了对方的思想，而且在交流中还碰撞火花，创造出全新的思想。 |
| **作者** | 李录 |
| **书籍** | 《文明、现代化、价值投资与中国》（增订版） |
| **章节** | 第十一讲「现代化的本质和铁律」 |
| **字体** | 草书（行草），仅用于引文首句；不用草书排作者与书名 |
| **版式** | 竖版 3:4（1080×1350），三层信息 + 顶部几何 |

---

## 一、版式结构（先定骨架，再交给引擎）

```
┌──────────────────────────────┐
│                              │
│   ────────●◗ ◖──────         │  ← 金色细线，圆环在左、断环在右（1+1 的几何双关）
│                              │
│                              │
│      一 ＋ 一 〉四            │  ← 草书大字（唯一草书区块）
│                              │
│                              │
│   知识思想交换时出现的情况是   │  ← 引文，宋体，右对齐窄栏
│   1+1〉4。不同的思想进行交换   │     每行 20–28 字，共 3–4 行
│   的时候，交换双方不仅保留了   │
│   自己的思想，获得了对方的思   │
│   想，而且在交流中还碰撞火花， │
│   创造出全新的思想。           │
│                              │
│        李 录                  │  ← 作者，独立一行，比引文粗、字号次之
│                              │
│   第十一讲「现代化的本质和铁律」│  ← 章节，比作者小
│   《文明、现代化、价值投资与   │  ← 书名，比章节略大、加书名号
│      中国》（增订版）          │
│                              │
│                              │
│ 开源之书·共读          We are │  ← 品牌草书左下 / slogan 罗马体右下
│                        what we│     均为小字，不争视觉
│                        read！ │
│                       人如其读！│
└──────────────────────────────┘
```

**层级顺序（从大到小）**：草书大字 > 引文 > 作者 > 书名 > 章节 > 品牌 / slogan。

**替代版式（引文太长时）**：把草书大字缩小为画面左侧竖排的一方印章式落款，右侧整栏放引文与三行署名。宁可换版式，不要缩字号。

---

## 二、中文提示词（主用，给中文生成引擎）

> 一张竖版金句海报，比例 3:4。深普鲁士蓝 #1B3B6B 厚质宣纸背景，纸面有连史纸纤维纹理，边缘泛暖白 #F5F0E8、做旧、留几处虫蛀般的微孔。
>
> 画面上三分之一处一道极细的金线横贯，金线左端是一个等粗的圆环，右端是同一圆环被拆成两段弧，一断一合，构成"一加一"的几何双关，两段弧之间留一道窄隙透光。这是全画唯一的装饰。
>
> 画面中上部是**草书大字**，行草，笔势连断分明，墨色有枯润、飞白处透出暖金 #B8860B，写"一 ＋ 一 〉四"，极简、留白极大，像一道书法的算式。字迹右下留一处自然晕开的墨点。
>
> 大字下方是一段中文引文，**宋体，右对齐，窄栏排版，每行约二十四字，共四行**，字号明显小于草书、大于后文署名，行距宽松。引文文字固定为："知识思想交换时出现的情况是 1+1〉4。不同的思想进行交换的时候，交换双方不仅保留了自己的思想，获得了对方的思想，而且在交流中还碰撞火花，创造出全新的思想。"
>
> 引文下方留一行空白，然后**单独一行写作者「李录」**，宋体加粗，字号小于引文；其下再一行写章节「第十一讲「现代化的本质和铁律」」，再下一行写书名「《文明、现代化、价值投资与中国》（增订版）」，字号依次略减。**此处不用破折号，不排成一句话。**
>
> 底部留白，左下角一行纤细草书品牌名「开源之书·共读」，右下角罗马体小字分三行：We are what we read！／人如其读！。均为小字，不与引文争视觉。
>
> 整体暗黑学院调性，理性克制，像一张贴在旧书房墙上的引文卡。无人物、无摄影、无插画、无 3D、无花纹边框。纯排版与几何抽象，大量留白。

---

## 三、English 提示词（备用）

> A vertical quote poster, 3:4. Deep Prussian blue #1B3B6B handmade paper background, laid-paper fiber texture, warm ivory #F5F0E8 vignette at the edges, gently aged with a few worm-hole speckles.
>
> In the upper third, one hairline gold rule spans the width; at its left end a perfect circle, at its right end the same ring split into two arcs — one broken, one whole — a visual pun on "one plus one"; a narrow gap between the arcs lets light through. This is the only ornament.
>
> Center-upper: large **Chinese cursive calligraphy** (xingcao), connected strokes with wet-to-dry ink and flying-white gaps showing warm gold #B8860B, writing "一 ＋ 一 〉四" in one breath — extremely minimal, huge negative space, reading like a poem-shaped formula. A natural ink blot bleeds at the lower right of the final stroke.
>
> Below it: the Chinese quotation in **Song-style serif, right-aligned, narrow column, about 24 characters per line, four lines**, smaller than the calligraphy but larger than the attribution, generous leading. Quote text is fixed and must not be altered.
>
> After one blank line, **the author name "李录" on its own line**, bold serif, smaller than the quotation; beneath it a line with the chapter "第十一讲「现代化的本质和铁律」"; beneath that the book title "《文明、现代化、价值投资与中国》（增订版）", each step slightly smaller. **No em dash, not run into one sentence.**
>
> Bottom: empty. Lower left, the brand in thin cursive "开源之书·共读". Lower right, roman-type slogan in two small lines: "We are what we read！" and "人如其读！". Both small; neither competes with the quote.
>
> Overall dark academic, restrained, intellectual — a quotation card pinned on the wall of an old study. No people, no photography, no illustration, no 3D render, no ornamental frame. Pure typography and geometric abstraction. Maximum whitespace.

---

## 四、给排版工具的文字层（推荐：图像引擎只出底与草书，其余用排版叠加）

```
[TOP RULE]
────────● ( ◗ ◖ )────────

[CURSIVE, 唯一草书]
一 ＋ 一 〉四

[QUOTE — 宋体, 右对齐, 24字/行]
知识思想交换时出现的情况是 1+1〉4。
不同的思想进行交换的时候，
交换双方不仅保留了自己的思想，
获得了对方的思想，而且在交流中
还碰撞火花，创造出全新的思想。

[AUTHOR — 独立一行, 加粗, 居中或右对齐]
李 录

[SOURCE — 两行, 字号递减]
第十一讲「现代化的本质和铁律」
《文明、现代化、价值投资与中国》（增订版）

[FOOTER]
开源之书·共读（草书，左下）
We are what we read！人如其读！（罗马体，右下）
```

---

## 五、执行注意（v1 遗留问题的修正）

1. **三要素各自成块**：原文 → 作者 → 书名／章节，中间必须有留白分隔，**不许合并成一行、不许用破折号连写**。
2. **草书只用在"一 ＋ 一 〉四"**。作者、书名、章节一律宋体——草书排版元数据会让海报看起来像装饰品而不是引文卡，也会让引擎写错字。
3. **引文宁可剪短不要缩小**。若引擎版面拥挤，先从引文末尾删，保留"1+1〉4"那一句为核心；**章节与书名不能删**——那是可信度的凭据。
4. **`〉` 是全角**，原书如此；排版时不要规范成 `>`。
5. **品牌与 slogan 不得放大**。系列识别靠位置与字体一致，不靠尺寸。
6. **引擎分次生成**：汉字超过 20 个错误率陡升。建议底图（纸+金线+圆环）与草书一次出，引文与三行署名用排版工具（Figma / Canva / HTML）叠加。
7. 全系列共用一套模板：**一次定版，长期复用**，后续只换草书大字与三行署名。
