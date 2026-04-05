<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: OpenCode Slash Commands -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

## Overview

OpenCode slash commands for this repository live in `/.opencode/commands/`.

Each command is a Markdown file that documents an expected workflow. These commands typically:

- run local CLI commands (`git`, `gh`, `task`),
- load and apply an OpenCode “skill” (implemented in this repo under `/.claude/skills/`),
- print a ready-to-paste output (for example, a `gh pr create` command).

## Commands

### `/prepare-pr`

Source: `.opencode/commands/prepare-pr.md`

What it does:

1. Inspects changes since `main`:
   - `git diff main...HEAD --stat`
   - `git log main...HEAD --oneline`
2. Loads skill: `git-release` (`.claude/skills/git-release/SKILL.md`).
3. Generates a PR description (summary, testing notes, migration steps if any, screenshots placeholders).
4. Outputs a `gh pr create` command ready to paste.

Requirements:

- `git`
- `gh` (GitHub CLI) for creating the PR

### `/update-pr`

Source: `.opencode/commands/update-pr.md`

What it does:

1. Runs validation: `task validate`.
2. Refreshes change context since `main`:
   - `git diff main...HEAD --stat`
   - `git log main...HEAD --oneline`
3. Pushes current branch:
   - `git push -u origin HEAD` if no upstream, else `git push`.
4. Detects the PR for the current branch (prefers `gh pr view`, falls back to `gh pr list --head ...`).
5. Loads skill: `update-pr` (`.claude/skills/update-pr/SKILL.md`).
6. Regenerates the PR body using `.github/PULL_REQUEST_TEMPLATE.md` as the base (proposed changes, testing, migration, screenshots, checkboxes).
7. Updates the PR body (prefers `gh api`, falls back to `gh pr edit`).

Requirements:

- `task`
- `git`
- `gh`

### `/validate-pr [PR]`

Source: `.opencode/commands/validate-pr.md`

Arguments:

- `$1` (optional): PR number or PR URL.

What it does:

1. Loads skill: `validate-pr` (`.claude/skills/validate-pr/SKILL.md`).
2. If `$1` is provided, validates that PR.
3. If `$1` is not provided, lists PRs assigned to `@me` and asks which to validate.

Requirements:

- `gh`

### `/release (major|minor|patch)`

Source: `.opencode/commands/release.md`

Arguments:

- `$1`: one of `major`, `minor`, `patch`.

What it does:

1. Loads skill: `release` (`.claude/skills/release/SKILL.md`).
2. Validates `$1` and asks the user if it is missing/invalid.
3. Runs `task release:$1`.
4. Confirms the new version and shows the generated changelog entry (if produced).

Requirements:

- `task`

### `/goji-commit-smart`

Source: `.opencode/commands/goji-commit-smart.md`

What it does:

1. Loads skill: `goji-commit-smart` (`.claude/skills/goji-commit-smart/SKILL.md`).
2. Runs `task validate`.
3. Groups local changes into 1..N commits.
4. Derives issue key/id from the current branch name (rules in `infobot.toml`).
5. Creates commits using goji conventions and sign-off.

Requirements:

- `task`
- `git`
- `goji` (commit tool configured in `infobot.toml`)

### `/task-template [feature]`

Source: `.opencode/commands/task-template.md`

Arguments:

- `$1` (optional): feature name (kebab-case)

What it does:

1. Creates `.infobot/.tmp/tasks/<feature>/`.
2. Generates a starter `task.json` and `subtask_01.json`.
3. Prints next commands to list and progress tasks.

Requirements:

- `python3`

### `/task-start [feature]`

Source: `.opencode/commands/task-start.md`

Arguments:

- `$1` (optional): feature name (kebab-case)

What it does:

1. Shows task status for the feature.
2. Finds the next ready `pending` subtask.
3. Marks it as `in_progress` in the subtask JSON.
4. Begins execution (delegates to the suggested agent).

Requirements:

- `python3`