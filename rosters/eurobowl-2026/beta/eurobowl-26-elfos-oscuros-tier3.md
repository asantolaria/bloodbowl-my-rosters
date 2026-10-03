# Elfos Oscuros — EuroBowl 2026 (Tier 3, Team Budget 1080k)

![Elfos Oscuros](../../../source/images/equipos/elfos-oscuros.webp)

> **#euro26** — [EuroBowl 2026](../../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Lista alineada con captura del builder (vídeo [EuroBowl / listas — YouTube](https://www.youtube.com/watch?v=wrmKRBFNqcM)). Posiciones: [`source/teams/elfos-oscuros.md`](../../../source/teams/elfos-oscuros.md).

> **Estado:** plantilla **desde captura**. **11 jugadores**. No regenerar con `_build_rosters.py` (ver `SKIP_EMIT`). Tag: `eurobowl-2026-wip-competitive`.

## Presupuesto EuroBowl (tier 3)

| Concepto | Valor |
|----------|--------|
| **Tier** | 3 |
| **Team Budget (base)** | 1.080.000 M.O. |
| **Skill Gold (pool)** | 160.000 M.O. |
| **Flowing Funds (máx.)** | 30.000 M.O. |

*En la captura: **Team budget** 1075k / 1080k (**1075k** gastados; **5k** del presupuesto base sin usar); **Skill Gold** 190k / 160k (**160k** pool + **30k** Flowing a Skill Gold = **190k** en avances); **Flowing Funds** 30k / 30k.*

## Alineación

*En **negrita**, avances de Skill Gold. Las **tres** líneas sin subidas cuestan **65k** cada una en lista BB2025 (la captura EN puede mostrar **50k** por error de etiqueta en el builder; aquí se usa el coste de `elfos-oscuros.md`).*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|-----|-------------|
| 1 | ____ | Bruja Elfa | 110k | 7 | 3 | 2+ | 4+ | 8+ | Esquivar, Furia, En pie de un salto, **Forcejeo** |
| 2 | ____ | Bruja Elfa | 110k | 7 | 3 | 2+ | 4+ | 8+ | Esquivar, Furia, En pie de un salto, **Forcejeo** |
| 3 | ____ | Elfo Oscuro Blitzer | 105k | 7 | 3 | 2+ | 3+ | 9+ | Placar, **Esquivar** |
| 4 | ____ | Elfo Oscuro Blitzer | 105k | 7 | 3 | 2+ | 3+ | 9+ | Placar, **Esquivar** |
| 5 | ____ | Elfo Oscuro Asesino | 90k | 7 | 3 | 2+ | 4+ | 8+ | Golpe a la carrera, Perseguir, Apuñalar, **Esquivar** |
| 6 | ____ | Elfo Oscuro Runner | 80k | 7 | 3 | 2+ | 3+ | 8+ | Pase precipitado, Patada de despeje, **Líder** |
| 7 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | **Forcejeo** |
| 8 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | **Forcejeo** |
| 9 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | — |
| 10 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | — |
| 11 | ____ | Elfo Oscuro Línea | 65k | 6 | 3 | 2+ | 3+ | 9+ | — |

**Total jugadores:** 11 | **Suma jugadores:** 925.000 M.O.

**Desglose presupuesto de equipo (captura):**

