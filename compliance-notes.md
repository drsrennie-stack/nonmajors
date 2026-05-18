# Compliance Notes — BIO 304 One-Pager Prototype

**Project:** BIO 304 · Foundations of Anatomy & Physiology · Body Regions one-pager
**Files covered:** `body-regions.html`
**Date:** 2026-05-18
**Reviewer:** Dr. Sharilyn Rennie (pending sign-off)

## WCAG version and target

WCAG 2.2 AA floor across the file. AAA achieved on all primary body text. Eyebrow/subhead/label text in terra-dark `#A0522D` on white sits at AA but below AAA — flagged below for future redesign if AAA across the board becomes a hard target.

## Color contrast audit (all text/background pairs in use)

| Pair | Ratio | AA-normal | AA-large | AAA-normal |
|---|---|---|---|---|
| Body text — navy `#1E3D4C` on white `#FFFFFF` | 11.49:1 | PASS | PASS | PASS |
| Eyebrow / subhead / small labels — terra-dark `#A0522D` on white | 5.62:1 | PASS | PASS | FAIL |
| Tie-in body — navy on navy-tint `#EDF1F3` | 10.11:1 | PASS | PASS | PASS |
| Tie-in eyebrow — terra-dark on navy-tint | 4.94:1 | PASS | PASS | FAIL |
| Toolbar resting button — navy on white | 11.49:1 | PASS | PASS | PASS |
| Toolbar active / Print button — white on navy | 11.49:1 | PASS | PASS | PASS |
| Image-slot hint — terra-dark on off-white `#FAFAF9` | ≈5.4:1 | PASS | PASS | FAIL |

No gold-on-white or white-on-gold text remains in the file. Gold is reserved for non-text affordances (focus rings only).

## Keyboard navigation flow verified

Tab order, top to bottom: skip link → Print view toggle → Interactive toggle → Print/Save PDF button → (when in interactive mode) each per-term "Your landmark" input in reading order, anterior then posterior then lateral → Sketch & synthesis textarea. All controls are reachable, operable with Enter/Space, and show a 2px gold focus ring at 2px offset against any background.

## Screen reader testing

- Landmarks: `<main id="main">`, `<section aria-labelledby="...">` for each column, `<div role="toolbar" aria-label="Sheet mode">`, `<div role="note" aria-label="Clinical tie-in">`.
- Heading hierarchy: single `<h1>`, `<h2>` per major region, `<h3>` per sub-region. No skipped levels.
- Each term-input has a visible label plus an explicit `aria-label` carrying the term name (e.g., "Your landmark for Antecubital") so a screen-reader user gets the term context even when the visible label is the generic "Your landmark".
- Toolbar buttons use `aria-pressed` to expose the mode state.
- Skip link present and visible on focus.
- Not yet tested with a live screen reader (VoiceOver/NVDA). Recommend a one-pass verification before publishing the first real student-facing version.

## Known limitations and remediation plan

1. **AAA gap on small eyebrow / subhead text.** Terra-dark on white is 5.62:1, which clears AA but not AAA. Acceptable per the "target AAA where achievable" rule. To close the gap, swap eyebrow color to navy and rely on size/weight/letter-spacing for visual separation. Defer until you decide whether AAA across the board is required for BIO 304 online materials.
2. **Image plate pulls from GitHub raw URLs** in `drsrennie-stack/nonmajors` on `main`. Each `<img>` has a descriptive `alt` attribute naming every labeled region for screen-reader users, plus `loading="lazy"`. If the repo ever goes private, the images break — at that point, either copy them locally next to the HTML or move them behind a GitHub Pages URL on a public repo. Note the double extension on `anterior-bodyUE.jpg.jpeg` — if you rename it in the repo, update the `src` attribute to match.
3. **Live screen-reader sweep not run.** Mark this as a pre-publish step for the first real lesson.
4. **No reduced-motion variant needed yet** — the only animation is a 200ms ease on toolbar button hover, which is decorative and within tolerance, but if more motion is added, wrap in `@media (prefers-reduced-motion: reduce)`.

## Embed readiness (Kajabi / Canvas)

- Iframe height-sender baked in: posts `{ id: 'bio304-body-regions', type: 'resize', height }` to parent on load, resize, and ResizeObserver mutations.
- No internal links present yet in the prototype; when added, every same-domain link must carry `target="_top"`, every external link `target="_blank" rel="noopener"`.
- Print stylesheet hides the toolbar and renders a clean Letter-size sheet at 0.45in margins. Save-as-PDF from Chrome produces the student handout.
