# pkg/ Directory CodeMap

## Overview

The `pkg/` directory constitutes the **public API layer** of the zsh-ai plugin. It exposes all user-facing functions that allow end-users to interact with AI tooling without understanding internal implementation details. This layer follows the **Facade Pattern**, providing a simplified and consistent interface to the underlying complex subsystem located in `internal/`.

---

## Responsibility

The pkg directory serves as the **public contract** between the plugin and its users. Its primary responsibilities include:

1. **Public API Exposure**: Export all user-callable functions (ai::install, ai::opencode::install, ai::fabric::install, etc.)
2. **Shell Aliases**: Define command shortcuts for rapid access to common operations
3. **OS-Specific Dispatching**: Route OS-dependent functionality to platform-specific implementations
4. **Delegation to Internal Layer**: Forward all function calls to corresponding `ai::internal::*` implementations

---

## Design Patterns

### 1. Facade Pattern

Each public function in `helper.zsh` acts as a thin wrapper that delegates to an internal implementation. This shields users from internal complexity while maintaining flexibility.

**Example:**
```zsh
function ai::opencode::install {
    ai::internal::opencode::install
}
```

### 2. Factory Pattern (main.zsh)

The `ai::pkg::main::factory` function implements a factory that conditionally loads platform-specific modules based on `${OSTYPE}`. This follows the **Conditional Loading** pattern.

**Factory Logic:**
```zsh
function ai::pkg::main::factory {
    source "${ZSH_AI_PATH}"/pkg/base.zsh
    case "${OSTYPE}" in
        darwin*)
            source "${ZSH_AI_PATH}"/pkg/osx.zsh
            ;;
        linux*)
            source "${ZSH_AI_PATH}"/pkg/linux.zsh
            ;;
    esac
    source "${ZSH_AI_PATH}"/pkg/helper.zsh
    source "${ZSH_AI_PATH}"/pkg/alias.zsh
}
```

### 3. Namespace Convention

The plugin uses a hierarchical namespace convention for function naming:

| Namespace Level | Description | Example |
|-----------------|-------------|---------|
| `ai::` | Top-level public API | `ai::install` |
| `ai::<tool>::` | Tool-specific public API | `ai::opencode::install` |
| `ai::<tool>::models::` | Sub-resource API | `ai::ollama::models::list` |
| `ai::internal::` | Internal implementation (private) | `ai::internal::packages::install` |

---

## File Structure and Responsibilities

### pkg/main.zsh

**Responsibility**: Entry point and factory loader. Orchestrates the loading sequence of all pkg modules.

**Key Function**: `ai::pkg::main::factory`

**Loading Sequence**:
1. `base.zsh` - Core public functions
2. `osx.zsh` OR `linux.zsh` - Platform-specific (conditional)
3. `helper.zsh` - Tool-specific public API
4. `alias.zsh` - Shell command aliases

---

### pkg/base.zsh

**Responsibility**: Core public functions that provide fundamental plugin operations.

**Public Functions**:

| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::install` | Install all AI packages | `ai::internal::packages::install` |
| `ai::post_install` | Post-installation hook | Messages only |
| `ai::upgrade` | Upgrade installed packages | Not implemented (warning) |
| `ai::packages::install` | Alias for ai::install | `ai::internal::packages::install` |

---

### pkg/helper.zsh

**Responsibility**: Primary public API containing all tool-specific installation and management functions. This is the **most important file** for users.

**Public Functions**:

#### OpenCode Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `editopencode` | Open config file in $EDITOR | Direct (no delegation) |
| `ai::opencode::install` | Install opencode CLI | `ai::internal::opencode::install` |
| `ai::opencode::sync` | Sync opencode configuration | `ai::internal::opencode::sync` |

#### Fabric Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::fabric::install` | Install fabric CLI | `ai::internal::fabric::install` |
| `ai::fabric::patterns::sync` | Sync custom patterns locally | `ai::internal::fabric::patterns::sync` |
| `ai::fabric::patterns::pull` | Pull official patterns | `ai::internal::fabric::patterns::pull` |

#### Ollama Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::ollama::install` | Install ollama CLI | `ai::internal::ollama::install` |
| `ai::ollama::models::list` | List installed models | `ai::internal::ollama::models::list` |
| `ai::ollama::models::pull` | Pull specific model | `ai::internal::ollama::models::pull "${@}"` |
| `ai::ollama::models::install` | Install default models | `ai::internal::ollama::models::install` |

#### Shimmy Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::shimmy::install` | Install shimmy CLI | `ai::internal::shimmy::install` |

