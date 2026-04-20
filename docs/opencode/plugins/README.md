# Opencode Plugins

This directory documents the plugins configured in `opencode.json`.

## Installed Plugins

### Authentication

- **`opencode-gemini-auth@latest`**: OAuth authentication for using Gemini models through your Google account.
- **`opencode-openai-codex-auth@latest`**: Lets you use a ChatGPT Plus/Pro account as the backend for OpenAI models.
- **`opencode-antigravity-auth@latest`**: Optional plugin that unifies access to multiple model providers such as Claude and Gemini, and also adds search capabilities.

### Productivity and Context

- **`opencode-dynamic-context-pruning@latest`**: Optimizes token usage by automatically pruning context and keeping only the most relevant information.
- **`opencode-websearch-cited@latest`**: Enables web search for the agent and adds citations for consulted sources, making responses more reliable and verifiable.
- **`opencode-type-inject@latest`**: Useful for TypeScript and Svelte projects. It injects type definitions into the context to improve generated code accuracy.
- **`tokenscope-opencode-plugin@latest`**: Provides visibility into token usage and cost, which helps with cost management.
- **`opencode-ignore@latest`**: Works similarly to `.gitignore`, allowing noisy files and directories to be excluded from the project context.

### Environment and Development

- **`opencode-devcontainers@latest`**: Improves integration with VS Code Dev Containers for a more consistent development environment.
- **`opencode-direnv@latest`**: Automatically loads environment variables managed with `direnv`.
- **`oh-my-opencode@latest`**: Starter package that includes a set of preconfigured agents and tools to speed up setup.

### Notifier

- **`@mohak34/opencode-notifier@latest`**: Plugin de OpenCode para notificaciones.

### Wakelock

- **`opencode-wakelock@latest`**: Plugin para mantener activo el sistema.

### Architecture

- **`@architecture/infosis-opencode-slim@1.2.1`**: Plugin de arquitectura Infosis para OpenCode.

## Documentación Individual

- [opencode-gemini-auth](./opencode-gemini-auth.md)
- [mohak34-opencode-notifier](./mohak34-opencode-notifier.md)
- [opencode-wakelock](./opencode-wakelock.md)
- [opencode-antigravity-auth](./opencode-antigravity-auth.md)
- [infosis-opencode-slim](./infosis-opencode-slim.md)