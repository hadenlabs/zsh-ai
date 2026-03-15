# Documentation Rules

## Purpose

Capture the documentation and generated-content rules that are specific to this repository.

## Source of Truth

- `AGENTS.md`
- `mkdocs.yml`
- `docs/index.md`
- `provision/templates/README.tpl.md`
- `provision/generators/README.yaml`

## Rules

- Write files under `docs/` in English.
- Keep documentation concise, scannable, and accurate.
- Do not edit `README.md` directly; regenerate it from the template and generator config.
- Keep command documentation under `.opencode/commands/` aligned with the workflows they describe.
- Keep context documentation under `.opencode/context/` aligned with the real repository layout and toolchain.

## Generated README

- Config: `provision/generators/README.yaml`
- Template: `provision/templates/README.tpl.md`
- Regeneration command: `task readme`

## README Rules

- Treat `provision/generators/README.yaml` as the canonical README content configuration.
- Treat `provision/templates/README.tpl.md` as the rendering template for that config.
- Update the generator config first when changing README sections, screenshots, workflows, links, or descriptive content.
- Update the template only when the README structure itself must change.
- After changing either file, rebuild `README.md` with `task readme`.

## Workflow Docs

- Use canonical skill and command names in workflow docs.
- If workflow pages or diagrams are introduced in this repo, add them deliberately and keep their paths accurate in context files.
