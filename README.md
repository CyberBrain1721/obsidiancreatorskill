# 文境 · Wenjing

> 一个协议驱动的 AI 协作创作系统。在无限答案的时代，帮助创作者构建自己的认知体系。

> ⚠️ **当前版本**：Hermes Agent 测试版。功能持续迭代中，欢迎反馈。

---

AI 能产出的内容已经无限多了。你丢一个题目，它给你三个方向。你选一个，它帮你写完。整个过程快得令人不安——但回头想一个问题：那个方向是你自己看出来的，还是 AI 替你的？

你之前在 AI 抛出选项时，根本没想过那个方向。你只是在三个锅里选了一口。这不是创作。这叫选题会。

---

## 概述

文境是一套基于 Obsidian Vault 的创作操作系统。它通过五层架构（道/境/卷/归藏/典阁）和五个指令（收录/共创/成卷/入典/整理）组织创作流程，核心理念是让创作者在 AI 协作中保持判断力——**第一个念头，永远是人的。**

---

## 五层架构

| 层 | 职责 |
|----|------|
| **道** | 系统原则与 AI 行为边界 |
| **境** | 知识积累：藏阁（灵感收集）+ 典阁（知识沉淀） |
| **卷** | 具体作品项目 |
| **归藏** | 已完成作品的归档 |
| **典阁** | 跨项目可复用的长期知识资产 |

## 五个指令

| 指令 | 用法 | 说明 |
|------|------|------|
| **收录** | `收录 [内容或URL]` | 将灵感和参考材料格式化存入藏阁 |
| **共创** | `共创` | 从藏阁中随机抽取灵感，展开讨论 |
| **成卷** | `成卷` | 基于讨论生成完整文章，建立卷项目 |
| **入典** | `入典 [描述]` | 将验证过的知识沉淀到典阁 |
| **整理** | `整理` | 分类、归并藏阁条目 |

---

## 看板

两个动态仪表盘，浏览器打开即用。数据定时自动刷新。

| 看板 | 内容 |
|------|------|
| `文境看板.html` | 全貌：道 / 藏阁 / 典阁 / 卷 / 归藏 / 共创指令 |
| `文境速览.html` | 精简：藏阁 / 典阁 / 成卷 + 最新三卷 |

---

## 快速开始

### Hermes Agent

```bash
hermes skills install https://github.com/CyberBrain1721/obsidiancreatorskill
hermes -s wenjing
# 然后说：启动文境
```

### 其他 Agent（WorkBuddy / Codex / Claude Code）

```bash
git clone https://github.com/CyberBrain1721/obsidiancreatorskill
cd /path/to/WenjingVault
python ../obsidiancreatorskill/scripts/bootstrap.py .   # 首次初始化
# 告诉 Agent：读取 04 Agent入口/00 文境入口.md，按协议执行
```

---

## 依赖

- [Obsidian](https://obsidian.md/download)
- [Dataview 插件](https://github.com/blacksmithgu/obsidian-dataview)（手动安装）

Bootstrap 自动安装的插件：
Startpage · HTML Viewer+ · Select Folder · Editing Toolbar · Full Calendar · Style Settings · PDF+

---

## 协议通用

文境的协议层（`04 Agent入口/` 下的入口、模式选择、Workflow Index、系统约束）是 Agent 无关的——任何能读写 Markdown 的 AI Agent 都可以读取并执行。

| 层面 | 当前实现 |
|------|---------|
| 协议文档（入口/Workflow/约束） | 通用 |
| Bootstrap / 看板刷新 | Python 脚本 |
| Skill 打包格式 | Hermes `SKILL.md` |
| 插件捆绑 / Obsidian 配置 | Python 脚本 |
| 定时刷新 | Hermes `cronjob` |

在其他 Agent 上使用：将 Vault 设为 working directory，指示 Agent「读取 `04 Agent入口/00 文境入口.md`，按协议执行」。Bootstrap 和看板刷新需手动运行 `scripts/` 下的 Python 脚本。

---

## 理念

文境的核心是 **Creative Runtime（创作运行时）**——在 AI 协作中，通过协议和结构帮助创作者保持判断力与主体性。

> **Human Self-Governance in the AI Era.**
