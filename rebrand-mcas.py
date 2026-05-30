#!/usr/bin/env python3
"""
rebrand-mcas.py
================
Bulk MCAS rebrand for the BIO 304 nonmajors repo.

Run this from a local clone of drsrennie-stack/nonmajors. It walks every .html
file at the root (skipping _OBSOLETE_, _TRASH_, and _archive prefixes), and
applies the MCAS branding without touching any existing JavaScript, classes,
ids, or DOM that scripts reference. That is the safety guarantee: video
gating and spaced recall logic are not modified, only the visual layer
and the surrounding chrome.

What it does, per file:
  1. Skip if the file already carries the marker comment
     <!-- MCAS_REBRAND_APPLIED vX --> for the current version (idempotent)
  2. Inject the Plus Jakarta Sans @import at the top of the first <style>
     block (or create a <style> block if there is none)
  3. Append the MCAS override CSS at the END of the first <style> block so
     it wins the cascade (uses !important on color and font properties only)
  4. Wrap the existing <body> contents with the MCAS site header and
     footer (header goes first, footer goes just before any trailing scripts
     and before </body>). The existing content stays exactly where it was,
     inside <main class="mcas-content">, so internal JS selectors keep working
  5. Ensure target="_top" on every internal/same-domain href, and
     target="_blank" rel="noopener" on every external href
  6. Append the iframe height-sender script just before </body> if missing
  7. Add the marker comment at the top of <head>
  8. Convert any prior #2F4F4F / teal hex codes to MCAS navy as a sanity
     pass (no teal, per Shar's hard rule)

Run:
    python3 rebrand-mcas.py /path/to/local/nonmajors

Flags:
    --dry-run      Show what would change, write nothing
    --force        Re-apply even if the marker is present (bumps version)
    --only FILE    Only process the given filename (e.g. --only course.html)
    --skip-target  Don't rewrite target attributes
"""

import argparse
import os
import re
import sys
from pathlib import Path

MARKER_VERSION = 6
MARKER = f"<!-- MCAS_REBRAND_APPLIED v{MARKER_VERSION} -->"
MARKER_ANY = re.compile(r"<!-- MCAS_REBRAND_APPLIED v\d+ -->")

# Files to skip outright.
# NOTE: _OBSOLETE_-prefixed files ARE rebranded — per Shar, those carry the
# active week-1 discussion, overview, and trainer pages despite the prefix.
# Only true throwaway prefixes are skipped here.
SKIP_PREFIXES = ("_TRASH_", "_archive", "_apply_", "_build_")
SKIP_FILES = {
    "index.html",
    "canvas-home.html",
    "ai_policy.html",          # hand-built MCAS-native; source of truth
    "ai_honor_contract.html",  # hand-built MCAS-native; source of truth
}

# ---------------------------------------------------------------------------
# MCAS palette
# ---------------------------------------------------------------------------
MCAS_NAVY   = "#0B1530"
MCAS_RUST   = "#8B3A2E"
MCAS_GOLD   = "#C9A14A"
MCAS_CREAM  = "#F5F1E8"
MCAS_DARK   = "#060A18"
MCAS_WHITE  = "#FFFFFF"

# Colors that should never appear (banned by global rule + Shar's "no teal")
BANNED_COLORS_TO_NAVY = [
    "#2F4F4F", "#2f4f4f",          # dark slate gray / pseudo-teal
    "#008080", "#008b8b", "#5F9EA0",  # teal, dark cyan, cadet blue
    "#20B2AA", "#48D1CC", "#40E0D0",  # light sea green, medium turquoise, turquoise
    "#00CED1", "#00FFFF", "#7FFFD4",  # dark turquoise, aqua, aquamarine
    "teal", "Teal", "TEAL",
]

# Sage-family colors should never appear in teaching deliverables (global rule)
BANNED_COLORS_TO_CREAM = [
    "#B2BEB5", "#9CAF88", "#A8B5A0",  # ashes of sage / sage tints
    "#E9EBE0", "#DDE4D4",              # cream-like sage tints (legacy)
    "#4F6B57", "#3F5B47",              # sage-dark and sage-deeper from syllabus tokens
    "#F1F4F1",                         # sage-tinted quiz-day background
]

# Map filename → week number on the hub. Each rebranded page links back to
# index.html#week-{N}. Order: explicit topic→week pairs first; the runtime
# extends this with regex matches for workbook_dayNN_*, weekNN_*, and
# _OBSOLETE_*weekN* patterns. Topics derived from biol304_syllabus.html.
TOPIC_WEEK_MAP = {
    # ---- Week 1: Foundations + Cell + Membrane Transport
    "levels-of-organization.html": 1,
    "anatomical-position.html": 1,
    "anatomical-terminology.html": 1,
    "body-regions.html": 1,
    "body-cavities.html": 1,
    "homeostasis-feedback.html": 1,
    "homeostasis.html": 1,
    "cell-structure.html": 1,
    "membrane-transport.html": 1,
    # ---- Week 2: Tissues + Integument
    "epithelial-tissue.html": 2,
    "connective-tissues.html": 2,
    "muscle-nervous-tissue.html": 2,
    "skin-layers.html": 2,
    "skin-functions.html": 2,
    # ---- Week 3: Skeletal
    "bone-tissue.html": 3,
    "axial-skeleton.html": 3,
    "appendicular-skeleton.html": 3,
    "joints-movements.html": 3,
    "joints-and-movements.html": 3,
    # ---- Week 4: Muscle + Nervous start
    "skeletal-muscle-microanatomy.html": 4,
    "motor-units.html": 4,
    "sliding-filament.html": 4,
    "cross-bridge-cycle.html": 4,
    "neurons-rmp.html": 4,
    "neurons-resting-potential.html": 4,
    "action-potentials.html": 4,
    "action-potentials-synapses.html": 4,
    # ---- Week 5: Nervous + Senses + Endocrine start
    "cns-organization.html": 5,
    "pns-autonomic.html": 5,
    "vision.html": 5,
    "hearing-equilibrium.html": 5,
    "hormone-mechanisms.html": 5,
    "major-glands.html": 5,
    "major-endocrine-glands.html": 5,
    # ---- Week 6: Blood + Cardiovascular
    "blood-composition.html": 6,
    "hemostasis-blood-typing.html": 6,
    "heart-anatomy.html": 6,
    "heart-cardiac-cycle.html": 6,
    "cardiac-conduction.html": 6,
    "conduction-ecg.html": 6,
    "blood-vessels-hemodynamics.html": 6,
    "vessels-hemodynamics.html": 6,
    # ---- Week 7: Immune + Respiratory + GI
    "lymphatic-innate.html": 7,
    "lymphatic-innate-immunity.html": 7,
    "adaptive-immunity.html": 7,
    "respiratory-anatomy-mechanics.html": 7,
    "resp-anatomy-mechanics.html": 7,
    "respiratory-anatomy.html": 7,
    "gas-exchange-transport.html": 7,
    "gi-anatomy-motility.html": 7,
    "digestion-absorption.html": 7,
    # ---- Week 8: Renal + Reproductive
    "kidney-filtration.html": 8,
    "kidney-anatomy-gfr.html": 8,
    "tubular-function.html": 8,
    "fluid-electrolyte-acid-base.html": 8,
    "fluid-acid-base.html": 8,
    "male-reproductive.html": 8,
    "female-reproductive.html": 8,
    "pregnancy-development.html": 8,
    "pregnancy-basics.html": 8,
}

