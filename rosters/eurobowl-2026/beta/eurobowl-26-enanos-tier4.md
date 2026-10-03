# Enanos — EuroBowl 2026 (Tier 4, Team Budget 1100k)

![Enanos](../../../source/images/equipos/enanos.webp)

> **#euro26** — [EuroBowl 2026](../../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Lista alineada con captura del builder en YouTube (*Blood Bowl Eurobowl Ruleset Review — 2026*, canal **AndyDavo's Blood Bowl**). Posiciones y habilidades base: [`source/teams/enanos.md`](../../../source/teams/enanos.md). En inglés GW la posición **Troll Slayer** = **MataTrols** en la ficha en español del repo.

> **Estado:** plantilla **desde captura**. **11 jugadores** (sin Apisonadora Enana en esta lista). No regenerar con `_build_rosters.py` (ver `SKIP_EMIT`). Tag: `eurobowl-2026-wip-competitive`.

## Presupuesto EuroBowl (tier 4)

| Concepto | Valor |
|----------|--------|
| **Tier** | 4 |
| **Team Budget (base)** | 1.100.000 M.O. |
| **Skill Gold (pool)** | 190.000 M.O. |
| **Flowing Funds (máx.)** | 30.000 M.O. |

*En la captura: **Team budget** 1095k / 1100k (**1095k** gastados; **5k** sin usar); **Skill Gold** 220k / 190k (**190k** pool + **30k** Flowing a Skill Gold = **220k** en avances); **Flowing Funds** 30k / 30k.*

## Alineación

*En **negrita**, avances de Skill Gold. **Nº** como en la captura del builder (1–11).*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|-----|-------------|
| 1 | ____ | MataTrols | 95k | 5 | 3 | 4+ | 5+ | 9+ | Placar, Agallas, Furia, Cabeza dura, Odio (Troll), **Golpe mortífero** |
| 2 | ____ | MataTrols | 95k | 5 | 3 | 4+ | 5+ | 9+ | Placar, Agallas, Furia, Cabeza dura, Odio (Troll), **Vigilar** |
| 3 | ____ | Enano Blitzer | 100k | 5 | 3 | 4+ | 4+ | 10+ | Placar, Placaje heroico, Placaje defensivo, Cabeza dura, **Vigilar**, **Mantenerse firme** |
| 4 | ____ | Enano Blitzer | 100k | 5 | 3 | 4+ | 4+ | 10+ | Placar, Placaje heroico, Placaje defensivo, Cabeza dura, **Vigilar**, **Mantenerse firme** |
| 5 | ____ | Enano Runner | 80k | 6 | 3 | 3+ | 4+ | 9+ | Esprintar, Manos seguras, Cabeza dura, **Líder** |
| 6 | ____ | Enano Runner | 80k | 6 | 3 | 3+ | 4+ | 9+ | Esprintar, Manos seguras, Cabeza dura, **Forcejeo** |
| 7 | ____ | Enano Línea | 70k | 4 | 3 | 4+ | 5+ | 10+ | Placar, Romper defensas, Cabeza dura |
| 8 | ____ | Enano Línea | 70k | 4 | 3 | 4+ | 5+ | 10+ | Placar, Romper defensas, Cabeza dura |
| 9 | ____ | Enano Línea | 70k | 4 | 3 | 4+ | 5+ | 10+ | Placar, Romper defensas, Cabeza dura |
| 10 | ____ | Enano Línea | 70k | 4 | 3 | 4+ | 5+ | 10+ | Placar, Romper defensas, Cabeza dura |
| 11 | ____ | Enano Línea | 70k | 4 | 3 | 4+ | 5+ | 10+ | Placar, Romper defensas, Cabeza dura |

**Total jugadores:** 11 | **Suma jugadores:** 900.000 M.O.

**Desglose presupuesto de equipo (captura):**

