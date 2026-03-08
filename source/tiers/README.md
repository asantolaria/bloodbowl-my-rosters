# Tiers — Blood Bowl 3ª Temporada

Esta carpeta contiene la referencia de **oro por tier** y **skill pack por tier** para construcción de rosters en torneos (NAF, Matched Play). El agente **Roster Builder** debe consultar estos archivos al proponer alineaciones.

## Contenido (2 archivos)

| Archivo | Contenido |
|---------|-----------|
| **oro-presupuesto.md** | Presupuesto de construcción (gp) por tier y tabla Tier \| Equipos. |
| **skill-pack.md** | Puntos de habilidad, límite de secundarias, apilamiento por tier, coste de puntos y tabla Tier \| Equipos. |

## Uso por el Roster Builder

1. Obtener el **tier del equipo** desde la tabla Tier | Equipos (en cualquiera de los dos archivos).
2. Aplicar el **presupuesto de oro** del tier (oro-presupuesto.md) y no superar ese tope.
3. Aplicar **Skill Points** y límites del tier (skill-pack.md): no gastar más puntos ni más secundarias de las permitidas; respetar apilamiento.
4. Si el torneo indica otro pack u oro único (ej. 1.150k para todos), usar el reglamento del evento.

## Referencias

- [GW Blood Bowl Downloads (Designer's Commentary)](https://www.warhammer-community.com/blood-bowl-downloads/)
- [NAF — Tiers and Tiering](https://thenaf.net/tournaments/running-a-tournament/tiers-and-tiering)
