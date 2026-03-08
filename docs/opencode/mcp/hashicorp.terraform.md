<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: MCP - hashicorp.terraform -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# `hashicorp.terraform`

- Type: local
- How it runs: `docker run -i --rm hashicorp/terraform-mcp-server:latest`
- What it does: HashiCorp's official MCP server for Terraform workflows (intended for Terraform-related queries/actions).
- Requirements:
  - Docker running locally.
- Notes:
  - Depending on integration, the container may need access to your workspace (volumes). Your current config does not mount volumes, so the server will not see local files unless the OpenCode launcher adds mounts.
