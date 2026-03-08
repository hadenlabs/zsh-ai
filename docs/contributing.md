<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: Contributing ZshAI -->
<!-- Label: ZshAI -->
<!-- Label: Contributing -->
<!-- Include: disclaimer.md -->
<!-- Include: ac:toc -->

# How To Contribute

Contributions to zsh-ai are welcome.

Feel free to use all of the contribution options:

- Contribute to zsh-ai repositories on [GitHub](https://github.com/hadenlabs/zsh-ai). See [GitHub flow](./contribute/github-flow.md).

## Getting Started

### Development

In general, MRs are welcome. We follow the typical "fork-and-pull" [Github flow](./contribute/github-flow.md).

1. **Fork** the repo on Github
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch using [Github Flow](./contribute/github-flow.md)
4. **Push** your work back up to your fork
5. Submit a **Pull Request** so that we can review your changes

**NOTE:** Be sure to rebase the latest changes from "upstream" before making a pull request!

## Adding New AI Tools

This guide explains how to add support for a new AI tool to the zsh-ai plugin. For a quick reference, see [AGENTS.md](../AGENTS.md) which provides a condensed version for AI agents.

### Overview

The zsh-ai plugin follows a modular architecture with clear separation between:

- **Configuration** (`config/`): Variables and OS-specific settings
- **Internal logic** (`internal/`): Installation functions
- **Public API** (`pkg/`): User-facing functions
- **Patterns** (`data/patterns/`): Custom patterns for fabric

### Step-by-Step Guide

#### 1. Update Base Configuration

Add the new tool to the `AI_TOOLS` array in `config/base.zsh`:

```zsh
#!/usr/bin/env ksh
AI_TOOLS=(
    opencode
    fabric
    ollama
    shimmy
    hf
    newtool  # Add your new tool here
)
```

#### 2. Define Configuration Variables

Add tool-specific configuration variables in `config/base.zsh`:

```zsh
# NewTool configuration
AI_NEWTOOL_BIN_PATH="${HOME}/.local/bin"
AI_INSTALL_URL_NEWTOOL="https://github.com/org/newtool/releases/latest/download/newtool"
```

#### 3. Add OS-Specific Configuration

Update OS-specific configuration files:

**For macOS** (`config/osx.zsh`):

```zsh
#!/usr/bin/env ksh
AI_INSTALL_URL_NEWTOOL="https://github.com/org/newtool/releases/latest/download/newtool-darwin-arm64.tar.gz"
```

**For Linux** (`config/linux.zsh`):

```zsh
#!/usr/bin/env ksh
AI_INSTALL_URL_NEWTOOL="https://github.com/org/newtool/releases/latest/download/newtool-linux-x64.tar.gz"
```

#### 4. Implement Internal Installation Function

Create the installation function in `internal/base.zsh`:

```zsh
#!/usr/bin/env ksh

function ai::internal::newtool::install {
    message_info "Installing newtool..."

    # Check for required dependencies
    if ! core::exists curl; then
        message_error "curl is required to install newtool"
        return 1
    fi

    local install_path="${AI_NEWTOOL_BIN_PATH}/newtool"

    # Download the binary
    if ! curl -L "${AI_INSTALL_URL_NEWTOOL}" -o "${install_path}"; then
        message_error "Failed to download newtool"
        return 1
    fi

    # Make it executable
    if ! chmod +x "${install_path}"; then
        message_error "Failed to make newtool executable"
        return 1
    fi

    message_success "newtool installed successfully at ${install_path}"
}
```

#### 5. Update Package Installation Dispatcher

Add a case for your new tool in `ai::internal::packages::install` function in `internal/base.zsh`:

```zsh
function ai::internal::packages::install {
    local package="$1"

    case "${package}" in
        opencode)
            ai::internal::opencode::install
            ;;
        fabric)
            ai::internal::fabric::install
            ;;
        ollama)
            ai::internal::ollama::install
            ;;
        shimmy)
            ai::internal::shimmy::install
            ;;
        hf)
            ai::internal::hf::install
            ;;
        newtool)
            ai::internal::newtool::install
            ;;
        *)
            message_error "Unknown package: ${package}"
            return 1
            ;;
    esac
}
```

#### 6. Create Public API Function

Add a public wrapper function in `pkg/helper.zsh`:

```zsh
#!/usr/bin/env ksh

function ai::newtool::install {
    ai::internal::packages::install "newtool"
}
```

#### 7. Update Package List

Ensure your tool is included in the `AI_PACKAGES` array (if needed) in `config/base.zsh`:

```zsh
AI_PACKAGES=(
    opencode
    fabric
    ollama
    shimmy
    hf
    newtool
)
```

#### 8. Document the Function

Add documentation in `docs/functions.md`:

````markdown
### ai::newtool::install

Installs newtool CLI by downloading the binary from GitHub Releases.

**Example:**

```zsh
ai::newtool::install
```
````

#### 9. Update Supported Tools List

Update the "Tools Implemented" section in `AGENTS.md`:

```markdown
### Currently Supported:

1. **opencode** - CLI for code generation
2. **fabric** - AI patterns framework
3. **ollama** - Local LLM execution
4. **shimmy** - Interface for AI models
5. **hf** (Hugging Face) - CLI for Hugging Face models
6. **newtool** - Description of your new tool
```

### Testing Your Implementation

1. Source the plugin:

   ```bash
   source zsh-ai.zsh
   ```

2. Test the function exists:

   ```bash
   type ai::newtool::install
   ```

3. Run the installation:

   ```bash
   ai::newtool::install
   ```

4. Verify the tool is installed:
   ```bash
   which newtool
   ```

### Code Conventions

- **Shebang**: All `.zsh` files must start with `#!/usr/bin/env ksh`
- **Function naming**:
  - Public functions: `ai::toolname::action`
  - Internal functions: `ai::internal::toolname::action`
- **Variables**: Use `AI_` prefix for global variables
- **Error handling**: Use `return 1` for errors and `message_error` for error messages
- **Language**: All code and documentation must be in English

### Common Patterns

#### Binary Installation Pattern

Most tools follow this pattern:

1. Check for `curl` dependency
2. Download binary from GitHub releases
3. Make it executable
4. Place in appropriate bin directory

#### Python Package Pattern

For tools installed via pip:

```zsh
function ai::internal::pytool::install {
    message_info "Installing pytool..."

    if ! core::exists pip3; then
        message_error "pip3 is required to install pytool"
        return 1
    fi

    if ! pip3 install pytool; then
        message_error "Failed to install pytool via pip"
        return 1
    fi

    message_success "pytool installed successfully"
}
```

### Adding Additional Functions

For tools that need more than just installation (like model management, configuration, etc.):

1. Add additional internal functions in `internal/base.zsh`:

   ```zsh
   function ai::internal::newtool::configure {
       # Configuration logic here
   }
   ```

2. Add corresponding public functions in `pkg/helper.zsh`:
   ```zsh
   function ai::newtool::configure {
       ai::internal::newtool::configure
   }
   ```

### Adding Custom Patterns (Fabric)

If your tool works with fabric patterns:

1. Create pattern directory in `data/patterns/`:

   ```
   data/patterns/
   └── newtool-pattern/
       ├── system.md
       └── user.md
   ```

2. Update pattern synchronization:
   ```bash
   ai::fabric::patterns::sync
   ```

### Troubleshooting

- **Tool not found after installation**: Ensure the installation path is in `$PATH`
- **Permission denied**: Check that `chmod +x` succeeded
- **Download fails**: Verify the URL is correct and accessible
- **Function not available**: Ensure you sourced the plugin correctly

### References

- [AGENTS.md](../AGENTS.md) - Quick reference for AI agents
- [functions.md](./functions.md) - Complete function reference
- [usage.md](./usage.md) - Usage guide
- [testing.md](./testing.md) - Testing guide

## Styleguides

### Git Commit Messages

Your commit messages should serve these 3 important purposes:

- To speed up the reviewing process.
- To provide the least amount of necessary documentation
- To help the future maintainers.

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) to make `git log`{.interpreted-text role="command"} easier to follow. We use commitlint to enforce the format (See [commitlint](https://github.com/conventional-changelog/commitlint)).

Accepted format:

```text
<type> <emoji> (<scope>): <subject>
```

Rules:

- Subject max length: 100 characters
- Use one of the allowed scopes: `core`, `accounts`, `ci`
- Sign-off is required (use `git commit -s` or ensure your commit tool adds it)
- For GitHub/GitLab issue references, append the issue at the end: `(#123)`

Types:

**feat**: introduce a new feature

**fix**: fix a bug

**docs**: documentation-only change

**refactor**: code restructure without behavior change

**style**: formatting/linting/aesthetic changes (no behavior change)

**test**: add or update tests

**chore**: maintenance tasks (versioning, deps bumps, tooling)

**ci**: CI configuration and pipelines

**build**: build scripts/config

**perf**: performance improvements

**hotfix**: critical production fix

**deprecate**: remove dead code / mark as deprecated

**package**: add/update compiled artifacts or packages

**sample**: add/update samples/examples

**prompt**: add/update prompts (PDD/Fabric)

**revert**: revert a previous change

**wip**: work in progress (avoid merging to `main`)

Examples:

- feat ✨ (core): add opencode MCP docs (#123)
- fix 🐛 (core): handle missing env var (#123)
- docs(core): update usage guide
- refactor(core): extract install helper
- style(core): format shell scripts
- test(core): add coverage for patterns sync
- ci 👷 (ci): run workflows on ubuntu-24.04 (#123)
- chore(core): bump action versions

**Keep it short and simple!**

### Branches

See [Github Flow](./contribute/github-flow.md).

### Documentation

Documentation is a part of the zsh-ai code base. You can find the documentation files in the `doc/` subdirectory of the [main repository](https://github.com/hadenlabs/zsh-ai). This means that the contribution process is the same for both the source code and documentation.

### Testing

See [Testing](./testing.md).

### Code Submission

1. See if a [Pull Request](https://github.com/hadenlabs/zsh-ai/pulls) exists
   - Add some comments or review the code to help it along
   - Don't be afraid to comment when logic needs clarification
2. Create a Fork and open a [Pull Request](https://github.com/hadenlabs/zsh-ai/pulls) if needed

### Code Review

- Anyone can review code
- Any [Pull Request](https://github.com/hadenlabs/zsh-ai/pulls) should be closed or merged within a week

### Code Acceptance

Try to keep history as linear as possible using a [rebase] merge strategy.
