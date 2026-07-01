#!/usr/bin/env python3
"""文境看板刷新脚本
扫描 Vault 真实文件，更新看板 HTML 中的统计数据。
由 Hermes Cron 定时触发，也可手动运行。
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path


def get_vault_path():
    """从环境变量或默认路径获取 Vault 根目录"""
    vault = os.environ.get("WENJING_VAULT", "")
    if vault and os.path.isdir(vault):
        return vault
    # 回退：从脚本位置推断（scripts/ → wenjing/ → skills/ → hermes/）
    script_dir = Path(__file__).parent
    # 尝试常见位置
    candidates = [
        script_dir.parent.parent.parent / "文境Vault",
        Path.cwd(),
    ]
    for c in candidates:
        inbox = c / "02 养境（知识）" / "01 藏阁" / "01 Inbox"
        if inbox.is_dir():
            return str(c)
    return str(Path.cwd())


def count_inbox(vault_path):
    """统计藏阁 Inbox 条目"""
    inbox_dir = Path(vault_path) / "02 养境（知识）" / "01 藏阁" / "01 Inbox"
    if not inbox_dir.is_dir():
        return {"total": 0, "摘": 0, "念": 0, "other": 0}

    counts = {"total": 0, "摘": 0, "念": 0, "other": 0}
    type_map = {
        "摘": "摘", "念": "念",
        "文": "other", "对": "other", "事": "other",
        "课": "other", "随": "other", "梦": "other",
        "感": "other", "白": "other", "图": "other",
    }

    for f in inbox_dir.glob("*.md"):
        counts["total"] += 1
        content = f.read_text(encoding="utf-8", errors="ignore")
        # 从 YAML frontmatter 或文件名提取 type
        m = re.search(r'type:\s*(\S+)', content)
        if m:
            t = m.group(1)
            key = type_map.get(t, "other")
            counts[key] += 1
        elif f.stem.startswith("【摘】"):
            counts["摘"] += 1
        elif f.stem.startswith("【念】"):
            counts["念"] += 1
        else:
            counts["other"] += 1
    return counts


def count_juan(vault_path):
    """统计成卷数量"""
    juan_dir = Path(vault_path) / "03 成卷（项目）"
    if not juan_dir.is_dir():
        return 0
    return sum(1 for d in juan_dir.iterdir() if d.is_dir() and d.name.startswith("卷"))


def count_guizang(vault_path):
    """统计归藏数量"""
    guizang_dir = Path(vault_path) / "05 归藏（存档）"
    if not guizang_dir.is_dir():
        return {"total": 0, "成卷归档": 0, "养境归档": 0, "典藏归档": 0}

    counts = {"total": 0, "成卷归档": 0, "养境归档": 0, "典藏归档": 0}
    for sub in ["01 成卷归档", "02 养境归档", "03 典藏归档"]:
        subdir = guizang_dir / sub
        if subdir.is_dir():
            n = len([f for f in subdir.glob("*.md")])
            key = sub.replace("01 ", "").replace("02 ", "").replace("03 ", "")
            counts[key] = n
            counts["total"] += n
    return counts


def count_dian(vault_path):
    """统计典阁条目"""
    dian_dir = Path(vault_path) / "02 养境（知识）" / "02 典阁" / "01 Library"
    if not dian_dir.is_dir():
        return {"total": 0, "创作体系": 0, "技术知识": 0, "法律客观": 0}

    counts = {"total": 0, "创作体系": 0, "技术知识": 0, "法律客观": 0}
    for root, _, files in os.walk(dian_dir):
        md_count = sum(1 for f in files if f.endswith(".md"))
        if md_count == 0:
            continue
        rel = Path(root).relative_to(dian_dir)
        parts = rel.parts
        if parts and parts[0] == "创作体系":
            counts["创作体系"] += md_count
        elif parts and parts[0] == "技术知识":
            counts["技术知识"] += md_count
        elif parts and parts[0] in ("法律与规则", "客观知识"):
            counts["法律客观"] += md_count
        counts["total"] += md_count
    return counts


def update_html(vault_path, inbox_stats, juan_count, guizang_stats, dian_stats):
    """更新看板 HTML 中的动态数据"""
    html_path = Path(vault_path) / "文境看板.html"
    if not html_path.is_file():
        print(f"✗ 看板文件不存在: {html_path}")
        return False

    html = html_path.read_text(encoding="utf-8", errors="ignore")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 替换 Vault 名称（用于 obsidian:// 链接）
    vault_name = Path(vault_path).name
    html = html.replace("VAULT_NAME", vault_name)

    # 替换藏阁统计
    html = re.sub(
        r'id="inbox-count">\d+<',
        f'id="inbox-count">{inbox_stats["total"]}<',
        html
    )
    # 摘
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">摘)',
        rf'\g<1>{inbox_stats["摘"]}\g<2>',
        html
    )
    # 念
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">念)',
        rf'\g<1>{inbox_stats["念"]}\g<2>',
        html
    )
    # other
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">文/对/事/课/随)',
        rf'\g<1>{inbox_stats["other"]}\g<2>',
        html
    )

    # 卷
    html = re.sub(
        r'id="juan-count">\d+<',
        f'id="juan-count">{juan_count}<',
        html
    )

    # 归藏
    html = re.sub(
        r'id="guizang-count">\d+<',
        f'id="guizang-count">{guizang_stats["total"]}<',
        html
    )

    # 典阁
    html = re.sub(
        r'id="dian-count">\d+<',
        f'id="dian-count">{dian_stats["total"]}<',
        html
    )
    # 创作体系
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">创作体系)',
        rf'\g<1>{dian_stats["创作体系"]}\g<2>',
        html
    )
    # 技术知识
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">技术知识)',
        rf'\g<1>{dian_stats["技术知识"]}\g<2>',
        html
    )
    # 法律/客观
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">法律/客观)',
        rf'\g<1>{dian_stats["法律客观"]}\g<2>',
        html
    )

    # 更新状态日期
    html = re.sub(
        r'id="status-date">[^<]*<',
        f'id="status-date">{now}<',
        html
    )

    html_path.write_text(html, encoding="utf-8")
    return True


def latest_volumes(vault_path):
    """获取最新 3 卷的正文文件名"""
    juan_dir = Path(vault_path) / "03 成卷（项目）"
    if not juan_dir.is_dir():
        return []
    vols = []
    for d in sorted(juan_dir.iterdir(), reverse=True):
        if d.is_dir() and d.name.startswith("卷"):
            for f in d.iterdir():
                if f.name.startswith("正文"):
                    vols.append((d.name, f.stem))
                    break
            if len(vols) >= 3:
                break
    return vols


def update_speedview(vault_path, inbox, juan, dian, vols):
    """更新文境速览.html"""
    sv_path = Path(vault_path) / "文境速览.html"
    if not sv_path.is_file():
        print(f"  ⚠ 速览文件不存在: {sv_path}")
        return False

    html = sv_path.read_text(encoding="utf-8", errors="ignore")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 三大数字
    html = re.sub(r'id="inbox-num">\d+<', f'id="inbox-num">{inbox["total"]}<', html)
    html = re.sub(r'id="dian-num">\d+<', f'id="dian-num">{dian["total"]}<', html)
    html = re.sub(r'id="juan-num">\d+<', f'id="juan-num">{juan}<', html)

    # 藏阁子统计
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">摘)',
        rf'\g<1>{inbox["摘"]}\g<2>', html)
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">念)',
        rf'\g<1>{inbox["念"]}\g<2>', html)
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">文/对/事/课/随)',
        rf'\g<1>{inbox["other"]}\g<2>', html)

    # 典阁子统计
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">创作体系)',
        rf'\g<1>{dian["创作体系"]}\g<2>', html)
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">技术知识)',
        rf'\g<1>{dian["技术知识"]}\g<2>', html)
    html = re.sub(
        r'(<div class="stat"><div class="num">)\d+(</div><div class="label">法律/客观)',
        rf'\g<1>{dian["法律客观"]}\g<2>', html)

    # Build volume list HTML
    if vols:
        vol_html = ""
        for vname, zname in vols:
            vol_html += f'<div class="vol-item"><span class="vol-tag">{vname}</span><span class="vol-name">{zname}</span></div>\n'
        html = re.sub(
            r'<div id="vol-list">.*?</div>',
            f'<div id="vol-list">\n{vol_html}</div>',
            html,
            flags=re.DOTALL
        )

    html = re.sub(r'id="foot-date">[^<]*<', f'id="foot-date">{now}<', html)
    sv_path.write_text(html, encoding="utf-8")
    return True


def main():
    vault_path = get_vault_path()
    print(f"Vault: {vault_path}")

    inbox = count_inbox(vault_path)
    juan = count_juan(vault_path)
    guizang = count_guizang(vault_path)
    dian = count_dian(vault_path)

    print(f"  藏阁: {inbox['total']} (摘{inbox['摘']} 念{inbox['念']} 其他{inbox['other']})")
    print(f"  成卷: {juan}")
    print(f"  归藏: {guizang['total']}")
    print(f"  典阁: {dian['total']} (创作{dian['创作体系']} 技术{dian['技术知识']} 法律客观{dian['法律客观']})")

    if update_html(vault_path, inbox, juan, guizang, dian):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"  ✓ 看板已刷新 ({now})")
    else:
        print("  ✗ 看板更新失败")

    vols = latest_volumes(vault_path)
    if update_speedview(vault_path, inbox, juan, dian, vols):
        print(f"  ✓ 速览已刷新")
    else:
        print("  ⚠ 速览更新跳过")


if __name__ == "__main__":
    main()
