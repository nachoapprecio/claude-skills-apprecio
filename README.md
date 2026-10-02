# Claude Skills — Apprecio

Skills personalizadas de Claude para el equipo de marketing de Apprecio / Dcanje.

| Skill | Para qué sirve |
|---|---|
| [aeo-apprecio](skills/aeo-apprecio) | Monitorear y mejorar la visibilidad de Apprecio y Dcanje en ChatGPT, Gemini, Claude, Perplexity y Google AI (AEO/GEO) vía HubSpot. |
| [hubspot-image-delivery](skills/hubspot-image-delivery) | Subir una imagen de Apprecio a HubSpot Files y entregar la URL canónica de `estudios.apprecio.com` (origen: Codex; incluye `scripts/hubspot-upload-image.sh`, que en local vive en `~/.openclaw/workspace/scripts/`). |
| [hubspot-hubl-module](skills/hubspot-hubl-module) | Crear o editar módulos de HubSpot CMS en HubL (module.html, module.css, module.js, fields.json, meta.json). |
| [outbound-email-specialist-apprecio](skills/outbound-email-specialist-apprecio) | Correos fríos y secuencias outbound (Apollo / HubSpot) para Apprecio y Dcanje. |
| [paid-media-apprecio](skills/paid-media-apprecio) | Copy de anuncios para Google Ads, Meta Ads y LinkedIn Ads (Rewards, Beat, Beat Performance). |

## Instalación

- **Claude.ai / Desktop:** comprime la carpeta de la skill en un `.zip` y súbela en *Settings → Capabilities → Skills*.
- **Claude Code:** copia la carpeta a `~/.claude/skills/` (personal) o a `.claude/skills/` dentro de un proyecto.

```bash
cd skills && zip -r ../paid-media-apprecio.zip paid-media-apprecio
```
