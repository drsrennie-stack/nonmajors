# Compliance Notes: Workbook Drawing Tool + PDF Export

**Project:** BIO 304 Human Anatomy & Physiology (American River College, online), Interactive Workbooks
**Files covered:** 42 workbook_dayNN_*.html pages in drsrennie-stack/nonmajors that contain the draw-and-upload tool
**Date:** June 25, 2026
**Reviewer:** Dr. Sharilyn Rennie

## What changed

A set of bug fixes plus a full upgrade of the in-page drawing tool. No page content, palette, fonts, headings, or saved-work storage keys were altered. Student answers and drawings already saved on a device continue to load.

Bug fixes:

1. Pen was misaligned (ink offset from the cursor). The pointer now maps from the canvas's actual rendered box, and the canvas is forced to zero padding and border, so the pen tracks the cursor exactly.
2. Drawings were clipped in the exported PDF. The drawing box now uses break-inside avoidance so it is never split across a page, and the canvas prints its own content.
3. Uploaded photos disappeared in the PDF. The no-print flag was moved onto the file-input label only, so the uploaded image prints while the picker does not.
4. Large PNG uploads silently failed to save, and one photo rendered as a solid black box. Uploads now always display the browser-decoded original (never black), and a shrunk JPEG copy is saved only after a black-frame guard confirms it is valid, otherwise the original is kept. Files the browser cannot decode (for example iPhone HEIC) show a clear message asking for a JPG or PNG.

Drawing tool upgrade:

5. New toolbar on each box: six pen colors (navy, rust, gold, green, purple, grey), three pen sizes (S/M/L), Pen, Eraser, Line, Arrow, Box, Circle, Text, and Move tools, plus Undo, Redo, Delete, and Clear.
6. Shapes are editable objects. With Move, click to select (dashed outline and corner handles), drag to reposition, and drag a handle to resize. A box can be reshaped into a rectangle and a circle into an oval; lines and arrows have endpoint handles.
7a. Each uploaded photo has a Remove photo button (appears once a photo is present) that clears just that image and its saved copy, without affecting drawings or answers.
7. Text tool places a typed label on the diagram (entered through a prompt, so it is keyboard friendly). Labels can be moved and deleted.
8. Snap-to-align guides appear while dragging a shape, snapping its edges and center to other shapes and to the canvas center, with a light guide line.
9. Undo and Redo cover draws, shapes, moves, resizes, text, and deletes (up to 30 steps). Eraser removes freehand ink; shapes are removed with Delete or the keyboard Delete or Backspace key.

## WCAG 2.2 conformance (scope: the change)

Target level AA minimum, AAA where already present. The upgrade preserves existing accessibility features (semantic landmarks, heading hierarchy, label and input pairing, aria-live save status, visible focus indicators, skip link, reduced-motion support).

- 1.1.1 Non-text Content (A): the uploaded image keeps descriptive alt text. Pass.
- 1.4.1 Use of Color (A): pen color is a free student choice, not a carrier of required meaning. Pass.
- 1.4.3 / 1.4.6 Contrast: no page text or background colors changed. No regression.
- 1.3.1 Info and Relationships (A): file input stays associated with its label. Pass.
- 2.1.1 Keyboard (A): all toolbar controls are native buttons, focusable and operable by keyboard; selected shapes can be removed with Delete or Backspace; text labels are entered by typing. Freehand and shape drawing are inherent pointer gestures; the upload-a-photo path remains the non-pointer alternative for producing a diagram.
- 4.1.2 Name, Role, Value (A): tool buttons use aria-pressed to expose active state; groups use role group with an accessible name. Pass.

## Color contrast audit

No page text or background colors were introduced or modified. The palette (navy #0B1530, rust #8B3A2E, gold #C9A14A on white and cream) is unchanged, so prior results stand. The new pen inks (green #2E7D32, purple #6A1B9A, grey #555555) are student drawing colors on a white canvas, not interface text.

## Keyboard navigation

All toolbar buttons are reachable and operable by keyboard and expose pressed state. Delete and Backspace remove a selected shape (ignored while typing in a text field). Drawing gestures are pointer based by nature; the photo upload remains the keyboard-accessible way to submit a diagram.

## Screen reader testing

Tool buttons announce their label and pressed state. Selection outlines and snap guides are visual only and are cleared before printing. Live-region save status still fires on input. No redundant or decorative elements are announced.

## Verification performed

- All 42 generated files pass a JavaScript syntax check.
- Engine simulated headlessly: pen mapping is 1:1 with no offset; box resizes from square to rectangle with the opposite corner anchored; line endpoints move independently; text places, moves, and persists; Undo and Redo round-trip; snap aligns a box's edges and center exactly to a neighbor and clears guides on release.
- Storage invariants confirmed unchanged across both page templates: TOPIC string, every data-key form field, the upload inputs, and canvas ids.

## Known limitations and remediation plan

- A full in-browser print-to-PDF render could not be run in this environment (headless browser download is blocked by network policy). Recommended smoke test before publishing: on one page, draw with the pen and confirm it tracks the cursor, add and move a few shapes, type a text label, upload a PNG and confirm it appears (not black) and persists after reload, then Save as PDF and confirm the drawing is complete and uncut and the photo appears.
- Drawing and shape gestures are pointer based; the photo-upload alternative covers non-pointer users.
- day32_pregnancy-a-p-basics.html has no drawing tool and was left unchanged (the parallel day32_pregnancy-aandp-basics.html carries the tool and was upgraded).

## Student work safety

The upgrade does not rename any storage key. Drawings are saved under the same draw-<id> key (now a JSON payload with a back-compat path that still loads older bitmap saves), uploads under up-<id>, and answers under their existing keys. Republishing to the same URL does not erase work already saved in a student's browser.

Dr. Sharilyn Rennie
