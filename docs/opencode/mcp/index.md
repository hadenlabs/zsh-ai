<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP servers (OpenCode) -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

# MCP servers (OpenCode)

This section describes the MCP (Model Context Protocol) servers configured in OpenCode and what each one is used for.

## Overview

| MCP id | Type | Purpose | Enabled | Requirements | Details |
| --- | --- | --- | :-: | --- | --- |
| `serena` | local | Code indexing/navigation and repo-local automations (via Serena) | yes | `uvx` + Python | `docs/opencode/mcp/serena.md` |
| `context7` | remote | On-demand, versioned documentation (Context7) | yes | internet access | `docs/opencode/mcp/context7.md` |
| `sequential-thinking` | local | Step-by-step reasoning tools (sequential-thinking MCP server) | yes | `npx`/Node | `docs/opencode/mcp/sequential-thinking.md` |
| `awslabs.aws-knowledge` | remote | AWS knowledge (knowledge MCP) | no | internet access | `docs/opencode/mcp/awslabs.aws-knowledge.md` |
| `awslabs.aws-terraform` | local | Terraform assistance (awslabs terraform-mcp-server) | no | `uvx` + Python | `docs/opencode/mcp/awslabs.aws-terraform.md` |
| `hashicorp.terraform` | local | Terraform assistance via official HashiCorp container | yes | `docker` | `docs/opencode/mcp/hashicorp.terraform.md` |
| `grafana` | local | Grafana queries and operations | yes | `uvx` + `GRAFANA_*` env vars | `docs/opencode/mcp/grafana.md` |
| `filesystem` | local | Filesystem read/write (scoped by `ROOT`) | yes | `npx`/Node | `docs/opencode/mcp/filesystem.md` |
| `github` | local | GitHub API access (issues/PRs/repos) | yes | `npx`/Node + `GITHUB_PERSONAL_ACCESS_TOKEN` | `docs/opencode/mcp/github.md` |
| `jira` | remote | Jira access via remote MCP | yes | `JIRA_MCP_URL` + OAuth (per your gateway) | `docs/opencode/mcp/jira.md` |

## Quick troubleshooting

- If a local MCP server does not start, verify dependencies (`uvx`/Node/Docker as applicable).
- If a remote MCP server fails, verify connectivity/network and the relevant `*_URL` variables.
- If `github`/`grafana`/`jira` fail with 401/403, review tokens and permissions.
