# 文境 · Wenjing

> 在无限答案的时代，保护你构建自己的认知，而非消费别人的。

> ⚠️ **当前版本**：Hermes Agent 测试版。功能持续迭代中，欢迎反馈。

---

AI 能产出的内容已经无限多了。你丢一个题目，它给你三个方向。你选一个，它帮你写完。整个过程快得令人不安——但回头想一个问题：**那个方向是你自己看出来的，还是 AI 替你看到的？**

答案不好听：你在 AI 抛出选项之前，根本没想过那个方向。你只是在三个锅里选了一口。这不是创作。这叫选题会。

文境要保护的，不是效率，不是产出，不是「写得更多」。是**主体性**——你作为一个创作者，能不能始终知道：哪个想法是我自己的，哪条路是我先看到的，哪个决定是未经 AI 修饰之前就已经在我脑子里的。

**第一个念头，永远是人的。**

---

## 不是什么

- ❌ 不是自动写作工具——AI 不替你生成内容，不替你产生第一个念头
- ❌ 不是知识图谱系统——不做自动知识网络构建。那是 Graphify、GBrain 做的事
- ❌ 不是 Markdown 模板——不规定你的文章长什么样

## 是什么

文境的核心资产是 **创作运行时（Creative Runtime）**：一套协议，组织创作者的注意力、判断和创作过程。

它是五层架构的一条循环——道指导境，境孕育卷，卷完成归藏，归藏提炼入典，典阁服务未来的卷。此循环永不终止。

它是五个指令——收录、共创、成卷、入典、整理。每条指令都有明确的「AI 不做什么」。这比「AI 做什么」更重要。

它是一句「启动文境」——新设备上 5 分钟全部就绪：创建目录、写入协议、安装 Obsidian 插件、设置看板定时刷新。

---

## 五层架构

| 层 | 职责 | 一句话 |
|----|------|--------|
| **道** | 系统原则 | 人做什么，AI 做什么，边界在哪 |
| **境** | 知识积累 | 灵感进藏阁，沉淀入典阁 |
| **卷** | 具体作品 | 从共创到正文到完成 |
| **归藏** | 作品归档 | 完成使命，不烂在作品里 |
| **典阁** | 长期资产 | 一年后，我还需要引用它吗？ |

## 五个指令

| 指令 | 用法 | AI 不做什么 |
|------|------|------------|
| **收录** | `收录 [内容或URL]` | 不追问「为什么收」——收录本身就是判断 |
| **共创** | `共创` | 不先于你提炼方向——先问「你看到了什么」 |
| **成卷** | `成卷` | 不跳过确认——标题和结构两步都等你点头 |
| **入典** | `入典 [描述]` | 不入未经验证的碎片——典阁不是第二个藏阁 |
| **整理** | `整理` | 不自行删除——删除权永远在你手里 |

## 系统约束

AI 不替创作者走第一步。七条约束全部内嵌，你不需要读——说「收录」「共创」「成卷」，AI 自己知道边界。

---

## 看板

两个动态仪表盘，浏览器打开即用。数据由 Cron 自动刷新，每格数字都是真实 Vault 扫描结果。

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

## 协议通用，工具层当前为 Hermes 实现

文境的协议层（`04 Agent入口/` 下的入口、模式选择、Workflow Index、系统约束）是 **Agent 无关的**——任何能读写 Markdown 的 AI Agent 都可以读取并执行。

| 层面 | 当前实现 |
|------|---------|
| 协议文档（入口/Workflow/约束） | 通用 |
| Bootstrap 脚本 / 看板刷新 | Python（Hermes `terminal` 工具执行） |
| Skill 打包格式 | Hermes `SKILL.md` |
| 插件捆绑 / Obsidian 配置 | Python 脚本 |
| Cron 定时刷新 | Hermes `cronjob` |

在其他 Agent（如 WorkBuddy、Codex、Claude Code）上使用：将 Vault 设为 working directory，指示 Agent「读取 `04 Agent入口/00 文境入口.md`，按协议执行」即可。Bootstrap 和看板刷新需手动运行 `scripts/` 下的 Python 脚本。

---

## 理念

文境的核心不是知识图谱——知识图谱可以从任何工具来。文境的核心是 **Creative Runtime**：在 AI 能吐出无限内容的世界里，如何保证你产出的每一个字，根源在你自己。

> **Human Self-Governance in the AI Era.**
