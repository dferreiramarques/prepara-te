import { yearIsAvailable } from "../catalog.js";
import { showToast } from "../toast.js";

export function renderYearSelect(root, catalog) {
  root.innerHTML = `
    <main class="stage stage--picker">
      <p class="picker-intro">Que ano frequentaste?</p>
      <div class="tile-grid" id="year-grid"></div>
    </main>
  `;

  const grid = root.querySelector("#year-grid");
  for (const year of catalog.years) {
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

  return { subtitle: "Escolhe o teu ano" };
}
