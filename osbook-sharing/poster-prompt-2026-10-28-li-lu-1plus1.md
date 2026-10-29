# 「开源之书·共读」金句海报提示词 — 李录 1+1>4

## 海报信息

| 字段 | 内容 |
|------|------|
| **品牌** | 「开源之书·共读」 |
| **Slogan** | We are what we read！人如其读！ |
| **金句来源** | 李录《文明、现代化、价值投资与中国（增订版）》第十一讲「现代化的本质和铁律」 |
| **字体** | 草书（行草/狂草），手写感，非印刷体 |
| **规格** | 竖版 3:4 或 2:3，适合微信公众号与朋友圈 |

---

## 一、中文版提示词（主用）

> 一张竖版学术金句海报。深普鲁士蓝 #1B3B6B 的厚质宣纸背景，纸面有细微的连史纸纤维纹理与古籍页边泛黄的暖白 #F5F0E8 晕染，边缘做旧、局部留有虫蛀般的微孔。构图取包豪斯几何：画面上三分之一处一道极细的金线横贯，金线左端是一个等粗的圆环，右端是同一圆环被拆成两段弧——一断一合，构成"1+1"的视觉双关；两段弧之间留出一道窄隙，隙中透出光。
>
> 画面中央偏上是**草书大字**，字体为行草，笔势连断分明、墨色有枯润变化，写两个并置的**"一"**与一个**"四"**，中间以草书连笔写出"＋"与"＞"，整体极简、留白极大，一眼看去像一道书法的算式。字迹右下角有一处墨点自然晕开，不做修饰。
>
> 大字下方是一行小字的中文引文，排成窄栏，字体为宋体或仿宋，字距宽松，仅占画面宽度的三分之二，右对齐；引文只留核心一句。
>
> 底部三分之一留白，左下角一行纤细的草书品牌名「开源之书·共读」，右下角一行罗马体小字 slogan：We are what we read！人如其读！。底部中央一行极小的出处：李录《文明、现代化、价值投资与中国》。所有文字均为深墨色，唯一暖色是草书大字中飞白处的暖金 #B8860B。
>
> 整体风格：暗黑学院（dark academic）调性，理性而克制，智识感强，像一张贴在旧书房墙上的讲学海报。无人物、无摄影、无插画、无 3D、无多余装饰。纯排版与几何抽象，大量留白。

---

## 二、English 版提示词（备用，给不识别中文的引擎）

> A vertical academic quote poster. Deep Prussian blue #1B3B6B handmade paper background with subtle laid-paper fiber texture, warm ivory #F5F0E8 wash at the edges, gently aged, a few tiny worm-hole speckles. Bauhaus geometric composition: a single hairline gold rule spans the upper third; at its left end a perfect circle, at its right end the same ring split into two arcs — one broken, one whole — a visual pun on "one plus one"; a narrow gap between the arcs leaks light.
>
> Center-upper: large **Chinese cursive calligraphy** (xingcao / wild cursive), confident connected strokes, ink varying from wet black to dry grey with visible flying-white. The brush writes "一", "＋", "一", "＞", "四" in a single breath, forming a calligraphic equation — extremely minimal, huge negative space, reads at a glance like a poem-shaped formula. One natural ink blot bleeding at the lower right of the last stroke; no cleanup.
>
> Below: a narrow column of small Chinese quotation text, Song-style serif, generous letter spacing, occupying two-thirds of the width, right-aligned; only the core sentence.
>
> Bottom third empty. Lower left: the brand in thin cursive — 开源之书·共读. Lower right: a small roman-type slogan — "We are what we read！人如其读！". Bottom center in very small type: 李录《文明、现代化、价值投资与中国》. All text deep ink black; the only warm accent is #B8860B gold in the flying-white gaps of the cursive strokes.
>
> Overall: dark academic, restrained, intellectual — looks like a lecture poster pinned on the wall of an old study. No people, no photography, no illustration, no 3D render, no ornamental flourishes. Pure typography and geometric abstraction. Maximum whitespace.

---

## 三、文字排版内容（给排版工具用，不是给图像引擎）

```
[上三分之一]
────────●  (◗ ◖)────────     ← 金色细线 + 圆环 / 断环

[中央，草书大字]
    一 ＋ 一 〉四

[中部小字引文，右对齐窄栏]
知识思想交换时出现的情况是 1+1〉4。
不同的思想进行交换的时候，
交换双方不仅保留了自己的思想，
获得了对方的思想，
而且在交流中还碰撞火花，
创造出全新的思想。

[左下]
开源之书·共读（草书）

[右下]
We are what we read！人如其读！

[底中，极小]
李录《文明、现代化、价值投资与中国》
```

---

## 四、注意事项（给执行图像生成时）

1. **草书是最大风险点**。多数图像引擎写汉字会糊、会错字、会造字。**草书大字务必人工复核**："一""四"可辨，但连笔的"＋""＞"极易被引擎写成乱码。若引擎不稳，退一步：**画面只留草书"一＋一〉四"，引文改用排版工具叠加**，不要让引擎一次生成全部文字。
2. **不要在提示词里要求"很多文字"**。引擎一次生成超过 20 个汉字，出错率陡升。分工：图像引擎出底与大字，排版工具叠小字。
3. **"断环"要做成暗示，不要做成插图**。它只是两个几何弧，不是链条、不是锁。
4. 品牌与 slogan 的位置固定：**品牌左下、slogan 右下**，与本系列其他海报一致。
5. 引文用「〉」还是「>」：原书第十一讲用的是 **「〉」（全角）**，排版时照原样，不要规范成半角。
