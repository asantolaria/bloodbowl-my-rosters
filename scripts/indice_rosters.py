#!/usr/bin/env python3
"""Genera el índice de rosters a partir de los títulos de cada fichero.

- rosters/README.md: sección «Rosters» con accesos a cada categoría y una tabla por categoría.
- rosters/iniciales/README.md: tabla de todos los rosters iniciales.

Uso: python3 scripts/indice_rosters.py   (idempotente; la sección va entre marcadores)
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from habilidades_en_rosters import escribir  # noqa: E402

START, END = "<!-- indice-rosters:inicio -->", "<!-- indice-rosters:fin -->"
CATEGORIAS = [
    ("iniciales", "Iniciales 1.000k", "Equipos recién creados con 1.000k, sin habilidades de progresión."),
    ("torneos-season-3", "Torneos Temporada 3", "Listas genéricas de torneo (Temporada 3 / BB2025) entre 1.000k y 1.200k."),
    ("eurobowl-2026", "EuroBowl 2026", "Listas del reglamento EuroBowl 2026 (7 tiers, Skill Gold y Flowing Funds), validadas."),
]


def titulo(path):
    for line in open(path, encoding="utf-8"):
        if line.startswith("# "):
            return line[2:].strip()
    return os.path.basename(path)


def filas(carpeta):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "rosters", carpeta, "*.md"))):
        if os.path.basename(f) == "README.md":
            continue
        t = titulo(f)
        equipo, _, resto = t.partition(" — ")
        m = re.search(r"\(([^)]*)\)\s*$", resto)
        detalle = m.group(1) if m else ""
        tier = re.search(r"Tier (\d)", detalle)
        out.append(dict(file=os.path.basename(f), equipo=equipo.strip(), detalle=detalle,
                        tier=int(tier.group(1)) if tier else None))
    return out


def tabla(carpeta, rel):
    rows = filas(carpeta)
    if carpeta == "eurobowl-2026":
        rows.sort(key=lambda r: (r["tier"] or 0, r["equipo"]))
        L = ["| Tier | Equipo |", "|------|--------|"]
        L += [f"| {r['tier']} | [{r['equipo']}]({rel}{r['file']}) |" for r in rows]
    else:
        rows.sort(key=lambda r: (r["equipo"], r["file"]))
        L = ["| Equipo | Valoración / variante |", "|--------|------------------------|"]
        L += [f"| [{r['equipo']}]({rel}{r['file']}) | {r['detalle']} |" for r in rows]
    return L, len(rows)


def reemplazar_seccion(path, cabecera, bloque):
    text = open(path, encoding="utf-8").read()
    if START in text:
        a, b = text.index(START), text.index(END) + len(END)
        text = text[:a] + bloque + text[b:]
    else:
        m = re.search(r"^## " + re.escape(cabecera) + r".*?(?=^## |\Z)", text, flags=re.M | re.S) if cabecera else None
        text = (text[:m.start()] + bloque + "\n\n" + text[m.end():]) if m else text.rstrip() + "\n\n" + bloque + "\n"
    escribir(path, text, newline="\n")


def main():
    # rosters/README.md
    accesos, secciones = [], []
    for carpeta, nombre, desc in CATEGORIAS:
        L, n = tabla(carpeta, f"{carpeta}/")
        accesos.append(f"- **[{nombre}]({carpeta}/README.md)** ({n}) — {desc}")
        secciones += [f"### {nombre}", "", *L, ""]
    bloque = "\n".join([START, "## Rosters", "", *accesos, "", *secciones, END])
    reemplazar_seccion(os.path.join(ROOT, "rosters", "README.md"), "Rosters actuales", bloque)
    # rosters/iniciales/README.md
    L, n = tabla("iniciales", "")
    bloque = "\n".join([START, f"## Rosters iniciales ({n})", "", *L, END])
    reemplazar_seccion(os.path.join(ROOT, "rosters", "iniciales", "README.md"), None, bloque)
    print("índices actualizados")


if __name__ == "__main__":
    main()
