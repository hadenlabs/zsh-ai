<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: EnvVars ZshAI -->
<!-- Label: ZshAI -->
<!-- Label: Project -->
<!-- Label: EnvVars -->
<!-- Include: disclaimer.md -->
<!-- Include: ac:toc -->

# Environment Variables

This document describes all environment variables used by the zsh-ai plugin.

## Overview

The zsh-ai plugin uses environment variables to configure AI tool installations and behavior. These variables are defined in the configuration files (`config/base.zsh`, `config/osx.zsh`, `config/linux.zsh`) and can be overridden by users if needed.

## Core Configuration Variables

### Tool List Variables

| Variable      | Description                              | Default Value                                 |
| ------------- | ---------------------------------------- | --------------------------------------------- |
| `AI_TOOLS`    | List of supported AI tools               | `(opencode fabric ollama shimmy hf openclaw)` |
| `AI_PACKAGES` | Packages to install (subset of AI_TOOLS) | `(opencode fabric ollama shimmy hf openclaw)` |

### Tool-Specific Path Variables

| Variable                         | Description                         | Default Value               |
| -------------------------------- | ----------------------------------- | --------------------------- |
| `AI_OPENCODE_ROOT_PATH`          | Root directory for opencode         | `~/.opencode`               |
| `AI_OPENCODE_BIN_PATH`           | Binary path for opencode            | `~/.opencode/bin`           |
| `AI_FABRIC_PATTERNS_PATH`        | Directory for fabric patterns       | `~/.config/fabric/patterns` |
| `AI_FABRIC_PATTERNS_SYNC_SOURCE` | Local patterns source directory     | `patterns/`                 |
| `AI_OLLAMA_MODELS_PATH`          | Directory for ollama models         | `~/.ollama/models`          |
| `AI_SHIMMY_BIN_PATH`             | Binary path for shimmy              | `~/.local/bin`              |
| `AI_OPENCLAW_BIN_PATH`           | Binary path for openclaw            | `~/.local/bin`              |
| `AI_APPLICATION_PATH`            | Applications directory (macOS only) | `/Applications`             |

### Tool-Specific URL Variables

| Variable                  | Description                               | Default Value |
| ------------------------- | ----------------------------------------- | ------------- |
| `AI_INSTALL_URL_OPENCODE` | opencode installation URL                 | OS-specific   |
| `AI_INSTALL_URL_FABRIC`   | fabric installation URL                   | OS-specific   |
| `AI_INSTALL_URL_OLLAMA`   | ollama installation URL                   | OS-specific   |
| `AI_INSTALL_URL_SHIMMY`   | shimmy installation URL (GitHub releases) | OS-specific   |
| `AI_INSTALL_URL_HF`       | hf CLI installation URL                   | OS-specific   |
| `AI_INSTALL_URL_OPENCLAW` | openclaw installation URL                 | OS-specific   |

### Model Configuration Variables

| Variable           | Description                      | Default Value                      |
| ------------------ | -------------------------------- | ---------------------------------- |
| `AI_OLLAMA_MODELS` | Default ollama models to install | `(llama3.2:latest mistral:latest)` |

### System Configuration Variables

| Variable               | Description                    | Default Value                                   |
| ---------------------- | ------------------------------ | ----------------------------------------------- |
| `AI_ARCHITECTURE_NAME` | System architecture identifier | `darwin-arm64` (macOS) or `linux-amd64` (Linux) |

## OS-Specific Defaults

### macOS (`config/osx.zsh`)

```zsh
AI_INSTALL_URL_OPENCODE="https://github.com/opencodeco/opencode/releases/latest/download/opencode-darwin-arm64.tar.gz"
AI_INSTALL_URL_FABRIC="https://github.com/danielmiessler/fabric/releases/latest/download/fabric-macos-arm64"
AI_INSTALL_URL_OLLAMA="https://ollama.com/download/Ollama-darwin.zip"
AI_INSTALL_URL_SHIMMY="https://github.com/shimmy-dev/shimmy/releases/latest/download/shimmy-darwin-arm64"
AI_INSTALL_URL_HF="https://huggingface.co/huggingface/llama.cpp/resolve/main/gguf/llama-2-7b-chat.Q4_K_M.gguf"
AI_INSTALL_URL_OPENCLAW="https://github.com/openclaw-ai/openclaw/releases/latest/download/openclaw-darwin-arm64.tar.gz"
AI_ARCHITECTURE_NAME="darwin-arm64"
```

### Linux (`config/linux.zsh`)

```zsh
AI_INSTALL_URL_OPENCODE="https://github.com/opencodeco/opencode/releases/latest/download/opencode-linux-x64.tar.gz"
AI_INSTALL_URL_FABRIC="https://github.com/danielmiessler/fabric/releases/latest/download/fabric-linux-amd64"
AI_INSTALL_URL_OLLAMA="https://ollama.com/download/Ollama-linux-amd64"
AI_INSTALL_URL_SHIMMY="https://github.com/shimmy-dev/shimmy/releases/latest/download/shimmy-linux-amd64"
AI_INSTALL_URL_HF="https://huggingface.co/huggingface/llama.cpp/resolve/main/gguf/llama-2-7b-chat.Q4_K_M.gguf"
AI_INSTALL_URL_OPENCLAW="https://github.com/openclaw-ai/openclaw/releases/latest/download/openclaw-linux-x64.tar.gz"
AI_ARCHITECTURE_NAME="linux-amd64"
```

## Usage Examples

### Overriding Default Values

You can override any of these variables before sourcing the plugin:

```zsh
# Customize installation paths
export AI_OLLAMA_MODELS_PATH="${HOME}/my-models"
export AI_FABRIC_PATTERNS_PATH="${HOME}/.config/my-fabric-patterns"

# Customize default models
export AI_OLLAMA_MODELS="(llama3.2:latest codellama:latest)"

# Source the plugin
source /path/to/zsh-ai.zsh
```

### Adding Custom Tools

To add support for a new tool, you need to define the appropriate variables:

```zsh
# Add to AI_TOOLS list
export AI_TOOLS=(${AI_TOOLS} my-new-tool)

# Define installation URL and path
export AI_MY_NEW_TOOL_BIN_PATH="${HOME}/.local/bin"
export AI_INSTALL_URL_MY_NEW_TOOL="https://example.com/my-new-tool.tar.gz"
```

## Variable Naming Convention

All environment variables follow this pattern:

- Prefix: `AI_`
- Tool name in uppercase: `OPENCODE`, `FABRIC`, `OLLAMA`, etc.
- Suffix describing purpose: `_PATH`, `_URL`, `_MODELS`

Examples:

- `AI_OPENCODE_BIN_PATH`
- `AI_INSTALL_URL_FABRIC`
- `AI_OLLAMA_MODELS`

## Related Documentation

- [Functions Reference](functions.md) - Complete API reference
- [Usage Guide](usage.md) - How to use the plugin
- [Contributing Guide](contributing.md) - How to add new tools
