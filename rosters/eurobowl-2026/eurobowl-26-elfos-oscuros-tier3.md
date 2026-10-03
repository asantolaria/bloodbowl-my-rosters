# Elfos Oscuros — EuroBowl 2026 FINAL (Tier 3)

![Elfos Oscuros](../../source/images/equipos/elfos-oscuros.webp)

> **#euro26 · reglamento [FINAL](../../source/tiers/eurobowl-2026-final.md).** Posiciones y costes: [`source/teams/elfos-oscuros.md`](../../source/teams/elfos-oscuros.md). Generado con `_build_final.py`.
>
> **Origen de la build:** [AndyDavo — Eurobowl Ruleset Review 2026](https://www.youtube.com/watch?v=wrmKRBFNqcM) (abr. 2026, BETA); mismo tier y presupuesto en FINAL, sin cambios.
>
> **Estado competitivo:** válida en cifras; revisión táctica propia pendiente.

## Presupuesto

| Concepto | Disponible | Usado |
|----------|-----------|-------|
| **Presupuesto de equipo** | 1.080.000 M.O. | 1.075.000 M.O. |
| **Skill Gold** | 160.000 M.O. | 190.000 M.O. |
| **Flowing Funds** | 30.000 M.O. | 0 → equipo · 30.000 → Skill Gold |

## Alineación

*Rellenar nombres. Habilidades compradas con Skill Gold en **negrita**.*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades | Skill Gold |
|----|--------|----------|-------|----|----|----|----|----|-------------|------------|
| 1 | ____ | Bruja Elfa | 110k | 7 | 3 | 2+ | 4+ | 8+ | En pie de un salto, Esquivar, Furia, **Forcejear** | Primaria 20k |
| 2 | ____ | Bruja Elfa | 110k | 7 | 3 | 2+ | 4+ | 8+ | En pie de un salto, Esquivar, Furia, **Forcejear** | Primaria 20k |
| 3 | ____ | Elfo Oscuro Blitzer | 105k | 7 | 3 | 2+ | 3+ | 9+ | Placar, **Esquivar** | Primaria élite 30k |
| 4 | ____ | Elfo Oscuro Blitzer | 105k | 7 | 3 | 2+ | 3+ | 9+ | Placar, **Esquivar** | Primaria élite 30k |
| 5 | ____ | Elfo Oscuro Asesino | 90k | 7 | 3 | 2+ | 4+ | 8+ | Apuñalar, Golpe a la carrera, Perseguir, **Esquivar** | Primaria élite 30k |
| 6 | ____ | Elfo Oscuro Runner | 80k | 7 | 3 | 2+ | 3+ | 8+ | Pase precipitado, Patada de despeje, **Líder** | Primaria 20k |
| 7 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | **Forcejear** | Primaria 20k |
| 8 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | **Forcejear** | Primaria 20k |
| 9 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | – | – |
| 10 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | – | – |
| 11 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | – | – |

**Total jugadores:** 11

| Concepto | Coste |
|----------|--------|
| Jugadores | 925.000 |
| Segundas oportunidades (2 × 50.000) | 100.000 |
| Apotecario | 50.000 |
| **Total** | **1.075.000** |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Apuñalar](../../source/habilidades/rasgos.md)** (*Stab* · Rasgo · Activa): Acción **Apuñalar** (sin límite por turno): rival **en pie** adyacente, **Armadura** sin mods.; si rompe → **Heridas**. Puede **sustituir** Placaje en **Penetración** (activación termina igualmente).
- **[En pie de un salto](../../source/habilidades/agilidad.md)** (*Jump Up* · Agilidad · Activa): **Tumbado boca arriba:** puede levantarse sin gastar **tres** casillas de movimiento. Puede declarar **Placaje** estando así: chequeo de **AG con +1**; si falla, sigue tumbado y termina la activación.
- **[Esquivar](../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Forcejear](../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe a la carrera](../../source/habilidades/agilidad.md)** (*Hit and Run* · Agilidad · Activa): Tras **Placaje** o acción especial **Apuñalar**, si sigue **en pie**: mueve **1 casilla** gratis ignorando zonas de defensa; al acabar **no** puede estar marcado ni marcando. **No** puede tener **Furia**.
- **[Líder](../../source/habilidades/pase.md)** (*Leader* · Pase · Pasiva): Con **≥1** con Líder **en campo** al inicio de cualquier mitad: gana **Segunda oportunidad de Líder** (como reroll normal salvo que **Chef Maestro Halfling** no la quite). Si **todos** los Líder salen **antes** de usarla, se **pierde**.
- **[Pase precipitado](../../source/habilidades/pase.md)** (*Dump-Off* · Pase · Activa): Antes de resolver **Placaje** o acción especial que lo **tome como blanco**: **Pase rápido** (no puede provocar cambio de turno; luego sigue la acción contra él).
- **[Patada de despeje](../../source/habilidades/pase.md)** (*Punt* · Pase · Activa): Acción especial **Patada de despeje** (**1** por turno): puede **Movimiento** antes; si tras mover es **portador**, plantilla de devolución, **1D6** dirección + **1D6** distancia (**Patada** puede repetir una o ambas, decidiendo dirección antes de distancia). Ocupa → atrapar o rebote. **No** cambio si balón al suelo; **sí** si rival lo tiene o va al público.
- **[Perseguir](../../source/habilidades/triquinuelas.md)** (*Shadowing* · Triquiñuelas · Activa): Rival **esquiva** saliendo de su ZD: **1D6** **4+** → ocupa la casilla vacada (**máx.** **MV** veces por turno). **Solo uno** por intento de salida.
- **[Placar](../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.

<!-- habilidades-roster:fin -->




## Skill Gold

Un avance por jugador. Secundarias: **0/3** · Stacks: **0/3**.

| Jugador (Nº) | Avance | Tipo | Coste |
|--------------|--------|------|-------|
| 1 Bruja Elfa | Forcejear | Primaria | 20.000 |
| 2 Bruja Elfa | Forcejear | Primaria | 20.000 |
| 3 Elfo Oscuro Blitzer | Esquivar | Primaria élite | 30.000 |
| 4 Elfo Oscuro Blitzer | Esquivar | Primaria élite | 30.000 |
| 5 Elfo Oscuro Asesino | Esquivar | Primaria élite | 30.000 |
| 6 Elfo Oscuro Runner | Líder | Primaria | 20.000 |
| 7 Elfo Oscuro Línea | Forcejear | Primaria | 20.000 |
| 8 Elfo Oscuro Línea | Forcejear | Primaria | 20.000 |
| **Total** | | | **190.000** |

## Notas de la build

- Esquivar en Blitzers y Asesino; Forcejear en Brujas y 2 Líneas; Runner con Líder.
- Los 30k de Flowing van íntegros a Skill Gold (190k); sobran 5k de equipo.
- Tier 3 igual en BETA y FINAL: la lista se mantiene.
