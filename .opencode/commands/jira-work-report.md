---
description: Genera un reporte de implementacion en Jira usando el issue del branch actual y un resumen basado en commits
agent: OpenRepoManager
---

1. Load skill: jira-work-report
2. Detect from `infobot.toml` whether the project uses Jira and derive the current issue key from the current branch name according to the configured branch rules.
3. If `$1` is provided, use it only as a safe optional hint for the report content when it can be applied without inventing unsupported facts; otherwise continue with the normal skill flow.
4. Read `.jira/issue_templates/jira-work-report.md`, build the implementation report from recent commits on the current branch according to the skill rules, and post it as a comment on the derived Jira issue.
