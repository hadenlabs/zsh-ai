# AGENTS.md - AI Agent Project Context

> **Project:** zsh-ai - Zsh plugin for managing AI tools  
> **Automation:** Taskfile | **Shell:** zsh/ksh | **Support:** macOS, Linux

---

## Description

Modular Zsh plugin for installing and managing AI tools. Implements a factory pattern with OS-specific conditional loading.

---

## Arquitectura

```
zsh-ai.zsh (entry point)
    ├── config/     → Variables y configuración global
    ├── core/       → Funciones core (extensión futura)
    ├── internal/   → Lógica interna de instalación
    ├── pkg/        → API pública expuesta al usuario
    └── patterns/   → Custom patterns para fabric
```

**Pattern:** Each module uses `main.zsh` as a factory that loads `base.zsh` + OS-specific file (`osx.zsh` | `linux.zsh`).

**Shebang:** All `.zsh` files must start with `#!/usr/bin/env ksh`

---

## Main API

| Function                      | Description                   |
| ----------------------------- | ----------------------------- |
| `ai::install`                 | Install all AI packages       |
| `ai::opencode::install`       | Install opencode CLI          |
| `ai::fabric::install`         | Install fabric CLI            |
| `ai::fabric::patterns::sync`  | Sync local patterns           |
| `ai::fabric::patterns::pull`  | Update official patterns      |
| `ai::ollama::install`         | Install ollama CLI            |
| `ai::ollama::models::list`    | List installed models         |
| `ai::ollama::models::pull`    | Download specific model       |
| `ai::ollama::models::install` | Install default models        |
| `ai::shimmy::install`         | Install shimmy CLI            |
| `ai::hf::install`             | Install hf CLI (Hugging Face) |
| `ai::upgrade`                 | Upgrade (not implemented)     |

See complete reference: [docs/functions.md](docs/functions.md)

---

## Configuration Variables

## Configuration Variables

For a complete list of all environment variables and their descriptions, see [docs/env-vars.md](docs/env-vars.md).

Key variables include:

- `AI_TOOLS` - List of supported tools: `(opencode fabric ollama shimmy hf)`
- `AI_PACKAGES` - Packages to install
- `AI_*_PATH` variables - Installation paths for each tool
- `AI_INSTALL_URL_*` variables - Download URLs for each tool

---

## Conventions

- Public functions: `ai::action`
- Internal functions: `ai::internal::action`
- Variables: `AI_VARIABLE_NAME`
- Files: `lowercase.zsh`

---

## Development Setup

Para guías completas de desarrollo, consulta:

- [docs/contributing.md](docs/contributing.md) - Guía de contribución y flujo de trabajo
- [docs/usage.md](docs/usage.md) - Guía de uso y comandos disponibles

---

## Adding a New Tool

For detailed development guidelines, code conventions, and contribution workflow, see [docs/contributing.md](docs/contributing.md).

### Quick Steps to Add a New Tool:

1. **Update configuration** - Add tool to `AI_TOOLS` and `AI_PACKAGES` in `config/base.zsh`
2. **Define configuration variables** - Add tool-specific variables in `config/base.zsh`
3. **Implement internal function** - Create `ai::internal::toolname::install` in `internal/base.zsh`
4. **Add to package dispatcher** - Update `ai::internal::packages::install` case statement
5. **Create public function** - Add `ai::toolname::install` in `pkg/helper.zsh`
6. **Document the function** - Add entry in `docs/functions.md`
7. **Test** - Run `source zsh-ai.zsh && ai::toolname::install`

### Example for OpenClaw:

```zsh
# In config/base.zsh
AI_TOOLS=(opencode fabric ollama shimmy hf openclaw)
AI_OPENCLAW_BIN_PATH="${HOME}/.local/bin"
AI_INSTALL_URL_OPENCLAW="https://github.com/openclaw-ai/openclaw/releases/latest/download/openclaw"

# In internal/base.zsh
function ai::internal::openclaw::install {
    message_info "Installing openclaw..."
    # Download binary implementation
}

# In pkg/helper.zsh
function ai::openclaw::install {
    ai::internal::packages::install "openclaw"
}
```

Para convenciones de desarrollo, estilo de commits, y guías de contribución, consulta:

- [docs/contributing.md](docs/contributing.md) - Convenciones de Git, estilo de código y proceso de contribución

### Convenciones Específicas del Plugin

**Shebang y Shell:**

