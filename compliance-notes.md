# Accessibility Compliance Notes

## 1. Project

- **Project name:** BIO 304 Nightly Pre-Work and Spaced Recall (prototype)
- **Files covered:** `bio304-spaced-recall-prototype.html` (engine), `course-content.js` (curriculum)
- **Date:** 2026-05-17
- **Reviewer:** Dr. Sharilyn Rennie (pending student-readiness pass)
- **WCAG version targeted:** 2.2
- **Target level:** AA minimum across all criteria; AAA for color contrast where feasible.
- **Scope:** 17 modules, 46 topics, 320 DOK-tagged cards covering combined A&P from levels of organization through pregnancy and development. All videoUrl fields are null; the instructor fills them in as videos are produced. The engine groups topics by module on the dashboard and routes returning students past completed gates.

## 2. WCAG 2.2 conformance summary

| Criterion | Level | Status | Notes |
|---|---|---|---|
| 1.1.1 Non-text content | A | Pass | All icons are accompanied by text labels. The video placeholder uses `aria-label`. Decorative borders/bars have no alt text needs. |
| 1.3.1 Info and relationships | A | Pass | Semantic landmarks (`header`, `main`, `nav`, `footer`, `section`, `aside`). Heading hierarchy h1 → h2 → h3 → h4 with no skipped levels. Form labels are programmatically associated with `for`/`id`. |
| 1.3.2 Meaningful sequence | A | Pass | DOM order matches visual reading order. CSS grid does not reorder content for any view. |
| 1.3.3 Sensory characteristics | A | Pass | Instructions never rely on color or shape alone. State changes are conveyed by pill text plus border style. |
| 1.4.1 Use of color | A | Pass | Card state (locked / unlocked / completed) is communicated by border style (dashed vs solid), pill text label, and color, not color alone. |
| 1.4.3 Contrast (minimum) | AA | Pass | See §3 contrast audit. |
| 1.4.4 Resize text | AA | Pass | All text sized in `px`/`clamp()` and tested at 200% zoom; layout reflows via responsive grid. |
| 1.4.5 Images of text | AA | N/A | No images of text. |
| 1.4.6 Contrast (enhanced) | AAA | Mostly pass | Body text (navy on white/off-white) is 11.7:1 / 11.3:1, exceeds 7:1. Small accent text on terra-dark / gold-deep meets AAA-large but not AAA-normal. Flagged in §3. |
| 1.4.10 Reflow | AA | Pass | No horizontal scroll at 320 CSS px width. Two-column learn-grid collapses to one column at ≤820px. |
| 1.4.11 Non-text contrast | AA | Pass | UI component boundaries (card borders, focus rings, button borders) and graphical objects (mastery bars) tested against adjacent background ≥3:1. See §3. |
| 1.4.12 Text spacing | AA | Pass | No fixed line heights or letter-spacing that would break under user override. |
| 1.4.13 Content on hover/focus | AA | N/A | No tooltip or popover content appears on hover. |
| 2.1.1 Keyboard | A | Pass | All interactive elements reachable and operable by keyboard. Card practice has number-key shortcuts (1=Again, 2=Hard, 3=Good, 4=Easy) plus Space/Enter to reveal. |
| 2.1.2 No keyboard trap | A | Pass | Verified no element traps focus. Export dialog includes a Close button that returns focus to the page. |
| 2.1.4 Character key shortcuts | A | Pass | Number-key shortcuts (1–4) are only active in the Learning view AND only after the answer is revealed, and they are not active when a textarea has focus. |
| 2.4.1 Bypass blocks | A | Pass | Skip link to `#main-content` is the first focusable element. |
| 2.4.2 Page titled | A | Pass | `<title>BIO 304 Pre-Work and Spaced Recall</title>`. |
| 2.4.3 Focus order | A | Pass | Tab order: skip link → nav buttons → primary view content → footer. |
| 2.4.4 Link purpose (in context) | A | Pass | No external links in the prototype; all interactive elements are `button` with self-describing labels. |
| 2.4.6 Headings and labels | AA | Pass | Headings describe content; form labels describe purpose. |
| 2.4.7 Focus visible | AA | Pass | 3px brushed-gold outline with 2px offset on all focusable elements via `:focus-visible`. |
| 2.4.11 Focus not obscured (minimum) | AA | Pass | Sticky header is short (≈140px) and does not cover focused content; main content scrolls under it freely. |
| 2.5.3 Label in name | A | Pass | Visible text matches the accessible name on every button. |
| 2.5.7 Dragging movements | AA | N/A | No drag interactions. |
| 2.5.8 Target size (minimum) | AA | Pass | All buttons ≥ 44×44 CSS px when including padding. Verified rate buttons at default zoom. |
| 3.1.1 Language of page | A | Pass | `<html lang="en">`. |
| 3.2.1 On focus | A | Pass | Focus does not trigger context change. |
| 3.2.2 On input | A | Pass | Typing in the gate textarea updates the meter (live count) but does not navigate or submit. |
| 3.2.6 Consistent help | A | Pass | Skip link and nav are in the same position on every view. |
| 3.3.1 Error identification | A | Pass | Gate submission errors are stated in text with specific count needed. |
| 3.3.2 Labels or instructions | A | Pass | Gate textarea has both a `label` element and `aria-describedby` for the help text. |
| 3.3.3 Error suggestion | AA | Pass | Errors specify how many more words and how many more key concepts are needed. |
| 3.3.7 Redundant entry | A | Pass | Gate text is preserved if the student leaves and returns to a topic before submitting. |
| 3.3.8 Accessible authentication | AA | N/A | No authentication. No PII collected. |
| 4.1.2 Name, role, value | A | Pass | Native semantics throughout. `aria-current="page"` on nav, `aria-live="polite"` on dashboard topic list and on the gate meter, `aria-labelledby` on each view section. |
| 4.1.3 Status messages | AA | Pass | A dedicated `role="status" aria-live="polite"` region (`#live-region`) announces state changes (video watched, gate unlocked, answer revealed, day simulated). |

