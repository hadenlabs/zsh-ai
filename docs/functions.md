<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: Functions ZshAI -->
<!-- Label: Functions -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

## Functions

### Public Functions

#### ai::install

Install all AI packages defined in `AI_PACKAGES`.

```bash
ai::install
```

#### ai::packages::install

Install all packages defined in `AI_PACKAGES` array.

```bash
ai::packages::install
```

#### ai::post_install

Execute post-installation steps.

```bash
ai::post_install
```

#### ai::upgrade

Upgrade AI packages (not yet implemented).

```bash
ai::upgrade
```

#### ai::opencode::install

Install opencode CLI tool. Checks if opencode is already installed using `which` before attempting installation.

```bash
ai::opencode::install
```

#### ai::fabric::install

Install fabric CLI tool for AI patterns. Checks if fabric is already installed before attempting installation.

```bash
ai::fabric::install
```

#### ai::fabric::patterns::sync

Sync custom patterns from local `patterns/` directory to fabric's patterns directory (`~/.config/fabric/patterns/`). Uses rsync for synchronization.

```bash
ai::fabric::patterns::sync
```

#### ai::fabric::patterns::pull

Update fabric patterns from the official repository using `fabric --updatepatterns`.

```bash
ai::fabric::patterns::pull
```

### Internal Functions

#### ai::internal::packages::install

Internal function that iterates through `AI_PACKAGES` and installs each one with appropriate handling.

```bash
ai::internal::packages::install
```

#### ai::internal::opencode::load

Internal function that adds opencode binary path to PATH. Checks if `~/.opencode/bin` exists and prepends it to PATH.

```bash
ai::internal::opencode::load
```

#### ai::internal::opencode::install

Internal function for opencode installation logic. Verifies if opencode exists before installing via curl.

```bash
ai::internal::opencode::install
```

#### ai::internal::fabric::install

Internal function for fabric installation logic. Verifies if fabric exists before installing via curl.

```bash
ai::internal::fabric::install
```

#### ai::internal::fabric::patterns::sync

Internal function for syncing patterns using rsync.

```bash
ai::internal::fabric::patterns::sync
```

#### ai::internal::fabric::patterns::pull

Internal function for pulling patterns from fabric's official repository.

```bash
ai::internal::fabric::patterns::pull
```

### Variables

| Variable                         | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| `AI_PACKAGE_NAME`                | Name of the package (default: `ai`)                            |
| `AI_TOOLS`                       | Array of AI tools to install                                   |
| `AI_PACKAGES`                    | Array of all packages (combines `AI_TOOLS`)                    |
| `AI_MESSAGE_BREW`                | Message for brew requirement                                   |
| `AI_OPENCODE_ROOT_PATH`          | Root path for opencode (default: `~/.opencode`)                |
| `AI_OPENCODE_BIN_PATH`           | Binary path for opencode (default: `~/.opencode/bin`)          |
| `AI_FABRIC_PATTERNS_PATH`        | Path to fabric patterns (default: `~/.config/fabric/patterns`) |
| `AI_FABRIC_PATTERNS_SYNC_SOURCE` | Source path for custom patterns (`ZSH_AI_PATH/patterns`)       |
| `AI_INSTALL_URL_OPENCODE`        | Installation URL for opencode                                  |
| `AI_INSTALL_URL_FABRIC`          | Installation URL for fabric                                    |
| `AI_APPLICATION_PATH`            | Path to applications (macOS only)                              |
| `AI_ARCHITECTURE_NAME`           | Architecture name (e.g., `darwin-arm64`, `linux-amd64`)        |
