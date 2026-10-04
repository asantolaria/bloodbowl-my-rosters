# Skavens — EuroBowl 2026 (Tier 2)

![Skavens](../../source/images/equipos/skavens.webp)

> **#euro26 · [reglamento EuroBowl 2026](../../source/tiers/eurobowl-2026.md).** Posiciones y costes: [`source/teams/skavens.md`](../../source/teams/skavens.md). Generado con `_build_rosters.py`.
>
> **Origen de la build:** [AndyDavo — Eurobowl Ruleset Review 2026](https://www.youtube.com/watch?v=wrmKRBFNqcM) (abr. 2026, reglamento preliminar); mismo tier y presupuesto en el reglamento actual, sin cambios.
>
> **Estado competitivo:** válida en cifras; revisión táctica propia pendiente.

## Presupuesto

| Concepto | Disponible | Usado |
|----------|-----------|-------|
| **Presupuesto de equipo** | 1.070.000 M.O. | 1.070.000 M.O. |
| **Skill Gold** | 140.000 M.O. | 160.000 M.O. |
| **Flowing Funds** | 20.000 M.O. | 0 → equipo · 20.000 → Skill Gold |

## Alineación

*Rellenar nombres. Habilidades compradas con Skill Gold en **negrita**.*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades | Skill Gold |
|----|--------|----------|-------|----|----|----|----|----|-------------|------------|
| 1 | ____ | Rata Ogro | 150k | 6 | 5 | 4+ | 6+ | 9+ | Ferocidad animal, Cola prensil, Furia, Golpe mortífero, Solitario (4+), **Imparable** | Primaria 20k |
| 2 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón, **Abrirse paso** | Primaria 20k |
| 3 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón, **Abrirse paso** | Primaria 20k |
| 4 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar, **Forcejear** | Primaria 20k |
| 5 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar, **Forcejear** | Primaria 20k |
| 6 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | **Forcejear** | Primaria 20k |
| 7 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | **Forcejear** | Primaria 20k |
| 8 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | **Forcejear** | Primaria 20k |
| 9 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – | – |
| 10 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – | – |
| 11 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – | – |
| 12 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | – | – |

**Total jugadores:** 12

| Concepto | Coste |
|----------|--------|
| Jugadores | 850.000 |
| Segundas oportunidades (3 × 50.000) | 150.000 |
| Apotecario | 50.000 |
| Ayudantes del entrenador (2 × 10.000) | 20.000 |
| **Total** | **1.070.000** |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Abrirse paso](../../source/habilidades/fuerza.md)** (*Break Tackle* · Fuerza · Activa): **Una vez por turno**, al **intentar esquivar**: **+1** al AG si **FU ≤ 3**, **+2** si **FU = 4**, **+3** si **FU ≥ 5**.
- **[Apuñalar](../../source/habilidades/rasgos.md)** (*Stab* · Rasgo · Activa): Acción **Apuñalar** (sin límite por turno): rival **en pie** adyacente, **Armadura** sin mods.; si rompe → **Heridas**. Puede **sustituir** Placaje en **Penetración** (activación termina igualmente).
- **[Cola prensil](../../source/habilidades/mutaciones.md)** (*Prehensile Tail* · Mutaciones · Activa): **-1** adicional al AG de rivales que **esquivan, saltan o brincan** desde su zona de defensa. **Solo uno** por intento de salida.
- **[Esquivar](../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Ferocidad animal](../../source/habilidades/rasgos.md)** (*Animal Savagery* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+2** si Placaje/Penetración). **4+** OK; **1–3** ataca **compañero adyacente en pie** (derribo); sin cambio de turno salvo que llevara el balón; con **Garras**/**Golpe mortífero** debe usarlos vs compañero; después puede seguir su activación (FAQ). **1–3** sin compañero adyacente → **Distraído**.
- **[Forcejear](../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe mortífero](../../source/habilidades/fuerza.md)** (*Mighty Blow* · Fuerza · Activa (Elite)): Si **derriba** a un rival en **Placaje** (aunque él también quede derribado), **+1** a **Armadura** **o** a **Heridas** (eliges **después** de tirar ese dado).
- **[Imparable](../../source/habilidades/fuerza.md)** (*Juggernaut* · Fuerza · Activa): En **Penetración**: cada **Ambos derribados** en sus Placajes cuenta como **Empujón**. Rivales **no** pueden **Forcejear**, **Mantenerse firme** ni **Zafarse** frente a sus Placajes en esa Penetración.
- **[Placar](../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Robar balón](../../source/habilidades/general.md)** (*Strip Ball* · General · Activa): Placaje al **portador** y **empuje**: el balón **cae y rebota** desde la casilla de destino **antes** de que el rival quede tumbado, pero **después** de que **este jugador** elija si hace **impulso**.
- **[Solitario](../../source/habilidades/rasgos.md)** (*Loner* · Rasgo · Pasiva (obligatoria)): Para usar **Segunda oportunidad**: **1D6** vs número entre paréntesis; si falla **no** repite pero **gasta** el reroll.

<!-- habilidades-roster:fin -->


## Skill Gold

Un avance por jugador. Secundarias: **0/3** · Stacks: **0/3**.

| Jugador (Nº) | Avance | Tipo | Coste |
|--------------|--------|------|-------|
| 1 Rata Ogro | Imparable | Primaria | 20.000 |
| 2 Blitzer | Abrirse paso | Primaria | 20.000 |
| 3 Blitzer | Abrirse paso | Primaria | 20.000 |
| 4 Gutter Runner | Forcejear | Primaria | 20.000 |
| 5 Gutter Runner | Forcejear | Primaria | 20.000 |
| 6 Linemen | Forcejear | Primaria | 20.000 |
| 7 Linemen | Forcejear | Primaria | 20.000 |
| 8 Linemen | Forcejear | Primaria | 20.000 |
| **Total** | | | **160.000** |

## Notas de la build

- Forcejear en Gutter Runners y 3 Linemen; Abrirse paso en los Blitzers; Rata Ogro con Imparable.
- 3 segundas oportunidades baratas (50k) y 2 ayudantes.
- Tier 2 igual en el reglamento de abril y en el actual: la lista se mantiene.
