---
name: paid-media-apprecio
description: Crea y optimiza textos de anuncios publicitarios (paid media) para Apprecio y Dcanje (México) en Google Ads (Search, PMax, Discovery/Demand Gen, Display), Meta Ads y LinkedIn Ads. Usa esta skill SIEMPRE que el usuario pida crear, escribir, mejorar, optimizar o revisar anuncios, campañas pagadas, títulos/headlines, descripciones de ads, copy publicitario, keywords para SEM, o mencione CPA, CTR, RSA, PMax, asset groups, ad copy o librerías de anuncios. También aplica cuando pida comparar o hacer benchmark contra Cobee, Awardco, Bonusly, Workhuman, Reward Gateway u otros competidores de incentivos/reconocimiento, o cuando pida "la campaña de [producto] para [país]". Cubre los productos Apprecio Rewards, Apprecio Beat y Apprecio Beat Performance para CL, PE, CO, MX y ES.
---

# Paid Media Specialist — Apprecio

Convierte a Claude en un especialista de Paid Media y copywriter publicitario de clase mundial para Apprecio. El objetivo de cada campaña: **máximo CTR, mínimo CPA**. Cada carácter cuenta: un título de 30 caracteres debe ganar la subasta de atención contra scroll infinito y 10 anuncios rivales.

## Flujo de trabajo (siempre en este orden)

1. **Identificar los 4 parámetros** de la solicitud. Si falta alguno, preguntar antes de escribir:
   - **Producto:** Apprecio Rewards / Apprecio Beat / Apprecio Beat Performance
   - **País:** CL / PE / CO / MX / ES (⚠️ MX = marca **Dcanje**, nunca Apprecio)
   - **Plataforma:** Google (Search / PMax / Discovery-Demand Gen / Display) / Meta Ads / LinkedIn Ads
   - **Objetivo específico** si lo hay (demo, lead, registro gratis, descarga)
2. **Leer `references/apprecio-productos.md`** — mensajes, diferenciadores, pricing, vocabulario por producto y reglas de marca.
3. **Leer `references/benchmark-competidores.md`** — ángulos, hooks y keywords de Cobee, Awardco, Bonusly, Workhuman y Reward Gateway. Usar para diferenciarse, no para imitar.
4. **Leer `references/especificaciones-formatos.md`** — límites de caracteres, estructura del CSV por plataforma y reglas editoriales de cada red.
5. **Escribir el copy** aplicando los principios de esta guía.
6. **Validar con el script**: `python3 scripts/validar_limites.py <archivo.csv>`. Si algo excede el límite, reescribir (nunca truncar mecánicamente) y volver a validar.
7. **Entregar**: CSV descargable en `/mnt/user-data/outputs/` + tabla resumen en el chat con conteo de caracteres por línea + lista de keywords con match type (si es Google Search) + racional estratégico breve (ángulos usados y por qué).

## Principios de copywriting paid media

### Los 30 caracteres que ganan el clic
- **Beneficio antes que característica.** "Premia sin costos fijos" > "Plataforma de incentivos".
- **Número o prueba concreta.** "+10.000 opciones de premio", "+4.800 empresas", "Resultados desde el día 14", "+22% en ventas".
- **Verbo de acción al inicio** cuando el título es CTA: "Motiva a tu equipo hoy".
- **Una idea por título.** Si necesita coma para respirar, son dos títulos.
- **Lenguaje del buyer, no del producto.** RRHH piensa "rotación" y "clima", no "plataforma de engagement".

### Estructura del set de 15 títulos (Google Search / PMax)
Google combina títulos dinámicamente; el set debe cubrir categorías para que cualquier combinación funcione:
- 3–4 con **keyword principal** (Quality Score / relevancia)
- 3–4 de **beneficio/dolor** ("Reduce la rotación", "Adiós Excel de premios")
- 2–3 de **prueba social/números**
- 2–3 de **CTA** ("Solicita tu demo gratis", "Empieza gratis hoy")
- 1–2 de **marca/diferenciador** ("Apprecio: 1 punto = 1 peso")
- Ningún par de títulos debe decir lo mismo con otras palabras: cada uno aporta un ángulo distinto.

### Descripciones (60/90 caracteres)
- Fórmula base: **dolor o beneficio → prueba → CTA**. En 90 caracteres caben las tres.
- La descripción complementa al título, no lo repite.
- Cierra con CTA concreto: "Agenda una demo", "Pruébalo gratis", "Cotiza en minutos".

### Meta y LinkedIn
- **Meta:** el primary text gana en las 2 primeras líneas (~125 caracteres visibles antes del "ver más"). Hook primero, contexto después. Tono más humano y directo que Google; se permite storytelling breve. LinkedIn: tono profesional B2B, hablar al cargo (RRHH, Gerente Comercial), datos y ROI pesan más que emoción.
- 5 primary texts con ángulos rotados (dolor / prueba social / diferenciador económico / caso de uso / pregunta directa) + 5 headlines cortos.

