export function fitCollage() {
  var collage = document.querySelector(".collage");
  var tiles = collage.querySelectorAll(".polaroid");
  if (!tiles.length) return;

  // space for the category bar, plus a small gap (same at the bottom)
  var bar = document.querySelector(".cat-bar");
  var space = (bar ? bar.offsetHeight : 0) + 16;
  collage.style.paddingTop = space + "px";
  collage.style.paddingBottom = space + "px";

  var cells = 0;
  tiles.forEach(function (t) {
    cells +=
      t.classList.contains("wide") || t.classList.contains("tall") ? 2 : 1;
  });
  cells = Math.ceil(cells * 1.15);

  var w = window.innerWidth;
  var h = window.innerHeight - space * 2; // height left for the photos
  var cols = Math.max(2, Math.round(Math.sqrt((cells * w) / h)));
  var rows = Math.ceil(cells / cols);
  var cell = Math.min(w / cols, h / rows);

  collage.style.setProperty("--cols", cols);
  collage.style.setProperty("--cell", cell + "px");
}

fitCollage();
window.addEventListener("resize", fitCollage);
