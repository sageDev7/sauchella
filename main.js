(function () {
  "use strict";
  var body = document.body;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- WhatsApp: un solo número; mensaje que ya filtra la consulta ---------- */
  var WA_NUMBER = "5491150419561";
  document.querySelectorAll(".js-wa").forEach(function (el) {
    var msg = el.getAttribute("data-msg") || "Hola, quisiera consultar por una causa penal en etapa de juicio oral.";
    el.href = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(msg);
    el.target = "_blank";
    el.rel = "noopener";
  });

  /* ---------- boceto: páginas internas todavía no construidas ---------- */
  document.querySelectorAll("[data-soon]").forEach(function (el) {
    el.addEventListener("click", function (e) { e.preventDefault(); });
  });

  /* ---------- header ---------- */
  var hdr = document.getElementById("hdr");
  function onScroll() { hdr.classList.toggle("sc", window.scrollY > 40); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- menú mobile (la hamburguesa se transforma en cruz) ---------- */
  var burger = document.getElementById("burger");
  function setNav(open) {
    body.classList.toggle("nav-open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    burger.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  }
  burger.addEventListener("click", function () { setNav(!body.classList.contains("nav-open")); });
  document.getElementById("mnavOv").addEventListener("click", function () { setNav(false); });
  document.querySelectorAll(".mnav a").forEach(function (a) { a.addEventListener("click", function () { setNav(false); }); });

  /* ---------- título: entra palabra por palabra (conserva el <em>) ---------- */
  var wordIdx = 0;
  function splitWords(node) {
    Array.prototype.slice.call(node.childNodes).forEach(function (n) {
      if (n.nodeType === 3) {
        var frag = document.createDocumentFragment();
        n.textContent.split(/([ \t\n\r]+)/).forEach(function (part) {   // el &nbsp; no separa: mantiene juntas las palabras que deben ir juntas
          if (!part) return;
          if (/^[ \t\n\r]+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
          var w = document.createElement("span");
          w.className = "w";
          w.textContent = part;
          w.style.animationDelay = (0.2 + wordIdx++ * 0.08) + "s";
          frag.appendChild(w);
        });
        node.replaceChild(frag, n);
      } else if (n.nodeType === 1 && n.tagName !== "BR") {
        splitWords(n);
      }
    });
  }
  if (!reduce) document.querySelectorAll(".split-words").forEach(splitWords);

  /* ---------- contadores ---------- */
  function runCount(el) {
    var to = parseFloat(el.getAttribute("data-to")), pre = el.getAttribute("data-prefix") || "";
    var dur = 1800, t0 = null;
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - k, 4);
      el.textContent = pre + Math.round(to * e);
      if (k < 1) requestAnimationFrame(step);
    }
    el.textContent = pre + "0";
    requestAnimationFrame(step);
  }
  if (!reduce && "IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { runCount(en.target); cio.unobserve(en.target); } });
    }, { threshold: 0.6 });
    document.querySelectorAll(".count").forEach(function (el) { cio.observe(el); });
  }

  /* ---------- preguntas: acordeón con apertura suave (una abierta a la vez por lista) ---------- */
  function animateTo(a, from, to, done) {
    a.style.height = from + "px";
    requestAnimationFrame(function () {
      a.style.transition = "height .45s cubic-bezier(.2,.7,.2,1)";
      a.style.height = to + "px";
    });
    a.addEventListener("transitionend", function te() { a.removeEventListener("transitionend", te); a.style.cssText = ""; if (done) done(); });
  }
  function closeFaq(d) {
    if (reduce) { d.open = false; return; }
    var a = d.querySelector(".faq-a");
    animateTo(a, a.scrollHeight, 0, function () { d.open = false; });
  }
  document.querySelectorAll(".faq-list details").forEach(function (d) {
    d.querySelector("summary").addEventListener("click", function (e) {
      e.preventDefault();
      if (d.open) { closeFaq(d); return; }
      d.closest(".faq-list").querySelectorAll("details").forEach(function (o) { if (o !== d && o.open) closeFaq(o); });
      d.open = true;
      if (reduce) return;
      var a = d.querySelector(".faq-a");
      animateTo(a, 0, a.scrollHeight);
    });
  });

  /* ---------- reveals (y la franja del proceso, que se llena al aparecer) ---------- */
  var items = document.querySelectorAll(".reveal, .proceso");
  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- parallax de la cabecera ---------- */
  var heroBg = document.querySelector(".hero-bg, .ph-bg"), ticking = false;
  if (heroBg && !reduce) {
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        if (window.scrollY < window.innerHeight * 1.2) heroBg.style.transform = "translate3d(0," + (window.scrollY * 0.25) + "px,0)";
      });
    }, { passive: true });
  }

  /* ---------- formulario (FormSubmit + modal) ---------- */
  var form = document.getElementById("contactForm"), btn = document.getElementById("formSubmitBtn");
  var iframe = document.getElementById("formsubmit-iframe"), modal = document.getElementById("okModal"), sending = false;
  if (form) {
    var valid = function (input) {
      var v = input.value.trim();
      var ok = v !== "" && (input.type !== "email" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
      input.closest(".field").classList.toggle("err", !ok);
      return ok;
    };
    form.addEventListener("submit", function (e) {
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (i) { if (!valid(i)) ok = false; });
      if (!ok) { e.preventDefault(); var f = form.querySelector(".field.err input,.field.err select,.field.err textarea"); if (f) f.focus(); return; }
      sending = true; btn.disabled = true; btn.textContent = "Enviando...";
    });
    form.querySelectorAll("[required]").forEach(function (i) {
      i.addEventListener("input", function () { if (i.closest(".field").classList.contains("err")) valid(i); });
      i.addEventListener("change", function () { if (i.closest(".field").classList.contains("err")) valid(i); });
    });
    iframe.addEventListener("load", function () {
      if (!sending) return;
      sending = false; form.reset(); btn.disabled = false; btn.textContent = "Enviar consulta";
      modal.classList.add("show");
    });
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.hasAttribute("data-close")) modal.classList.remove("show"); });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { setNav(false); if (modal) modal.classList.remove("show"); }
  });

  // ---------- reseñas: carrusel (reseñas fijas, se actualizan a mano) ----------
  var track = document.getElementById("resTrack");
  function clamp(card) {
    var p = card.querySelector("blockquote p");
    if (p.scrollHeight - p.clientHeight < 4 || card.querySelector(".res-more")) return;
    var b = document.createElement("button");
    b.type = "button"; b.className = "res-more"; b.textContent = "Leer más";
    b.addEventListener("click", function () { b.textContent = card.classList.toggle("open") ? "Leer menos" : "Leer más"; });
    card.insertBefore(b, card.querySelector("figcaption"));
  }
  if (track) {
    [].forEach.call(track.children, clamp);
    document.querySelectorAll(".res-btn").forEach(function (b) {
      b.addEventListener("click", function () {
        var c = track.querySelector(".res-card");
        track.scrollBy({ left: (c.offsetWidth + 22) * +b.dataset.dir, behavior: reduce ? "auto" : "smooth" });
      });
    });
  }

  document.getElementById("yr").textContent = new Date().getFullYear();
})();
