# BIO 304 — Phase B push (lecture page wiring)

This folder contains **167 modified lecture HTML files**. Each one was edited to load `slide-modal.js` and (where the topic matched a slide deck) drop a "Drawing tools" button row right under the page's `<h1>`.

Phase A (slides) is already live, so this push activates the integration.

## What got wired

- **109 lectures** got concept-anchored drawing buttons. Example: `tubular-function.html` now has a "Draw the nephron tubular function" button under its title; clicking opens `slides-tubular-function.html` in a centered floating panel without leaving the page.
- **58 lectures** got just the `<script src="slide-modal.js" defer></script>` include with no buttons. These are pages where no slide topic matched cleanly (e.g., portfolio templates, weekly checklists, course orientation, the comprehensive practice final). You can add `data-slide` buttons by hand to any of them later — the modal is already loaded.
- **77 admin pages skipped** entirely (syllabus, accessibility, AI policy, indexes, slide files themselves).

## Push commands

```bash
cd /path/to/nonmajors
git checkout main
git pull origin main

# Copy all modified lecture HTML files
cp "/Users/sharilynrennie/Documents/Claude/Projects/Lecture Slides/_PUSH-TO-GITHUB/BIO-304-PhaseB/"*.html .

# Sanity check: confirm nothing unexpected staged
git status

# Commit + push
git add *.html
git commit -m "Phase B: wire slide-modal into lecture pages with concept-anchored drawing buttons"
git push origin main
```

## What to verify after the push

GitHub Pages takes 1-3 minutes. Then test ONE wired lecture:

**Open:** https://drsrennie-stack.github.io/nonmajors/tubular-function.html

**Look for:**

1. A bordered box right under the H1 title labeled "Drawing tools" with a navy button: **"✎ Draw the nephron tubular function"**
2. Click the button → a centered white floating panel opens with the tubular function slide deck inside. The rest of the lecture page stays visible behind a barely-tinted layer.
3. Close the panel: click the X in the top right, or hit Escape, or click outside the panel. Focus returns to the button you clicked.
4. Click **"Open in new tab"** in the panel's top bar → slide deck opens in a separate browser tab.

**Test a multi-deck page:**

Some lectures match more than one slide deck. Example:
https://drsrennie-stack.github.io/nonmajors/workbook_day08_skin-functions-and-accessory-structures.html

Should show two buttons in the row: one for skin functions, one possibly for skin structure. Both should work independently.

## What's NOT in Phase B

- BIO 004 — that's a separate repo with its own Phase A + B. Hold off on BIO 004 until you've confirmed Phase B works on BIO 304.

## Full report

`wire-report.json` in this folder lists every lecture file, what slides matched (or didn't), and the H1 text used for matching. Useful if you want to spot-check or add buttons manually to no-match pages.

## If something's wrong

- **Button shows but click does nothing**: check browser console (Cmd+Option+I → Console tab). Most likely cause is the slide HTML 404ing because the path is wrong. The buttons use `data-slide="slides-tubular-function.html"` (relative path) so it expects the slide files at the same directory level as the lecture page. Phase A put them at repo root, so this should work.
- **Modal opens but iframe is empty**: same issue — path or 404. Check Network tab.
- **Modal opens behind Kajabi/Canvas nav**: not relevant since these are GitHub Pages, but if you embed in Kajabi later, add `.slide-modal-shell { z-index: 10001 !important; }` to the page.

Tell me when this is pushed and confirmed, and I'll prep BIO 004 Phase A.
