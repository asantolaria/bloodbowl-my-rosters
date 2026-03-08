# Imágenes — Nuffle Zone

Imágenes de equipos obtenidas desde [Nuffle Zone](https://nufflezone.com/equipos-blood-bowl/) para uso en las fichas de `source/teams/` y en los rosters de `rosters/`.

## Estructura

- **`equipos/`** — Una imagen por equipo (logo o ilustración). Nombre del archivo: slug del equipo (ej. `altos-elfos.webp`, `khorne.png`).

## Cómo descargar las imágenes

Desde la raíz del repositorio, con Python 3 y `requests` instalado:

```bash
pip install requests
python scripts/download_nufflezone_images.py
```

El script descarga la [página índice de equipos](https://nufflezone.com/equipos-blood-bowl/) de Nuffle Zone, extrae la imagen (logo) asociada a cada equipo y la guarda en `source/images/equipos/<slug>.<ext>`.

Si no usas Python, puedes descargar manualmente desde la página de equipos de Nuffle Zone y guardar cada logo con el nombre del slug (ej. `altos-elfos.jpg`) en `source/images/equipos/`.

## Uso en fichas y rosters

- En **`source/teams/*.md`** la imagen se referencia como `![Nombre equipo](images/equipos/<slug>.webp)` (ruta relativa a `source/`; Khorne usa `.png`).
- En **`rosters/*.md`** se usa la imagen del equipo correspondiente: `![Equipo](../source/images/equipos/<slug>.webp)` o la ruta relativa que aplique según dónde se visualice el markdown.

## Origen y uso

Las imágenes son de Nuffle Zone. Uso para referencia personal y rosters del proyecto. Si publicas o redistribuyes, respeta los derechos del sitio.
