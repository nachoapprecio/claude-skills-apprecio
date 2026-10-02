#!/usr/bin/env python3
"""
Valida límites de caracteres de los CSV de anuncios generados por la skill
paid-media-apprecio. Uso:

    python3 validar_limites.py archivo.csv [--plataforma auto|search|pmax|meta|linkedin|keywords]

Detecta la plataforma por el nombre del archivo o las columnas si no se indica.
Sale con código 1 si hay violaciones (para encadenar en flujos).
"""
import csv
import re
import sys
from pathlib import Path

LIMITES = {
    "search": {  # columnas del formato Google Ads Editor
        r"^Headline \d+$": 30,
        r"^Description \d+$": 90,
        r"^Path \d$": 15,
    },
    "pmax": {  # formato Asset group,Tipo,Texto,...
        "Titulo": 30,
        "TituloLargo": 90,
        "Descripcion": 90,
        "DescripcionBreve": 60,
    },
    "meta": {
        "PrimaryText": 300,   # límite duro laxo; el hook <=125 se revisa como warning
        "Headline": 40,
        "Description": 30,
    },
    "linkedin": {
        "IntroText": 600,
        "Headline": 70,
        "Description": 100,
    },
}
WARNINGS = {
    "meta": {"PrimaryText": (125, "hook visible"), "Headline": (27, "truncado en feed")},
    "linkedin": {"IntroText": (150, "truncado desktop"), "Headline": (50, "truncado móvil")},
}
PROHIBIDAS = re.compile(r"\bcanje\w*\b|\bcanjear\w*\b", re.IGNORECASE)
# "empleado/s" prohibido en copy de anuncios (no aplica a keywords)
EMPLEADOS = re.compile(r"\bemplead[oa]s?\b", re.IGNORECASE)


def detectar(path, headers):
    n = path.name.lower()
    for k in ("search", "pmax", "meta", "linkedin", "keywords"):
        if k in n or (k == "search" and "google_search" in n):
            return k
    if any(h.startswith("Headline 1") for h in headers):
        return "search"
    if "Keyword" in headers:
        return "keywords"
    if "Tipo" in headers:
        return "pmax" if "Asset group" in headers else "meta"
    return "desconocida"


def largo(s):
    return len(s.strip())


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = Path(sys.argv[1])
    plataforma = None
    if "--plataforma" in sys.argv:
        plataforma = sys.argv[sys.argv.index("--plataforma") + 1]

    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("CSV vacío")
        sys.exit(1)
    headers = list(rows[0].keys())
    if not plataforma or plataforma == "auto":
        plataforma = detectar(path, headers)
    print(f"Plataforma detectada: {plataforma} · {len(rows)} filas\n")

    errores, avisos = [], []

    for i, row in enumerate(rows, start=2):  # fila 1 = header
        # Regla de marca: nunca canje/canjear en textos
        for col, val in row.items():
            if val and PROHIBIDAS.search(val) and "dcanje" not in val.lower():
                errores.append(f"Fila {i} [{col}]: contiene 'canje/canjear' → usar 'elegir su premio' / 'usar sus puntos'")
            if val and plataforma != "keywords" and col not in ("Keyword", "Campaign", "Campaña", "Ad group", "Asset group", "Conjunto") and EMPLEADOS.search(val):
                errores.append(f"Fila {i} [{col}]: contiene 'empleado(s)' → usar equipo / colaboradores / trabajadores / talento")

        if plataforma == "search":
            for col, val in row.items():
                if not val:
                    continue
                for patron, lim in LIMITES["search"].items():
                    if re.match(patron, col):
                        if largo(val) > lim:
                            errores.append(f"Fila {i} [{col}]: {largo(val)}/{lim} → «{val}»")
                        if col.startswith("Headline") and "!" in val:
                            errores.append(f"Fila {i} [{col}]: '!' no permitido en títulos de Search → «{val}»")
                        if col.startswith("Description") and val.count("!") > 1:
                            errores.append(f"Fila {i} [{col}]: más de un '!' → «{val}»")
        elif plataforma in ("pmax", "meta", "linkedin"):
            tipo, texto = row.get("Tipo", ""), row.get("Texto", "")
            lim = LIMITES.get(plataforma, {}).get(tipo)
            if lim and largo(texto) > lim:
                errores.append(f"Fila {i} [{tipo}]: {largo(texto)}/{lim} → «{texto}»")
            w = WARNINGS.get(plataforma, {}).get(tipo)
            if w and largo(texto) > w[0]:
                avisos.append(f"Fila {i} [{tipo}]: {largo(texto)} > {w[0]} ({w[1]})")
            if plataforma == "pmax" and tipo == "Titulo" and "!" in texto:
                errores.append(f"Fila {i} [Titulo]: '!' no recomendado en títulos → «{texto}»")
            # verificar columna Caracteres si existe
            if row.get("Caracteres") and row["Caracteres"].isdigit() and int(row["Caracteres"]) != largo(texto):
                avisos.append(f"Fila {i}: columna Caracteres dice {row['Caracteres']} pero el texto mide {largo(texto)}")
        elif plataforma == "keywords":
            mt = row.get("Match type", "")
            if mt and mt not in ("Broad", "Phrase", "Exact", "Negative phrase", "Negative exact", "Negative broad"):
                errores.append(f"Fila {i}: Match type inválido «{mt}»")

    if avisos:
        print("AVISOS:")
        for a in avisos:
            print(f"  ⚠ {a}")
        print()
    if errores:
        print("ERRORES:")
        for e in errores:
            print(f"  ✗ {e}")
        print(f"\n{len(errores)} error(es). Reescribir y volver a validar.")
        sys.exit(1)
    print("✓ Todos los límites y reglas OK")


if __name__ == "__main__":
    main()
