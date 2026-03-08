<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP: TinyPNG (Pipedream) -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

# TinyPNG (Pipedream MCP)

This MCP server exposes TinyPNG image compression through Pipedream's hosted MCP gateway.

## Configuration

This repo configures the server under the MCP id `tinypng`.

Project config:

- `opencode.json`

Synced global template:

- `data/opencode/opencode.json`

The server uses a hosted (remote) MCP endpoint:

- `https://mcp.pipedream.net/v2`

## Requirements

- A Pipedream MCP account
- TinyPNG enabled in your Pipedream MCP account

## Troubleshooting

- If the server prompts for auth, complete the Pipedream MCP login/authorization flow.
- If you do not want this enabled by default, set `enabled: false` under `mcp.tinypng`.