| Concepto | Coste |
|----------|--------|
| Jugadores (2×95k + 2×100k + 2×80k + 5×70k) | 900.000 |
| Rerolls de equipo (2 × 60.000) | 120.000 |
| Apotecario | 50.000 |
| Team Mascot (×1; inducement permitido #euro26, **25k** según lista común GW / ver [`eurobowl-26-orcos-tier2.md`](eurobowl-26-orcos-tier2.md)) | 25.000 |
| Asistentes / cheerleaders / Hinchas | 0 |
| **Total gastado** | **1.095.000** |
| **Team Budget base (tier 4)** | 1.100.000 |
| **Presupuesto equipo sin usar (captura)** | 5.000 |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Agallas](../../../source/habilidades/general.md)** (*Dauntless* · General · Activa): En **Placaje** contra rival con **FU mayor** (**antes** de mods.): **1D6 + FU** propia; si el total **>** FU **sin modificar** del rival, su FU **iguala** al rival **solo** para ese Placaje; luego mods. normales. Con **Furia**, una tirada **por** Placaje.
- **[Cabeza dura](../../../source/habilidades/fuerza.md)** (*Thick Skull* · Fuerza · Pasiva): Tirada de **Heridas**: **Inconsciente** solo con **9**; **8** = **Aturdido**. Con **Escurridizo**: Inconsciente con **8**, **7** = Aturdido.
- **[Defensa](../../../source/habilidades/fuerza.md)** (*Guard* · Fuerza · Activa (Elite)): Siempre puede **apoyar** (ofensivo y defensivo) en Placajes aunque lo marquen **varios** rivales.
- **[Esprintar](../../../source/habilidades/agilidad.md)** (*Sprint* · Agilidad · Activa): En una acción de **Movimiento** puede intentar **forzar la marcha una vez más** de lo que podría normalmente.
- **[Forcejear](../../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe mortífero](../../../source/habilidades/fuerza.md)** (*Mighty Blow* · Fuerza · Activa (Elite)): Si **derriba** a un rival en **Placaje** (aunque él también quede derribado), **+1** a **Armadura** **o** a **Heridas** (eliges **después** de tirar ese dado).
- **[Líder](../../../source/habilidades/pase.md)** (*Leader* · Pase · Pasiva): Con **≥1** con Líder **en campo** al inicio de cualquier mitad: gana **Segunda oportunidad de Líder** (como reroll normal salvo que **Chef Maestro Halfling** no la quite). Si **todos** los Líder salen **antes** de usarla, se **pierde**.
- **[Manos seguras](../../../source/habilidades/general.md)** (*Sure Hands* · General · Activa): Puede **repetir** el **D6** al **recoger** el balón (**no** en **Asegurar el balón**). **Robar balón** **no** puede usarse contra él.
- **[Mantenerse firme](../../../source/habilidades/fuerza.md)** (*Stand Firm* · Fuerza · Activa): Ante **empuje** por Placaje (incl. cadena) puede **no moverse**. **No** bloquea el **segundo Placaje** de **Furia** si sigue en pie.
- **[Odio](../../../source/habilidades/rasgos.md)** (*Hatred* · Rasgo · Pasiva (obligatoria)): Placaje vs rival con clave entre paréntesis: puede **repetir un** resultado **Atacante derribado**.
- **[Placaje defensivo](../../../source/habilidades/general.md)** (*Tackle* · General · Activa): Rival que **esquive** para salir de su zona de defensa **no** puede usar **Esquivar**. Si **él** hace un Placaje y sale **Desequilibrado**, el rival se trata **como sin Esquivar**.
- **[Placaje heroico](../../../source/habilidades/agilidad.md)** (*Diving Tackle* · Agilidad · Activa): Rival que **esquivando, saltando o brincando** sale de su zona de defensa: **después** de su chequeo de AG (con mods. y repeticiones), este jugador aplica **-2** al rival y se coloca **tumbado boca arriba** en la casilla que deja. **Solo uno** por intento de salida si varios tienen la habilidad.
- **[Placar](../../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Romper defensas](../../../source/habilidades/agilidad.md)** (*Defensive* · Agilidad · Activa): En **turnos rivales**, rivales que esté **marcando** no pueden usar **Defensa** ni **Meter la bota**.

<!-- habilidades-roster:fin -->


## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF / EuroBowl** | 4 |
| **Team Budget (captura)** | 1095k / 1100k (5k sin gastar) |
| **Skill Gold (captura)** | 220k / 190k (+30k Flowing) |
| **Flowing Funds (captura)** | 30k / 30k |
| **Rerolls** | 2 |
| **Apotecario** | Sí |
| **Team Mascot** | 1 |
| **Inducements** | Ninguno más |
| **Opción listas** | Sin estrellas |
| **Ligas / reglas (captura EN)** | Worlds Edge Superleague; Brawlin' Brutes; Bribery and Corruption |
| **Equivalencia repo (ES)** | **Superliga del Fin del Mundo**; **Brutos brutales**; **Sobornos y corrupción** (`enanos.md`) |

## Skill Gold — avances (según captura)

**Seis** bloques (cada Blitzer **#3** y **#4** usa **Stack** de dos habilidades). Desglose que suma **220.000 M.O.** (reclasifica si el export del torneo marca **Golpe mortífero** / **Vigilar** (MataTrols #2) como primaria/secundaria distinta):

| Nº | Jugador | Habilidad (EN → ES) | Tipo (referencia #euro26) | Coste Skill Gold |
|----|---------|---------------------|---------------------------|------------------|
| 1 | MataTrols | Mighty Blow → **Golpe mortífero** | Prim. General **élite** | 30.000 |
| 2 | MataTrols | Guard → **Vigilar** | Sec. Fuerza **élite** | 50.000 |
| 3 | Enano Blitzer | Guard + Stand Firm → **Vigilar** + **Mantenerse firme** | **Stack** (2× prim. no élite) | 50.000 |
| 4 | Enano Blitzer | Guard + Stand Firm → **Vigilar** + **Mantenerse firme** | **Stack** (2× prim. no élite) | 50.000 |
| 5 | Enano Runner | Leader → **Líder** | Prim. General no élite | 20.000 |
| 6 | Enano Runner | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| | **Total Skill Gold** | | | **220.000** |

*Si **Golpe mortífero** en MataTrols **#1** cuenta como **primaria no élite** (20k), el total baja **10k**; sube **Vigilar** en MataTrols **#2** a **secundaria no élite** (40k) o ajusta otra fila permitida por el pack para mantener **220k**.*

**Límites #euro26:** **2** Stack (Blitzers **#3** y **#4**); **1** secundario **élite** (MataTrols **#2**); **0** secundarios no élite en este desglose base.

## Estrellas (Tiers 1–4)

Sin Veterans ni Legends en la captura. Listas: [`eurobowl-2026.md`](../../../source/tiers/eurobowl-2026.md).

## Inducements

Solo los permitidos en `eurobowl-2026.md`. En presupuesto de equipo: **Team Mascot** (ver desglose arriba).

## Estrategia (breve)

- **MataTrols:** uno con **Golpe mortífero** para heridas; el otro con **Vigilar** y cadena **Furia** / **Odio (Troll)**.
- **Blitzers:** doble **Stack** **Vigilar** + **Mantenerse firme** con **Placaje heroico** / **Placaje defensivo** para anclaje y bajar esquivas.
- **Runners:** **Líder** y **Forcejeo** con **Manos seguras** / **Esprintar**; cinco **Líneas** base a TV.

## Progresión sugerida

Tras #euro26, seguir tablas **DG / GP / GF / D** de `enanos.md` por posición.
