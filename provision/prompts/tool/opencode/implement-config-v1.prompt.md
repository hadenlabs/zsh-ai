# Prompt: Implementar configuracion y sync para opencode (sin instalar)

## Contexto

Estas trabajando dentro de este repositorio. Debes seguir estrictamente todas las reglas definidas en AGENTS.md.

No asumas convenciones fuera de ese archivo. No introduzcas cambios que rompan compatibilidad.

---

## Objetivo

Implementar soporte de configuracion para la herramienta: opencode

IMPORTANTE:

- NO debes implementar instalacion de opencode.
- NO debes modificar el comportamiento de `ai::install` ni `ai::internal::opencode::install`.
- Solo debes crear configuracion y un comando de sync.

---

## Reglas Obligatorias (AGENTS.md)

Debes respetar estrictamente:

- Todos los archivos `.zsh` deben iniciar con: `#!/usr/bin/env ksh`
- Variables globales en mayusculas con prefijo `AI_`
- Funciones publicas: `ai::*`
- Funciones internas: `ai::internal::*`
- Validar precondiciones al inicio
- Usar:
  - `core::exists`
  - `message_info`
  - `message_success`
  - `message_error`
- Retornar `return 1` ante errores

---

## Alcance de la Implementacion

1. Actualizar `config/base.zsh`
   - Definir variables necesarias para configuracion (sin instalacion), por ejemplo:
     - `AI_OPENCODE_CONFIG_PATH="${HOME}/.config/opencode"`
     - `AI_OPENCODE_CONFIG_FILE="opencode.json"`
   - NO agregar nuevas herramientas ni tocar `AI_TOOLS` si no es necesario.

2. Crear estructura de datos (si no existe)
   - Crear `data/opencode/` con un archivo de configuracion base (solo un ejemplo minimo y seguro, sin secretos):
     - `data/opencode/opencode.json`

3. Implementar funcion interna (sin instalacion)
   - Archivo: `internal/base.zsh`
   - Agregar:
     - `ai::internal::opencode::sync`
   - Requisitos:
     - Validar precondiciones (por ejemplo: que exista `AI_OPENCODE_CONFIG_SOURCE_PATH` y el archivo fuente).
     - Crear el directorio destino `AI_OPENCODE_CONFIG_PATH` si no existe.
     - Sincronizar el archivo(s) de configuracion desde `data/opencode/` hacia `AI_OPENCODE_CONFIG_PATH`.
     - Usar `message_info/message_success/message_error`.
     - Retornar `return 1` si falla.
     - NO descargar nada, NO ejecutar instaladores, NO tocar `ai::internal::opencode::install`.

4. Crear funcion publica
   - Archivo: `pkg/helper.zsh`
   - Agregar:
     - `ai::opencode::sync` que delega a `ai::internal::opencode::sync`

5. Documentar
   - Archivo: `docs/functions.md`
   - Agregar seccion con el formato existente (como ollama), por ejemplo:
     - `### ai::opencode::sync`
     - Descripcion + ejemplo de uso

---

## Restricciones

- No explicar nada.
- No agregar texto adicional.
- No modificar otras herramientas.
- No cambiar estructura existente.
- Mantener estilo consistente con el codigo actual.

---

## Formato de Salida

Responder unicamente con:

1. Snippet de `config/base.zsh`
2. Implementacion en `internal/base.zsh`
3. Snippet de `pkg/helper.zsh`
4. Seccion para `docs/functions.md`
5. (Si agregas archivos) contenido de `data/opencode/opencode.json`
6. validar con el comando: `task validate`

- Agrupar por archivo.
- No agregar comentarios fuera del codigo.