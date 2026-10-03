// Tablas de alineación de los rosters: marca la tabla (columnas Posición + Habilidades),
// etiqueta cada celda con su cabecera (para la vista en tarjetas del móvil) y marca la página.
function prepararTablasRoster() {
  let hay = false;
  document.querySelectorAll(".md-typeset table").forEach((tabla) => {
    const cab = [...tabla.querySelectorAll("thead th")].map((th) => th.textContent.trim());
    const bajo = cab.map((t) => t.toLowerCase());
    if (!bajo.some((t) => t.startsWith("habilidades")) || !bajo.some((t) => t === "posición" || t === "position")) return;
    hay = true;
    tabla.classList.add("tabla-roster");
    const tipo = { "nº": "num", "#": "num", nombre: "nombre", "posición": "pos", coste: "coste", habilidades: "hab",
                   "skill gold": "sg", mv: "stat", fu: "stat", ag: "stat", ps: "stat", ar: "stat",
                   ma: "stat", st: "stat", pa: "stat", av: "stat" };
    const ths = [...tabla.querySelectorAll("thead th")];
    ths.forEach((th, i) => {
      const clave = Object.keys(tipo).find((k) => bajo[i].startsWith(k));
      th.classList.add("c-" + (clave ? tipo[clave] : "otro"));
    });
    tabla.querySelectorAll("tbody tr").forEach((tr) => {
      [...tr.children].forEach((td, i) => {
        const etiqueta = cab[i] || "";
        td.dataset.label = etiqueta;
        const clave = Object.keys(tipo).find((k) => etiqueta.toLowerCase().startsWith(k));
        td.classList.add("c-" + (clave ? tipo[clave] : "otro"));
        if (td.classList.contains("c-nombre") && /^_+$/.test(td.textContent.trim())) td.classList.add("vacio");
      });
      // salto de línea (solo visible en tarjetas) antes del primer atributo
      const stat = tr.querySelector("td.c-stat");
      if (stat && !tr.querySelector("td.c-salto")) {
        const salto = document.createElement("td");
        salto.className = "c-salto";
        salto.setAttribute("aria-hidden", "true");
        tr.insertBefore(salto, stat);
      }
    });
    const nombres = [...tabla.querySelectorAll("tbody td.c-nombre")];
    tabla.classList.toggle("sin-nombres", nombres.length > 0 && nombres.every((td) => td.classList.contains("vacio")));
  });
  document.body.classList.toggle("pagina-roster", hay);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(prepararTablasRoster); // navegación instantánea de Material
} else {
  document.addEventListener("DOMContentLoaded", prepararTablasRoster);
}
