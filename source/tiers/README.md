# Tiers — Blood Bowl 3ª Temporada

Esta carpeta contiene la referencia de **oro por tier** y **skill pack por tier** para construcción de rosters en torneos (NAF, Matched Play). El agente **Roster Builder** debe consultar estos archivos al proponer alineaciones.

## Contenido

**Referencia general (2 archivos)**

| Archivo | Contenido |
|---------|-----------|
| **oro-presupuesto.md** | Presupuesto de construcción (gp) por tier y tabla Tier \| Equipos. |
| **skill-pack.md** | Puntos de habilidad, límite de secundarias, apilamiento por tier, coste de puntos y tabla Tier \| Equipos. |

**Guías por equipo (en `rosters/`)**

| Ubicación | Contenido |
|-----------|-----------|
| [rosters/limite-valoracion/orcos-negros-valoracion-limitada.md](../../rosters/limite-valoracion/orcos-negros-valoracion-limitada.md) | Orcos Negros: rosters para torneos con valoración limitada por tier (Control y Fouling, Triple Dirty, Doble Troll muro). |
| [rosters/limite-valoracion/nobleza-imperial-valoracion-limitada.md](../../rosters/limite-valoracion/nobleza-imperial-valoracion-limitada.md) | Nobleza Imperial: rosters para torneos con valoración limitada (Clásico competitivo, Control sin Ogre). |
| [rosters/skill-pack/orcos-negros-skill-pack.md](../../rosters/skill-pack/orcos-negros-skill-pack.md) | Orcos Negros: builds para torneos con skill pack (Meta estándar, Doble Troll Control, Fouling machine). |
| [rosters/skill-pack/nobleza-imperial-skill-pack.md](../../rosters/skill-pack/nobleza-imperial-skill-pack.md) | Nobleza Imperial: builds para torneos con skill pack (Meta estándar, Anti-elfos, Control brutal). |
| [rosters/limite-valoracion/altos-elfos-valoracion-limitada.md](../../rosters/limite-valoracion/altos-elfos-valoracion-limitada.md) | Altos Elfos: rosters para torneos con valoración limitada (Clásico competitivo, Más jugadores). |
| [rosters/skill-pack/altos-elfos-skill-pack.md](../../rosters/skill-pack/altos-elfos-skill-pack.md) | Altos Elfos: builds para torneos con skill pack (Meta competitivo, Anti bash, Ultra defensivo). |
| [rosters/limite-valoracion/union-elfica-valoracion-limitada.md](../../rosters/limite-valoracion/union-elfica-valoracion-limitada.md) | Unión Élfica: rosters para torneos con valoración limitada (Clásico competitivo, Más velocidad). |
| [rosters/skill-pack/union-elfica-skill-pack.md](../../rosters/skill-pack/union-elfica-skill-pack.md) | Unión Élfica: builds para torneos con skill pack (Meta estándar, Anti bash, Ultra agresivo). |
| [rosters/limite-valoracion/hombres-lagarto-valoracion-limitada.md](../../rosters/limite-valoracion/hombres-lagarto-valoracion-limitada.md) | Hombres Lagarto: rosters para torneos con valoración limitada (TV 1100, 1150, 1200). |
| [rosters/skill-pack/hombres-lagarto-skill-pack.md](../../rosters/skill-pack/hombres-lagarto-skill-pack.md) | Hombres Lagarto: builds para torneos con skill pack (6–9 skills, Block/Guard/Sure Hands). |
| [rosters/limite-valoracion/no-muertos-valoracion-limitada.md](../../rosters/limite-valoracion/no-muertos-valoracion-limitada.md) | No Muertos: rosters para torneos con valoración limitada (TV 1100, 1150, 1200). |
| [rosters/skill-pack/no-muertos-skill-pack.md](../../rosters/skill-pack/no-muertos-skill-pack.md) | No Muertos: builds para torneos con skill pack (Guard/Sure Hands/Block/Tackle/Wrestle). |
| [rosters/limite-valoracion/skavens-valoracion-limitada.md](../../rosters/limite-valoracion/skavens-valoracion-limitada.md) | Skavens: rosters para torneos con valoración limitada (TV 1100–1200, con/sin Rata Ogro). |
| [rosters/skill-pack/skavens-skill-pack.md](../../rosters/skill-pack/skavens-skill-pack.md) | Skavens: builds para torneos con skill pack (Wrestle/Strip Ball/Block/Sidestep/sacker). |

## Uso por el Roster Builder

1. Obtener el **tier del equipo** desde la tabla Tier | Equipos (en cualquiera de los dos archivos).
2. Aplicar el **presupuesto de oro** del tier (oro-presupuesto.md) y no superar ese tope.
3. Aplicar **Skill Points** y límites del tier (skill-pack.md): no gastar más puntos ni más secundarias de las permitidas; respetar apilamiento.
4. Si el torneo indica otro pack u oro único (ej. 1.150k para todos), usar el reglamento del evento.
5. Para Orcos Negros (Tier 3), Nobleza Imperial (Tier 2), Altos Elfos (Tier 1), Unión Élfica (Tier 2), Hombres Lagarto (Tier 1), No Muertos (Tier 2) y Skavens (Tier 2), consultar las guías en `rosters/limite-valoracion/` y `rosters/skill-pack/` si se quieren rosters tipo torneo ya optimizados.

## Referencias

- [GW Blood Bowl Downloads (Designer's Commentary)](https://www.warhammer-community.com/blood-bowl-downloads/)
- [NAF — Tiers and Tiering](https://thenaf.net/tournaments/running-a-tournament/tiers-and-tiering)
