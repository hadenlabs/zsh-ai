<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - docker -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `docker`

- Type: local
- How it runs: `bunx -y docker-mcp`
- What it does: MCP tools to interact with Docker (containers, images, volumes, networks).
- Requirements:
  - Bun runtime.
  - Docker running locally.
  - Environment variables: `DOCKER_MCP_LOCAL`, `DOCKER_MCP_HOST`, `DOCKER_MCP_USERNAME`, `DOCKER_MCP_PRIVATE_KEY`, `DOCKER_MCP_PORT`, `DOCKER_MCP_PASSPHRASE`.
- Notes:
  - Currently disabled in configuration.