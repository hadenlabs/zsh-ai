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
| `google-calendar` | local | Google Calendar access | yes | `bunx` + OAuth credentials | `docs/opencode/mcp/google-calendar.md` |
| `awslabs.aws-knowledge` | remote | AWS knowledge base queries | no | internet access | `docs/opencode/mcp/awslabs.aws-knowledge.md` |
| `awslabs.aws-terraform` | local | Terraform assistance (AWS Labs) | no | `uvx` + Python | `docs/opencode/mcp/awslabs.aws-terraform.md` |
| `chrome-devtools` | local | Chrome DevTools automation | no | `npx` + Chrome | `docs/opencode/mcp/chrome-devtools.md` |
| `memglobal` | local | Persistent knowledge graph | yes | `npx` + file path | `docs/opencode/mcp/memglobal.md` |
| `tmux` | local | Tmux session management | yes | `npx` + tmux | `docs/opencode/mcp/tmux.md` |
| `markitdown` | local | Document conversion to Markdown | no | `uvx` + Python | `docs/opencode/mcp/markitdown.md` |
| `context7` | local | On-demand documentation lookup | yes | `npx` + `CONTEXT7_API_KEY` | `docs/opencode/mcp/context7.md` |
| `docker` | local | Docker container management | no | `bunx` + Docker | `docs/opencode/mcp/docker.md` |
| `engram` | local | Knowledge management | yes | Engram binary | `docs/opencode/mcp/engram.md` |
| `filesystem` | local | Filesystem read/write | yes | `bunx` + `ROOT` env | `docs/opencode/mcp/filesystem.md` |
| `github` | local | GitHub API access | yes | `bunx` + `GITHUB_PERSONAL_ACCESS_TOKEN` | `docs/opencode/mcp/github.md` |
| `gitlab` | local | GitLab API access | no | `bunx` + `GITLAB_PERSONAL_ACCESS_TOKEN` | `docs/opencode/mcp/gitlab.md` |
| `grep` | remote | Code search | yes | internet access | `docs/opencode/mcp/grep.md` |
| `hashicorp.terraform` | local | Terraform assistance (HashiCorp) | yes | `docker` | `docs/opencode/mcp/hashicorp.terraform.md` |
| `image-compression` | local | Image compression | yes | `bunx` | `docs/opencode/mcp/image-compression.md` |
| `infosis` | remote | Custom InfoSys operations | yes | internet access | `docs/opencode/mcp/infosis.md` |
| `atlassian` | local | Atlassian/Jira access | yes | `bunx` + `JIRA_*` env vars | `docs/opencode/mcp/atlassian.md` |
| `jira` | remote | Jira access via MCP gateway | yes | `JIRA_MCP_URL` + OAuth | `docs/opencode/mcp/jira.md` |
| `kubernetes` | local | Kubernetes cluster management | no | `bunx` + kubeconfig | `docs/opencode/mcp/kubernetes.md` |
| `notebooklm` | local | Google NotebookLM access | yes | `npx` | `docs/opencode/mcp/notebooklm.md` |
| `notion` | local | Notion workspace access | no | `bunx` + `NOTION_TOKEN` | `docs/opencode/mcp/notion.md` |
| `obsidian` | local | Obsidian vault access | yes | `uvx` + `OBSIDIAN_API_KEY` | `docs/opencode/mcp/obsidian.md` |
| `playwright` | local | Browser automation | yes | `npx` + Playwright | `docs/opencode/mcp/playwright.md` |
| `sentry` | local | Sentry error tracking | no | `uvx` + `SENTRY_AUTH_TOKEN` | `docs/opencode/mcp/sentry.md` |
| `sequential-thinking` | local | Step-by-step reasoning tools | yes | `bunx` | `docs/opencode/mcp/sequential-thinking.md` |
| `serena` | local | Code indexing/navigation | no | `uvx` + Python | `docs/opencode/mcp/serena.md` |
| `supabase` | local | Supabase database access | no | `bunx` + `SUPABASE_*` env vars | `docs/opencode/mcp/supabase.md` |

## Quick troubleshooting

- If a local MCP server does not start, verify dependencies (`uvx`/Node/Docker/Bun as applicable).
- If a remote MCP server fails, verify connectivity/network and the relevant `*_URL` variables.
- If `github`/`atlassian`/`jira` fail with 401/403, review tokens and permissions.
- For OAuth-based MCPs (google-calendar), ensure credential files are valid and not expired.