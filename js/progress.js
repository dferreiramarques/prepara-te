const STORAGE_KEY = "prepara-te-progress-v1";
const OLD_STORAGE_KEY = "revisoes5-progress-v1";

function todayKey() {
  return new Date().toISOString().slice(0, 10);
}

function emptyDeckProgress() {
  return { cardStats: {}, today: todayKey(), todayCount: 0, streak: 0 };
}

function loadStore() {
  let store = null;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) store = JSON.parse(raw);
  } catch (e) { /* ignore corrupt storage */ }
  if (!store) store = { decks: {} };

  // one-time migration from the old single-deck (5º ano Matemática) key
  if (!store.decks["5:matematica"]) {
    try {
      const oldRaw = localStorage.getItem(OLD_STORAGE_KEY);
      if (oldRaw) store.decks["5:matematica"] = JSON.parse(oldRaw);
    } catch (e) { /* ignore corrupt storage */ }
  }

  return store;
}

function saveStore(store) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
}

// deckKey is "<yearId>:<subjectOrGeral>", e.g. "5:matematica" or "5:geral"
export function loadDeckProgress(deckKey) {
  const store = loadStore();
  if (!store.decks[deckKey]) store.decks[deckKey] = emptyDeckProgress();
  saveStore(store);
  return store.decks[deckKey];
}

export function saveDeckProgress(deckKey, progress) {
  const store = loadStore();
  store.decks[deckKey] = progress;
  saveStore(store);
}

export function resetDeckProgress(deckKey) {
  const fresh = emptyDeckProgress();
  saveDeckProgress(deckKey, fresh);
  return fresh;
}

export function ensureToday(progress) {
  const key = todayKey();
  if (progress.today !== key) {
    progress.today = key;
    progress.todayCount = 0;
  }
  return progress;
}
