# Repository Overview

## Purpose

This repository contains infrastructure automation for `architecture/infrastructure` plus the local OpenCode agent, skill, command, and context configuration used to operate on it.

## Main Areas

- `.agents/skills/` - optional location for repo-specific OpenCode-native skill definitions when this repo ships them
- `.claude/skills/` - homologated or shared skills used by several repo workflows
- `.opencode/skills/` - internal or compatibility skill implementations used by local tooling; this repo currently keeps local task-management compatibility files and the `context-sync` skill here
- `.opencode/commands/` - reusable command prompts that load skills or orchestrate repo workflows
- `.opencode/context/` - local context files used by agents for standards and repo-specific guidance
- `provision/terraform/` - Terraform and Terragrunt infrastructure code
- `provision/ansible/` - Ansible inventories, roles, and playbooks
- `provision/templates/` - generated file templates, including the README template
- `provision/generators/` - configuration inputs for generated files, including the canonical README config
- `docs/` - project documentation rendered with MkDocs when docs content exists
- `.jira/issue_templates/` - Jira reporting templates
- `.gitlab/merge_request_templates/` - merge request body templates

## Working Model

- Infrastructure code lives under `provision/` and is operated primarily through `task` targets from `Taskfile.yml`.
- Local skills and commands automate repo workflows such as releases, Jira work logging, PR preparation, and context maintenance.
- Commands that use `Load skill:` may resolve skills from `.agents/skills/`, `.claude/skills/`, or `.opencode/skills/` depending on where the implementation lives.
- Context files under `.opencode/context/` must match the current repository layout, commands, and operational rules.
- Jira and GitLab workflows are derived from branch names and commit history through `infobot.toml`, `.goji.json`, and the command prompts in `.opencode/commands/`.
- The README is generated from `provision/generators/README.yaml` through `provision/templates/README.tpl.md` using `task readme`.