#### Hugging Face Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::hf::install` | Install Hugging Face CLI | `ai::internal::hf::install` |

#### OpenClaw Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::openclaw::install` | Install openclaw CLI | `ai::internal::openclaw::install` |

#### TmuxAI Tool
| Function | Responsibility | Delegates To |
|----------|---------------|--------------|
| `ai::tmuxai::install` | Install tmuxai CLI | `ai::internal::tmuxai::install` |

---

### pkg/osx.zsh

**Responsibility**: Platform-specific functions for macOS (darwin).

**Current Status**: Empty placeholder file reserved for future macOS-specific implementations.

---

### pkg/linux.zsh

**Responsibility**: Platform-specific functions for Linux.

**Current Status**: Empty placeholder file reserved for future Linux-specific implementations.

---

### pkg/alias.zsh

**Responsibility**: Define shell command aliases for rapid access to common operations.

**Current Status**: Empty placeholder file reserved for future alias definitions.

---

## Data & Control Flow

### Control Flow Diagram

```
User Input (zsh shell)
        |
        v
ai::install / ai::<tool>::install
        |
        v
pkg/base.zsh / pkg/helper.zsh
        |
        v
Delegation: ai::internal::<module>::<function>
        |
        v
internal/base.zsh (implementation)
        |
        v
OS-specific checks (osx.zsh / linux.zsh in internal/)
        |
        v
External commands (curl, brew, etc.)
```

### Data Flow

1. **Configuration Input**: Environment variables (`AI_TOOLS`, `AI_PACKAGES`, `AI_*_PATH`) are sourced from `config/base.zsh`
2. **Function Arguments**: Passed through to internal layer (e.g., `ai::ollama::models::pull "${@}"`)
3. **Return Values**: Standard shell return codes (`0` for success, `1` for failure)
4. **Output**: Messages via `message_info`, `message_success`, `message_warning`, `message_error`

---

## Integration Points

### Dependencies From

The pkg layer integrates with and depends upon:

| Component | File | Dependency Type |
|-----------|------|-----------------|
| Configuration | `config/base.zsh` | Reads AI_* environment variables |
| Internal Implementation | `internal/base.zsh` | Delegates all tool installations |
| Core Utilities | External plugin functions | Uses message_* functions |
| Shell | zsh/ksh | Provides public API |

### Dependencies To

The pkg layer exposes functions that are consumed by:

| Consumer | Usage |
|----------|-------|
| End Users | Direct shell invocation |
| Documentation | `docs/functions.md` reference |
| Contributing Guide | `docs/contributing.md` examples |
| Test Scripts | Validation of public API |

---

## API Summary Table

### Core Functions (base.zsh)
- `ai::install` - Install all packages
- `ai::post_install` - Post-install hook
- `ai::upgrade` - Upgrade (not implemented)
- `ai::packages::install` - Alias for install

### Tool Installation Functions (helper.zsh)

| Function | Tool | Capability |
|----------|------|------------|
| `ai::opencode::install` | OpenCode | CLI installation |
| `ai::opencode::sync` | OpenCode | Configuration sync |
| `ai::fabric::install` | Fabric | CLI installation |
| `ai::fabric::patterns::sync` | Fabric | Local pattern sync |
| `ai::fabric::patterns::pull` | Fabric | Official pattern pull |
| `ai::ollama::install` | Ollama | CLI installation |
| `ai::ollama::models::list` | Ollama | Model listing |
| `ai::ollama::models::pull` | Ollama | Model download |
| `ai::ollama::models::install` | Ollama | Default model install |
| `ai::shimmy::install` | Shimmy | CLI installation |
| `ai::hf::install` | Hugging Face | CLI installation |
| `ai::openclaw::install` | OpenClaw | CLI installation |
| `ai::tmuxai::install` | TmuxAI | CLI installation |

---

## Usage Examples

```zsh
# Install all AI tools
ai::install

# Install specific tool
ai::opencode::install
ai::fabric::install
ai::ollama::install

# Manage Ollama models
ai::ollama::models::list
ai::ollama::models::pull llama3.2
ai::ollama::models::install

# Manage Fabric patterns
ai::fabric::patterns::sync
ai::fabric::patterns::pull
```

---

## Future Considerations

The empty files (`osx.zsh`, `linux.zsh`, `alias.zsh`) are reserved for:

1. **OS-Specific Optimizations**: Platform-specific installation methods
2. **Shell Aliases**: Quick command shortcuts (e.g., `alias aii='ai::install'`)
3. **Extended Functionality**: Additional platform-dependent features

---

*Generated: 2026-03-27*