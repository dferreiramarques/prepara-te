import { deckFilesFor, yearLabel, subjectLabel } from "./catalog.js";
import { loadDeckProgress, saveDeckProgress, resetDeckProgress, ensureToday } from "./progress.js";
import { showToast } from "./toast.js";

const DOMAIN_SLUGS = {
  "Números": "numeros",
  "Geometria e Medida": "geometria",
  "Álgebra": "algebra",
  "Dados e Probabilidade": "dados",
  "Gramática": "gramatica",
  "Educação Literária": "literaria",
  "Leitura": "leitura",
  "Escrita": "escrita",
  "Oralidade": "oralidade",
  "A água, o ar, as rochas e o solo – materiais terrestres": "materiais-terrestres",
  "Diversidade de seres vivos e suas interações com o meio": "seres-vivos",
  "Unidade na diversidade de seres vivos": "celula",
  "A Península Ibérica – localização e quadro natural": "peninsula",
  "Península Ibérica: dos primeiros povos à formação de Portugal": "primeiros-povos",
  "Portugal do século XIII a 1385": "seculo-xiii",
  "Portugal do século XV ao século XVII": "seculo-xv",
  "Vocabulário": "vocabulario",
  "Gramática Inglesa": "gramatica-en",
  "Cultura e Países Anglófonos": "cultura-en",
};
const FALLBACK_SLUGS = Object.values(DOMAIN_SLUGS);

function domainSlugMap(domains) {
  const map = {};
  const unknown = domains.filter((d) => !DOMAIN_SLUGS[d]);
  for (const d of domains) {
    map[d] = DOMAIN_SLUGS[d] || FALLBACK_SLUGS[unknown.indexOf(d) % FALLBACK_SLUGS.length];
  }
  return map;
}

