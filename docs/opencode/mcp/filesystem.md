<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - filesystem -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `filesystem`

- Type: local
- How it runs: `bunx -y @modelcontextprotocol/server-filesystem`
- What it does: Filesystem read/write operations (scoped by `ROOT` environment variable).
- Requirements:
  - Bun runtime.
  - Environment variable `ROOT` set to `.` (current directory).