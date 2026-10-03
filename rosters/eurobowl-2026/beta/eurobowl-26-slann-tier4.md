# Slann — EuroBowl 2026 (Tier 4, Team Budget 1100k)

![Slann](../../../source/images/equipos/slann.webp)

> **#euro26** — [EuroBowl 2026](../../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Lista alineada con captura del builder (vídeo [EuroBowl / listas — YouTube](https://www.youtube.com/watch?v=wrmKRBFNqcM)). Lista nueva **Slann** (costes/stats distintos del bloque antiguo Kroxigor en `slann.md`); validar con PDF GW / Nuffle cuando actualicen la ficha.

> **Estado:** plantilla **desde captura**. **13 jugadores**. No regenerar con `_build_rosters.py` (ver `SKIP_EMIT`). Tag: `eurobowl-2026-wip-competitive`.

## Presupuesto EuroBowl (tier 4)

| Concepto | Valor |
|----------|--------|
| **Tier** | 4 |
| **Team Budget (base)** | 1.100.000 M.O. |
| **Skill Gold (pool)** | 190.000 M.O. |
| **Flowing Funds (máx.)** | 30.000 M.O. |

*En la captura: **Team budget** 1100k / 1100k; **Skill Gold** 220k / 190k (**190k** pool + **30k** Flowing a Skill Gold = **220k** en avances); **Flowing Funds** 30k / 30k.*

## Alineación

*En **negrita**, avances de Skill Gold. Nombres de posición en inglés del builder (**Slann Blitzer**, etc.). **Diving Catch** → **Atrapada de inmersión** (nombre habitual; contrastar con PDF GW).*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|-----|-------------|
| 1 | ____ | Slann Blitzer | 100k | 7 | 3 | 3+ | 4+ | 9+ | Placaje heroico, Golpe a la carrera, En pie de un salto, Pogo saltarín, **Placar** |
| 2 | ____ | Slann Catcher | 80k | 7 | 2 | 2+ | 3+ | 8+ | Atento al balón, Atrapada de inmersión, Piernas muy largas, Pogo saltarín, **Esquivar** |
| 3 | ____ | Slann Catcher | 80k | 7 | 2 | 2+ | 3+ | 8+ | Atento al balón, Atrapada de inmersión, Piernas muy largas, Pogo saltarín, **Vigilar** |
| 4 | ____ | Slann Blitzer | 100k | 7 | 3 | 3+ | 4+ | 9+ | Placaje heroico, Golpe a la carrera, En pie de un salto, Pogo saltarín, **Forcejeo** |
| 5 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín, **Forcejeo** |
| 6 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín, **Forcejeo** |
| 7 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín, **Robar balón**, **Forcejeo** |
| 8 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |
| 9 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |
| 10 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |
| 11 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |
| 12 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |
| 13 | ____ | Slann Lineman | 60k | 6 | 3 | 3+ | 4+ | 9+ | Pogo saltarín |

**Total jugadores:** 13 | **Suma jugadores:** 900.000 M.O.

**Desglose presupuesto de equipo (captura):**

