---
name: wenjing
description: 文境创作者操作系统——一键启动道/境/卷/归藏/典阁五层结构。五个核心指令（收录/共创/成卷/入典/整理）驱动日常创作，动态看板可视化知识积累。核心理念：第一个念头，永远是人的。
version: 1.0.0
author: 文境创作者
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [wenjing, 文境, creator, writing, knowledge-management, agency]
    category: productivity
    related_skills: [wenjing-protocol]
---

# 文境（Wenjing）

文境是一套协议驱动的 AI 协作创作操作系统。它不是一个写作工具，而是一套确保「创作者在任何 AI 的帮助下，始终是自己的主人」的系统。

## 核心理念

**第一个念头，永远是人的。**

AI 帮你走得更远。但它不替你走出第一步。

- 收录，是你做的第一个判断（「这个东西让我有兴趣」）
- 共创，是你先看见的连接（AI 不先于你提炼方向）
- 成卷，标题和结构是你确认的（AI 不跳过确认）
- 入典，是你验证过的东西才入库
- 整理，删除权在你手里

## 何时触发

当用户说以下任一内容时，进入文境 Skill：
- 「启动文境」「创建文境」「初始化文境」
- 「收录 [内容]」「共创」「成卷」「入典 [内容]」「整理」

如果 Vault 已存在（非首次启动），直接进入共创模式。

---

## 一、Bootstrap：首次启动

当用户在新设备上首次说「启动文境」时，执行以下流程：

### 第 0 步：检查 Obsidian

确认用户设备上已安装 Obsidian。如未安装：

```
⚠ 未检测到 Obsidian。

请先下载安装：
  https://obsidian.md/download

安装完成后，创建一个新的 Vault，然后回来说「启动文境」。
```

不跳过此步骤。Obsidian 是文境的创作界面，没有它后续步骤无意义。

### 第 1 步：确认路径

询问用户 Obsidian Vault 的路径。如果用户未指定，使用当前工作目录。

```
请指定 Obsidian Vault 路径（留空使用当前目录）：
```

### 第 2 步：创建目录结构

在 Vault 路径下创建完整的五层目录。参考 `templates/` 目录中预定义的目录结构，使用 `write_file` 逐个创建。

目录清单（必须全部创建）：
```
01 悟道（系统）/
  01 山门/
  02 境志/

02 养境（知识）/
  00 知识目录/
  01 藏阁/
    01 Inbox/
  02 典阁/
    01 Library/
      创作体系/
      技术知识/
      法律与规则/
      客观知识/

03 成卷（项目）/

04 Agent入口/

05 归藏（存档）/
  01 成卷归档/
  02 养境归档/
  03 典藏归档/

06 文境开发（Development）/    ← 仅当用户明确需要开发模式时创建
```

### 第 3 步：写入种子文档

按 `templates/` 目录中的文件，逐一写入 Vault。templates/ 路径与 Vault 路径一一对应：

| 模板路径 | → Vault 路径 |
|----------|-------------|
| `templates/道/00 道说明.md` | `01 悟道（系统）/00 道说明.md` |
| `templates/道/01 山门/1.1 文境门训.md` | `01 悟道（系统）/01 山门/1.1 文境门训.md` |
| `templates/道/01 山门/1.2 文境总纲.md` | `01 悟道（系统）/01 山门/1.2 文境总纲.md` |
| `templates/道/01 山门/1.3 入境录.md` | `01 悟道（系统）/01 山门/1.3 入境录.md` |
| `templates/道/03 文境系统约束.md` | `01 悟道（系统）/03 文境系统约束.md` |
| `templates/境/境层知识索引.md` | `02 养境（知识）/境层知识索引.md` |
| `templates/境/01 藏阁/00 藏阁使用方式.md` | `02 养境（知识）/01 藏阁/00 藏阁使用方式.md` |
| `templates/境/02 典阁/00 典阁使用方式.md` | `02 养境（知识）/02 典阁/00 典阁使用方式.md` |
| `templates/卷/卷使用方式.md` | `03 成卷（项目）/卷使用方式.md` |
| `templates/归藏/00 归藏说明.md` | `05 归藏（存档）/00 归藏说明.md` |
| `templates/文境看板.html` | `文境看板.html` |

