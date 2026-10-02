---
name: hubspot-hubl-module
description: >
  Crea o edita módulos de HubSpot CMS con renderizado SSR/SSG usando HubL.
  Usar esta skill siempre que el usuario pida crear un nuevo módulo de HubSpot,
  convertir un HTML a módulo HubL, agregar secciones a un módulo existente,
  editar campos o estilos de un módulo ya creado, o cualquier tarea que involucre
  archivos .module de HubSpot (module.html, module.css, module.js, fields.json,
  meta.json). También aplica cuando el usuario diga "sigue el proceso de la guía",
  "convierte este HTML a módulo", "crea el módulo para [solución]" o "edita el módulo".
---

# Skill: HubSpot HubL Module (SSR/SSG)

## Cuándo aplicar esta skill

- Crear un módulo nuevo desde un HTML de referencia
- Editar o extender un módulo existente (agregar sección, cambiar campo, ajustar estilos)
- El usuario dice "sigue el proceso de la guía" (se asume que ya adjuntó el HTML fuente y la carpeta `.module` base)

---

## Archivos de un módulo

Cada módulo vive en una carpeta `nombre.module/` con exactamente estos archivos:

| Archivo | Responsabilidad |
|---|---|
| `module.html` | Estructura + variables HubL. Sin lógica inline ni scripts. |
| `module.css` | Todos los estilos, encapsulados bajo `#root-nombre`. |
| `module.js` | Interacciones y animaciones, en IIFE, apuntando solo al root. |
| `fields.json` | Esquema completo de campos con defaults reales del HTML fuente. |
| `meta.json` | Metadatos del módulo para HubSpot CMS. |

**Regla operativa:** todo cambio ocurre dentro de esos 5 archivos. No crear archivos alternos.

---

## Proceso: creación (HTML → módulo HubL)

### 1. Leer y analizar el HTML fuente

Antes de escribir cualquier código:

1. Identificar todas las **secciones** del HTML (hero, features, pricing, CTA, etc.)
2. Marcar qué contenido es **editable** (textos, títulos, CTAs, imágenes, listas) → irá a `fields.json`
3. Marcar qué contenido es **decorativo/estructural** → se queda hardcodeado o como emoji/texto
4. Ignorar `<nav>` y `<footer>` si vienen en el HTML — se gestionan desde CMS
5. Identificar si el HTML trae animaciones de entrada → solo implementarlas si están presentes o el usuario las pide

### 2. Definir el root ID

Convención: `root-[nombre-modulo]` en kebab-case, sin la palabra "módulo".

Ejemplos: `root-apprecio-rewards`, `root-beat-performance`, `root-home-new`

Declarar al inicio de `module.html`:
```html
{% set root_id = "root-nombre" %}
<div id="{{ root_id }}" class="module-reset nombre-module">
  ...
</div>
```

### 3. Construir `module.html`

- Migrar el markup del HTML fuente manteniendo semántica HTML5
- Reemplazar cada texto/título/CTA visible por una variable HubL: `{{ module.seccion.campo }}`
- Usar `{% for item in module.seccion.items %}` para listas repetibles
- Usar `{% if module.seccion.enabled %}` solo cuando una sección completa sea opcional
- Para imágenes: `{{ module.seccion.imagen.src }}` con `alt="{{ module.seccion.imagen.alt }}"`
- Si el HTML usa emojis como iconos, mantenerlos como campo de texto editable (en edición podrán reemplazarse por SVG)
- No incluir `<style>` ni `<script>` inline

### 4. Construir `fields.json`

**Reglas:**
- Cada variable HubL en `module.html` debe tener su campo en `fields.json`
- El `default` de cada campo debe ser **el contenido real del HTML fuente** (no placeholders genéricos)
- Los textos en español deben preservar tildes, ñ y caracteres especiales
- Usar `richtext` para títulos con HTML (spans de color, `<br>`, `<strong>`)
- Usar `text` para textos planos, labels, URLs, CTAs
- Usar `image` para imágenes reales
- Para listas repetibles usar `group` con `occurrence` y array de `default`
- Evitar nombres de campo conflictivos: no usar `label` solo — preferir `label_text`, `chip_label`, etc.

**Tipos de campo más usados:**

