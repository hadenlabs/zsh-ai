# Prompt: mover carpeta patterns to data/patterns en zsh-ai

## Contexto

Estás trabajando dentro de este repositorio. Debes seguir estrictamente todas las reglas definidas en AGENTS.md.

No asumas convenciones fuera de ese archivo. No introduzcas cambios que rompan compatibilidad.

---

## Objetivo

En nuestro proyecto, la carpeta `patterns/` contiene templates, scripts y prompts.  
Se requiere moverla a `data/patterns/` para mantener consistencia en la estructura y que todos los módulos apunten a la nueva ruta.

Actualizar todos los templates, prompts y scripts dentro de Fabric que referencian `patterns/` para que apunten a `data/patterns/`.

## Entradas

- Ruta antigua: `patterns/`
- Ruta nueva: `data/patterns/`
- Lista de archivos de Fabric que usan la carpeta (`grep -rnw './' -e 'patterns'`)
- Tipos de referencia: imports, open(), includes, paths en YAML o JSON, referencias dentro de prompts

---

## Restricciones

- No explicar nada.
- No agregar texto adicional.
- No modificar otras archivos.
- No cambiar estructura existente.
- Mantener estilo consistente con el código actual.

---

## Formato de Salida

Responder únicamente con:

1. Actualizacion en `AGENTS.md`
2. Actualizacion en `config/base.zsh`
3. Actualización en `docs/env-vars.md`

Agrupar por archivo. No agregar comentarios fuera del código.
