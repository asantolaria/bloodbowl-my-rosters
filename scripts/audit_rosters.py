"""Auditoría: rosters vs source/teams (cupos CTD, costes, tabla detectada)."""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAP = {
    "union-elfica": "union-elfica",
    "skavens": "skavens",
    "orcos-negros": "orcos-negros",
    "nobleza-imperial": "nobleza-imperial",
    "elegidos-del-caos": "elegidos-del-caos",
    "hombres-lagarto": "hombres-lagarto",
    "no-muertos": "no-muertos",
    "humanos": "humanos",
    "altos-elfos": "altos-elfos",
    "renegados-del-caos": "renegados-del-caos",
    "vampiros": "vampiros",
    "ogros": "ogros",
    "gnomos": "gnomos",
    "halflings": "halflings",
    "goblins": "goblins",
    "snotlings": "snotlings",
    "khorne": "khorne",
    "enanos-del-caos": "enanos-del-caos",
    "bretonia": "bretonia",
    "nurgle": "nurgle",
    "reyes-funerarios": "reyes-funerarios",
    "slann": "slann",
    "enanos": "enanos",
    "nigromantes": "nigromantes",
    "nordicos": "nordicos",
    "elfos-oscuros": "elfos-oscuros",
    "habitantes-inframundo": "habitantes-inframundo",
    "orcos": "orcos",
    "amazonas": "amazonas",
    "alianza-viejo-mundo": "alianza-viejo-mundo",
    "elfos-silvanos": "elfos-silvanos",
}

# Variantes de nombre (roster EN / typo) → también probadas contra claves de fuente
POS_ALIASES: list[tuple[str, str]] = [
    ("ogre", "ogro"),
    ("ogro", "ogre"),
    ("troll entrenado", "troll"),
    ("forest troll", "forest troll"),
    ("bloater", "bloater"),
    ("bloaters", "bloater"),
    ("pestigor", "pestigor"),
    ("rotter", "rotter"),
    ("werewolf", "hombre lobo"),
    ("hombre lobo", "werewolf"),
    ("treeman", "hombre árbol"),
    ("orco negro", "black orc"),
]

# Tokens demasiado genéricos para decidir coste solo por solapamiento
GENERIC_TOKENS = frozenset(
    {
        "elfo",
        "elfos",
        "alto",
        "altos",
        "oscuro",
        "oscuros",
        "silvano",
        "silvanos",
        "humano",
        "humanos",
        "enano",
        "enanos",
        "orco",
        "orcos",
        "gnomo",
        "gnomos",
        "goblin",
        "goblins",
        "skaven",
        "skavens",
        "guerrero",
        "guerreros",
        "del",
        "los",
        "las",
        "reyes",
        "funerarios",
        "caballero",
        "caballeros",
        "marauder",
        "nacidos",
        "sangre",
        "elfica",
        "unión",
        "union",
    }
)

def team_label_expansions(team: str, pname: str) -> list[str]:
    """Sinónimos / acortados usados en rosters frente al nombre largo en la lista de equipo."""
    n = norm(pname)
    out: list[str] = []
    if team == "altos-elfos":
        if n == "blitzer":
            out.append("alto elfo white lion blitzer")
        if n == "catcher":
            out.append("alto elfo dragon warrior")
        if n == "thrower":
            out.append("alto elfo phoenix prince thrower")
    if team == "khorne":
        if "marauder" in n and ("línea" in n or "linea" in n):
            out.append("líneas marauder nacidos de la sangre")
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower().strip())


def roster_pos_variants(pname: str, team: str = "") -> list[str]:
    n = norm(pname)
    if not n or n == "____":
        return []
    out = [n]
    for a, b in POS_ALIASES:
        if a in n:
            out.append(n.replace(a, b))
    out.extend(team_label_expansions(team, pname))
    return list(dict.fromkeys(out))


def _significant_tokens(s: str) -> set[str]:
    return set(re.findall(r"[a-záéíóúñ]{3,}", norm(s)))


def _non_generic_overlap(v: str, lk: str) -> set[str]:
    return _significant_tokens(v) & _significant_tokens(lk) - GENERIC_TOKENS


