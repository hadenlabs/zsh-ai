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

### Internal Functions

#### ai::internal::packages::install

Internal function that iterates through `AI_PACKAGES` and installs each one with appropriate handling.

```bash
ai::internal::packages::install
```

#### ai::internal::opencode::install

Internal function for opencode installation logic. Verifies if opencode exists before installing via curl.

```bash
ai::internal::opencode::install
```

### Variables

| Variable               | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `AI_PACKAGE_NAME`      | Name of the package (default: `ai`)                     |
| `AI_TOOLS`             | Array of AI tools to install                            |
| `AI_PACKAGES`          | Array of all packages (combines `AI_TOOLS`)             |
| `AI_MESSAGE_BREW`      | Message for brew requirement                            |
| `AI_APPLICATION_PATH`  | Path to applications (macOS only)                       |
| `AI_ARCHITECTURE_NAME` | Architecture name (e.g., `darwin-arm64`, `linux-amd64`) |
