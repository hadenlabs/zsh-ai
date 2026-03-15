# Skills Architecture

## Purpose

Describe how local skills, commands, and context are modeled and connected inside this repository.

## Source of Truth

- `.agents/skills/<skill-name>/SKILL.md` - optional preferred location for repo-specific OpenCode-native skills when this repo ships them
- `.claude/skills/<skill-name>/` - valid skill location for homologated or shared skills used by commands in this repo
- `.opencode/skills/<skill-name>/` - valid internal or compatibility skill location when a workflow is implemented there
- `.opencode/commands/*.md` - command prompts that load skills or orchestrate repeatable workflows
- `opencode.json` - active agent configuration and instruction sources
- `.opencode/context/project/*.md` - project-specific context that must stay aligned with the real repo

## Rules

- Update related command prompts and context files when a skill changes behavior.
- Use canonical skill names in docs, commands, and context files.
- When resolving `Load skill: <name>`, check `.agents/skills/`, then `.claude/skills/`, then `.opencode/skills/`.
- Prefer branch-derived issue keys and commit-derived summaries when the workflow supports them.
- Keep repo context aligned with the actual skills and commands shipped in the repository.

## Key Skills In This Repo

- `jira-start-task` - selects a Jira issue and creates or reuses `feature/<ISSUE-KEY>`
- `goji-commit-smart` - validates and creates commits using Goji conventions
- `jira-add-worklog` - registers Jira worklogs from branch and commit context
- `gitlab-create-mr` - validates, pushes, and opens a GitLab merge request
- `jira-work-report` - posts a Jira implementation report using template and commit history
- `release` - bumps the project version and generates the next changelog entry
- `context-sync` - audits local OpenCode files and `AGENTS.md` against the current repository (implemented in `.opencode/skills/context-sync/SKILL.md`)

## Skill Resolution Order

1. `.agents/skills/<skill-name>/SKILL.md`
2. `.claude/skills/<skill-name>/`
3. `.opencode/skills/<skill-name>/`

Use the first matching location that contains the requested skill implementation for this repo.
