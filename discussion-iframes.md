# BIO 304 — Discussion iframe embeds

Served from GitHub Pages: `https://drsrennie-stack.github.io/nonmajors/`

## 1. Parent height listener (paste ONCE per page that holds any of these)

```html
<!-- ============================================================
     PARENT HEIGHT LISTENER  —  paste ONCE per Canvas/Kajabi page
     (handles BOTH message types the BIO 304 pages may send)
     ============================================================ -->
<script>
(function () {
  window.addEventListener('message', function (e) {
    if (!e.data || !e.data.id || !e.data.height) return;
    if (e.data.type !== 'resize' && e.data.type !== 'iframe-height') return;
    var f = document.getElementById(e.data.id);
    if (f) f.style.height = e.data.height + 'px';
  }, false);
})();
</script>
```

## 2. One iframe per discussion (paste where you want each prompt to appear)

### Welcome Discussion

```html
<iframe
  id="bio304-welcome-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/welcome_discussion.html"
  title="BIO 304 — Welcome Discussion"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:900px;"
  scrolling="no"
></iframe>
```

### Week 1 Discussion — Homeostasis

```html
<iframe
  id="bio304-week01-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week01_discussion.html"
  title="BIO 304 — Week 1 Discussion — Homeostasis"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1100px;"
  scrolling="no"
></iframe>
```

### Week 2 Discussion — Tissues & skin (with skin-cancer risk self-check)

```html
<iframe
  id="bio304-week02-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week02_discussion.html"
  title="BIO 304 — Week 2 Discussion — Tissues & skin (with skin-cancer risk self-check)"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1700px;"
  scrolling="no"
></iframe>
```

### Week 3 Discussion — Skeletal / fracture

```html
<iframe
  id="bio304-week03-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week03_discussion.html"
  title="BIO 304 — Week 3 Discussion — Skeletal / fracture"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1100px;"
  scrolling="no"
></iframe>
```

### Week 4 Discussion — Nervous system

```html
<iframe
  id="bio304-week04-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week04_discussion.html"
  title="BIO 304 — Week 4 Discussion — Nervous system"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1100px;"
  scrolling="no"
></iframe>
```

### Week 5 Discussion — Endocrine (EWG Skin Deep, two products)

```html
<iframe
  id="bio304-week05-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week05_discussion.html"
  title="BIO 304 — Week 5 Discussion — Endocrine (EWG Skin Deep, two products)"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1200px;"
  scrolling="no"
></iframe>
```

### Week 6 Discussion — Cardiovascular (BP/MAP, Karvonen, ASCVD)

```html
<iframe
  id="bio304-week06-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week06_discussion.html"
  title="BIO 304 — Week 6 Discussion — Cardiovascular (BP/MAP, Karvonen, ASCVD)"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1800px;"
  scrolling="no"
></iframe>
```

### Week 7 Discussion — Respiratory/immune barriers (STOP-BANG, ACT)

```html
<iframe
  id="bio304-week07-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week07_discussion.html"
  title="BIO 304 — Week 7 Discussion — Respiratory/immune barriers (STOP-BANG, ACT)"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1700px;"
  scrolling="no"
></iframe>
```

### Week 8 Discussion — Renal/repro (Cockcroft-Gault, water needs)

```html
<iframe
  id="bio304-week08-discussion"
  src="https://drsrennie-stack.github.io/nonmajors/week08_discussion.html"
  title="BIO 304 — Week 8 Discussion — Renal/repro (Cockcroft-Gault, water needs)"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1700px;"
  scrolling="no"
></iframe>
```
