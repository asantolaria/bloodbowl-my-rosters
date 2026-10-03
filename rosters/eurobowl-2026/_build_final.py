"""Genera y valida los rosters EuroBowl 2026 (reglamento FINAL, 7 tiers).

Uso:
    python3 rosters/eurobowl-2026/_build_final.py            # valida todos los equipos
    python3 rosters/eurobowl-2026/_build_final.py --check X  # valida solo el slug X
    python3 rosters/eurobowl-2026/_build_final.py --write    # valida y escribe los .md

Los datos de cada lista están en `_final_data.py`. Posiciones, costes, Pri/Sec y rerolls
se leen de `source/teams/`; categoría y élite de cada habilidad, de `source/habilidades/`.
Reglas: `source/tiers/eurobowl-2026-final.md`.
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

# Tier FINAL: (presupuesto equipo, Skill Gold, Flowing Funds) en k
FINAL = {1: (1070, 120, 10), 2: (1070, 140, 20), 3: (1080, 160, 30), 4: (1100, 190, 30),
         5: (1120, 220, 30), 6: (1140, 240, 40), 7: (1150, 270, 50)}
TIER = {
    "alianza-viejo-mundo": 1, "orcos": 1, "elfos-silvanos": 1,
    "amazonas": 2, "skavens": 2, "habitantes-inframundo": 2,
    "elfos-oscuros": 3, "altos-elfos": 3, "humanos": 3, "hombres-lagarto": 3, "no-muertos": 3, "vampiros": 3,
    "nigromantes": 4, "nordicos": 4, "nurgle": 4, "slann": 4, "reyes-funerarios": 4,
    "elegidos-del-caos": 5, "enanos-del-caos": 5, "enanos": 5, "union-elfica": 5, "nobleza-imperial": 5, "snotlings": 5,
    "orcos-negros": 6, "bretonia": 6, "renegados-del-caos": 6, "gnomos": 6, "goblins": 6, "halflings": 6, "khorne": 6,
    "ogros": 7,
}
# Recargo en Skill Gold por estrella: tier -> (Veteran, Legend); tiers 1-4 no permiten estrellas
STAR_TAX = {5: (50, 100), 6: (40, 80), 7: (40, 80)}  # lámina FINAL
# Incentivos: nombre -> (coste, coste con Sobornos y corrupción)
INDUC = {
    "Sobornos": (100, 50),
    "Amañafaltas": (120, 80),
    "Novatos embravecidos": (150, 150),
    "Mascota del equipo": (25, 25),
    "Barriles de Estrella Blitzer": (50, 50),
    "Chef Maestro Halfling": (300, 100),
    "Apotecarios errantes": (100, 100),
}
CAT_FILES = {"general": "G", "agilidad": "A", "fuerza": "F", "pase": "P", "triquinuelas": "D", "mutaciones": "M"}


def skill_catalog():
    cat = {}
    for fn, letter in CAT_FILES.items():
        for line in open(os.path.join(REPO, "source", "habilidades", fn + ".md"), encoding="utf-8"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0] and not c[0].startswith("-") and "(ES)" not in c[0] and c[0] not in ("Nombre", "Habilidad"):
                cat[c[0].replace("**", "")] = (letter, "Elite" in line or "élite" in c[2].lower())
    return cat


SK = skill_catalog()


def team_sheet(slug):
    t = open(os.path.join(REPO, "source", "teams", slug + ".md"), encoding="utf-8").read()
    rows = {}
    for line in t.splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 11 and re.match(r"0-\d+", c[0]):
            rows[c[1]] = dict(max=int(c[0][2:]), cost=int(c[2].rstrip("k")), ma=c[3], st=c[4], ag=c[5], pa=c[6],
                              ar=c[7], sk=c[8], pri=c[9], sec=c[10])
    rr = int(re.search(r"Rerolls:\*\*\s*(\d+)k", t).group(1))
    apo = not re.search(r"Apotecario:\*\*\s*No", t)
    sac = bool(re.search(r"Sobornos? y [Cc]orrupción", t))
    title = t.splitlines()[0].lstrip("# ").split(" — ")[0]
    thimble = "Copa Dedal Halfling" in t
    return rows, rr, apo, sac, title, thimble


def advance_cost(skills, pos, who):
    if not skills:
        return 0, ""
    for s in skills:
        if s not in SK:
            raise ValueError(f"{who}: habilidad desconocida '{s}' (usa el nombre de source/habilidades/)")
    cats = [SK[s] for s in skills]
    prim = [c in pos["pri"] for c, _ in cats]
    if len(skills) == 1:
        (c, e), p = cats[0], prim[0]
        if p:
            return (30 if e else 20), "Primaria élite" if e else "Primaria"
        if c not in pos["sec"]:
            raise ValueError(f"{who}: {skills[0]} ({c}) no es Pri ni Sec ({pos['pri']}/{pos['sec']})")
        return (50 if e else 40), "Secundaria élite" if e else "Secundaria"
    if len(skills) == 2 and all(prim):
        return {0: 50, 1: 60, 2: 70}[sum(e for _, e in cats)], "Stack"
    raise ValueError(f"{who}: avance inválido {skills} (stack = 2 primarias)")


def build(team):
    slug = team["slug"]
    tier = TIER[slug]
    rows, rr, apo_ok, sac, title, thimble = team_sheet(slug)
    b, sg, ff = FINAL[tier]
    errs = []
    players, count = [], {}
    for name, n, skills in team["players"]:
        if name not in rows:
            raise ValueError(f"{slug}: posición '{name}' no está en la ficha: {list(rows)}")
        count[name] = count.get(name, 0) + n
        players += [(name, rows[name], list(skills))] * n
    for k, v in count.items():
        if v > rows[k]["max"]:
            errs.append(f"{k}: {v} > 0-{rows[k]['max']}")
    stars = team.get("stars", [])
    if stars:
        if tier not in STAR_TAX:
            errs.append("estrellas prohibidas en tiers 1-4")
        kinds = [k for _, _, k in stars]
        if not (kinds.count("Legend") == 1 and len(kinds) == 1 or (kinds.count("Veteran") == len(kinds) and len(kinds) <= 2)):
            errs.append("hasta dos Veterans o una Legend")
    if team.get("apo") and not apo_ok:
        errs.append("el equipo no puede contratar apotecario")
    psum = sum(p[1]["cost"] for p in players)
    star_cost = sum(c for _, c, _ in stars)
    # Precio reducido: Sobornos y corrupción (Sobornos, Amañafaltas) o Copa Dedal Halfling (Chef)
    ind = [(k, n, INDUC[k][1 if (thimble if k == "Chef Maestro Halfling" else sac) else 0]) for k, n in team.get("induc", [])]
    staff = team["rr"] * rr + (50 if team.get("apo") else 0) + 10 * team.get("ac", 0) + 10 * team.get("cheer", 0)
    budget_used = psum + star_cost + staff + sum(n * c for _, n, c in ind)
    adv = []
    for i, p in enumerate(players):
        cost, kind = advance_cost(p[2], p[1], f"{slug} #{i + 1} {p[0]}")
        adv.append((i + 1, p, cost, kind))
    tax = sum(STAR_TAX.get(tier, (0, 0))[0 if k == "Veteran" else 1] for _, _, k in stars)
    sg_used = sum(a[2] for a in adv) + tax
    nsec = sum(1 for a in adv if a[3].startswith("Secundaria"))
    nstk = sum(1 for a in adv if a[3] == "Stack")
    ff_team, ff_sg = max(0, budget_used - b), max(0, sg_used - sg)
    if ff_team + ff_sg > ff:
        errs.append(f"Flowing {ff_team}+{ff_sg} > {ff} (equipo {budget_used}/{b}, SG {sg_used}/{sg})")
    if nsec > 3 or nstk > 3:
        errs.append(f"secundarias {nsec}, stacks {nstk} (máx. 3 cada uno)")
    if stars and (nsec or nstk):
        errs.append("con estrellas no se permiten secundarias ni stacks")
    if len(players) + len(stars) < 11:
        errs.append("menos de 11 jugadores")
    insig = sum(1 for p in players if "Insignificante" in p[1]["sk"])
    if insig > len(players) + len(stars) - insig:
        errs.append("más Insignificantes que no Insignificantes")
    return dict(slug=slug, title=title, tier=tier, players=players, adv=adv, rr=rr, sac=sac, ind=ind, psum=psum,
                stars=stars, tax=tax, budget_used=budget_used, sg_used=sg_used, ff_team=ff_team, ff_sg=ff_sg,
                b=b, sg=sg, ff=ff, nsec=nsec, nstk=nstk, errs=errs)


def gp(k):
    return f"{k * 1000:,}".replace(",", ".")


def emit(team, r):
    slug, tier, name = r["slug"], r["tier"], team.get("name", r["title"])
    L = [f"# {name} — EuroBowl 2026 FINAL (Tier {tier})", ""]
    img = team.get("img")
    if img:
        L += [f"![{name}](../../source/images/equipos/{img})", ""]
    L += [f"> **#euro26 · reglamento [FINAL](../../source/tiers/eurobowl-2026-final.md).** Posiciones y costes: [`source/teams/{slug}.md`](../../source/teams/{slug}.md). Generado con `_build_final.py`.", ">",
          f"> **Origen de la build:** {team['fuente']}", ">",
          "> **Estado competitivo:** válida en cifras; revisión táctica propia pendiente.", ""]
    if team.get("nota"):
        L += [f"!!! note \"Nota\"", f"    {team['nota']}", ""]
    L += ["## Presupuesto", "", "| Concepto | Disponible | Usado |", "|----------|-----------|-------|",
          f"| **Presupuesto de equipo** | {gp(r['b'])} M.O. | {gp(r['budget_used'])} M.O. |",
          f"| **Skill Gold** | {gp(r['sg'])} M.O. | {gp(r['sg_used'])} M.O. |",
          f"| **Flowing Funds** | {gp(r['ff'])} M.O. | {gp(r['ff_team'])} → equipo · {gp(r['ff_sg'])} → Skill Gold |", "",
          "## Alineación", "", "*Rellenar nombres. Habilidades compradas con Skill Gold en **negrita**.*", "",
          "| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades | Skill Gold |",
          "|----|--------|----------|-------|----|----|----|----|----|-------------|------------|"]
    for i, (pos, row, sk), cost, kind in r["adv"]:
        extra = ", ".join(f"**{s}**" for s in sk)
        base = "" if row["sk"] in ("–", "-", "") else row["sk"]
        skills = ", ".join(x for x in (base, extra) if x) or "–"
        L.append(f"| {i} | ____ | {pos} | {row['cost']}k | {row['ma']} | {row['st']} | {row['ag']} | {row['pa']} | {row['ar']} | {skills} | {kind + ' ' + str(cost) + 'k' if cost else '–'} |")
    for j, (sname, scost, kind) in enumerate(r["stars"], len(r["adv"]) + 1):
        L.append(f"| {j} | {sname} | Jugador estrella ({kind}) | {scost}k | | | | | | Ver [jugadores estrella](../../source/jugadores-estrella/README.md) | Recargo {STAR_TAX[tier][0 if kind == 'Veteran' else 1]}k |")
    L += ["", f"**Total jugadores:** {len(r['players']) + len(r['stars'])}", "", "| Concepto | Coste |", "|----------|--------|",
          f"| Jugadores | {gp(r['psum'])} |"]
    if r["stars"]:
        L.append(f"| Jugadores estrella | {gp(sum(c for _, c, _ in r['stars']))} |")
    L += [f"| Segundas oportunidades ({team['rr']} × {gp(r['rr'])}) | {gp(team['rr'] * r['rr'])} |",
          f"| Apotecario | {'50.000' if team.get('apo') else 'No'} |"]
    if team.get("ac"):
        L.append(f"| Ayudantes del entrenador ({team['ac']} × 10.000) | {gp(10 * team['ac'])} |")
    if team.get("cheer"):
        L.append(f"| Animadoras ({team['cheer']} × 10.000) | {gp(10 * team['cheer'])} |")
    for k, n, c in r["ind"]:
        L.append(f"| Incentivo: {k} ({n} × {gp(c)}{' (precio reducido por regla del equipo)' if INDUC[k][0] != c else ''}) | {gp(n * c)} |")
    L += [f"| **Total** | **{gp(r['budget_used'])}** |", "", "## Skill Gold", "",
          f"Un avance por jugador. Secundarias: **{r['nsec']}/3** · Stacks: **{r['nstk']}/3**.", "",
          "| Jugador (Nº) | Avance | Tipo | Coste |", "|--------------|--------|------|-------|"]
    for i, (pos, row, sk), cost, kind in r["adv"]:
        if cost:
            L.append(f"| {i} {pos} | {' + '.join(sk)} | {kind} | {gp(cost)} |")
    if r["tax"]:
        L.append(f"| Estrellas | Recargo | — | {gp(r['tax'])} |")
    L += [f"| **Total** | | | **{gp(r['sg_used'])}** |", ""]
    if team.get("tactica"):
        L += ["## Notas de la build", ""] + [f"- {t}" for t in team["tactica"]] + [""]
    return "\n".join(L)


def main():
    from _final_data import TEAMS
    only = sys.argv[sys.argv.index("--check") + 1] if "--check" in sys.argv else None
    bad = 0
    for t in TEAMS:
        if only and t["slug"] != only:
            continue
        try:
            r = build(t)
        except ValueError as e:
            print(f"ERROR {e}")
            bad += 1
            continue
        ok = "OK " if not r["errs"] else "MAL"
        print(f"{ok} {t['slug']:22} T{r['tier']} equipo {r['budget_used']}/{r['b']} SG {r['sg_used']}/{r['sg']} "
              f"FF {r['ff_team']}+{r['ff_sg']}/{r['ff']} sec {r['nsec']} stk {r['nstk']} jug {len(r['players']) + len(r['stars'])}"
              + ("" if not r["errs"] else "  ← " + "; ".join(r["errs"])))
        bad += bool(r["errs"])
        if "--write" in sys.argv and not r["errs"]:
            p = os.path.join(HERE, f"eurobowl-26-{t['slug']}-tier{r['tier']}.md")
            open(p, "w", encoding="utf-8", newline="\n").write(emit(t, r))
            sys.path.insert(0, os.path.join(REPO, "scripts"))
            import habilidades_en_rosters  # sección «Habilidades del roster»
            habilidades_en_rosters.process(p)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