# Files that don't belong to any week (course-wide pages). Back-link to plain index.html.
COURSE_WIDE_PAGES = {
    "canvas-home.html",
    "index.html",
    "biol304_syllabus.html",
    "biol304_how_to_reach_me.html",
    "biol304_accessibility.html",
    "biol304_rsi_statement.html",
    "biol304_tech_setup.html",
    "biol304_textbook.html",
    "biol304_reading_map.html",
    "ai_honor_contract.html",
    "ai_transparency_document.html",
    "integrity.html",
    "discussions.html",
    "concept_videos.html",
    "bio304-spaced-recall-prototype.html",
    "comprehensive-practice-final.html",
    "submission-directions.html",
    "course.html",
    "course-orientation.html",
    "enter-course.html",
    "clinical_portfolio_hub.html",
    "schedule.html",
    "nonmajors_ap_rhythm_card.html",
    "if-you-fall-behind.html",
    "how_spaced_recall_works.html",
}

def week_for_filename(name: str) -> int | None:
    """Return week number (1-8) for the given filename, or None."""
    if name in COURSE_WIDE_PAGES:
        return None
    if name in TOPIC_WEEK_MAP:
        return TOPIC_WEEK_MAP[name]
    # workbook_dayNN_* → day NN belongs to week ceil(NN/4)
    m = re.match(r"workbook_day(\d+)_", name, flags=re.IGNORECASE)
    if m:
        day = int(m.group(1))
        if 1 <= day <= 32:
            return (day - 1) // 4 + 1
    # weekNN_discussion.html and other week-prefixed pages
    m = re.match(r"week(\d{1,2})_", name, flags=re.IGNORECASE)
    if m:
        wk = int(m.group(1))
        if 1 <= wk <= 8:
            return wk
    # portfolio_weekNN_template.html (clinical portfolio per-week templates)
    m = re.match(r"portfolio_week(\d{1,2})_", name, flags=re.IGNORECASE)
    if m:
        wk = int(m.group(1))
        if 1 <= wk <= 8:
            return wk
    # _OBSOLETE_biol304_weekN_*, _OBSOLETE_weekNN_*
    m = re.match(r"_OBSOLETE_(?:biol304_)?week(\d{1,2})_", name, flags=re.IGNORECASE)
    if m:
        wk = int(m.group(1))
        if 1 <= wk <= 8:
            return wk
    return None

def back_link_target(name: str) -> str:
    """Anchor URL for this page's back-to-hub link."""
    wk = week_for_filename(name)
    return f"index.html#week-{wk}" if wk else "index.html"

