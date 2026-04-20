---
name: hadx-opencode-sync
description: Wrapper para ejecutar skills de sincronización (plugins y MCPs)
---

# hadx-opencode-sync

Execute synchronization skills for OpenCode configuration.

## Usage

Run one or more sync skills. If no arguments provided, runs both skills:

- `sync-plugins` - Synchronize plugins from opencode.json to docs/opencode/plugins/
- `sync-mcps` - Synchronize MCP servers from opencode.json to docs/opencode/mcp/

## Execution

Run the specified skill(s) with all provided arguments: {{args}}

- If no arguments provided, execute both `sync-plugins` and `sync-mcps` in sequence
- Do not interpret arguments
- Do not transform arguments
- Forward them directly to the skill
- Execute autonomously
- Return only the final result

## Examples

```
/hadx-opencode-sync              # Runs both sync-plugins and sync-mcps
/hadx-opencode-sync sync-plugins # Runs only sync-plugins
/hadx-opencode-sync sync-mcps   # Runs only sync-mcps
/hadx-opencode-sync sync-plugins sync-mcps  # Runs both (explicit)
```

## Skills

- **sync-plugins**: Synchronize and generate documentation for OpenCode plugins from opencode.json configuration
- **sync-mcps**: Synchronize and generate documentation for OpenCode MCP servers from opencode.json configuration