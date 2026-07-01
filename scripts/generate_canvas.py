#!/usr/bin/env python3
"""生成文境速览.canvas — Obsidian 原生看板，wiki 链接可点击"""

import os, json
from datetime import datetime
from pathlib import Path

def generate_canvas(vault_path):
    vault = Path(vault_path)
    inbox_dir = vault / "02 养境（知识）" / "01 藏阁" / "01 Inbox"
    juan_dir = vault / "03 成卷（项目）"
    dian_dir = vault / "02 养境（知识）" / "02 典阁" / "01 Library"

    # ---- 统计 ----
    inbox_files = list(inbox_dir.glob("*.md")) if inbox_dir.is_dir() else []
    inbox_total = len(inbox_files)

    # 按 status 分类 Inbox
    status_groups = {}
    for f in inbox_files:
        content = f.read_text(encoding="utf-8", errors="ignore")
        status = "其他"
        for line in content.split("\n")[:10]:
            if line.startswith("status:"):
                status = line.split(":", 1)[1].strip()
                break
        status_groups.setdefault(status, []).append(f.stem)

    # 成卷
    volumes = []
    if juan_dir.is_dir():
        for d in sorted(juan_dir.iterdir(), reverse=True):
            if d.is_dir() and d.name.startswith("卷"):
                zhengwen = None
                for f in d.iterdir():
                    if f.name.startswith("正文"):
                        zhengwen = f.stem
                        break
                if zhengwen:
                    volumes.append((d.name, zhengwen))
                if len(volumes) >= 3:
                    break
    juan_count = sum(1 for d in juan_dir.iterdir() if d.is_dir() and d.name.startswith("卷")) if juan_dir.is_dir() else 0

    # 典阁
    dian_count = 0
    if dian_dir.is_dir():
        for _, _, files in os.walk(dian_dir):
            dian_count += sum(1 for f in files if f.endswith(".md"))

    # ---- 构建 Canvas ----
    nodes = []

    # Header
    header_text = f"# 文境速览\n\n> **藏阁** {inbox_total} 条　·　**成卷** {juan_count} 个　·　**典阁** {'暂无内容' if dian_count == 0 else f'{dian_count} 条'}"
    nodes.append({"id": "header", "type": "text", "text": header_text, "x": -100, "y": -840, "width": 610, "height": 109, "color": "#A6B8C4"})

    # Inbox group
    nodes.append({"id": "inbox-group", "type": "group", "x": 580, "y": -800, "width": 520, "height": 720, "color": "#9DA9B8", "label": f"藏阁 Inbox（{inbox_total}）"})

    # Inbox status cards
    status_order = ["待发展", "待消化", "成卷", "其他"]
    status_labels = {"待发展": "待发展", "待消化": "待消化", "成卷": "成卷", "其他": "其他"}
    status_colors = {"待发展": "#C9B4A8", "待消化": "#C9B0B0", "成卷": "#AFC0AF", "其他": "#B8B0C4"}

    col_x = [600, 845]
    col_width = [230, 235]
    row_y = [-700, -360]
    row_height = [320, 240]

    col_idx = 0
    for si, status in enumerate(status_order):
        if status not in status_groups or not status_groups[status]:
            continue
        items = status_groups[status][:8]  # max 8 per card
        lines = [f"**{status_labels.get(status, status)}**　({len(status_groups[status])})", ""]
        for item in items:
            lines.append(f"- [[{item}]]")

        x = col_x[col_idx % 2]
        y = row_y[col_idx // 2]
        w = col_width[col_idx % 2]
        h = row_height[col_idx // 2]

        nodes.append({"id": f"status-{status}", "type": "text", "text": "\n".join(lines),
                       "x": x, "y": y, "width": w, "height": h,
                       "color": status_colors.get(status, "#B8B0C4")})
        col_idx += 1

    # Volumes group
    if volumes:
        vol_count = juan_count
        nodes.append({"id": "volumes-group", "type": "group", "x": -100, "y": -660, "width": 610, "height": 325, "color": "#A8B8A8", "label": f"最新成卷（共{vol_count}卷）"})

        for vi, (vname, zname) in enumerate(volumes):
            y_pos = -625 + vi * 90
            h = 85 if vi == 2 else 75
            nodes.append({"id": f"vol-{vi}", "type": "text",
                          "text": f"**{vname}**\n→ [[{zname}]]",
                          "x": -80, "y": y_pos, "width": 530, "height": h})

    # 典阁 group
    dian_label = "典阁 Library" if dian_count == 0 else f"典阁 Library（{dian_count}）"
    nodes.append({"id": "diange-group", "type": "group", "x": -100, "y": -260, "width": 610, "height": 180, "color": "#B8ADA8", "label": dian_label})

    dian_text = "##### 暂无内容\n\n长期沉淀的知识未来将归档于此" if dian_count == 0 else f"##### {dian_count} 条典阁条目\n\n[[02 养境（知识）/02 典阁/01 Library/|进入典阁]]"
    nodes.append({"id": "diange-content", "type": "text", "text": dian_text, "x": -80, "y": -200, "width": 330, "height": 80})

    canvas = {"nodes": nodes, "edges": []}

    canvas_path = vault / "文境速览.canvas"
    canvas_path.write_text(json.dumps(canvas, indent="\t", ensure_ascii=False), encoding="utf-8")
    return True


if __name__ == "__main__":
    import sys
    vault = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("WENJING_VAULT", os.getcwd())
    generate_canvas(vault)
    print(f"✓ 文境速览.canvas 已生成")
