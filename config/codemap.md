# Configuration Directory (`config/`)

## Responsibility

The `config/` directory is responsible for centralized **configuration management** for the zsh-ai plugin. It provides:

- **Global environment variables** (AI_*) that define installation paths, download URLs, supported tools, and default models
- **Platform-aware configuration** that adapts paths and URLs based on the operating system (macOS vs Linux)
- **Architecture detection** using `uname -m` to determine system architecture for binary downloads

All configuration variables use the `AI_` prefix and are exported to make them available to all functions throughout the plugin.

## Design Patterns

### Factory Pattern with OS-Specific Loading

The configuration system implements a **factory pattern** through the `ai::config::main::factory` function in `main.zsh`:

```
ai::config::main::factory
    ├── sources config/base.zsh  (always loaded)
    ├── checks ${OSTYPE} variable
    └── conditionally sources:
        ├── config/osx.zsh   (if darwin*)
        └── config/linux.zsh (if linux*)
```

This pattern ensures:
1. **Base configuration** is always loaded first (common paths, URLs, tool lists)
2. **OS-specific overrides** are applied conditionally
3. **Extensibility** - new OS variants can be added by creating new files and updating the case statement

### Layered Configuration

| Layer | File | Purpose |
|-------|------|---------|
| Base | `base.zsh` | Common defaults for all platforms |
| OS-Specific | `osx.zsh` / `linux.zsh` | Platform-specific overrides |

## Data & Control Flow

### Loading Sequence

```
1. Entry Point: zsh-ai.zsh
       │
       ▼
2. Sources: config/main.zsh
       │
       ▼
3. Calls: ai::config::main::factory
       │
       ├──▶ sources config/base.zsh
       │         │
       │         ├── Sets ARCH_NAME=$(uname -m)
       │         ├── Defines AI_TOOLS array
       │         ├── Defines AI_PACKAGES array
       │         ├── Exports AI_*_PATH variables
       │         └── Exports AI_INSTALL_URL_* variables
       │
       └──▶ evaluates OSTYPE case statement
                 │
                 ├──▶ if darwin*: sources config/osx.zsh
                 │         │
                 │         ├── Overrides AI_APPLICATION_PATH
                 │         ├── Sets AI_ARCHITECTURE_NAME=macos-${ARCH_NAME}
                 │         └── Overrides AI_INSTALL_URL_SHIMMY
                 │
                 └──▶ if linux*: sources config/linux.zsh
                           │
                           ├── Sets AI_ARCHITECTURE_NAME=linux-${ARCH_NAME}
                           └── Overrides AI_INSTALL_URL_SHIMMY
```

### Key Variables Exposed

#### From `base.zsh` (Always Loaded)

| Variable | Purpose |
|----------|---------|
| `ARCH_NAME` | System architecture (arm64, x86_64, etc.) |
| `AI_TOOLS` | Array of supported tool names |
| `AI_PACKAGES` | Array of packages to install |
| `AI_OPENCODE_ROOT_PATH` | opencode installation root |
| `AI_OPENCODE_BIN_PATH` | opencode binary directory |
| `AI_OPENCODE_CONFIG_PATH` | opencode config directory |
| `AI_FABRIC_PATTERNS_PATH` | fabric patterns directory |
| `AI_OLLAMA_MODELS_PATH` | ollama models directory |
| `AI_SHIMMY_BIN_PATH` | shimmy binary directory |
| `AI_INSTALL_URL_OPENCODE` | opencode installer URL |
| `AI_INSTALL_URL_FABRIC` | fabric installer URL |
| `AI_INSTALL_URL_OLLAMA` | ollama installer URL |
| `AI_INSTALL_URL_SHIMMY` | shimmy download URL (overridden per OS) |
| `AI_INSTALL_URL_HF` | HuggingFace CLI installer URL |
| `AI_OLLAMA_MODELS` | Default models to install |

#### From `osx.zsh` (macOS Only)

| Variable | Purpose |
|----------|---------|
| `AI_APPLICATION_PATH` | /Applications |
| `AI_ARCHITECTURE_NAME` | macos-${ARCH_NAME} |

#### From `linux.zsh` (Linux Only)

| Variable | Purpose |
|----------|---------|
| `AI_ARCHITECTURE_NAME` | linux-${ARCH_NAME} |

## Integration

### Upstream Dependencies

The configuration system **depends on**:

| Dependency | Source | Purpose |
|------------|--------|---------|
| `ZSH_AI_PATH` | Set by main entry point (zsh-ai.zsh) | Base path for locating config and data directories |
| `OSTYPE` | Shell builtin | Determines which OS-specific config to load |
| `uname -m` | System command | Determines system architecture |

### Downstream Consumers

The following modules **consume configuration variables**:

| Module | File | Variables Used |
|--------|------|----------------|
| Internal Installation | `internal/base.zsh` | `AI_INSTALL_URL_*`, `AI_TOOLS`, `AI_PACKAGES` |
| opencode | `pkg/helper.zsh` | `AI_OPENCODE_*_PATH`, `AI_INSTALL_URL_OPENCODE` |
| fabric | `pkg/helper.zsh` | `AI_FABRIC_PATTERNS_PATH`, `AI_FABRIC_PATTERNS_SYNC_SOURCE` |
| ollama | `pkg/helper.zsh` | `AI_OLLAMA_MODELS_PATH`, `AI_OLLAMA_MODELS` |
| shimmy | `pkg/helper.zsh` | `AI_SHIMMY_BIN_PATH`, `AI_INSTALL_URL_SHIMMY` |
| hf | `pkg/helper.zsh` | `AI_INSTALL_URL_HF` |

### Public API Exposure

Configuration variables are accessed indirectly through public functions:

- `ai::install` - Uses `AI_PACKAGES` to iterate and install tools
- `ai::opencode::install` - Uses `AI_OPENCODE_*_PATH` variables
- `ai::fabric::install` / `ai::fabric::patterns::sync` - Uses `AI_FABRIC_PATTERNS_*` variables
- `ai::ollama::install` / `ai::ollama::models::install` - Uses `AI_OLLAMA_*` variables
- `ai::shimmy::install` - Uses `AI_SHIMMY_BIN_PATH`, `AI_INSTALL_URL_SHIMMY`
- `ai::hf::install` - Uses `AI_INSTALL_URL_HF`

## File Structure Summary

```
config/
├── base.zsh      # Base configuration - always loaded
├── main.zsh      # Factory loader - entry point for config
├── osx.zsh       # macOS-specific overrides
└── linux.zsh     # Linux-specific overrides
```

## Extension Points

### Adding a New Tool

1. Add tool name to `AI_TOOLS` array in `base.zsh`
2. Add `AI_<TOOL>_BIN_PATH` or relevant path variables
3. Add `AI_INSTALL_URL_<TOOL>` for download URL
4. If OS-specific URLs needed, add overrides in `osx.zsh` and `linux.zsh`

### Adding a New OS Variant

1. Create `config/<os>.zsh` with OS-specific variables
2. Add new case in `ai::config::main::factory` in `main.zsh`
3. Source the OS file conditionally based on `${OSTYPE}`

## Error Handling

The configuration system has minimal error handling:

- No validation of `ZSH_AI_PATH` - assumes it's set before sourcing
- No fallback for unknown OSTYPE values - OS-specific config is simply not sourced
- No validation of URLs or paths - assumed to be valid

This design prioritizes simplicity over robustness, appropriate for a shell plugin configuration system.