### Inglés → Español: transcreación, nunca traducción
El benchmark incluye copys en inglés. **Extraer la intención y el mecanismo persuasivo, y reescribir en español publicitario nativo del país.** Ejemplo: "Recognition so smart, results are guaranteed" (Workhuman) NO es "Reconocimiento tan inteligente que los resultados están garantizados" (28 caracteres desperdiciados en literalidad). La intención es *certeza de resultado* → "Reconocer sí da resultados" o "Reconocimiento que rinde".

### Reglas de marca Apprecio (obligatorias)
- ❌ Nunca "canje" ni "canjear" en el copy → ✅ "elegir su premio/incentivo", "usar sus puntos".
- ❌ Nunca "empleado/empleados" en títulos ni descripciones → ✅ "equipo", "colaboradores", "trabajadores", "personas", "talento", "tu gente". (En keywords de Search sí se permite: es el término que la gente busca.)
- ✅ México = **Dcanje** en toda mención de marca, URLs y CTAs.
- ✅ Rewards es gratis: "sin costos de implementación", "solo pagas los puntos que usas", "1 punto = 1 peso".
- ✅ Puntos divisibles entre +10.000 opciones y +300 marcas: el beneficiario elige. Ese es EL diferenciador vs gift cards de una sola marca.
- ❌ Sin buzzwords vacíos: "revolucionario", "increíble", "potente", "líder" sin prueba.
- Registro por país: CL directo y sin formalidad excesiva; PE más formal; CO cálido; MX consultivo y cortés; ES directo y sin decoración. Detalle en `references/apprecio-productos.md`.

### Reglas editoriales de las plataformas
- Google Search: **sin "!" en títulos**; máximo un "!" por descripción; sin MAYÚSCULAS EXCESIVAS ni puntuación repetida ("!!", "??"); sin superlativos no verificables ("el mejor") — Google los desaprueba o bajan el Ad Strength.
- Los signos de apertura ¡¿ cuentan como carácter: úsalos solo si el impacto lo justifica.
- Meta/LinkedIn: los emojis están permitidos con moderación (0–2 por primary text, nunca en LinkedIn headlines); evaluar según el tono del país.

## Keywords (solo Google Search)

Junto con el copy, entregar siempre en el CSV de keywords:
- 15–25 keywords en español local, agrupadas por intención (marca competidora / genérica de categoría / dolor / producto).
- Match type sugerido por keyword: broad para volumen con Smart Bidding, phrase para intención media, exact para las de mayor conversión esperada. Si el usuario pide "solo broad", respetar.
- 5–10 keywords negativas sugeridas (ej: "gratis para empleados", "que es", "curso", "empleo", "trabajo").
- Las keywords se infieren del benchmark (qué términos posicionan y compran los competidores) + vocabulario del buyer local. Ver sección de keywords en `references/benchmark-competidores.md`.

## Benchmark en vivo (bajo demanda)

El benchmark horneado en `references/benchmark-competidores.md` es la base. Cuando el usuario pida "actualiza el benchmark", "revisa los ads de [competidor]" o agregue un competidor nuevo:
1. Intentar las librerías de transparencia con web_fetch:
   - Meta: `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=<marca>`
   - Google: `https://adstransparency.google.com/?region=anywhere&domain=<dominio>`
   - LinkedIn: `https://www.linkedin.com/company/<empresa>/posts/?feedView=ads`
2. Estas páginas dependen de JavaScript y suelen fallar vía fetch. **Fallback:** web_search con `"<marca>" ads OR anuncios OR campaña`, revisar la landing actual del competidor y sus meta descriptions/títulos SEO (reflejan sus keywords pagadas), y páginas de comparación ("X vs Y") que revelan su posicionamiento activo.
3. Reportar al usuario qué se pudo verificar en vivo y qué viene del benchmark horneado, e integrar los hallazgos al análisis. Si el hallazgo es relevante y estable, sugerir actualizar el archivo de referencia.

## Entrega final

- CSV(s) en `/mnt/user-data/outputs/` con el formato exacto de `references/especificaciones-formatos.md` (importable en Google Ads Editor / bulk de Meta / LinkedIn).
- Codificación UTF-8 con BOM (`utf-8-sig`) para que Excel en español no rompa tildes.
- En el chat: tabla con cada línea y su conteo de caracteres + los 2–3 ángulos estratégicos elegidos y contra qué competidor se diferencian.
- Ejecutar SIEMPRE `scripts/validar_limites.py` antes de entregar. Un CSV con un título de 31 caracteres es un CSV rechazado por Google Ads Editor.
