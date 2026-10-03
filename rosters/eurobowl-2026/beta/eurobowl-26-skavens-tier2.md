# Skavens — EuroBowl 2026 (Tier 2, Team Budget 1070k)

![Skavens](../../../source/images/equipos/skavens.webp)

> **#euro26** — [EuroBowl 2026](../../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Posiciones y costes: [`source/teams/skavens.md`](../../../source/teams/skavens.md).

> **Estado competitivo:** presupuesto EuroBowl válido en cifras; **sin revisión meta**. Repaso táctico pendiente — [README `eurobowl-2026`](../README.md) · tag `eurobowl-2026-wip-competitive`.

## Presupuesto EuroBowl

| Concepto | Valor |
|----------|--------|
| **Tier** | 2 |
| **Team Budget (base)** | 1070.000 M.O. |
| **Skill Gold (pool)** | 140.000 M.O. |
| **Flowing Funds (máx.)** | 20.000 M.O. |

*Desglose de equipo = **1070k** M.O. (debe coincidir con Team Budget base + la parte de Flowing que asignes al equipo). Resto de Flowing puede ir a Skill Gold.*

## Alineación (gasto de presupuesto de equipo)

*Sin avances de Skill Gold. Rellenar nombres. Texto de habilidades resumido.*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|----|-------------|
| 1 | ____ | Rata Ogro | 150k | 6 | 5 | 4+ | — | 9+ | Ferocidad animal, … |
| 2 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón |
| 3 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón |
| 4 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 5 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 6 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 7 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 8 | ____ | Thrower | 80k | 7 | 3 | 3+ | 2+ | 8+ | Manos seguras, Pasar |
| 9 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – |
| 10 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – |
| 11 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – |
| 12 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – |

**Total jugadores:** 12 | **Presupuesto equipo usado:** 1070k M.O.

| Concepto | Coste |
|----------|--------|
| Jugadores (total 950k) | 950.000 |
| Rerolls (2 × 50.000) | 100.000 |
| Apotecario | No (lista del equipo) |
| Hinchas (2 × 10.000) | 20.000 |
| **Total** | **1.070.000** |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Apuñalar](../../../source/habilidades/rasgos.md)** (*Stab* · Rasgo · Activa): Acción **Apuñalar** (sin límite por turno): rival **en pie** adyacente, **Armadura** sin mods.; si rompe → **Heridas**. Puede **sustituir** Placaje en **Penetración** (activación termina igualmente).
- **[Cola prensil](../../../source/habilidades/mutaciones.md)** (*Prehensile Tail* · Mutaciones · Activa): **-1** adicional al AG de rivales que **esquivan, saltan o brincan** desde su zona de defensa. **Solo uno** por intento de salida.
- **[Esquivar](../../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Ferocidad animal](../../../source/habilidades/rasgos.md)** (*Animal Savagery* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+2** si Placaje/Penetración). **4+** OK; **1–3** ataca **compañero adyacente en pie** (derribo); sin cambio de turno salvo que llevara el balón; con **Garras**/**Golpe mortífero** debe usarlos vs compañero; después puede seguir su activación (FAQ). **1–3** sin compañero adyacente → **Distraído**.
- **[Furia](../../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe mortífero](../../../source/habilidades/fuerza.md)** (*Mighty Blow* · Fuerza · Activa (Elite)): Si **derriba** a un rival en **Placaje** (aunque él también quede derribado), **+1** a **Armadura** **o** a **Heridas** (eliges **después** de tirar ese dado).
- **[Manos seguras](../../../source/habilidades/general.md)** (*Sure Hands* · General · Activa): Puede **repetir** el **D6** al **recoger** el balón (**no** en **Asegurar el balón**). **Robar balón** **no** puede usarse contra él.
- **[Pasar](../../../source/habilidades/pase.md)** (*Pass* · Pase · Activa): Puede **repetir** cualquier chequeo de **Pase** fallido en acción de **Pase**.
- **[Placar](../../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Robar balón](../../../source/habilidades/general.md)** (*Strip Ball* · General · Activa): Placaje al **portador** y **empuje**: el balón **cae y rebota** desde la casilla de destino **antes** de que el rival quede tumbado, pero **después** de que **este jugador** elija si hace **impulso**.
- **[Solitario](../../../source/habilidades/rasgos.md)** (*Loner* · Rasgo · Pasiva (obligatoria)): Para usar **Segunda oportunidad**: **1D6** vs número entre paréntesis; si falla **no** repite pero **gasta** el reroll.

<!-- habilidades-roster:fin -->


## Skill Gold — avances (ejemplo editable)

Cada jugador: **un solo bloque** de avance. Máx. **3** Secondary y **3** Stack en todo el equipo. Costes: ver tabla en [`eurobowl-2026.md`](../../../source/tiers/eurobowl-2026.md).

| Jugador (Nº) | Tipo | Coste (Skill Gold) |
|--------------|------|---------------------|
| _pendiente_ | 1 primaria no élite | 20.000 |

**Pool Skill Gold base:** 140.000 M.O. (+ Flowing si lo asignas).

## Estrellas (Tiers 1–4)

Sin Veterans ni Legends. Con estrella (tier 5–6): no avances Secondary ni Stack en jugadores de plantilla.

## Inducements

Solo los listados como permitidos en `eurobowl-2026.md`.
