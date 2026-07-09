(function () {
  var doc = document.documentElement;

  /* ---------- theme toggle ---------- */
  var toggle = document.getElementById('themeToggle');
  function effectiveTheme() {
    return doc.dataset.theme ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      doc.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  /* ---------- contents drawer (mobile) ---------- */
  var drawerBtn = document.getElementById('drawerBtn');
  var veil = document.getElementById('drawerVeil');
  function closeDrawer() { document.body.classList.remove('drawer-open'); }
  if (drawerBtn) {
    drawerBtn.addEventListener('click', function () {
      document.body.classList.toggle('drawer-open');
    });
  }
  if (veil) veil.addEventListener('click', closeDrawer);
  [].slice.call(document.querySelectorAll('.drawer-list a')).forEach(function (a) {
    a.addEventListener('click', closeDrawer);
  });
})();
