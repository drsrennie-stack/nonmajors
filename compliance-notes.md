# Accessibility Compliance Notes

**Project:** BIO 304 Student Reference Notes
**Files covered:** module-01-foundations.html, module-02-tissues-integument.html, chemistry-for-ap-reference.html, index.html (course home, Notes pills + reference link)
**Date:** 2026-06-09
**Reviewer:** Dr. Sharilyn Rennie

---

## 1. Project name and scope

BIO 304 Human Anatomy & Physiology (online, no TBL). Module 1 of 16, Week 1. Student-facing "look-it-up" reference notes for non-majors, with plain-language ("explain like you're 10") boxes for the harder concepts. Four topics: Levels of Organization; Anatomical Terminology and Body Regions; Homeostasis and Feedback Loops (including two filled feedback grid charts); Cell Anatomy and Physiology (membrane transport, tonicity and RBCs, exocytosis and endocytosis). Built as a reusable single-file template for Modules 2 to 16.

## 2. Brand and palette

MCAS palette per Project Update 2026-05-29, dark-only variant per instruction (navy #0B1530 removed entirely; only the dark #060A18 is used):

- Dark #060A18 (primary text, dark callout/footer panels)
- Rust #8B3A2E (eyebrows, accents, labels, links)
- Gold #C9A14A (accents and labels on dark backgrounds only)
- Cream #F5F1E8 (table headers, highlight and self-check panels, text on dark)
- White #FFFFFF (page and card background)

Font: Plus Jakarta Sans Variable (single family). No bookend borders or decorative left-bars anywhere (verified: zero `border-left` rules); section and box differentiation comes from background and a uniform 1px card border only, consistent with the MCAS course-home brand.

## 3. WCAG version and target level

Target WCAG 2.2. AA met across all criteria; AAA met for contrast on all body text, headings, table content, and dark-panel text.

## 4. Color contrast audit

| Text / element | Foreground | Background | Ratio | Result |
|---|---|---|---|---|
| Body text | Dark #060A18 | White #FFFFFF | 19.73:1 | AAA |
| Text on cream panels | Dark #060A18 | Cream #F5F1E8 | 17.5:1 | AAA |
| Eyebrows, labels, links | Rust #8B3A2E | White #FFFFFF | 7.66:1 | AAA |
| Rust labels on cream | Rust #8B3A2E | Cream #F5F1E8 | 6.79:1 | AAA (large) / AA (normal) |
| Clinical + footer labels | Gold #C9A14A | Dark #060A18 | 8.16:1 | AAA |
| Clinical body text | Cream #F5F1E8 | Dark #060A18 | 17.5:1 | AAA |
| Emphasis on dark | White #FFFFFF | Dark #060A18 | 19.73:1 | AAA |

Gold is never used as text on a white background (would be 2.42:1). Gold appears only as: a label/heading color on dark panels (8.16:1), dark text placed on a gold fill in the SVG diagram (high contrast), and decorative box borders where a background-color change already distinguishes the box.

## 5. Keyboard navigation and focus

Tab order: skip link to `#main`, TOC links (4), in-content links, then each topic's self-check `summary` (Enter/Space toggles). No keyboard traps. Focus indicator is a 3px rust outline (gold inside dark clinical panels) with offset, visible at every stop.

## 6. Screen reader testing

Structurally verified (recommend a live VoiceOver/NVDA pass before publishing):

- Landmarks reach banner, navigation, main, contentinfo.
- One h1, h2 per topic, h3 per subsection; no skipped levels.
- All tables are real data tables with `scope` on column and row headers. This includes the two new feedback grid charts, where the loop components are row headers (vertical axis) and the regulated variables are column headers (horizontal axis).
- SVG diagrams expose `title` + `desc` via `aria-labelledby`.
- `details` self-checks announce expanded/collapsed; all default to open.

## 7. Content design notes

- Plain-language boxes ("Explain it simply, like you're 10") added for the four hardest concepts: emergence, negative feedback, diffusion and gradients, osmosis and tonicity. Non-major-level prose carries the rest.
- Two filled feedback grid charts: Chart 1 (negative feedback) across body temperature, blood glucose, and blood pressure; Chart 2 (positive feedback) across childbirth, blood clotting, and milk let-down. Components run down the side; regulated variables run across the top.
- Emergent property is stated explicitly with a worked cardiac example plus a second table of two emergence examples.

## 8. Print rendering

`@media print`: each topic starts on its own page, cards avoid internal breaks, all self-check prompts force-expand, dark and cream panels keep their fills via `print-color-adjust:exact`. Produces a clean textbook-style handout from the browser Print command.

## 9. House rules verified

- No em dashes (0 in file).
- Byline "Dr. Sharilyn Rennie" with no credential suffix; no ", ND" / ", MD".
- Dark-only palette; navy #0B1530 fully removed (0 occurrences); no sage.
- No bookend borders (0 `border-left` rules).
- iframe height-sender (postMessage with id, ResizeObserver, load/resize listeners, plus a toggle listener for the disclosure widgets) baked in before `</body>`, message shape matched to the MCAS course-home page (`type:"resize"`).
- All internal/same-page links carry `target="_top"`. No external links present.

## 10. Known limitations and remediation plan

1. Live screen-reader pass not yet performed this session. Remediation: run VoiceOver and NVDA before assigning.
2. Cell Anatomy and Physiology (Topic 4) and both feedback grid charts were authored from standard non-majors A&P content, since the uploaded teaching guide covered Topics 1 to 3 only. Remediation: reconcile against your own cards/notes when available.
3. Web fonts load from a CDN (@fontsource Plus Jakarta Sans, matching the brand file). If the embed environment blocks external fonts, system sans-serif fallback applies without breaking layout.

## 11. Addendum (2026-06-09): content additions and second file

**module-01-foundations.html, added after audit:**

- Topic 1: anatomy vs. physiology opener (structure-determines-function rule, gross vs. microscopic); characteristics of life table (organization, metabolism, responsiveness, movement, growth, reproduction); survival needs table (oxygen, nutrients, water, normal temperature, atmospheric pressure).
- Topic 2: serous membranes (parietal vs. visceral, pleura/pericardium/peritoneum, plus inflammation terms); compact medical imaging table (X-ray, CT, MRI, ultrasound, PET).
- Topic 4: organelle table expanded (cytoskeleton, rough vs. smooth ER split, peroxisomes, cilia and microvilli).

All additions use the same MCAS dark-only palette, real table markup with `scope`, and carry no bookend borders.

**chemistry-for-ap-reference.html (new):** standalone, ungraded look-it-up chemistry companion. Eight sections (atoms/ions/electrolytes, bonds, water/solvent, solutions and concentration, gradients, pH and buffers, biomolecules and ATP, reactions and enzymes), each ending in a "Where you'll meet this in A&P" dark callout. Includes one sequence diagram (gradient to signal). Same template, palette, fonts, print rules, skip link, focus model, and height-sender as the module file. Verified: 0 em dashes, 0 navy #0B1530, 0 bookend borders, byline correct, all internal links `target="_top"`, contrast identical to the audited module values (dark on white 19.73:1; rust on white 7.66:1; gold and cream on dark 8.16:1 and 17.5:1). Reference values (electrolyte ranges, blood pH 7.35 to 7.45, plasma osmolarity ~285 to 295 mOsm/L, fasting glucose 70 to 99 mg/dL, resting membrane potential ~-70 mV) are standard clinical figures.

## 12. Addendum (2026-06-09): Week 2 module and print buttons

**module-02-tissues-integument.html (new):** Week 2 / Module 2, six topics (four tissue types and epithelium; connective tissue; muscle and nervous tissue; tissue membranes and repair; skin layers; skin color and accessory structures). Covers the high-yield core plus medium/light-yield topics (glands and secretion modes, cell junctions, tissue membranes, tissue repair, the -plasia/-trophy adaptation terms). Includes a classification mind-map (tissue family tree) and a two-step epithelium naming key (algorithm), plain-language boxes, clinical callouts, and open self-checks. Same MCAS dark-only palette, fonts, accessibility model, and height-sender. The tissue tree uses a thin left connector line, this is a functional hierarchy indicator for the mind-map, not a decorative bookend bar. Verified: 0 em dashes, 0 navy #0B1530, correct byline, internal links target="_top".

**Print buttons + book-style print (all three note files):** a visible "Print" button (rust pill, real `<button>` calling `window.print()`, accessible name, hidden in print output) added to module 1, module 2, and the chemistry reference. Print CSS rewritten so output reads like a book: each topic starts a fresh page; tables, figures, callouts, list items, and self-checks use `break-inside:avoid` so they are not split awkwardly; table headers repeat across pages (`thead{display:table-header-group}`); headings stay with following content (`break-after:avoid`); orphan/widow control on paragraphs; card boxes drop their borders in print so long topics flow as continuous text instead of clipping. Students reach the chemistry reference from the course-home Reference shelf; week notes are reached via the per-week Notes pill (Weeks 1 and 2 wired).

## 13. Reviewer

Dr. Sharilyn Rennie
