---
name: aeo-apprecio
description: Monitorea, analiza y mejora la visibilidad de Apprecio y Dcanje en las respuestas de ChatGPT, Gemini, Claude, Perplexity y Google AI Mode/Overviews usando la herramienta de AEO de HubSpot vía MCP. Usa esta skill SIEMPRE que el usuario mencione AEO, GEO, answer engine optimization, visibilidad en IA, share of voice en IA, menciones o citaciones en respuestas de IA, prompts trackeados, "cómo aparecemos en ChatGPT", "qué dice la IA de nosotros", "nos citan las IA", o pida crear, revisar, priorizar u optimizar prompts de AEO por país (Chile, Perú, Colombia, México, España). También aplica cuando pida el informe mensual de AEO, comparar la visibilidad contra competidores como Cobee, Awardco, Bonusly, Workhuman o Reward Gateway, o analizar qué dominios están siendo citados por las IA en nuestra categoría.
---

# AEO para Apprecio y Dcanje

El AEO (Answer Engine Optimization) mide y mejora cuánto y cómo aparece la marca cuando una persona le pregunta a una IA por soluciones de nuestra categoría. No es SEO: no hay ranking ni clics, hay menciones dentro de una respuesta generada y dominios citados como fuente.

La herramienta de AEO de HubSpot funciona así: se registran "prompts" (preguntas reales de compradores), HubSpot los ejecuta periódicamente contra varios asistentes de IA, y guarda la respuesta literal, las menciones de marca y las URLs citadas. De ahí salen tres cosas que importan:

- **Visibilidad**: en qué proporción de ejecuciones aparece la marca.
- **Share of voice**: cuánto aparecemos nosotros frente a cada competidor.
- **Citaciones**: qué dominios usan las IA como fuente, y cuáles son nuestros (owned) y cuáles no.

El trabajo real está en el portafolio de prompts. Un portafolio mal diseñado produce métricas que se ven bien y no significan nada. Por eso `references/redaccion-de-prompts.md` es la parte más importante de esta skill y hay que leerla antes de proponer cualquier prompt.

## Antes de empezar

Carga siempre el contexto de marca desde la carpeta local del proyecto (ruta configurada en `references/configuracion.md`). Sin ese contexto los prompts salen genéricos y las recomendaciones no sirven. Si la carpeta no está disponible, dilo y pide la ruta antes de seguir.

Lee también `references/configuracion.md`: ahí están los países, marcas por mercado, competidores, el registro local de prompts y la carpeta de Drive donde va el informe.

## Flujo de trabajo

### 1. Resolver el contexto del portal

Nunca asumas IDs. En este orden:

1. `get_aeo_metrics` con `include: ["BUSINESS_UNITS"]` para obtener el `businessUnitId`.
2. `get_aeo_metrics` con `include: ["ICPS_AND_PRODUCTS"]` para obtener los `icpIds` y `productIds` válidos, que son obligatorios al crear prompts.
3. `get_aeo_metrics` con `include: ["LIMITS"]` para saber cuántos prompts quedan disponibles (`promptsUsed` vs `promptsCapacity`).

Si la respuesta trae `setupStatus.inputProfileConfigured: false`, el AEO no está configurado en esa business unit. No reportes "no hay datos todavía": explica que falta completar el setup de AEO en HubSpot, porque son cosas distintas.

Si la llamada devuelve un error de permisos, para y dile al usuario que su usuario de HubSpot no tiene habilitado el acceso a AEO. No hay forma de sortearlo desde aquí.

El detalle de secciones, filtros y campos está en `references/flujo-hubspot-aeo.md`. Léelo antes de la primera llamada de cada sesión.

### 2. Diagnóstico

Para una lectura completa del periodo, pide en una sola llamada: `SUMMARY`, `PROMPTS`, `CITATIONS`, `COMPETITORS`, `ASSISTANT_BREAKDOWN` y `RUN_STATUS`. Por defecto usa los últimos 30 días, y siempre trae también el periodo anterior equivalente para poder comparar. Un número de visibilidad sin su variación no dice nada.

Cuando un prompt tenga visibilidad baja y quieras entender por qué, usa `manage_aeo_prompts` con la operación `DETAIL` para leer la respuesta literal de la IA. Ahí se ve lo que de verdad pasa: a quién sí mencionó, con qué argumento, y qué fuentes citó. Baja el `maxRuns` si solo necesitas una muestra, porque estas respuestas son largas.

### 3. Análisis

Interpreta, no listes métricas. Las preguntas que el informe debe contestar:

