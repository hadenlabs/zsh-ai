# Task Management Skill (Infobot)

This directory provides the task-management router used by Infobot.

Commands:

- `bash .infobot/skills/task-management/router.sh init <feature>`
- `bash .infobot/skills/task-management/router.sh status <feature>`
- `bash .infobot/skills/task-management/router.sh start <feature> <seq> [agent_id]`
- `bash .infobot/skills/task-management/router.sh next <feature>`
- `bash .infobot/skills/task-management/router.sh parallel <feature>`
- `bash .infobot/skills/task-management/router.sh complete <feature> <seq> "summary"`

Task files live under:

- `.infobot/.tmp/tasks/{feature}/subtask_XX.json`