Agent 入口文档（04 Agent入口/）在 Bootstrap 阶段不需要创建——这些协议由 `wenjing-protocol` skill 运行时读取，不存储在 Vault 中。**但如果用户明确要求将协议文档写入 Vault**，则将以下文件写入：

| 模板路径 | → Vault 路径 |
|----------|-------------|
| `templates/Agent入口/00 文境入口.md` | `04 Agent入口/00 文境入口.md` |
| `templates/Agent入口/01 工作模式确认.md` | `04 Agent入口/01 工作模式确认.md` |
| `templates/Agent入口/02 共创入口.md` | `04 Agent入口/02 共创入口.md` |
| `templates/Agent入口/03 AI阅读原则.md` | `04 Agent入口/03 AI阅读原则.md` |
| `templates/Agent入口/05 Workflow Index.md` | `04 Agent入口/05 Workflow Index.md` |

### 第 4 步：配置 Obsidian

运行 `scripts/setup_obsidian.py` 自动完成：
- 开启推荐的核心插件（文件浏览器、图谱、反向链接、Canvas 等 18 项）
- 下载并安装 7 个社区插件（Startpage / HTML Viewer+ / Select Folder / Editing Toolbar / Full Calendar / Style Settings / PDF+）
- 启用社区插件模式

```bash
python scripts/setup_obsidian.py "VAULT_PATH"
```

需要网络连接。安装完成后提示用户重启 Obsidian。

### 第 5 步：设置看板刷新

使用 `cronjob` 工具创建定时任务，按用户指定频率（默认每天一次）运行 `scripts/refresh_dashboard.py` 刷新看板数据。

```bash
# 每天一次（默认）
cronjob create: 文境看板刷新，schedule="0 9 * * *"，script="scripts/refresh_dashboard.py"

# 或按用户指定频率
```

### 第 6 步：确认完成

输出初始化报告：

```
文境已就绪。

✓ 01 悟道（系统）  — 道说明 / 门训 / 总纲 / 入境录 / 系统约束
✓ 02 养境（知识）  — 藏阁 Inbox / 典阁 Library / 知识目录
✓ 03 成卷（项目）  — 卷使用方式
✓ 05 归藏（存档）  — 归藏说明
✓ Obsidian 配置   — 核心插件 + 7 个社区插件（请重启 Obsidian）
✓ 文境看板.html   — 动态仪表盘（每天自动刷新）

五个指令：
  收录 · 共创 · 成卷 · 入典 · 整理

重启 Obsidian → 打开文境看板.html → 开始创作。
```

---

## 二、日常协作：五个指令

Bootstrap 完成后，Agent 进入 Conversation Runtime（默认状态），持续监听五个指令。

### 1. 收录

**触发词**：「收录 [内容]」「保存到藏阁」「记录」

**Agent 执行**：
1. 加载 `wenjing-protocol` skill 中的 Capture Workflow
2. 将内容写入 `02 养境（知识）/01 藏阁/01 Inbox/`，遵循 Inbox Standard 格式
3. 文件命名：【类型】标题（类型从：念/摘/事/梦/感/随/文/对/白/图 中选择最匹配的）
4. YAML frontmatter 必须包含：status / type / tags / publish_date / confidence。`resource_url` 仅当有真实 URL 时保留空值则删行
5. 正文含：Resource / Original Content / Summary / Insight / References

**Agent 不做什么**：
- 不追问「你为什么收了它」——收录本身就是判断
- 不替创作者评估价值
- 不自行决定类型（应基于内容特征建议，但可由创作者调整）

### 2. 共创

**触发词**：「共创」

**Agent 执行**：
1. 扫描 `02 养境（知识）/01 藏阁/01 Inbox/` 中 status ≠ 成卷 的条目
2. 随机抽取 3 条，展示**原文摘要**（不提炼、不总结、不生成方向）
3. 问：「哪一条让你有感觉？或者你感觉到了什么联系？」

