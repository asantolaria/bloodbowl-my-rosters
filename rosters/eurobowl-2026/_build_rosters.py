# Genera rosters EuroBowl 2026. Ejecutar: python rosters/eurobowl-2026/_build_rosters.py
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

EURO = {
    1: (1060, 120, 10),
    2: (1070, 140, 20),
    3: (1080, 160, 30),
    4: (1100, 190, 30),
    5: (1120, 220, 30),
    6: (1140, 240, 40),
}

# Equipos sin apotecario en lista oficial
NO_APO = frozenset({"no-muertos", "nigromantes", "reyes-funerarios"})


def solve_extras(tier: int, psum: int, rr: int, slug: str) -> tuple[int, bool, int, int] | None:
    """Devuelve (n_rr, apo, n_fans, flowing_gp_resto) o None si no hay solución."""
    target = EURO[tier][0] * 1000
    player = psum * 1000
    apo_opts = [False] if slug in NO_APO else [True, False]
    for n_rr in range(5, -1, -1):
        for apo in apo_opts:
            fixed = n_rr * rr * 1000 + (50000 if apo else 0)
            rem = target - player - fixed
            if rem >= 0:
                return (n_rr, apo, rem // 10000, rem % 10000)
    return None


def row_md(i: int, r: tuple) -> str:
    pos, cost, ma, st, ag, pa, ar, sk = r
    pa = pa if pa != "–" else "—"
    return f"| {i} | ____ | {pos} | {cost}k | {ma} | {st} | {ag} | {pa} | {ar} | {sk} |"


def emit(team: dict) -> str:
    slug = team["slug"]
    name = team["name"]
    tier = team["tier"]
    img_fn = team.get("img_file", f'{team["img"]}.webp')
    rr = team["rr"]
    rows = team["rows"]
    psum = sum(r[1] for r in rows)
    sol = solve_extras(tier, psum, rr, slug)
    if sol is None:
        raise SystemExit(f"No hay combinación reroll/apo/fans para {slug} (jugadores {psum}k)")
    n_rr, apo, n_fan, rflow = sol
    b, sk, fl = EURO[tier]
    extra_rr = n_rr * rr * 1000
    extra_apo = 50000 if apo else 0
    extra_fan = n_fan * 10000
    total_gp = psum * 1000 + extra_rr + extra_apo + extra_fan + rflow
    total_k = total_gp // 1000

    lines = [
        f"# {name} — EuroBowl 2026 (Tier {tier}, Team Budget {b}k)",
        "",
        f"![{name}](../../source/images/equipos/{img_fn})",
        "",
        f"> **#euro26** — [EuroBowl 2026](../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Posiciones y costes: [`source/teams/{slug}.md`](../../source/teams/{slug}.md).",
        "",
        "> **Estado competitivo:** presupuesto EuroBowl válido en cifras; **sin revisión meta**. Repaso táctico pendiente — [README `eurobowl-2026`](README.md) · tag `eurobowl-2026-wip-competitive`.",
        "",
        "## Presupuesto EuroBowl",
        "",
        "| Concepto | Valor |",
        "|----------|--------|",
        f"| **Tier** | {tier} |",
        f"| **Team Budget (base)** | {b}.000 gp |",
        f"| **Skill Gold (pool)** | {sk}.000 gp |",
        f"| **Flowing Funds (máx.)** | {fl}.000 gp |",
        "",
        f"*Desglose de equipo = **{total_k}k** gp (debe coincidir con Team Budget base + la parte de Flowing que asignes al equipo). Resto de Flowing puede ir a Skill Gold.*",
        "",
        "## Alineación (gasto de presupuesto de equipo)",
        "",
        "*Sin avances de Skill Gold. Rellenar nombres. Texto de habilidades resumido.*",
        "",
        "| Nº | Nombre | Posición | Coste | MA | ST | AG | PA | AR | Habilidades |",
        "|----|--------|----------|-------|----|----|----|----|----|-------------|",
    ]
    for i, r in enumerate(rows, 1):
        lines.append(row_md(i, r))
    npl = len(rows)
    lines.extend(
        [
            "",
            f"**Total jugadores:** {npl} | **Presupuesto equipo usado:** {total_k}k gp",
            "",
            "| Concepto | Coste |",
            "|----------|--------|",
            f"| Jugadores (total {psum}k) | {psum * 1000:,} |".replace(",", "."),
            f"| Rerolls ({n_rr} × {rr}.000) | {extra_rr:,} |".replace(",", "."),
        ]
    )
    if apo:
        lines.append("| Apotecario | 50.000 |")
    else:
        lines.append("| Apotecario | No (lista del equipo) |")
    if n_fan:
        lines.append(f"| Fans dedicados ({n_fan} × 10.000) | {extra_fan:,} |".replace(",", "."))
    if rflow:
        lines.append(
            f"| Flowing Funds → presupuesto equipo (resto no múltiplo de 10k) | {rflow:,} |".replace(
                ",", "."
            )
        )
    lines.append(f"| **Total** | **{total_gp:,}** |".replace(",", "."))
    lines.extend(
        [
            "",
            "## Skill Gold — avances (ejemplo editable)",
            "",
            "Cada jugador: **un solo bloque** de avance. Máx. **3** Secondary y **3** Stack en todo el equipo. Costes: ver tabla en [`eurobowl-2026.md`](../../source/tiers/eurobowl-2026.md).",
            "",
            "| Jugador (Nº) | Tipo | Coste (Skill Gold) |",
            "|--------------|------|---------------------|",
            "| _pendiente_ | 1 primaria no élite | 20.000 |",
            "",
            f"**Pool Skill Gold base:** {sk}.000 gp (+ Flowing si lo asignas).",
            "",
            "## Estrellas (Tiers 1–4)",
            "",
            "Sin Veterans ni Legends. Con estrella (tier 5–6): no avances Secondary ni Stack en jugadores de plantilla.",
            "",
            "## Inducements",
            "",
            "Solo los listados como permitidos en `eurobowl-2026.md`.",
            "",
        ]
    )
    return "\n".join(lines)


TEAMS: list[dict] = [
    {
        "slug": "elfos-silvanos",
        "name": "Elfos Silvanos",
        "tier": 1,
        "img": "elfos-silvanos",
        "rr": 50,
        "rows": [
            ("Loren Forest Treeman", 120, 2, 6, "5+", "5+", "11+", "GM, MF, …"),
            ("Wardancer", 130, 8, 3, "2+", "3+", "8+", "Placar, Esquivar, Saltar"),
            ("Elfo Silvano Thrower", 85, 7, 3, "2+", "2+", "8+", "Pasar, Proteger el cuero"),
            ("Elfo Silvano Thrower", 85, 7, 3, "2+", "2+", "8+", "Pasar, Proteger el cuero"),
            ("Elfo Silvano Catcher", 90, 8, 2, "2+", "3+", "8+", "Atrapar, Esprintar, Esquivar"),
            ("Elfo Silvano Catcher", 90, 8, 2, "2+", "3+", "8+", "Atrapar, Esprintar, Esquivar"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
            ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "–"),
        ],
    },
    {
        "slug": "alianza-viejo-mundo",
        "name": "Alianza del Viejo Mundo",
        "tier": 1,
        "img": "alianza-viejo-mundo",
        "rr": 70,
        "rows": [
            ("Hombre Árbol", 120, 2, 6, "5+", "5+", "11+", "GM, …"),
            ("Ogro", 140, 5, 5, "4+", "5+", "10+", "Estúpido, GM, …"),
            ("Enano Blocker", 70, 4, 3, "4+", "5+", "10+", "Cabeza dura, Placar, …"),
            ("Enano Blocker", 70, 4, 3, "4+", "5+", "10+", "Cabeza dura, Placar, …"),
            ("Humano Blitzer", 85, 7, 3, "3+", "4+", "9+", "Placaje def., Placar"),
            ("Humano Blitzer", 85, 7, 3, "3+", "4+", "9+", "Placaje def., Placar"),
            ("Humano Thrower", 75, 6, 3, "3+", "3+", "9+", "Manos seguras, Pasar"),
            ("Humano Catcher", 75, 8, 3, "3+", "4+", "8+", "Atrapar, Esquivar"),
            ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "–"),
            ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "–"),
            ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "–"),
            ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "–"),
            ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "–"),
        ],
    },
    {
        "slug": "amazonas",
        "name": "Amazonas",
        "tier": 2,
        "img": "amazonas",
        "rr": 60,
        "rows": [
            ("Guerrera Jaguar Blocker", 110, 6, 4, "3+", "4+", "9+", "Esquivar, Romper defensas"),
            ("Guerrera Jaguar Blocker", 110, 6, 4, "3+", "4+", "9+", "Esquivar, Romper defensas"),
            ("Guerrera Piraña Blitzer", 90, 7, 3, "3+", "4+", "8+", "Hit and Run, …"),
            ("Guerrera Piraña Blitzer", 90, 7, 3, "3+", "4+", "8+", "Hit and Run, …"),
            ("Guerrera Pitón Thrower", 80, 6, 3, "3+", "3+", "8+", "Pasar, Pase seguro, …"),
            ("Guerrera Pitón Thrower", 80, 6, 3, "3+", "3+", "8+", "Pasar, Pase seguro, …"),
            *[
                ("Guerrera Águila Línea", 50, 6, 3, "3+", "4+", "8+", "Esquivar")
                for _ in range(6)
            ],
        ],
    },
    {
        "slug": "orcos",
        "name": "Orcos",
        "tier": 2,
        "img": "orcos",
        "rr": 60,
        "rows": [
            ("Troll", 115, 4, 5, "5+", "5+", "10+", "Hambriento, GM, …"),
            ("Big Un Blocker", 95, 5, 4, "4+", "6+", "10+", "Cabeza dura, GM, …"),
            ("Big Un Blocker", 95, 5, 4, "4+", "6+", "10+", "Cabeza dura, GM, …"),
            ("Orco Blitzer", 85, 6, 3, "3+", "4+", "10+", "Abrirse paso, Placar"),
            ("Orco Blitzer", 85, 6, 3, "3+", "4+", "10+", "Abrirse paso, Placar"),
            ("Orco Lanzador", 75, 6, 3, "3+", "3+", "9+", "Pasar, Manos seguras"),
            ("Goblin", 40, 6, 2, "3+", "3+", "8+", "Esquivar, Escurridizo, …"),
            ("Goblin", 40, 6, 2, "3+", "3+", "8+", "Esquivar, Escurridizo, …"),
            *[
                ("Orco Línea", 50, 5, 3, "3+", "4+", "10+", "–")
                for _ in range(6)
            ],
        ],
    },
    {
        "slug": "no-muertos",
        "name": "No Muertos",
        "tier": 2,
        "img": "no-muertos",
        "rr": 70,
        "rows": [
            ("Momia", 125, 3, 5, "5+", "6+", "10+", "GM, Regeneración"),
            ("Caballero", 95, 6, 3, "3+", "5+", "9+", "Placar, Placaje def., …"),
            ("Caballero", 95, 6, 3, "3+", "5+", "9+", "Placar, Placaje def., …"),
            *[
                ("Necrófago", 75, 7, 3, "3+", "3+", "8+", "Esquivar, Regeneración")
                for _ in range(4)
            ],
            ("Esqueleto", 40, 5, 3, "4+", "6+", "8+", "Regeneración, Cabeza dura"),
            ("Esqueleto", 40, 5, 3, "4+", "6+", "8+", "Regeneración, Cabeza dura"),
            ("Zombie", 40, 4, 3, "4+", "6+", "9+", "Regeneración, Inestable, …"),
            ("Zombie", 40, 4, 3, "4+", "6+", "9+", "Regeneración, Inestable, …"),
        ],
    },
    {
        "slug": "skavens",
        "name": "Skavens",
        "tier": 2,
        "img": "skavens",
        "rr": 50,
        "rows": [
            ("Rata Ogro", 150, 6, 5, "4+", "–", "9+", "Ferocidad animal, …"),
            ("Blitzer", 90, 8, 3, "3+", "4+", "9+", "Placar, Robar balón"),
            ("Blitzer", 90, 8, 3, "3+", "4+", "9+", "Placar, Robar balón"),
            *[
                ("Gutter Runner", 85, 9, 2, "2+", "4+", "8+", "Apuñalar, Esquivar")
                for _ in range(4)
            ],
            ("Thrower", 80, 7, 3, "3+", "2+", "8+", "Manos seguras, Pasar"),
            *[
                ("Linemen", 50, 7, 3, "3+", "4+", "8+", "–")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "habitantes-inframundo",
        "name": "Habitantes del Inframundo",
        "tier": 2,
        "img": "habitantes-inframundo",
        "rr": 50,
        "rows": [
            ("Rata Ogro", 150, 6, 5, "4+", "–", "9+", "Ferocidad animal, …"),
            ("Blitzer", 90, 7, 3, "3+", "4+", "9+", "Placar, Robar balón"),
            ("Blitzer", 90, 7, 3, "3+", "4+", "9+", "Placar, Robar balón"),
            *[
                ("Gutter Runner", 85, 9, 2, "2+", "4+", "8+", "Apuñalar, Esquivar")
                for _ in range(2)
            ],
            ("Thrower", 80, 6, 3, "3+", "2+", "8+", "Manos seguras, Pasar"),
            ("Mutante", 85, 6, 3, "3+", "4+", "8+", "Mutación aleatoria"),
            *[
                ("Linemen", 50, 6, 3, "3+", "4+", "8+", "–")
                for _ in range(6)
            ],
        ],
    },
    {
        "slug": "elfos-oscuros",
        "name": "Elfos Oscuros",
        "tier": 3,
        "img": "elfos-oscuros",
        "rr": 50,
        "rows": [
            ("Elfo Oscuro Asesino", 90, 7, 3, "2+", "4+", "8+", "Apuñalar, Hit and Run, …"),
            *[
                ("Elfo Oscuro Blitzer", 105, 7, 3, "2+", "3+", "9+", "Placar")
                for _ in range(2)
            ],
            *[
                ("Elfo Oscuro Runner", 80, 7, 3, "2+", "3+", "8+", "Pase precipitado, …")
                for _ in range(2)
            ],
            *[
                ("Elfo Oscuro Línea", 65, 6, 3, "2+", "3+", "9+", "–")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "altos-elfos",
        "name": "Altos Elfos",
        "tier": 3,
        "img": "altos-elfos",
        "rr": 50,
        "rows": [
            *[
                ("White Lion Blitzer", 110, 7, 3, "2+", "3+", "9+", "Forcejear, Garras")
                for _ in range(2)
            ],
            ("Dragon Warrior", 110, 8, 3, "2+", "4+", "9+", "Mi balón, Equilibrio firme, Placar"),
            *[
                ("Phoenix Prince Thrower", 90, 6, 3, "2+", "2+", "9+", "Partenubes, Pasar, …")
                for _ in range(2)
            ],
            *[
                ("Alto Elfo Línea", 65, 6, 3, "2+", "3+", "9+", "–")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "humanos",
        "name": "Humanos",
        "tier": 3,
        "img": "humanos",
        "rr": 50,
        "rows": [
            ("Ogre", 140, 5, 5, "4+", "5+", "10+", "Estúpido, GM, …"),
            *[
                ("Blitzer", 85, 7, 3, "3+", "4+", "9+", "Placar, Placaje def.")
                for _ in range(3)
            ],
            *[
                ("Catcher", 75, 8, 3, "3+", "4+", "8+", "Atrapar, Esquivar")
                for _ in range(2)
            ],
            ("Thrower", 75, 6, 3, "3+", "3+", "9+", "Manos seguras, Pasar"),
            *[
                ("Línea", 50, 6, 3, "3+", "4+", "9+", "–")
                for _ in range(5)
            ],
        ],
    },
    {
        "slug": "hombres-lagarto",
        "name": "Hombres Lagarto",
        "tier": 3,
        "img": "hombres-lagarto",
        "rr": 70,
        "rows": [
            ("Kroxigor", 140, 6, 5, "5+", "6+", "10+", "Estúpido, GM, …"),
            *[
                ("Saurio", 90, 6, 4, "5+", "6+", "10+", "Imparable, Tembloroso")
                for _ in range(4)
            ],
            *[
                ("Eslizón Línea", 60, 8, 2, "3+", "4+", "8+", "Esquivar, Escurridizo")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "nigromantes",
        "name": "Nigromantes",
        "tier": 3,
        "img": "nigromantes",
        "rr": 70,
        "rows": [
            *[
                ("Flesh Golem", 110, 4, 4, "4+", "6+", "10+", "Cabeza dura, Inestable, …")
                for _ in range(2)
            ],
            *[
                ("Werewolf", 120, 8, 3, "3+", "3+", "9+", "Garras, Furia, …")
                for _ in range(2)
            ],
            *[
                ("Ghoul", 75, 7, 3, "3+", "3+", "8+", "Esquivar, Regeneración")
                for _ in range(2)
            ],
            *[
                ("Wraith", 85, 6, 3, "3+", "–", "9+", "Placar, …")
                for _ in range(2)
            ],
            *[
                ("Zombie Línea", 40, 4, 3, "4+", "6+", "9+", "Regeneración, …")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "nordicos",
        "name": "Nórdicos",
        "tier": 3,
        "img": "nordicos",
        "rr": 60,
        "rows": [
            *[
                ("Ulfwerener", 110, 6, 4, "3+", "4+", "9+", "Furia, Regeneración")
                for _ in range(2)
            ],
            *[
                ("Berserker", 90, 6, 3, "3+", "4+", "8+", "Furia, Placar")
                for _ in range(2)
            ],
            ("Runner", 80, 7, 3, "3+", "4+", "8+", "Esquivar, Esprintar"),
            ("Thrower", 75, 6, 3, "3+", "3+", "8+", "Pasar, Manos seguras"),
            *[
                ("Línea", 65, 6, 3, "3+", "4+", "9+", "–")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "elegidos-del-caos",
        "name": "Elegidos del Caos",
        "tier": 4,
        "img": "Chaos",
        "rr": 50,
        "rows": [
            ("Minotauro", 150, 5, 5, "4+", "6+", "9+", "Frenesí, Imparable, …"),
            *[
                ("Guerrero Caos", 100, 5, 4, "3+", "–", "10+", "Brazo armado")
                for _ in range(4)
            ],
            *[
                ("Beastman", 55, 6, 3, "3+", "–", "9+", "Cuernos, Cabeza dura")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "enanos",
        "name": "Enanos",
        "tier": 4,
        "img": "enanos",
        "rr": 60,
        "rows": [
            ("Apisonadora Enana", 170, 5, 7, "5+", "–", "11+", "Arma secreta, …"),
            ("MataTrols", 95, 5, 3, "4+", "5+", "9+", "Agallas, Furia, …"),
            *[
                ("Enano Blitzer", 100, 5, 3, "4+", "4+", "10+", "Placar, Placaje def., …")
                for _ in range(2)
            ],
            ("Enano Runner", 80, 6, 3, "3+", "4+", "9+", "Esprintar, Manos seguras, …"),
            *[
                ("Enano Línea", 70, 4, 3, "4+", "5+", "10+", "Placar, Romper defensas, …")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "nobleza-imperial",
        "name": "Nobleza Imperial",
        "tier": 4,
        "img": "nobleza-imperial",
        "rr": 50,
        "rows": [
            ("Ogre", 140, 5, 5, "4+", "5+", "10+", "Estúpido, GM, …"),
            *[
                ("Bodyguard", 85, 5, 3, "3+", "4+", "9+", "Mantenerse firme, Forcejeo")
                for _ in range(3)
            ],
            *[
                ("Noble Blitzer", 90, 7, 3, "3+", "4+", "9+", "Placar, Atrapar, …")
                for _ in range(2)
            ],
            ("Imperial Thrower", 75, 6, 3, "3+", "2+", "9+", "Pasar, …"),
            *[
                ("Retainer Línea", 45, 6, 3, "3+", "4+", "8+", "Zafarse")
                for _ in range(5)
            ],
        ],
    },
    {
        "slug": "nurgle",
        "name": "Nurgle",
        "tier": 4,
        "img": "nurgle",
        "rr": 60,
        "rows": [
            *[
                ("Bloaters", 115, 4, 4, "4+", "6+", "10+", "Cabeza dura, Distraer, …")
                for _ in range(4)
            ],
            *[
                ("Pestigor", 80, 6, 3, "3+", "4+", "9+", "Cuernos, GM, …")
                for _ in range(2)
            ],
            *[
                ("Rotter", 35, 5, 3, "4+", "6+", "9+", "Regeneración, …")
                for _ in range(6)
            ],
        ],
    },
    {
        "slug": "slann",
        "name": "Slann",
        "tier": 4,
        "img": "slann",
        "rr": 60,
        "rows": [
            ("Kroxigor", 140, 6, 5, "5+", "6+", "10+", "Cola prensil, GM, …"),
            *[
                ("Blitzer", 95, 7, 3, "2+", "4+", "9+", "Placar, Saltar, …")
                for _ in range(2)
            ],
            *[
                ("Catcher", 85, 8, 2, "2+", "4+", "8+", "Atrapar, Saltar, Esquivar")
                for _ in range(2)
            ],
            *[
                ("Linemen", 60, 7, 2, "2+", "4+", "8+", "Saltar, Esquivar")
                for _ in range(7)
            ],
        ],
    },
    {
        "slug": "reyes-funerarios",
        "name": "Reyes Funerarios",
        "tier": 4,
        "img": "reyes-funerarios",
        "rr": 70,
        "rows": [
            ("Momia de Reyes Funerarios", 110, 3, 5, "5+", "6+", "10+", "GM, …"),
            *[
                ("Blitzer de Reyes Funerarios", 90, 6, 3, "3+", "4+", "9+", "Placar, Regeneración")
                for _ in range(2)
            ],
            *[
                ("Guardián de Reyes Funerarios", 70, 6, 3, "3+", "4+", "9+", "Mantenerse firme, …")
                for _ in range(4)
            ],
            ("Thrower de Reyes Funerarios", 70, 6, 3, "3+", "3+", "9+", "Pasar, …"),
            *[
                ("Esqueleto de Reyes Funerarios Línea", 40, 5, 3, "4+", "6+", "9+", "Regeneración")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "orcos-negros",
        "name": "Orcos Negros",
        "tier": 5,
        "img": "orcos-negros",
        "rr": 60,
        "rows": [
            ("Troll", 115, 4, 5, "5+", "5+", "10+", "Hambriento, GM, …"),
            *[
                ("Black Orc", 90, 4, 4, "4+", "6+", "10+", "Cabeza dura, Placar")
                for _ in range(4)
            ],
            *[
                ("Blitzer", 80, 6, 3, "3+", "4+", "9+", "Placar, Placaje def.")
                for _ in range(2)
            ],
            ("Thrower", 65, 5, 3, "3+", "3+", "9+", "Pasar, Manos seguras"),
            *[
                ("Goblin", 45, 6, 2, "3+", "4+", "8+", "Esquivar, …")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "bretonia",
        "name": "Bretonia",
        "tier": 5,
        "img": "bretonia",
        "rr": 60,
        "rows": [
            *[
                ("Caballero del Grial", 95, 7, 3, "3+", "4+", "10+", "Agallas, Equilibrio firme, Placar")
                for _ in range(4)
            ],
            *[
                ("Caballero Receptor", 85, 7, 3, "3+", "4+", "9+", "Agallas, Atrapar, …")
                for _ in range(2)
            ],
            *[
                ("Caballero Lanzador", 80, 6, 3, "3+", "3+", "9+", "Agallas, Pasar, …")
                for _ in range(2)
            ],
            *[
                ("Escuderos", 50, 6, 3, "3+", "4+", "8+", "Forcejear")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "enanos-del-caos",
        "name": "Enanos del Caos",
        "tier": 5,
        "img": "enanos-del-caos",
        "rr": 70,
        "rows": [
            ("Minotauro Esclavizado", 150, 5, 5, "4+", "6+", "9+", "Furia, GM, …"),
            ("Bull Centaur", 130, 6, 4, "4+", "6+", "10+", "Esprintar, …"),
            *[
                ("Enano del Caos Blocker", 70, 4, 3, "4+", "6+", "10+", "Placar, Piel de hierro, …")
                for _ in range(4)
            ],
            *[
                ("Flamesmith", 80, 5, 3, "4+", "6+", "10+", "Aliento de fuego, …")
                for _ in range(2)
            ],
            *[
                ("Hobgoblin Línea", 40, 6, 3, "3+", "4+", "8+", "–")
                for _ in range(4)
            ],
        ],
    },
    {
        "slug": "union-elfica",
        "name": "Unión Élfica",
        "tier": 5,
        "img": "union-elfica",
        "rr": 50,
        "rows": [
            *[
                ("Blitzer", 100, 7, 3, "2+", "4+", "9+", "Placar, Placaje def.")
                for _ in range(2)
            ],
            *[
                ("Thrower", 80, 6, 3, "2+", "2+", "8+", "Pasar, Proteger el cuero")
                for _ in range(2)
            ],
            *[
                ("Catcher", 85, 7, 2, "2+", "4+", "8+", "Atrapar, Esquivar")
                for _ in range(2)
            ],
            *[
                ("Línea", 65, 6, 3, "2+", "4+", "9+", "–")
                for _ in range(6)
            ],
        ],
    },
    {
        "slug": "goblins",
        "name": "Goblins",
        "tier": 5,
        "img": "goblins",
        "rr": 60,
        "rows": [
            ("Troll", 115, 4, 5, "5+", "5+", "10+", "Hambriento, GM, …"),
            *[
                ("Pogo", 70, 6, 2, "3+", "4+", "8+", "Esquivar, Pogo, …")
                for _ in range(2)
            ],
            *[
                ("Goblin", 40, 6, 2, "3+", "4+", "8+", "Esquivar, Escurridizo, …")
                for _ in range(9)
            ],
        ],
    },
    {
        "slug": "khorne",
        "name": "Khorne",
        "tier": 5,
        "img": "khorne",
        "img_file": "khorne.png",
        "rr": 60,
        "rows": [
            ("BloodSpawn", 160, 5, 5, "4+", "6+", "9+", "Garras, GM, …"),
            *[
                ("Bloodseeker", 105, 5, 4, "4+", "6+", "10+", "Furia")
                for _ in range(2)
            ],
            *[
                ("Khorngor", 70, 6, 3, "3+", "4+", "9+", "Cuernos, Imparable, …")
                for _ in range(4)
            ],
            *[
                ("Línea Marauder", 50, 6, 3, "3+", "4+", "8+", "Furia")
                for _ in range(5)
            ],
        ],
    },
    {
        "slug": "snotlings",
        "name": "Snotlings",
        "tier": 5,
        "img": "snotlings",
        "rr": 60,
        "rows": [
            *[
                ("Troll Entrenado", 95, 4, 5, "5+", "5+", "10+", "GM, Regeneración, …")
                for _ in range(2)
            ],
            ("Pump Wagon", 80, 5, 5, "5+", "6+", "9+", "Arma secreta, GM, …"),
            *[
                ("Riotous Rookie", 40, 5, 2, "4+", "6+", "7+", "Lanzar compañero, …")
                for _ in range(2)
            ],
            *[
                ("Fungus Flinga", 30, 5, 1, "4+", "6+", "6+", "Lanzar compañero, …")
                for _ in range(2)
            ],
            *[
                ("Stilty Runna", 25, 7, 1, "4+", "6+", "6+", "Esprintar, …")
                for _ in range(2)
            ],
            *[
                ("Snotling Línea", 15, 5, 1, "4+", "6+", "6+", "Escurridizo, …")
                for _ in range(3)
            ],
        ],
    },
    {
        "slug": "gnomos",
        "name": "Gnomos",
        "tier": 6,
        "img": "gnomos",
        "rr": 70,
        "rows": [
            ("Forest Troll", 110, 4, 5, "5+", "5+", "10+", "GM, Hambriento, …"),
            ("Gnomo Blitzer", 70, 6, 2, "3+", "4+", "8+", "Placar, Escurridizo, …"),
            ("Gnomo Thrower", 65, 5, 2, "3+", "3+", "8+", "Pasar, …"),
            ("Gnomo Troll Slayer", 95, 5, 2, "3+", "4+", "9+", "Berserker, …"),
            ("Bombardero", 40, 5, 2, "3+", "4+", "8+", "Arma secreta, …"),
            *[
                ("Gnomo Línea", 40, 5, 2, "3+", "4+", "8+", "Esquivar, Escurridizo, …")
                for _ in range(11)
            ],
        ],
    },
    {
        "slug": "halflings",
        "name": "Halflings",
        "tier": 6,
        "img": "halflings",
        "rr": 60,
        "rows": [
            ("Treeman", 120, 2, 6, "5+", "5+", "11+", "GM, Lanzar compañero, …"),
            *[
                ("Halfling Hopeful", 30, 5, 2, "3+", "4+", "7+", "Esquivar, …")
                for _ in range(11)
            ],
        ],
    },
    {
        "slug": "ogros",
        "name": "Ogros",
        "tier": 6,
        "img": "ogros",
        "rr": 140,
        "rows": [
            *[
                ("Ogre Línea", 140, 5, 5, "5+", "5+", "10+", "Muro de carne, GM, …")
                for _ in range(5)
            ],
            *[
                ("Gnoblar Línea", 20, 5, 1, "4+", "6+", "6+", "Escurridizo, …")
                for _ in range(10)
            ],
        ],
    },
]


STUBS = [
    (
        "vampiros",
        "Vampiros",
        3,
        "vampiros",
        "La ficha `source/teams/vampiros.md` aún no incluye el roster oficial BB2025; completar cuando Nuffle Zone publique costes y posiciones.",
    ),
    (
        "renegados-del-caos",
        "Renegados del Caos",
        5,
        "renegados-del-caos",
        "La ficha `source/teams/renegados-del-caos.md` está pendiente de roster oficial; construir desde GW / NAF y validar con el reglamento EuroBowl.",
    ),
]


def emit_stub(slug: str, name: str, tier: int, img: str, note: str) -> str:
    b, sk, fl = EURO[tier]
    img_fn = f"{img}.webp"
    return f"""# {name} — EuroBowl 2026 (Tier {tier}) — PLANTILLA

![{name}](../../source/images/equipos/{img_fn})

> **Plantilla:** {note}
>
> Reglamento: [eurobowl-2026.md](../../source/tiers/eurobowl-2026.md).
>
> **Estado competitivo:** **sin revisión meta** — [README `eurobowl-2026`](README.md) · tag `eurobowl-2026-wip-competitive`.

## Presupuesto EuroBowl

| Concepto | Valor |
|----------|--------|
| **Team Budget (base)** | {b}.000 gp |
| **Skill Gold (pool)** | {sk}.000 gp |
| **Flowing Funds** | {fl}.000 gp |

## Alineación

*Añadir cuando exista roster en `source/teams/{slug}.md`.*

## Skill Gold

Pool de {sk}.000 gp para avances según tablas del reglamento EuroBowl.
"""


def main() -> None:
    for team in TEAMS:
        psum = sum(r[1] for r in team["rows"])
        sol = solve_extras(team["tier"], psum, team["rr"], team["slug"])
        if sol is None:
            raise SystemExit(f"Sin solución: {team['slug']}")
        path = os.path.join(ROOT, f"eurobowl-26-{team['slug']}-tier{team['tier']}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(emit(team))
        print("ok", path)
    for slug, name, tier, img, note in STUBS:
        path = os.path.join(ROOT, f"eurobowl-26-{slug}-tier{tier}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(emit_stub(slug, name, tier, img, note))
        print("stub", path)


if __name__ == "__main__":
    main()
