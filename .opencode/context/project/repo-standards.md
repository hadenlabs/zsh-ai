# Repository Standards

Repo-specific conventions for the `architecture/infrastructure` repository.

## Purpose

- This repository stores infrastructure code, supporting automation, generated documentation inputs, and local OpenCode configuration.
- Do not assume structure from other repos; verify paths and commands against the current checkout.

## Source of Truth

- `AGENTS.md`
- `Taskfile.yml`
- `opencode.json`
- `.opencode/paths.json`
- `.opencode/context/`
- `infobot.toml`
- `.goji.json`

## Rules

- Prefer `task` commands for setup, validation, formatting, and generated outputs.
- Prefer the concrete validation commands documented in `AGENTS.md` and `Taskfile.yml` over assumptions from other repositories.
- Do not edit generated `README.md` directly; update `provision/generators/README.yaml` and `provision/templates/README.tpl.md`, then regenerate it with `task readme`.
- Keep files under `docs/` written in English.
- Treat `.agents/skills/`, `.claude/skills/`, and `.opencode/skills/` as valid local skill sources in this repo.
- Prefer `.agents/skills/<skill-name>/SKILL.md` for repo-specific OpenCode-native skills, but resolve `Load skill:` references by checking `.agents/skills/`, then `.claude/skills/`, then `.opencode/skills/`.
- Keep `.opencode/commands/*.md` aligned with the skills and workflows they invoke.
- Keep `.opencode/context/project/*.md` aligned with the actual repository structure, not copied assumptions from another repo.
- Avoid editing generated or cached directories such as `.task/`, `.terraform/`, `.venv/`, `node_modules/`, `dist/`, and `build/`.
