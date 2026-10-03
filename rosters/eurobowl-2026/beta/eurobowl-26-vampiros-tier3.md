# Vampiros — EuroBowl 2026 (Tier 3, Team Budget 1080k)


> **#euro26** — [EuroBowl 2026](../../../source/tiers/eurobowl-2026.md). **BB 3ª temporada / BB2025.** Lista alineada con captura del builder (vídeo [EuroBowl / listas — YouTube](https://www.youtube.com/watch?v=wrmKRBFNqcM)). Referencia de equipo: [`source/teams/vampiros.md`](../../../source/teams/vampiros.md) (tabla rellenada desde esta captura hasta publicar Nuffle oficial).

> **Estado:** plantilla **desde captura**. **13 jugadores**. No regenerar con `_build_rosters.py` (ver `SKIP_EMIT`). Tag: `eurobowl-2026-wip-competitive`.

> **Aviso presupuesto:** la captura muestra **1100k gastados / 1080k** de presupuesto base del tier (**+20k**). No es legal tal cual en #euro26 sin recortar sideline o plantilla — ver nota al pie del desglose.

## Presupuesto EuroBowl (tier 3)

| Concepto | Valor |
|----------|--------|
| **Tier** | 3 |
| **Team Budget (base)** | 1.080.000 M.O. |
| **Skill Gold (pool)** | 160.000 M.O. |
| **Flowing Funds (máx.)** | 30.000 M.O. |

*En la captura: **Team budget** **1100k** / 1080k; **Skill Gold** 170k / 160k (**160k** pool + **10k** Flowing a Skill Gold = **170k** en avances; **20k** de Flowing no asignados a Skill Gold en esta lectura, o el builder muestra otro reparto); **Flowing Funds** 30k / 30k.*

## Alineación

*En **negrita**, avances de Skill Gold. **Thrall Lineman** EN = **Siervo Línea**.*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|-----|-------------|
| 1 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |
| 2 | ____ | Vampiro Blitzer | 110k | 6 | 4 | 2+ | 4+ | 9+ | Ansia de Sangre (3+), Imparable, Mirada hipnótica, Regeneración, **Furia** |
| 3 | ____ | Vampiro Blitzer | 110k | 6 | 4 | 2+ | 4+ | 9+ | Ansia de Sangre (3+), Imparable, Mirada hipnótica, Regeneración, **Robar balón** |
| 4 | ____ | Vampiro Lanzador | 110k | 6 | 4 | 2+ | 2+ | 9+ | Ansia de Sangre (2+), Mirada hipnótica, Pasar, Regeneración, **Líder** |
| 5 | ____ | Vampiro Lanzador | 110k | 6 | 4 | 2+ | 2+ | 9+ | Ansia de Sangre (2+), Mirada hipnótica, Pasar, Regeneración, **Placar** |
| 6 | ____ | Vampiro Runner | 100k | 8 | 3 | 2+ | 3+ | 8+ | Ansia de Sangre (2+), Mirada hipnótica, Regeneración, **Esquivar** |
| 7 | ____ | Vampiro Runner | 100k | 8 | 3 | 2+ | 3+ | 8+ | Ansia de Sangre (2+), Mirada hipnótica, Regeneración, **Esquivar** |
| 8 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | **Forcejeo** |
| 9 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |
| 10 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |
| 11 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |
| 12 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |
| 13 | ____ | Siervo Línea | 40k | 6 | 3 | 3+ | 4+ | 8+ | — |

**Total jugadores:** 13 | **Suma jugadores:** 920.000 M.O.

**Desglose presupuesto de equipo (captura; cuadra a 1100k):**

| Concepto | Coste |
|----------|--------|
| Jugadores (920k) | 920.000 |
| Rerolls de equipo (3 × **60.000**) | 180.000 |
| Apotecario | 0 |
| Asistentes / cheerleaders / Hinchas | 0 |
| **Total gastado (captura)** | **1.100.000** |
| **Team Budget base (tier 3)** | 1.080.000 |
| **Diferencia vs tier (captura)** | **+20.000** |

