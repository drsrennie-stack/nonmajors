# BIO 304 iframe embed snippets

Canvas-ready embeds for the rebranded `drsrennie-stack/nonmajors` repo, served from GitHub Pages at `https://drsrennie-stack.github.io/nonmajors/`.

**Two entry points:**

1. **`canvas-home.html`** — the Canvas course home page. One big "Enter the course" button that lands students on the hub. Drop this as the Canvas Front Page.
2. **`index.html`** — the hub. Eight-week grid, all study tools, all policy links. Every spoke page links back here at the right week anchor (`#week-1` through `#week-8`).

## 1. Parent-side height listener (paste ONCE per Kajabi page)

This goes in any Kajabi page that holds one or more BIO 304 iframes. It listens for the `postMessage` resize calls that every rebranded page sends, and sets the matching iframe's height.

```html
<script>
(function(){
  window.addEventListener('message', function (e) {
    if (!e.data || e.data.type !== 'resize' || !e.data.id) return;
    var f = document.getElementById(e.data.id);
    if (f) f.style.height = e.data.height + 'px';
  }, false);
})();
</script>
```

You only need this snippet once per Kajabi page, even if the page holds multiple iframes.

## 2. Standard iframe template

Every BIO 304 page uses the same wrapper. Drop one of these per embed.

```html
<iframe
  id="bio304-{SLUG}"
  src="https://drsrennie-stack.github.io/nonmajors/{FILENAME}.html"
  title="BIO 304 — {HUMAN TITLE}"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:600px;"
  scrolling="no"
></iframe>
```

`{SLUG}` is the filename without extension, lowercased, hyphens for spaces. The rebrand script (`rebrand-mcas.py`) bakes the matching `FRAME_ID = "bio304-{slug}"` into every page so the height-sender lines up automatically.

## 3. Keystone pages (ready to paste)

### Canvas front door (course home page)

```html
<iframe
  id="bio304-canvas-home"
  src="https://drsrennie-stack.github.io/nonmajors/canvas-home.html"
  title="BIO 304 — Welcome"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:760px;"
  scrolling="no"
></iframe>
```

### Course home (the hub)

```html
<iframe
  id="bio304-index"
  src="https://drsrennie-stack.github.io/nonmajors/index.html"
  title="BIO 304 — Course Home"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1200px;"
  scrolling="no"
></iframe>
```

### Syllabus

```html
<iframe
  id="bio304-biol304-syllabus"
  src="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html"
  title="BIO 304 — Syllabus"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:800px;"
  scrolling="no"
></iframe>
```

### Course orientation

```html
<iframe
  id="bio304-course-orientation"
  src="https://drsrennie-stack.github.io/nonmajors/course-orientation.html"
  title="BIO 304 — Course Orientation"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:800px;"
  scrolling="no"
></iframe>
```

### Concept videos (gated)

```html
<iframe
  id="bio304-concept-videos"
  src="https://drsrennie-stack.github.io/nonmajors/concept_videos.html"
  title="BIO 304 — Concept Videos"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:800px;"
  scrolling="no"
></iframe>
```

### Spaced recall

```html
<iframe
  id="bio304-bio304-spaced-recall-prototype"
  src="https://drsrennie-stack.github.io/nonmajors/bio304-spaced-recall-prototype.html"
  title="BIO 304 — Spaced Recall"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:700px;"
  scrolling="no"
></iframe>
```

### Comprehensive practice final

```html
<iframe
  id="bio304-comprehensive-practice-final"
  src="https://drsrennie-stack.github.io/nonmajors/comprehensive-practice-final.html"
  title="BIO 304 — Comprehensive Practice Final"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:800px;"
  scrolling="no"
></iframe>
```

### How to reach me

```html
<iframe
  id="bio304-biol304-how-to-reach-me"
  src="https://drsrennie-stack.github.io/nonmajors/biol304_how_to_reach_me.html"
  title="BIO 304 — How to Reach Me"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:500px;"
  scrolling="no"
></iframe>
```

### Accessibility statement

```html
<iframe
  id="bio304-biol304-accessibility"
  src="https://drsrennie-stack.github.io/nonmajors/biol304_accessibility.html"
  title="BIO 304 — Accessibility Statement"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:500px;"
  scrolling="no"
></iframe>
```

### Reading map

```html
<iframe
  id="bio304-biol304-reading-map"
  src="https://drsrennie-stack.github.io/nonmajors/biol304_reading_map.html"
  title="BIO 304 — Reading Map"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:600px;"
  scrolling="no"
></iframe>
```

### AI policy (the explainer)

```html
<iframe
  id="bio304-ai-policy"
  src="https://drsrennie-stack.github.io/nonmajors/ai_policy.html"
  title="BIO 304 — AI Policy"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1200px;"
  scrolling="no"
></iframe>
```

### AI Honor Contract (the signed agreement)

```html
<iframe
  id="bio304-ai-honor-contract"
  src="https://drsrennie-stack.github.io/nonmajors/ai_honor_contract.html"
  title="BIO 304 — AI Honor Contract"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:1400px;"
  scrolling="no"
></iframe>
```

## 4. Module concept pages (one snippet per topic)

