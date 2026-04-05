<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - grafana -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `grafana`

- Type: local
- How it runs: `uvx mcp-grafana`
- What it does: integrates MCP tools to query/administer Grafana (dashboards, datasources, alerts, etc. depending on server support).
- Requirements:
  - `uvx` (UV) + Python.
  - Environment variables:
    - `GRAFANA_URL`
    - `GRAFANA_SERVICE_ACCOUNT_TOKEN`
- Notes:
  - The token should belong to a Service Account with the minimum required permissions.