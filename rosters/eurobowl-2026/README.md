# Rosters — EuroBowl 2026 (#euro26)

Plantillas de equipo para la copa NAF **EuroBowl 2026** (*Living Ruleset* BETA + HE patch), **Blood Bowl 3ª temporada / BB2025**.

**Reglas y presupuestos:** [source/tiers/eurobowl-2026.md](../../source/tiers/eurobowl-2026.md).

---

## Estado — revisión competitiva pendiente

> **No usar como listas “finales” para torneo** sin repasar.  
> Cada archivo cumple el **marco económico** EuroBowl 2026 (Team Budget, rerolls/apo/fans, Skill Gold y Flowing según tier), pero las **alineaciones de ejemplo** y el bloque de **Skill Gold** no están optimizados para **meta competitiva** (ni contrastados con estadísticas NAF / guías recientes).  
> **Trabajo pendiente:** revisar por raza/tier composición, reparto de avances, estrellas e inducements antes de jugar en serio.

**Etiqueta de seguimiento (búsqueda en repo):** `eurobowl-2026-wip-competitive`

---

## Convención de archivos

`eurobowl-26-[slug-equipo]-tier[N].md`

- **slug-equipo:** como en `source/teams/` (ej. `altos-elfos`, `enanos-del-caos`).
- **tier:** tier EuroBowl 1–6 (presupuesto de equipo 1.060k–1.140k según tabla del reglamento).

## Índice por tier

| Tier | Team Budget | Skill Gold (pool) | Flowing | Equipos (archivo) |
|------|-------------|-------------------|---------|-------------------|
| 1 | 1.060k | 120k | 10k | [Elfos Silvanos](eurobowl-26-elfos-silvanos-tier1.md), [Alianza del Viejo Mundo](eurobowl-26-alianza-viejo-mundo-tier1.md) |
| 2 | 1.070k | 140k | 20k | [Amazonas](eurobowl-26-amazonas-tier2.md), [Orcos](eurobowl-26-orcos-tier2.md), [No Muertos](eurobowl-26-no-muertos-tier2.md), [Skavens](eurobowl-26-skavens-tier2.md), [Habitantes del Inframundo](eurobowl-26-habitantes-inframundo-tier2.md) |
| 3 | 1.080k | 160k | 30k | [Elfos Oscuros](eurobowl-26-elfos-oscuros-tier3.md), [Altos Elfos](eurobowl-26-altos-elfos-tier3.md), [Humanos](eurobowl-26-humanos-tier3.md), [Hombres Lagarto](eurobowl-26-hombres-lagarto-tier3.md), [Nigromantes](eurobowl-26-nigromantes-tier3.md), [Nórdicos](eurobowl-26-nordicos-tier3.md), [Vampiros (plantilla)](eurobowl-26-vampiros-tier3.md) |
| 4 | 1.100k | 190k | 30k | [Elegidos del Caos](eurobowl-26-elegidos-del-caos-tier4.md), [Enanos](eurobowl-26-enanos-tier4.md), [Nobleza Imperial](eurobowl-26-nobleza-imperial-tier4.md), [Nurgle](eurobowl-26-nurgle-tier4.md), [Slann](eurobowl-26-slann-tier4.md), [Reyes Funerarios](eurobowl-26-reyes-funerarios-tier4.md) |
| 5 | 1.120k | 220k | 30k | [Orcos Negros](eurobowl-26-orcos-negros-tier5.md), [Bretonia](eurobowl-26-bretonia-tier5.md), [Enanos del Caos](eurobowl-26-enanos-del-caos-tier5.md), [Renegados (plantilla)](eurobowl-26-renegados-del-caos-tier5.md), [Unión Élfica](eurobowl-26-union-elfica-tier5.md), [Goblins](eurobowl-26-goblins-tier5.md), [Khorne](eurobowl-26-khorne-tier5.md), [Snotlings](eurobowl-26-snotlings-tier5.md) |
| 6 | 1.140k | 240k | 40k | [Gnomos](eurobowl-26-gnomos-tier6.md), [Halflings](eurobowl-26-halflings-tier6.md), [Ogros](eurobowl-26-ogros-tier6.md) |

## Contenido de cada roster

- Tabla de **jugadores** al coste de lista (sin Skill Gold).
- **Desglose** que suma exactamente el **Team Budget base** del tier: rerolls, apotecario (si aplica), fans dedicados y, si hace falta, una línea de **Flowing Funds** en oro suelto (resto no múltiplo de 10k).
- Bloque editable para **gastar Skill Gold** en avances (Primary / Secondary / Stack según reglamento).
- Referencias a estrellas (por tier) e inducements permitidos.

## Regenerar archivos

Tras editar datos en `_build_rosters.py`:

```bash
python rosters/eurobowl-2026/_build_rosters.py
```

## Plantillas incompletas

**Vampiros** y **Renegados del Caos** no tienen aún roster completo en `source/teams/`; los `.md` son plantillas con presupuestos EuroBowl hasta completar fichas oficiales.