*Para cuadrar en **1080k** sin tocar plantilla de 920k: bajar a **2 rerolls** (ahorra **60k**) y usar **20k** de Flowing al presupuesto de equipo, o sustituir un siervo por opción más barata si el pack lo permite. Ajusta según PDF #euro26.*

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Esquivar](../../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Forcejear](../../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Imparable](../../../source/habilidades/fuerza.md)** (*Juggernaut* · Fuerza · Activa): En **Penetración**: cada **Ambos derribados** en sus Placajes cuenta como **Empujón**. Rivales **no** pueden **Forcejear**, **Mantenerse firme** ni **Zafarse** frente a sus Placajes en esa Penetración.
- **[Líder](../../../source/habilidades/pase.md)** (*Leader* · Pase · Pasiva): Con **≥1** con Líder **en campo** al inicio de cualquier mitad: gana **Segunda oportunidad de Líder** (como reroll normal salvo que **Chef Maestro Halfling** no la quite). Si **todos** los Líder salen **antes** de usarla, se **pierde**.
- **[Mirada hipnótica](../../../source/habilidades/rasgos.md)** (*Hypnotic Gaze* · Rasgo · Activa): **Mirada** (varios/turno): puede **Movimiento** antes, luego rival **en pie** adyacente **1D6** **1–2** nada (fin); **3+** rival **Distraído** (fin).
- **[Pasar](../../../source/habilidades/pase.md)** (*Pass* · Pase · Activa): Puede **repetir** cualquier chequeo de **Pase** fallido en acción de **Pase**.
- **[Placar](../../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Regeneración](../../../source/habilidades/rasgos.md)** (*Regeneration* · Rasgo · Pasiva): Al sufrir **Lesión**, antes de tabla de lesiones: **1D6** **1–3** normal; **4+** **regenera** (ignora lesión; SPP al causante igual); va a **reservas**.
- **[Robar balón](../../../source/habilidades/general.md)** (*Strip Ball* · General · Activa): Placaje al **portador** y **empuje**: el balón **cae y rebota** desde la casilla de destino **antes** de que el rival quede tumbado, pero **después** de que **este jugador** elija si hace **impulso**.
- **[Sed de sangre](../../../source/habilidades/rasgos.md)** (*Bloodlust* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+1** si Placaje/Penetración). Si **≥** número entre paréntesis → normal. Si **menor** o **1 natural**: activa normal pero puede cambiar a **Movimiento**; acciones «1/turno» (p. ej. Penetración) siguen contando. Al **final** de activación puede **morder** a un **Thrall de línea** (Thrall Lineman) **compañero** adyacente (cualquier estado); Heridas (Lesión = **Magullado**; cambio de turno solo si el Thrall llevaba el balón); si **no** muerde → **cambio de turno**, **Distraído**, suelta balón y, si estaba en la zona de anotación rival, **no** anota. Para **Pase**, **Entregar** o **TD** tras fallar la tirada debe morder **antes**.

<!-- habilidades-roster:fin -->


## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF / EuroBowl** | 3 |
| **Team Budget (captura)** | **1100k** / 1080k (**sobrepasa**) |
| **Skill Gold (captura)** | 170k / 160k (+10k Flowing a Skill Gold en esta lectura) |
| **Flowing Funds (captura)** | 30k / 30k |
| **Rerolls** | 3 (× **60k** en el desglose que cuadra la captura) |
| **Apotecario** | No |
| **Inducements** | Ninguno |
| **Opción listas** | Sin estrellas |
| **Ligas / reglas (captura EN)** | Sylvanian Spotlight; Masters of Undeath |
| **Equivalencia repo (ES)** | **Selectiva de Sylvania**; **Señores de los No Muertos** |

## Skill Gold — avances (según captura)

**Siete** jugadores con **un** bloque de avance cada uno. Desglose que suma **170.000 M.O.**:

| Nº | Jugador | Habilidad (EN → ES) | Tipo (referencia #euro26) | Coste Skill Gold |
|----|---------|---------------------|---------------------------|------------------|
| 2 Vampiro Blitzer | Frenzy → **Furia** | Sec. Fuerza no élite | 40.000 |
| 3 Vampiro Blitzer | Strip Ball → **Robar balón** | Prim. General no élite | 20.000 |
| 4 Vampiro Lanzador | Leader → **Líder** | Prim. General **élite** | 30.000 |
| 5 Vampiro Lanzador | Block → **Placar** | Prim. General no élite | 20.000 |
| 6 Vampiro Runner | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 7 Vampiro Runner | Dodge → **Esquivar** | Prim. Agilidad no élite | 20.000 |
| 8 Siervo Línea | Wrestle → **Forcejeo** | Prim. General no élite | 20.000 |
| **Total Skill Gold** | | | **170.000** |

**Límites #euro26:** **1** secundario (**Furia**); **1** primaria **élite** (**Líder**); **0** Stack.

*Si **Furia** cuenta como primaria de Fuerza (20k), el total baja **20k**; reclasifica para mantener **170k** y los techos del pack.*

## Estrellas (Tiers 1–4)

Sin Veterans ni Legends en la captura. Listas: [`eurobowl-2026.md`](../../../source/tiers/eurobowl-2026.md).

## Inducements

Solo los permitidos en `eurobowl-2026.md`. Captura: ninguno.

## Estrategia (breve)

- **Blitzers** con **Imparable** y **Ansia de Sangre**; uno con **Furia** y otro con **Robar balón** para balón.
- **Lanzadores:** **Líder** y **Placar** con pase y mirada; **Runners** con **Esquivar** y MV 8.
- **Siervos** para alimentar ansia; uno con **Forcejeo**; sin apo (**Señores de los No Muertos**).

## Progresión sugerida

Completar categorías de avance por posición cuando `vampiros.md` incorpore la tabla oficial Nuffle / PDF GW Season 3.