# ---------------------------------------------------------------------------
# Override CSS block — appended at the end of the first <style> in every page
# ---------------------------------------------------------------------------
MCAS_OVERRIDE_CSS = """
/* ============================================================
   MCAS REBRAND OVERRIDES — appended by rebrand-mcas.py
   These rules win the cascade so the underlying page styling
   does not need to change. JS logic (video gating, spaced recall)
   is untouched.
   ============================================================ */
:root {
  /* New MCAS tokens for any rule that wants them */
  --mcas-navy:  #0B1530;
  --mcas-rust:  #8B3A2E;
  --mcas-gold:  #C9A14A;
  --mcas-cream: #F5F1E8;
  --mcas-dark:  #060A18;
  /* Remap legacy PRIMARY palette tokens (syllabus, schedule, etc.)
     so every rule that references them switches to MCAS values
     automatically. No rule-by-rule rewriting needed. */
  --navy: #0B1530;
  --navy-deep: #060A18;
  --navy-tint: #F5F1E8;
  --gold: #C9A14A;
  --gold-deep: #B08B3A;
  --terra: #8B3A2E;
  --terra-dark: #8B3A2E;
  /* Sage is banned. Remap any sage tokens to MCAS gold so legacy
     sage rules render as gold accents on dark sections. */
  --sage-dark: #C9A14A;
  --sage-deeper: #B08B3A;
  --white: #FFFFFF;
  --off-white: #FFFFFF;
  --gray-line: rgba(11, 21, 48, 0.18);
  --gray-soft: rgba(11, 21, 48, 0.72);
}
html, body.mcas-page {
  font-family: 'Plus Jakarta Sans Variable', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
  background: #FFFFFF !important;
  color: var(--mcas-navy) !important;
}
/* Force Plus Jakarta Sans across EVERY element except code/monospace.
   This kills Lora, DM Sans, Cormorant Garamond, Georgia, and any other
   stray font-family declarations on child elements that were winning
   the specificity fight against the body rule. */
body.mcas-page,
body.mcas-page *:not(code):not(pre):not(kbd):not(samp):not(tt) {
  font-family: 'Plus Jakarta Sans Variable', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
}
body.mcas-page h1, body.mcas-page h2, body.mcas-page h3,
body.mcas-page h4, body.mcas-page h5, body.mcas-page h6 {
  color: var(--mcas-navy) !important;
  letter-spacing: -0.015em;
}
body.mcas-page a { color: var(--mcas-rust); }
body.mcas-page a:hover { color: #A0452F; }
body.mcas-page a:focus-visible {
  outline: 3px solid var(--mcas-rust);
  outline-offset: 3px;
  border-radius: 4px;
}

/* ----- NO BOOKENDS RULE -----
   Strip section-edge bookend borders from header.page-head, section.band,
   nav.toc, .banner, .page-head, the syllabus's section blocks, etc.
   Cards (.card, [class*="-card"], details, table, button) keep their
   functional outlines. Sections rely on background contrast and hover
   lifts for differentiation. */
body.mcas-page header.page-head,
body.mcas-page .banner,
body.mcas-page .page-head,
body.mcas-page section.band,
body.mcas-page nav.toc,
body.mcas-page .footer-section,
body.mcas-page .footer-top {
  border-top: none !important;
  border-bottom: none !important;
}
/* Hover lift utility — ONLY on elements that are actually clickable
   (an anchor) or interactive (FAQ summary). Read-only info elements
   like .glance-item never lift. */
body.mcas-page a[class*="-card"],
body.mcas-page a[class*="-tile"],
body.mcas-page a.resource-tile,
body.mcas-page details.faq-item {
  transition: transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease;
}
body.mcas-page a[class*="-card"]:hover,
body.mcas-page a[class*="-tile"]:hover,
body.mcas-page a.resource-tile:hover,
body.mcas-page details.faq-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(11, 21, 48, 0.10);
}

/* Responsive: stack each day-tile pill button on its own line below 900px.
   This covers phones AND tablets, so each Pre-work / SR / Lab workbook /
   Daily Review / Discussion button sits on its own row, full-width,
   with a comfortable 44px tap target. Above 900px the original inline
   layout shows. */
@media (max-width: 900px) {
  body.mcas-page .day-tile a.day-pill,
  body.mcas-page a.day-pill {
    display: flex !important;
    width: 100% !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 8px 0 !important;
    padding: 12px 18px !important;
    min-height: 44px !important;
    box-sizing: border-box !important;
  }
  body.mcas-page .day-tile {
    padding: 14px !important;
  }
}

/* Course-at-a-Glance (syllabus Section 2 / schedule overview) — one info
   panel, not eight clickable-looking cards. Forces white background,
   thin shadow, and strips the individual card styling from inner items. */
body.mcas-page .glance {
  background: #FFFFFF !important;
  border: none !important;
  border-radius: 10px !important;
  box-shadow: 0 1px 3px rgba(11, 21, 48, 0.08) !important;
  padding: 30px 34px !important;
  display: grid !important;
  gap: 24px 36px !important;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) !important;
}
body.mcas-page .glance-item {
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  padding: 0 !important;
  transform: none !important;
  cursor: default !important;
}
body.mcas-page .glance-item:hover {
  transform: none !important;
  box-shadow: none !important;
}

/* MCAS chrome (site header + footer) — scoped so it never collides
   with existing IDs/classes on the page */
.mcas-chrome,
.mcas-chrome * { box-sizing: border-box; }
.mcas-header {
  /* No bookend border per MCAS rule — separation via background contrast */
  background: #FFFFFF;
  padding: 24px max(40px, 5vw);
  font-family: 'Plus Jakarta Sans Variable', 'Plus Jakarta Sans', system-ui, sans-serif;
}
.mcas-header-row {
  display: flex; align-items: center; justify-content: space-between;
  gap: 16px; flex-wrap: wrap;
}
.mcas-brand { display: inline-flex; align-items: center; gap: 14px; text-decoration: none; color: var(--mcas-navy); }
.mcas-brand svg { height: 44px; width: auto; display: block; }
.mcas-brand-title { font-size: 18px; font-weight: 800; line-height: 1; letter-spacing: -0.015em; }
.mcas-brand-title .accent { color: var(--mcas-rust); }
.mcas-brand-sub {
  font-size: 9.5px; font-weight: 700; letter-spacing: 0.20em;
  text-transform: uppercase; color: var(--mcas-navy); opacity: 0.72;
  display: block; margin-top: 3px;
}
.mcas-back {
  font-size: 11px; font-weight: 700; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--mcas-rust);
  text-decoration: none; padding: 8px 14px; border: 1px solid var(--mcas-rust);
  border-radius: 4px;
}
.mcas-back:hover, .mcas-back:focus-visible {
  background: var(--mcas-rust); color: #FFFFFF;
}
/* Thin back-link strip — used when the page already has its own brand */
.mcas-backlink-strip {
  background: #FFFFFF;
  padding: 14px max(40px, 5vw);
  display: flex; justify-content: flex-start; align-items: center;
}
.mcas-footer {
  /* No bookend border — dark background is the separator */
  background: var(--mcas-dark);
  color: var(--mcas-cream);
  padding: 40px max(40px, 5vw) 28px;
  font-family: 'Plus Jakarta Sans Variable', 'Plus Jakarta Sans', system-ui, sans-serif;
  margin-top: 56px;
}
/* Footer link color — bumped to body-scoped selector so it wins
   specificity against body.mcas-page a (which was forcing rust on dark
   navy and failing WCAG contrast). White on the near-black footer
   passes AAA; gold on hover gives brand pop. */
body.mcas-page .mcas-footer a,
.mcas-footer a {
  color: #FFFFFF !important;
  text-decoration: none;
  opacity: 0.92;
}
body.mcas-page .mcas-footer a:hover,
body.mcas-page .mcas-footer a:focus-visible,
.mcas-footer a:hover,
.mcas-footer a:focus-visible {
  color: var(--mcas-gold) !important;
  opacity: 1;
  text-decoration: underline;
}
body.mcas-page .mcas-footer a:focus-visible,
.mcas-footer a:focus-visible {
  outline: 3px solid var(--mcas-gold);
  outline-offset: 3px;
  border-radius: 4px;
}
.mcas-footer-row {
  /* No bookend border — extra padding-top supplies the separation */
  display: flex; justify-content: space-between; align-items: center;
  gap: 16px; flex-wrap: wrap; padding-top: 32px; margin-top: 24px;
}
.mcas-footer-links { display: flex; gap: 22px; flex-wrap: wrap; }
.mcas-footer-link { font-size: 12.5px; font-weight: 500; letter-spacing: 0.02em; }
.mcas-footer-copyright {
  font-size: 11px; opacity: 0.72; letter-spacing: 0.03em;
}
.mcas-footer-byline {
  font-size: 11px; font-weight: 700; color: var(--mcas-gold);
  letter-spacing: 0.16em; text-transform: uppercase;
}
.mcas-skip {
  position: absolute; top: -100px; left: 8px;
  background: var(--mcas-navy); color: var(--mcas-cream);
  padding: 12px 20px; text-decoration: none;
  font-size: 13px; font-weight: 700;
  border-radius: 4px; z-index: 9999; letter-spacing: 0.04em;
}
.mcas-skip:focus { top: 8px; }
@media (prefers-reduced-motion: reduce) {
  .mcas-chrome *, .mcas-chrome { transition: none !important; animation: none !important; }
}

/* ----- Primary CTA button (.btn-gold) — accessibility fix -----
   The underlying page styled .btn-gold as navy bg + white text, but the
   body.mcas-page anchor color rule (rust on a) won the cascade and gave
   us rust text on dark navy — fails WCAG contrast. Override: dark terra
   cotta background (brand rust) with white text. Hover deepens to
   rust-dark per the MCAS spec.
*/
body.mcas-page a.btn-gold,
body.mcas-page .btn-gold {
  background: var(--mcas-rust) !important;
  color: #FFFFFF !important;
  border: 2px solid var(--mcas-rust) !important;
}
body.mcas-page a.btn-gold:hover,
body.mcas-page a.btn-gold:focus-visible,
body.mcas-page .btn-gold:hover,
body.mcas-page .btn-gold:focus-visible {
  background: #A0452F !important;
  color: #FFFFFF !important;
  border-color: #A0452F !important;
}

/* ----- Pre-work ↔ Workbook wiring asides -----
   .mcas-next-up        appears on a pre-work topic spoke, points forward
                        to the Day-N lab workbook.
   .mcas-prework-link   appears on a Day-N workbook, points back to its
                        pre-work topic spoke.
   Same visual: white card, thin shadow, gold accent line on the left,
   no hover-lift (these are read-then-click affordances, not browsing tiles).
*/
body.mcas-page .mcas-next-up,
body.mcas-page .mcas-prework-link {
  background: #FFFFFF;
  border: none;
  border-left: 4px solid var(--mcas-gold);
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(11, 21, 48, 0.08);
  padding: 20px 24px;
  margin: 28px 0;
  display: block;
}
body.mcas-page .mcas-next-up-eyebrow,
body.mcas-page .mcas-prework-link-eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mcas-rust);
  margin: 0 0 6px 0;
}
body.mcas-page a.mcas-next-up-cta,
body.mcas-page a.mcas-prework-link-cta {
  display: inline-block;
  font-size: 17px;
  font-weight: 700;
  color: var(--mcas-navy);
  text-decoration: none;
  line-height: 1.35;
}
body.mcas-page a.mcas-next-up-cta:hover,
body.mcas-page a.mcas-prework-link-cta:hover,
body.mcas-page a.mcas-next-up-cta:focus-visible,
body.mcas-page a.mcas-prework-link-cta:focus-visible {
  color: var(--mcas-rust);
  text-decoration: underline;
}
body.mcas-page a.mcas-next-up-cta:focus-visible,
body.mcas-page a.mcas-prework-link-cta:focus-visible {
  outline: 3px solid var(--mcas-rust);
  outline-offset: 3px;
  border-radius: 4px;
}

/* ----- Lecture video notes section (on spoke pages, under the video) -----
   Freeform textarea that autosaves to localStorage keyed by topic ID.
   Visible in Notes and Study modes; hidden in Quiz mode. Prints cleanly
   so handwritten or typed notes can be carried out of class.
*/
body.mcas-page .mcas-lecture-notes {
  background: #FFFFFF;
  border: none;
  border-left: 4px solid var(--mcas-gold);
  border-radius: 6px;
  padding: 22px 24px 18px;
  margin: 16px 0 24px;
  box-shadow: 0 1px 3px rgba(11, 21, 48, 0.06);
}
body.mcas-page .mcas-lecture-notes-eyebrow {
  font-family: 'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mcas-rust);
  margin: 0 0 4px;
}
body.mcas-page .mcas-lecture-notes h2 {
  font-size: 20px;
  font-weight: 800;
  color: var(--mcas-navy);
  margin: 0 0 6px;
  letter-spacing: -0.01em;
}
body.mcas-page .mcas-lecture-notes-instr {
  font-style: italic;
  font-size: 13.5px;
  color: var(--mcas-navy);
  opacity: 0.78;
  margin: 0 0 10px;
}
body.mcas-page #mcas-lecture-notes-input {
  width: 100%;
  min-height: 160px;
  padding: 14px 16px;
  font-family: 'Plus Jakarta Sans Variable', 'Plus Jakarta Sans', system-ui, sans-serif;
  font-size: 15px;
  color: var(--mcas-navy);
  line-height: 1.55;
  border: 1px solid rgba(11, 21, 48, 0.18);
  border-radius: 6px;
  background: #FFFFFF;
  resize: vertical;
  box-sizing: border-box;
}
body.mcas-page #mcas-lecture-notes-input:focus-visible {
  outline: 3px solid var(--mcas-rust);
  outline-offset: 1px;
  border-color: var(--mcas-navy);
}
body.mcas-page .mcas-lecture-notes-status {
  font-size: 12px;
  color: var(--mcas-navy);
  opacity: 0.6;
  margin: 6px 0 0;
  min-height: 1.2em;
}
/* Hide in quiz mode (consistent with other interactive elements). */
body.mcas-page.quiz .mcas-lecture-notes { display: none; }
@media print {
  body.mcas-page .mcas-lecture-notes {
    box-shadow: none;
    border: 1px solid rgba(0,0,0,0.15);
    page-break-inside: avoid;
  }
  body.mcas-page #mcas-lecture-notes-input {
    border: 1px solid rgba(0,0,0,0.3);
    background: #FFFFFF;
    color: #000;
  }
}

/* Gated state — workbook aside is locked until the spoke page's retrieval
   check is passed. The gating JS adds .gate-locked to the CTA when the
   localStorage flag bio304-gate-{TOPIC_ID} is not yet set. */
body.mcas-page .mcas-next-up.is-gated {
  border-left-color: rgba(11, 21, 48, 0.25);
}
body.mcas-page a.mcas-next-up-cta.gate-locked {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: auto;
  color: var(--mcas-navy);
}
body.mcas-page a.mcas-next-up-cta.gate-locked:hover,
body.mcas-page a.mcas-next-up-cta.gate-locked:focus-visible {
  color: var(--mcas-navy);
  text-decoration: none;
}
body.mcas-page .mcas-next-up-gate-hint {
  display: block;
  margin-top: 8px;
  font-family: 'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mcas-rust);
}
body.mcas-page .mcas-next-up-gate-hint[hidden] { display: none; }
"""

