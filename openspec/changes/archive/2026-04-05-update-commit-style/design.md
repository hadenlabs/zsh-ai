## Context

The project uses jasper.toml to define commit message conventions, but these are not currently enforced. The configuration specifies:
- Tool: goji
- Format: `<type> <emoji> (<scope>): <subject>`
- Style: GitHub
- Signoff: enabled
- Subject max length: 100 characters

Currently, developers write commits manually without enforcing this style, leading to inconsistent commit messages.

## Goals / Non-Goals

**Goals:**
- Configure goji to read and enforce jasper.toml commit settings
- Enable goji CLI for creating properly formatted commits
- Ensure signoff is automatically added to commits

**Non-Goals:**
- Not modifying jasper.toml configuration (already correct)
- Not implementing git hooks at this stage
- Not creating custom commit validation beyond goji defaults

## Decisions

1. **Use goji as commit tool**: The jasper.toml already specifies `tool = "goji"`, so we'll configure goji to use this configuration.
2. **Install and configure goji**: Use goji CLI with jasper.toml integration to create properly formatted commits.
3. **No custom validation**: Rely on goji's built-in validation rather than adding custom scripts.

**Alternative considered**: Manual commit validation via git hooks - rejected because it adds complexity without additional benefit since goji already validates.

## Risks / Trade-offs

- **Risk**: Developers may not use goji CLI
  - **Mitigation**: Document usage and consider adding git aliases or hooks in future

- **Risk**: goji may not read jasper.toml automatically
  - **Mitigation**: Create explicit goji configuration or use `--config` flag if needed