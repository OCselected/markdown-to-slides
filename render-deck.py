#!/usr/bin/env python3
"""
render-deck.py — 把日读 markdown + 配图组装成自包含 HTML 幻灯片

用法：
  python3 render-deck.py 2026-10-26
  python3 render-deck.py 2026-10-26 --out /tmp/deck.html

设计取舍：
  • 单文件输出，图片走相对路径（不 base64 塞进 HTML，否则单页几十 MB）
  • 无外部依赖、无 CDN——断网也能看，方便直接丢到 nginx 上
  • 版式遵循 template.md 的视觉规范：深普鲁士蓝 #1B3B6B + 暖白 #F5F0E8
  • 配图与文字左右分栏；配图缺失时自动退化为纯文字版，不出现破图

为什么自己写而不复用现成的：
  markdown-to-slides 仓库里只有「wiki → 带视觉隐喻的 markdown」生成器
  （wiki-to-slides.py），没有 markdown → HTML 的渲染环节。缺的就是这一段。
"""

import argparse
import html
import os
import re
import sys
from pathlib import Path

HOME = Path.home()
DAILY_DIR = HOME / "developing/markdown-to-slides/daily-reading"
DECKS_DIR = HOME / "developing/ppt_decks"


# ── 解析 ────────────────────────────────────────────────────────────

def parse_slides(content):
    """按 '## Slide N' 切分，返回 [(序号, 正文)]。

    与 daily-reading-ppt-wrapper.sh 保持同一口径：
    序号取自标题里的 N，而不是数组下标。
    """
    starts = [(m.start(), int(m.group(1))) for m in
              re.finditer(r'^## Slide\s+(\d+)', content, re.MULTILINE)]
    slides = []
    for idx, (pos, num) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(content)
        slides.append((num, content[pos:end]))
    return slides


def grab(block, key):
    """取 '* **key：** 值' 或 '**key**：值' 形式的字段。"""
    pats = [
        rf'\*\s*\*\*\s*{key}\s*[：:]\s*\*\*\s*([^\n]+)',
        rf'\*\*\s*{key}\s*[：:]\s*\*\*\s*([^\n]+)',
        rf'\*\s*\*\*\s*{key}\s*\*\*\s*[：:]\s*([^\n]+)',
    ]
    for p in pats:
        m = re.search(p, block)
        if m:
            return m.group(1).strip()
    return ""


def grab_multiline(block, key, stops=("书摘", "桥接", "追问", "显示要点", "视觉隐喻",
                                      "讲者信息", "时间/地点", "主标题", "副标题", "---")):
    """取可能跨行的字段（视觉隐喻常常很长）。

    视觉隐喻后面常紧跟 `* **讲者信息：** ...`、`* **时间/地点：** ...` 这类
    同级字段。这些行同样以 `* ` 开头，若不在 stops 里就会一并被吞进隐喻，
    导致配图说明把「讲者信息」「时间/地点」也显示出来。
    """
    m = re.search(rf'\*\*?\s*{key}\s*[：:]\s*\*\*?\s*(.*)', block, re.DOTALL)
    if not m:
        return ""
    body = m.group(1)
    # ① 遇到任何同级 bullet 字段（* **xxx：**）就截断
    cut = re.search(r'\n\s*\*\s*\*\*[^*]+\*\*\s*[：:]', body)
    if cut:
        body = body[:cut.start()]
    # ② 再按显式小节名截断
    for s in stops:
        for pat in (f"**{s}", f"\n{s}"):
            idx = body.find(pat)
            if idx != -1:
                body = body[:idx]
    return body.strip().strip("*").strip()


def grab_bullets(block, section):
    """取出某个小节下的 bullet 列表。

    边界要卡死：只收「该小节标题」到「下一个 **小节名**」之间的行。
    旧实现的停止条件过宽，遇到 **粗体** 开头的正文行时不会被当成分隔
    不会被当成分隔，导致桥接、书摘的内容被吞进「要点」。
    """
    # 小节标题形如： **显示要点（2 条）**：  或  **「开源之道」·窄廊追问**：
    m = re.search(rf'\*\*{re.escape(section)}[^*]*\*\*\s*[：:]?\s*\n', block)
    if not m:
        return []
    rest = block[m.end():]
    # 下一个以 ** 开头的小节标题即止
    stop = re.search(r'\n\*\*[^\n]+?\*\*\s*[：:]?\s*\n', rest)
    body = rest[:stop.start()] if stop else rest
    items = []
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
    return items


def md_inline(s):
    """极简 markdown 行内转换：**粗体**、*斜体*、`code`。

    只做这几种——足够帖子用，且避免引入 markdown 库依赖。
    """
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', s)
    return s


# ── 找配图 ──────────────────────────────────────────────────────────