# ---------------------------------------------------------------------------
# MCAS chrome — header + footer to wrap the page
# ---------------------------------------------------------------------------
MCAS_LOGO_SVG = '''<svg viewBox="40 10 125 148" role="img" aria-hidden="true" focusable="false">
<g transform="translate(0, 18)">
<g transform="translate(60, 0) rotate(8 0 130)">
<circle cx="0" cy="20" r="10" fill="#0B1530"/>
<path d="M 0,32 C -10,32 -16,36 -16,42 C -16,55 -13,68 -11,82 C -10,100 -12,118 -14,130 L 14,130 C 12,118 10,100 11,82 C 13,68 16,55 16,42 C 16,36 10,32 0,32 Z" fill="#0B1530"/>
</g>
<g transform="translate(100, 0)">
<circle cx="0" cy="10" r="11" fill="#8B3A2E"/>
<path d="M 0,22 C -11,22 -17,26 -17,34 C -17,52 -14,70 -12,86 C -11,108 -13,122 -15,132 L 15,132 C 13,122 11,108 12,86 C 14,70 17,52 17,34 C 17,26 11,22 0,22 Z" fill="#8B3A2E"/>
</g>
<g transform="translate(140, 0) rotate(-8 0 130)">
<circle cx="0" cy="20" r="10" fill="#C9A14A"/>
<path d="M 0,32 C -10,32 -16,36 -16,42 C -16,55 -13,68 -11,82 C -10,100 -12,118 -14,130 L 14,130 C 12,118 10,100 11,82 C 13,68 16,55 16,42 C 16,36 10,32 0,32 Z" fill="#C9A14A"/>
</g>
</g>
</svg>'''

