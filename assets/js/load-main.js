// Defer Minimal Mistakes' theme bundle (jQuery + greedy-nav + plugins) until
// after webfonts have loaded. Greedy-nav caches menu-item widths the first
// time it runs; if Fraunces hasn't loaded yet it caches the fallback widths
// and never recomputes, leaving the hamburger collapse broken at narrow
// viewports.
(function () {
  function loadMain() {
    var s = document.createElement("script");
    s.src = "/assets/js/main.min.js";
    s.async = false;
    document.body.appendChild(s);
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(loadMain, loadMain);
  } else {
    loadMain();
  }
})();
