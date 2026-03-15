# Jira GitLab Workflow

## Purpose

Describe the main delivery workflow used in this repository when work starts in Jira and is delivered through GitLab.

## Source of Truth

- `.opencode/commands/jira-start-task.md`
- `.opencode/commands/goji-commit-smart.md`
- `.opencode/commands/jira-add-worklog.md`
- `.opencode/commands/gitlab-create-mr.md`
- `.opencode/commands/jira-work-report.md`
- `infobot.toml`
- `.goji.json`

## Main Flow

1. `jira-start-task` selects the Jira issue and creates or reuses `feature/<ISSUE-KEY>`.
2. Implementation work happens on that branch.
3. `goji-commit-smart` runs `task validate` and creates signed commits.
4. `jira-add-worklog` registers worked time using the branch-derived Jira issue and commit-based summary.
5. `gitlab-create-mr` validates the branch, pushes it, and opens or reuses the merge request.
6. After review approval, `jira-work-report` publishes the final implementation report in Jira.

## Optional Flow

- `jira-add-worklog` can be used again at the end to log additional time after review feedback or final adjustments.

## Branch And Commit Rules

- Derive the Jira issue key from the current branch according to `infobot.toml`.
- Use Goji commit format and signoff rules from `.goji.json` and `infobot.toml`.
- Do not invent Jira keys, MR URLs, or unsupported testing claims.