```json
{ "name": "campo", "label": "Label", "type": "text", "default": "Valor del HTML" }
{ "name": "campo", "label": "Label", "type": "richtext", "default": "Texto con <span>HTML</span>" }
{ "name": "campo", "label": "Label", "type": "image", "default": { "src": "", "alt": "" } }
{
  "name": "items",
  "label": "Items",
  "type": "group",
  "occurrence": { "min": 1, "max": 8, "default": 3 },
  "children": [ ... ],
  "default": [ { ... }, { ... } ]
}
```

### 5. Construir `module.css`

Ver sección **Reglas de CSS** más abajo — es la parte más detallada.

### 6. Construir `module.js`

- Siempre en IIFE: `(function () { ... })();`
- Usar `var` (no `let`/`const`) para máxima compatibilidad con HubSpot
- Apuntar siempre al root: `document.querySelectorAll('#root-nombre')`
- Bootstrapear con `DOMContentLoaded` o check de `document.readyState`:
  ```js
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }
  ```
- Si no hay interacciones ni animaciones, dejar el archivo con comentario: `/* No JS required for this module */`

### 7. Construir `meta.json`

```json
{
  "label": "Nombre legible del módulo",
  "content_types": ["SITE_PAGE", "LANDING_PAGE"],
  "is_available_for_new_content": true,
  "global": false,
  "help_text": "Descripción breve del módulo",
  "tags": ["apprecio", "tag-relevante"]
}
```

---

## Proceso: edición de módulo existente

1. Leer los 5 archivos del módulo existente antes de modificar nada
2. Identificar qué se cambia: ¿nueva sección? ¿nuevo campo? ¿ajuste de estilos?
3. Mantener el `root_id` y la convención de nombres existente
4. Si se agrega una sección nueva:
   - Añadir el bloque HTML con variables HubL nuevas
   - Agregar los campos correspondientes en `fields.json` con defaults reales
   - Añadir estilos en `module.css` siguiendo el orden y formato de las secciones existentes
5. Si se modifica un campo existente: actualizar `fields.json` y las referencias en `module.html`
6. No romper campos existentes ni renombrarlos sin avisar al usuario

---

## Reglas de CSS

### Variables del root (siempre estas, sin más)

```css
#root-nombre {
  --pink: #fa345e;
  --white: #ffffff;
  --soft-pink: #ffe6e8;
  --text: #1b1b1b;
}
```

No agregar variables adicionales de color fuera de estas cuatro. Si se necesita una variante (ej. color semitransparente), calcularla inline con `rgba()` o derivarla directamente.

### Fuente

Siempre Montserrat. Siempre declarar en el root:
```css
#root-nombre {
  font-family: 'Montserrat', sans-serif;
}
```

Font-weight máximo: **700**. No usar 800, 900 ni `font-weight: black`.

### Botones

Usar siempre estas dos clases base, nombradas `btn-red` y `btn-white`:

```css
/* Section: botones */
#root-nombre .btn {
  text-decoration: none;
  border: 2px solid var(--text);
  border-radius: 4px;
  box-shadow: 4px 4px 0 0 var(--text);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  font-weight: 500;
  line-height: 1.2;
  padding: 10px 28px;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

#root-nombre .btn-red {
  background-color: var(--pink);
  color: var(--white);
}

#root-nombre .btn-red:hover {
  background-color: var(--white);
  color: var(--text);
}

#root-nombre .btn-white {
  background-color: var(--white);
  color: var(--text);
}

#root-nombre .btn-white:hover {
  background-color: var(--pink);
  color: var(--white);
}
```

En `module.html` los botones usan: `class="btn btn-red"` o `class="btn btn-white"`.

### Fondos

- **Todas las secciones:** fondo blanco (`background: var(--white)`)
- **Fondo ambiente:** si el diseño lo requiere, va en el root o body con gradiente `fixed`, nunca como color sólido de sección
- Si el HTML de referencia incluye un SVG de fondo decorativo (ej. patrón repeat-x), puede aplicarse como `background-image` adicional en la sección que corresponda

### Formato y orden del CSS

**Estructura del archivo:**

1. Reset del módulo (box-sizing)
2. Variables del root + tipografía + overflow
3. Estilos base del body/root
4. Animaciones globales (si aplica)
5. Componentes reutilizables (botones, containers, labels)
6. Sección por sección, en el mismo orden que aparecen en el HTML

**Formato de cada sección — siempre así:**

