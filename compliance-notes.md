# Accessibility Compliance Notes

## 1. Project

- Project: BIO 304 Anatomy & Physiology, course revamp (branding pass)
- Files covered: `index.html` (new course-home page)
- Repo: drsrennie-stack/nonmajors
- Date: May 25, 2026
- Design system: Course Site Design System (`course-design-system.md`)

## 2. WCAG version and target level

WCAG 2.2. Target level AA minimum, AAA where achievable. Status by criterion:

| Criterion | Level achieved | Notes |
|-----------|---------------|-------|
| 1.1.1 Non-text content | AA | Instructor photo has descriptive alt text; logo SVG is `aria-hidden` with an accessible name on its parent link; arrow glyphs are `aria-hidden`. |
| 1.3.1 Info and relationships | AA | Semantic `header`, `main`, `section`, `footer`; every `section` has `aria-labelledby`; headings nest h1 to h4 with no skipped levels. |
| 1.4.3 Contrast (minimum) | AAA on body text | See audit in section 3. |
| 1.4.10 Reflow | AA | Single-column responsive layout; grids collapse with `auto-fill` / `auto-fit`. |
| 1.4.11 Non-text contrast | AA, one watch-item | Focus rings exceed 3:1; white-card border is below 3:1 (see section 6). |
| 1.4.12 Text spacing | AA | Relative units and generous line-height; no fixed-height text containers. |
| 2.1.1 Keyboard | AA | All interactive elements are native links; fully operable by keyboard. |
| 2.4.1 Bypass blocks | AA | Skip link to `#main` is the first focusable element. |
| 2.4.7 Focus visible | AAA | 3px focus ring, 3px offset, rust on light bands and gold on dark bands. |
| 2.4.6 Headings and labels | AA | One h1; descriptive section headings. |
| 2.5.8 Target size (minimum) | AA | Cards and buttons exceed the 24px minimum. |
| 2.3.3 Animation from interactions | AAA | `prefers-reduced-motion` disables all transitions and smooth scroll. |
| 3.1.1 Language of page | AA | `<html lang="en">`. |
| 4.1.2 Name, role, value | AA | Icon-only and logo links have accessible names; native elements throughout. |

## 3. Color contrast audit

All text pairs in `index.html`, measured against the design system tokens.

| Text | Background | Ratio | Level | Where used |
|------|-----------|-------|-------|------------|
| Navy `#0B1530` | White `#FFFFFF` | 18:1 | AAA | h1, h2 (light), week and card titles |
| Navy `#0B1530` at 82% | White `#FFFFFF` | ~13:1 | AAA | card and hero body text |
| Rust `#8B3A2E` | White `#FFFFFF` | 7.7:1 | AAA | eyebrows, accent words, module labels, CTA text link |
| White `#FFFFFF` | Rust `#8B3A2E` | 7.7:1 | AAA | primary button label |
| Cream `#F5F1E8` | Near-black `#060A18` | 17.5:1 | AAA | dark-band headings, body, footer text |
| Gold `#C9A14A` | Near-black `#060A18` | 8.2:1 | AAA | dark-band eyebrows, footer headers, instructor quote |
| Gold `#C9A14A` | Card-navy `#1C2E4F` | 5.6:1 | AA | study-sheet card labels (Mode 01, etc.) |
| Cream `#F5F1E8` | Card-navy `#1C2E4F` | ~13:1 | AAA | study-sheet card titles and body |
| Terra cotta `#C2734D` | Near-black `#060A18` | 5.5:1 | AA | accent words inside dark-band h2 (large text) |

No failing text pair. Rust is never placed as text on a dark background, per the design system watch-out.

## 4. Keyboard navigation flow

Verified tab order: skip link, header logo, hero "Open the syllabus" button, hero "See the course map" link, the 44 course-map cards in reading order, the 4 "Start here" cards, then the footer links. Every interactive element is reachable, operable with Enter, and shows a visible focus ring. The skip link jumps focus to `#main`. No keyboard traps. No positive `tabindex` values.

## 5. Screen reader testing

Code-level and structural verification completed: landmark regions (`header`, `main`, `section`, `footer`), `aria-labelledby` on every section, heading hierarchy h1 to h4 with no skips, alt text on the instructor image, accessible names on the icon-bearing logo links, and decorative SVG and glyphs marked `aria-hidden`.

A live pass with VoiceOver (Safari) and NVDA (Firefox) has not yet been run in this environment. Recommended before the page goes live. See section 6.

## 6. Known limitations and remediation plan

1. Live screen reader pass not yet performed. Remediation: run VoiceOver and NVDA on the published page and confirm landmark and heading announcement before launch.
2. White-card border `#8C90A0` on white measures about 2.6:1, below the 3:1 non-text contrast minimum (WCAG 1.4.11). The cards stay identifiable by their drop shadow, title text, and hover state, so this is not a functional barrier. Remediation if strict 1.4.11 is required: darken the border token to roughly `#6B6F80`.
3. The instructor photo loads from `raw.githubusercontent.com` (the STAT repo). If that repo is made private the image will break; the alt text covers the content either way.
4. The 44 one-pager study sheets and the support pages (syllabus, schedule, orientation) are not yet rebranded to this design system. Planned as phase 2.
5. The optional "current week" marker from the BIO 004 sample was omitted because BIO 304 term start dates were not provided. Can be added later.

## 7. Reviewer

Built and self-reviewed by Claude (Cowork) on May 25, 2026. Final review and sign-off: Dr. Sharilyn Rennie.
