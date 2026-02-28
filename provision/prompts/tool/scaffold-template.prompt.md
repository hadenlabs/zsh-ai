# Prompt: Agregar nueva herramienta a zsh-ai

## Contexto

Estás trabajando dentro de este repositorio. Debes seguir estrictamente todas las reglas definidas en AGENTS.md.

No asumas convenciones fuera de ese archivo. No introduzcas cambios que rompan compatibilidad.

---

## Objetivo

Implementar soporte para la herramienta: {{tool_name}}

La implementación debe integrarse completamente con la arquitectura actual del plugin.

---

## Reglas Obligatorias (AGENTS.md)

Debes respetar estrictamente:

- Todos los archivos `.zsh` deben iniciar con: `#!/usr/bin/env ksh`
- Variables globales en mayúsculas con prefijo `AI_`
- Funciones públicas: `ai::*`
- Funciones internas: `ai::internal::*`
- Validar precondiciones al inicio
- Usar:
  - `core::exists`
  - `message_info`
  - `message_success`
  - `message_error`
- Retornar `return 1` ante errores
- No romper compatibilidad con:
  - `ai::install`
  - `ai::internal::packages::install`

---

## Alcance de la Implementación

1. Actualizar `config/base.zsh`
   - Agregar la herramienta a `AI_TOOLS`
   - Definir variables necesarias:
     - `AI_INSTALL_URL_{{TOOL_UPPER}}`
     - Variables adicionales si son necesarias

2. Implementar función interna en:
   - `internal/base.zsh`
   - Nombre: `ai::internal::{{tool_name}}::install`

3. Registrar en el dispatcher:
   - Modificar `ai::internal::packages::install`

4. Crear función pública en:
   - `pkg/helper.zsh`
   - Nombre: `ai::{{tool_name}}::install`

5. Documentar en:
   - `docs/functions.md`
   - Seguir el formato existente (como ollama)

---

## Restricciones

- No explicar nada.
- No agregar texto adicional.
- No modificar otras herramientas.
- No cambiar estructura existente.
- Mantener estilo consistente con el código actual.

---

## Formato de Salida

Responder únicamente con:

1. Snippet de `config/base.zsh`
2. Implementación en `internal/base.zsh`
3. Actualización del dispatcher
4. Snippet de `pkg/helper.zsh`
5. Sección para `docs/functions.md`

Agrupar por archivo. No agregar comentarios fuera del código.
