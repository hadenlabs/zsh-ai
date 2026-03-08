<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - jira -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `jira`

- Type: remote
- URL: `{env:JIRA_MCP_URL}`
- What it does: integrates Jira (issues, comments, transitions, etc.) via an MCP gateway.
- Requirements:
  - Environment variable `JIRA_MCP_URL`.
  - OAuth configuration (depends on your provider/instance; your config shows `oauth: {}` as a placeholder).
