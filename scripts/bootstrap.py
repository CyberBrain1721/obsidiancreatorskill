#!/usr/bin/env python3
"""文境 Bootstrap 脚本
从 Skill 的 templates/ 目录批量复制种子文档到 Vault。
"""

import os, shutil, json
from pathlib import Path


CORE_PLUGINS = {
    "file-explorer": True, "global-search": True, "switcher": True,
    "graph": True, "backlink": True, "canvas": True,
    "outgoing-link": True, "tag-pane": True, "properties": True,
    "page-preview": True, "daily-notes": True, "templates": True,
    "note-composer": True, "command-palette": True, "editor-status": True,
    "bookmarks": True, "markdown-importer": True, "outline": True,
    "word-count": True, "file-recovery": True,
    "sync": False, "publish": False, "slides": False,
    "audio-recorder": False, "workspaces": False, "footnotes": False,
    "slash-command": False, "zk-prefixer": False, "random-note": False,
    "bases": False, "webviewer": False,
}

COMMUNITY_PLUGINS = [
    "start-page", "html-viewer-plus", "select-folder",
    "editing-toolbar", "obsidian-full-calendar",
    "obsidian-style-settings", "pdf-plus",
]


def bootstrap(vault_path):
    vault = Path(vault_path)
    skill_dir = Path(__file__).parent.parent

    # ---- 1. 创建目录结构 ----
    dirs = [
        "01 悟道（系统）/01 山门",
        "01 悟道（系统）/02 境志",
        "02 养境（知识）/00 知识目录",
        "02 养境（知识）/01 藏阁/01 Inbox",
        "02 养境（知识）/02 典阁/01 Library/创作体系",
        "02 养境（知识）/02 典阁/01 Library/技术知识",
        "02 养境（知识）/02 典阁/01 Library/法律与规则",
        "02 养境（知识）/02 典阁/01 Library/客观知识",
        "03 成卷（项目）",
        "04 Agent入口",
        "05 归藏（存档）/01 成卷归档",
        "05 归藏（存档）/02 养境归档",
        "05 归藏（存档）/03 典藏归档",
    ]
    for d in dirs:
        (vault / d).mkdir(parents=True, exist_ok=True)
    print(f"  ✓ 目录结构已创建")

    # ---- 2. 复制种子文档 ----
    templates_dir = skill_dir / "templates"
    copied = 0
    for root, _, files in os.walk(templates_dir):
        for f in files:
            src = Path(root) / f
            rel = src.relative_to(templates_dir)
            dst = vault / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1
    print(f"  ✓ {copied} 个种子文档已写入")

    # ---- 3. 复制插件 ----
    plugins_src = skill_dir / "plugins"
    plugins_dst = vault / ".obsidian" / "plugins"
    if plugins_src.is_dir():
        plugins_dst.mkdir(parents=True, exist_ok=True)
        plugin_count = 0
        for pid in os.listdir(plugins_src):
            src_p = plugins_src / pid
            dst_p = plugins_dst / pid
            if src_p.is_dir():
                if dst_p.exists():
                    shutil.rmtree(dst_p)
                shutil.copytree(src_p, dst_p)
                plugin_count += 1
        print(f"  ✓ {plugin_count} 个插件已安装")

    # ---- 4. 写入 Obsidian 配置 ----
    obsidian = vault / ".obsidian"
    obsidian.mkdir(parents=True, exist_ok=True)

    (obsidian / "core-plugins.json").write_text(
        json.dumps(CORE_PLUGINS, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (obsidian / "community-plugins.json").write_text(
        json.dumps(COMMUNITY_PLUGINS, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"  ✓ Obsidian 配置已写入")

    # ---- 5. 写入 AGENTS.md（Codex/Claude Code/WorkBuddy 通用入口） ----
    agents_src = skill_dir / "templates" / "AGENTS.md"
    if agents_src.is_file():
        shutil.copy2(agents_src, vault / "AGENTS.md")

    # ---- 6. 生成 Canvas 速览 ----
    sys.path.insert(0, str(script_dir / "scripts"))
    from generate_canvas import generate_canvas
    generate_canvas(str(vault))
    print(f"  ✓ Canvas 速览已生成")

    print(f"\n文境已就绪。重启 Obsidian 后打开 文境速览.canvas 或 文境看板.html。")


if __name__ == "__main__":
    import sys
    vault = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("WENJING_VAULT", os.getcwd())
    print(f"Vault: {vault}\n")
    bootstrap(vault)
