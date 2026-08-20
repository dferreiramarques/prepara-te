import { renderYearSelect } from "./views/year-select.js";
import { renderSubjectSelect } from "./views/subject-select.js";
import { renderStudy } from "./study.js";

function parseHash() {
  const hash = location.hash.replace(/^#\/?/, "");
  const parts = hash.split("/").filter(Boolean);
  if (parts[0] === "ano" && parts[1] && parts[2]) {
    return { view: "study", yearId: parts[1], subjectOrGeral: parts[2] };
  }
  if (parts[0] === "ano" && parts[1]) {
    return { view: "subject-select", yearId: parts[1] };
  }
  return { view: "year-select" };
}

export function createRouter(root, catalog, onSubtitleChange) {
  async function route() {
    const r = parseHash();
    let result;
    if (r.view === "study") {
      result = await renderStudy(root, catalog, r.yearId, r.subjectOrGeral);
    } else if (r.view === "subject-select") {
      result = renderSubjectSelect(root, catalog, r.yearId);
    } else {
      result = renderYearSelect(root, catalog);
    }
    if (result?.subtitle) onSubtitleChange(result.subtitle);
  }

  window.addEventListener("hashchange", route);
  return { route };
}
