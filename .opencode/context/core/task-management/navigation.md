# Task Management

This repo includes a minimal task-management CLI used by agent prompts:

- `.opencode/skills/task-management/router.sh`

Schema notes:

- Subtasks live under `.tmp/tasks/{feature}/subtask_XX.json`
- Fields supported by the CLI:
  - `title` (string)
  - `status` (pending|in_progress|completed)
  - `depends_on` (array of seq strings like "01")
  - `parallel` (boolean)

See: `standards/enhanced-task-schema.md`
