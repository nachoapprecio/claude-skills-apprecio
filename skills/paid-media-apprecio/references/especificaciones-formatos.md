# Especificaciones por plataforma y formatos CSV

Los conteos incluyen espacios y signos (¡¿ cuentan). Validar SIEMPRE con `scripts/validar_limites.py` antes de entregar.

## Cantidades y límites por tipo de campaña

| Campaña | Activo | Cantidad | Límite |
|---|---|---|---|
| **Google Search (RSA)** | Título | 15 | 30 |
| | Descripción | 4 | 90 |
| | Ruta (path) | 2 | 15 |
| **Google PMax** | Título | 15 | 30 |
| | Título largo | 6 | 90 |
| | Descripción | 4 | 90 |
| | Descripción breve | 1 | 60 |
| **Google Discovery / Demand Gen** | Título | 5 | 40 |
| | Descripción | 5 | 90 |
| **Google Display (responsive)** | Título | 5 | 30 |
| | Título largo | 1 | 90 |
| | Descripción | 5 | 90 |
| **Meta Ads** | Primary text | 5 | ~125 visibles (hook en las 2 primeras líneas; total puede ser mayor pero el gancho va al inicio) |
| | Headline | 5 | 40 (27 recomendado para no truncar en feed) |
| | Description | opcional 2 | 30 |
| **LinkedIn Ads (single image)** | Introductory text | 5 | 150 recomendado (600 máx; se trunca ~150 en desktop) |
| | Headline | 5 | 70 (50 recomendado) |
| | Description | opcional | 100 |

Notas Google:
- Business name ≤ 25 · logo y creatividades no van en el CSV.
- Search: sin "!" en títulos; 1 "!" máximo por descripción; sin caps excesivas; sin "el mejor/único" no verificable.
- PMax títulos largos: se muestran sin el título corto — deben sostenerse solos.

## Formatos CSV (UTF-8 con BOM, separador coma, textos entre comillas si contienen comas)

### Google Search RSA — `google_search_<producto>_<pais>.csv`
Formato Google Ads Editor (una fila por anuncio):
```
Campaign,Ad group,Headline 1,...,Headline 15,Description 1,...,Description 4,Path 1,Path 2,Final URL
```

### Keywords — `keywords_<producto>_<pais>.csv`
```
Campaign,Ad group,Keyword,Match type
```
Match type: `Broad` / `Phrase` / `Exact`. Negativas en bloque aparte con Match type `Negative phrase` o como sección separada del archivo (`Campaign,Ad group,Negative keyword,Match type`).

### PMax — `google_pmax_<producto>_<pais>.csv`
Una fila por activo (los asset groups de PMax no se importan como los RSA; este formato es para carga/revisión ordenada):
```
Asset group,Tipo,Texto,Caracteres,Límite
```
Tipo ∈ {Titulo, TituloLargo, Descripcion, DescripcionBreve}.

### Meta — `meta_<producto>_<pais>.csv`
```
Campaña,Conjunto,Tipo,Texto,Caracteres
```
Tipo ∈ {PrimaryText, Headline, Description}.

### LinkedIn — `linkedin_<producto>_<pais>.csv`
```
Campaña,Tipo,Texto,Caracteres
```
Tipo ∈ {IntroText, Headline, Description}.

## URLs finales por defecto
- CL/PE/CO: https://apprecio.com (o landing de solución: /rewards, /beat, /beat-performance si el usuario confirma slugs)
- MX: dominio Dcanje (confirmar con el usuario la URL vigente antes de fijarla en el CSV)
- ES: https://apprecio.com/es (confirmar)
Si no hay URL confirmada, dejar la columna con la mejor hipótesis y marcarla al usuario en el resumen.
