# Compliance Notes: Workbook Drawing & PDF Export Fix

**Project:** BIO 304 Human Anatomy & Physiology (American River College, online), Interactive Workbooks
**Files covered:** 42 `workbook_dayNN_*.html` pages in `drsrennie-stack/nonmajors` that contain the draw-and-upload tool
**Date:** June 25, 2026
**Reviewer:** Dr. Sharilyn Rennie

## What changed

Three defects were repaired. No content, colors, fonts, headings, or saved-work storage keys were altered.

1. **Pen was misaligned (ink landed about an inch from the cursor).** The drawing `<canvas>` carried the page layout `pad` class, which adds horizontal inner padding. The pointer-to-bitmap math did not account for that padding, so strokes were offset. Fix: `canvas.pad{padding:0}` so the cursor and the ink line up exactly.
2. **Drawings were cut off in the exported PDF.** The drawing box could be split at a page break. Fix: `break-inside:avoid` (and `page-break-inside:avoid`) on `.canvas-wrap`, so the whole box moves to the next page instead of being clipped. The live canvas prints its own bitmap directly, so the drawing always appears.
3. **Uploaded hand-drawing photos disappeared in the exported PDF.** The uploaded `<img>` sat inside a container marked `no-print`, so it was removed when printing. Fix: `no-print` was moved onto the file-input `<label>` only, so the upload control stays out of the PDF while the uploaded image prints.

4. **Large PNG uploads silently failed to save (JPEG worked, PNG did not).** PNG files (often screenshots) are much larger than JPEGs and exceeded the browser per-page storage limit (~5MB), so they displayed once but were lost on reload/export. Fix: every upload is now decoded, downscaled to a 1600px max dimension, flattened on a white background, and re-encoded to JPEG (quality 0.85) before display and save. This keeps any phone photo small enough to persist. Files the browser cannot decode (for example iPhone HEIC) now show a clear message asking for a JPG or PNG instead of a blank box. Backward compatible: uploads already saved on a student device still load unchanged.

## WCAG 2.2 conformance (scope: the change itself)

Target level: AA minimum, AAA where already present. The fix is additive and preserves every existing accessibility feature on these pages (semantic landmarks, heading hierarchy, `for`/`id` label pairing, `aria-live` save status, visible focus indicators, skip link, `prefers-reduced-motion`).

- **1.1.1 Non-text Content (A):** No non-text content was added. The uploaded image retains its descriptive `alt`. Pass.
- **1.4.1 Use of Color (A):** No color used to convey meaning was added or removed. Pass.
- **1.4.3 / 1.4.6 Contrast:** No text or color values changed; the existing palette is untouched. No regression.
- **1.3.1 Info and Relationships (A):** The file input stays associated with its label; the uploaded image remains a labeled sibling. Pass.
- **2.5.x Pointer:** Correcting the pen offset improves pointer accuracy for drawing input. Improvement.

## Color contrast audit

No text or background colors were introduced or modified. The page palette (navy #0B1530, rust #8B3A2E, gold #C9A14A on white/cream) is unchanged, so prior contrast results stand. No new pair to audit.

## Keyboard navigation

Unchanged. No interactive elements were added or removed. Tab order, Save as PDF, color-swatch buttons, Clear buttons, and file inputs operate as before.

## Screen reader testing

No new announced content. Label and live-region relationships were not disturbed; the `aria-live="polite"` save indicator still fires on input.

## Verification performed

- Static checks across all 42 output files: zero remaining `uploader no-print`; pen-alignment rule present; break-inside print rules present; the canvas is NOT hidden in print; canvas ids, `data-key` attributes, and `TOPIC` storage strings byte-for-byte unchanged.
- Confirmed the earlier print-time canvas-to-image swap (which blanked drawings because the image had not decoded before printing) is fully removed.

## Known limitations and remediation plan

- The new upload path was verified by simulation (a 4000x3000 image downscales to 1600x1200 JPEG, displays, and saves; an undecodable file shows the guidance message) and the full page script passed a JavaScript syntax check in both file variants.
- A full in-browser print-to-PDF render could not be run in this environment (headless browser download blocked by network policy). Recommend one manual smoke test before pushing: open one fixed page, draw in a box, upload a photo in the other box, Save as PDF, and confirm the pen tracks the cursor, the drawing appears and is not clipped, and the uploaded photo appears.
- `day32_pregnancy-a-p-basics.html` has no drawing tool and was left unchanged (the parallel `day32_pregnancy-aandp-basics.html` carries the tool and was fixed).

## Student work safety

The fix does not read or write any saved-answer storage. `TOPIC`, every `data-key`, and the canvas ids are unchanged, so answers and drawings already saved in a student's browser load back normally after the new pages are published.

Dr. Sharilyn Rennie
