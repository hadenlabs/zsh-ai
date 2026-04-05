# Prompt: Agregar nueva herramienta a zsh-ai (tmuxai)

## Contexto

Estas trabajando dentro de este repositorio. Debes seguir estrictamente todas las reglas definidas en AGENTS.md.

No asumas convenciones fuera de ese archivo. No introduzcas cambios que rompan compatibilidad.

---

## Objetivo

Implementar soporte para la herramienta: tmuxai

La implementacion debe integrarse completamente con la arquitectura actual del plugin.

IMPORTANTE:

- SI debes implementar la instalacion de tmuxai.
- NO debes modificar el comportamiento de `ai::install`.
- NO debes romper compatibilidad con `ai::internal::packages::install`

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
- No modificar otras herramientas
- No cambiar estructura existente
- Mantener estilo consistente con el codigo actual

---

## Alcance de la Implementacion

1. Actualizar `config/base.zsh`
   - Agregar `tmuxai` a `AI_TOOLS`
   - Definir variables necesarias:
     - `AI_INSTALL_URL_TMUXAI="<URL_DE_INSTALACION_DE_TMUXAI>"`
   - Agregar variables adicionales solo si son necesarias (por ejemplo `AI_TMUXAI_BIN_PATH` si el instalador coloca binarios fuera del PATH)

2. Implementar funcion interna en `internal/base.zsh`
   - Nombre: `ai::internal::tmuxai::install`
   - Requisitos:
     - Validar precondiciones al inicio:
       - Si `core::exists tmuxai` retorna true: `return 0`
       - Verificar dependencias necesarias si aplica (por ejemplo `curl`/`bash`/`sh`) usando `core::exists`
     - Usar `message_info` antes de instalar
     - Instalar usando el metodo oficial via `curl -fsSL "${AI_INSTALL_URL_TMUXAI}" | <shell>` o el metodo oficial equivalente
     - En exito: `message_success "tmuxai installed successfully"`
     - En falla: `message_error "Failed to install tmuxai"` y `return 1`

3. Registrar en el dispatcher
   - Modificar `ai::internal::packages::install` en `internal/base.zsh`
   - Agregar el case:
     - `tmuxai) ai::internal::tmuxai::install ;;`

4. Crear funcion publica en `pkg/helper.zsh`
   - Nombre: `ai::tmuxai::install`
   - Debe delegar a: `ai::internal::tmuxai::install`

5. Documentar en `docs/functions.md`
   - Agregar seccion en "Public Functions":
     - `#### ai::tmuxai::install`
     - Descripcion corta en el mismo estilo que `ai::ollama::install`
     - Ejemplo:
       - ```bash
         ai::tmuxai::install
         ```
   - Agregar seccion en "Internal Functions":
     - `#### ai::internal::tmuxai::install`
     - Descripcion corta
     - Ejemplo:
       - ```bash
         ai::internal::tmuxai::install
         ```

6. Validar
   - Ejecutar:
     - `task validate`
   - Si falla por cambios introducidos por tmuxai, corregirlos.
   - No arreglar fallas preexistentes no relacionadas con los cambios de tmuxai.

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
3. Actualizacion del dispatcher
4. Snippet de `pkg/helper.zsh`
5. Seccion para `docs/functions.md`
6. Resultado de `task validate` (solo el estado final: Passed/Failed y hooks que fallan si aplica)

- Agrupar por archivo.
- No agregar comentarios fuera del codigo.