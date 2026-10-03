# Skavens — Inicio 1000k (1.000k)

![Skavens](../../source/images/equipos/skavens.webp)

> **BB 3ª temporada / BB2025.** Roster de inicio a **1.000k** según [`source/teams/skavens.md`](../../source/teams/skavens.md). Reglamento: `reglamento-bb3-season3.pdf` *(copia local, no publicada)*. Build estándar con **Rata Ogro** y núcleo de posicionales a tope permitido.

## Alineación

*Roster inicial sin habilidades de progresión. **Dorsales:** Thrower **1** y **2** (solo un Thrower en esta lista: **1**; **2** libre para el segundo), Gutter Runner **3** y **4**, Blitzer **5** y **6**, Linemen **7–11** (cinco en este inicio; **12** libre para un sexto), Rata Ogro **20**. Stats: [`source/teams/skavens.md`](../../source/teams/skavens.md).*

| Nº | Nombre | Posición    | Coste | MV | FU | AG | PS | AR | Habilidades |
|----|--------|-------------|-------|----|----|----|----|----|-------------|
| 1 | ____ | Thrower | 80k | 7 | 3 | 3+ | 2+ | 8+ | Manos seguras, Pasar |
| 3 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 4 | ____ | Gutter Runner | 85k | 9 | 2 | 2+ | 4+ | 8+ | Apuñalar, Esquivar |
| 5 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón |
| 6 | ____ | Blitzer | 90k | 8 | 3 | 3+ | 4+ | 9+ | Placar, Robar balón |
| 7 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | — |
| 8 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | — |
| 9 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | — |
| 10 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | — |
| 11 | ____ | Linemen | 50k | 7 | 3 | 3+ | 4+ | 8+ | — |
| 20 | ____ | Rata Ogro | 150k | 6 | 5 | 4+ | — | 9+ | Ferocidad animal, Cola prensil, Furia, Golpe mortífero (+1), Solitario (4+) |

**Total jugadores:** 11 | **TV:** 1.000k

**Desglose TV (todo lo que tiene precio):** Referencia de precios: Reroll 50.000 | Apotecario 50.000 | Hinchas 10.000 c/u.

| Concepto | Coste |
|----------|--------|
| Jugadores (1 Rata Ogro 150k, 1 Thrower 80k, 2 Blitzers 180k, 2 Gutter Runners 170k, 5 Linemen 250k) | 830.000 |
| Rerolls (3 × 50.000) | 150.000 |
| Hinchas (2 × 10.000) | 20.000 |
| **Total TV** | **1.000.000** |

<!-- habilidades-roster:inicio -->
## Habilidades del roster

*Definición de todas las habilidades y rasgos de los jugadores de esta lista (de serie y compradas). Generado con `scripts/habilidades_en_rosters.py`.*

