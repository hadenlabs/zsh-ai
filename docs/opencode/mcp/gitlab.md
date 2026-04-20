<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - gitlab -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `gitlab`

- Type: local
- How it runs: `bunx -y @modelcontextprotocol/server-gitlab`
- What it does: MCP tools to interact with GitLab (repos, issues, merge requests, pipelines).
- Requirements:
  - Bun runtime.
  - Environment variables: `GITLAB_PERSONAL_ACCESS_TOKEN`, `GITLAB_API_URL` (defaults to `https://gitlab.com/api/v4`).
- Notes:
  - Currently disabled in configuration.