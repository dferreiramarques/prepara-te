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

  const installBtn = document.getElementById("install-btn");
  const installHelp = document.getElementById("install-help");
  const installHelpClose = document.getElementById("install-help-close");

  const isStandalone =
    window.matchMedia("(display-mode: standalone)").matches ||
    window.navigator.standalone === true;
  const isIOS =
    /iP(hone|od|ad)/.test(navigator.userAgent) ||
    (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);

  let deferredPrompt = null;

  if (!isStandalone && isIOS) {
    // iOS never fires beforeinstallprompt; show manual instructions instead.
    installBtn.hidden = false;
  }

  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferredPrompt = e;
    installBtn.hidden = false;
  });

  installBtn.addEventListener("click", async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      await deferredPrompt.userChoice;
      deferredPrompt = null;
      installBtn.hidden = true;
      return;
    }
    installHelp.hidden = !installHelp.hidden;
  });
  installHelpClose.addEventListener("click", () => { installHelp.hidden = true; });
  window.addEventListener("appinstalled", () => {
    installBtn.hidden = true;
    installHelp.hidden = true;
  });
}

init();