export async function renderStudy(root, catalog, yearId, subjectOrGeral) {
  const files = deckFilesFor(catalog, yearId, subjectOrGeral);
  const heading = subjectOrGeral === "geral" ? "Geral" : subjectLabel(catalog, subjectOrGeral);
  const subtitle = `${yearLabel(catalog, yearId)} · ${heading}`;

  if (!files.length) {
    root.innerHTML = `<main class="stage stage--picker"><p class="picker-intro">Ainda não há cartões para esta escolha.</p></main>`;
    return { subtitle };
  }

  const decks = await Promise.all(files.map((f) => fetch(f).then((r) => r.json())));
  const allCards = decks.flatMap((d) => d.cards);
  const domains = [...new Set(allCards.map((c) => c.domain))];
  const slugFor = domainSlugMap(domains);
  const deckKey = `${yearId}:${subjectOrGeral}`;

  root.innerHTML = `
    <button class="back-link back-link--floating" id="back-link">← ${subtitle}</button>
    <button class="tabs-toggle" id="tabs-toggle" aria-expanded="false" aria-controls="domain-tabs">
      <span class="tabs-toggle-label" id="tabs-toggle-label">Temas <span class="tabs-toggle-count">(${domains.length})</span></span>
      <span class="tabs-toggle-icon" aria-hidden="true">▾</span>
    </button>
    <nav class="tabs" id="domain-tabs" aria-label="Filtrar por domínio" hidden>
      <button class="tab tab--all is-active" data-domain="__all__">Todos<span class="tab-count" id="count-all"></span></button>
      ${domains.map((d) => `<button class="tab tab--${slugFor[d]}" data-domain="${d}">${d}<span class="tab-count" id="count-${d}"></span></button>`).join("")}
    </nav>

    <main class="stage">
      <div class="deck-meta">
        <span id="deck-position">— / —</span>
        <span class="dot">·</span>
        <span id="deck-topic">a carregar…</span>
      </div>

      <div class="card-wrap">
        <button class="card" id="flashcard" aria-live="polite">
          <div class="card-face card-front">
            <span class="tag" id="front-tag">Domínio</span>
            <p class="question" id="front-question"></p>
            <span class="flip-hint">toca para ver a resposta</span>
          </div>
          <div class="card-face card-back">
            <span class="tag tag--answer">Resposta</span>
            <p class="answer" id="back-answer"></p>
            <p class="explanation" id="back-explanation"></p>
            <span class="flip-hint">toca para voltar à pergunta</span>
          </div>
        </button>
      </div>

      <div class="rate-row" id="rate-row" hidden>
        <button class="rate-btn rate-btn--no" data-know="0">Ainda não sei</button>
        <button class="rate-btn rate-btn--yes" data-know="1">Já sei ✓</button>
      </div>

      <div class="controls">
        <button class="btn btn--ghost" id="prev-btn" aria-label="Cartão anterior">←</button>
        <button class="btn btn--primary" id="next-btn">Próxima carta</button>
        <button class="btn btn--ghost" id="shuffle-btn" aria-label="Baralhar">⤨ Baralhar</button>
      </div>
    </main>

    <footer class="statsbar">
      <div class="stat"><span class="stat-num" id="stat-today">0</span><span class="stat-label">hoje</span></div>
      <div class="stat"><span class="stat-num" id="stat-streak">0</span><span class="stat-label">seguidas certas</span></div>
      <div class="stat"><span class="stat-num" id="stat-mastered">0</span><span class="stat-label">dominados</span></div>
      <button class="reset-link" id="reset-progress">reiniciar progresso</button>
    </footer>
  `;

  const els = {
    tabs: root.querySelector("#domain-tabs"),
    tabsToggle: root.querySelector("#tabs-toggle"),
    tabsToggleLabel: root.querySelector("#tabs-toggle-label"),
    backLink: root.querySelector("#back-link"),
    card: root.querySelector("#flashcard"),
    frontTag: root.querySelector("#front-tag"),
    frontQuestion: root.querySelector("#front-question"),
    backAnswer: root.querySelector("#back-answer"),
    backExplanation: root.querySelector("#back-explanation"),
    deckPosition: root.querySelector("#deck-position"),
    deckTopic: root.querySelector("#deck-topic"),
    rateRow: root.querySelector("#rate-row"),
    nextBtn: root.querySelector("#next-btn"),
    prevBtn: root.querySelector("#prev-btn"),
    shuffleBtn: root.querySelector("#shuffle-btn"),
    statToday: root.querySelector("#stat-today"),
    statStreak: root.querySelector("#stat-streak"),
    statMastered: root.querySelector("#stat-mastered"),
    resetBtn: root.querySelector("#reset-progress"),
  };

  let progress = loadDeckProgress(deckKey);
  let pool = [];
  let history = [];
  let historyIndex = -1;
  let activeDomain = "__all__";

  function byId(id) {
    return allCards.find((c) => c.id === id);
  }

  function currentPoolIds() {
    return activeDomain === "__all__"
      ? allCards.map((c) => c.id)
      : allCards.filter((c) => c.domain === activeDomain).map((c) => c.id);
  }

  function cardWeight(id) {
    const s = progress.cardStats[id];
    if (!s) return 3;
    if (s.know === 0) return 4;
    return Math.max(1, 3 - s.knowStreak);
  }

  function weightedPick(ids) {
    const recent = new Set(history.slice(-4));
    const candidates = ids.filter((id) => !recent.has(id));
    const list = candidates.length ? candidates : ids;
    const weights = list.map(cardWeight);
    const total = weights.reduce((a, b) => a + b, 0);
    let r = Math.random() * total;
    for (let i = 0; i < list.length; i++) {
      r -= weights[i];
      if (r <= 0) return list[i];
    }
    return list[list.length - 1];
  }

  function renderCounts() {
    const counts = { __all__: allCards.length };
    for (const c of allCards) counts[c.domain] = (counts[c.domain] || 0) + 1;
    root.querySelector("#count-all").textContent = ` ${counts.__all__ || 0}`;
    for (const d of domains) {
      const el = root.querySelector(`#count-${CSS.escape(d)}`);
      if (el) el.textContent = ` ${counts[d] || 0}`;
    }
  }

  function renderCard(id, { flipped = false } = {}) {
    const c = byId(id);
    if (!c) return;
    els.card.classList.toggle("is-flipped", flipped);
    els.card.style.setProperty("--domain-color", `var(--${slugFor[c.domain]})`);
    els.card.style.setProperty("--domain-bg", `var(--${slugFor[c.domain]}-bg)`);
    els.frontTag.textContent = c.domain;
    els.frontQuestion.textContent = c.question;
    els.backAnswer.textContent = c.answer;
    els.backExplanation.textContent = c.explanation;
    els.deckTopic.textContent = c.topic;
    const total = currentPoolIds().length;
    const seen = Object.keys(progress.cardStats).filter((k) => currentPoolIds().includes(k)).length;
    els.deckPosition.textContent = `${seen} / ${total} revistos`;
    els.rateRow.hidden = !flipped;
  }

  function showNext() {
    pool = currentPoolIds();
    if (!pool.length) return;
    const id = weightedPick(pool);
    history.push(id);
    if (history.length > 50) history.shift();
    historyIndex = history.length - 1;
    renderCard(id, { flipped: false });
  }

  function showPrev() {
    if (historyIndex <= 0) return;
    historyIndex -= 1;
    renderCard(history[historyIndex], { flipped: false });
  }

  function flipCurrent() {
    const isFlipped = els.card.classList.contains("is-flipped");
    renderCard(history[historyIndex], { flipped: !isFlipped });
  }

  function renderStats() {
    ensureToday(progress);
    els.statToday.textContent = progress.todayCount;
    els.statStreak.textContent = progress.streak;
    const mastered = Object.values(progress.cardStats).filter((s) => s.know === 1 && s.knowStreak >= 2).length;
    els.statMastered.textContent = mastered;
  }

  function rate(know) {
    const id = history[historyIndex];
    const s = progress.cardStats[id] || { know: null, knowStreak: 0, seenCount: 0 };
    s.seenCount += 1;
    if (know) {
      s.knowStreak = (s.know === 1 ? s.knowStreak : 0) + 1;
      progress.streak += 1;
    } else {
      s.knowStreak = 0;
      progress.streak = 0;
    }
    s.know = know;
    progress.cardStats[id] = s;

    ensureToday(progress);
    progress.todayCount += 1;
    saveDeckProgress(deckKey, progress);
    renderStats();
    showToast(know ? "Boa! ✓" : "Vamos rever mais vezes esta 🔁");
    setTimeout(showNext, 420);
  }

  function updateTabsToggleLabel() {
    els.tabsToggleLabel.innerHTML =
      activeDomain === "__all__"
        ? `Temas <span class="tabs-toggle-count">(${domains.length})</span>`
        : activeDomain;
  }

  function collapseTabs() {
    els.tabs.hidden = true;
    els.tabsToggle.setAttribute("aria-expanded", "false");
    els.tabsToggle.classList.remove("is-open");
  }

  function setActiveDomain(domain) {
    activeDomain = domain;
    root.querySelectorAll(".tab").forEach((t) => {
      t.classList.toggle("is-active", t.dataset.domain === domain);
    });
    updateTabsToggleLabel();
    collapseTabs();
    history = [];
    historyIndex = -1;
    showNext();
  }

  els.tabsToggle.addEventListener("click", () => {
    const expanded = els.tabsToggle.getAttribute("aria-expanded") === "true";
    els.tabs.hidden = expanded;
    els.tabsToggle.setAttribute("aria-expanded", String(!expanded));
    els.tabsToggle.classList.toggle("is-open", !expanded);
  });

  els.card.addEventListener("click", flipCurrent);
  els.card.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); flipCurrent(); }
  });
  els.nextBtn.addEventListener("click", showNext);
  els.prevBtn.addEventListener("click", showPrev);
  els.shuffleBtn.addEventListener("click", showNext);
  els.rateRow.addEventListener("click", (e) => {
    const btn = e.target.closest(".rate-btn");
    if (!btn) return;
    rate(Number(btn.dataset.know));
  });
  els.tabs.addEventListener("click", (e) => {
    const btn = e.target.closest(".tab");
    if (!btn) return;
    setActiveDomain(btn.dataset.domain);
  });
  els.resetBtn.addEventListener("click", () => {
    if (!confirm("Reiniciar o progresso guardado neste dispositivo para esta escolha?")) return;
    progress = resetDeckProgress(deckKey);
    renderStats();
    showToast("Progresso reiniciado");
  });
  els.backLink.addEventListener("click", () => {
    location.hash = `#/ano/${yearId}`;
  });

  renderCounts();
  renderStats();
  showNext();

  return { subtitle };
}
