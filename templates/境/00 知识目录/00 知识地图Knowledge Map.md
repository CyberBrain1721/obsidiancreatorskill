

## 目的

Knowledge Map 是文境 Knowledge Layer 的统一知识地图。

它保存文境当前已经确认的 Canonical Knowledge。

Knowledge Map 不保存文章。

不保存灵感。

不保存项目。

不保存开发文档。

Knowledge Map 仅维护长期稳定存在的核心知识节点，并作为整个文境知识网络唯一的规范引用来源。

所有 Agent 在建立 Tags 与 Related Links 前，应首先查询 Knowledge Map。

---

# 使用说明

Knowledge Map 采用 Registry 方式维护。

每一行代表一个 Canonical Node。

Canonical Node 是整个文境知识网络唯一允许引用的标准概念。

所有 Agent 应优先复用已有 Canonical。

只有经过创作者确认的新概念，方可加入 Knowledge Map。

---

# 字段说明

Canonical

文境唯一标准名称。

所有 Wikilink 应统一引用 Canonical。

---

Tag

Obsidian 标准标签。

所有 Metadata 应统一引用 Tag。

Tag 不得使用 Alias。

---

Alias

Canonical 的同义词。

Agent 查询时，应同时匹配 Canonical 与 Alias。

Alias 不作为最终输出。

---

Status

节点生命周期。

目前支持：

Active

Deprecated

---

Notes

节点说明。

用于帮助 Agent 判断引用范围。

Notes 不保存正文内容。

---

# Knowledge Registry

| Canonical | Tag | Alias | Status | Notes |
|------------|-----|--------|---------|-------|
| AI | AI | 人工智能；Artificial Intelligence | Active | AI 统一知识入口 |
| Agent | Agent | 智能体 | Active | Agent 统一入口 |
| 文境 | 文境 | Wenjing | Active | 文境系统 |
| 主体性 | 主体性 | Agency | Active | 主体性理论 |
| 创作 | 创作 | 创作者；Creation | Active | 创作体系 |
| Loop Engineering | LoopEngineering | 循环工程 | Active | Loop Engineering 理论 |

---

# 更新原则

Knowledge Map 的目标不是不断增加节点。

而是保持知识网络拥有统一、稳定且长期有效的核心概念。

任何新增 Canonical Node，均应经过创作者确认。

新增节点应具有长期价值。

能够成为其它知识引用对象。

不得因为一次讨论、一篇文章或一个临时项目而新增 Canonical。

Knowledge Map 应始终保持远小于整个知识库规模。

随着知识增长，Knowledge Map 应保持缓慢增长，并持续作为整个文境知识网络的统一知识地图。