- **[Apuñalar](../../source/habilidades/rasgos.md)** (*Stab* · Rasgo · Activa): Acción **Apuñalar** (sin límite por turno): rival **en pie** adyacente, **Armadura** sin mods.; si rompe → **Heridas**. Puede **sustituir** Placaje en **Penetración** (activación termina igualmente).
- **[Cola prensil](../../source/habilidades/mutaciones.md)** (*Prehensile Tail* · Mutaciones · Activa): **-1** adicional al AG de rivales que **esquivan, saltan o brincan** desde su zona de defensa. **Solo uno** por intento de salida.
- **[Esquivar](../../source/habilidades/agilidad.md)** (*Dodge* · Agilidad · Activa (Elite)): **Una vez por turno** puede repetir un **único** chequeo de AG al **intentar esquivar**. Afecta al resultado **Desequilibrado** cuando un rival le hace un Placaje.
- **[Ferocidad animal](../../source/habilidades/rasgos.md)** (*Animal Savagery* · Rasgo · Pasiva (obligatoria)): Tras declarar: **1D6** (**+2** si Placaje/Penetración). **4+** OK; **1–3** ataca **compañero adyacente en pie** (derribo); sin cambio de turno salvo que llevara el balón; con **Garras**/**Golpe mortífero** debe usarlos vs compañero; después puede seguir su activación (FAQ). **1–3** sin compañero adyacente → **Distraído**.
- **[Furia](../../source/habilidades/general.md)** (*Frenzy* · General · Activa (obligatoria)): Tras **empujar** en Placaje debe **impulso** si puede; si el blanco sigue **en pie**, **segundo Placaje** al mismo (e impulso otra vez). En **Penetración**, el segundo cuesta **movimiento**; si no puede forzar marcha, **no** hay segundo placaje. **No** **Apartar**, **Golpe a la carrera** ni **Placaje múltiple**.
- **[Golpe mortífero](../../source/habilidades/fuerza.md)** (*Mighty Blow* · Fuerza · Activa (Elite)): Si **derriba** a un rival en **Placaje** (aunque él también quede derribado), **+1** a **Armadura** **o** a **Heridas** (eliges **después** de tirar ese dado).
- **[Manos seguras](../../source/habilidades/general.md)** (*Sure Hands* · General · Activa): Puede **repetir** el **D6** al **recoger** el balón (**no** en **Asegurar el balón**). **Robar balón** **no** puede usarse contra él.
- **[Pasar](../../source/habilidades/pase.md)** (*Pass* · Pase · Activa): Puede **repetir** cualquier chequeo de **Pase** fallido en acción de **Pase**.
- **[Placar](../../source/habilidades/general.md)** (*Block* · General · Activa (Elite)): En Placaje con **Ambos derribados** puede elegir **no** ser **derribado**.
- **[Robar balón](../../source/habilidades/general.md)** (*Strip Ball* · General · Activa): Placaje al **portador** y **empuje**: el balón **cae y rebota** desde la casilla de destino **antes** de que el rival quede tumbado, pero **después** de que **este jugador** elija si hace **impulso**.
- **[Solitario](../../source/habilidades/rasgos.md)** (*Loner* · Rasgo · Pasiva (obligatoria)): Para usar **Segunda oportunidad**: **1D6** vs número entre paréntesis; si falla **no** repite pero **gasta** el reroll.

<!-- habilidades-roster:fin -->


## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF** | Tier 2 |
| **Valoración del equipo (TV)** | 1.000k |
| **Total plantilla** | 11 jugadores |
| **Tesorería actual** | 0 |
| **Rerolls** | 3 |
| **Asistentes de entrenador** | 0 |
| **Animadoras** | 0 |
| **Hinchas** | 2 |
| **Apotecario** | No (incluible como inducement) |


## Inducements

- Apotecario según reglamento. Rerolls y Fans según torneo.

## Estrategia

- **Ataque:** Thrower (Manos seguras, Pasar) para llevar y pasar el balón; Gutter Runners (MV9, Esquivar, Apuñalar) para recepción y anotar; Blitzers (MV8, Placar, Robar balón) para blitz y presión al portador; Rata Ogro y Linemen para pantalla. Velocidad y juego de pase.
- **Defensa:** Blitzers para Robar balón; Rata Ogro (Cola prensil, Furia) para marcar y frenar; Gutter Runners para perseguir. Cuidado con Ferocidad animal y Solitario en la Rata Ogro.

## Progresión recomendada

- **Blitzer:** Primaria Golpe mortífero o Defensa; secundarias Forcejear, Abrirse paso (GF / ADM según source/teams/skavens.md).
- **Gutter Runner:** Primaria Echarse a un lado; secundarias Manos seguras, Esquivar (ADG / MF).
- **Thrower:** Primaria Echarse a un lado o Líder; secundarias Manos seguras, Esquivar (GP / ADMF).
- **Linemen:** Primaria Placar; secundarias Echarse a un lado, Manos seguras (DG / AMF).
- **Rata Ogro:** Primaria Defensa; secundarias Mantenerse firme, Abrirse paso (F / AGM).