| Concepto | Coste |
|----------|--------|
| Jugadores (2×110k + 2×105k + 90k + 80k + 5×65k) | 925.000 |
| Rerolls de equipo (2 × 50.000) | 100.000 |
| Apotecario | 50.000 |
| Asistentes / cheerleaders / Hinchas | 0 |
| **Total gastado** | **1.075.000** |
| **Team Budget base (tier 3)** | 1.080.000 |
| **Presupuesto equipo sin usar (captura)** | 5.000 |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Apuñalar](../../../source/habilidades/rasgos.md)** (*Stab* · Rasgo · Activa): Acción **Apuñalar** (sin límite por turno): rival **en pie** adyacente, **Armadura** sin mods.; si rompe → **Heridas**. Puede **sustituir** Placaje en **Penetración** (activación termina igualmente).
- **[En pie de un salto](../../../source/habilidades/agilidad.md)** (*Jump Up* · Agilidad · Activa): **Tumbado boca arriba:** puede levantarse sin gastar **tres** casillas de movimiento. Puede declarar **Placaje** estando así: chequeo de **AG con +1**; si falla, sigue tumbado y termina la activación.
- **[Esquivar](../../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Forcejear](../../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe a la carrera](../../../source/habilidades/agilidad.md)** (*Hit and Run* · Agilidad · Activa): Tras **Placaje** o acción especial **Apuñalar**, si sigue **en pie**: mueve **1 casilla** gratis ignorando zonas de defensa; al acabar **no** puede estar marcado ni marcando. **No** puede tener **Furia**.
- **[Líder](../../../source/habilidades/pase.md)** (*Leader* · Pase · Pasiva): Con **≥1** con Líder **en campo** al inicio de cualquier mitad: gana **Segunda oportunidad de Líder** (como reroll normal salvo que **Chef Maestro Halfling** no la quite). Si **todos** los Líder salen **antes** de usarla, se **pierde**.
- **[Pase precipitado](../../../source/habilidades/pase.md)** (*Dump-Off* · Pase · Activa): Antes de resolver **Placaje** o acción especial que lo **tome como blanco**: **Pase rápido** (no puede provocar cambio de turno; luego sigue la acción contra él).
- **[Patada de despeje](../../../source/habilidades/pase.md)** (*Punt* · Pase · Activa): Acción especial **Patada de despeje** (**1** por turno): puede **Movimiento** antes; si tras mover es **portador**, plantilla de devolución, **1D6** dirección + **1D6** distancia (**Patada** puede repetir una o ambas, decidiendo dirección antes de distancia). Ocupa → atrapar o rebote. **No** cambio si balón al suelo; **sí** si rival lo tiene o va al público.
- **[Perseguir](../../../source/habilidades/triquinuelas.md)** (*Shadowing* · Triquiñuelas · Activa): Rival **esquiva** saliendo de su ZD: **1D6** **4+** → ocupa la casilla vacada (**máx.** **MV** veces por turno). **Solo uno** por intento de salida.
- **[Placar](../../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.

<!-- habilidades-roster:fin -->


## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF / EuroBowl** | 3 |
| **Team Budget (captura)** | 1075k / 1080k (5k sin gastar) |
| **Skill Gold (captura)** | 190k / 160k (+30k Flowing) |
| **Flowing Funds (captura)** | 30k / 30k |
| **Rerolls** | 2 |
| **Apotecario** | Sí |
| **Inducements** | Ninguno |
| **Opción listas** | Sin estrellas |
| **Liga (captura EN)** | Elven Kingdom League |
| **Equivalencia repo (ES)** | **Liga de los Reinos Élficos** (`elfos-oscuros.md`) |

## Skill Gold — avances (según captura)

**Ocho** jugadores con **un** bloque de avance cada uno. Desglose **orientativo** que suma **190.000 M.O.** (ajusta tipos si tu builder etiqueta distinto):

| Nº | Jugador | Habilidad (EN → ES) | Tipo (referencia #euro26) | Coste Skill Gold |
|----|---------|---------------------|---------------------------|------------------|
| 1 Bruja Elfa | Wrestle → **Forcejeo** | Sec. General no élite | 40.000 |
| 2 Bruja Elfa | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| 3 Blitzer | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 4 Blitzer | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 5 Asesino | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 6 Runner | Leader → **Líder** | Prim. General **élite** | 30.000 |
| 7 Línea | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| 8 Línea | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| **Total Skill Gold** | | | **190.000** |

**Límites #euro26:** **1** secundario en este desglose; **1** primaria **élite**; **0** Stack.

*Si **Forcejeo** en Brujas / Líneas cuenta todo como **secundaria** (40k), el total sube por encima de **190k** salvo que otras filas bajen de coste (p. ej. **Líder** no élite a **20k**). Mantén **190k** y los techos del pack al alinear con el export del torneo.*

## Estrellas (Tiers 1–4)

Sin Veterans ni Legends en la captura. Listas: [`eurobowl-2026.md`](../../../source/tiers/eurobowl-2026.md).

## Inducements

Solo los permitidos en `eurobowl-2026.md`. Captura: ninguno.

## Estrategia (breve)

- **Brujas** con **Forcejeo** y **Furia** para cadena y bajar portadores; **Blitzers** con **Placar** y **Esquivar** en cabeza.
- **Asesino** con **Esquivar** y kit de **Apuñalar** / **Perseguir**; **Runner** con **Líder** y despeje.
- **Líneas** con **Forcejeo** en dos piezas y tres **65k** «limpios» para marcaje y TV.

## Progresión sugerida

Tras #euro26, seguir tablas **AG / AD / DF / GF / GP** de `elfos-oscuros.md` por posición.
