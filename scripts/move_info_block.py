#!/usr/bin/env python3
"""Mueve el bloque '## Información del equipo' para que quede debajo de la tabla de desglose TV."""
import re
from pathlib import Path

ROSTERS = Path(__file__).resolve().parent.parent / "rosters"

def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    # Solo si actualmente Información del equipo va ANTES de Alineación
    if "## Información del equipo" not in text or "## Alineación" not in text:
        return False
    pos_info = text.find("## Información del equipo")
    pos_alineacion = text.find("## Alineación")
    if pos_info > pos_alineacion:
        return False  # Ya está después
    # Extraer el bloque Información (hasta el ## Alineación exclusive)
    block_end = text.find("\n## Alineación", pos_info)
    if block_end == -1:
        return False
    info_block = text[pos_info:block_end]
    rest_after_info = text[block_end:]  # desde "\n## Alineación"
    # Quitar el bloque de su posición actual
    text_without = text[:pos_info].rstrip() + "\n\n" + rest_after_info.lstrip()
    # Buscar dónde insertar: después de la línea | **Total TV** | **...** |
    total_tv = re.search(r'\|\s*\*\*Total TV\*\*\s*\|\s*\*\*[^*]+\*\*\s*\|', text_without)
    if not total_tv:
        return False
    insert_pos = total_tv.end()
    # Insertar después del bloque (hasta el próximo ##)
    next_sec = text_without.find("\n## ", insert_pos)
    if next_sec != -1:
        insert_pos = next_sec
    else:
        next_nl = text_without.find("\n", insert_pos)
        if next_nl != -1:
            insert_pos = next_nl + 1
    new_text = (
        text_without[:insert_pos].rstrip() +
        "\n\n" + info_block + "\n\n" +
        text_without[insert_pos:].lstrip()
    )
    path.write_text(new_text, encoding="utf-8")
    return True

def main():
    count = 0
    for md in ROSTERS.rglob("*.md"):
        if "README" in md.name or md.name.startswith("."):
            continue
        try:
            if process(md):
                count += 1
                print(md.relative_to(ROSTERS))
        except Exception as e:
            print(f"Error {md}: {e}")
    print(f"Procesados: {count}")

if __name__ == "__main__":
    main()
