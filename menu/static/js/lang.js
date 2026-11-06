export function Lang() {
  var saved = localStorage.getItem("lang");
  var lang =
    saved || (navigator.language.toLowerCase().startsWith("bg") ? "bg" : "en");

  function setLang(l) {
    document.body.dataset.lang = l;
    document.documentElement.lang = l;
    localStorage.setItem("lang", l);
    document.querySelectorAll(".lang-bg").forEach(function (el) {
      el.style.display = l === "bg" ? "" : "none";
    });
    document.querySelectorAll(".lang-en").forEach(function (el) {
      el.style.display = l === "en" ? "" : "none";
    });
  }

  setLang(lang);
  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () {
      setLang(b.dataset.setLang);
    });
  });
}
