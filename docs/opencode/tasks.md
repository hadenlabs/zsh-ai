<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: OpenCode Tasks -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

## Overview

This repository uses a simple task file convention under `.tmp/tasks/` to support agent-driven work (TaskManager -> CoderAgent) and lightweight parallel tracking.

The task files are regular JSON. They are intended to be:

- small,
- verifiable,
- easy to mark complete.

## Directory layout

- Feature folder: `.tmp/tasks/<feature>/`
- Subtasks: `.tmp/tasks/<feature>/subtask_XX.json`

## Subtask schema (minimal)

The local router expects the following fields.

```json
{
  "seq": "01",
  "title": "Implement X",
  "status": "pending",
  "parallel": true,
  "depends_on": ["00"],
  "deliverables": ["path/to/file"],
  "acceptance_criteria": ["Behavior works"]
}
```

Notes:

- `seq`: string like `"01"`.
- `status`: `pending` | `in_progress` | `completed`.
- `depends_on`: list of `seq` values that must be `completed` first.
- `parallel`: if `true`, `parallel` command will list it when it is ready.

## Router commands

This repo ships a small router used by several agent prompts.

Location:

- `.opencode/skills/task-management/router.sh`

Commands:

```bash
bash .opencode/skills/task-management/router.sh status <feature>
bash .opencode/skills/task-management/router.sh next <feature>
bash .opencode/skills/task-management/router.sh parallel <feature>
bash .opencode/skills/task-management/router.sh complete <feature> <seq> "summary"
```

## How agents use tasks

Typical flow:

1. A primary agent (usually `OpenCoder` or `OpenRepoManager`) asks `TaskManager` to break work into subtasks.
2. `CoderAgent` implements one subtask at a time.
3. On completion, `CoderAgent` marks the subtask complete using the router (`complete`).

## Practical example

Create the files:

- `.tmp/tasks/readme-refresh/subtask_01.json`
- `.tmp/tasks/readme-refresh/subtask_02.json`

Then:

```bash
bash .opencode/skills/task-management/router.sh status readme-refresh
bash .opencode/skills/task-management/router.sh next readme-refresh
```
