---
description: Start working on the next ready subtask for a feature (marks it in_progress)
agent: OpenCoder
---

1. Read the feature name from `$1`.
2. If `$1` is missing:
   - List available features by enumerating directories under `.infobot/.tmp/tasks/` (one directory per feature).
   - If no features exist, ask the user for the feature name (recommend `kebab-case`, e.g. `readme-refresh`).
   - Otherwise, show a numbered list (`1..N`) and ask the user to select one to start.
3. Show current status:
   - Run `bash .infobot/skills/task-management/router.sh status <feature>`
4. Determine the next ready subtask:
   - Run `bash .infobot/skills/task-management/router.sh next <feature>`
5. Mark that subtask as started:
   - Run `bash .infobot/skills/task-management/router.sh start <feature> <seq> opencode`
6. Read `.infobot/.tmp/tasks/<feature>/subtask_<seq>.json` and begin implementation (delegate to the `suggested_agent` if present).
