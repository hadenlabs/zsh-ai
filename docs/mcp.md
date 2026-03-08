# MCP servers (OpenCode)

This document describes the MCP (Model Context Protocol) servers configured in OpenCode and what each one is used for.

## Overview

| MCP id | Type | Purpose | Enabled | Requirements |
| --- | --- | --- | :-: | --- |
| `serena` | local | Code indexing/navigation and repo-local automations (via Serena) | yes | `uvx` + Python |
| `context7` | remote | On-demand, versioned documentation (Context7) | yes | internet access |
| `sequential-thinking` | local | Step-by-step reasoning tools (sequential-thinking MCP server) | yes | `npx`/Node |
| `awslabs.aws-knowledge` | remote | AWS knowledge (knowledge MCP) | no | internet access |
| `awslabs.aws-terraform` | local | Terraform assistance (awslabs terraform-mcp-server) | no | `uvx` + Python |
| `hashicorp.terraform` | local | Terraform assistance via official HashiCorp container | yes | `docker` |
| `grafana` | local | Grafana queries and operations | yes | `uvx` + `GRAFANA_*` env vars |
| `filesystem` | local | Filesystem read/write (scoped by `ROOT`) | yes | `npx`/Node |
| `github` | local | GitHub API access (issues/PRs/repos) | yes | `npx`/Node + `GITHUB_PERSONAL_ACCESS_TOKEN` |
| `jira` | remote | Jira access via remote MCP | yes | `JIRA_MCP_URL` + OAuth (per your gateway) |

## Server details

### `serena`

- Type: local
- How it runs: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server`
- What it does: exposes MCP tools to work with the local repository (for example: understand project structure, navigate symbols/files, and perform server-assisted actions).
- Requirements:
  - `uvx` (UV) and a Python runtime.
- Notes:
  - As a local server, it inherits the permissions of the user running it.

### `context7`

- Type: remote
- URL: `https://mcp.context7.com/mcp`
- What it does: provides up-to-date, on-demand documentation for libraries/frameworks (useful for current API examples).
- Requirements: internet connectivity.

### `sequential-thinking`

- Type: local
- How it runs: `npx -y @modelcontextprotocol/server-sequential-thinking`
- What it does: provides MCP tools aimed at breaking problems down and reasoning in steps; typically used for planning/analysis before code changes.
- Requirements:
  - Node.js + `npx`.

### `awslabs.aws-knowledge` (disabled)

- Type: remote
- URL: `https://knowledge-mcp.global.api.aws`
- What it does: access to AWS knowledge/documentation via an MCP endpoint.
- Status: `enabled: false`.

### `awslabs.aws-terraform` (disabled)

- Type: local
- How it runs: `uvx awslabs.terraform-mcp-server@latest`
- What it does: Terraform-focused MCP tools (analysis/help with configurations, patterns, etc.).
- Status: `enabled: false`.
- Environment:
  - `FASTMCP_LOG_LEVEL=ERROR` (reduces log verbosity).

### `hashicorp.terraform`

- Type: local
- How it runs: `docker run -i --rm hashicorp/terraform-mcp-server:latest`
- What it does: HashiCorp's official MCP server for Terraform workflows (intended for Terraform-related queries/actions).
- Requirements:
  - Docker running locally.
- Notes:
  - Depending on integration, the container may need access to your workspace (volumes). Your current config does not mount volumes, so the server will not see local files unless the OpenCode launcher adds mounts.

### `grafana`

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

### `filesystem`

- Type: local
- How it runs: `npx -y @modelcontextprotocol/server-filesystem`
- What it does: allows OpenCode to read/write files through MCP.
- Environment:
  - `ROOT=.` limits server access to the current directory (workspace) when launched.
- Security notes:
  - Keep `ROOT` as restricted as possible.

### `github`

- Type: local
- How it runs: `npx -y @modelcontextprotocol/server-github`
- What it does: MCP tools to interact with GitHub (repos, issues, PRs, comments, etc.).
- Requirements:
  - Node.js + `npx`.
  - Environment variable `GITHUB_PERSONAL_ACCESS_TOKEN`.
- Notes:
  - Use a PAT with minimum scopes (for example, only `repo` if needed, or finer scopes if you use fine-grained tokens).

### `jira`

- Type: remote
- URL: `{env:JIRA_MCP_URL}`
- What it does: integrates Jira (issues, comments, transitions, etc.) via an MCP gateway.
- Requirements:
  - Environment variable `JIRA_MCP_URL`.
  - OAuth configuration (depends on your provider/instance; your config shows `oauth: {}` as a placeholder).

## Quick troubleshooting

- If a local MCP server does not start, verify dependencies (`uvx`/Node/Docker as applicable).
- If a remote MCP server fails, verify connectivity/network and the relevant `*_URL` variables.
- If `github`/`grafana`/`jira` fail with 401/403, review tokens and permissions.
