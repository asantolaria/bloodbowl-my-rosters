# Blood Bowl — My Rosters

Repositorio para guardar y consultar **rosters de Blood Bowl** en Markdown, enfocado en **Blood Bowl Third Season (2025)**.

---

## Rosters existentes

Los rosters están en **[`rosters/`](rosters/)**. Índice completo: [rosters/README.md](rosters/README.md).

| Equipo | Nombre del equipo | TV | Archivo |
|--------|-------------------|-----|---------|
| Altos Elfos | Inicio 1000k | 1.000k | [inicio-1000k-altos-elfos-1000k.md](rosters/iniciales/inicio-1000k-altos-elfos-1000k.md) |
| Nobleza Imperial | Barones Bigotudos | 1.070k | [barones-bigotudos-nobleza-imperial-1070k.md](rosters/barones-bigotudos-nobleza-imperial-1070k.md) |
| Nobleza Imperial | Inicio 1000k | 1.000k | [inicio-1000k-nobleza-imperial-1000k.md](rosters/iniciales/inicio-1000k-nobleza-imperial-1000k.md) |
| Nobleza Imperial | Barones Bigotudos | 1.205k | [barones-bigotudos-nobleza-imperial-1205k.md](rosters/barones-bigotudos-nobleza-imperial-1205k.md) |
| Elegidos del Caos | Bollychaos | 1.285k | [bollychaos-elegidos-del-caos-1285k.md](rosters/bollychaos-elegidos-del-caos-1285k.md) |
| Elegidos del Caos | Inicio 1000k | 1.000k | [inicio-1000k-elegidos-del-caos-1000k.md](rosters/iniciales/inicio-1000k-elegidos-del-caos-1000k.md) |
| Orcos Negros | Brutorcos | 1.230k | [brutorcos-orcos-negros-1230k.md](rosters/brutorcos-orcos-negros-1230k.md) |
| Orcos Negros | Inicio 1000k | 1.000k | [inicio-1000k-orcos-negros-1000k.md](rosters/iniciales/inicio-1000k-orcos-negros-1000k.md) |
| Skavens | Inicio 1000k | 1.000k | [inicio-1000k-skavens-1000k.md](rosters/iniciales/inicio-1000k-skavens-1000k.md) |
| Unión Élfica | Elven Thunders | 1.200k | [elven-thunders-union-elfica-1200k.md](rosters/elven-thunders-union-elfica-1200k.md) |
| Unión Élfica | Inicio 1000k | 1.000k | [inicio-1000k-union-elfica-1000k.md](rosters/iniciales/inicio-1000k-union-elfica-1000k.md) |
| Unión Élfica | Sugerencia torneo | 1.145k | [union-elfica-mas-velocidad-1145k.md](rosters/limite-valoracion/union-elfica-mas-velocidad-1145k.md) |
| No Muertos | Muertos de Risa | 1.100k | [muertos-de-risa-no-muertos-1100k.md](rosters/muertos-de-risa-no-muertos-1100k.md) |
| No Muertos | Inicio 1000k | 1.000k | [inicio-1000k-no-muertos-1000k.md](rosters/iniciales/inicio-1000k-no-muertos-1000k.md) |
| Hombres Lagarto | Pandora | 1.140k | [pandora-hombres-lagarto-1140k.md](rosters/pandora-hombres-lagarto-1140k.md) |
| Hombres Lagarto | Inicio 1000k | 1.000k | [inicio-1000k-hombres-lagarto-1000k.md](rosters/iniciales/inicio-1000k-hombres-lagarto-1000k.md) |

---

## Datos de referencia (`source/`)

Toda la referencia de equipos, habilidades, jugadores estrella, tablas y tiers está en **[`source/`](source/)**. Resumen por tipo:

