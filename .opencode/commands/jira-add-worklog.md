---
description: Registra un worklog en Jira usando el issue del branch actual y una descripcion basada en commits
---

1. Load skill: jira-add-worklog
2. Detect from `infobot.toml` whether the project uses Jira and derive the current issue key from the current branch name according to the configured branch rules.
3. Read input from `{{args}}`
4. If `{{args}}` is provided, use it as the worklog duration when it is a safe Jira-compatible time format; otherwise ask the user for the duration.
5. Build the worklog description from recent commits on the current branch and add the worklog to the derived Jira issue according to the skill rules.