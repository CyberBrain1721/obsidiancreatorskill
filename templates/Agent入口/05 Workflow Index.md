# Workflow Index

## Purpose

Workflow Index 是 Creator Runtime 的工作流索引。

它定义 Agent 在共创过程中可以调用的内部 Workflow，以及每个 Workflow 的触发条件和所需文档。

Workflow Index 不负责实现 Workflow。

也不保存任何知识内容。

它仅负责告诉 Agent：

**什么时候进入哪个 Workflow，以及进入该 Workflow 前必须读取哪些文档。**

---

# Runtime Principle

进入 Creator Mode 后。

Agent 默认进入 Conversation Runtime。

Conversation Runtime 是整个共创过程的默认运行状态。

Agent 不应主动进入任何 Workflow。

Workflow 仅在创作者提出对应任务时，由 Runtime 自动触发。

Workflow 执行结束后。

Agent 应立即退出 Workflow，并返回 Conversation Runtime，继续当前共创。

---

# Capture Workflow

## Trigger

当创作者提出以下任务时，应进入 Capture Workflow。

- 收录
- 保存
- 记录下来
- 加入 Inbox
- Capture
- 保存到藏阁

---

## Required Documents

进入 Capture Workflow 前，应依次读取：

1. Capture Convention
2. Knowledge Map Convention
3. Knowledge Map
4. Inbox Standard

Capture Convention 用于建立本次 Capture Pipeline。

Knowledge Map Convention 用于规范知识匹配流程。

Knowledge Map 用于查询 Canonical Node，并建立统一的 Tags 与 Related。

---

## Workflow Principle

Capture Workflow 的目标不是保存正文。

Capture Workflow 的目标是将外部资源建立为文境中的可引用 Resource。

任何 Capture Workflow 都必须首先完成 Resource Registration。

随后，由创作者选择本次 Resource Policy。

例如：

- Bookmark（仅资源索引）
- Snapshot（摘要）
- Full Content（正文）
- Archive（正文 + 图片 + 附件）

Resource Policy 仅决定 Payload 的保存范围。

不得影响 Resource Registration。

---

## Exit

完成 Capture Workflow 后。

Agent 应立即退出当前 Workflow。

恢复：

Conversation Runtime。

Current Workflow：

None。

---

# Organization Workflow

## Trigger

当创作者提出以下任务时，应进入 Organization Workflow。

- 整理
- 分类
- 重构
- 优化结构
- 调整知识

---

## Required Documents

进入 Organization Workflow 前，应依次读取：

1. Knowledge Organization Convention（未来）
2. Knowledge Map

---

## Exit

完成整理后。

立即返回 Conversation Runtime。

---

# Archive Workflow

## Trigger

当创作者提出以下任务时，应进入 Archive Workflow。

- 归档
- Archive
- 收卷
- 完成项目

---

## Required Documents

进入 Archive Workflow 前，应读取：

1. Archive Convention（未来）

---

## Exit

完成归档后。

立即返回 Conversation Runtime。

---

# Reflection Workflow

## Trigger

当创作者提出以下任务时，应进入 Reflection Workflow。

- 反思
- 总结
- Review
- 回顾

---

## Required Documents

进入 Reflection Workflow 前，应读取：

1. Reflection Convention（未来）

---

## Exit

完成反思后。

立即返回 Conversation Runtime。

---

# Runtime Rule

Workflow 不属于 Creator Entry。

Workflow 不属于工作模式。

Workflow 属于 Creator Runtime。

Agent 应持续监听创作者任务。

仅在 Trigger 出现时加载对应 Workflow。

除当前 Workflow 所要求的文档外。

Agent 不得主动读取其他 Workflow 的 Convention。

不得主动遍历整个 Vault。

所有 Workflow 应遵循 Lazy Loading 原则。

仅按需读取。

按需执行。

执行结束立即释放当前 Workflow，并返回 Conversation Runtime。