**关键原则**：AI 不先于创作者提炼方向。展示原文，等创作者先说出自己的直觉，AI 再基于创作者的回答展开/补充/挑战/连接。

**严禁**：
- 列出全部条目（浪费算力）
- 先于创作者输出「三个创作方向」
- 把分析结果表述为「确定答案」

### 3. 成卷

**触发词**：「成卷」

**Agent 执行**：
1. 基于当前讨论，生成 3 个标题方向供选择
2. 用户选择后，生成章节结构，再次等待确认
3. 确认后，一次性生成完整正文
4. 创建卷目录（命名：`卷NNN · 标题简写/`）
5. 创建两个文件：`创作过程：标题.md`（YAML + 共创记录 + 来源链接）和 `正文：标题.md`（纯正文）
6. 创作过程文件 YAML 中声明 `aliases`（主题简称 + 卷编号）
7. 将来源 Inbox 条目的 status 更新为「成卷」，在 References 中建立双向链接

**两步确认缺一不可。AI 不跳过确认直接写，不替创作者定标题。**

### 4. 入典

**触发词**：「入典 [内容描述]」

**Agent 执行**：
1. 确认内容类型：创作体系 / 技术知识 / 法律与规则 / 客观知识
2. 确认子目录位置
3. 将内容写入 `02 养境（知识）/02 典阁/01 Library/[分类]/`
4. 文件命名：描述性标题，不强制前缀格式

**入典判断标准**：一年后，我还需要引用它吗？

**不做什么**：不入典未经验证的灵感碎片。典阁不是第二个藏阁。

### 5. 整理

**触发词**：「整理」「分类」「重构」

**Agent 执行**：
1. 扫描 Inbox，按 type 和 tags 分类展示
2. 建议归并、状态更新
3. 等待创作者确认后执行

**不做什么**：不自行决定删除任何内容。删除权永远在创作者手里。

---

## 三、看板维护

动态看板 `文境看板.html` 位于 Vault 根目录。

### 手动刷新

当用户说「刷新看板」时，运行 `scripts/refresh_dashboard.py` 脚本。

脚本逻辑：
1. 扫描 Inbox 目录，统计各 type 数量
2. 扫描成卷目录，统计卷数量
3. 扫描归藏目录，统计归档数量
4. 扫描典阁 Library 目录，统计各类条目数
5. 更新看板 HTML 中的数字和状态日期

### 自动刷新

Bootstrap 第 4 步已设置 cron job。默认每天刷新一次。用户可通过「看板刷新频率 [小时/天]」调整。

---

## 四、协议依赖

本 Skill 依赖 `wenjing-protocol` skill 提供协议层逻辑：
- 入口协议（00 文境入口 → 01 模式选择 → 02/04 模式入口）
- Workflow Index（Capture / Organization / Archive / Reflection）
- 系统约束（决策权/收敛/阶段控制/缓判）
- Inbox Standard、Capture Convention 等格式规范

本 Skill 负责：
- Bootstrap（首次初始化）
- 五个指令的触发与分发
- 看板维护
- 典阁规则（wenjing-protocol 中未定义）

---

## 五、注意事项

1. **Vault 根目录保护**：Bootstrap 时不在 Vault 根目录创建除看板外的任何文件
2. **Lazy Loading**：不主动索引整个 Vault，仅按需读取
3. **阶段控制**：AI 不主动切换阶段、不主动推进流程
4. **缓判**：重要方向不因 AI 一次建议立即确定
5. **收敛约束**：共创阶段不主动生成完整成品
6. **文件操作**：Windows 环境下禁用 `sed -i`，使用 `patch` 或 Python 原生 `open()` 修改文件

---

## 六、文件路径速查

| 内容 | 路径 |
|------|------|
| 藏阁 Inbox | `{vault}/02 养境（知识）/01 藏阁/01 Inbox/` |
| 典阁 Library | `{vault}/02 养境（知识）/02 典阁/01 Library/` |
| 成卷目录 | `{vault}/03 成卷（项目）/` |
| 归藏目录 | `{vault}/05 归藏（存档）/` |
| 道层文档 | `{vault}/01 悟道（系统）/` |
| 看板 | `{vault}/文境看板.html` |
