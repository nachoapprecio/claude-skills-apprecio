---
name: hubspot-image-delivery
description: Deliver a branded Apprecio image through HubSpot Files when the user asks for a URL instead of an attachment.
argument-hint: "<image-path>"
disable-model-invocation: true
allowed-tools: Read, Bash
---

# HubSpot Image Delivery

## When to use

Use for a generated or received Apprecio image that must be saved/uploaded and returned as a canonical HubSpot URL. Do not use for an attachment-only request or when the authenticated HubSpot CLI is unavailable.

## Step 0 — Definir rutas (installation rule, mandatory)

This skill uses no hardcoded machine paths. Before any other step, resolve these two paths and keep them for the rest of the task:

| Variable | What it is | Default suggestion |
|---|---|---|
| `IMAGES_DIR` | Local folder where images are **saved** before upload and **read from** for upload | `~/apprecio-agent-files/images` |
| `UPLOAD_SCRIPT` | Upload wrapper that is **executed** | `scripts/hubspot-upload-image.sh` inside this skill's folder |

Resolution order:

1. If the environment defines `HUBSPOT_IMAGES_DIR` and/or `HUBSPOT_UPLOAD_SCRIPT`, use them, and tell the user which paths are in use in one line.
2. If the user already gave the paths earlier in the conversation, reuse them.
3. Otherwise **ask the user** before touching any file, stating explicitly what will happen in each path. Use this message (in Spanish):

   > Antes de subir la imagen necesito definir dos rutas:
   > 1. **Carpeta de imágenes** — ahí se **guardará** la imagen (o se copiará si me la entregas desde otro lugar) y desde ahí se **extraerá** para subirla a HubSpot. Sugerencia: `~/apprecio-agent-files/images`.
   > 2. **Script de subida** — el archivo que se **ejecutará** para subir la imagen. Sugerencia: `scripts/hubspot-upload-image.sh` incluido en esta skill.
   >
   > ¿Uso estas rutas o prefieres otras?

Rules:

- Never assume a path silently, and never use another user's home directory.
- If `IMAGES_DIR` does not exist, ask for confirmation before creating it.
- Copying or moving an image into `IMAGES_DIR` requires the user's authorization for this task; prefer copying over moving.
- Verify `UPLOAD_SCRIPT` exists and is executable (`chmod +x` only with confirmation).
- Optional: `HUBSPOT_ACCOUNT` overrides the HubSpot portal ID used by the script (default `7357268`).

## Inputs and context

1. Confirm the image is in `IMAGES_DIR` (copy it there only with user-authorized task scope).
2. For generated work, apply the supplied Apprecio HTML/CSS visual guidance and export a high-quality image before upload.
3. Inspect `UPLOAD_SCRIPT` before relying on it; do not print credentials or secret-bearing environment values.

## Procedure

1. Run:
   ```sh
   "$UPLOAD_SCRIPT" "$IMAGES_DIR/<filename>"
   ```
2. Capture the returned filename/URL and form the delivery URL only as:
   `https://estudios.apprecio.com/hubfs/agent-files/images/<filename>`.
   (`/agent-files/images/` is the remote HubSpot Files folder, independent of the local `IMAGES_DIR`.)
3. Validate the URL with `curl --head` and require HTTP 200 plus the expected image MIME type before sharing it.
4. Return the canonical `estudios.apprecio.com` URL, not a technical `hubspotusercontent` URL. Attach the file only if explicitly requested.

## Efficiency plan

- Use the wrapper directly; it stages the source in a temporary directory to avoid `.hsignore` exclusions and applies `PUBLIC_NOT_INDEXABLE`.
- Stop at the first failed wrapper invocation; inspect its error rather than retrying direct uploads.
- Do not try native-shell `curl` with `HUBSPOT_PRIVATE_APP_TOKEN`: protected secrets are not injected into that runtime.

## Pitfalls and fixes

- `Falta el secreto HUBSPOT_PRIVATE_APP_TOKEN en el runtime.` -> use the authenticated `hs` CLI wrapper, not the Private App path.
- `The file ... is being ignored via an .hsignore rule` -> use the wrapper; it must stage the file outside the source folder before CLI upload.
- No API confirmation, file ID, or reachable URL -> upload is unconfirmed; do not report success.

## Verification checklist

- `IMAGES_DIR` and `UPLOAD_SCRIPT` were defined (env, earlier answer, or confirmed by the user).
- The requested image exists in `IMAGES_DIR`.
- Wrapper completed and returned an upload result.
- Canonical URL responds HTTP 200 with the expected content type.
- Final handoff contains the canonical URL only, unless the user requested an attachment.
