<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: OpenCode Agents Usage -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

## Defaults in this repo

- Repo/PR workflows and slash commands in `.opencode/commands/`: use `OpenRepoManager`.
- Code changes (feature/bugfix): use `OpenCoder`.
- Documentation in `docs/`: use `OpenTechnicalWriter`.

## Delegating to a subagent

Use the subagent frontmatter `name` as `subagent_type`:

```text
task(
  subagent_type="TestEngineer",
  description="Add regression tests",
  prompt="Add tests for ...; follow project conventions."
)
```

## Notes

- `@path/to/file` attaches file contents to the conversation; it does not execute a command file.
- Slash commands are executed as `/command` (TUI) or `opencode run --command <name>` (CLI).
- `README.md` is generated from templates; update `provision/generators/README.yaml` / `provision/templates/README.tpl.md` and run `task readme`.

## Tasks

- Task files live under `.infobot/.tmp/tasks/<feature>/`.

### Generate a task template

From the OpenCode TUI:

```text
/task-template my-feature
```

From CLI:

```bash
opencode run --command task-template my-feature
```

Directly (no OpenCode):

```bash
bash .infobot/skills/task-management/router.sh init my-feature
```

This creates:

- `.infobot/.tmp/tasks/my-feature/task.json`
- `.infobot/.tmp/tasks/my-feature/subtask_01.json`

Fill those JSON files with your objective, deliverables, and acceptance criteria.

### Track progress

```bash
bash .infobot/skills/task-management/router.sh status my-feature
bash .infobot/skills/task-management/router.sh next my-feature
bash .infobot/skills/task-management/router.sh parallel my-feature
bash .infobot/skills/task-management/router.sh complete my-feature 01 "summary"
```

### Start the next task

From the OpenCode TUI:

```text
/task-start my-feature
```

From CLI:

```bash
opencode run --command task-start my-feature
```

Directly (no OpenCode):

```bash
bash .infobot/skills/task-management/router.sh execute my-feature
```

Router commands and schema reference: `docs/opencode/tasks.md`.

## Permissions & safety

- Many subagents intentionally cannot edit or run arbitrary shell commands.
- Anything that looks like secret material (`*.env*`, `*.key`, `*.secret`) is commonly denied by agent permissions.