- ¿Aparecemos más o menos que el mes pasado, y por qué? Cruza la variación con prompts nuevos, cambios de contenido y movimientos de competidores.
- ¿En qué asistentes somos fuertes y en cuáles invisibles? Perplexity y Google AI Mode dependen mucho de fuentes indexadas recientes; ChatGPT y Claude pesan más el contenido consolidado. Un hueco en un solo asistente casi siempre es un problema de fuentes, no de marca.
- ¿Qué dominios nos están citando y cuáles no son nuestros? Los dominios no propios que se repiten son la lista de trabajo de PR, directorios y comparadores. Es la palanca más rápida.
- ¿Dónde nos gana cada competidor? Mira share of voice por fase del journey, no solo el total.
- ¿Qué prompts están muertos? Prompts con cero menciones sostenidas durante dos periodos son candidatos a reemplazo, porque el cupo es limitado.

### 4. Diseñar prompts nuevos

Lee `references/redaccion-de-prompts.md` completo antes de escribir el primero. Resumen de lo no negociable:

- Escribe como escribe una persona real hablándole a una IA, no como una keyword. Una o dos frases, un solo intent.
- No metas el nombre de la marca salvo en los prompts branded explícitos. Un prompt que dice "Apprecio" se autocumple y ensucia la visibilidad.
- Localiza de verdad: cambia el vocabulario del país, no solo el nombre del país. En México la marca es Dcanje.
- Cubre las cuatro fases del journey, no solo comparativas.

Propón siempre los prompts en una tabla para revisión antes de crearlos, con país, fase, texto y qué hipótesis se está probando con cada uno.

### 5. Crear los prompts

`manage_aeo_prompts` con la operación `CREATE` exige un flujo de confirmación en dos pasos, y no es opcional:

1. Primera llamada con `confirmed: false`. Devuelve una vista previa con el consumo de cupo.
2. Muestra al usuario los prompts y los números `promptsUsed` / `promptsCapacity`.
3. Solo con su aprobación explícita, vuelve a llamar con `confirmed: true`.

Si la vista previa avisa que se excede el límite, para ahí. No fuerces la creación: presenta las dos salidas (liberar prompts existentes o ampliar el plan) e incluye el `managePromptsUrl` que viene en la respuesta.

Usa `location` para el país (por ejemplo "Chile", "Mexico", "Spain") y `language` para el idioma. Como todos nuestros mercados son de habla hispana, la diferenciación real la hace el texto del prompt más el `location`.

Después de crear, HubSpot ejecuta los prompts de inmediato. Sondea `get_aeo_metrics` con `include: ["RUN_STATUS"]` hasta que `runInProgress` sea false para saber que terminó.

Importante: por MCP se pueden crear prompts pero no editarlos ni eliminarlos. Eso solo se hace en la interfaz de HubSpot. Trata cada creación como definitiva y revisa el texto dos veces antes de confirmar.

### 6. Registrar y reportar

Después de crear prompts, actualiza el registro local descrito en `references/configuracion.md` con el `promptId`, país, fase y fecha. HubSpot no guarda el país como filtro, así que sin ese registro el análisis por mercado se vuelve imposible en el siguiente ciclo.

Genera el informe siguiendo `references/plantilla-informe.md`. El entregable es un documento compatible con Google Docs: usa la skill `docx` para producir un .docx, guárdalo en la carpeta local del proyecto y súbelo a la carpeta de Drive indicada en la configuración. Si no tienes forma de escribir en Drive en esa sesión, entrega la ruta del archivo y dilo claramente en vez de dar por hecha la subida.

## Cómo escribir

Todo lo que salga de esta skill, prompts e informe, va en español natural. Nada de guiones largos. Nada de lenguaje de agencia ("potenciar sinergias", "impulsar el engagement de manera holística"). Frases cortas y directas. En el informe, cada hallazgo va seguido de qué hacer con él, porque un dato sin acción asociada no se usa nunca.

## Errores que arruinan el trabajo

- Reportar visibilidad sin comparar contra el periodo anterior.
- Crear prompts que mencionan la marca y luego celebrar la visibilidad alta.
- Usar el mismo prompt traducido para los cinco países cambiando solo el nombre del país.
- Confundir "setup incompleto" con "sin datos".
- Quemar cupo de prompts en preguntas que ninguna persona real haría.
- Proponer acciones de contenido sin mirar antes qué dominios están citando las IA.

## Archivos de referencia

- `references/configuracion.md`: rutas locales, países, marcas, competidores, carpeta de Drive y registro de prompts.
- `references/flujo-hubspot-aeo.md`: secciones, parámetros y límites reales de las tres herramientas MCP de AEO.
- `references/redaccion-de-prompts.md`: cómo se escribe un prompt de tracking que sirve, con banco de ejemplos por país y fase.
- `references/plantilla-informe.md`: estructura exacta del informe mensual.
