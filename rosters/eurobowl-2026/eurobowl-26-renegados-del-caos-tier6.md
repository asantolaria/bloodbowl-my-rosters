# Renegados del Caos — EuroBowl 2026 FINAL (Tier 6)

> **#euro26 · reglamento [FINAL](../../source/tiers/eurobowl-2026-final.md).** Posiciones y costes: [`source/teams/renegados-del-caos.md`](../../source/teams/renegados-del-caos.md). Generado con `_build_final.py`.
>
> **Origen de la build:** [AndyDavo — Eurobowl Ruleset Review 2026](https://www.youtube.com/watch?v=wrmKRBFNqcM) (abr. 2026, BETA), adaptada al presupuesto FINAL.
>
> **Estado competitivo:** válida en cifras; revisión táctica propia pendiente.

## Presupuesto

| Concepto | Disponible | Usado |
|----------|-----------|-------|
| **Presupuesto de equipo** | 1.140.000 M.O. | 1.135.000 M.O. |
| **Skill Gold** | 240.000 M.O. | 270.000 M.O. |
| **Flowing Funds** | 40.000 M.O. | 0 → equipo · 30.000 → Skill Gold |

## Alineación

*Rellenar nombres. Habilidades compradas con Skill Gold en **negrita**.*

| Nº | Nombre | Posición | Coste | MV | FU | AG | PS | AR | Habilidades | Skill Gold |
|----|--------|----------|-------|----|----|----|----|----|-------------|------------|
| 1 | ____ | Ogro Renegado | 140k | 5 | 5 | 4+ | 5+ | 10+ | Estúpido, Solitario (3+), Golpe mortífero, Cabeza dura, Lanzar compañero, **Defensa** | Primaria élite 30k |
| 2 | ____ | Rata Ogro Renegada | 150k | 6 | 5 | 4+ | 6+ | 9+ | Ferocidad animal, Furia, Solitario (4+), Golpe mortífero, Cola prensil, **Placar** | Secundaria élite 50k |
| 3 | ____ | Troll Renegado | 115k | 4 | 5 | 5+ | 5+ | 10+ | Siempre hambriento, Solitario (4+), Golpe mortífero, Proyectil de vómito, Realmente estúpido, Regeneración, Lanzar compañero, **Defensa** | Primaria élite 30k |
| 4 | ____ | Elfo Oscuro Renegado | 65k | 6 | 3 | 2+ | 3+ | 9+ | Animosidad (todos), **Placar**, **Esquivar** | Stack 70k |
| 5 | ____ | Lanzador Humano Renegado | 75k | 6 | 3 | 3+ | 3+ | 9+ | Animosidad (todos), Pasar, Manos seguras, **Líder** | Primaria 20k |
| 6 | ____ | Orco Renegado | 50k | 5 | 3 | 3+ | 4+ | 10+ | Animosidad (todos) | – |
| 7 | ____ | Skaven Renegado | 50k | 7 | 3 | 3+ | 4+ | 8+ | Animosidad (todos), **Placar** | Primaria élite 30k |
| 8 | ____ | Línea Humano Renegado | 50k | 6 | 3 | 3+ | 4+ | 9+ | Animosidad (todos), **Forcejear** | Primaria 20k |
| 9 | ____ | Línea Humano Renegado | 50k | 6 | 3 | 3+ | 4+ | 9+ | Animosidad (todos), **Forcejear** | Primaria 20k |
| 10 | ____ | Línea Humano Renegado | 50k | 6 | 3 | 3+ | 4+ | 9+ | Animosidad (todos) | – |
| 11 | ____ | Línea Humano Renegado | 50k | 6 | 3 | 3+ | 4+ | 9+ | Animosidad (todos) | – |
| 12 | ____ | Línea Humano Renegado | 50k | 6 | 3 | 3+ | 4+ | 9+ | Animosidad (todos) | – |
| 13 | ____ | Goblin Renegado | 40k | 6 | 2 | 3+ | 4+ | 8+ | Animosidad (todos), Esquivar, Humanoide bala, Escurridizo | – |

**Total jugadores:** 13

| Concepto | Coste |
|----------|--------|
| Jugadores | 935.000 |
| Segundas oportunidades (2 × 70.000) | 140.000 |
| Apotecario | 50.000 |
| Ayudantes del entrenador (1 × 10.000) | 10.000 |
| **Total** | **1.135.000** |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Animosidad](../../source/habilidades/rasgos.md)** (*Animosity* · Rasgo · Activa (obligatoria)): Al **Pasar** o **Entregar** a compañero con la **clave** entre paréntesis: **1D6**, **1** = se niega y termina activación. **(todos)** = afecta a **todos** los compañeros.
- **[Cabeza dura](../../source/habilidades/fuerza.md)** (*Thick Skull* · Fuerza · Pasiva): Tirada de **Heridas**: **Inconsciente** solo con **9**; **8** = **Aturdido**. Con **Escurridizo**: Inconsciente con **8**, **7** = Aturdido.
- **[Cola prensil](../../source/habilidades/mutaciones.md)** (*Prehensile Tail* · Mutaciones · Activa): **-1** adicional al AG de rivales que **esquivan, saltan o brincan** desde su zona de defensa. **Solo uno** por intento de salida.
- **[Defensa](../../source/habilidades/fuerza.md)** (*Guard* · Fuerza · Activa (Elite)): Siempre puede **apoyar** (ofensivo y defensivo) en Placajes aunque lo marquen **varios** rivales.
- **[Escurridizo](../../source/habilidades/rasgos.md)** (*Stunty* · Rasgo · Pasiva (obligatoria)): Al **esquivar**, **sin** mods. negativos por marcadores rivales. **-1** al **interceptar**. Heridas en **tabla Escurridizos**.
- **[Esquivar](../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Estúpido](../../source/habilidades/rasgos.md)** (*Bone Head* · Rasgo · Pasiva (obligatoria)): Tras declarar acción: **1D6** **2+** OK; **1** = **Distraído**.
- **[Ferocidad animal](../../source/habilidades/rasgos.md)** (*Animal Savagery* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+2** si Placaje/Penetración). **4+** OK; **1–3** ataca **compañero adyacente en pie** (derribo); sin cambio de turno salvo que llevara el balón; con **Garras**/**Golpe mortífero** debe usarlos vs compañero; después puede seguir su activación (FAQ). **1–3** sin compañero adyacente → **Distraído**.
- **[Forcejear](../../source/habilidades/general.md)** (*Wrestle* · General · Activa): En **Placaje** (activo o como blanco), si aplicaría **Ambos derribados**, puede usarla: **ambos** quedan **tumbados boca arriba**, sin importar otras habilidades.
- **[Furia](../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe mortífero](../../source/habilidades/fuerza.md)** (*Mighty Blow* · Fuerza · Activa (Elite)): Si **derriba** a un rival en **Placaje** (aunque él también quede derribado), **+1** a **Armadura** **o** a **Heridas** (eliges **después** de tirar ese dado).
- **[Humanoide bala](../../source/habilidades/rasgos.md)** (*Right Stuff* · Rasgo · Pasiva (obligatoria)): Puede ser **lanzado** aunque esté **tumbado boca arriba**.
- **[Lanzar compañero](../../source/habilidades/rasgos.md)** (*Throw Team-Mate* · Rasgo · Activa): Puede declarar **Lanzar compañero**.
- **[Líder](../../source/habilidades/pase.md)** (*Leader* · Pase · Pasiva): Con **≥1** con Líder **en campo** al inicio de cualquier mitad: gana **Segunda oportunidad de Líder** (como reroll normal salvo que **Chef Maestro Halfling** no la quite). Si **todos** los Líder salen **antes** de usarla, se **pierde**.
- **[Manos seguras](../../source/habilidades/general.md)** (*Sure Hands* · General · Activa): Puede **repetir** el **D6** al **recoger** el balón (**no** en **Asegurar el balón**). **Robar balón** **no** puede usarse contra él.
- **[Pasar](../../source/habilidades/pase.md)** (*Pass* · Pase · Activa): Puede **repetir** cualquier chequeo de **Pase** fallido en acción de **Pase**.
- **[Placar](../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Proyectil de vómito](../../source/habilidades/rasgos.md)** (*Projectile Vomit* · Rasgo · Activa): **Proyectil de vómito** (varios/turno): rival adyacente **en pie**, **1D6** **2+** Armadura sin mods. (rompe → Heridas); **1** Armadura sin mods. a **ti**. Puede sustituir Placaje en **Penetración** (activación termina).
- **[Realmente estúpido](../../source/habilidades/rasgos.md)** (*Really Stupid* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+2** si adyacente a compañero **en pie**, no Distraído, sin este rasgo). **4+** OK; **1–3** Distraído.
- **[Regeneración](../../source/habilidades/rasgos.md)** (*Regeneration* · Rasgo · Pasiva): Al sufrir **Lesión**, antes de tabla de lesiones: **1D6** **1–3** normal; **4+** **regenera** (ignora lesión; SPP al causante igual); va a **reservas**.
- **[Siempre hambriento](../../source/habilidades/rasgos.md)** (*Always Hungry* · Rasgo · Activa (obligatoria)): En **Lanzar compañero**, **antes** del chequeo de Pase: **1D6** **2+** OK; **1** intenta comérselo → **1D6** **2+** pifia de lanzamiento; **1** **devorado** (se retira de la plantilla; sin apo ni regen); si el compañero llevaba el balón, rebota desde **su** casilla. El texto dice «se produce cambio de turno», pero la FAQ aclara que solo si el devorado llevaba el balón.
- **[Solitario](../../source/habilidades/rasgos.md)** (*Loner* · Rasgo · Pasiva (obligatoria)): Para usar **Segunda oportunidad**: **1D6** vs número entre paréntesis; si falla **no** repite pero **gasta** el reroll.

<!-- habilidades-roster:fin -->




## Skill Gold

Un avance por jugador. Secundarias: **1/3** · Stacks: **1/3**.

| Jugador (Nº) | Avance | Tipo | Coste |
|--------------|--------|------|-------|
| 1 Ogro Renegado | Defensa | Primaria élite | 30.000 |
| 2 Rata Ogro Renegada | Placar | Secundaria élite | 50.000 |
| 3 Troll Renegado | Defensa | Primaria élite | 30.000 |
| 4 Elfo Oscuro Renegado | Placar + Esquivar | Stack | 70.000 |
| 5 Lanzador Humano Renegado | Líder | Primaria | 20.000 |
| 7 Skaven Renegado | Placar | Primaria élite | 30.000 |
| 8 Línea Humano Renegado | Forcejear | Primaria | 20.000 |
| 9 Línea Humano Renegado | Forcejear | Primaria | 20.000 |
| **Total** | | | **270.000** |

## Notas de la build

- Tres grandullones: Defensa en el Ogro y el Troll, y Placar (secundaria) en la Rata Ogro. El Elfo Oscuro lleva el stack Placar + Esquivar.
- Cambio frente a la BETA: en el tier 6 entra completa con 15k de equipo de margen. Se suma Placar al Skaven Renegado (30k de Flowing) y un ayudante del entrenador.
- No hay presupuesto para un tercer reroll a 70k: costaría 55k de Flowing y el máximo es 40k.
