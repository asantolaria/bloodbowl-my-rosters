# Guía de referencia rápida (BB2025)

Hoja de consulta en mesa: la **Cheat Sheet oficial** de Blood Bowl 3ª temporada (BB2025) traducida al español, con la terminología del repo.

Fuente: [bloodbowlbase — Cheat Sheet (BB2025)](https://bloodbowlbase.ru/bb2025/core_rules/cheat_sheet/). Las referencias de página («pág.») son las del reglamento oficial.

## Índice

- [Secuencia de juego](#secuencia-de-juego)
- [Tabla de clima](#tabla-de-clima)
- [Cambio de turno (Turnover)](#cambio-de-turno-turnover)
- [Secuencia postpartido](#secuencia-postpartido)
- [Tabla de eventos de patada inicial](#tabla-de-eventos-de-patada-inicial)
- [Activaciones de jugadores](#activaciones-de-jugadores)
- [Acción de Pase](#acción-de-pase)
- [Acción de Placaje](#acción-de-placaje)
- [Dados de placaje](#dados-de-placaje)
- [Riesgo de herida](#riesgo-de-herida)
- [Herido por el público](#herido-por-el-público)
- [Retrasar el juego (Stalling)](#retrasar-el-juego-stalling)
- [Falta](#falta)
- [Ganar Puntos de Estrella (PE)](#ganar-puntos-de-estrella-pe)
- [Mapa de bloodbowlbase en el repo](#mapa-de-bloodbowlbase-en-el-repo)

---

## Secuencia de juego

### Secuencia prepartido

1. **Los Hinchas** — pág. 45
2. **El Clima** — pág. 46
3. **Contratar sustitutos** — pág. 94
4. **Incentivos** — pág. 94
5. **Elegir equipo pateador** — pág. 46

### Secuencia de inicio de entrada

Al inicio de **cada entrada**:

1. **Despliegue** — pág. 47
2. **Patada inicial** — pág. 47
3. **Evento de patada inicial** — pág. 48

### Turnos de equipo

- Los entrenadores **alternan** turnos.
- En cada entrada, el equipo que **recibe** el balón juega el **primer turno**.

### Secuencia de final de entrada

Cuando se anota un **touchdown** o se juega el **último turno de una parte**, la entrada acaba. Si quedan turnos, seguir esta secuencia y empezar una nueva entrada:

1. **Armas Secretas** — pág. 83
2. **Efectos de final de entrada** — pág. 83
3. **Recuperar Inconscientes** — pág. 83
4. **Fin de la entrada** — pág. 83

→ Detalle: [tablas/secuencia-de-partido.md](tablas/secuencia-de-partido.md)

---

## Tabla de clima

| 2D6 | Clima | Efecto |
|-----|-------|--------|
| 2 | **Calor asfixiante** | Al final de cada entrada, un entrenador tira **1D3**. Cada entrenador elige **al azar** esa cantidad de jugadores suyos que estaban en el campo al acabar la entrada: van a **Reservas** y **no** pueden desplegarse en la siguiente entrada. |
| 3 | **Muy soleado** | **-1** a todos los chequeos de **Pase** (PS). |
| 4-10 | **Clima perfecto** | Sin efecto adicional. |
| 11 | **Lluvioso** | **-1** al **recoger** el balón, **atrapar** o **interceptar**. |
| 12 | **Ventisca** | **-1** a **Forzar la marcha**. En una acción de Pase solo se puede intentar **Pase Rápido** o **Pase Corto**. |

→ Detalle: [tablas/clima.md](tablas/clima.md)

---

## Cambio de turno (Turnover)

Hay cambio de turno si:

- Un jugador del equipo activo **se cae** durante su propia activación.
- Un jugador del equipo activo es **derribado** durante el turno de su equipo.
- El **portador** del equipo activo queda **tumbado** o es forzado a salir del campo por cualquier motivo.
- Un jugador del equipo activo intenta **recoger** el balón del suelo y falla.
- Un jugador del equipo activo intenta un **Pase** y lo **pifia**.
- Un jugador del equipo activo falla al **atrapar** tras un Pase o una Entrega y el balón queda en el suelo. *Excepción:* si rebota directamente a la casilla de otro jugador del equipo activo que lo atrapa, no hay cambio de turno.
- Tras un Pase, **ningún** jugador del equipo activo atrapa el balón y este toca el suelo (rebota o queda en el suelo).
- Un jugador del equipo **inactivo** acaba con el balón tras un **Pase** o una **Entrega**, o al **interceptarlo**.
- El **portador** del equipo activo es lanzado por un compañero y no aterriza bien, cae al **público** o es **comido**.
- Un jugador del equipo activo es **expulsado** por una **Falta**.
- Se anota un **touchdown**.

→ Detalle: [tablas/secuencia-de-partido.md](tablas/secuencia-de-partido.md#cambio-de-turno-turnover)

---

## Secuencia postpartido

Solo en **liga**, al acabar el partido:

1. **Registrar resultado y cobrar ganancias** — pág. 95
2. **Actualizar Hinchas** — pág. 95
3. **Mejoras de jugadores** — pág. 96
4. **Contratar, despedir y retirar temporalmente** — pág. 99
5. **Errores costosos** — pág. 100
6. **Preparar el siguiente partido** — pág. 100

→ Detalle: [tablas/liga-postpartido.md](tablas/liga-postpartido.md)

---

## Tabla de eventos de patada inicial

| 2D6 | Evento | Efecto |
|-----|--------|--------|
| 2 | **Árbitro intimidado** | Cada equipo recibe un **Soborno** gratuito. Debe usarse antes del final del partido o se pierde. |
| 3 | **¡Tiempo muerto!** | Si el marcador de turno del equipo **pateador** está en el turno **6, 7 u 8** de la parte → ambos marcadores **retroceden** una casilla. Si no → ambos **avanzan** una casilla. |
| 4 | **Defensa sólida** | El pateador elige hasta **D3+3** jugadores **desmarcados** suyos; se retiran y se vuelven a desplegar con las restricciones normales. |
| 5 | **Patada alta** | Un jugador **desmarcado** del receptor puede colocarse inmediatamente en la casilla donde va a caer el balón. |
| 6 | **Los hinchas animan** | Cada entrenador tira **1D6 + nº de Animadoras**. El **primer Placaje** del siguiente turno del que saque más recibe **un apoyo ofensivo adicional**. Empate → ambos lo reciben en su siguiente turno. |
| 7 | **Entrenador brillante** | Cada entrenador tira **1D6 + nº de Ayudantes del entrenador**. El mayor (o ambos si empatan) gana **un Reroll de equipo** gratis para la entrada; si no se usa, se pierde al final de la entrada. |
| 8 | **Clima cambiante** | Nueva tirada en la [Tabla de clima](#tabla-de-clima). Si sale **Clima perfecto**, el balón se **dispersa** (Scatter 3) en el aire antes de caer. |
| 9 | **Anticipación** | El receptor elige hasta **D3+3** jugadores **desmarcados** suyos; cada uno puede moverse **1 casilla** en cualquier dirección, incluso a la mitad rival. |
| 10 | **¡A la carga!** | El pateador elige hasta **D3+3** jugadores **desmarcados**; se activan uno a uno como en su turno y hacen un **Movimiento** gratis. **Uno** puede hacer en su lugar una **Penetración**, **uno** un **Lanzar compañero** y **uno** un **Chutar compañero**. Si uno **se cae** o es **derribado**, no se activan más y la Carga termina. |
| 11 | **Indigestión** | Cada entrenador tira 1D6. El que saque **menos** (o ambos si empatan) elige al azar un jugador suyo en el campo y tira 1D6: **2+** → **-1 MV y -1 AR** durante la entrada; **1** → va a **Reservas** (pasa la entrada encerrado en el baño). |
| 12 | **Invasión de campo** | Cada entrenador tira **1D6 + Factor de Hinchas**. El que saque **menos** (o ambos si empatan) elige al azar **D3** jugadores suyos en el campo: quedan **tumbados** y **Aturdidos**. |

→ Detalle: [tablas/patada-inicial.md](tablas/patada-inicial.md)

---

## Activaciones de jugadores

- En tu turno puedes activar a cada jugador **de pie** y/o **tumbado** para hacer **una** acción disponible.
- Los que empezaron el turno **Aturdidos** no pueden activarse.

| Acción | Notas | Pág. |
|--------|-------|------|
| **Movimiento** | Hasta su MV; puede **Forzar la marcha**. | 54 |
| **Placaje** | Placar a un jugador adyacente. | 60 |
| **Penetración** (Blitz) | Mover y luego Placar. | 64 |
| **Pase** | Mover y luego pasar el balón. | 70 |
| **Entrega** (Hand-off) | Pasar a un jugador adyacente; solo se tira para **atrapar**. | 74 |
| **Falta** | Mover y luego hacer Falta a un rival **tumbado** adyacente. | 69 |
| **Lanzar compañero** | «Pasar» a un jugador con el rasgo **Humanoide bala**. | 76 |
| **Acciones especiales** | Acción de habilidad o rasgo. | 123 |
| **Asegurar el balón** | Mover y luego recoger el balón con seguridad. | 59 |

→ Detalle: [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#acciones)

---

## Acción de Pase

**Una vez por turno de equipo**, un jugador con el balón puede hacer una acción de Pase:

1. **Declarar casilla objetivo.**
2. **Medir distancia** — con la regla de pase o la tabla de distancias de pase, mide hasta la casilla objetivo y determina el tipo de pase.
3. **Chequeo de precisión** — chequeo de **PS** del lanzador, aplicando modificadores.
4. **Intercepción** — un jugador rival puede intentar interceptar el balón.
5. **Resolver el Pase** — ver si el objetivo atrapa el balón o dónde acaba.

*Complemento (The Game of Blood Bowl, no está en la Cheat Sheet):*

| Tipo de pase (regla) | Mod. al chequeo de PS |
|----------------------|-----------------------|
| I — **Pase Rápido** | 0 |
| II — **Pase Corto** | -1 |
| III — **Pase Largo** | -2 |
| IIII — **Bomba Larga** | -3 |
| Por cada rival que **marque al lanzador** | -1 |

→ Detalle: [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#pase)

---

## Acción de Placaje

Se tiran **dados de placaje** y se elige **un** resultado. El número de dados se obtiene comparando la **FU modificada** del atacante y del objetivo:

| Comparación de FU modificada | Dados |
|------------------------------|-------|
| Iguales | 1 |
| Uno tiene **más** FU | 2* |
| Uno tiene **más del doble** de FU | 3* |

\* Elige el resultado el entrenador del jugador con **más FU**.

### Apoyos en un Placaje

La forma habitual de modificar la FU en un Placaje son los **apoyos**:

- **Atacante:** **+1 FU** por cada compañero que **marque al objetivo** y **no esté marcado** por otro rival.
- **Objetivo:** **+1 FU** por cada compañero que **marque al atacante** y **no esté marcado** por otro rival.

→ Detalle: [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#placaje)

---

## Dados de placaje

| Resultado | Efecto |
|-----------|--------|
| **Atacante derribado** (Player Down) | El atacante es **derribado** inmediatamente por el objetivo, como si el objetivo hubiera hecho el Placaje. |
| **Ambos derribados** (Both Down) | Atacante y objetivo se **derriban** mutuamente en sus casillas, como si ambos hubieran hecho un Placaje. |
| **Empujón** (Push Back) | El objetivo es **empujado** por el atacante. El atacante puede hacer **impulso** (follow-up) a la casilla que deja libre. |
| **Desequilibrado** (Stumble) | Si el objetivo tiene **Esquivar** → **Empujón**. Si no → **¡Pow!**. |
| **¡Pow!** | Se aplica el **Empujón** y luego el objetivo es **derribado** por el atacante en la casilla en la que queda. |

→ Detalle: [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#placaje) · Habilidades: [habilidades/README.md](habilidades/README.md)

---

## Riesgo de herida

Cuando un jugador es **derribado** o **se cae**, queda **tumbado** y arriesga una herida: el entrenador **rival** hace una **tirada de Armadura** contra él (pág. 37).

### Tirada de Heridas

Si la armadura se **rompe**, el entrenador rival tira **2D6** en la tabla de Heridas.

### Tabla de Heridas

| 2D6 | Resultado | Efecto |
|-----|-----------|--------|
| 2-7 | **Aturdido** | El jugador queda **Aturdido** inmediatamente. |
| 8-9 | **Inconsciente** | Se retira del campo a la casilla de **Inconscientes** de su banquillo. |
| 10-12 | **Lesión** (Casualty) | Se retira a la casilla de **Lesionados** de su banquillo. El rival hace una tirada en la **Tabla de Lesiones** (pág. 67). |

### Tabla de Lesiones

| D16 | Resultado | Efecto |
|-----|-----------|--------|
| 1-8 | **Magullado** | Sin secuelas a largo plazo. |
| 9-10 | **Apaleado** | Se pierde el **próximo partido**. |
| 11-12 | **Herida grave** | Sufre una **Lesión mal curada** y se pierde el próximo partido. |
| 13-14 | **Herida permanente** | Sufre una **reducción de atributo** y se pierde el próximo partido. |
| 15-16 | **Muerto** | El jugador muere. |

### Tabla de Heridas permanentes

| D6 | Herida permanente | Reducción |
|----|-------------------|-----------|
| 1-2 | Cabeza fracturada | -1 AR |
| 3 | Rodilla aplastada | -1 MV |
| 4 | Brazo roto | -1 PS |
| 5 | Cadera dislocada | -1 AG |
| 6 | Rotura de hombro | -1 FU |

→ Detalle: [tablas/heridas-y-lesiones.md](tablas/heridas-y-lesiones.md) (incluye la tabla de **Escurridizos**, Apotecario y mínimos de características)

---

## Herido por el público

- Jugador **empujado al público** (pág. 68): se hace directamente una **Tirada de Heridas**.
- Si saldría **Aturdido** → va a **Reservas**.
- Si no → se aplica el resultado de la tabla de Heridas correspondiente.

→ Detalle: [tablas/heridas-y-lesiones.md](tablas/heridas-y-lesiones.md#reglas-relacionadas)

---

## Retrasar el juego (Stalling)

- Un **portador** que al activarse **puede anotar sin tirar dados**, pero termina su activación **sin anotar**, está haciendo **Stalling**.
- Tirar **1D6**: si el resultado es **≥ número de turno actual** del equipo, el jugador es **derribado** y hay **cambio de turno**.

→ Detalle: [tablas/secuencia-de-partido.md](tablas/secuencia-de-partido.md#retrasar-el-juego-stalling)

---

## Falta

- Tirada de **Armadura** contra el objetivo de la Falta.
- **+1** por cada **apoyo ofensivo**; **-1** por cada **apoyo defensivo**.

→ Detalle (expulsión con dobles, Protestar al árbitro, Sobornos): [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#falta)

---

## Ganar Puntos de Estrella (PE)

En **liga**, los jugadores ganan PE (SPP) por (detalle en pág. 96):

| Acción | PE |
|--------|----|
| **Pase completo** | 1 |
| **Lanzar compañero** | Ver pág. 76 |
| **Intercepción** | 2 |
| **Causar una Lesión** | 2 |
| **Touchdown** | 3 |
| **Jugador Más Valioso (MVP)** | 4 |

→ Detalle (Lanzar compañero, Brutos brutales, coste de mejoras): [tablas/experiencia-y-spp.md](tablas/experiencia-y-spp.md)

---

## Lo que no se reproduce aquí

- **Regla de pase** y **tabla de distancias de pase** (Passing Range Chart): son imágenes en el reglamento; usa la regla física. Tipos y modificadores en [Acción de Pase](#acción-de-pase).
- **Plantillas** (dispersión, saque de banda): ver [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md#saque-de-banda) y [tablas/secuencia-de-partido.md](tablas/secuencia-de-partido.md#reglas-generales-útiles).

---

## Mapa de bloodbowlbase en el repo

| Sección de bloodbowlbase (BB2025) | Archivo del repo |
|-----------------------------------|------------------|
| [Core Rules](https://bloodbowlbase.ru/bb2025/core_rules/) | [referencias-reglamento-bb3.md](referencias-reglamento-bb3.md) · [reglamento/README.md](reglamento/README.md) · [tablas/README.md](tablas/README.md) |
| [Game Essentials](https://bloodbowlbase.ru/bb2025/core_rules/game_essentials/) | [tablas/fundamentos-y-principios.md](tablas/fundamentos-y-principios.md) |
| [Rules and Regulations](https://bloodbowlbase.ru/bb2025/core_rules/rules_and_regulations/) | [tablas/fundamentos-y-principios.md](tablas/fundamentos-y-principios.md) · [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md) |
| [The Game of Blood Bowl](https://bloodbowlbase.ru/bb2025/core_rules/the_game_of_blood_bowl/) | [tablas/secuencia-de-partido.md](tablas/secuencia-de-partido.md) · [tablas/clima.md](tablas/clima.md) · [tablas/patada-inicial.md](tablas/patada-inicial.md) · [tablas/acciones-y-modificadores.md](tablas/acciones-y-modificadores.md) · [tablas/heridas-y-lesiones.md](tablas/heridas-y-lesiones.md) |
| [Drafting a Blood Bowl Team](https://bloodbowlbase.ru/bb2025/core_rules/drafting_a_blood_bowl_team/) | [tablas/creacion-de-equipo.md](tablas/creacion-de-equipo.md) |
| [Exhibition Play](https://bloodbowlbase.ru/bb2025/core_rules/exhibition_play/) | [tablas/juego-igualado.md](tablas/juego-igualado.md) |
| [Matched Play](https://bloodbowlbase.ru/bb2025/core_rules/matched_play/) | [tablas/juego-igualado.md](tablas/juego-igualado.md) |
| [League Play](https://bloodbowlbase.ru/bb2025/core_rules/league_play/) | [tablas/liga-postpartido.md](tablas/liga-postpartido.md) · [tablas/experiencia-y-spp.md](tablas/experiencia-y-spp.md) |
| [Inducements](https://bloodbowlbase.ru/bb2025/core_rules/inducements/) | [tablas/incentivos.md](tablas/incentivos.md) · [tablas/plegarias-nuffle.md](tablas/plegarias-nuffle.md) |
| [Skills and Traits](https://bloodbowlbase.ru/bb2025/core_rules/skills_and_traits/) | [habilidades/README.md](habilidades/README.md) |
| [The Teams](https://bloodbowlbase.ru/bb2025/core_rules/the_teams/) | [tablas/creacion-de-equipo.md](tablas/creacion-de-equipo.md) (ligas y reglas especiales) · [teams/README.md](teams/README.md) |
| [Latest FAQ](https://bloodbowlbase.ru/bb2025/core_rules/latest_faq/) | [tablas/faq-errata.md](tablas/faq-errata.md) |
| [Cheat Sheet](https://bloodbowlbase.ru/bb2025/core_rules/cheat_sheet/) | Esta guía |
| [Teams](https://bloodbowlbase.ru/bb2025/teams/) | [teams/README.md](teams/README.md) (un archivo por equipo) |
| [Star Players](https://bloodbowlbase.ru/bb2025/starplayers/) | [jugadores-estrella/README.md](jugadores-estrella/README.md) (un archivo por jugador) |
| [Spike! Journal 19](https://bloodbowlbase.ru/bb2025/spike_journal/issue_19/) · [20](https://bloodbowlbase.ru/bb2025/spike_journal/issue_20/) · [21](https://bloodbowlbase.ru/bb2025/spike_journal/issue_21/) | [tablas/copas-tematicas-spike.md](tablas/copas-tematicas-spike.md) |
| [Spike! Journal 22](https://bloodbowlbase.ru/bb2025/spike_journal/issue_22/) | [tablas/sevens.md](tablas/sevens.md) |
