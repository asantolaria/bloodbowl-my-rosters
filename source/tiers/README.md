# Tiers — Blood Bowl 3ª Temporada

Esta carpeta contiene la referencia de **oro por tier** y **skill pack por tier** para construcción de rosters en torneos (NAF, Matched Play). El agente **Roster Builder** debe consultar estos archivos al proponer alineaciones.

## Contenido

**Referencia general**

| Archivo | Contenido |
|---------|-----------|
| **oro-presupuesto.md** | Presupuesto de construcción (gp) por tier y tabla Tier \| Equipos (GW / NAF genérico). |
| **skill-pack.md** | Puntos de habilidad, límite de secundarias, apilamiento por tier, coste de puntos y tabla Tier \| Equipos. |
| **eurobowl-2026.md** | **EuroBowl 2026** (NAF): 6 tiers, presupuesto 1.060k–1.140k, Skill Gold, Flowing Funds, avances Primary/Secondary/Stack, estrellas e inducements (Living Ruleset BETA + HE patch). Rosters de ejemplo: [rosters/eurobowl-2026/README.md](../../rosters/eurobowl-2026/README.md). |

**Guías por equipo (en `rosters/`)**

| Ubicación | Contenido |
|-----------|-----------|
| [rosters/limite-valoracion/orcos-negros-valoracion-limitada.md](../../rosters/limite-valoracion/orcos-negros-valoracion-limitada.md) | Orcos Negros: rosters para torneos con valoración limitada por tier (Control y Fouling, Triple Dirty, Doble Troll muro). |
| [rosters/limite-valoracion/nobleza-imperial-valoracion-limitada.md](../../rosters/limite-valoracion/nobleza-imperial-valoracion-limitada.md) | Nobleza Imperial: rosters para torneos con valoración limitada (Clásico competitivo, Control sin Ogre). |
| [rosters/limite-valoracion/altos-elfos-valoracion-limitada.md](../../rosters/limite-valoracion/altos-elfos-valoracion-limitada.md) | Altos Elfos: lista **2026** (Nuffle Zone); dos builds a **1.060k** (tope tier 1 = 1.140k en oro-presupuesto). |
| [rosters/limite-valoracion/union-elfica-valoracion-limitada.md](../../rosters/limite-valoracion/union-elfica-valoracion-limitada.md) | Unión Élfica: rosters para torneos con valoración limitada (Clásico competitivo, Más velocidad). |
| [rosters/limite-valoracion/hombres-lagarto-valoracion-limitada.md](../../rosters/limite-valoracion/hombres-lagarto-valoracion-limitada.md) | Hombres Lagarto: rosters para torneos con valoración limitada (TV 1100, 1150, 1200). |
| [rosters/limite-valoracion/no-muertos-valoracion-limitada.md](../../rosters/limite-valoracion/no-muertos-valoracion-limitada.md) | No Muertos: tope **Tier 2 = 1.160k** según oro-presupuesto; sin apotecario en roster oficial. |
| [rosters/limite-valoracion/skavens-valoracion-limitada.md](../../rosters/limite-valoracion/skavens-valoracion-limitada.md) | Skavens: rosters para torneos con valoración limitada (TV 1100–1200, con/sin Rata Ogro). |
| [rosters/limite-valoracion/elegidos-del-caos-valoracion-limitada.md](../../rosters/limite-valoracion/elegidos-del-caos-valoracion-limitada.md) | Elegidos del Caos: roster para torneo clásico Tier 3 (1.180k, BB2025). |
| [rosters/skill-pack/README.md](../../rosters/skill-pack/README.md) | Formaciones skill pack (un archivo por build; nombres `xP-yS-zA`; Altos Elfos, Unión Élfica, Skavens, No Muertos, Hombres Lagarto, Nobleza, Orcos Negros, Elegidos). |

## Uso por el Roster Builder

1. Obtener el **tier del equipo** desde la tabla Tier | Equipos (en cualquiera de los dos archivos).
2. Aplicar el **presupuesto de oro** del tier (oro-presupuesto.md) y no superar ese tope.
3. Aplicar **Skill Points** y límites del tier (skill-pack.md): no gastar más puntos ni más secundarias de las permitidas; respetar apilamiento.
4. Si el torneo es **EuroBowl 2026** (o similar NAF con pack propio), usar **eurobowl-2026.md**. Si el torneo indica otro pack u oro único (ej. 1.150k para todos), usar el reglamento del evento.
5. Para Orcos Negros (Tier 3), Elegidos del Caos (Tier 3), Nobleza Imperial (Tier 2), Altos Elfos (Tier 1), Unión Élfica (Tier 2), Hombres Lagarto (Tier 1), No Muertos (Tier 2) y Skavens (Tier 2), consultar las guías en `rosters/limite-valoracion/` y `rosters/skill-pack/` si se quieren rosters tipo torneo ya optimizados.

## Referencias

- [GW Blood Bowl Downloads (Designer's Commentary)](https://www.warhammer-community.com/blood-bowl-downloads/)
- [NAF — Tiers and Tiering](https://thenaf.net/tournaments/running-a-tournament/tiers-and-tiering)
