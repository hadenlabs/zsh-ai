# Repository Atlas: zsh-ai

## Project Responsibility

Modular Zsh plugin for installing and managing AI tools (opencode, fabric, ollama, shimmy, hf). Implements a factory pattern with OS-specific conditional loading for macOS and Linux.

## System Entry Points

| File | Purpose |
|------|---------|
| `zsh-ai.zsh` | Main entry point - sources all modules in order |
| `config/main.zsh` | Configuration factory - loads base + OS-specific config |
| `core/main.zsh` | Core utilities loader (placeholder for future) |
| `internal/main.zsh` | Internal implementation loader |
| `pkg/main.zsh` | Public API loader |

## Supported AI Tools

- **opencode** - CLI for code generation
- **fabric** - AI patterns framework
- **ollama** - Local LLM model execution
- **shimmy** - Interface for AI models
- **hf** (Hugging Face) - CLI for Hugging Face models
- **openclaw** - Additional tool (in development)
- **tmuxai** - tmux AI integration (in development)

## Directory Map (Aggregated)

| Directory | Responsibility Summary | Detailed Map |
|-----------|----------------------|--------------|
| `config/` | Centralized configuration management - defines all AI tool paths, URLs, and supported tools via exported `AI_*` environment variables | [View Map](config/codemap.md) |
| `core/` | Foundation layer - provides system utilities, platform abstraction, dependency management, and path handling (currently placeholder) | [View Map](core/codemap.md) |
| `internal/` | Core implementation layer - contains all installation logic for AI tools with dispatcher pattern | [View Map](internal/codemap.md) |
| `pkg/` | Public API layer - exposes user-facing functions with facade pattern delegating to internal implementations | [View Map](pkg/codemap.md) |

## Architecture

```
zsh-ai.zsh (entry point)
    ├── config/     → Variables y configuración global
    ├── core/       → Funciones core (extensión futura)
    ├── internal/   → Lógica interna de instalación
    ├── pkg/        → API pública expuesta al usuario
    └── data/patterns/ → Custom patterns para fabric
```

## Pattern: Factory with OS-Specific Loading

Each module uses `main.zsh` as a factory that loads:
1. `base.zsh` - Always loaded (common functionality)
2. `osx.zsh` or `linux.zsh` - Loaded conditionally based on `${OSTYPE}`

## External Dependencies

The plugin requires external functions (defined in other plugins):
- `message_info`, `message_success`, `message_warning`, `message_error`
- `core::install`, `core::exists`

## Key Configuration Variables

- `AI_TOOLS` - List of supported tools
- `AI_PACKAGES` - Packages to install
- `AI_*_PATH` variables - Installation paths for each tool
- `AI_INSTALL_URL_*` variables - Download URLs for each tool

## Flow Summary

1. User sources `zsh-ai.zsh`
2. Config factory loads configuration
3. User calls public API (e.g., `ai::ollama::install`)
4. Public function delegates to internal implementation
5. Internal function checks if tool exists, then installs via curl/download

---

_Last updated: 2026-03-27_