| Concepto | Coste |
|----------|--------|
| Jugadores (2×100k + 2×80k + 9×60k) | 900.000 |
| Rerolls de equipo (4 × 50.000) | 200.000 |
| Apotecario | 0 |
| Asistentes / cheerleaders / Hinchas | 0 |
| **Total gastado** | **1.100.000** |
| **Team Budget base (tier 4)** | 1.100.000 |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Atento al balón](../../../source/habilidades/pase.md)** (*On the Ball* · Pase · Activa): Tras **objetivo** de **Pase** rival y **antes** del chequeo de Pase: mueve **hasta 3** (sin forzar marcha); si **cae**, termina el movimiento y sigue el pase. Varios con la habilidad **uno tras otro**. Tras **desvío** en inicio, **un** desmarcado receptor puede mover **hasta 3** antes del evento de patada (**no** con recepción libre; **no** cruzar mitad rival).
- **[Defensa](../../../source/habilidades/fuerza.md)** (*Guard* · Fuerza · Activa (Elite)): Siempre puede **apoyar** (ofensivo y defensivo) en Placajes aunque lo marquen **varios** rivales.
- **[En pie de un salto](../../../source/habilidades/agilidad.md)** (*Jump Up* · Agilidad · Activa): **Tumbado boca arriba:** puede levantarse sin gastar **tres** casillas de movimiento. Puede declarar **Placaje** estando así: chequeo de **AG con +1**; si falla, sigue tumbado y termina la activación.
- **[Esquivar](../../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Forcejear](../../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Golpe a la carrera](../../../source/habilidades/agilidad.md)** (*Hit and Run* · Agilidad · Activa): Tras **Placaje** o acción especial **Apuñalar**, si sigue **en pie**: mueve **1 casilla** gratis ignorando zonas de defensa; al acabar **no** puede estar marcado ni marcando. **No** puede tener **Furia**.
- **[Piernas muy largas](../../../source/habilidades/mutaciones.md)** (*Very Long Legs* · Mutaciones · Activa): **+1** al AG al **brincar** o **saltar**; **+2** al **interceptar**. **Ignora Partenubes**.
- **[Placaje heroico](../../../source/habilidades/agilidad.md)** (*Diving Tackle* · Agilidad · Activa): Rival que **esquivando, saltando o brincando** sale de su zona de defensa: **después** de su chequeo de AG (con mods. y repeticiones), este jugador aplica **-2** al rival y se coloca **tumbado boca arriba** en la casilla que deja. **Solo uno** por intento de salida si varios tienen la habilidad.
- **[Placar](../../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Pogo saltarín](../../../source/habilidades/rasgos.md)** (*Pogo* · Rasgo · Activa): **Pogo** sobre una casilla adyacente como **Brincar** pero **ignora** mods. negativos. **No** puede tener **Saltar**.
- **[Recepción heroica](../../../source/habilidades/agilidad.md)** (*Diving Catch* · Agilidad · Activa): Puede intentar atrapar si el balón **cae** en su zona de defensa por **pase**, **patada inicial** o **devolución** (**no** si solo **rebota** ahí). **+1** al AG al atrapar como parte de un **Pase** si está en la **casilla objetivo**.
- **[Robar balón](../../../source/habilidades/general.md)** (*Strip Ball* · General · Activa): Placaje al **portador** y **empuje**: el balón **cae y rebota** desde la casilla de destino **antes** de que el rival quede tumbado, pero **después** de que **este jugador** elija si hace **impulso**.

<!-- habilidades-roster:fin -->


## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF / EuroBowl** | 4 |
| **Team Budget (captura)** | 1100k / 1100k |
| **Skill Gold (captura)** | 220k / 190k (+30k Flowing) |
| **Flowing Funds (captura)** | 30k / 30k |
| **Rerolls** | 4 |
| **Apotecario** | No |
| **Inducements** | Ninguno |
| **Opción listas** | Sin estrellas |
| **Liga (captura EN)** | Lustrian Superleague |
| **Equivalencia repo (ES)** | **Superliga Lustriana** (cf. `amazonas.md`, `slann.md`) |

## Skill Gold — avances (según captura)

**Siete** bloques (el Slann Lineman #7 usa **Stack** de dos primarias). Desglose que suma **220.000 M.O.** (el builder marca **Vigilar** en verde en un Catcher = secundaria típica):

| Nº | Jugador | Habilidad (EN → ES) | Tipo (referencia #euro26) | Coste Skill Gold |
|----|---------|---------------------|---------------------------|------------------|
| 1 | Slann Blitzer | Block → **Placar** | Sec. General no élite | 40.000 |
| 2 | Slann Catcher | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 3 | Slann Catcher | Guard → **Vigilar** | Sec. Fuerza **élite** | 50.000 |
| 4 | Slann Blitzer | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| 5 | Slann Lineman | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| 6 | Slann Lineman | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| 7 | Slann Lineman | Strip Ball + Wrestle → **Robar balón** + **Forcejeo** | **Stack** (2× prim. no élite) | 50.000 |
| | **Total Skill Gold** | | | **220.000** |

**Límites #euro26:** **1** Stack; **2** secundarios no élite + **1** secundario **élite** (o reclasifica si el pack cuenta distinto); **0** primarias **élite** sueltas en este desglose salvo la línea de **Vigilar** sec. élite.

*Si **Vigilar** en Catcher #3 es **secundaria no élite** (40k), el total baja **10k**; añade **élite** en otro avance o reclasifica **Placar** en Blitzer #1 para mantener **220k**.*

## Estrellas (Tiers 1–4)

Sin Veterans ni Legends en la captura. Listas: [`eurobowl-2026.md`](../../../source/tiers/eurobowl-2026.md).

## Inducements

Solo los permitidos en `eurobowl-2026.md`. Captura: ninguno.

## Estrategia (breve)

- **Blitzers:** cadena **Placaje heroico** / **Golpe a la carrera** / **Pogo**; uno con **Placar** y otro con **Forcejeo**.
- **Catchers:** **Esquivar** y **Vigilar** con **Piernas muy largas** y **Atento al balón**.
- **Líneas:** **Forcejeo** y **Stack Robar balón + Forcejeo** en una pieza; resto **Pogo** para movilidad.

## Progresión sugerida

Cuando `source/teams/slann.md` unifique lista antigua y nueva Slann, seguir tablas de primarias/secundarias por posición en esa ficha.
