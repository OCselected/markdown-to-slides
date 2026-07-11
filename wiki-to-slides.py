#!/usr/bin/env python3
"""
将 llm-wiki 的书籍推荐条目转换为 markdown-to-slides 格式。
用法：
  python3 wiki-to-slides.py                          # 转为全部待推荐条目
  python3 wiki-to-slides.py --slug trust-and-power-luhmann  # 指定单本书
  
输出：写入 markdown-to-slides/slides/<slug>.md
"""

import os, sys, json, re
from pathlib import Path

WIKI = Path("/Users/lee/Library/CloudStorage/GoogleDrive-opensourceway.community@gmail.com/My Drive/open-source-way-wiki")
SLIDES_DIR = Path("/Users/lee/developing/markdown-to-slides/slides")
SLIDES_DIR.mkdir(parents=True, exist_ok=True)

# 系统提示模板（与 template.md 保持一致）
SYSTEM_PROMPT = """# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
用于和读书思考爱好者的交流（Deck）。

## 使用场景
「开源之道」「OSCAR·开源之书·共读」分享

## 听众画像
思考者，阅读者，善于交流者。对制度经济学、开源文化有基本认知框架。

## 讲者视角
思维活跃者、独立开源研究者、协作机制设计师（社会黑客）。

## 核心诉求
展示人类的思维活动，渴望获得交流。

## 核心基调
dark academic tone, Intellectual Visual System, art taste.

## 视觉风格关键词
- 包豪斯几何构成（Bauhaus geometric composition）
- Red Hat 红色 #CC0000 作为强调色
- 暖白底色 #F5F2ED，复古学术质感
- 极简主义排版，大字号标题
- 深色学术风格（dark academic）
"""

def parse_frontmatter(content):
    """Extract YAML frontmatter fields."""
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)\s*\n', content, re.DOTALL)
    if not m:
        return {}, content
    raw_fm = m.group(1)
    body = content[m.end():]
    fm = {}
    for line in raw_fm.split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, body