| Tipo | Dónde | Descripción |
|------|--------|-------------|
| **Equipos** | [Índice (Equipos)](source/index.md#equipos) · [Carpeta `teams/`](source/teams/) | Posiciones, costes, estadísticas (MA, ST, AG, PA, AR), habilidades y progresión por equipo. |
| **Habilidades** | [Índice (Habilidades)](source/index.md#habilidades) · [Carpeta `habilidades/`](source/habilidades/) | Descripción oficial por categoría (Agilidad, Fuerza, General, Mutaciones, Pase, Rasgos, Triquiñuelas). |
| **Jugadores estrella** | [Índice (Jugadores estrella)](source/index.md#jugadores-estrella) · [Carpeta `jugadores-estrella/`](source/jugadores-estrella/) | Coste, estadísticas, habilidades y equipos para los que juegan. |
| **Tiers** | [Oro / presupuesto](source/tiers/oro-presupuesto.md) · [Skill pack](source/tiers/skill-pack.md) | Presupuesto (gp) por tier, Skill Points, límites de secundarias, apilamiento y tabla **Tier \| Equipos** (lista GW). |
| **Tablas de juego** | [Índice (Tablas)](source/index.md#tablas-de-juego) · [Carpeta `tablas/`](source/tablas/) | Heridas y lesiones, clima, patada inicial, plegarias de Nuffle, experiencia y SPP. |
| **Plantilla y más** | [Plantilla roster](source/plantilla-roster.md) · [Convenciones](source/README.md) | Plantilla para crear rosters y convenciones del repo (coste en k, CTD, etc.). |

---

## Preparar un partido (prepartido)

Secuencia típica antes de la primera jugada (3ª Temporada). Consultar las tablas en **[source/tablas/](source/tablas/)**.

1. **Rosters e incentivos**  
   Confirmar TV de cada equipo y calcular **incentivos** (inducements) si hay diferencia de TV. Ver [Incentivos](https://nufflezone.com/incentivos-blood-bowl/) (Nuffle Zone).

2. **Clima**  
   Cada entrenador tira **1D6**; se **suman** los dos resultados (2D6) y se consulta la **[Tabla de Clima](source/tablas/clima.md)**. El resultado aplica a todo el partido hasta que un evento (p. ej. «Clima Cambiante» en Patada Inicial) lo cambie.

3. **Elegir pateador y receptor**  
   Los entrenadores deciden quién **patea** (sale primero) y quién **recibe** (coloca primero y recibe el balón). Suele decidirse por sorteo (1D6, mayor elige).

4. **Despliegue**  
   El equipo **receptor** coloca primero hasta 11 jugadores en su mitad; luego el equipo **pateador** en su mitad. Después se coloca el balón y se realiza la patada.

5. **Patada inicial**  
   En cada **entrada**, después de colocar el balón, el entrenador del equipo **pateador** tira **2D6** en la **[Tabla de Eventos de Patada Inicial](source/tablas/patada-inicial.md)**. Aplicar el efecto antes de que el receptor active jugadores.

6. **Plegarias de Nuffle**  
   Si aplica (p. ej. por evento «Los Hinchas Animan» o por tener menor TV), se tira en la **[Tabla de Plegarias de Nuffle](source/tablas/plegarias-nuffle.md)** (D16; en exhibición puede usarse D8).

---

## Después del partido (postpartido)

En **liga** (o cuando apliquen las reglas de progresión):

1. **Heridas y lesiones**  
   Resolver jugadores en Zona de Lesionados con la **[Tirada de Heridas](source/tablas/heridas-y-lesiones.md)** (2D6), **[Tirada de Lesiones](source/tablas/heridas-y-lesiones.md)** (D16) y, si toca, **[Heridas Permanentes](source/tablas/heridas-y-lesiones.md)** (D6). Aplicar recuperación de Inconscientes si aplica.

2. **Experiencia (PE / SPP)**  
   Asignar PE según **[Experiencia y SPP](source/tablas/experiencia-y-spp.md)**: MVP (aleatorio), touchdowns, heridas por placaje, interceptaciones, pases completos, etc.

3. **Subidas de nivel**  
   Si un jugador alcanza los SPP necesarios (3/6/12 para primaria aleatoria/elegida/secundaria en primer nivel), se hace la subida y se anota la mejora en el roster. El **[coste en TV](source/tablas/experiencia-y-spp.md)** (ej. +20k primaria elegida) actualiza la valoración del equipo.

4. **Actualizar roster**  
   Anotar bajas (muertos, lesiones que pierden partidos), nuevas habilidades y TV actual del equipo.

---

## Blood Bowl Third Season (2025)

- **Reglas base:** [Blood Bowl Third Season (2025)](https://www.warhammer-community.com/blood-bowl-downloads/).
- **Rosters y habilidades:** [NuffleZone.com](https://nufflezone.com) — listas oficiales y noticias.

Para **tiers en torneos** (NAF, Matched Play), ver los enlaces de la tabla anterior (Oro / presupuesto y Skill pack) y [NAF — Tiers and Tiering](https://thenaf.net/tournaments/running-a-tournament/tiers-and-tiering).

---

## Licencia y uso

Uso personal para rosters y referencia. Blood Bowl y NAF son marcas de sus respectivos propietarios.
