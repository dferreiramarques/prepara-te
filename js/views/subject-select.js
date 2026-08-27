import { yearLabel, subjectIsAvailable, yearIsAvailable, subjectsForYear } from "../catalog.js";
import { showToast } from "../toast.js";

export function renderSubjectSelect(root, catalog, yearId) {
  const label = yearLabel(catalog, yearId);
  const generalAvailable = yearIsAvailable(catalog, yearId);

  root.innerHTML = `
    <main class="stage stage--picker">
      <button class="back-link" id="back-link">← Trocar ano</button>
      <p class="picker-intro">${label} · Geral ou por disciplina?</p>
      <div class="tile-grid" id="subject-grid"></div>
    </main>
  `;

  root.querySelector("#back-link").addEventListener("click", () => {
    location.hash = "#/";
  });

  const grid = root.querySelector("#subject-grid");

  const options = [
    { id: "geral", label: "Geral (todas as disciplinas)", available: generalAvailable },
    ...subjectsForYear(catalog, yearId).map((s) => ({
      id: s.id,
      label: s.label,
      available: subjectIsAvailable(catalog, yearId, s.id),
    })),
  ];

  for (const option of options) {
    const tile = document.createElement("button");
    tile.className = "tile" + (option.available ? "" : " tile--locked");
    tile.innerHTML = `
      <span class="tile-label">${option.label}</span>
      ${option.available ? "" : '<span class="tile-badge">brevemente</span>'}
    `;
    tile.addEventListener("click", () => {
      if (!option.available) {
        showToast("Ainda não disponível — brevemente!");
        return;
      }
      location.hash = `#/ano/${yearId}/${option.id}`;
    });
    grid.appendChild(tile);
  }

  return { subtitle: label };
}
