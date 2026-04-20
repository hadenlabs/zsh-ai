## Why

Currently, plugin configuration in `opencode.json` is not synchronized with the project documentation in `docs/opencode/plugins`. This creates visibility issues and potential inconsistencies between the actual configuration and what is documented. This change enables automatic documentation sync to maintain alignment between executable configuration and system documentation.

## What Changes

- Create new command `hadx-opencode-sync` for plugin documentation synchronization
- Read plugin section from `opencode.json`
- Generate or update plugin documentation in `docs/opencode/plugins`
- Define standard Markdown documentation format
- Support preview of changes before applying (--dry-run mode)
- Show diff of changes
- Detect plugin changes and update documentation automatically
- Prevent overwriting manual changes without control

## Capabilities

### New Capabilities

- `plugin-sync-command`: New CLI command `hadx-opencode-sync` that reads plugins from `opencode.json` and generates documentation in `docs/opencode/plugins`
- `plugin-documentation-format`: Standard Markdown format for plugin documentation
- `dry-run-preview`: Ability to preview changes before applying with `--dry-run` flag
- `diff-display`: Show diff of changes before applying
- `manual-change-protection`: Detect and protect manual changes from being overwritten

### Modified Capabilities

- None - this is a new capability

## Impact

- New command: `hadx-opencode-sync` in the project
- New directory: `docs/opencode/plugins` for generated documentation
- Configuration file: `opencode.json` (read-only access)
- No external dependencies required