# Sentinel comments so re-runs can cleanly strip the previous chrome before
# re-injecting. NEVER write chrome without these markers.
HEADER_OPEN_TAG  = "<!-- mcas-chrome-header -->"
HEADER_CLOSE_TAG = "<!-- mcas-chrome-header-end -->"
FOOTER_OPEN_TAG  = "<!-- mcas-chrome-footer -->"
FOOTER_CLOSE_TAG = "<!-- mcas-chrome-footer-end -->"
HEIGHT_OPEN_TAG  = "<!-- mcas-iframe-height-sender -->"
HEIGHT_CLOSE_TAG = "<!-- mcas-iframe-height-sender-end -->"
WBGATE_OPEN_TAG  = "<!-- mcas-workbook-aside-gate -->"
WBGATE_CLOSE_TAG = "<!-- mcas-workbook-aside-gate-end -->"
LECNOTES_OPEN_TAG  = "<!-- mcas-lecture-notes-injector -->"
LECNOTES_CLOSE_TAG = "<!-- mcas-lecture-notes-injector-end -->"

# Auto-injector for the lecture-video-notes section. Inserts a freeform
# textarea right after the page's video-panel (or .video-panel) element,
# wires localStorage persistence keyed by topic id (from SHEET_CONFIG)
# or by document title. No-op on pages without a video panel.
LECTURE_NOTES_INJECTOR = '''<!-- mcas-lecture-notes-injector -->
<script>
(function(){
  function init(){
    var videoPanel = document.querySelector("#video-panel, .video-panel");
    if (!videoPanel) return;
    if (document.getElementById("mcas-lecture-notes-input")) return;

    var cfg = window.SHEET_CONFIG || {};
    var m = (cfg.prework || "").match(/topic=([\\w-]+)/);
    var topicId = m ? m[1] : null;
    var keyBase = topicId || (document.title || "page").toLowerCase().replace(/[^a-z0-9]+/g, "-");
    var key = "bio304-lecture-notes-" + keyBase;

    var section = document.createElement("section");
    section.className = "mcas-lecture-notes";
    section.setAttribute("aria-labelledby", "mcas-lecture-notes-h");
    section.innerHTML =
      '<p class="mcas-lecture-notes-eyebrow">While you watch</p>' +
      '<h2 id="mcas-lecture-notes-h">Lecture video notes</h2>' +
      '<p class="mcas-lecture-notes-instr">A scratchpad for what stands out as the video runs. Your notes save on this device and stay here when you come back.</p>' +
      '<textarea id="mcas-lecture-notes-input" rows="8" aria-describedby="mcas-lecture-notes-status" placeholder="Type what is clicking for you..."></textarea>' +
      '<p class="mcas-lecture-notes-status" id="mcas-lecture-notes-status" aria-live="polite"></p>';

    if (videoPanel.parentNode) videoPanel.parentNode.insertBefore(section, videoPanel.nextSibling);

    var ta = section.querySelector("#mcas-lecture-notes-input");
    var status = section.querySelector("#mcas-lecture-notes-status");

    try {
      var saved = window.localStorage.getItem(key);
      if (saved) ta.value = saved;
      if (status) status.textContent = saved ? "Restored from your last session." : "";
    } catch (e) {}

    var t, debounceTimer;
    function save(){
      try { window.localStorage.setItem(key, ta.value); } catch (e) {}
      if (status) {
        status.textContent = "Saved on this device";
        clearTimeout(t);
        t = setTimeout(function(){ if (status) status.textContent = ""; }, 1400);
      }
    }
    ta.addEventListener("input", function(){
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(save, 350);
    });
    ta.addEventListener("blur", save);
    window.addEventListener("pagehide", save);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
</script>
<!-- mcas-lecture-notes-injector-end -->'''

# Gate script — injected at end of <body> on every page that carries a
# .mcas-next-up workbook aside. Reads SHEET_CONFIG.prework on spoke pages
# to derive the topic id; no-op on pages without SHEET_CONFIG.
WORKBOOK_GATE_SCRIPT = '''<!-- mcas-workbook-aside-gate -->
<script>
/* Gate the lab-workbook CTA on this spoke until the retrieval check is
   passed. Re-derives the topic id from SHEET_CONFIG.prework so the same
   block works on any spoke page that follows the bio304-option-a pattern.
   On pages without a SHEET_CONFIG, this is a no-op (aside stays unlocked). */
(function(){
  function init(){
    var cfg = window.SHEET_CONFIG || {};
    var m = (cfg.prework || "").match(/topic=([\\w-]+)/);
    var topicId = m ? m[1] : null;
    if (!topicId) return;

    var aside = document.querySelector("aside.mcas-next-up");
    var cta   = aside ? aside.querySelector("a.mcas-next-up-cta") : null;
    var hint  = document.getElementById("mcas-next-up-gate-hint");
    if (!cta) return;

    function gatePassed(){
      try { return window.localStorage.getItem("bio304-gate-" + topicId) === "true"; }
      catch (e) { return false; }
    }
    function lock(){
      cta.classList.add("gate-locked");
      cta.setAttribute("aria-disabled", "true");
      if (hint) hint.hidden = false;
      if (aside) aside.classList.add("is-gated");
    }
    function unlock(){
      cta.classList.remove("gate-locked");
      cta.removeAttribute("aria-disabled");
      if (hint) hint.hidden = true;
      if (aside) aside.classList.remove("is-gated");
    }

    if (gatePassed()) {
      unlock();
    } else {
      lock();
      cta.addEventListener("click", function(e){
        if (!cta.classList.contains("gate-locked")) return;
        e.preventDefault();
        var gateSection = document.getElementById("explain-gate");
        if (gateSection && gateSection.hidden) {
          alert("Watch the video first, then complete the retrieval check below.");
        } else if (gateSection) {
          gateSection.scrollIntoView({ behavior: "smooth", block: "center" });
          var input = document.getElementById("gate-input");
          if (input) input.focus();
        }
      });
      var submitBtn = document.getElementById("gate-submit");
      if (submitBtn) {
        submitBtn.addEventListener("click", function(){
          setTimeout(function(){ if (gatePassed()) unlock(); }, 60);
        });
      }
      window.addEventListener("storage", function(e){
        if (e.key === "bio304-gate-" + topicId && e.newValue === "true") unlock();
      });
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
</script>
<!-- mcas-workbook-aside-gate-end -->'''

def mcas_header_full_html(back_href: str = "index.html", back_label: str = "Course home"):
    """Full MCAS header with brand SVG, for pages that have NO existing header."""
    return f'''{HEADER_OPEN_TAG}
<a href="#mcas-content" class="mcas-skip">Skip to main content</a>
<div class="mcas-chrome">
<header class="mcas-header">
  <div class="mcas-header-row">
    <a class="mcas-brand" href="index.html" target="_top" aria-label="BIO 304 Human Anatomy and Physiology, course home">
      {MCAS_LOGO_SVG}
      <span>
        <span class="mcas-brand-title">Human <span class="accent">A&amp;P</span></span>
        <span class="mcas-brand-sub">BIO 304 &middot; American River College</span>
      </span>
    </a>
    <a class="mcas-back" href="{back_href}" target="_top">&larr; {back_label}</a>
  </div>
</header>
</div>
<main id="mcas-content" class="mcas-content">
{HEADER_CLOSE_TAG}'''

