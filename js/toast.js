let hideTimer = null;

export function showToast(msg) {
  const el = document.getElementById("toast");
  if (!el) return;
  el.textContent = msg;
  el.hidden = false;
  clearTimeout(hideTimer);
  hideTimer = setTimeout(() => { el.hidden = true; }, 1400);
}
