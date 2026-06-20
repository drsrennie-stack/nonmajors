# Compliance Notes — BIO 304 MCAS Rebrand

**Project:** BIO 304 Human Anatomy &amp; Physiology, American River College (online, summer 2026, 8 weeks, June 8 to August 2)
**Repo:** drsrennie-stack/nonmajors
**Files covered:** `canvas-home.html` (hand-crafted Canvas front door), `index.html` (hand-crafted 8-week hub coordinated with syllabus), `rebrand-mcas.py` v2 (bulk rebrand for the remaining ~160 pages including syllabus, schedule, and `_OBSOLETE_*`).
**Branding applied:** MCAS per Project Update 2026-05-29 — Plus Jakarta Sans · Navy #0B1530 · Rust #8B3A2E · Gold #C9A14A · Cream #F5F1E8 · Dark #060A18
**Date:** 2026-05-30
**Reviewer:** Dr. Sharilyn Rennie (pending sign-off)

## 1. WCAG target

- **Floor:** WCAG 2.2 Level AA across every rebranded page
- **Target:** Level AAA where achievable

## 2. Color contrast audit

Ratios computed against the WCAG 2.2 formula. AA-normal requires 4.5:1, AA-large requires 3.0:1, AAA-normal requires 7.0:1.

| Foreground / background | Ratio | AA normal | AA large | AAA normal |
|---|---|---|---|---|
| Navy #0B1530 on White #FFFFFF | 18.04:1 | pass | pass | pass |
| Navy #0B1530 on Cream #F5F1E8 | 16.00:1 | pass | pass | pass |
| Cream #F5F1E8 on Dark #060A18 | 17.50:1 | pass | pass | pass |
| Cream #F5F1E8 on Navy #0B1530 | 16.00:1 | pass | pass | pass |
| Rust #8B3A2E on White | 7.66:1 | pass | pass | pass |
| Rust #8B3A2E on Cream | 6.79:1 | pass | pass | fail (AAA) |
| Rust hover #A0452F on White | 6.20:1 | pass | pass | fail (AAA) |
| White #FFFFFF on Rust button #8B3A2E | 7.66:1 | pass | pass | pass |
| Gold #C9A14A on Dark | 8.16:1 | pass | pass | pass |
| Gold #C9A14A on Navy | 7.46:1 | pass | pass | pass |
| Gold #C9A14A on Cream | 2.15:1 | **fail** | **fail** | **fail** |
| Gold #C9A14A on White | 2.42:1 | **fail** | **fail** | **fail** |
| Navy 0.72-opacity on White (#4D556E) | 7.39:1 | pass | pass | pass |
| Navy 0.80-opacity on White (#393F58) | 10.37:1 | pass | pass | pass |
| Cream 0.88-opacity on Dark (#D7D3CB) | 13.22:1 | pass | pass | pass |

**Use rules baked into the design system:**

- **Gold #C9A14A is decorative on dark backgrounds only.** It is used as a small accent (eyebrow text, footer headers, the closing CTA accent) where the background is Navy or Dark. It is never used as text on White or Cream.
- **Rust #8B3A2E is the light-section accent.** It is used for CTAs, hover states, and accents on White or Cream backgrounds. Achieves AA on Cream and AAA on White.
- **Cream is for dark-section text only.** Cream is never used as a light background, only as the foreground color on Navy or Dark sections.
- **Sage is excluded** from the system entirely, per global rule.
- **Teal is banned** at the script level — `rebrand-mcas.py` substitutes any `#2F4F4F`, `#008080`, `#5F9EA0`, `teal`, and related teal-family hex codes for Navy on every page it processes.

## 3. Typography

- Font family: **Plus Jakarta Sans** (variable), loaded via `https://cdn.jsdelivr.net/npm/@fontsource-variable/plus-jakarta-sans/index.css`, with `system-ui, -apple-system, sans-serif` fallback chain
- Headings: weight 800, tight tracking (`letter-spacing: -0.015em` to `-0.025em`)
- Body: 16px / 1.65 line-height; section copy uses 14–15px / 1.6
- No CSS reductions below 12px anywhere in the hub
- All headings use semantic levels (h1 → h2 → h3 → h4); no skipped levels
- Italic Lora is **not** used in this course (per global rule, Lora italic is the Solano teaching family; ARC online uses Plus Jakarta throughout)

## 4. Keyboard navigation

Verified on the hub `index.html`:

- **Skip link** at top of body, hidden until focused, jumps to `#main`
- **Tab order** follows visual order (header logo → hero CTAs → "How to thrive" cards → module cards in order → tools cards → about → FAQ summaries → closing CTA → footer links)
- **Focus indicator** is a 3px Rust outline on light sections, Gold on dark sections, with 3px offset and 4px radius. Visible against every background in the system.
- **FAQ accordions** open and close with Enter or Space on the `<summary>` element. The plus / minus glyph is `aria-hidden="true"` so screen readers don't announce it.
- **No `:hover`-only affordances.** Every hover state is mirrored by `:focus-visible`.

## 5. Screen reader testing

Verified semantic landmarks and ARIA on the hub:

- `<header>` for the site header, `<main id="main">` for content, `<footer>` for the footer
- The site logo carries `aria-label="BIO 304 Human Anatomy and Physiology, course home"`
- The logo SVG is `role="img" aria-hidden="true" focusable="false"` (the link's `aria-label` carries the semantics)
- The current-week marker on module cards is excluded (this is BIO 304 online, no rolling weekly cohort)
- The FAQ uses the `<details>` / `<summary>` pattern (native disclosure semantics)
- Module cards use `<ul>` / `<li>` for list semantics, with each card as an `<a>` whose entire body is the link target
- Tools cards follow the same `<ul>` / `<li>` / `<a>` pattern
- No images on the hub are purely decorative without `alt=""`; the instructor photo carries a meaningful `alt`

Recommended verification before launch:
- VoiceOver (macOS) on Safari (the screen reader most ARC students use on iOS / Mac)
- NVDA on Firefox (the screen reader most ARC students use on Windows)
- Verify the iframe height-sender works inside Kajabi — the iframe should grow to match content with no scrollbar

## 6. Motion and reduced-motion

- All transitions (hover lifts, focus outline, FAQ toggle rotation) are guarded by `@media (prefers-reduced-motion: reduce) { * { transition: none !important; animation: none !important; } }`
- `scroll-behavior: smooth` on `<html>` is also disabled when reduced motion is requested
- No autoplaying audio or video on the hub
- No marquees, flashing, or content that updates faster than 5Hz

## 7. Iframe and embedding behavior

- Every rebranded page sends `postMessage({type:'resize', id:FRAME_ID, height:h}, '*')` to its parent on load, on resize, and whenever the body's size changes (`ResizeObserver`)
- The hub's `FRAME_ID` is `bio304-course-home`; every other page's `FRAME_ID` follows `bio304-{slug-of-filename}`
- The Kajabi page needs the one-time parent listener snippet documented in `iframes.md` section 1
- Every internal and same-domain link uses `target="_top"` so navigation breaks the iframe and lands on the full page (per global rule)
- External links use `target="_blank" rel="noopener"`

## 8. JavaScript behavior preservation

This is the most important load-bearing claim of the rebrand. `rebrand-mcas.py` is explicitly designed not to touch:

- Any `<script>` tag's contents
- Any `id` or `class` attribute on an element that JS references
- The DOM structure beneath any element that JS queries (the rebrand wraps the existing body in `<main id="mcas-content" class="mcas-content">` but does not move or rename any internal element)
- `localStorage` keys, `dataset` attributes, or any data store
- Existing event listeners or scheduling code

Concrete consequence: the **video gating** logic on `concept_videos.html` and the **spaced recall** scheduler on `bio304-spaced-recall-prototype.html` (plus `course-content.js` if it's referenced) continue to work without modification.

The script was tested against three synthetic pages mimicking each pattern (an inline-style page with localStorage-backed spaced recall logic, a video-gating page with `data-video` attributes and `classList.replace`, and a plain content page). All three rebranded cleanly with no JS modification — verified by grepping for the original event listeners, dataset references, and localStorage calls in the rebranded output.

## 9. Known limitations and remediation plan

- **Hub + front door + script verified; per-page sampling pending.** This pass was completed against `canvas-home.html`, `index.html`, and a synthetic test fixture run of `rebrand-mcas.py` v2 across topic-page, workbook, discussion, `_OBSOLETE_`, and syllabus patterns (all six fixtures rebranded cleanly, back-links resolved to the correct week anchors). Once the script has been run against the full repo, pick five random rebranded pages, confirm no inline color (e.g. an in-page `<span style="color:teal">`) slipped through, and re-run the contrast check on any page that uses heavy inline styling.
- **Gold-on-light is excluded by design.** If a future page wants gold on a light background (e.g. an icon on White), the design system flags it and either darkens the gold to AA, swaps to rust, or moves the element onto a dark surface. The rebrand script does not detect this automatically; a manual eye is needed.
- **Tests on the cross-bridge cycle and action-potential pages** likely use complex inline SVG with their own color choices. Sample at least one of those after rebrand and confirm legibility hasn't regressed.
- **Syllabus deadline cards.** The script remaps the syllabus's `--sage-dark` token to MCAS gold so the "quiz closes" deadline card renders gold-on-navy after rebrand. Gold-on-cream would fail contrast; gold-on-navy (deadlines are on a dark or navy band by default) passes AAA. Verify visually that no quiz card ends up on a light background after rebrand.
- **PDF module guides** are linked from the hub but were not audited for accessibility in this pass. Module PDFs are an existing deliverable; auditing them is a separate workstream.
- **ARC's institutional accessibility policy.** Confirm the hub copy is compatible with ARC's Section 508 / WCAG 2.2 institutional policy. The hub meets WCAG 2.2 AA. If ARC requires evidence of testing with assistive technology, run the screen-reader checks in section 5 and add a screenshot or transcript to this file.
- **Canvas front door.** `canvas-home.html` ships at AAA contrast on every text/background pair (Cream on Dark = 17.5:1; Gold on Dark = 8.16:1; White on Rust button = 7.66:1). Verify the button doesn't get covered by Canvas chrome when embedded as the Front Page.

## 11. Week 3 concept video pages (added 2026-06-20)

**Files added:** `bone-tissue-video.html` (live Loom), `axial-skeleton-video.html`, `appendicular-skeleton-video.html`, `joints-and-movements-video.html` (Loom IDs pending). **Prework wiring:** a "Concept video" pill added to each of the four day cards in `week03_prework.html`.

These follow the BIO 004 concept-video pattern (16:9 player plus a clickable chapter list that restarts the player at a timestamp), rebranded to MCAS for BIO 304.

- **Video pill contrast.** The new pill uses Navy #0B1530 text on a Gold #C9A14A surface = **7.46:1** (passes AA and AAA normal). This is gold-as-surface with dark text, not the excluded gold-as-text-on-light case. Hover surface Gold-deep #B08B3A keeps navy text well above 4.5:1.
- **Chapters are real `<button>` elements** inside a `<nav aria-label="Video chapters">`, fully keyboard operable, with a 3px Gold focus ring (`:focus-visible`) and `aria-current="true"` on the active chapter.
- **Empty-video state.** Pages with no Loom ID hide the `<iframe>` and show a Navy panel reading "This video will be posted here." No broken iframe, no console error. Cream #F5F1E8 on Navy = 16:1.
- **Player iframe** has a descriptive `title`; chapter glyphs/arrows are `aria-hidden`.
- **Iframe height-sender** present on all four, IDs `bio304-bone-tissue-video`, `bio304-axial-skeleton-video`, `bio304-appendicular-skeleton-video`, `bio304-joints-and-movements-video`.
- **Links:** crumb back to `week03_prework.html` uses `target="_top"`; Loom embeds are the only external resource and load in-frame by design.
- **Reduced motion** honored (chapter transition disabled under `prefers-reduced-motion`).
- **Pending:** add Loom IDs and real chapter timestamps for axial, appendicular, and joints before those three go live to students.

## 12. Week 3 path + gating removal (updated 2026-06-20)

**Prework hub day path.** Each day card on `week03_prework.html` now shows the learning path in order: **Notes** (navy, the topic note page) -> **Concept video** (gold, the chapter video page) -> **Recall** (rust, that topic's spaced-recall cards), followed by a secondary **Submit lab** ghost pill (navy outline) for the Canvas turn-in. Recall links: `bio304-spaced-recall-prototype.html#topic=t-bone-tissue`, `t-axial-skeleton`, `t-appendicular-skeleton`, `t-joints-movements`.

- Pill contrast: Notes = white on navy 18:1; Concept video = navy on gold 7.46:1; Recall = white on rust 7.66:1; Submit lab = navy on white 18:1 (rest), white on navy on hover. All pass AA, most AAA.

**Gating and video tracking removed** from the four Week 3 note pages (`bone-tissue.html`, `axial-skeleton.html`, `appendicular-skeleton.html`, `joints-and-movements.html`) per instructor decision ("causes more problems than it is worth"). A small appended script removes: the 4-step pre-work tracker, the retrieval-check gate (`#explain-gate`), all gate hints, and every `gate-locked`/`is-gated` lock, so spaced recall and the workbook open directly with no prerequisite. The inline "Watch the video" toggle is replaced by a direct link to the topic's concept video page; no video-completion tracking remains.

- No new contrast or keyboard concerns: the script only removes elements and unlocks existing links. Remaining interactive elements (mode toolbar, term reveals, recall/video links) keep their original focus styles.
- Note: the removal is an appended override (reliable and reversible). A full source-level strip of the dormant gating/tracker script blocks can be done later once the sandbox shell is available to test.

## 13. Full-course rollout (updated 2026-06-20)

The Week 3 pattern is now applied to all eight weeks. Every prework hub day card (42 total across weeks 1-8) carries the path Notes -> Concept video -> Recall, with a secondary Submit lab ghost pill. Verified by script: 42/42 day cards link Notes, Concept video, and Recall to the **same topic** (0 mismatches), and every target file exists (0 missing).

- **Video pages:** 42 total (4 hand-built for Week 3, 38 generated). Each is the chapter-player format, back-linked to its week hub, with an empty `LOOM_ID` showing the "coming soon" placeholder until the instructor pastes the Loom embed ID and chapter times. Bone tissue carries the live Loom (`d9edbbcea2ca4ac88778adbaedf1d37d`) and real chapters.
- **Gating/tracking removed** from all 42 note pages via the appended cleanup script; all 42 scripts pass `node --check`.
- **Per-pill contrast** unchanged from section 12 (all AA, most AAA).
- **Still outstanding:** instructor to add Loom IDs + chapter times to the 38 placeholder video pages as videos are recorded. Pre-existing footer links `concept_videos.html` and `course-orientation.html` (from the original rebrand) have no local file and will 404 unless present in the repo.

## 10. Sign-off

- **Author:** Dr. Sharilyn Rennie (hub + bulk-rebrand approach)
- **Built:** 2026-05-30
- **Last audit:** 2026-06-20 (Week 3 concept video pages + prework pills)
- **Status:** Hub ready. Bulk script ready for first run against the full repo. Awaiting first-run audit on ~5 sampled rebranded pages. Week 3 video pages built; three await Loom IDs.
