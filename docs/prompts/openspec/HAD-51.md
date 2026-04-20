# Entrada para OpenSpec

## Issue

- Key: HAD-51
- Title: Implementar sincronización de plugins desde opencode.json hacia documentación

---

## Contenido Fuente

### Scenario

Se requiere implementar un mecanismo que permita sincronizar la configuración de **plugins definidos en** `opencode.json`
hacia documentación dentro del proyecto que esta en docs/opencode/plugins.

Actualmente, la configuración de plugins está en docs/opencode/plugins pero no esta sincronizada.

Para resolver esto, se propone:

* crear un comando (`hadx-opencode-sync`)
* leer la sección de plugins desde `opencode.json`
* generar o actualizar la documentación de plugins en `docs/opencode/plugins`
* definir un formato estándar de documentación en Markdown
* soportar preview de cambios antes de aplicar

Esta tarea permite mantener alineada la configuración ejecutable con la documentación del sistema.

### Acceptance Tests
- existe el comando `hadx-opencode-sync`
- se leen correctamente los plugins desde `opencode.json`
- se crea la carpeta `docs/opencode/plugins` si no existe
- se genera un archivo `.md` por cada plugin
- los archivos siguen una estructura estándar
- soporta modo `--dry-run`
- muestra diff de cambios
- detecta cambios en plugins y actualiza la documentación
- no sobrescribe cambios manuales sin control

### Sources
- https://github.com/hadenlabs/zsh-ai.git
- Epic: Implementar capacidades AI con zsh-ai, opencode y MCP
- internal design

---

## Tarea

Generar una especificación completa en OpenSpec basada ÚNICAMENTE en el contenido proporcionado.

---

## Guía

Usa la información para:

- Entender el contexto del problema
- Identificar el problema principal
- Definir el alcance functional
- Convertir los acceptance tests en requerimientos claros y testeables
- Mantener una estructura clara, consistente y sin ambigüedad

Este prompt está diseñado para ayudar tanto a humanos como a sistemas a generar especificaciones de alta calidad a partir de issues de Jira.

---

## Restricciones

- NO inventar información
- Usar SOLO el contenido proporcionado
- Mantener la intención original del issue
- Evitar ambigüedades
- Usar keywords tipo RFC en los requerimientos:
  - MUST
  - SHOULD
  - MAY

---

## Post-Procesamiento (OBLIGATORIO)

Después de generar la especificación:

`task validate`

---

## Requisitos de Salida

- Generar una especificación válida de OpenSpec
- Los requerimientos deben estar en inglés usando:
  - The system MUST ...
  - The system SHOULD ...
  - The system MAY ...
- Mantener trazabilidad con el issue (HAD-51)
- Usar markdown estructurado