def position_keys_match(pname: str, lkn: str) -> bool:
    """Misma heurística que cupos: ¿esta fila de roster corresponde a esta posición de lista?"""
    pname = norm(pname)
    lkn = norm(lkn)
    if not pname or not lkn:
        return False
    if lkn in pname or pname in lkn:
        return True
    pt = set(re.findall(r"[a-záéíóúñ]+", pname))
    lt = set(re.findall(r"[a-záéíóúñ]+", lkn))
    if not pt or not lt or not (pt & lt):
        return False
    if "línea" in pname and "línea" in lkn:
        return True
    if "elfo" in pname and "elfo" in lkn:
        return True
    if "guerrero" in pname and "guerrero" in lkn:
        return True
    if "humano" in pname and "humano" in lkn:
        return True
    if "enano" in pname and "enano" in lkn:
        return True
    if "orco" in pname and "orco" in lkn:
        return True
    if "gnomo" in pname and "gnomo" in lkn:
        return True
    if "goblin" in pname and "goblin" in lkn:
        return True
    if "skaven" in pname and "skaven" in lkn:
        return True
    if "marauder" in pname and "marauder" in lkn:
        return True
    if "khorngor" in pname and "khorngor" in lkn:
        return True
    if "bloodseeker" in pname and "bloodseeker" in lkn:
        return True
    if "bloodspawn" in pname and "bloodspawn" in lkn:
        return True
    return False


def team_table_prefix(text: str) -> str:
    if "## Descripción" in text:
        return text.split("## Descripción", 1)[0]
    return text[:12000]


def parse_limits(text: str) -> dict[str, int]:
    limits: dict[str, int] = {}
    pre = team_table_prefix(text)
    for m in re.finditer(r"\|\s*0-(\d+)\s*\|\s*([^|]+)\|", pre):
        mx = int(m.group(1))
        pos = norm(re.sub(r"\*+", "", m.group(2)).strip())
        if pos and not pos.startswith("elegir"):
            limits[pos] = mx
    return limits


def parse_team_position_costs(text: str) -> list[tuple[str, int]]:
    """Filas | 0-N | Posición | XXk | del listado de equipo."""
    pre = team_table_prefix(text)
    rows: list[tuple[str, int]] = []
    for m in re.finditer(
        r"\|\s*0-\d+\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*k\b",
        pre,
        re.IGNORECASE,
    ):
        pos = norm(re.sub(r"\*+", "", m.group(1)).strip())
        if not pos or "elegir" in pos:
            continue
        cost = int(m.group(2)) * 1000
        rows.append((pos, cost))
    return rows


def parse_cost_gp(cell: str) -> int | None:
    s = cell.strip().lower().replace(" ", "").replace("gp", "")
    if not s:
        return None
    if s.endswith("k"):
        num = s[:-1].replace(",", ".")
        try:
            v = float(num)
            return int(round(v * 1000))
        except ValueError:
            return None
    digits = re.sub(r"\D", "", s)
    if digits:
        return int(digits)
    return None


def roster_table_rows(content: str) -> list[tuple[str, str, int | None]]:
    """
    Primera tabla con cabecera Posición + Coste.
    Devuelve (posición cruda, posición normalizada, coste_gp o None).
    """
    rows: list[tuple[str, str, int | None]] = []
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and "Posición" in line and "Coste" in line:
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                if re.match(r"^\|\s*---", lines[i]):
                    i += 1
                    continue
                parts = [p.strip() for p in lines[i].split("|")]
                if len(parts) >= 6:
                    pos_raw = parts[3]
                    cost_cell = parts[4]
                    if pos_raw and pos_raw not in ("Posición", "Nombre", "____"):
                        rows.append((pos_raw, norm(pos_raw), parse_cost_gp(cost_cell)))
                i += 1
            break
        i += 1
    return rows


def match_score(variant: str, lk: str) -> int:
    """Puntuación de emparejamiento roster↔lista; 0 = no corresponde."""
    lv, vv = norm(lk), norm(variant)
    if not vv or not lv:
        return 0
    if lv == vv:
        return 1_000_000
    if vv in lv or lv in vv:
        return 500_000 + min(len(lv), len(vv))
    nog = _non_generic_overlap(variant, lk)
    if nog:
        return 10_000 + 100 * len(nog) + min(len(lv), len(vv))
    return 0