def mcas_backlink_only_html(back_href: str = "index.html", back_label: str = "Course home"):
    """Thin back-link strip only, for pages that ALREADY have their own
    brand header — avoids the duplicate-brand problem."""
    return f'''{HEADER_OPEN_TAG}
<a href="#mcas-content" class="mcas-skip">Skip to main content</a>
<div class="mcas-chrome">
<div class="mcas-backlink-strip">
  <a class="mcas-back" href="{back_href}" target="_top">&larr; {back_label}</a>
</div>
</div>
<main id="mcas-content" class="mcas-content">
{HEADER_CLOSE_TAG}'''

def _strip_nested_div_blocks_by_class(html: str, class_name: str) -> str:
    """Strip every <div class="...class_name..."> ... </div> block, walking
    the token stream and counting <div>/</div> depth so nested divs are
    matched correctly. Removes the entire block (inclusive of outer open
    and close tags). Repeats until no more matches."""
    open_re = re.compile(
        r'<div\b[^>]*\bclass\s*=\s*"[^"]*\b' + re.escape(class_name) + r'\b[^"]*"[^>]*>',
        re.IGNORECASE,
    )
    div_tok = re.compile(r'<(/?)div\b[^>]*>', re.IGNORECASE)
    guard = 0
    while True:
        guard += 1
        if guard > 50:
            return html  # paranoid bail-out
        m = open_re.search(html)
        if not m:
            return html
        start = m.start()
        depth = 0
        end = None
        for dm in div_tok.finditer(html, start):
            if not dm.group(1):
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end = dm.end()
                    break
        if end is None:
            return html  # malformed; safer to leave as-is
        html = html[:start] + html[end:]


# Orphan close-tag corrective pass — runs once after sentinel chrome is
# stripped. v5 lazy-regex stripping left runs of orphan </div>/</header>
# tags right after <body ...> on files that were --force'd multiple times.
# This pass mops them up. Safe: only fires immediately after <body ...>,
# never touches deeper structure.
_ORPHAN_CLOSE_RUN = re.compile(
    r'\A(?:\s*</(?:div|header|main|section|nav|article|aside|footer)>)+\s*',
    re.IGNORECASE,
)

def strip_orphans_after_body_open(html: str) -> str:
    m = re.search(r"<body[^>]*>", html, re.IGNORECASE)
    if not m:
        return html
    after = m.end()
    run = _ORPHAN_CLOSE_RUN.match(html[after:])
    if not run:
        return html
    return html[:after] + "\n" + html[after + run.end():]


def strip_previous_mcas_chrome(html: str) -> str:
    """Remove any previously-injected MCAS chrome (header, footer, height-sender)
    based on sentinel comments. Safe to call on un-chromed pages — no-op.

    v6: legacy fallback uses counter-based nested-div matching instead of a
    lazy regex, so the outer </div> of every <div class="mcas-chrome">
    block closes correctly (no more orphan close tags after re-runs)."""
    # Sentinel-bounded strips. Consume immediately adjacent whitespace so
    # re-runs with --force don't accumulate blank lines around the inject
    # points.
    html = re.sub(
        r"\s*" + re.escape(HEADER_OPEN_TAG) + r".*?" + re.escape(HEADER_CLOSE_TAG) + r"\s*",
        "\n", html, flags=re.DOTALL,
    )
    html = re.sub(
        r"\s*" + re.escape(FOOTER_OPEN_TAG) + r".*?" + re.escape(FOOTER_CLOSE_TAG) + r"\s*",
        "\n", html, flags=re.DOTALL,
    )
    html = re.sub(
        r"\s*" + re.escape(HEIGHT_OPEN_TAG) + r".*?" + re.escape(HEIGHT_CLOSE_TAG) + r"\s*",
        "\n", html, flags=re.DOTALL,
    )
    # Legacy (pre-sentinel v1–v4) chrome strip
    html = re.sub(
        r'<a href="#mcas-content" class="mcas-skip">[^<]*</a>\s*',
        "", html, flags=re.IGNORECASE,
    )
    # Counter-based nested-div strip for <div class="mcas-chrome">…</div>
    html = _strip_nested_div_blocks_by_class(html, "mcas-chrome")
    # Strip the orphan <main id="mcas-content"> opening tag, then its
    # matching </main>. Both are unique to MCAS-injected chrome.
    main_open = re.search(r'<main\s+id="mcas-content"[^>]*>\s*', html, flags=re.IGNORECASE)
    if main_open:
        # Find the matching </main> using <main>/</main> depth counting,
        # starting from the opening match.
        main_tok = re.compile(r'<(/?)main\b[^>]*>', re.IGNORECASE)
        depth = 0
        end_close = None
        for tm in main_tok.finditer(html, main_open.start()):
            if not tm.group(1):
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end_close = tm
                    break
        # Remove the opening tag
        html = html[:main_open.start()] + html[main_open.end():]
        # Remove the matching closing tag (offset shifted)
        if end_close is not None:
            # Re-search relative to remaining string, near old position
            shift = main_open.end() - main_open.start()
            close_start = end_close.start() - shift
            close_end = end_close.end() - shift
            html = html[:close_start] + html[close_end:]
    # One-time corrective pass for already-broken files (orphan close tags
    # left between <body> and the page's real content by past --force runs).
    html = strip_orphans_after_body_open(html)
    return html

# Regex to detect a pre-existing branded header anywhere in the page
EXISTING_HEADER_PATTERNS = [
    re.compile(r'<header[^>]*class="[^"]*\bpage-head\b[^"]*"', re.IGNORECASE),
    re.compile(r'<header[^>]*class="[^"]*\bsite-header\b[^"]*"', re.IGNORECASE),
    re.compile(r'<header[^>]*class="[^"]*\bbanner\b[^"]*"',     re.IGNORECASE),
    re.compile(r'<div[^>]*class="[^"]*\bbanner\b[^"]*"',        re.IGNORECASE),
    re.compile(r'<header[^>]*class="[^"]*\bmasthead\b[^"]*"',   re.IGNORECASE),
]

def page_has_existing_branded_header(html: str) -> bool:
    return any(p.search(html) for p in EXISTING_HEADER_PATTERNS)

MCAS_FOOTER_HTML = '''<!-- mcas-chrome-footer -->
</main>
<div class="mcas-chrome">
<footer class="mcas-footer">
  <div class="mcas-footer-links">
    <a class="mcas-footer-link" href="index.html" target="_top">Course home</a>
    <a class="mcas-footer-link" href="biol304_syllabus.html" target="_top">Syllabus</a>
    <a class="mcas-footer-link" href="course-orientation.html" target="_top">Orientation</a>
    <a class="mcas-footer-link" href="concept_videos.html" target="_top">Concept videos</a>
    <a class="mcas-footer-link" href="bio304-spaced-recall-prototype.html" target="_top">Spaced recall</a>
    <a class="mcas-footer-link" href="biol304_accessibility.html" target="_top">Accessibility</a>
  </div>
  <div class="mcas-footer-row">
    <div class="mcas-footer-copyright">BIO 304 Human Anatomy &amp; Physiology &middot; American River College</div>
    <div class="mcas-footer-byline">Dr. Sharilyn Rennie</div>
  </div>
</footer>
</div>
<!-- mcas-chrome-footer-end -->'''