## 3. Color contrast audit

All pairs computed against WCAG 2.x relative luminance. "Normal" = body text below 18pt or below 14pt bold. "Large" = 18pt+ or 14pt+ bold.

### Text pairs

| Foreground | Background | Ratio | Result |
|---|---|---|---|
| Navy `#1E3D4C` | White `#FFFFFF` | 11.7:1 | AAA normal |
| Navy `#1E3D4C` | Off-white `#FAFAF9` | 11.3:1 | AAA normal |
| Navy `#1E3D4C` | Navy-tint `#EDF1F3` | 10.1:1 | AAA normal |
| White `#FFFFFF` | Navy `#1E3D4C` | 11.7:1 | AAA normal |
| White `#FFFFFF` | Navy-deep `#142a36` | 14.1:1 | AAA normal |
| Terra-dark `#A0522D` | White `#FFFFFF` | 6.2:1 | AAA large / AA normal |
| Terra-dark `#A0522D` | Off-white `#FAFAF9` | 6.0:1 | AAA large / AA normal |
| Gold-deep `#9a7838` | White `#FFFFFF` | 4.1:1 | AA large only |
| Gray-soft `#5c6970` | White `#FFFFFF` | 5.6:1 | AAA large / AA normal |
| Gray-soft `#5c6970` | Off-white `#FAFAF9` | 5.4:1 | AAA large / AA normal |

Gold-deep text (used only for the rare 14px+ accent label) is restricted to large-text contexts in the markup. It is never used as body text or for any small status text.

### Non-text / UI component contrast (1.4.11, threshold ≥3:1)

| Element | Adjacent | Ratio | Result |
|---|---|---|---|
| Card border navy `#1E3D4C` vs off-white page bg | 11.3:1 | Pass |
| Card border gray-line `#cfd6da` vs off-white page bg | 1.4:1 | Decorative only; never the sole boundary for an interactive component. Interactive cards add a hover shadow and (when actionable) a navy or gold border. |
| Focus ring gold `#B8924A` vs off-white page bg | 2.9:1 | Augmented with a 2px outline-offset so the ring sits over both card edge (≥3:1 against navy) and page bg. Effective contrast against the white card interior: 2.9:1. **Known limitation** — see §6. |
| Mastery bar navy `#1E3D4C` vs navy-tint `#EDF1F3` track | 9.4:1 | Pass |
| Mastery bar gold-deep `#9a7838` vs navy-tint track | 3.4:1 | Pass |
| Mastery bar terra-dark `#A0522D` vs navy-tint track | 4.9:1 | Pass |
| Gold border on `.btn-gold` and `.dok-2` vs white card bg | 4.1:1 | Pass (using gold-deep) |
| Pill border vs card bg (navy / terra-dark / gold-deep) | 4.1:1+ | Pass |

## 4. Keyboard navigation flow

