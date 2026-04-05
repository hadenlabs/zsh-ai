<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - serena -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `serena`

- Type: local
- How it runs: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server`
- What it does: exposes MCP tools to work with the local repository (for example: understand project structure, navigate symbols/files, and perform server-assisted actions).
- Requirements:
  - `uvx` (UV) and a Python runtime.
- Notes:
  - As a local server, it inherits the permissions of the user running it.