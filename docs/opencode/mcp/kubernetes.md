<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - kubernetes -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `kubernetes`

- Type: local
- How it runs: `bunx -y mcp-server-kubernetes`
- What it does: MCP tools to interact with Kubernetes clusters (pods, services, deployments).
- Requirements:
  - Bun runtime.
  - Kubernetes cluster access (kubeconfig).
  - Environment variable `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS` set to `true`.
- Notes:
  - Currently disabled in configuration.