```css
/* ─── Section: nombre-seccion ─── */
#root-nombre .nombre-seccion {
  /* estilos del contenedor de sección */
}

#root-nombre .nombre-seccion .nombre-seccion-title {
  /* estilos del título */
}

#root-nombre .nombre-seccion .nombre-seccion-subtitle {
  /* estilos del subtítulo */
}

#root-nombre .nombre-seccion .nombre-seccion-item {
  /* estilos de cada ítem */
}
```

**Lo que NO debe aparecer nunca:**

```css
/* MAL: agrupación multi-selector entre secciones */
#root-nombre .seccion-1,
#root-nombre .seccion-2,
#root-nombre .seccion-3 {
  padding: 60px 0;
}
```

Cada sección tiene sus propios bloques. Si dos secciones comparten exactamente el mismo valor, puede crearse una clase utilitaria global (ej. `.section-padding`) declarada en la parte de componentes reutilizables, nunca agrupando selectores de distintas secciones.

### Breakpoints

Incluir siempre al menos estos dos breakpoints al final del archivo, con los ajustes de cada sección que lo requieran:

```css
/* ─── Breakpoint: tablet (≤ 1100px) ─── */
@media (max-width: 1100px) {
  #root-nombre .hero {
    grid-template-columns: 1fr;
  }
  /* ... */
}

/* ─── Breakpoint: mobile (≤ 760px) ─── */
@media (max-width: 760px) {
  #root-nombre .hero {
    padding: 48px 20px;
  }
  /* ... */
}
```

Los breakpoints van al final del archivo, agrupados. Dentro de cada breakpoint, las secciones van en el mismo orden que en el CSS base.

---

## Animaciones de entrada (opcional)

Solo incluir si el HTML de referencia las trae o el usuario las solicita.

**Patrón estándar:**

```css
/* ─── Section: animaciones ─── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}

#root-nombre .anim-section {
  opacity: 0;
  transform: translateY(28px);
}

#root-nombre .anim-section.is-visible {
  animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

#root-nombre .anim-card {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.55s cubic-bezier(0.22, 1, 0.36, 1),
              transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
  transition-delay: calc(var(--i, 0) * 90ms);
}

#root-nombre .anim-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
function initReveal(root) {
  var sections = root.querySelectorAll('.anim-section');
  if (!sections.length || typeof IntersectionObserver === 'undefined') {
    for (var i = 0; i < sections.length; i++) {
      sections[i].classList.add('is-visible');
      var cards = sections[i].querySelectorAll('.anim-card');
      for (var c = 0; c < cards.length; c++) cards[c].classList.add('is-visible');
    }
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    for (var e = 0; e < entries.length; e++) {
      if (!entries[e].isIntersecting) continue;
      var section = entries[e].target;
      section.classList.add('is-visible');
      var cards = section.querySelectorAll('.anim-card');
      for (var c = 0; c < cards.length; c++) {
        (function (card, idx) {
          setTimeout(function () { card.classList.add('is-visible'); }, 70 + idx * 80);
        })(cards[c], c);
      }
      observer.unobserve(section);
    }
  }, { threshold: 0.18 });
  for (var s = 0; s < sections.length; s++) observer.observe(sections[s]);
}
```

---

## Checklist antes de entregar

- [ ] `module.html`: no tiene `<style>` ni `<script>` inline
- [ ] Todas las variables HubL tienen su campo en `fields.json`
- [ ] Todos los `default` en `fields.json` usan el contenido real del HTML fuente (en español, con tildes y ñ)
- [ ] El CSS usa solo `--pink`, `--white`, `--soft-pink`, `--text`
- [ ] Font-weight máximo 700 en todo el CSS
- [ ] Los botones usan `btn-red` o `btn-white`
- [ ] El CSS está ordenado por sección con comentarios `/* ─── Section: nombre ─── */`
- [ ] No hay agrupaciones multi-sección en el CSS
- [ ] Todas las secciones tienen fondo blanco
- [ ] No hay header/footer del HTML de referencia en el módulo
- [ ] JS en IIFE con `var`, apuntando al root

---

## Deploy de referencia

```bash
yes | hs cms upload 'ruta/nombre.module' 'ruta/nombre.module' --account='ID_CUENTA'
```

Validar en CMS: carga sin errores, render SSR correcto, campos editables sin romper layout.
