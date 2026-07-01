#!/usr/bin/env python3
"""文境 Obsidian 初始化脚本
配置 Obsidian 核心设置并自动安装 7 个必备插件。
由文境 Skill bootstrap 流程调用，也可手动运行。
"""

import os
import json
import shutil
import urllib.request
from pathlib import Path


# ============================================================
# 插件定义
# ============================================================

PLUGINS = [
    {
        "id": "start-page",
        "name": "Startpage",
        "repo_owner": "kuzzh",
        "repo_name": "obsidian-startpage",
        "branch": "main",
    },
    {
        "id": "html-viewer-plus",
        "name": "HTML Viewer +",
        "repo_owner": "kuaile1407",
        "repo_name": "html-viewer-plus",
        "branch": "main",
    },
    {
        "id": "select-folder",
        "name": "Select Folder",
        "repo_owner": "frogtempest",
        "repo_name": "select-folder",
        "branch": "main",
    },
    {
        "id": "editing-toolbar",
        "name": "Editing Toolbar",
        "repo_owner": "pkm-er",
        "repo_name": "obsidian-editing-toolbar",
        "branch": "main",
    },
    {
        "id": "obsidian-full-calendar",
        "name": "Full Calendar",
        "repo_owner": "obsidian-community",
        "repo_name": "obsidian-full-calendar",
        "branch": "main",
    },
    {
        "id": "obsidian-style-settings",
        "name": "Style Settings",
        "repo_owner": "obsidian-community",
        "repo_name": "obsidian-style-settings",
        "branch": "main",
    },
    {
        "id": "pdf-plus",
        "name": "PDF +",
        "repo_owner": "ryotaushio",
        "repo_name": "obsidian-pdf-plus",
        "branch": "main",
    },
]

# 核心插件：推荐开启的列表
CORE_PLUGINS = {
    "file-explorer": True,
    "global-search": True,
    "switcher": True,
    "graph": True,
    "backlink": True,
    "canvas": True,
    "outgoing-link": True,
    "tag-pane": True,
    "properties": True,
    "page-preview": True,
    "daily-notes": True,
    "templates": True,
    "note-composer": True,
    "command-palette": True,
    "editor-status": True,
    "bookmarks": True,
    "markdown-importer": True,
    "outline": True,
    "word-count": True,
    "file-recovery": True,
    "sync": False,
    "publish": False,
    "slides": False,
    "audio-recorder": False,
    "workspaces": False,
    "footnotes": False,
    "slash-command": False,
    "zk-prefixer": False,
    "random-note": False,
    "bases": False,
    "webviewer": False,
}


# ============================================================
# 安装逻辑
# ============================================================

def download_file(url, dest):
    """下载单个文件，带 User-Agent 避免 GitHub 403"""
    req = urllib.request.Request(url, headers={"User-Agent": "wenjing-setup/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(dest, "wb") as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f"    ✗ 下载失败: {e}")
        return False


def install_plugin(vault_path, plugin):
    """安装单个 Obsidian 插件"""
    plugin_dir = Path(vault_path) / ".obsidian" / "plugins" / plugin["id"]
    plugin_dir.mkdir(parents=True, exist_ok=True)

    owner = plugin["repo_owner"]
    repo = plugin["repo_name"]
    branch = plugin["branch"]
    base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"

    files = ["manifest.json", "main.js"]
    # styles.css 是可选的
    styles_url = f"{base_url}/styles.css"

    success = True
    for filename in files:
        url = f"{base_url}/{filename}"
        dest = plugin_dir / filename
        if download_file(url, str(dest)):
            print(f"    ✓ {filename}")
        else:
            success = False

    # 尝试下载 styles.css（不存在也不报错）
    try:
        req = urllib.request.Request(styles_url, headers={"User-Agent": "wenjing-setup/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            dest = plugin_dir / "styles.css"
            with open(dest, "wb") as f:
                f.write(resp.read())
            print(f"    ✓ styles.css")
    except Exception:
        pass  # styles.css 不存在是正常的

    return success


def write_core_plugins(vault_path):
    """写入核心插件配置"""
    config_path = Path(vault_path) / ".obsidian" / "core-plugins.json"
    config_path.write_text(
        json.dumps(CORE_PLUGINS, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print("  ✓ core-plugins.json")


def write_community_plugins(vault_path):
    """写入社区插件启用列表"""
    plugin_ids = [p["id"] for p in PLUGINS]
    config_path = Path(vault_path) / ".obsidian" / "community-plugins.json"
    config_path.write_text(
        json.dumps(plugin_ids, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print("  ✓ community-plugins.json")


def setup_obsidian(vault_path):
    """一键配置 Obsidian：核心插件 + 7 个社区插件"""
    vault = Path(vault_path)
    if not vault.is_dir():
        print(f"✗ Vault 路径不存在: {vault_path}")
        return False

    obsidian_dir = vault / ".obsidian"
    obsidian_dir.mkdir(parents=True, exist_ok=True)

    print("📦 配置核心插件...")
    write_core_plugins(vault_path)

    print(f"\n📥 安装 {len(PLUGINS)} 个社区插件...")
    success_count = 0
    for i, plugin in enumerate(PLUGINS, 1):
        print(f"  [{i}/{len(PLUGINS)}] {plugin['name']} ({plugin['id']})")
        if install_plugin(vault_path, plugin):
            success_count += 1
        else:
            print(f"    ⚠ 部分文件下载失败，请检查网络")

    print(f"\n🔌 启用社区插件...")
    write_community_plugins(vault_path)

    print(f"\n✓ 完成: {success_count}/{len(PLUGINS)} 个插件安装成功")
    print("  请重启 Obsidian 使配置生效。")
    return True


def main():
    import sys
    vault_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("WENJING_VAULT", os.getcwd())
    print(f"Vault: {vault_path}\n")
    setup_obsidian(vault_path)


if __name__ == "__main__":
    main()