# Iframe height-sender (Kajabi-friendly), parameterized per-page
HEIGHT_SENDER_TEMPLATE = '''<!-- mcas-iframe-height-sender -->
<script>
/* MCAS iframe height-sender (rebrand-mcas.py) */
(function(){{
  var FRAME_ID = "bio304-{slug}";
  function sendHeight(){{
    var h = Math.max(document.documentElement.scrollHeight,
                     document.body ? document.body.scrollHeight : 0);
    parent.postMessage({{type:"resize", id:FRAME_ID, height:h}}, "*");
  }}
  window.addEventListener("load", sendHeight);
  window.addEventListener("resize", sendHeight);
  if (window.ResizeObserver) new ResizeObserver(sendHeight).observe(document.body);
}})();
</script>
<!-- mcas-iframe-height-sender-end -->'''

FONT_IMPORT = "@import url('https://cdn.jsdelivr.net/npm/@fontsource-variable/plus-jakarta-sans/index.css');"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def slug_from_filename(name: str) -> str:
    base = os.path.splitext(os.path.basename(name))[0]
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")

def banned_color_pass(html: str) -> str:
    for c in BANNED_COLORS_TO_NAVY:
        html = html.replace(c, MCAS_NAVY)
    for c in BANNED_COLORS_TO_CREAM:
        html = html.replace(c, MCAS_CREAM)
    return html

def ensure_body_class(html: str) -> str:
    """Add 'mcas-page' to <body class="..."> exactly once, deduping any
    repeats from past --force runs and trimming whitespace."""
    def repl(m):
        attrs = m.group(1) or ""
        if re.search(r'\bclass\s*=', attrs, flags=re.IGNORECASE):
            def fix_class(mm):
                tokens = mm.group(1).split()
                if "mcas-page" not in tokens:
                    tokens.append("mcas-page")
                seen = []
                for t in tokens:
                    if t and t not in seen:
                        seen.append(t)
                return 'class="' + " ".join(seen) + '"'
            new_attrs = re.sub(r'class\s*=\s*"([^"]*)"', fix_class, attrs, count=1, flags=re.IGNORECASE)
            return f"<body{new_attrs}>"
        else:
            return f"<body{attrs} class=\"mcas-page\">"
    return re.sub(r"<body([^>]*)>", repl, html, count=1, flags=re.IGNORECASE)

def inject_style_overrides(html: str) -> str:
    """Append MCAS_OVERRIDE_CSS to the first <style> block, or create one in
    <head>. Normalizes surrounding whitespace so --force re-runs don't
    accumulate blank lines."""
    style_match = re.search(r"(<style[^>]*>)(.*?)(</style>)", html, flags=re.DOTALL | re.IGNORECASE)
    if style_match:
        opening, body, closing = style_match.group(1), style_match.group(2), style_match.group(3)
        # Normalize: strip surrounding whitespace before re-composing so
        # --force re-runs don't accumulate blank lines inside <style>.
        body = body.strip()
        # Add font import at the very top if missing (dedup: keep one)
        if FONT_IMPORT not in body:
            body = FONT_IMPORT + "\n" + body
        new_block = opening + "\n" + body + "\n\n" + MCAS_OVERRIDE_CSS.strip() + "\n" + closing
        return html[:style_match.start()] + new_block + html[style_match.end():]
    head_match = re.search(r"</head>", html, flags=re.IGNORECASE)
    if head_match:
        insertion = f"<style>\n{FONT_IMPORT}\n{MCAS_OVERRIDE_CSS.strip()}\n</style>\n"
        return html[:head_match.start()] + insertion + html[head_match.start():]
    return html  # malformed page; leave alone

def wrap_body_with_chrome(html: str, filename: str) -> str:
    """Insert MCAS chrome right after <body ...> and just before </body>.

    If the page already carries its own branded header element
    (page-head, site-header, banner, masthead, etc.), inject only a
    thin back-link strip so the brand is not duplicated. Otherwise
    inject the full MCAS header with logo.

    The back-link points to index.html#week-N for spoke pages and
    plain index.html for course-wide pages."""
    back_href = back_link_target(filename)
    wk = week_for_filename(filename)
    back_label = f"Course home (Week {wk})" if wk else "Course home"
    if page_has_existing_branded_header(html):
        header = mcas_backlink_only_html(back_href, back_label)
    else:
        header = mcas_header_full_html(back_href, back_label)
    html = re.sub(
        r"(<body[^>]*>)",
        lambda m: m.group(1) + "\n" + header + "\n",
        html, count=1, flags=re.IGNORECASE,
    )
    html = re.sub(
        r"(</body>)",
        MCAS_FOOTER_HTML + "\n" + r"\1",
        html, count=1, flags=re.IGNORECASE,
    )
    return html

def rewrite_targets(html: str) -> str:
    """target=_top for internal/relative/same-domain links, target=_blank rel=noopener for external."""
    def fix_anchor(m):
        tag = m.group(0)
        # Already has target?
        if re.search(r'\btarget\s*=', tag, flags=re.IGNORECASE):
            return tag
        href_m = re.search(r'href\s*=\s*"([^"]*)"', tag, flags=re.IGNORECASE)
        if not href_m:
            return tag
        href = href_m.group(1).strip()
        if not href or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:") or href.startswith("tel:"):
            return tag
        is_external = bool(re.match(r'^https?://', href, flags=re.IGNORECASE))
        same_domain = "drsrennie-stack.github.io" in href or "github.com/drsrennie-stack" in href
        if is_external and not same_domain:
            # External
            new_tag = re.sub(r"<a\b", '<a target="_blank" rel="noopener"', tag, count=1, flags=re.IGNORECASE)
        else:
            new_tag = re.sub(r"<a\b", '<a target="_top"', tag, count=1, flags=re.IGNORECASE)
        return new_tag
    return re.sub(r"<a\b[^>]*>", fix_anchor, html, flags=re.IGNORECASE)

def inject_height_sender(html: str, filename: str) -> str:
    # Sentinel guard: strip_previous_mcas_chrome already removed prior MCAS
    # sender, so this fires unconditionally. Existing non-MCAS resize code in
    # the page (if any) is left alone.
    if HEIGHT_OPEN_TAG in html:
        return html
    slug = slug_from_filename(filename)
    sender = HEIGHT_SENDER_TEMPLATE.format(slug=slug)
    return re.sub(r"</body>", sender + "\n</body>", html, count=1, flags=re.IGNORECASE)

