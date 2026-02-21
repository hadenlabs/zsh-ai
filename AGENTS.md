# AGENTS.md - Contexto del Proyecto para Agentes de IA

> **Proyecto:** zsh-ai - Plugin de Zsh para gestión de herramientas de IA  
> **Automatización:** Taskfile | **Shell:** zsh/ksh | **Soporte:** macOS, Linux

---

## Descripción

Plugin de Zsh modular para instalar y gestionar herramientas de IA. Implementa un patrón factory con carga condicional por OS.

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

**Patrón:** Cada módulo usa `main.zsh` como factory que carga `base.zsh` + archivo específico del OS (`osx.zsh` | `linux.zsh`).

---

## API Principal

| Función                      | Descripción                   |
| ---------------------------- | ----------------------------- |
| `ai::install`                | Instala todos los paquetes AI |
| `ai::opencode::install`      | Instalar opencode CLI         |
| `ai::fabric::install`        | Instalar fabric CLI           |
| `ai::fabric::patterns::sync` | Sincronizar patterns locales  |
| `ai::fabric::patterns::pull` | Actualizar patterns oficiales |
| `ai::upgrade`                | Actualizar (no implementado)  |

Ver referencia completa: [docs/functions.md](docs/functions.md)

---

## Variables de Configuración

| Variable                         | Descripción                                |
| -------------------------------- | ------------------------------------------ |
| `AI_TOOLS`                       | Lista de herramientas: `(opencode fabric)` |
| `AI_PACKAGES`                    | Paquetes a instalar                        |
| `AI_OPENCODE_ROOT_PATH`          | `~/.opencode`                              |
| `AI_OPENCODE_BIN_PATH`           | `~/.opencode/bin`                          |
| `AI_FABRIC_PATTERNS_PATH`        | `~/.config/fabric/patterns`                |
| `AI_FABRIC_PATTERNS_SYNC_SOURCE` | `patterns/` local                          |
| `AI_INSTALL_URL_OPENCODE`        | URL de instalación opencode                |
| `AI_INSTALL_URL_FABRIC`          | URL de instalación fabric                  |
| `AI_APPLICATION_PATH`            | `/Applications` (macOS)                    |
| `AI_ARCHITECTURE_NAME`           | `darwin-arm64` / `linux-amd64`             |

---

## Convenciones

- Funciones públicas: `ai::accion`
- Funciones internas: `ai::internal::accion`
- Variables: `AI_VARIABLE_NAME`
- Archivos: `lowercase.zsh`

---

## Desarrollo

```bash
task --yes && task setup && task environment  # Setup inicial
task --list                                   # Ver comandos
source zsh-ai.zsh && ai::install              # Testing
```

Ver guía completa: [docs/usage.md](docs/usage.md)

---

## Agregar Nueva Herramienta

1. Agregar a `AI_TOOLS` en `config/base.zsh`
2. Crear `ai::internal::tool::install` en `internal/helper.zsh`
3. Agregar case en `internal/base.zsh`
4. Crear función pública en `pkg/helper.zsh`
5. Documentar en `docs/functions.md`

---

## Patterns (Fabric)

La carpeta `patterns/` contiene custom patterns para fabric.

**Estructura:**

```
patterns/
├── README.md
└── pattern_name/
    ├── system.md    # Requerido
    └── user.md      # Opcional
```

**Sincronizar:**

```bash
ai::fabric::patterns::sync  # Local → ~/.config/fabric/patterns
```

---

## Documentación

| Archivo                                            | Propósito               |
| -------------------------------------------------- | ----------------------- |
| [docs/functions.md](docs/functions.md)             | Referencia de funciones |
| [docs/usage.md](docs/usage.md)                     | Guía de uso             |
| [docs/contributing.md](docs/contributing.md)       | Guía de contribución    |
| [docs/testing.md](docs/testing.md)                 | Guía de testing         |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Solución de problemas   |
| [patterns/README.md](patterns/README.md)           | Guía de patterns        |

---

## Dependencias Externas

El plugin requiere funciones externas (definidas en otros plugins):

```zsh
message_info, message_success, message_warning, message_error
core::install, core::exists
```

---

_Última actualización: 2026-02-20_
