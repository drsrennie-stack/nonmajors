# Accessibility Compliance Notes

## 1. Project

Non-Majors Slides, BIO 304 Human Anatomy & Physiology (American River College, online).
Files covered:

- axial-skeleton-nonmajors.html
- appendicular-skeleton-nonmajors.html
- joints-nonmajors.html
- index.html (BIO 304 course home with weekly release gating)

Date: June 20, 2026.

Each deck is built on the provided bone-tissue template (branding, present mode, lightbox, iframe height-sender) and now also carries a lecture-video block with chapters at the top, then the concept slides. Practice-question slides were intentionally omitted per request.

Imagery in the decks is a mix of (a) OpenStax / CNX Anatomy & Physiology figures, licensed CC BY, referenced from Wikimedia Commons, and attributed in each caption, and (b) original on-brand inline SVG diagrams (concept maps and flowcharts for the physiology and step sequences). The OpenStax photos load from an online library and need an internet connection; the SVG diagrams work offline. A footer line on each deck states this. Slides with no clean figure fit are intentionally left without one (and without a caption), so nothing reads as unfinished.

## 2. WCAG version and target level

Target: WCAG 2.2 Level AA (floor), with AAA met where noted.

| Criterion | Level | Notes |
|-----------|-------|-------|
| 1.1.1 Non-text content | AA | Logo SVG has role="img" with a name. OpenStax photos carry descriptive alt text. Each diagram SVG has role="img" with a title and desc, and the same information is in the adjacent bullet list. |
| 1.3.1 Info and relationships | AA | Semantic landmarks (header, main, footer, nav), heading hierarchy, lists for content, a real button for each video chapter, label/input pairing on the "mark watched" checkboxes. |
| 1.4.3 Contrast (minimum) | AA | All text pairs meet or exceed 4.5:1 (small) / 3:1 (large). See Section 3. |
| 1.4.6 Contrast (enhanced) | AAA (most text) | Body and primary accent text exceed 7:1. A few muted helper labels meet AA. |
| 2.1.1 Keyboard | AA | Present mode, lightbox, video chapter jumps, checkboxes, reset, and all index links/cards are keyboard operable. No trap. |
| 2.4.1 Bypass blocks | AA | "Skip to slides" (decks) and "Skip to main content" (index). |
| 2.4.7 Focus visible | AA | Global focus-visible outline (brick, 3px offset). |
| 2.3.3 / reduced motion | AAA | Transitions and animations disabled under prefers-reduced-motion. |
| 4.1.2 Name, role, value | AA | Chapter buttons, checkboxes, present-bar and lightbox-close icon buttons, and the logo SVG all expose accessible names. |
| 4.1.3 Status messages | AA | The video progress text uses aria-live="polite" so a count change is announced. |

## 3. Color contrast audit

Background tokens: page #FAFAF9, card #FFFFFF, dark hero/divider #060A18.

| Text | Foreground | Background | Ratio | Result |
|------|-----------|-----------|-------|--------|
| Body copy, list items | #060A18 | #FAFAF9 | ~16.8:1 | Pass AAA |
| Accent (eyebrow, bullets, captions, chapter time) | #8B3A2E | #FAFAF9 / #FFFFFF | ~7.5:1 | Pass AAA |
| Headings / chapter labels | #0B1530 | #FFFFFF | ~15:1 | Pass AAA |
| Chapter hint, progress text muted | #5a6573 | #FFFFFF | ~5.8:1 | Pass AA |
| Divider hero body | #FFFFFF | #060A18 | ~17:1 | Pass AAA |
| Divider eyebrow (gold) | #DCB45C | #060A18 | ~10:1 | Pass AAA |
| Buttons / present bar | #FFFFFF | #060A18 / #8B3A2E | 7:1+ | Pass AAA / AA |

Muted helper labels (hint text, placeholder subtext) clear the AA floor; revisit if AAA is required throughout.

## 4. Keyboard navigation flow

Decks: Skip link, then header buttons (Back, Present, Print/Save PDF), then the video chapter buttons and "mark watched" checkboxes and Reset, then each slide's figures. Present mode: Enter via Present; arrows / PageUp / PageDown move slides; Escape exits. Lightbox: Enter via a figure; Escape or close button dismisses. Video block is hidden in present mode.

Index: Skip link, then header, hero CTAs, the eight week cards (open weeks expose their pre-work and discussion links; locked weeks expose no links, only a dated lock note), then tools and footer. No keyboard trap anywhere.

## 5. Screen reader testing

Structure verified against semantic markup: one h1 per page, h2 for section and slide titles, lists for content, nav landmarks for chapters (decks) and the week grid (index). Icon-only buttons have names. Progress count is in an aria-live region. Recommended manual pass with VoiceOver (Safari) or NVDA (Firefox) once a real video is embedded and final captions/alt text are confirmed.

## 6. Video block and student-privacy notes

The chapter "watched" checkboxes and progress bar store state only in the student's own browser via localStorage, wrapped in try/catch so a browser that blocks storage degrades gracefully. No accounts, no server, and no student names, IDs, or identifiers are stored or transmitted. This satisfies the project's session-only / no-PII rule. The video itself is a clearly-marked placeholder; paste the Loom embed (keep id="lecvid") and edit the example chapter rows and timestamps before publishing.

## 7. Weekly release gating (index.html)

Each week's links unlock at 8:00 PM Pacific the Sunday before its Monday start and stay open the rest of the term, so students keep access to everything released to date. Not-yet-open weeks show a dashed, dated lock card with no clickable links. This is front-end gating for student experience, not hard security; Canvas remains the real access control. To adjust the schedule, edit the starts array in the gating script.

## 8. Known limitations and remediation plan

- OpenStax photos load from Wikimedia Commons and need an internet connection; they are CC BY and attributed in each caption, with a footer note. For a fully offline file, download and self-host the images and repoint the src. Confirm each thumbnail loads before class.
- The schematic SVG diagrams are simplified teaching illustrations, not exhaustive atlas art; specific names are carried in the slide text.
- Each title slide now has a scannable QR code (inline SVG, generated locally, offline) that encodes the deck's hosted GitHub Pages URL (drsrennie-stack.github.io/A-P-lecture-core/...). The QR has an accessible name. If a deck's filename or hosted path changes, regenerate that QR. The PowerPoint-download link from the source template was not added; say the word and I will include one.

## 9. Reviewer

Drafted in Cowork for review and sign-off by Dr. Sharilyn Rennie.
