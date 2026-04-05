<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - filesystem -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `filesystem`

- Type: local
- How it runs: `npx -y @modelcontextprotocol/server-filesystem`
- What it does: allows OpenCode to read/write files through MCP.
- Environment:
  - `ROOT=.` limits server access to the current directory (workspace) when launched.
- Security notes:
  - Keep `ROOT` as restricted as possible.