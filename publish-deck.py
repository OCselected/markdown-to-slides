#!/usr/bin/env python3
"""
publish-deck.py — 把日读 deck 发布到 8.211.12.147 的 nginx

用法：
  python3 publish-deck.py 2026-10-26          # 发布单期
  python3 publish-deck.py --index             # 只重建索引页

设计取舍：
  • 用 rsync 而不是挂载（rclone/sshfs）。发布是单向动作，挂载会把远端
    伪装成本地磁盘，换来「可能 hang、删除取消上传、跨网络 stat」的代价。
  • 每期一个目录 /YYYY-MM-DD/，图片就近放在其 images/ 下——
    远端不依赖本地 ppt_decks 的目录结构，自成一体。
  • 生成 index.html 列表页，按日期倒序列出所有已发布 deck。
  • 幂等：重复发布同一期直接覆盖，不累积。

远端路径：/www/wwwroot/slides
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HOME = Path.home()
DAILY_DIR = HOME / "developing/markdown-to-slides/daily-reading"
DECKS_DIR = HOME / "developing/ppt_decks"
RENDER = HOME / "developing/markdown-to-slides/render-deck.py"

REMOTE_HOST = "8.211.12.147"
REMOTE_ROOT = "/www/wwwroot/slides"
PUBLIC_BASE = "http://8.211.12.147"


def sh(cmd, **kw):
    """跑命令；失败直接抛，避免静默把错误当成功。"""
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"命令失败: {' '.join(map(str, cmd))}\n{r.stderr[:500]}")
    return r.stdout


def find_images(date, slide_nums):
    """与 render-deck.py 同一口径：取最新 deck，兼容旧的下标命名。"""
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
    if 0 in found:
        return found
    ordered = [found[k] for k in sorted(found)]
    return {num: p for num, p in zip(slide_nums, ordered)}


def build_one(date, workdir):
    """在临时目录里构建一期的发布产物：deck.html + images/。"""
    src = DAILY_DIR / date[:7] / f"{date}.md"
    if not src.exists():
        raise SystemExit(f"找不到源文件：{src}")

    stage = Path(workdir) / date
    (stage / "images").mkdir(parents=True, exist_ok=True)

    # ① 先渲染成 HTML（图片路径此时指向本地，后面统一改写）
    tmp_html = stage / "deck.html"
    sh([sys.executable, str(RENDER), date, "--out", str(tmp_html)])

    # ② 把用到的图片拷到 images/，并把路径改写为相对路径
    texts = list(re.finditer(r'^## Slide\s+(\d+)', src.read_text(encoding="utf-8"), re.M))
    nums = [int(m.group(1)) for m in texts]
    imgs = find_images(date, nums)

    doc = tmp_html.read_text(encoding="utf-8")
    copied = 0
    for num, p in imgs.items():
        dst = stage / "images" / p.name
        shutil.copy2(p, dst)
        # 源文件常是 600（SenseNova 生成时 umask 所致），nginx 以 www 用户
        # 运行会 Permission denied → 403。发布产物一律放成 644。
        os.chmod(dst, 0o644)
        copied += 1
        # 任何指向本地 ppt_decks 的路径都改写为 images/<文件名>
        doc = re.sub(r'src="[^"]*' + re.escape(p.name) + r'"',
                     f'src="images/{p.name}"', doc)
    tmp_html.write_text(doc, encoding="utf-8")
    os.chmod(tmp_html, 0o644)

    leftover = re.findall(r'src="(\.\./[^"]+)"', doc)
    if leftover:
        raise RuntimeError(f"仍有未改写的本地路径: {leftover[:3]}")

    return stage, copied


def build_index(workdir):
    """扫描远端已有目录，生成索引页。"""
    listing = sh(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10",
                  REMOTE_HOST, f"ls -1 {REMOTE_ROOT} 2>/dev/null || true"])
    dates = sorted([d.strip() for d in listing.splitlines()
                    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', d.strip())], reverse=True)

    items = []
    for d in dates:
        # 取该期标题（从本地源文件读，远端没有 markdown）
        title = d
        src = DAILY_DIR / d[:7] / f"{d}.md"
        if src.exists():
            m = re.search(r'## Slide 0[^\n]*\n\* \*\*主标题：\*\*\s*([^\n]+)',
                          src.read_text(encoding="utf-8"))
            if m:
                title = m.group(1).strip()
        items.append(f'''    <li>
      <a href="{d}/deck.html">
        <span class="date">{d}</span>
        <span class="title">{html.escape(title)}</span>
      </a>
    </li>''')

    idx = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>「开源之道」日读 · 幻灯片</title>
<style>
:root{{--ink:#1B3B6B;--paper:#F5F0E8;--rule:#C9BFA8;--accent:#8B6914;--text:#2C2A26}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--paper);color:var(--text);line-height:1.7;
  font-family:"Source Han Serif SC","Songti SC",Georgia,serif}}
.wrap{{max-width:760px;margin:0 auto;padding:3.5rem 1.5rem 6rem}}
.kicker{{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;
  color:var(--accent);margin-bottom:.7rem}}
h1{{font-size:1.7rem;color:var(--ink);margin-bottom:.5rem;letter-spacing:.02em}}
.sub{{color:#6B6459;font-size:.9rem;margin-bottom:2.5rem;
  padding-left:1rem;border-left:2px solid var(--accent)}}
ul{{list-style:none}}
li{{border-bottom:1px solid var(--rule)}}
li a{{display:flex;gap:1.2rem;align-items:baseline;
  padding:1.05rem .4rem;text-decoration:none;color:inherit;
  transition:background .15s}}
li a:hover{{background:rgba(27,59,107,.05)}}
.date{{font-size:.82rem;color:#8A6D1E;letter-spacing:.06em;
  flex-shrink:0;width:7.2em;
  font-variant-numeric:tabular-nums;font-feature-settings:"tnum" 1}}
.title{{font-size:1rem;color:var(--ink)}}
.empty{{color:#6B6459;padding:2rem 0}}
.arch-link{{margin-top:2.4rem;font-size:.82rem}}
.arch-link a{{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(139,105,20,.4);
  padding-bottom:1px}}
.arch-link a:hover{{color:var(--ink);border-bottom-color:var(--ink)}}
footer{{margin-top:1.6rem;padding-top:1rem;border-top:1px solid var(--rule);
  font-size:.78rem;color:#6B6459;text-align:right}}
</style>
</head>
<body>
<div class="wrap">
  <div class="kicker">OSCAR · 开源之书 · 共读</div>
  <h1>每日阅读 · 幻灯片</h1>
  <p class="sub">「开源之道」·适兕 ／ 配图由 SenseNova u1.5-lite 生成</p>
  <ul>
{chr(10).join(items) if items else '    <li class="empty">还没有已发布的幻灯片</li>'}
  </ul>
  <p class="arch-link"><a href="architecture.html">查看发布链路架构图 →</a></p>
  <footer>共 {len(dates)} 期</footer>
</div>
</body>
</html>
'''
    p = Path(workdir) / "index.html"
    p.write_text(idx, encoding="utf-8")
    return p, dates


def push(stage, date):
    """rsync 到远端。--delete 只针对该期目录内部，不碰其他期。

    --chmod=D755,F644：rsync -a 默认保留源权限位，而 SenseNova 产出的
    PNG 常是 600，原样推过去 nginx（www 用户）读不到 → 403。
    在传输时强制目标权限，比事后 ssh chmod 更可靠。
    """
    sh(["rsync", "-az", "--delete", "--chmod=D755,F644",
        "-e", "ssh -o BatchMode=yes -o ConnectTimeout=10",
        f"{stage}/", f"{REMOTE_HOST}:{REMOTE_ROOT}/{date}/"])
    # 当期图片若已被清理，--delete 会同步删掉远端旧图，保持两边一致


def push_index(idx_path):
    sh(["rsync", "-az", "--chmod=F644",
        "-e", "ssh -o BatchMode=yes -o ConnectTimeout=10",
        str(idx_path), f"{REMOTE_HOST}:{REMOTE_ROOT}/index.html"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", nargs="?", help="要发布的日期，如 2026-10-26")
    ap.add_argument("--index", action="store_true", help="只重建索引页")
    ap.add_argument("--no-index", action="store_true", help="不重建索引页")
    args = ap.parse_args()

    if not args.date and not args.index:
        ap.error("请给出日期，或使用 --index")

    with tempfile.TemporaryDirectory() as wd:
        if args.date:
            stage, n_img = build_one(args.date, wd)
            push(stage, args.date)
            print(f"✅ 已发布 {PUBLIC_BASE}/{args.date}/deck.html")
            print(f"   配图 {n_img} 张")
        if args.index or not args.no_index:
            idx, dates = build_index(wd)
            push_index(idx)
            print(f"✅ 索引页已更新（共 {len(dates)} 期）→ {PUBLIC_BASE}/")


if __name__ == "__main__":
    main()
