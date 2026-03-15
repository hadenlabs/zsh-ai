---
description: Lista las tareas pendientes en Jira y crea un feature branch para la seleccionada
agent: OpenRepoManager
---

1. Load skill: jira-start-task
2. If `$1` is provided, use it as a hint to select the issue when it can be resolved safely; otherwise ask the user to choose from the pending assigned issues in the configured project.
3. Create or reuse the branch using the format `feature/<ISSUE-KEY>` according to the skill rules.