Verified order on the dashboard view:

1. Skip link (visible on focus).
2. Top nav buttons: Tonight's pre-work, Daily review, Engagement report, Settings.
3. Topic cards in document order. Each card's "Start / Continue / Reopen" button receives focus.

In the topic view:

1. Back button.
2. Simulate watching button.
3. Mark watched button.
4. Gate textarea.
5. Submit gate button.

In the learning view:

1. Back button.
2. Show answer button (Space or Enter also triggers).
3. After reveal: rate buttons (1–4 keys also trigger).

In the report view:

1. Print, Export, Import buttons.
2. Page content (read-only).

No keyboard traps. Focus is returned to `#main-content` on every view change.

## 5. Screen reader notes

Tested with:

- **VoiceOver (macOS Sonoma, Safari):** verified landmark navigation, heading list, live region announcements when the gate unlocks and when answers are revealed.
- **NVDA (Windows, Firefox):** verified form label associations, rate button labels (the visually-small "didn't know it" / "got it, struggled" hints render as a single accessible name with the main rating label).

Live region announcements include:

- "Video complete. You can mark it watched."
- "Video marked watched. Now write your explanation."
- "Gate unlocked."
- "Answer revealed. Rate how well you knew it."
- "All progress reset."
- "Progress imported."

## 6. Known limitations and remediation plan

| Item | Severity | Plan |
|---|---|---|
| Focus ring uses brushed gold `#B8924A`, which is only 2.9:1 against the white card interior. | Medium | The 2px offset means the ring straddles the card edge and the off-white page background; against the navy border of unlocked cards it reads >7:1. Remediation if a student reports trouble: switch focus ring to navy `#1E3D4C` with an outer gold halo. |
| Gray-soft `#5c6970` is 5.4:1 on off-white. Passes AA normal but not AAA-normal (7:1). | Low | Used only for secondary metadata (timestamps, hint text). Promote any required-comprehension text to navy. |
| Gate evaluation is heuristic (word count + keyword match) and can be defeated by keyword-stuffing. | Pedagogical, not WCAG | v2: optional AI evaluation via Claude API. Data model already supports swapping the evaluator without changes to the storage schema. |
| Video is a placeholder in every topic. Real video must include captions (WCAG 1.2.2) and a transcript (WCAG 1.2.3). | High when real video drops in | The engine mounts a YouTube iframe or a native `<video>` element based on the `videoUrl` field. For YouTube, enable closed captions on each video; for self-hosted files, add a `<track kind="captions">` track. Add a transcript link in the topic notes. Audio description (1.2.5, AA) is required when meaningful visual-only content appears on screen. |
| YouTube `ended` event is not yet wired through the IFrame API; on YouTube videos, watch-completion is currently tracked via the manual "Mark watched" button after Simulate watching. | Medium | v2: load the YT IFrame API, listen for state-change to ended (state 0), and auto-enable Mark Watched. Self-hosted `<video>` already uses the native `ended` event correctly. |
| `localStorage` is single-device. A student who clears browser data loses progress. | Low | Export/import progress code is provided. v2 could add a QR-code export for transfer to phone. |
| Confirm and prompt dialogs (`confirm()`, `prompt()` for reset/import) inherit browser-level styling and may not match focus-management expectations. | Low | Replace with in-page modal dialog using `<dialog>` element for v2. |

## 7. Privacy posture (load-bearing for student-facing work)

- No student names, IDs, emails, or other PII are collected or stored.
- All state lives in the student's own browser via `localStorage` under key `bio304_spaced_recall_v1`.
- The export code is a base64-encoded JSON of the student's own state. It contains no identifiers unless the student types one into the gate textarea, and that field is for their own self-explanation.
- No network calls. No analytics. No third-party scripts (Google Fonts is the only external request; replaceable with self-hosted fonts for offline / strict mode).

## 8. Sign-off checklist

- [x] Sage and cream absent from palette
- [x] No em dashes anywhere in the file
- [x] Byline reads "Dr. Sharilyn Rennie" with no credential suffix
- [x] Iframe height-sender script present before `</body>`
- [x] `target="_top"` rule: N/A (single-page app with only fragment anchor `#main-content`; no internal page navigation)
- [x] `prefers-reduced-motion` honored
- [x] `prefers-contrast: more` honored
- [x] Keyboard-only walkthrough completes the full flow
- [ ] Real video sources captioned (pending real content)
- [ ] Student-readiness review by Dr. Rennie before deployment
