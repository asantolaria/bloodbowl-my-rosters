# Rosters — EuroBowl 2026 FINAL (#euro26)

Listas para la copa NAF **EuroBowl 2026** (17–18 de octubre de 2026, Varsovia) según el reglamento [FINAL](../../source/tiers/eurobowl-2026-final.md) (7 tiers). **Blood Bowl Temporada 3 / BB2025.**

**Origen de las reglas:** [lámina oficial FINAL del organizador](https://81ccd0e8d4.clvaw-cdnwnd.com/5c60ea6ad06557d471522410634695d3/200000051-e21a7e21a9/rules%20final.webp?ph=81ccd0e8d4) ([eurobowl.eu](https://www.eurobowl.eu/entrance-options/)), transcrita en [EuroBowl 2026 FINAL](../../source/tiers/eurobowl-2026-final.md).

Cada lista está **validada** con [`_build_final.py`](https://github.com/asantolaria/bloodbowl-my-rosters/blob/main/rosters/eurobowl-2026/_build_final.py): presupuesto de equipo, Skill Gold y Flowing Funds del tier, cupos de cada posición, categoría primaria/secundaria de cada avance, máx. 3 secundarias y 3 stacks, estrellas y regla de Insignificantes.

| Tier | Equipo | Skill Gold | Flowing | Listas |
|------|--------|-----------|---------|--------|
| **1** | 1070k | 120k | 10k | [Alianza del Viejo Mundo](eurobowl-26-alianza-viejo-mundo-tier1.md) · [Elfos Silvanos](eurobowl-26-elfos-silvanos-tier1.md) · [Orcos](eurobowl-26-orcos-tier1.md) |
| **2** | 1070k | 140k | 20k | [Amazonas](eurobowl-26-amazonas-tier2.md) · [Habitantes del Inframundo](eurobowl-26-habitantes-inframundo-tier2.md) · [Skavens](eurobowl-26-skavens-tier2.md) |
| **3** | 1080k | 160k | 30k | [Altos Elfos](eurobowl-26-altos-elfos-tier3.md) · [Elfos Oscuros](eurobowl-26-elfos-oscuros-tier3.md) · [Hombres Lagarto](eurobowl-26-hombres-lagarto-tier3.md) · [Humanos](eurobowl-26-humanos-tier3.md) · [No Muertos](eurobowl-26-no-muertos-tier3.md) · [Vampiros](eurobowl-26-vampiros-tier3.md) |
| **4** | 1100k | 190k | 30k | [Nigromantes](eurobowl-26-nigromantes-tier4.md) · [Nurgle](eurobowl-26-nurgle-tier4.md) · [Nórdicos](eurobowl-26-nordicos-tier4.md) · [Reyes Funerarios](eurobowl-26-reyes-funerarios-tier4.md) · [Slann](eurobowl-26-slann-tier4.md) |
| **5** | 1120k | 220k | 30k | [Elegidos del Caos](eurobowl-26-elegidos-del-caos-tier5.md) · [Enanos del Caos](eurobowl-26-enanos-del-caos-tier5.md) · [Enanos](eurobowl-26-enanos-tier5.md) · [Nobleza Imperial](eurobowl-26-nobleza-imperial-tier5.md) · [Snotlings](eurobowl-26-snotlings-tier5.md) · [Unión Élfica](eurobowl-26-union-elfica-tier5.md) |
| **6** | 1140k | 240k | 40k | [Bretonia](eurobowl-26-bretonia-tier6.md) · [Gnomos](eurobowl-26-gnomos-tier6.md) · [Goblins](eurobowl-26-goblins-tier6.md) · [Halflings](eurobowl-26-halflings-tier6.md) · [Khorne](eurobowl-26-khorne-tier6.md) · [Orcos Negros](eurobowl-26-orcos-negros-tier6.md) · [Renegados del Caos](eurobowl-26-renegados-del-caos-tier6.md) |
| **7** | 1150k | 270k | 50k | [Ogros](eurobowl-26-ogros-tier7.md) |

## Origen de las builds

- **Base:** capturas del builder del vídeo [AndyDavo — Eurobowl Ruleset Review 2026](https://www.youtube.com/watch?v=wrmKRBFNqcM) (abr. 2026, BETA), adaptadas al presupuesto FINAL (cada lista explica el cambio en «Notas de la build»).
- **Ajustes:** [Artemis Black — Road to Eurobowl 2026](https://www.youtube.com/@ArtemisBlackBB) (sept. 2026) en Altos Elfos, Humanos y Unión Élfica.
- **Goblins:** diseño propio (sin captura).
- Inventario completo de fuentes: [fuentes de rosters](../../source/referencias-rosters-torneos.md).

!!! warning "Antes del torneo"
    Listas **válidas en cifras** según la lámina FINAL (incentivos y estrellas incluidos), sin revisión táctica propia.

## Cómo modificar una lista

1. Editar el equipo en `_final_data_g1.py` … `_final_data_g4.py` (posiciones y habilidades con los nombres exactos de `source/teams/` y `source/habilidades/`).
2. Validar: `python3 rosters/eurobowl-2026/_build_final.py` (o `--check <slug>`).
3. Generar los `.md`: `python3 rosters/eurobowl-2026/_build_final.py --write`.