def strip_sketch_section(html: str) -> str:
    """Remove the legacy 'Sketch & synthesis' notes-block from spoke pages.
    Per Shar's direction: spoke pages don't need an in-page sketch area
    because the printed weekly workbook already provides space for it.

    Targets the canonical pattern only:
        <section class="notes-block" ...>
          ...
          <div class="sketch-space" ...></div>
        </section>
    Counts <section>/</section> tokens to handle nesting correctly. Only
    removes notes-block sections that actually contain a sketch-space
    div, so any other notes-block on the page is preserved. Safe on
    pages without the section (no-op)."""
    sec_re  = re.compile(r'<section\b[^>]*class="[^"]*\bnotes-block\b[^"]*"[^>]*>', re.IGNORECASE)
    sec_tok = re.compile(r'<(/?)section\b[^>]*>', re.IGNORECASE)

    ranges = []
    for m in sec_re.finditer(html):
        start = m.start()
        depth = 0
        end = None
        for tm in sec_tok.finditer(html, start):
            if not tm.group(1):
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end = tm.end()
                    break
        if end is None:
            continue
        block = html[start:end]
        if 'class="sketch-space"' not in block and "class='sketch-space'" not in block:
            continue
        # Consume trailing whitespace to avoid leaving an empty gap
        trailing = re.match(r'\s*', html[end:])
        if trailing:
            end += trailing.end()
        ranges.append((start, end))

    # Apply removals back-to-front so positions don't shift
    for start, end in reversed(ranges):
        html = html[:start] + html[end:]
    return html


def upgrade_workbook_aside(html: str) -> str:
    """Upgrade legacy <aside class="mcas-next-up"> blocks (from earlier
    wiring passes) to the gated form: add `is-gated` class and a
    `mcas-next-up-gate-hint` span. Idempotent — if the aside already has
    `is-gated`, no change."""
    # Skip if every aside on the page is already gated
    if 'class="mcas-next-up "' not in html and 'class="mcas-next-up"' not in html:
        return html
    aside_re = re.compile(
        r'<aside\s+class="mcas-next-up"\s+(aria-label="[^"]*">\s*'
        r'<p\s+class="mcas-next-up-eyebrow">[^<]+</p>\s*'
        r'<a\s+class="mcas-next-up-cta"[^>]*>[^<]*<span[^>]*>[^<]+</span></a>)\s*'
        r'</aside>',
        re.IGNORECASE,
    )
    def repl(m):
        return (
            '<aside class="mcas-next-up is-gated" '
            + m.group(1)
            + '\n  <span class="mcas-next-up-gate-hint" id="mcas-next-up-gate-hint" hidden>Unlocks after the retrieval check</span>\n'
            + '</aside>'
        )
    return aside_re.sub(repl, html)


def inject_lecture_notes_script(html: str) -> str:
    """Strip any prior lecture-notes injector script, then inject the
    current one just before </body>. Always safe — script is a no-op
    on pages without a video-panel.

    Uses a lambda for replacement to avoid re.sub's backreference parsing
    interpreting `\\w` (which appears inside the injected JS regex) as a
    bad escape sequence."""
    html = re.sub(
        r'\s*' + re.escape(LECNOTES_OPEN_TAG) + r'.*?' + re.escape(LECNOTES_CLOSE_TAG) + r'\s*',
        '\n', html, flags=re.DOTALL,
    )
    return re.sub(
        r'(</body>)',
        lambda m: LECTURE_NOTES_INJECTOR + '\n' + m.group(1),
        html, count=1, flags=re.IGNORECASE,
    )


def inject_workbook_gate_script(html: str) -> str:
    """Strip any prior workbook-aside-gate script (by sentinel), then
    inject the current one just before </body>. Only injects on pages
    that carry a .mcas-next-up workbook aside — other pages get nothing.
    The script itself is a no-op on pages without window.SHEET_CONFIG, so
    even spoke pages without the bio304-option-a IIFE are safe.

    Uses a lambda for replacement (see inject_lecture_notes_script note)."""
    html = re.sub(
        r'\s*' + re.escape(WBGATE_OPEN_TAG) + r'.*?' + re.escape(WBGATE_CLOSE_TAG) + r'\s*',
        '\n', html, flags=re.DOTALL,
    )
    if 'class="mcas-next-up' not in html:
        return html
    return re.sub(
        r'(</body>)',
        lambda m: WORKBOOK_GATE_SCRIPT + '\n' + m.group(1),
        html, count=1, flags=re.IGNORECASE,
    )


def stamp_marker(html: str) -> str:
    if MARKER_ANY.search(html):
        html = MARKER_ANY.sub(MARKER, html, count=1)
    else:
        html = re.sub(r"(<head[^>]*>)", lambda m: m.group(1) + "\n" + MARKER, html, count=1, flags=re.IGNORECASE)
    return html

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def process_file(path: Path, dry_run: bool, force: bool) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if not force and MARKER_ANY.search(raw):
        return "skip-marker"
    html = raw
    # Strip ANY previous MCAS chrome first so re-runs never stack.
    html = strip_previous_mcas_chrome(html)
    # Also strip any previously appended MCAS override CSS so re-runs don't
    # accumulate duplicate override blocks at the end of <style>.
    html = re.sub(
        r"/\* =+\s*MCAS REBRAND OVERRIDES.*?(?=</style>)",
        "", html, flags=re.DOTALL,
    )
    html = banned_color_pass(html)
    html = strip_sketch_section(html)
    html = inject_style_overrides(html)
    html = ensure_body_class(html)
    html = wrap_body_with_chrome(html, path.name)
    html = rewrite_targets(html)
    html = upgrade_workbook_aside(html)
    html = inject_workbook_gate_script(html)
    html = inject_lecture_notes_script(html)
    html = inject_height_sender(html, path.name)
    html = stamp_marker(html)
    if html == raw:
        return "no-change"
    if dry_run:
        return "would-update"
    path.write_text(html, encoding="utf-8")
    return "updated"

def should_process(name: str, only: str | None) -> bool:
    if only:
        return name == only
    if not name.endswith(".html"):
        return False
    if name in SKIP_FILES:
        return False
    if any(name.startswith(p) for p in SKIP_PREFIXES):
        return False
    return True

def main():
    ap = argparse.ArgumentParser(description="MCAS bulk rebrand for BIO 304 nonmajors")
    ap.add_argument("repo_dir", help="Path to local clone of drsrennie-stack/nonmajors")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default=None, help="Process only this filename")
    args = ap.parse_args()

    root = Path(args.repo_dir).resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(2)

    counts = {"updated": 0, "skip-marker": 0, "no-change": 0, "would-update": 0, "skipped": 0}
    for name in sorted(os.listdir(root)):
        if not should_process(name, args.only):
            counts["skipped"] += 1
            continue
        path = root / name
        try:
            r = process_file(path, args.dry_run, args.force)
        except Exception as e:
            print(f"ERROR {name}: {e}", file=sys.stderr)
            continue
        counts[r] = counts.get(r, 0) + 1
        print(f"{r:14s}  {name}")

    print("\nSummary:")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print(f"\nMarker: {MARKER}")
    if args.dry_run:
        print("(dry run — no files written)")

if __name__ == "__main__":
    main()
