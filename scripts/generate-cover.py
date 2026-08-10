#!/usr/bin/env python3
"""
generate-cover.py — 为 daily-reading 当天文件生成一句话主题概括。

工作流：
1. 读取 /home/lee/developing/markdown-to-slides/daily-reading/YYYY-MM/YYYY-MM-DD.md
2. 提取所有 ## Slide N: 标题 + 每张 Slide 中适兕评论首句
3. 调用 SenseNova 大模型合成一句话主题概括（主标题 + 副标题）
4. Patch 写入 Cover 段落

设计原则：
- 主标题：一句话概括当天所有阅读/思考的共同张力（不出现书名列表）
- 副标题：更抽象的元判断，指向制度分析或思维方法的层面
- 不修改其他 Slide
- 幂等：如果 Cover 已有内容（非占位符），跳过

Usage:
    python3 generate-cover.py [--date 2026-08-10]
"""

import re
import os
import sys
import json
import argparse
import urllib.request
from datetime import datetime

REPO = "/home/lee/developing/markdown-to-slides"
DAILY = os.path.join(REPO, "daily-reading")

# SenseNova API
BASE_URL = "https://token.sensenova.cn/v1"
API_KEY = None  # 从 .env 读取

def load_api_key():
    env_path = os.path.join(os.path.expanduser("~"), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("SENSENOVA_API_KEY="):
                    return line.strip().split("=", 1)[1].strip('"').strip("'")
    # Fallback: try hermes config
    cfg_path = os.path.join(os.path.expanduser("~"), ".hermes", "config.yaml")
    if os.path.exists(cfg_path):
        with open(cfg_path) as f:
            for line in f:
                m = re.match(r"^  api_key:\s*(\S+)", line)
                if m:
                    return m.group(1)
    print("ERROR: cannot find SENSENOVA_API_KEY in ~/.env or ~/.hermes/config.yaml", file=sys.stderr)
    sys.exit(1)

def call_llm(messages):
    api_key = load_api_key()
    payload = json.dumps({
        "model": "sensenova-6.7-flash-lite",
        "messages": messages,
        "max_tokens": 5000,
        "temperature": 0.7,
        "response_format": {"type": "json_object"}
    }).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    msg = data["choices"][0]["message"]
    content = msg.get("content", "") or ""
    reasoning = msg.get("reasoning", "") or ""
    return content, reasoning

def read_file(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8")

def extract_slides(text):
    """Extract all Slide headers and each slide's 适兕评论 first sentence."""
    slides = re.findall(r"^## Slide \d+[:：]\s*(.+)$", text, re.MULTILINE)
    # Split text by slide boundaries
    boundaries = [m.start() for m in re.finditer(r"^## Slide \d+[:：]", text, re.MULTILINE)]
    boundaries.append(len(text))
    results = []
    for i, header in enumerate(slides):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(text)
        block = text[start:end]
        # Extract 适兕评论
        suiti = re.search(r"「开源之道」·适兕[评论]{0,2}[：:](.+?)(?=\n\*\s*\*\*|\Z|\n###|\n\* \*\*|Bridge|窄廊|Narrow)", block, re.DOTALL)
        comment_text = suiti.group(1).strip()[:200] if suiti else ""
        # Also extract bridge concept
        bridge = re.search(r"\*\*Bridge\s*[—–-]\s*\*\*\s*(.+?)(?=\*\*|$|\n)", block)
        bridge_text = bridge.group(1).strip()[:100] if bridge else ""
        results.append({
            "header": header.strip(),
            "suiti": comment_text,
            "bridge": bridge_text
        })
    return results

def build_prompt(slides):
    # Filter out Cover slide (Slide 1) — it has no real content
    content_slides = [s for s in slides if s["header"] != "Cover"]
    # Build compact prompt — critical: keep total prompt < 400 chars to avoid LLM truncation
    parts = []
    for i, s in enumerate(content_slides):
        header = s["header"]
        # Aggressively truncate 适兕 comment — LLM needs the essence, not full text
        suiti = s["suiti"].replace("\n", " ").replace("**", "").strip()[:120] if s["suiti"] else ""
        bridge = s["bridge"] if s["bridge"] else ""
        parts.append(f"[Slide {i+1}] {header}")
        if suiti:
            parts.append(f"    适兕: {suiti}")
        if bridge:
            parts.append(f"    桥接: {bridge}")

    return f"""你是「开源之道」阅读思考者。阅读以下笔记，输出一句话主题概括作为当日 Slide Deck 的 Cover 标题。

## 材料
{chr(10).join(parts)}

## 输出（JSON）
{{"title":"一句话主题概括(≤30字)","subtitle":"副标题(≤50字)"}}

## 风格：看不见的能量转换，才是这个世界运转的关键环节之一。制度经济学视角，冷静智识感。"""

def parse_json(response):
    # Find ALL JSON candidates in combined content+reasoning
    # Return the LAST valid one (often the final decision)
    candidates = list(re.finditer(r'\{[^{}]*"title"[^{}]*"subtitle"[^{}]*\}', response, re.DOTALL))
    best = None
    for m in candidates:
        try:
            obj = json.loads(m.group())
            if obj.get("title") and obj["title"] not in ("...", ""):
                best = obj
        except json.JSONDecodeError:
            continue
    if best:
        return best
    # Fallback: try first-line
    first_line = response.strip().split("\n")[0].strip()
    try:
        obj = json.loads(first_line)
        if "title" in obj and obj["title"] not in ("...", ""):
            return obj
    except json.JSONDecodeError:
        pass
    return None

def patch_cover(path, title, subtitle):
    text = read_file(path)
    cover_match = re.search(r"(## Slide 1[:：]\s*Cover[\s\S]*?)(?=\n## Slide \d|\Z)", text)
    if not cover_match:
        print("ERROR: Cover block not found", file=sys.stderr)
        return False
    cover_block = cover_match.group(1)
    if "[待生成]" not in cover_block:
        print("Cover already has content, skipping", file=sys.stderr)
        return False
    # Replace line-by-line: find lines containing [待生成] and patch them
    lines = cover_block.split("\n")
    new_lines = []
    title_done = False
    subtitle_done = False
    for line in lines:
        if "[待生成]" in line:
            stripped = line.strip()
            # Determine if this is title or subtitle line
            is_title = ("主标题" in stripped or "Title" in stripped) and not title_done
            is_subtitle = ("副标题" in stripped or "Subtitle" in stripped) and not subtitle_done
            if is_title:
                new_lines.append(line.replace("[待生成]", title))
                title_done = True
            elif is_subtitle:
                new_lines.append(line.replace("[待生成]", subtitle))
                subtitle_done = True
            else:
                new_lines.append(line.replace("[待生成]", title if not title_done else subtitle))
        else:
            new_lines.append(line)
    new_cover = "\n".join(new_lines)
    # If nothing changed, append
    if new_cover == cover_block:
        new_cover = cover_block.rstrip() + f'\n\n* **主标题：** {title}\n* **副标题：** {subtitle}\n'
    text = text[:cover_match.start()] + new_cover + text[cover_match.end():]
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="Target date YYYY-MM-DD")
    args = parser.parse_args()

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")
    year_month = date_str[:7]
    filepath = os.path.join(DAILY, year_month, f"{date_str}.md")

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(0)

    text = read_file(filepath)
    slides = extract_slides(text)

    if not slides:
        print("No slides found")
        sys.exit(0)

    print(f"Found {len(slides)} slides in {filepath}")
    for s in slides[:3]:
        print(f"  - {s['header'][:80]}")

    # Check if Cover already filled
    cover_match = re.search(r"(## Slide 1[:：]\s*Cover[\s\S]*?)(?=\n## Slide \d|\Z)", text)
    if cover_match and "[待生成]" not in cover_match.group(1):
        print("Cover already filled, skipping")
        sys.exit(0)

    prompt = build_prompt(slides)
    print(f"\nCalling LLM...")
    content, reasoning = call_llm([{"role": "user", "content": prompt}])
    combined = content + reasoning
    result = parse_json(combined)

    if not result or "title" not in result:
        print(f"Failed to parse JSON from response")
        print(f"Content: {content[:200]}")
        print(f"Reasoning tail: {reasoning[-200:]}")
        sys.exit(1)

    title = result["title"]
    subtitle = result.get("subtitle", "")
    print(f"\nGenerated Cover:")
    print(f"  主标题: {title}")
    print(f"  副标题: {subtitle}")

    if patch_cover(filepath, title, subtitle):
        print(f"✓ Patched {filepath}")
    else:
        print("✗ Cover was not patched")

if __name__ == "__main__":
    main()