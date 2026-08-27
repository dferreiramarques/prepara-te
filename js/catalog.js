let catalogPromise = null;

export function loadCatalog() {
  if (!catalogPromise) {
    catalogPromise = fetch("data/catalog.json").then((res) => res.json());
  }
  return catalogPromise;
}

export function yearLabel(catalog, yearId) {
  return catalog.years.find((y) => y.id === yearId)?.label || yearId;
}

export function subjectLabel(catalog, subjectId) {
  return catalog.subjects.find((s) => s.id === subjectId)?.label || subjectId;
}

export function decksForYear(catalog, yearId) {
  return catalog.decks.filter((d) => d.year === yearId);
}

export function yearIsAvailable(catalog, yearId) {
  return decksForYear(catalog, yearId).length > 0;
}

export function subjectIsAvailable(catalog, yearId, subjectId) {
  return catalog.decks.some((d) => d.year === yearId && d.subject === subjectId);
}

// only the subjects that belong to the given year's cycle (e.g. HGP is
// 2º ciclo only; História/Geografia are 3º ciclo only)
export function subjectsForYear(catalog, yearId) {
  const year = catalog.years.find((y) => y.id === yearId);
  if (!year) return catalog.subjects;
  return catalog.subjects.filter((s) => !s.cycles || s.cycles.includes(year.cycle));
}

// files to load for a given year + "geral" or a specific subject id
export function deckFilesFor(catalog, yearId, subjectOrGeral) {
  if (subjectOrGeral === "geral") {
    return decksForYear(catalog, yearId).map((d) => d.file);
  }
  const deck = catalog.decks.find((d) => d.year === yearId && d.subject === subjectOrGeral);
  return deck ? [deck.file] : [];
}
