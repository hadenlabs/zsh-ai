<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - github -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `github`

- Type: local
- How it runs: `bunx -y @modelcontextprotocol/server-github`
- What it does: MCP tools to interact with GitHub (repos, issues, PRs, comments, etc.).
- Requirements:
  - Bun runtime.
  - Environment variable `GITHUB_PERSONAL_ACCESS_TOKEN`.
- Notes:
  - Use a PAT with minimum scopes (for example, only `repo` if needed, or finer scopes if you use fine-grained tokens).