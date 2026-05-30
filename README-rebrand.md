# BIO 304 MCAS Rebrand — How to run it

This folder holds the BIO 304 (`drsrennie-stack/nonmajors`) rebrand kit. Five files:

- **`canvas-home.html`** — Canvas course home page. One big "Enter the course" button that lands students on the hub. Use this as the Canvas Front Page.
- **`index.html`** — the new 8-week BIO 304 hub (course home). Coordinated with the syllabus: weekly rhythm, hard deadlines, four-component grading, eight week cards anchored as `#week-1` through `#week-8` so spoke pages can deep-link back. Drop in at the root of the repo.
- **`rebrand-mcas.py`** — bulk script (v2) that walks every other `.html` file in the repo and applies MCAS branding without touching JavaScript. Video gating and spaced recall keep working by design. Adds an anchored back-link to the correct week on the hub. Rebrands the syllabus and schedule automatically via CSS-variable remap.
- **`iframes.md`** — Canvas embed snippets (parent-side listener + per-page iframes)
- **`compliance-notes.md`** — WCAG 2.2 audit, contrast ratios, sign-off log per the global rule

## Run it

```bash
# 1. Clone the repo locally (or pull the latest if you already have it)
git clone https://github.com/drsrennie-stack/nonmajors.git
cd nonmajors

# 2. Drop the new hub + the Canvas front door in
cp /path/to/this/folder/index.html ./index.html
cp /path/to/this/folder/canvas-home.html ./canvas-home.html

# 3. Dry run the bulk script to preview what changes
python3 /path/to/this/folder/rebrand-mcas.py . --dry-run

# 4. Run for real
python3 /path/to/this/folder/rebrand-mcas.py .

# 5. Spot-check a few pages locally (open in browser), then commit
git add -A
git commit -m "MCAS rebrand v2: Canvas front door + 8-week hub + anchored back-links"
git push
```

## What the script does (and doesn't do)

**Does:**

- Adds the Plus Jakarta Sans `@import` at the top of every page's `<style>` block
- Appends an MCAS override CSS block at the END of every page's `<style>` (it wins the cascade via `!important` on color and font properties only)
- **Remaps legacy CSS variables.** If a page uses `--navy`, `--gold`, `--terra`, `--sage-dark`, `--off-white`, etc. (which the syllabus and schedule do), the script redefines those tokens to MCAS values at the end of the cascade. The syllabus and schedule rebrand themselves automatically with no hand edits.
- Replaces any teal / sage hex codes with Navy / Cream / Gold
- Wraps the page's existing body content with MCAS site header + footer (the original content goes inside `<main id="mcas-content" class="mcas-content">`)
- **Anchored back-link.** The header carries a "← Course home (Week N)" link that points to `index.html#week-N` for spoke pages (e.g. `cell-structure.html` → `index.html#week-1`, `cardiac-conduction.html` → `index.html#week-6`). Course-wide pages (syllabus, accessibility, AI honor contract, etc.) get a plain "Course home" link to `index.html`.
- Adds `target="_top"` to every internal / same-domain link
- Adds `target="_blank" rel="noopener"` to every external link
- Bakes in the iframe height-sender script just before `</body>` with a unique `FRAME_ID` per page
- Stamps each rebranded page with `<!-- MCAS_REBRAND_APPLIED v2 -->` for idempotency

**Doesn't:**

- Touch any `<script>` tag contents
- Touch any `id`, `class`, or `dataset` attribute that JavaScript references
- Modify the existing DOM structure inside the body (only wraps it)
- Modify `course-content.js` (your spaced recall question bank)
- Modify the module PDFs
- Touch `index.html` or `canvas-home.html` (both are hand-built; in the script's skip list)
- Touch anything prefixed `_TRASH_`, `_archive`, `_apply_`, or `_build_`

**Note on `_OBSOLETE_` files:** despite the prefix, these are active in BIO 304 — they carry the week-1 discussion, overview, and trainer pages. The script rebrands them along with everything else, and routes their back-links to the correct week (e.g. `_OBSOLETE_biol304_week1_discussion.html` → `index.html#week-1`).

## Flags

```
--dry-run        Show what would change, write nothing
--force          Re-apply even if the marker is present
--only FILE      Process only one specific filename
--skip-target    Don't rewrite target attributes (useful if you've already done it)
```

## After the run

1. Open `index.html` in a browser and confirm the hub looks right
2. Open `bio304-spaced-recall-prototype.html` and confirm the cards still answer, schedule, and persist (i.e. spaced recall logic is intact)
3. Open `concept_videos.html` and confirm later videos still unlock after earlier ones (i.e. gating still works)
4. Run the parent-side listener snippet in your Kajabi page (see `iframes.md` section 1)
5. Embed an iframe per page using the templates in `iframes.md`
6. Update `compliance-notes.md` with the date of your sampled audit and your sign-off

## If something looks off

- **A page's text is too small or invisible after rebrand.** The override only forces font-family and color. If the original page hardcoded `color` with high specificity (e.g. an inline `style="color:#ddd"`), the override may not win. Inspect the element, find the offending rule, and fix it in the source page. Or run with `--force` after editing the override block in the script.
- **A button stopped working.** That would mean a `<script>` reference was disturbed, which the script is designed not to do. Open an issue and quote the page; this is a script bug, not a config issue.
- **Iframe height keeps growing or shrinking.** That's a known browser oddity when an inner element has `position: fixed` or a `transform`. Open the page directly, find the element, and confirm it sits in flow.