- Todos los archivos `.zsh` deben comenzar con `#!/usr/bin/env ksh`
- Usar `ksh` como intérprete para compatibilidad entre shells
- Mantener compatibilidad con `zsh` para funciones específicas del plugin

**Estructura de Archivos:**

```zsh
#!/usr/bin/env ksh
# Descripción del archivo

function ai::example::function {
    # code here
}
```

**Manejo de Errores:**

- Usar `return 1` para errores
- Usar `message_error` para mostrar mensajes de error
- Validar precondiciones al inicio de funciones

**Variables y Funciones:**

- Variables globales: `AI_*` (en mayúsculas)
- Funciones públicas: `ai::*`
- Funciones internas: `ai::internal::*`
- Funciones locales: `_ai_*` (con guión bajo)

---

## Agregar Nueva Herramienta

### Pasos para implementar una nueva herramienta (ejemplo: openclaw)

1. **Actualizar configuración base** - Agregar a `AI_TOOLS` en `config/base.zsh`:

   ```zsh
   #!/usr/bin/env ksh
   AI_TOOLS=(
       opencode
       fabric
       ollama
       shimmy
       hf
   )
   ```

2. **Definir variables de configuración** - Agregar en `config/base.zsh`:

   ```zsh
   # OpenClaw configuration
   AI_OPENCLAW_BIN_PATH="${HOME}/.local/bin"
   AI_INSTALL_URL_OPENCLAW="https://github.com/openclaw-ai/openclaw/releases/latest/download/openclaw"
   ```

3. **Implementar función interna** - Agregar en `internal/base.zsh`:

   ```zsh
   #!/usr/bin/env ksh

   function ai::internal::openclaw::install {
       message_info "Installing openclaw..."

       if ! core::exists curl; then
           message_error "curl is required to install openclaw"
           return 1
       fi

       local install_path="${AI_OPENCLAW_BIN_PATH}/openclaw"

       # Download openclaw binary
       if ! curl -L "${AI_INSTALL_URL_OPENCLAW}" -o "${install_path}"; then
           message_error "Failed to download openclaw"
           return 1
       fi

       # Make executable
       if ! chmod +x "${install_path}"; then
           message_error "Failed to make openclaw executable"
           return 1
       fi

       message_success "openclaw installed successfully at ${install_path}"
   }
   ```

4. **Integrar en función principal** - Actualizar `ai::internal::packages::install` en `internal/base.zsh`:

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
           *)
               message_error "Unknown package: ${package}"
               return 1
               ;;
       esac
   }
   ```

5. **Crear función pública** - Agregar en `pkg/helper.zsh`:

   ```zsh
   #!/usr/bin/env ksh

   function ai::openclaw::install {
       ai::internal::packages::install "openclaw"
   }
   ```

6. **Documentar la función** - Agregar en `docs/functions.md`:

   ````markdown
   ### ai::openclaw::install

   Instala openclaw CLI descargando el binario desde GitHub Releases.

   **Ejemplo:**

   ```zsh
   ai::openclaw::install
   ```
   ````

### Verificación

```bash
# Probar la instalación
source zsh-ai.zsh
ai::openclaw::install
```

---

## Patterns (Fabric)

The `patterns/` folder contains custom patterns for fabric.

**Structure:**

```
patterns/
├── README.md
└── pattern_name/
    ├── system.md    # Requerido
    └── user.md      # Opcional
```

**Sync:**

```bash
ai::fabric::patterns::sync  # Local → ~/.config/fabric/patterns
```

---

## Documentation

| File                                               | Purpose               |
| -------------------------------------------------- | --------------------- |
| [docs/functions.md](docs/functions.md)             | Function reference    |
| [docs/usage.md](docs/usage.md)                     | Usage guide           |
| [docs/contributing.md](docs/contributing.md)       | Contribution guide    |
| [docs/testing.md](docs/testing.md)                 | Testing guide         |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Troubleshooting guide |
| [patterns/README.md](patterns/README.md)           | Patterns guide        |

---

## External Dependencies

The plugin requires external functions (defined in other plugins):

```zsh
message_info, message_success, message_warning, message_error
core::install, core::exists
```

---

## Implemented Tools

### Currently supported:

1. **opencode** - CLI for code generation
2. **fabric** - AI patterns framework
3. **ollama** - Local LLM model execution
4. **shimmy** - Interface for AI models
5. **hf** (Hugging Face) - CLI for Hugging Face models

### To be implemented:

7. _(New tool here)_

---

_Last updated: 2026-02-27_
