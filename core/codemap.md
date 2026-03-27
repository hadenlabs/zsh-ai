# core/

## Responsibility

The `core/` directory serves as the foundational layer for the zsh-ai plugin. It provides core utility functions, system-level operations, and cross-platform abstractions that other modules (config, internal, pkg) depend upon.

**Primary responsibilities:**

1. **Low-level system utilities** - Functions that interact with the operating system, file system, and shell environment
2. **Platform abstraction** - OS-specific logic for macOS (darwin) and Linux
3. **Dependency management** - Detection and installation of external tools
4. **Path management** - Handling of binary paths, configuration directories, and installation locations
5. **Extensibility** - Providing a foundation for future core functionality

Currently, the core files contain only shebangs, indicating they are placeholder files awaiting implementation. The module follows the established factory pattern for future extensibility.

## Design

### Factory Pattern

Each module in the plugin uses a factory pattern for OS-specific loading. The core module follows this convention:

```
core/
├── main.zsh    # Factory function: ai::core::main::factory
├── base.zsh   # Base/common functions (platform-agnostic)
├── osx.zsh    # macOS-specific functions (OSTYPE=darwin*)
└── linux.zsh  # Linux-specific functions (OSTYPE=linux*)
```

**Factory Implementation** (`core/main.zsh`):

```zsh
function ai::core::main::factory {
    source "${ZSH_AI_PATH}"/core/base.zsh
    case "${OSTYPE}" in
    darwin*)
        source "${ZSH_AI_PATH}"/core/osx.zsh
        ;;
    linux*)
        source "${ZSH_AI_PATH}"/core/linux.zsh
      ;;
    esac
}
```

### Module Naming Conventions

| Component | Pattern | Example |
|-----------|---------|---------|
| Factory function | `ai::<module>::main::factory` | `ai::core::main::factory` |
| Base file | `base.zsh` | Core base functions |
| OS-specific | `<os>.zsh` | `osx.zsh`, `linux.zsh` |

### Load Order

The plugin loads modules in a specific sequence defined in `zsh-ai.zsh`:

1. **config/main.zsh** - Configuration variables and settings
2. **core/main.zsh** - Core utilities (current module)
3. **internal/main.zsh** - Internal installation logic
4. **pkg/main.zsh** - Public API and helpers

This order ensures that core utilities are available before internal functions that depend on them.

## Flow

### Entry Point Flow

```
zsh-ai.zsh (entry point)
    │
    ├── Sets ZSH_AI_PATH="${0}" (plugin directory)
    │
    ├── source config/main.zsh
    │       └── Loads AI_* configuration variables
    │
    ├── source core/main.zsh
    │       └── Loads core utilities (currently empty)
    │
    ├── source internal/main.zsh
    │       └── Loads ai::internal::* installation functions
    │
    └── source pkg/main.zsh
            └── Loads public API: ai::install, ai::opencode::install, etc.
```

### Environment Variables

The core module depends on and interacts with the following variables:

| Variable | Source | Purpose |
|----------|--------|---------|
| `ZSH_AI_PATH` | `zsh-ai.zsh` | Plugin root directory |
| `OSTYPE` | Shell builtin | Platform detection (darwin*/linux*) |
| `ARCH_NAME` | `config/base.zsh` | Architecture (x86_64, arm64, etc.) |
| `HOME` | Shell builtin | User home directory |
| `PATH` | Shell builtin | Executable search path |

### External Dependencies

The core module relies on external functions provided by other zsh plugins:

| Function | Source Plugin | Purpose |
|----------|---------------|---------|
| `core::exists` | External (spinnern/zsh-core) | Check if command exists |
| `core::install` | External | Install a package |
| `message_info` | External (chr-fra/chr-zsh-lib) | Display info message |
| `message_success` | External | Display success message |
| `message_warning` | External | Display warning message |
| `message_error` | External | Display error message |

### Future Function Categories

Based on the plugin architecture, the core module would typically contain:

1. **System Utilities**
   - Path validation and creation
   - Command existence checking
   - Process management

2. **Package Management**
   - Package installer abstractions
   - Version detection
   - Dependency resolution

3. **Configuration Management**
   - Config file validation
   - Default configuration handling

4. **Logging/Debugging**
   - Debug output functions
   - Verbose mode handling

## Integration

### Upstream Dependencies

The core module depends on:

| Dependency | Type | Description |
|------------|------|-------------|
| `config/main.zsh` | Module | Must load before core for `ZSH_AI_PATH` |
| External plugins | Functions | `core::*`, `message_*` functions |
| Shell builtin | Runtime | `uname`, `OSTYPE`, `HOME`, `PATH` |

### Downstream Consumers

The following modules depend on core utilities:

| Module | Usage |
|--------|-------|
| `internal/base.zsh` | Uses `core::exists` for tool detection |
| `internal/base.zsh` | Uses `message_*` for user feedback |
| `pkg/` | Public functions may call internal functions |

### File Structure Integration

```
zsh-ai/
├── zsh-ai.zsh              # Entry point (sets ZSH_AI_PATH)
├── config/
│   ├── main.zsh           # Loads first
│   ├── base.zsh           # AI_* variables
│   ├── osx.zsh
│   └── linux.zsh
├── core/                   # This module
│   ├── main.zsh           # Factory (currently empty)
│   ├── base.zsh           # (empty)
│   ├── osx.zsh            # (empty)
│   └── linux.zsh          # (empty)
├── internal/
│   ├── main.zsh           # Installation logic
│   └── base.zsh           # ai::internal::* functions
└── pkg/
    ├── main.zsh           # Public API factory
    └── helper.zsh         # ai::* public functions
```

## Current State

The core files are currently placeholder implementations:

| File | Status | Contents |
|------|--------|----------|
| `core/main.zsh` | Active | Factory function (19 lines) |
| `core/base.zsh` | Empty | Shebang only (2 lines) |
| `core/osx.zsh` | Empty | Shebang only (2 lines) |
| `core/linux.zsh` | Empty | Shebang only (2 lines) |

The factory function in `core/main.zsh` is invoked but loads empty files, indicating the core module is prepared for future implementation but currently defers functionality to external plugins.

## Extending the Core Module

To add core functionality:

1. **Add to `core/base.zsh`** for platform-agnostic functions:
   ```zsh
   function ai::core::utility::example {
       # Implementation
   }
   ```

2. **Add to `core/osx.zsh`** for macOS-specific functions:
   ```zsh
   function ai::core::osx::specific {
       # macOS-specific implementation
   }
   ```

3. **Add to `core/linux.zsh`** for Linux-specific functions:
   ```zsh
   function ai::core::linux::specific {
       # Linux-specific implementation
   }
   ```

Functions should follow the naming convention: `ai::core::<category>::<action>`

## Related Documentation

- [AGENTS.md](../AGENTS.md) - Project architecture overview
- [docs/contributing.md](../docs/contributing.md) - Development guidelines
- [docs/functions.md](../docs/functions.md) - Function reference