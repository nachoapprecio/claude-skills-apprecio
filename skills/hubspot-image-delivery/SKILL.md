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

## Inputs and context

1. Confirm the image is in `/Users/ignaciomolina/.openclaw/workspace/agent-files/images/` (move/copy only with user-authorized task scope).
2. For generated work, apply the supplied Apprecio HTML/CSS visual guidance and export a high-quality image before upload.
3. Inspect `/Users/ignaciomolina/.openclaw/workspace/scripts/hubspot-upload-image.sh` before relying on it; do not print credentials or secret-bearing environment values.

## Procedure

1. From `/Users/ignaciomolina/.openclaw/workspace`, run:
   ```sh
   scripts/hubspot-upload-image.sh agent-files/images/<filename>
   ```
2. Capture the returned filename/URL and form the delivery URL only as:
   `https://estudios.apprecio.com/hubfs/agent-files/images/<filename>`.
3. Validate the URL with `curl --head` and require HTTP 200 plus the expected image MIME type before sharing it.
4. Return the canonical `estudios.apprecio.com` URL, not a technical `hubspotusercontent` URL. Attach the file only if explicitly requested.

## Efficiency plan

- Use the wrapper directly; it stages the source in a temporary directory to avoid workspace `.hsignore` exclusions and applies `PUBLIC_NOT_INDEXABLE`.
- Stop at the first failed wrapper invocation; inspect its error rather than retrying direct uploads from the workspace.
- Do not try native-shell `curl` with `HUBSPOT_PRIVATE_APP_TOKEN`: protected secrets are not injected into that runtime.

## Pitfalls and fixes

- `Falta el secreto HUBSPOT_PRIVATE_APP_TOKEN en el runtime.` -> use the authenticated `hs` CLI wrapper, not the Private App path.
- `The file ... is being ignored via an .hsignore rule` -> use the wrapper; it must stage the file outside the workspace before CLI upload.
- No API confirmation, file ID, or reachable URL -> upload is unconfirmed; do not report success.

## Verification checklist

- The requested image exists in `agent-files/images/`.
- Wrapper completed and returned an upload result.
- Canonical URL responds HTTP 200 with the expected content type.
- Final handoff contains the canonical URL only, unless the user requested an attachment.
