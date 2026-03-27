# internal/

## Responsibility

The `internal/` directory serves as the core implementation layer for the zsh-ai plugin. It encapsulates all installation logic, runtime loading mechanisms, and platform-specific handling for AI tooling. This directory is responsible for detecting, installing, and configuring AI tools including opencode, fabric, ollama, shimmy, hf (Hugging Face CLI), openclaw, and tmuxai. The internal layer acts as a bridge between the public API exposed to users and the actual system-level operations required to manage these tools.

The directory implements a factory pattern with OS-specific conditional loading, allowing the plugin to adapt to different operating systems while maintaining a unified internal interface. All functions within this directory follow the naming convention `ai::internal::<module>::<action>` to clearly distinguish internal implementations from public-facing functions in the `pkg/` layer.

## Design

### Factory Pattern

The `main.zsh` file implements a factory pattern through the `ai::internal::main::factory` function. This function orchestrates the loading of internal modules based on the detected operating system. The factory function sources `base.zsh` first (which contains all platform-agnostic installation logic), then conditionally sources either `osx.zsh` or `linux.zsh` based on the `${OSTYPE}` environment variable, and finally sources `helper.zsh` for additional utility functions. This pattern enables the plugin to maintain a single codebase while supporting multiple platforms with platform-specific optimizations when needed.

### Dispatcher Pattern

The `ai::internal::packages::install` function in `base.zsh` implements a dispatcher pattern that routes installation requests to the appropriate tool-specific installation function. The dispatcher iterates through the `${AI_PACKAGES[@]}` array and uses a case statement to match package names to their corresponding installation functions. This pattern allows for easy extensibility when adding new tools—developers simply add a new case to the dispatcher and implement the corresponding installation function.

### Lazy Loading Pattern

The internal module implements lazy loading for certain tools through `ai::internal::opencode::load` and `ai::internal::shimmy::load` functions. These functions are called during plugin initialization to add tool binaries to the PATH only if they exist on the system. This approach avoids unnecessary PATH modifications and ensures that the shell environment remains clean until tools are actually available.

### Pre-check Pattern

All installation functions follow a consistent pre-check pattern: they first verify whether the tool is already installed using `core::exists <toolname>`, and if found, they return early with status code 0. This prevents redundant installation attempts and improves plugin performance during repeated source operations.

## Flow

### Initialization Flow

When the zsh-ai plugin is sourced, the initialization flow begins in `main.zsh` where `ai::internal::main::factory` is invoked. The factory function sources the modules in a specific order: first `base.zsh` for core installation logic, then the OS-specific module based on `${OSTYPE}` (darwin* for macOS, linux* for Linux), and finally `helper.zsh` for pattern and model management functions. After sourcing completes, the factory calls `ai::internal::opencode::load` and `ai::internal::shimmy::load` to register available tools in the PATH.

### Installation Flow for Single Tool

The installation flow for a single tool follows a predictable sequence. When a user invokes a public function like `ai::opencode::install`, it delegates to the internal function `ai::internal::opencode::install`. This function first performs a pre-check using `core::exists opencode` to determine if the tool is already installed. If the tool exists, the function returns immediately with status 0. If not, the function displays an informational message, attempts installation via curl from the configured `${AI_INSTALL_URL_OPENCODE}`, and reports success or failure through message functions. The installation typically involves downloading an installation script and executing it with bash or sh depending on the tool's requirements.

### Package Batch Installation Flow

The `ai::internal::packages::install` function provides batch installation capabilities. It receives a list of package names from the `${AI_PACKAGES[@]}` array and iterates through each one. For each package, the dispatcher pattern matches the package name to a specific installation function. If no match is found in the case statement, the function falls back to `core::install "${package}"` for generic installation. After processing all packages, the function displays a success message. This flow enables users to install multiple AI tools in a single command by configuring the `AI_PACKAGES` environment variable.

### Configuration Sync Flow

For tools that require configuration files, the internal layer provides synchronization functions. The `ai::internal::opencode::sync` function demonstrates this pattern: it verifies that rsync is available, displays the source and destination paths, and uses rsync to copy configuration files from the plugin's data directory to the user's configuration directory. The `ai::internal::opencode::ensure_config` function implements a more sophisticated check that verifies both the main config file and a nested runtime config file exist before performing synchronization, preventing unnecessary rsync operations.

### Pattern Management Flow

The fabric patterns management flow involves two functions: `ai::internal::fabric::patterns::sync` and `ai::internal::fabric::patterns::pull`. The sync function copies patterns from the plugin's `data/patterns/` directory to the user's fabric configuration directory using rsync with the delete flag to ensure the destination matches the source exactly. The pull function leverages the fabric CLI's built-in `--updatepatterns` flag to fetch the latest official patterns from the fabric repository, providing users with both local custom patterns and official updates.

### Model Management Flow

For ollama, the internal layer provides model management functions through `helper.zsh`. The `ai::internal::ollama::models::list` function lists installed models by invoking `ollama list`. The `ai::internal::ollama::models::pull` function accepts a model name as an argument and downloads it using `ollama pull`. The `ai::internal::ollama::models::install` function iterates through the `${AI_OLLAMA_MODELS[@]}` array, which contains default models configured in the plugin, and pulls each one sequentially to set up a standard model environment.

## Integration

### Dependencies from External Plugins

The internal layer depends on external functions that must be provided by other zsh plugins or the user's shell environment. The message functions (`message_info`, `message_success`, `message_warning`, `message_error`) are used throughout the internal layer to provide user feedback during installation and configuration operations. The `core::exists` function is used to check whether system tools like rsync, curl, and bash are available before attempting operations that require them. The `core::install` function serves as a fallback in the package dispatcher for handling generic package installations that do not have dedicated internal implementation functions.

### Configuration Dependencies

The internal layer depends on configuration variables defined in the `config/` directory. These include `AI_PACKAGES` (array of packages to install), `AI_INSTALL_URL_*` variables (URLs for installing each tool), `AI_OPENCODE_BIN_PATH`, `AI_OPENCODE_CONFIG_PATH`, `AI_OPENCODE_RUNTIME_CONFIG_PATH`, `AI_SHIMMY_BIN_PATH`, `AI_FABRIC_PATTERNS_SYNC_SOURCE`, `AI_FABRIC_PATTERNS_PATH`, and `AI_OLLAMA_MODELS`. The internal functions read these variables to determine installation targets, URLs, and configuration paths.

### Integration with Public API

The internal layer is consumed by the public API layer in `pkg/`. Public functions in `pkg/helper.zsh` delegate to internal functions, providing a clean separation between the interface exposed to users and the implementation details. For example, `ai::opencode::install` calls `ai::internal::opencode::install`, and `ai::fabric::patterns::sync` calls `ai::internal::fabric::patterns::sync`. This layered architecture allows the internal implementation to evolve without affecting the public interface.

### Integration with Main Entry Point

The `zsh-ai.zsh` main entry point sources the internal module through the factory pattern in `main.zsh`. The entry point relies on the internal layer to perform all tool detection, installation, and configuration tasks. After the internal module is loaded, the entry point can expose public functions that depend on the internal implementation being in place.

### Integration with Shell Environment

The internal layer modifies the shell environment by adding tool binaries to PATH through the load functions. The `ai::internal::opencode::load` function prepends `${AI_OPENCODE_BIN_PATH}` to PATH if the directory exists, and `ai::internal::shimmy::load` performs the same operation for shimmy. This ensures that installed AI tools are immediately available in the user's shell session after the plugin loads.