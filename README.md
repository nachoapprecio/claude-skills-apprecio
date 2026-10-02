# Claude Skills — Apprecio

Skills personalizadas de Claude para el equipo de marketing de Apprecio / Dcanje.

| Skill | Para qué sirve |
|---|---|
| [aeo-apprecio](skills/aeo-apprecio) | Monitorear y mejorar la visibilidad de Apprecio y Dcanje en ChatGPT, Gemini, Claude, Perplexity y Google AI (AEO/GEO) vía HubSpot. |
| [hubspot-image-delivery](skills/hubspot-image-delivery) | Subir una imagen de Apprecio a HubSpot Files y entregar la URL canónica de `estudios.apprecio.com` (origen: Codex; incluye `scripts/hubspot-upload-image.sh`). |
| [hubspot-hubl-module](skills/hubspot-hubl-module) | Crear o editar módulos de HubSpot CMS en HubL (module.html, module.css, module.js, fields.json, meta.json). |
| [outbound-email-specialist-apprecio](skills/outbound-email-specialist-apprecio) | Correos fríos y secuencias outbound (Apollo / HubSpot) para Apprecio y Dcanje. |
| [paid-media-apprecio](skills/paid-media-apprecio) | Copy de anuncios para Google Ads, Meta Ads y LinkedIn Ads (Rewards, Beat, Beat Performance). |

## Instalación

- **Claude.ai / Desktop:** comprime la carpeta de la skill en un `.zip` y súbela en *Settings → Capabilities → Skills*.
- **Claude Code:** copia la carpeta a `~/.claude/skills/` (personal) o a `.claude/skills/` dentro de un proyecto.

```bash
cd skills && zip -r ../paid-media-apprecio.zip paid-media-apprecio
```

## Regla de instalación: Definir rutas

Las skills no usan rutas fijas de ningún computador. Si una skill necesita leer o guardar archivos locales, su primer paso es **Definir rutas**: toma las rutas de variables de entorno o se las pregunta al usuario, indicando qué se guardará o extraerá en cada una, y no toca archivos hasta tener esa confirmación.

`hubspot-image-delivery` usa:

| Variable de entorno | Uso |
|---|---|
| `HUBSPOT_IMAGES_DIR` | Carpeta local donde se guarda la imagen y desde donde se extrae para subirla |
| `HUBSPOT_UPLOAD_SCRIPT` | Script de subida que se ejecuta (por defecto, el incluido en la skill) |
| `HUBSPOT_ACCOUNT` | (Opcional) ID del portal de HubSpot; por defecto `7357268` |

Si no están definidas, la skill las pregunta en la primera ejecución. Para dejarlas fijas en tu equipo:

```bash
echo 'export HUBSPOT_IMAGES_DIR="$HOME/apprecio-agent-files/images"' >> ~/.zshrc
```

Requisitos de esa skill: CLI de HubSpot (`hs`) autenticada y `jq`.

