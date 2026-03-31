<!-- Plantilla para el Roster Builder: rellenar todos los [MARCADORES] y reemplazar las secciones "…" con los datos del roster.

**Nombre del archivo (obligatorio):** Al guardar, el archivo debe llamarse:
**[nombre que le ha puesto el usuario al equipo] - [nombre del equipo/raza] - [valoración del equipo]**
en formato slug (minúsculas, guiones, sin acentos), extensión .md, dentro de la carpeta `rosters/`.

- **Nombre del usuario:** el que el usuario da a su equipo (ej. Barones Bigotudos, Elven Thunders, Muertos de Risa).
- **Nombre del equipo/raza:** la raza o equipo oficial (ej. Nobleza Imperial, Unión Élfica, No Muertos).
- **Valoración:** la TV final del roster en miles con «k» (ej. 1070k, 1200k).

Ejemplos de nombre de archivo:
- `barones-bigotudos-nobleza-imperial-1070k.md`
- `elven-thunders-union-elfica-1200k.md`
- `muertos-de-risa-no-muertos-1100k.md`

Regla: todo lo que tenga precio debe aparecer al lado del nombre (o en la misma línea): jugadores → columna Coste; rerolls, apotecario, fans → en desglose TV con cantidad y precio; habilidades → en descripción **Nombre (English) — 20k / 40k / incl.:**
-->

# [RAZA] — [NOMBRE DEL EQUIPO] ([TV]k)

![RAZA](images/equipos/[SLUG_EQUIPO].webp)

*Si copias esta plantilla a `rosters/` o `rosters/iniciales/`, cambia la imagen a `../../source/images/equipos/[SLUG_EQUIPO].webp` (o la ruta relativa que corresponda desde ese archivo).*

> [Nota opcional: ej. "Roster inicial torneo NAF" o "Datos desde BB Roster (bbrosters)".]

## Alineación

*En **negrita**, las habilidades ganadas por progresión. Orden: [indicar orden usado, ej. Big Guy → Throwers → Blitzers → Catchers → Linemen].*

| Nº | Nombre | Posición | Coste | MA | ST | AG | PA | AR | Habilidades |
|----|--------|----------|-------|----|----|----|----|----|-------------|
| 1  | [— / nombre] | [Posición] | [Coste]k | [MA] | [ST] | [AG] | [PA / —] | [AR] | [Habilidades de roster], **[Habilidad progresión]** |
| …  | …      | …         | …     | …  | …  | …  | …  | …  | … |
| N  | …      | …         | …     | …  | …  | …  | …  | …  | … |

**Total jugadores:** [N] | **TV:** [TV]k

**Desglose TV (todo lo que tiene precio):** Incluir siempre una tabla con cada partida. Referencia de precios: Reroll 50.000 | Apotecario 50.000 | Fans dedicados 10.000 c/u | Habilidades: primaria elegida +20k, secundaria elegida +40k (`source/tablas/experiencia-y-spp.md`).

| Concepto | Coste |
|----------|--------|
| Jugadores (desglose por posición o total) | [XXX].000 |
| Rerolls ([N] × 50.000) | [XXX].000 |
| Apotecario (si Sí) | 50.000 |
| Fans dedicados ([N] × 10.000) | [XXX].000 |
| Habilidades progresión (listar o total) | [XXX].000 |
| **Total TV** | **[TV].000** |

## Información del equipo

| Concepto | Valor |
|----------|--------|
| **Tier NAF** | [Tier 1 / Tier 2 / Tier 3 / Tier 4] |
| **Valoración del equipo (TV)** | [TV]k (incl. coste de habilidades; ver desglose) |
| **Total plantilla** | [N] jugadores |
| **Tesorería actual** | [0 / positivo / negativo; ej. -60.000] |
| **Rerolls** | [N] |
| **Asistentes de entrenador** | [N] |
| **Cheerleaders** | [N] |
| **Fans dedicados** | [N] |
| **Apotecario** | [Sí / No / No aplica + motivo si procede] |

## Descripción oficial de las habilidades

* **Todas las habilidades que aparecen en la tabla de jugadores (columna Habilidades) deben tener aquí su descripción.** Una línea por cada habilidad distinta. **Incluir siempre el coste en TV al lado del nombre:** **Nombre (English) — Xk:** descripción. Usar 20k (primaria elegida), 40k (secundaria elegida) o **incl.** si la habilidad viene de la posición (ya en el coste del jugador). Textos en `source/habilidades/` o `source/teams/<raza>.md`.

* **[Habilidad 1] ([English]) — [20k / 40k / incl.]:**
* **[Habilidad 2] ([English]) — [20k / 40k / incl.]:**
* …

## Inducements

- Rerolls, Apothecary (si aplica), Fans dedicados — según reglamento del torneo.

## Estrategia

- **Ataque:** [2–3 líneas: cómo atacar con este roster].
- **Defensa:** [2–3 líneas: cómo defender].

## Progresión recomendada

- **[Tipo jugador 1]:** Primaria [habilidad]; secundarias [lista]. (Alineado con Pri/Sec de `source/teams/<raza>.md` y FUMBBL BB25.)
- **[Tipo jugador 2]:** …
- …
