#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Uso: $0 /ruta/a/imagen" >&2
  exit 64
fi

input_file="$1"
if [[ ! -f "$input_file" ]]; then
  echo "No existe el archivo: $input_file" >&2
  exit 66
fi

if ! command -v hs >/dev/null 2>&1; then
  echo "No está instalada la CLI de HubSpot (hs)." >&2
  exit 69
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "Falta jq, necesario para validar la respuesta de HubSpot." >&2
  exit 69
fi

hubspot_account="${HUBSPOT_ACCOUNT:-7357268}"
file_name="$(basename "$input_file")"
remote_path="/agent-files/images/${file_name}"
encoded_path="$(printf '%s' "$remote_path" | jq -sRr @uri)"

# HubSpot CLI respeta reglas .hsignore del directorio de origen. Un directorio
# temporal evita que las reglas del workspace bloqueen PNG, JPG u otros binarios.
temp_dir="$(mktemp -d)"
temp_file="${temp_dir}/${file_name}"

cleanup() {
  if [[ -f "$temp_file" ]]; then
    rm "$temp_file"
  fi
  if [[ -d "$temp_dir" ]]; then
    rmdir "$temp_dir"
  fi
}
trap cleanup EXIT

cp "$input_file" "$temp_file"
(
  cd "$temp_dir"
  hs filemanager upload "$file_name" "$remote_path" --account "$hubspot_account" >/dev/null
)

metadata="$(hs api "/files/v3/files/search?path=${encoded_path}" \
  --account "$hubspot_account" \
  --json)"

file_id="$(printf '%s' "$metadata" | jq -er --arg path "$remote_path" \
  '.results[] | select(.path == $path and .archived == false) | .id' | head -n 1)"

result="$(hs api "/files/v3/files/${file_id}" \
  --method PATCH \
  --data '{"access":"PUBLIC_NOT_INDEXABLE"}' \
  --account "$hubspot_account" \
  --json)"

printf '%s\n' "$result" | jq '{id, name, path, access, url: (.url // .defaultHostingUrl)}'
