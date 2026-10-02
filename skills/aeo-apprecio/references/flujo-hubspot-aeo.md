# Herramientas MCP de AEO de HubSpot

Tres herramientas: `get_aeo_metrics` (lectura de métricas), `manage_aeo_prompts` (leer respuestas y crear prompts) y `manage_aeo_recommendations` (recomendaciones de contenido).

## get_aeo_metrics

Parámetros obligatorios: `startDate` y `endDate` en formato YYYY-MM-DD, interpretados en la zona horaria del portal. `businessUnitId` es opcional; si se omite, usa la business unit del portal.

Se eligen las secciones con `include`. Por defecto trae solo SUMMARY y RUN_STATUS.

| Sección | Qué devuelve |
|---|---|
| SUMMARY | averageVisibility, totalPrompts, totalResponses, totalRunsWithMentions, totalCitations, averageCompetitorsMentioned |
| PROMPTS | lista por prompt con visibilidad, menciones, respuestas y citaciones |
| CITATIONS | totales de citaciones, cuántas son de dominios propios y cuántas no, y el top 50 de dominios con marca de propio o de competidor |
| COMPETITORS | menciones por marca y share of voice, cuando hay competidores configurados |
| ASSISTANT_BREAKDOWN | las métricas abiertas por asistente, para comparar ChatGPT, Gemini, Claude, Perplexity y los productos de Google |
| RUN_STATUS | si hay una ejecución en curso, cuándo terminó la última y cuándo es la siguiente |
| ICPS_AND_PRODUCTS | los ICP y productos del Brand Identity con sus IDs, necesarios para crear prompts |
| BUSINESS_UNITS | business units del portal con sus IDs |
| LIMITS | promptsUsed, promptsCapacity, answersCapacity, onCredits y managePromptsUrl |

Detalles que cambian el resultado:

- `filters`, `models` y `assistants` solo afectan a SUMMARY y PROMPTS. CITATIONS, COMPETITORS y ASSISTANT_BREAKDOWN siempre vienen a nivel de portal para la ventana de fechas.
- `filters` permite fase del journey (AWARENESS, CONSIDERATION, EVALUATION, DECISION), estado de tracking, rango de visibilidad, producto, ICP, tema e idioma. No permite filtrar por país.
- `maxPrompts` por defecto es 100. Súbelo solo si el portafolio es mayor.
- `setupStatus.inputProfileConfigured` viene siempre que se pueda determinar. Si es false, falta el setup de AEO y el resto de secciones viene vacío por diseño. Si `setupStatus` no viene, no afirmes nada sobre el estado del setup.

## manage_aeo_prompts

Se pasa exactamente una operación.

**DETAIL**: entra a un prompt concreto y devuelve el texto completo de la respuesta de la IA, las URLs citadas y el conteo de menciones por ejecución, más las recomendaciones abiertas asociadas. Requiere `promptId` (sale de PROMPTS), `startDate` y `endDate`. `aiAssistant` filtra por asistente. `maxRuns` por defecto 10, tope 25. Las respuestas son largas: pide pocas ejecuciones salvo que necesites el detalle completo.

**CREATE**: crea prompts y los ejecuta de inmediato. Requiere `businessUnitId`, `promptTexts`, `icpIds` y `productIds`. Opcionales: `language` (BCP-47), `location` (texto libre, por ejemplo "Chile") y `topicIds`.

Flujo de confirmación obligatorio:

1. Llamada con `confirmed: false` para obtener la vista previa con el consumo de cupo.
2. Mostrar al usuario los prompts y los números promptsUsed / promptsCapacity.
3. Llamada con `confirmed: true` solo tras aprobación explícita.

Si la vista previa indica que se excede el límite, detenerse y ofrecer las dos alternativas: liberar prompts o ampliar el plan, con el `managePromptsUrl` de la respuesta.

La business unit debe tener input profile ya configurado. Esta herramienta no hace el onboarding.

Después de crear, sondear `get_aeo_metrics` con `include: ["RUN_STATUS"]` hasta que `runInProgress` sea false.

**No existe operación de edición ni de borrado por MCP.** Eso se hace en la interfaz de HubSpot.

## manage_aeo_recommendations

**LIST**: recomendaciones de la business unit, filtrables por estado y por prompts. Cada una trae id, estado, tipo, prioridad, título, resumen, justificación, dominio o URL objetivo, score y las URLs de citación que la originaron. Ciclo de vida: NEW, IN_PROGRESS, COMPLETED, DISMISSED, FAILED, ARCHIVED, DRAFT_CREATED. `limit` por defecto 25, máximo 100.

**DETAIL**: una recomendación con el estado de su acción automatizada.

**START_ACTION**: lanza la acción automática, por ejemplo publicar un post de blog. Requiere el mismo flujo de dos pasos con `confirmed`.

En el alcance actual de esta skill, las recomendaciones se usan como insumo de análisis y se llevan al informe como acciones propuestas. No se ejecuta `START_ACTION` sin que el usuario lo pida de forma explícita: publica contenido real en el portal.

## Errores conocidos

- Error de permisos en cualquier llamada: el usuario de HubSpot no tiene el acceso a AEO habilitado. No hay alternativa técnica desde aquí, hay que resolverlo con el administrador del portal.
- Secciones vacías con `setupStatus.inputProfileConfigured: false`: falta completar el setup de AEO, no es ausencia de datos.