def extract_concepts(body, max_slides=4):
    """Parse wiki entry body into slide content."""
    slides = []
    
    # Title from first heading
    title_m = re.search(r'^# (.+)$', body, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""
    
    # Extract structured sections
    sections = re.split(r'^## ', body, flags=re.MULTILINE)
    
    current_section = ""
    current_lines = []
    
    for sec in sections:
        if not sec.strip():
            continue
        lines = sec.strip().split('\n')
        heading = lines[0].strip().rstrip(':')  # section name
        content = '\n'.join(lines[1:]).strip()
        
        # Key concepts
        if '关键概念' in heading or '核心概念' in heading:
            concepts = []
            for line in lines[1:]:
                line_s = line.strip()
                # Match: - **concept** — explanation
                m = re.search(r'-\s*\*{1,2}(.+?)\*{1,2}\s*[—\-–:：]?\s*(.+)', line_s)
                if m:
                    concepts.append(f"  * {m.group(1).strip()}: {m.group(2).strip()}")
            if concepts:
                slides.append({
                    'heading': '关键概念',
                    'metaphor': '概念之间的关系网络图，每个节点是一本书或一个思想',
                    'points': concepts
                })
        
        # 与开源的关系 / 对开源的启示
        if '对开源' in heading or '开源的启示' in heading:
            points = [f"  * {l.strip().lstrip('- ')}" for l in lines[1:] if l.strip().startswith('-')]
            if points:
                slides.append({
                    'heading': '与开源的关系',
                    'metaphor': '代码节点与制度结构交织的网络',
                    'points': points[:5]
                })
        
        # 在信任思想谱系中的位置 / 延伸思考
        if '延伸思考' in heading or '对开源的启示' in heading:
            points = []
            for line in lines[1:]:
                ls = line.strip()
                if ls and not ls.startswith('##'):
                    # Remove numbering
                    ls_clean = re.sub(r'^\d+\.\s*', '', ls)
                    if len(ls_clean) > 10:
                        points.append(f"  * {ls_clean[:120]}")
            if points:
                slides.append({
                    'heading': '延伸思考',
                    'metaphor': '打开的书本中延伸出的问号与分支',
                    'points': points[:4]
                })

    # Fallback: if no structured sections found, extract from body
    if len(slides) < 2:
        # Get bullet points from rest of body
        bullets = []
        for line in body.split('\n'):
            ls = line.strip()
            if ls.startswith('- ') and len(ls) > 15:
                bullets.append(f"  * {ls[2:]}")
        if bullets:
            slides.append({
                'heading': '阅读笔记',
                'metaphor': '散落书页上的手写批注',
                'points': bullets[:5]
            })

    return title, slides


def wiki_entry_to_slides(filepath):
    """Convert one wiki entry to a slide deck markdown."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    fm, body = parse_frontmatter(content)
    title, slides = extract_concepts(body)
    
    if not title:
        title = fm.get('title', filepath.stem)
    
    slug = filepath.stem
    author = fm.get('author', fm.get('tags', ''))
    
    lines = []
    lines.append(SYSTEM_PROMPT)
    lines.append("---")
    lines.append("")
    lines.append(f"# 幻灯片大纲: {title}")
    lines.append("")
    
    # Slide 1: Cover
    lines.append("## Slide 1: 封面 (Cover)")
    lines.append(f"* **主标题：** {title}")
    lines.append("* **副标题：** 「开源之书·共读」每日推荐")
    lines.append("* **讲者信息：** 「开源之道」·适兕")
    lines.append("* **时间/地点：**")
    lines.append("")
    
    # Slide 2: Why this book
    lines.append("## Slide 2: 为什么读这本书")
    lines.append("* 视觉隐喻：")
    lines.append("  * 打开的书本，书页之间散发着微光")
    lines.append("* 显示要点：")
    
    # Extract first paragraph of body as intro
    paras = body.split('\n\n')
    intro = ""
    for p in paras:
        p_clean = p.strip()
        if len(p_clean) > 30 and not p_clean.startswith('##') and not p_clean.startswith('-') and not p_clean.startswith('|'):
            intro = p_clean[:200]
            break
    if intro:
        lines.append(f"  * {intro}")
    lines.append("")
    
    # Remaining slides
    for s in slides[:5]:
        lines.append(f"## Slide: {s['heading']}")
        lines.append("* 视觉隐喻：")
        lines.append(f"  * {s['metaphor']}")
        lines.append("* 显示要点：")
        for p in s['points'][:5]:
            lines.append(f"  {p}")
        lines.append("")
    
    # Final slide
    lines.append("## Slide: 讨论问题")
    lines.append("* 视觉隐喻：")
    lines.append("  * 圆桌旁围坐的人影")
    lines.append("* 显示要点：")
    lines.append("  * 这本书的核心论点在今天的语境下是否仍然成立？")
    lines.append("  * 它的分析框架能否迁移到其他领域？")
    lines.append("  * 如果你要反驳这本书，你的切入点是什么？")
    lines.append("")
    
    return '\n'.join(lines)


def convert_all():
    """Convert all wiki recommendation entries to slide decks."""
    rec_dir = WIKI / "raw/articles/osbook-book-recommendation"
    count = 0
    for fp in sorted(rec_dir.glob("*.md")):
        try:
            output = wiki_entry_to_slides(fp)
            out_path = SLIDES_DIR / f"{fp.stem}.md"
            out_path.write_text(output, encoding='utf-8')
            count += 1
            print(f"  ✅ {fp.stem}")
        except Exception as e:
            print(f"  ❌ {fp.stem}: {e}")
    return count


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--slug":
        slug = sys.argv[2]
        fp = WIKI / "raw/articles/osbook-book-recommendation" / f"{slug}.md"
        if fp.exists():
            output = wiki_entry_to_slides(fp)
            out_path = SLIDES_DIR / f"{slug}.md"
            out_path.write_text(output, encoding='utf-8')
            print(f"✅ Generated: {out_path}")
        else:
            print(f"❌ Not found: {fp}")
    else:
        print("=== Converting all wiki entries to slides ===")
        count = convert_all()
        print(f"\n✅ Done. {count} slide decks generated in {SLIDES_DIR}")