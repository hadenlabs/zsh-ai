<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - google-calendar -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `google-calendar`

- Type: local
- How it runs: `bunx -y @cocal/google-calendar-mcp`
- What it does: MCP tools to interact with Google Calendar (events, calendars, attendees).
- Requirements:
  - Bun runtime.
  - Environment variable `GOOGLE_OAUTH_CREDENTIALS` pointing to OAuth JSON file.
- Notes:
  - Uses OAuth credentials for authentication.
  - Credential file path: `/Users/luchomayta/.local/secure/google/mcp-infosis-oauth.json`.