## Context

The project `zsh-ai` uses `opencode.json` to define plugins configuration. Currently, there is no mechanism to synchronize this configuration with the documentation in `docs/opencode/plugins`. This creates a gap between what is configured and what is documented.

The solution requires a CLI command that:
1. Reads plugin configuration from `opencode.json`
2. Generates Markdown documentation for each plugin
3. Supports preview mode before applying changes
4. Protects manual changes from being overwritten

## Goals / Non-Goals

**Goals:**
- Create `hadx-opencode-sync` command that reads plugins from `opencode.json`
- Generate standardized Markdown documentation in `docs/opencode/plugins`
- Support `--dry-run` mode to preview changes
- Display diff of changes before applying
- Detect and protect manual changes from being overwritten

**Non-Goals:**
- Modify `opencode.json` structure
- Support other configuration formats (YAML, TOML)
- Implement real-time file watching
- Create a generic documentation generator for other config sections

## Decisions

### 1. CLI Framework
**Decision:** Use standard shell script with zsh functions
**Rationale:** Project is a zsh plugin, native shell implementation aligns with project architecture
**Alternative considered:** Use Go binary - would add external dependency

### 2. Documentation Format
**Decision:** One Markdown file per plugin in `docs/opencode/plugins/`
**Rationale:** Follows existing documentation pattern in project, easy to review changes
**Alternative considered:** Single aggregated file - harder to track changes per plugin

### 3. Manual Change Protection
**Decision:** Use marker comments in generated files to detect manual changes
**Rationale:** Simple to implement, doesn't require external tools
**Alternative considered:** Git diff - would require git dependency and be slower

### 4. Diff Display
**Decision:** Use `diff` command for showing changes
**Rationale:** Standard Unix tool, no additional dependencies
**Alternative considered:** Custom diff implementation - unnecessary complexity

## Risks / Trade-offs

- [Risk] Plugin names with special characters may cause file system issues → Mitigation: Sanitize filenames, use slugify function
- [Risk] Large number of plugins may slow down generation → Mitigation: Process in parallel if needed
- [Risk] Documentation format may need to evolve → Mitigation: Use versioned format with clear schema