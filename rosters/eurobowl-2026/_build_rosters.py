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
    # Roster EuroBowl en `eurobowl-26-elfos-silvanos-tier1.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "elfos-silvanos",
        "name": "Elfos Silvanos",
        "tier": 1,
        "img": "elfos-silvanos",
        "rr": 50,
        "rows": [
            ("Wardancer", 130, 8, 3, "2+", "3+", "8+", "Placar, Esquivar, Saltar"),
            ("Wardancer", 130, 8, 3, "2+", "3+", "8+", "Placar, Esquivar, Saltar"),
            ("Elfo Silvano Catcher", 90, 8, 2, "2+", "3+", "8+", "Atrapar, Esprintar, Esquivar"),
            ("Elfo Silvano Catcher", 90, 8, 2, "2+", "3+", "8+", "Atrapar, Esprintar, Esquivar"),
            ("Elfo Silvano Thrower", 85, 7, 3, "2+", "2+", "8+", "Pasar, Proteger el cuero"),
            *[
                ("Elfo Silvano Línea", 65, 7, 3, "2+", "3+", "8+", "—")
                for _ in range(6)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-alianza-viejo-mundo-tier1.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "alianza-viejo-mundo",
        "name": "Alianza del Viejo Mundo",
        "tier": 1,
        "img": "alianza-viejo-mundo",
        "rr": 70,
        "rows": [
            (
                "Hombre-Árbol",
                120,
                2,
                6,
                "5+",
                "5+",
                "11+",
                "GM (+1), Mantenerse Firme, Brazo Fuerte, Echar Raíces, Cabeza Dura, Lanzar compañero, ¡Tronco va!",
            ),
            (
                "Enano Blitzer",
                100,
                5,
                3,
                "4+",
                "4+",
                "10+",
                "Placar, Placaje Heroico, Placaje Defensivo, Cabeza Dura",
            ),
            (
                "Humano Blitzer",
                85,
                7,
                3,
                "3+",
                "4+",
                "9+",
                "Placar, Placaje Defensivo",
            ),
            *[
                (
                    "Enano Blocker",
                    70,
                    4,
                    3,
                    "4+",
                    "5+",
                    "10+",
                    "Placar, Romper Defensas, Cabeza Dura",
                )
                for _ in range(3)
            ],
            ("Humano Catcher", 75, 8, 3, "3+", "4+", "8+", "Atrapar, Esquivar"),
            ("Humano Thrower", 75, 6, 3, "3+", "3+", "9+", "Manos Seguras, Pasar"),
            *[
                ("Humano Línea", 50, 6, 3, "3+", "4+", "9+", "—")
                for _ in range(4)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-amazonas-tier2.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "amazonas",
        "name": "Amazonas",
        "tier": 2,
        "img": "amazonas",
        "rr": 60,
        "rows": [
            ("Guerrera Jaguar Blocker", 110, 6, 4, "3+", "4+", "9+", "Esquivar, Romper Defensas"),
            ("Guerrera Jaguar Blocker", 110, 6, 4, "3+", "4+", "9+", "Esquivar, Romper Defensas"),
            ("Guerrera Piraña Blitzer", 90, 7, 3, "3+", "4+", "8+", "Esquivar, Golpe a la Carrera, En Pie de un Salto"),
            ("Guerrera Piraña Blitzer", 90, 7, 3, "3+", "4+", "8+", "Esquivar, Golpe a la Carrera, En Pie de un Salto"),
            (
                "Guerrera Pitón Thrower",
                80,
                6,
                3,
                "3+",
                "3+",
                "8+",
                "Atento al Balón, Esquivar, Pasar, Pase Seguro",
            ),
            *[
                ("Guerrera Águila Línea", 50, 6, 3, "3+", "4+", "8+", "Esquivar")
                for _ in range(8)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-orcos-tier2.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "orcos",
        "name": "Orcos",
        "tier": 2,
        "img": "orcos",
        "rr": 60,
        "rows": [
            (
                "Troll",
                115,
                4,
                5,
                "5+",
                "5+",
                "10+",
                "Siempre Hambriento, Solitario (4+), Golpe Mortífero, Proyectil Vómito, Realmente Estúpido, Regeneración, Lanzar Compañero",
            ),
            (
                "Big Un Blocker",
                95,
                5,
                4,
                "4+",
                "6+",
                "10+",
                "Cabeza Dura, Golpe Mortífero, Provocar, Inestable",
            ),
            (
                "Big Un Blocker",
                95,
                5,
                4,
                "4+",
                "6+",
                "10+",
                "Cabeza Dura, Golpe Mortífero, Provocar, Inestable",
            ),
            ("Orco Blitzer", 85, 6, 3, "3+", "4+", "10+", "Abrirse Paso, Placar"),
            ("Orco Blitzer", 85, 6, 3, "3+", "4+", "10+", "Abrirse Paso, Placar"),
            ("Orco Lanzador", 75, 6, 3, "3+", "3+", "9+", "Pasar, Manos Seguras"),
            ("Orco Lanzador", 75, 6, 3, "3+", "3+", "9+", "Pasar, Manos Seguras"),
            *[
                ("Orco Línea", 50, 5, 3, "3+", "4+", "10+", "–")
                for _ in range(4)
            ],
            (
                "Goblin",
                40,
                6,
                2,
                "3+",
                "3+",
                "8+",
                "Esquivar, Humanoide Bala, Escurridizo",
            ),
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
    # Roster EuroBowl en `eurobowl-26-habitantes-inframundo-tier2.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "habitantes-inframundo",
        "name": "Habitantes del Inframundo",
        "tier": 2,
        "img": "habitantes-inframundo",
        "rr": 50,
        "rows": [
            (
                "Rata Ogro",
                150,
                6,
                5,
                "4+",
                "6+",
                "9+",
                "Ferocidad Animal, Furia, Golpe Mortífero, Cola Prensil, Solitario (4+)",
            ),
            (
                "Gutter Runner",
                85,
                9,
                2,
                "2+",
                "4+",
                "8+",
                "Animosidad (Goblin), Apuñalar, Esquivar",
            ),
            (
                "Blitzer skaven",
                90,
                8,
                3,
                "3+",
                "4+",
                "9+",
                "Animosidad (Goblin), Placar, Robar Balón",
            ),
            *[
                (
                    "Clanrat skaven",
                    50,
                    7,
                    3,
                    "3+",
                    "4+",
                    "8+",
                    "Animosidad (Goblin)",
                )
                for _ in range(3)
            ],
            (
                "Lanzador skaven",
                80,
                7,
                3,
                "3+",
                "2+",
                "8+",
                "Animosidad (Goblin), Manos Seguras, Pasar",
            ),
            *[
                (
                    "Goblin",
                    40,
                    6,
                    2,
                    "3+",
                    "4+",
                    "8+",
                    "Esquivar, Humanoide Bala, Escurridizo",
                )
                for _ in range(5)
            ],
            *[
                (
                    "Snotling",
                    15,
                    5,
                    1,
                    "3+",
                    "4+",
                    "6+",
                    "Canijo, Esquivar, Echarse a un Lado, Escurridizo, Humanoide Bala, Insignificante",
                )
                for _ in range(3)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-elfos-oscuros-tier3.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "elfos-oscuros",
        "name": "Elfos Oscuros",
        "tier": 3,
        "img": "elfos-oscuros",
        "rr": 50,
        "rows": [
            *[
                (
                    "Bruja Elfa",
                    110,
                    7,
                    3,
                    "2+",
                    "4+",
                    "8+",
                    "En Pie de un Salto, Esquivar, Furia",
                )
                for _ in range(2)
            ],
            *[
                ("Elfo Oscuro Blitzer", 105, 7, 3, "2+", "3+", "9+", "Placar")
                for _ in range(2)
            ],
            (
                "Elfo Oscuro Asesino",
                90,
                7,
                3,
                "2+",
                "4+",
                "8+",
                "Apuñalar, Golpe a la Carrera, Perseguir",
            ),
            (
                "Elfo Oscuro Runner",
                80,
                7,
                3,
                "2+",
                "3+",
                "8+",
                "Pase Precipitado, Patada de Despeje",
            ),
            *[
                ("Elfo Oscuro Línea", 65, 6, 3, "2+", "3+", "9+", "–")
                for _ in range(5)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-altos-elfos-tier3.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "altos-elfos",
        "name": "Altos Elfos",
        "tier": 3,
        "img": "altos-elfos",
        "rr": 50,
        "rows": [
            *[
                (
                    "Alto Elfo Dragon Warrior",
                    110,
                    8,
                    3,
                    "2+",
                    "4+",
                    "9+",
                    "El Balón es Mío, Equilibrio Firme, Placar",
                )
                for _ in range(2)
            ],
            *[
                ("Alto Elfo White Lion Blitzer", 110, 7, 3, "2+", "3+", "9+", "Forcejear, Garras")
                for _ in range(2)
            ],
            (
                "Alto Elfo Phoenix Prince Thrower",
                90,
                6,
                3,
                "2+",
                "2+",
                "9+",
                "Partenubes, Pasar, Pase Seguro",
            ),
            *[
                ("Alto Elfo Línea", 65, 6, 3, "2+", "3+", "9+", "–")
                for _ in range(6)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-humanos-tier3.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "humanos",
        "name": "Humanos",
        "tier": 3,
        "img": "humanos",
        "rr": 50,
        "rows": [
            (
                "Ogro",
                140,
                5,
                5,
                "4+",
                "5+",
                "10+",
                "Estúpido, Solitario (3+), Golpe Mortífero, Cabeza Dura, Lanzar Compañero",
            ),
            *[
                (
                    "Blitzer",
                    85,
                    7,
                    3,
                    "3+",
                    "4+",
                    "9+",
                    "Placar, Placaje Defensivo",
                )
                for _ in range(2)
            ],
            *[
                ("Catcher", 75, 8, 3, "3+", "4+", "8+", "Atrapar, Esquivar")
                for _ in range(2)
            ],
            ("Thrower", 75, 6, 3, "3+", "3+", "9+", "Manos Seguras, Pasar"),
            *[
                ("Línea", 50, 6, 3, "3+", "4+", "9+", "–")
                for _ in range(6)
            ],
            (
                "Halfling",
                30,
                5,
                2,
                "3+",
                "4+",
                "7+",
                "Esquivar, Humanoide Bala, Escurridizo",
            ),
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
    # Roster EuroBowl en `eurobowl-26-nigromantes-tier3.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "nigromantes",
        "name": "Nigromantes",
        "tier": 3,
        "img": "nigromantes",
        "rr": 70,
        "rows": [
            *[
                (
                    "Gólem de Carne",
                    110,
                    4,
                    4,
                    "4+",
                    "6+",
                    "10+",
                    "Cabeza Dura, Inestable, Mantenerse Firme, Regeneración",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Wraith",
                    85,
                    6,
                    3,
                    "3+",
                    "–",
                    "9+",
                    "Apariencia Asquerosa, Echarse a un Lado, Placar, Regeneración, Sin Manos",
                )
                for _ in range(2)
            ],
            *[
                ("Hombre Lobo", 120, 8, 3, "3+", "3+", "9+", "Furia, Garras, Regeneración")
                for _ in range(2)
            ],
            *[
                ("Ghoul", 75, 7, 3, "3+", "3+", "8+", "Esquivar, Regeneración")
                for _ in range(2)
            ],
            *[
                (
                    "Zombie Línea",
                    40,
                    4,
                    3,
                    "4+",
                    "6+",
                    "9+",
                    "Inestable, Piquete de Ojos, Regeneración",
                )
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
    # Roster EuroBowl en `eurobowl-26-enanos-tier4.md` (manual, captura AndyDavo); SKIP_EMIT.
    {
        "slug": "enanos",
        "name": "Enanos",
        "tier": 4,
        "img": "enanos",
        "rr": 60,
        "rows": [
            (
                "MataTrols",
                95,
                5,
                3,
                "4+",
                "5+",
                "9+",
                "Placar, Agallas, Furia, Cabeza Dura, Odio (Troll)",
            ),
            (
                "MataTrols",
                95,
                5,
                3,
                "4+",
                "5+",
                "9+",
                "Placar, Agallas, Furia, Cabeza Dura, Odio (Troll)",
            ),
            *[
                (
                    "Enano Blitzer",
                    100,
                    5,
                    3,
                    "4+",
                    "4+",
                    "10+",
                    "Placar, Placaje Heroico, Placaje Defensivo, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Enano Runner",
                    80,
                    6,
                    3,
                    "3+",
                    "4+",
                    "9+",
                    "Esprintar, Manos Seguras, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Enano Línea",
                    70,
                    4,
                    3,
                    "4+",
                    "5+",
                    "10+",
                    "Placar, Romper Defensas, Cabeza Dura",
                )
                for _ in range(5)
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
                ("Bodyguard", 85, 5, 3, "3+", "4+", "9+", "Mantenerse Firme, Forcejear")
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
    # Roster EuroBowl en `eurobowl-26-slann-tier4.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "slann",
        "name": "Slann",
        "tier": 4,
        "img": "slann",
        "rr": 50,
        "rows": [
            (
                "Slann Blitzer",
                100,
                7,
                3,
                "3+",
                "4+",
                "9+",
                "En Pie de un Salto, Golpe a la Carrera, Placaje Heroico, Pogo Saltarín",
            ),
            (
                "Slann Catcher",
                80,
                7,
                2,
                "2+",
                "3+",
                "8+",
                "Atento al Balón, Atrapada de inmersión, Piernas Muy Largas, Pogo Saltarín",
            ),
            (
                "Slann Catcher",
                80,
                7,
                2,
                "2+",
                "3+",
                "8+",
                "Atento al Balón, Atrapada de inmersión, Piernas Muy Largas, Pogo Saltarín",
            ),
            (
                "Slann Blitzer",
                100,
                7,
                3,
                "3+",
                "4+",
                "9+",
                "En Pie de un Salto, Golpe a la Carrera, Placaje Heroico, Pogo Saltarín",
            ),
            *[
                (
                    "Slann Lineman",
                    60,
                    6,
                    3,
                    "3+",
                    "4+",
                    "9+",
                    "Pogo Saltarín",
                )
                for _ in range(9)
            ],
        ],
    },
    {
        "slug": "reyes-funerarios",
        "name": "Reyes Funerarios",
        "tier": 4,
        "img": "reyes-funerarios",
        "rr": 60,
        "rows": [
            *[
                (
                    "Guardián de tumbas",
                    115,
                    4,
                    5,
                    "5+",
                    "6+",
                    "10+",
                    "Descomposición, Luchador, Regeneración",
                )
                for _ in range(4)
            ],
            *[
                (
                    "Blitzer de Rey Funerario",
                    85,
                    6,
                    3,
                    "4+",
                    "5+",
                    "9+",
                    "Placar, Regeneración, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Lanzador de Rey Funerario",
                    65,
                    6,
                    3,
                    "4+",
                    "3+",
                    "9+",
                    "Pasar, Regeneración, Manos Seguras, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Esqueleto Línea",
                    40,
                    5,
                    3,
                    "4+",
                    "6+",
                    "8+",
                    "Regeneración, Cabeza Dura",
                )
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
            *[
                (
                    "Orco Negro",
                    90,
                    4,
                    4,
                    "4+",
                    "5+",
                    "10+",
                    "Luchador, Apartar",
                )
                for _ in range(6)
            ],
            (
                "Troll adiestrado",
                115,
                4,
                5,
                "5+",
                "5+",
                "10+",
                "Siempre Hambriento, Solitario (3+), GM (+1), Proyectil Vómito, Realmente Estúpido, Regeneración, Lanzar Compañero",
            ),
            *[
                (
                    "Goblin Bruiser",
                    45,
                    6,
                    2,
                    "3+",
                    "4+",
                    "8+",
                    "Esquivar, Humanoide Bala, Escurridizo, Cabeza Dura",
                )
                for _ in range(5)
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
                (
                    "Caballero del Grial",
                    95,
                    7,
                    3,
                    "3+",
                    "4+",
                    "10+",
                    "Agallas, Equilibrio Firme, Placar",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Caballero Receptor",
                    85,
                    7,
                    3,
                    "3+",
                    "4+",
                    "9+",
                    "Agallas, Atrapar, Nervios de Acero",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Caballero Lanzador",
                    80,
                    6,
                    3,
                    "3+",
                    "3+",
                    "9+",
                    "Agallas, Pasar, Nervios de Acero",
                )
                for _ in range(2)
            ],
            *[
                ("Escudero", 50, 6, 3, "3+", "4+", "8+", "Forcejear")
                for _ in range(7)
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
            (
                "Minotauro esclavizado",
                150,
                5,
                5,
                "4+",
                "6+",
                "9+",
                "Furia, Cuernos, Solitario (4+), GM (+1), Cabeza Dura, Ira Descontrolada",
            ),
            *[
                (
                    "Bull Centaur",
                    130,
                    6,
                    4,
                    "4+",
                    "6+",
                    "10+",
                    "Esprintar, Equilibrio Firme, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Enano del Caos Blocker",
                    70,
                    4,
                    3,
                    "4+",
                    "6+",
                    "10+",
                    "Placar, Piel Ferrea, Cabeza Dura",
                )
                for _ in range(4)
            ],
            *[
                (
                    "Flamesmith",
                    80,
                    5,
                    3,
                    "4+",
                    "6+",
                    "10+",
                    "Peleón, Aliento de Fuego, Presencia Perturbadora, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                ("Hobgoblin Línea", 40, 6, 3, "3+", "4+", "8+", "—")
                for _ in range(2)
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
                (
                    "Elfo Blitzer",
                    115,
                    7,
                    3,
                    "2+",
                    "3+",
                    "9+",
                    "Placar, Echarse a un Lado",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Elfo Catcher",
                    100,
                    8,
                    3,
                    "2+",
                    "4+",
                    "8+",
                    "Atrapar, Recepción Heroica, Nervios de Acero",
                )
                for _ in range(2)
            ],
            (
                "Elfo Lanzador",
                75,
                6,
                3,
                "2+",
                "2+",
                "8+",
                "Pasar, Pase a lo Loco",
            ),
            *[
                ("Elfo Línea", 65, 6, 3, "2+", "3+", "8+", "Dejada")
                for _ in range(7)
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
    # Roster EuroBowl en `eurobowl-26-khorne-tier5.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "khorne",
        "name": "Khorne",
        "tier": 5,
        "img": "khorne",
        "img_file": "khorne.png",
        "rr": 60,
        "rows": [
            (
                "BloodSpawn",
                160,
                5,
                5,
                "4+",
                "6+",
                "9+",
                "Garras, Furia, Golpe Mortífero(+1), Ira Descontrolada, Solitario (4+)",
            ),
            *[
                ("Bloodseeker", 105, 5, 4, "4+", "6+", "10+", "Furia")
                for _ in range(4)
            ],
            *[
                (
                    "Khorngor",
                    70,
                    6,
                    3,
                    "3+",
                    "4+",
                    "9+",
                    "Cuernos, Imparable, En Pie de un Salto, Cabeza Dura",
                )
                for _ in range(2)
            ],
            *[
                ("Líneas Marauder Nacidos de la Sangre", 50, 6, 3, "3+", "4+", "8+", "Furia")
                for _ in range(4)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-snotlings-tier5.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "snotlings",
        "name": "Snotlings",
        "tier": 5,
        "img": "snotlings",
        "rr": 70,
        "rows": [
            *[
                (
                    "Troll Entrenado",
                    115,
                    4,
                    5,
                    "5+",
                    "5+",
                    "10+",
                    "GM, Lanzar compañero, Proyectil Vómito, Realmente Estúpido, Regeneración, Siempre Hambriento",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Pump Wagon",
                    100,
                    5,
                    5,
                    "5+",
                    "6+",
                    "9+",
                    "Juego Sucio, Imparable, GM, Mantenerse Firme, Realmente Estúpido",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Stilty Runna",
                    20,
                    6,
                    1,
                    "3+",
                    "4+",
                    "6+",
                    "Esquivar, Humanoide Bala, Echarse a un Lado, Escurridizo, Esprintar",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Fun-hoppa",
                    20,
                    6,
                    1,
                    "3+",
                    "4+",
                    "6+",
                    "Echarse a un Lado, Escurridizo, Esquivar, Humanoide Bala, Pogo Saltarín",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Snotling",
                    15,
                    5,
                    1,
                    "3+",
                    "4+",
                    "6+",
                    "Canijo, Colarse, Echarse a un Lado, Escurridizo, Esquivar, Humanoide Bala, Insignificante",
                )
                for _ in range(8)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-gnomos-tier6.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "gnomos",
        "name": "Gnomos",
        "tier": 6,
        "img": "gnomos",
        "rr": 50,
        "rows": [
            *[
                (
                    "Hombre-Árbol",
                    120,
                    2,
                    6,
                    "5+",
                    "5+",
                    "11+",
                    "GM, Mantenerse Firme, Brazo Fuerte, Echar Raíces, Cabeza Dura, Lanzar compañero, ¡Tronco va!",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Gnomo Maestro de las Bestias",
                    55,
                    5,
                    2,
                    "3+",
                    "4+",
                    "8+",
                    "Vigilar, En Pie de un Salto, Escurridizo, Forcejeo",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Gnomo Ilusionista",
                    50,
                    5,
                    2,
                    "3+",
                    "3+",
                    "7+",
                    "En Pie de un Salto, Escurridizo, Embaucador, Forcejeo",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Zorro de Bosque",
                    50,
                    7,
                    2,
                    "2+",
                    "–",
                    "6+",
                    "Esquivar, Mi Balón, Echarse a un Lado, Escurridizo",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Gnomo Línea",
                    40,
                    5,
                    2,
                    "3+",
                    "4+",
                    "7+",
                    "En Pie de un Salto, Humanoide Bala, Escurridizo, Forcejeo",
                )
                for _ in range(7)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-halflings-tier6.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "halflings",
        "name": "Halflings",
        "tier": 6,
        "img": "halflings",
        "rr": 60,
        "rows": [
            *[
                (
                    "Hombre-Árbol",
                    120,
                    2,
                    6,
                    "5+",
                    "5+",
                    "11+",
                    "GM (+1), Mantenerse Firme, Brazo Fuerte, Echar Raíces, Cabeza Dura, Lanzar compañero, ¡Tronco va!",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Halfling Catcher",
                    55,
                    5,
                    2,
                    "3+",
                    "4+",
                    "7+",
                    "Atrapar, Esquivar, Humanoide Bala, Esprintar, Escurridizo",
                )
                for _ in range(2)
            ],
            *[
                (
                    "Halfling Hefty",
                    50,
                    5,
                    2,
                    "3+",
                    "3+",
                    "8+",
                    "Esquivar, Zafarse, Escurridizo",
                )
                for _ in range(2)
            ],
            *[
                ("Halfling Hopeful", 30, 5, 2, "3+", "4+", "7+", "Esquivar, Humanoide Bala, Escurridizo")
                for _ in range(7)
            ],
            ("Grombrindal", 170, 5, 3, "3+", "4+", "10+", "Placar, Agallas, …"),
            ("Rumbelow Sheepskin", 170, 6, 3, "3+", "5+", "8+", "Placar, Cuernos, …"),
        ],
    },
    # Roster EuroBowl en `eurobowl-26-ogros-tier6.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "ogros",
        "name": "Ogros",
        "tier": 6,
        "img": "ogros",
        "rr": 70,
        "rows": [
            *[
                (
                    "Ogro",
                    140,
                    5,
                    5,
                    "4+",
                    "5+",
                    "10+",
                    "Cabeza Dura, Estúpido, GM (+1), Lanzar compañero",
                )
                for _ in range(5)
            ],
            (
                "Runt Punter",
                145,
                5,
                5,
                "4+",
                "4+",
                "10+",
                "Cabeza Dura, Chutar compañero, Estúpido, GM (+1)",
            ),
            *[
                (
                    "Gnoblar",
                    15,
                    5,
                    1,
                    "3+",
                    "4+",
                    "6+",
                    "Canijo, Esquivar, Echarse a un Lado, Escurridizo, Humanoide Bala",
                )
                for _ in range(8)
            ],
        ],
    },
    # Roster EuroBowl en `eurobowl-26-vampiros-tier3.md` (manual, captura); SKIP_EMIT.
    {
        "slug": "vampiros",
        "name": "Vampiros",
        "tier": 3,
        "img": "vampiros",
        "rr": 60,
        "rows": [
            ("Siervo Línea", 40, 6, 3, "3+", "4+", "8+", "–"),
            (
                "Vampiro Blitzer",
                110,
                6,
                4,
                "2+",
                "4+",
                "9+",
                "Ansia de Sangre (3+), Imparable, Mirada Hipnótica, Regeneración",
            ),
            (
                "Vampiro Blitzer",
                110,
                6,
                4,
                "2+",
                "4+",
                "9+",
                "Ansia de Sangre (3+), Imparable, Mirada Hipnótica, Regeneración",
            ),
            (
                "Vampiro Lanzador",
                110,
                6,
                4,
                "2+",
                "2+",
                "9+",
                "Ansia de Sangre (2+), Mirada Hipnótica, Pasar, Regeneración",
            ),
            (
                "Vampiro Lanzador",
                110,
                6,
                4,
                "2+",
                "2+",
                "9+",
                "Ansia de Sangre (2+), Mirada Hipnótica, Pasar, Regeneración",
            ),
            (
                "Vampiro Runner",
                100,
                8,
                3,
                "2+",
                "3+",
                "8+",
                "Ansia de Sangre (2+), Mirada Hipnótica, Regeneración",
            ),
            (
                "Vampiro Runner",
                100,
                8,
                3,
                "2+",
                "3+",
                "8+",
                "Ansia de Sangre (2+), Mirada Hipnótica, Regeneración",
            ),
            ("Siervo Línea", 40, 6, 3, "3+", "4+", "8+", "–"),
            *[
                ("Siervo Línea", 40, 6, 3, "3+", "4+", "8+", "–")
                for _ in range(5)
            ],
        ],
    },
]


# Rosters mantenidos a mano (capturas / packs); no sobrescribir al ejecutar este script.
SKIP_EMIT = frozenset(
    {
        "khorne",
        "snotlings",
        "gnomos",
        "halflings",
        "ogros",
        "elfos-silvanos",
        "alianza-viejo-mundo",
        "amazonas",
        "orcos",
        "habitantes-inframundo",
        "elfos-oscuros",
        "altos-elfos",
        "humanos",
        "nigromantes",
        "vampiros",
        "slann",
        "enanos",
    }
)


STUBS = [
    (
        "renegados-del-caos",
        "Renegados del Caos",
        5,
        "renegados-del-caos",
        "Roster 2025 en `source/teams/renegados-del-caos.md` (Nuffle EN); validar costes con PDF GW / pack #euro26.",
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
        if team["slug"] in SKIP_EMIT:
            path = os.path.join(ROOT, f"eurobowl-26-{team['slug']}-tier{team['tier']}.md")
            print("skip (manual roster)", path)
            continue
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