Every concept page follows the same pattern. Generate the snippet by substituting `{FILENAME}` and `{HUMAN TITLE}`.

```html
<iframe
  id="bio304-{slug-of-FILENAME}"
  src="https://drsrennie-stack.github.io/nonmajors/{FILENAME}.html"
  title="BIO 304 — {HUMAN TITLE}"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:600px;"
  scrolling="no"
></iframe>
```

Pages confirmed in the repo (use file basename as slug, lowercased, hyphens):

- `action-potentials-synapses.html` — Action potentials and synapses
- `adaptive-immunity.html` — Adaptive immunity
- `anatomical-position.html` — Anatomical position
- `appendicular-skeleton.html` — Appendicular skeleton
- `axial-skeleton.html` — Axial skeleton
- `blood-composition.html` — Blood composition
- `blood-vessels-hemodynamics.html` — Blood vessels and hemodynamics
- `body-cavities.html` — Body cavities
- `body-regions.html` — Body regions
- `bone-tissue.html` — Bone tissue
- `cardiac-conduction.html` — Cardiac conduction
- `cell-structure.html` — Cell structure
- `cns-organization.html` — CNS organization
- `connective-tissues.html` — Connective tissues
- `cross-bridge-cycle.html` — Cross-bridge cycle
- `digestion-absorption.html` — Digestion and absorption
- `epithelial-tissue.html` — Epithelial tissue
- `female-reproductive.html` — Female reproductive system
- `fluid-electrolyte-acid-base.html` — Fluid, electrolyte, acid-base balance
- `gas-exchange-transport.html` — Gas exchange and transport
- `gi-anatomy-motility.html` — GI anatomy and motility
- `hearing-equilibrium.html` — Hearing and equilibrium
- `heart-anatomy.html` — Heart anatomy
- `hemostasis-blood-typing.html` — Hemostasis and blood typing

(Repository has ~140 content pages total. Generate snippets in bulk with the script in section 6 below.)

## 5. Module PDFs (sixteen modules)

Module PDFs are linked directly from the hub `index.html` and don't need an iframe wrapper — they open in a new tab via the hub. If you want to embed them in Kajabi anyway, use a standard PDF embed:

```html
<iframe
  src="https://drsrennie-stack.github.io/nonmajors/BIO-304-Module-01-foundations-of-anatomy-and-physiology.pdf"
  title="BIO 304 — Module 1 Guide"
  style="width:100%; height:900px; border:0; display:block;"
></iframe>
```

Substitute the module number and slug as needed.

## 6. Generate snippets in bulk

If you want one HTML file containing every iframe (e.g. for a one-page directory in Kajabi), run this Python one-liner from your local repo clone after rebranding:

```python
import os, re, sys
BASE = "https://drsrennie-stack.github.io/nonmajors/"
print('<script>window.addEventListener("message",function(e){if(!e.data||e.data.type!=="resize"||!e.data.id)return;var f=document.getElementById(e.data.id);if(f)f.style.height=e.data.height+"px";},false);</script>')
for f in sorted(os.listdir(".")):
    if not f.endswith(".html"): continue
    if f.startswith(("_OBSOLETE_","_TRASH_","_archive","_apply_","_build_")): continue
    slug = re.sub(r"[^a-z0-9]+","-", os.path.splitext(f)[0].lower()).strip("-")
    title = os.path.splitext(f)[0].replace("_"," ").replace("-"," ").title()
    print(f'<iframe id="bio304-{slug}" src="{BASE}{f}" title="BIO 304 — {title}" loading="lazy" style="width:100%;border:0;display:block;min-height:600px;" scrolling="no"></iframe>')
```

## 7. Notes on the iframe behavior

The rebrand script bakes a `postMessage({type:'resize', id:FRAME_ID, height:h})` call on every rebranded page. It fires on `load`, on `resize`, and whenever the body's size changes (via `ResizeObserver`). That means:

- The iframe grows and shrinks to match its content automatically
- No inner scrollbars (`scrolling="no"`)
- No fixed height needed (the `min-height` is just a fallback while the iframe is loading)
- Multiple iframes on one page each match their own height, because every frame's `id` is unique

If a page's height ever sticks (rare), reload the Canvas page once and the listener will recompute.

## 8. Anchored back-links from spoke pages

Every rebranded spoke page carries a "← Course home (Week N)" link at the top, where N is the week that page belongs to (mapped from the syllabus). When the student clicks it, they land at the exact week card on the hub, not at the top of the page.

The mapping in `rebrand-mcas.py`:

- Topic pages (e.g. `cell-structure.html`, `cardiac-conduction.html`, `female-reproductive.html`) → mapped explicitly to their syllabus week
- `workbook_dayNN_*.html` → week = `ceil(NN / 4)` (days 1-4 = week 1, days 5-8 = week 2, etc., through day 32)
- `weekNN_*.html` (e.g. `week04_discussion.html`) → week = NN
- `_OBSOLETE_*weekN*.html` → week = N (the `_OBSOLETE_` prefix is misleading; these are live)
- Course-wide pages (syllabus, accessibility, integrity, AI honor contract, etc.) → plain `index.html` (no anchor)
- Unknown filename → plain `index.html`