def find_images(date, slide_nums=None):
    """找到该日期最新一次生成的 deck 目录，返回 {slide序号: 图片绝对路径}。

    取最新目录：同一天可能重跑多次（backfill），以最后一次为准。

    历史兼容：2026-10-28 之前的产物按**数组下标**命名（slide-03/05/07），
    而正确序号应是 slide-00/01/02。这里做一次映射：
    若目录里没有 slide-00.png 但有更高编号，则按文件名排序后依次对应
    slide_nums。命名 bug 已修，此后新产物直接对上，不再走这条分支。
    """
    cands = sorted(DECKS_DIR.glob(f"日读_{date}_*/images"))
    if not cands:
        return {}
    imgdir = cands[-1]

    found = {}
    for f in imgdir.glob("slide-*.png"):
        m = re.search(r'slide-(\d+)\.png$', f.name)
        if m:
            found[int(m.group(1))] = f
    if not found:
        return {}

    # 新命名：直接从 0 开始且连续 → 直接用
    if 0 in found:
        return found

    # 旧命名：按下标排序，重新映射到真实 slide 序号
    if slide_nums:
        ordered = [found[k] for k in sorted(found)]
        return {num: p for num, p in zip(slide_nums, ordered)}
    return found


# ── 渲染 ────────────────────────────────────────────────────────────

CSS = """
:root{
  --ink:#1B3B6B; --ink-soft:#3D5A80; --paper:#F5F0E8; --paper-2:#EDE6D9;
  --rule:#C9BFA8; --accent:#8B6914; --text:#2C2A26; --muted:#6B6459;
}
*{box-sizing:border-box;margin:0;padding:0}
body{
  background:var(--paper); color:var(--text);
  font-family:"Source Han Serif SC","Songti SC","Noto Serif CJK SC",Georgia,serif;
  line-height:1.75; -webkit-font-smoothing:antialiased;
}
.deck{max-width:1180px;margin:0 auto;padding:0 1.25rem 6rem}

/* 顶部信息条 */
.masthead{
  padding:2.5rem 0 1.5rem;border-bottom:1px solid var(--rule);
  margin-bottom:2rem;position:relative;
}
/* 返回索引：固定在信息条右上，滚动时也保持可达 */
.back-home{
  position:absolute;right:0;top:2.5rem;
  display:inline-flex;align-items:center;gap:.4rem;
  font-size:.8rem;color:var(--accent);text-decoration:none;
  border:1px solid var(--rule);border-radius:100px;
  padding:.32rem .85rem;letter-spacing:.04em;
  transition:background .15s,border-color .15s;
}
.back-home:hover{background:rgba(139,105,20,.07);border-color:var(--accent)}
@media(max-width:640px){
  .back-home{position:static;margin-top:.9rem;display:inline-flex}
}
.masthead .kicker{
  font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;
  color:var(--accent);margin-bottom:.6rem;
}
.masthead h1{font-size:1.35rem;color:var(--ink);font-weight:700;letter-spacing:.02em}

/* 单页 slide */
.slide{
  padding:2.5rem 0;border-bottom:1px solid var(--rule);
}
.slide:last-child{border-bottom:none}
.slide-head{
  display:flex;align-items:baseline;gap:.9rem;margin-bottom:1.4rem;
}
.slide-no{
  font-size:.72rem;letter-spacing:.18em;color:var(--accent);
  border:1px solid var(--rule);border-radius:2px;
  padding:.15rem .45rem;flex-shrink:0;
}
.slide-title{
  font-size:1.5rem;font-weight:700;color:var(--ink);
  line-height:1.4;letter-spacing:.01em;
}

/* 封面 */
.slide.cover .slide-title{font-size:2.1rem}
.cover-sub{
  font-size:1.02rem;color:var(--muted);margin:.4rem 0 1.2rem;
  padding-left:1rem;border-left:2px solid var(--accent);
}
.cover-meta{font-size:.85rem;color:var(--accent);letter-spacing:.06em}
.slide.cover figure.shot{margin:1.2rem 0 1.6rem}
.slide.cover .cover-body{margin-top:.5rem}

/* 图文分栏 */
.split{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start}
@media(max-width:820px){.split{grid-template-columns:1fr;gap:1.2rem}}

figure.shot{margin:0}
figure.shot img{
  width:100%;height:auto;display:block;border-radius:3px;
  box-shadow:0 2px 18px rgba(27,59,107,.13);
}
figure.shot figcaption{
  margin-top:.6rem;font-size:.78rem;color:var(--muted);
  line-height:1.6;font-style:italic;
}

/* 正文块 */
.lede{font-size:1.02rem;color:var(--ink-soft);margin-bottom:1.2rem}
.block{margin-bottom:1.35rem}
.block-label{
  font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);margin-bottom:.5rem;
}
.block ul{list-style:none}
.block li{
  position:relative;padding-left:1.1rem;margin-bottom:.7rem;
  font-size:.94rem;line-height:1.8;
}
.block li:before{
  content:"";position:absolute;left:0;top:.62em;
  width:6px;height:6px;background:var(--ink);border-radius:50%;opacity:.55;
}
.quote{
  border-left:2px solid var(--accent);
  padding:.7rem 0 .7rem 1.1rem;margin:.9rem 0;
  font-size:.95rem;color:var(--ink-soft);font-style:italic;
}
.quote cite{display:block;font-style:normal;font-size:.8rem;color:var(--muted);margin-top:.45rem}
.question{
  background:var(--paper-2);border-radius:4px;
  padding:1rem 1.15rem;margin-top:.9rem;
}
.question .block-label{color:var(--ink)}
.question li{font-size:.9rem}
code{
  background:rgba(27,59,107,.08);padding:.08em .32em;border-radius:2px;
  font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:.88em;
}
.plain{
  padding:1.2rem;border:1px dashed var(--rule);border-radius:4px;
  color:var(--muted);font-size:.88rem;text-align:center;
}
/* 上一期 / 下一期 */
.pager{
  display:grid;grid-template-columns:1fr 1fr;gap:1rem;
  margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--rule);
}
.pager a,.pager span{
  display:block;text-decoration:none;border:1px solid var(--rule);
  border-radius:6px;padding:.9rem 1.1rem;transition:background .15s,border-color .15s;
}
.pager a:hover{background:rgba(27,59,107,.045);border-color:var(--ink-soft)}
.pager .dir{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent);margin-bottom:.35rem}
.pager .ttl{font-size:.94rem;color:var(--ink);line-height:1.5;font-weight:600}
.pager .dd{font-size:.75rem;color:var(--muted);margin-top:.3rem;
  font-variant-numeric:tabular-nums}
.pager .next{text-align:right}
/* 没有相邻期次时占位，保持左右对称不塌陷 */
.pager .none{border-style:dashed;opacity:.5}
.pager .none .ttl{color:var(--muted);font-weight:400}

footer{
  margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--rule);
  font-size:.78rem;color:var(--muted);letter-spacing:.04em;
}
"""


