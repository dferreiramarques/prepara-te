import { yearIsAvailable } from "../catalog.js";
import { showToast } from "../toast.js";

export function renderYearSelect(root, catalog) {
  const cycles = [...new Set(catalog.years.map((y) => y.cycle || ""))];

  root.innerHTML = `
    <main class="stage stage--picker">
      <p class="picker-intro">Que ano frequentaste?</p>
      ${cycles
        .map(
          (cycle, i) => `
        <h2 class="cycle-heading">${cycle}</h2>
        <div class="tile-grid" id="year-grid-${i}"></div>
      `
        )
        .join("")}
    </main>
  `;

  cycles.forEach((cycle, i) => {
    const grid = root.querySelector(`#year-grid-${i}`);
    const years = catalog.years.filter((y) => (y.cycle || "") === cycle);
    for (const year of years) {
      const available = yearIsAvailable(catalog, year.id);
      const tile = document.createElement("button");
      tile.className = "tile" + (available ? "" : " tile--locked");
      tile.innerHTML = `
        <span class="tile-label">${year.label}</span>
        ${available ? "" : '<span class="tile-badge">brevemente</span>'}
      `;
      tile.addEventListener("click", () => {
        if (!available) {
          showToast("Ainda não disponível — brevemente!");
          return;
        }
        location.hash = `#/ano/${year.id}`;
      });
      grid.appendChild(tile);
    }
  });

  return { subtitle: "Escolhe o teu ano" };
}
