# BIO 304 — Phase A push (slides only)

This folder contains **slide-modal.js + 63 slide HTML files**. NO lecture-page edits yet. Goal: confirm the slides render correctly in production before wiring lecture pages in Phase B.

## What's in this bundle

- `slide-modal.js` — the iframe-popup script (added but not yet used by any lecture page)
- 54 master-library slide decks (palette-corrected, print PDF buttons, working toolbar)
- 9 BIO 16 life-skills overlay decks (cross-applicable: lipid panel, A1C, blood pressure, skin cancer ABCDE that overlap with BIO 304's clinical literacy)

## What this push does to the existing repo

**Overwrites** 58 existing `slides-*.html` files with the new versions (corrects the cream palette to off-white, fixes the toolbar bug, adds print-PDF buttons).

**Adds** 5 net-new files:
- slides-heart-risk-calculator.html
- slides-medication-labels.html
- slides-mental-health-basics.html
- slides-vaccines-literacy.html
- slides-when-to-call-911.html

**Adds** slide-modal.js.

**Leaves alone** two old GI files in your repo that have been replaced in the master library:
- `slides-digestion-absorption.html` (replaced by `slides-gi-alimentary-canal.html` + `slides-gi-accessory-structures.html`)
- `slides-gi-anatomy-motility.html` (same replacement)

You can delete those two later if you want (they're not referenced anywhere new). They won't hurt anything if you leave them.

## Push commands

Open a terminal. Replace `/path/to/nonmajors` with wherever you have the repo cloned locally.

```bash
# 1. Navigate to your local clone of the repo
cd /path/to/nonmajors

# 2. Make sure your local main is up to date
git checkout main
git pull origin main

# 3. Copy everything from this bundle into the repo root
cp "/Users/sharilynrennie/Documents/Claude/Projects/Lecture Slides/_PUSH-TO-GITHUB/BIO-304-PhaseA/"slide-modal.js .
cp "/Users/sharilynrennie/Documents/Claude/Projects/Lecture Slides/_PUSH-TO-GITHUB/BIO-304-PhaseA/"slides-*.html .

# 4. Optional: delete the two obsolete GI files
git rm slides-digestion-absorption.html slides-gi-anatomy-motility.html

# 5. Stage, commit, push
git add slide-modal.js slides-*.html
git commit -m "Phase A: refreshed slide decks (off-white palette, print PDF, toolbar fix) + life-skills overlay decks"
git push origin main
```

## What to verify after the push

GitHub Pages takes 1-3 minutes to redeploy. Then open these URLs and check:

1. **A migrated slide deck** (palette + print PDF working):
   https://drsrennie-stack.github.io/nonmajors/slides-tubular-function.html
   - White cards on off-white background (no cream)
   - Pen + color + size + eraser + undo + image + save toolbar visible on every drawable slide
   - Hero buttons: "Download all drawings" + "Clear all canvases" + **"Download blank PDF pack"** (new)
   - On each slide header, hover to see **"Print this slide"** button (new)

2. **A net-new life-skills deck**:
   https://drsrennie-stack.github.io/nonmajors/slides-blood-pressure.html
   - Should look identical in style to the tubular function deck
   - 6 slides, 4 with drawing canvases

3. **The modal script loads without error**:
   https://drsrennie-stack.github.io/nonmajors/slide-modal.js
   - Should show the JS source. If it 404s, GitHub Pages hasn't deployed yet.

4. **Print PDF works**:
   - On any drawable slide, click "Download blank PDF pack" — should open print dialog showing one slide per page with framed drawing boxes (NOT canvases)
   - Click "Print this slide" on any single slide — should show just that one slide in the print preview

## If something's wrong

- **Toolbar missing**: hard refresh (Cmd+Shift+R). If still missing, message me with the URL.
- **Cream still appearing**: hard refresh. Browser cached the old version.
- **404 on slide-modal.js**: wait 5 minutes for GitHub Pages to redeploy.
- **Print PDF shows the live canvas instead of blank box**: that's a print stylesheet issue, message me.

## What's NOT in Phase A

- No lecture-page edits. Your existing lecture HTMLs are untouched.
- No `data-slide` buttons inside lectures yet.
- The modal script is loaded into the repo but no page triggers it yet.

That's Phase B — once you confirm Phase A renders correctly, I'll generate the lecture-page edits.