def render_slide(num, block, img_path, out_dir):
    """渲染单张 slide。"""
    parts = []

    title_m = re.search(r'## Slide\s+\d+\s*[：:]?\s*([^\n]*)', block)
    raw_title = title_m.group(1).strip() if title_m else ""
    is_cover = (num == 0)

    parts.append(f'<section class="slide{" cover" if is_cover else ""}" id="s{num}">')
    parts.append('<div class="slide-head">')
    parts.append(f'<span class="slide-no">{"COVER" if is_cover else f"{num:02d}"}</span>')
    # 封面不把「封面」二字当标题（那是页码性质，不是内容）；
    # 封面的正式标题来自「主标题」字段，在下面单独渲染。
    if not is_cover and raw_title:
        parts.append(f'<h2 class="slide-title">{md_inline(raw_title)}</h2>')
    elif not is_cover:
        parts.append('<h2 class="slide-title">&nbsp;</h2>')
    parts.append('</div>')

    # 封面：主标题 / 副标题 / 讲者
    if is_cover:
        main = grab(block, "主标题")
        sub = grab(block, "副标题")
        who = grab(block, "讲者信息")
        when = grab(block, "时间/地点")
        if main:
            parts.append(f'<h2 class="slide-title" style="font-size:2.4rem;margin-bottom:.3rem">'
                         f'{md_inline(main)}</h2>')
        if sub:
            parts.append(f'<p class="cover-sub">{md_inline(sub)}</p>')
        meta = " ｜ ".join(x for x in (who, when) if x)
        if meta:
            parts.append(f'<p class="cover-meta">{md_inline(meta)}</p>')

    # 视觉隐喻（作为配图说明，不重复显示成正文）
    metaphor = grab_multiline(block, "视觉隐喻")

    # 显示要点
    bullets = grab_bullets(block, "显示要点")
    if not bullets:
        # 兜底：抓所有 '- ' 开头且不在其他小节里的行
        bullets = [l.strip()[2:].strip() for l in block.split("\n")
                   if l.strip().startswith("- ")]

    # 追问
    questions = grab_bullets(block, "「开源之道」·窄廊追问")

    # 书摘
    quote_m = re.search(r'\*\*书摘\*\*[：:]?\s*\n+((?:>[^\n]*\n?)+)', block)
    quote_html = ""
    if quote_m:
        qlines = [l.lstrip("> ").rstrip() for l in quote_m.group(1).split("\n") if l.strip().startswith(">")]
        qtext = " ".join(x for x in qlines if x and not x.startswith("——"))
        cite = next((x for x in qlines if x.startswith("——")), "")
        if qtext:
            quote_html = f'<div class="quote">{md_inline(qtext)}'
            if cite:
                quote_html += f'<cite>{md_inline(cite)}</cite>'
            quote_html += '</div>'

    # 图片
    img_html = ""
    if img_path and Path(img_path).exists():
        # 直接用相对路径：从输出目录到图片文件的真实位置，
        # 不要手工拼 parent.name——images 目录会被重复一层。
        rel = os.path.relpath(img_path, Path(out_dir))
        cap = md_inline(metaphor) if metaphor else ""
        img_html = (f'<figure class="shot"><img src="{rel}" alt="配图" loading="lazy">'
                    + (f'<figcaption>{cap}</figcaption>' if cap else "")
                    + '</figure>')
    else:
        img_html = '<div class="plain">本期无配图</div>'

    # 正文
    body = []
    if bullets:
        body.append('<div class="block"><div class="block-label">要点</div><ul>'
                    + "".join(f"<li>{md_inline(b)}</li>" for b in bullets) + "</ul></div>")
    if quote_html:
        body.append('<div class="block"><div class="block-label">书摘</div>' + quote_html + "</div>")
    if questions:
        body.append('<div class="block question"><div class="block-label">窄廊追问</div><ul>'
                    + "".join(f"<li>{md_inline(q)}</li>" for q in questions) + "</ul></div>")

    if is_cover and img_html:
        # 封面：图在上、文字在下，通栏排列。
        # 左右分栏会让封面左侧留出大片空白，看着像没排完。
        parts.append(img_html)
        parts.append('<div class="cover-body">' + "".join(body) + '</div>')
    elif img_html:
        parts.append('<div class="split">')
        parts.append('<div>' + "".join(body) + '</div>')
        parts.append('<div>' + img_html + '</div>')
        parts.append('</div>')
    else:
        parts.append("".join(body))

    parts.append('</section>')
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="日期，如 2026-10-26")
    ap.add_argument("--out", help="输出 HTML 路径")
    ap.add_argument("--prev", help="上一期（更早）日期，如 2026-10-24")
    ap.add_argument("--next", help="下一期（更新）日期，如 2026-10-28")
    ap.add_argument("--prev-title", default="", help="上一期标题")
    ap.add_argument("--next-title", default="", help="下一期标题")
    ap.add_argument("--home", default="../", help="返回索引的相对路径")
    args = ap.parse_args()

    date = args.date
    src = DAILY_DIR / date[:7] / f"{date}.md"
    if not src.exists():
        sys.exit(f"找不到源文件：{src}")

    content = src.read_text(encoding="utf-8")
    slides = parse_slides(content)
    if not slides:
        sys.exit("未解析到任何 slide")

    images = find_images(date, [num for num, _ in slides])

    out_path = Path(args.out) if args.out else Path(f"/tmp/deck-{date}.html")

    out_dir = out_path.parent
    rendered = [render_slide(num, block, images.get(num), out_dir)
                for num, block in slides]

    # ── 导航：返回索引 + 上一期/下一期 ──
    def esc(s):
        return html.escape(s or "", quote=True)

    def pager_card(kind, day, title):
        """kind: 'prev' | 'next'。没有相邻期次时给占位，保持左右对称。"""
        label = "← 上一期" if kind == "prev" else "下一期 →"
        cls = "prev" if kind == "prev" else "next"
        if day:
            return (f'    <a class="{cls}" href="../{day}/deck.html">'
                    f'<div class="dir">{label}</div>'
                    f'<div class="ttl">{esc(title) or day}</div>'
                    f'<div class="dd">{day}</div>'
                    f'</a>')
        return (f'    <span class="{cls} none">'
                f'<div class="dir">{label}</div>'
                f'<div class="ttl">已是{"最早" if kind == "prev" else "最新"}一期</div>'
                f'</span>')

    pager = "\n".join([
        '  <nav class="pager">',
        pager_card("prev", args.prev, args.prev_title),
        pager_card("next", args.next, args.next_title),
        '  </nav>',
    ])

    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>「开源之道」日读 · {date}</title>
<style>{CSS}</style>
</head>
<body>
<div class="deck">
  <header class="masthead">
    <div class="kicker">OSCAR · 开源之书 · 共读 ／ 每日阅读</div>
    <h1>{date}</h1>
    <a class="back-home" href="{esc(args.home)}">← 返回列表</a>
  </header>
{chr(10).join(rendered)}
{pager}
  <footer>「开源之道」·适兕 ／ 配图由 SenseNova u1.5-lite 生成 · {len(slides)} 张</footer>
</div>
</body>
</html>
"""
    out_path.write_text(doc, encoding="utf-8")
    print(f"✅ 已生成 {out_path}  ({len(slides)} 张 slide, {len(images)} 张配图)")
    print(f"   输出目录: {out_dir}")


if __name__ == "__main__":
    main()
