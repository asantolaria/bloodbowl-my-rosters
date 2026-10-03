#!/usr/bin/env python3
"""Añade a cada roster la sección «Habilidades del roster»: definición de todas las habilidades
y rasgos que llevan sus jugadores (de serie según la ficha de equipo y compradas).

Uso:
    python3 scripts/habilidades_en_rosters.py            # actualiza todos los rosters
    python3 scripts/habilidades_en_rosters.py --dry      # solo informa
    python3 scripts/habilidades_en_rosters.py RUTA.md …  # solo esos ficheros

Es idempotente: la sección va entre marcadores y se regenera en cada ejecución.
Fuentes: source/habilidades/*.md (definiciones), source/teams/*.md (habilidades de serie),
source/jugadores-estrella/*.md (estrellas).
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import audit_rosters as audit  # noqa: E402

START, END = "<!-- habilidades-roster:inicio -->", "<!-- habilidades-roster:fin -->"
CATS = {"general": "General", "agilidad": "Agilidad", "fuerza": "Fuerza", "pase": "Pase",
        "triquinuelas": "Triquiñuelas", "mutaciones": "Mutaciones", "rasgos": "Rasgo"}
# Abreviaturas y nombres antiguos usados en algunas listas
ALIAS = {"GM": "Golpe mortífero", "Hambriento": "Siempre hambriento", "Placaje def.": "Placaje defensivo",
         "Frenesí": "Furia", "Bola y cadena": "Bola con cadena", "Proyectil vómito": "Proyectil de vómito",
         "Mega-estrella": None, "Placaje def": "Placaje defensivo", "Forcejeo": "Forcejear", "Vigilar": "Defensa",
         "Inestable": "Tembloroso", "Brazo armado": "Llave de brazo", "Distraer": "Presencia perturbadora",
         "Derribar": "Placaje defensivo", "Ansia de Sangre": "Sed de sangre", "Peleón": "Luchador",
         "Aliento de Fuego": "Exhalar fuego", "Embaucador": "Embustero", "Mi Balón": "El balón es mío",
         "Sin Manos": "El balón ni verlo", "Atrapada de inmersión": "Recepción heroica", "Juego Sucio": "Jugar sucio"}


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def catalog():
    cat = {}
    for fn, label in CATS.items():
        path = os.path.join(ROOT, "source", "habilidades", fn + ".md")
        for line in open(path, encoding="utf-8"):
            c = cells(line)
            if len(c) < 4 or not c[0] or c[0].startswith("-") or "(ES)" in c[0]:
                continue
            es = c[0].replace("**", "")
            cat[es] = dict(es=es, en=re.sub(r"\s*\(X\+?\)", "", c[1]), tipo=c[2].replace("*", " (obligatoria)").strip(),
                           cat=label, file=fn, desc=c[-1])
    return cat


CAT = catalog()
# patrón: nombre ES o EN, insensible a mayúsculas, con límites de palabra «unicode»
NAMES = sorted([(k, k) for k in CAT] + [(v["en"], k) for k, v in CAT.items() if v["en"]] +
               [(a, t) for a, t in ALIAS.items() if t], key=lambda x: -len(x[0]))


def find_skills(text):
    found, rest = set(), text
    for name, key in NAMES:
        pat = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", re.IGNORECASE)
        if pat.search(rest):
            found.add(key)
            rest = pat.sub(" ", rest)  # evita que «Placar» vuelva a casar dentro de otro nombre ya contado
    return found


def team_rows(team):
    t = open(os.path.join(ROOT, "source", "teams", team + ".md"), encoding="utf-8").read()
    rows = []
    for line in t.splitlines():
        c = cells(line)
        if len(c) == 11 and re.match(r"0-\d+", c[0]):
            rows.append((audit.norm(re.sub(r"\*+", "", c[1])), int(c[2].rstrip("k")) * 1000, c[8]))
    return rows


def base_skills(pos, cost, team, rows):
    variants = audit.roster_pos_variants(pos, team)
    scored = [(max((audit.match_score(v, lk) for v in variants), default=0), lk, c, sk) for lk, c, sk in rows]
    scored = [s for s in scored if s[0] > 0]
    if not scored:
        return set()
    best = max(s[0] for s in scored)
    top = [s for s in scored if s[0] == best]
    if len(top) > 1 and cost:
        top = [s for s in top if s[2] == cost] or top
    return find_skills(top[0][3]) if len({s[3] for s in top}) == 1 else set()


def star_skills(name):
    for f in glob.glob(os.path.join(ROOT, "source", "jugadores-estrella", "*.md")):
        t = open(f, encoding="utf-8").read()
        if name and name.lower() in t.splitlines()[0].lower():
            m = re.search(r"\*\*Habilidades:\*\*([^\n]+)", t)
            return find_skills(m.group(1)) if m else set()
    return set()


def tables(lines):
    """Devuelve (inicio, fin, cabecera) de cada tabla Markdown."""
    out, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append((i, j, cells(lines[i])))
            i = j
        else:
            i += 1
    return out


def team_of(path):
    base = os.path.basename(path)
    for k in sorted(audit.MAP, key=len, reverse=True):
        if k in base:
            return audit.MAP[k]
    return None


def section(path, skills):
    lines = [START, "## Habilidades del roster", "",
             "*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). "
             "Generado con `scripts/habilidades_en_rosters.py`.*", ""]
    for k in sorted(skills, key=lambda s: s.lower()):
        s = CAT[k]
        rel = os.path.relpath(os.path.join(ROOT, "source", "habilidades", s["file"] + ".md"), os.path.dirname(path))
        lines.append(f"- **[{s['es']}]({rel.replace(os.sep, '/')})** (*{s['en']}* · {s['cat']} · {s['tipo']}): {s['desc']}")
    return lines + ["", END]


def process(path, dry=False):
    text = open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.replace("\r\n", "\n").split("\n")
    # quitar sección generada previa y la antigua «Descripción oficial de las habilidades»
    if START in lines:
        a, b = lines.index(START), lines.index(END)
        del lines[a:b + 1]
    for i, l in enumerate(lines):
        if re.match(r"^## Descripción oficial de las habilidades", l):
            j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
            del lines[i:j]
            break
    team = team_of(path)
    rows = team_rows(team) if team else []
    skills, last_lineup_end = set(), None
    for a, b, head in tables(lines):
        low = [h.lower() for h in head]
        if any("habilidades" in h for h in low) and any(h in ("posición", "position") for h in low):
            hi, pi = low.index(next(h for h in low if "habilidades" in h)), low.index(next(h for h in low if h in ("posición", "position")))
            ci = next((k for k, h in enumerate(low) if h in ("coste", "cost")), None)
            for line in lines[a + 2:b]:
                c = cells(line)
                if len(c) <= max(hi, pi):
                    continue
                skills |= find_skills(c[hi])
                cost = audit.parse_cost_gp(c[ci]) if ci is not None and ci < len(c) else None
                if "estrella" in c[pi].lower():
                    skills |= star_skills(c[1] if len(c) > 1 and c[1] not in ("____", "") else c[pi])
                elif rows:
                    skills |= base_skills(c[pi], cost, team, rows)
            last_lineup_end = b
        elif any("avance" in h or "skill" in h for h in low):
            for line in lines[a + 2:b]:
                skills |= find_skills(" ".join(cells(line)[1:3]))
    if last_lineup_end is None or not skills:
        return 0
    ins = next((k for k in range(last_lineup_end, len(lines)) if lines[k].startswith("## ")), len(lines))
    while ins > 0 and lines[ins - 1].strip() == "":
        ins -= 1
    new = lines[:ins] + [""] + section(path, skills) + [""] + lines[ins:]
    out = nl.join(new)
    if not dry:
        open(path, "w", encoding="utf-8", newline="").write(out)
    return len(skills)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = args or [f for f in glob.glob(os.path.join(ROOT, "rosters", "**", "*.md"), recursive=True)
                     if os.path.basename(f) != "README.md"]
    for f in sorted(files):
        n = process(f, dry="--dry" in sys.argv)
        print(f"{n:3d} habilidades  {os.path.relpath(f, ROOT)}")


if __name__ == "__main__":
    main()