def resolve_expected_cost(
    pname: str, team: str, source_rows: list[tuple[str, int]]
) -> tuple[str | None, str, set[int]]:
    """
    Devuelve (clave_fuente_ganadora, estado, costes).
    estado: ok | none | ambiguous | mismatch_internal
    """
    variants = roster_pos_variants(pname, team)
    scored: list[tuple[int, str, int]] = []
    for lk, c in source_rows:
        ms = max((match_score(v, lk) for v in variants), default=0)
        if ms > 0:
            scored.append((ms, lk, c))
    if not scored:
        return None, "none", set()
    best = max(t[0] for t in scored)
    top = [(lk, c) for s, lk, c in scored if s == best]
    costs = {c for _, c in top}
    if len(costs) == 1:
        return top[0][0], "ok", costs
    return None, "ambiguous", costs


def count_vs_limits(cnt: Counter, limits: dict[str, int], team: str) -> list[str]:
    problems: list[str] = []
    for pname, c in cnt.items():
        if "scrappa" in pname:
            continue
        best = None
        bestk = None
        for lk, mx in limits.items():
            if any(position_keys_match(v, lk) for v in roster_pos_variants(pname, team)):
                best = mx
                bestk = lk
                break
        if best is not None and c > best:
            problems.append(f"[CUPO] {pname}: {c} > max {best} ({bestk})")
    return problems


def audit_file(
    fp: str,
    team: str,
    source_text: str,
    content: str,
    check_costs: bool,
) -> list[str]:
    issues: list[str] = []
    limits = parse_limits(source_text)
    source_cost_rows = parse_team_position_costs(source_text)
    table = roster_table_rows(content)

    if not table:
        head = content[:3000]
        if "PLANTILLA" in head and "EuroBowl" in head:
            return ["[SKIP] plantilla EuroBowl sin tabla Posición+Coste (esperado)"]
        issues.append("[TABLA] sin tabla de alineación (cabecera Posición + Coste)")
        return issues

    pos_list = [r[1] for r in table]
    cnt = Counter(pos_list)
    issues.extend(count_vs_limits(cnt, limits, team))

    if not check_costs:
        return issues
    if not source_cost_rows:
        issues.append("[FUENTE] sin filas CTD/coste parseables en source/teams; omito coste por fila")
        return issues

    for pos_raw, pos_norm, cost_gp in table:
        if "scrappa" in pos_norm:
            continue
        if cost_gp is None:
            issues.append(f"[COSTE] no parseable: {pos_raw!r}")
            continue
        _lk, st, expected = resolve_expected_cost(pos_raw, team, source_cost_rows)
        if st == "none":
            issues.append(f"[FUENTE] sin match en lista de equipo: {pos_raw!r}")
        elif st == "ambiguous":
            ks = sorted(expected)
            issues.append(
                f"[AMBIGUO] {pos_raw!r}: empate entre posiciones de fuente con costes distintos {ks}"
            )
        else:
            (exp,) = tuple(expected)
            if cost_gp != exp:
                issues.append(
                    f"[COSTE] {pos_raw!r}: roster {cost_gp // 1000}k vs fuente {exp // 1000}k"
                )
    return issues


def main() -> None:
    ap = argparse.ArgumentParser(description="Auditar rosters vs source/teams")
    ap.add_argument(
        "--no-costs",
        action="store_true",
        help="solo cupos y tabla, no comparar coste por fila",
    )
    ap.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="incluye mensajes [SKIP] de plantillas EuroBowl sin alineación",
    )
    args = ap.parse_args()
    check_costs = not args.no_costs

    all_issues: list[tuple[str, str]] = []
    for fp in sorted(glob.glob(os.path.join(ROOT, "rosters", "**", "*.md"), recursive=True)):
        if "README" in os.path.basename(fp):
            continue
        base = os.path.basename(fp)
        team = None
        for k in sorted(MAP.keys(), key=len, reverse=True):
            if k in base:
                team = MAP[k]
                break
        if not team:
            all_issues.append((fp, "[MAPEO] sin mapeo de equipo en script"))
            continue
        sp = os.path.join(ROOT, "source", "teams", f"{team}.md")
        if not os.path.isfile(sp):
            all_issues.append((fp, f"[MAPEO] no existe {sp}"))
            continue
        source_text = open(sp, encoding="utf-8").read()
        content = open(fp, encoding="utf-8").read()
        for msg in audit_file(fp, team, source_text, content, check_costs):
            all_issues.append((fp, msg))

    for fp, msg in all_issues:
        if not args.verbose and msg.startswith("[SKIP]"):
            continue
        print(f"{os.path.relpath(fp, ROOT)}\t{msg}")


if __name__ == "__main__":
    main()
