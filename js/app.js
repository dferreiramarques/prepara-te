import { loadCatalog } from "./catalog.js";
import { createRouter } from "./router.js";

async function init() {
  const viewRoot = document.getElementById("view-root");
  const subtitleEl = document.getElementById("brand-subtitle");

  const catalog = await loadCatalog();
  const router = createRouter(viewRoot, catalog, (subtitle) => {
    subtitleEl.textContent = subtitle;
  });
  router.route();

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").catch(() => {});
  }

  let deferredPrompt = null;
  const installBtn = document.getElementById("install-btn");
  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferredPrompt = e;
    installBtn.hidden = false;
  });
  installBtn.addEventListener("click", async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installBtn.hidden = true;
  });
  window.addEventListener("appinstalled", () => { installBtn.hidden = true; });
}

init();
