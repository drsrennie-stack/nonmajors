# BIO 304 MCAS Rebrand — Handoff for next chat

**Repo:** `https://github.com/drsrennie-stack/nonmajors` (Dr. Sharilyn Rennie / ARC BIO 304, online, summer 2026)
**Working folder:** `/Users/sharilynrennie/Documents/Claude/Projects/Non Majors Branding Course/`
**Current rebrand-mcas.py version:** v5 (v6 fix started but not finished — see "What's broken" below)
**User constraint:** not comfortable running terminal commands. The script needs to either work from chat or the user uploads a zip.

---

## Brand spec (MCAS, per Project Update 2026-05-29)

- **Navy** `#0B1530` — primary text on light, brand mark
- **Rust** `#8B3A2E` — accent on LIGHT sections, CTAs, hover hits `#A0452F`
- **Gold** `#C9A14A` — accent on DARK sections only (fails contrast on light)
- **Cream** `#F5F1E8` — text on dark sections, occasional tint background
- **Dark** `#060A18` — dark section background
- **White** `#FFFFFF` — card backgrounds, primary page background
- **Font:** Plus Jakarta Sans Variable (everywhere; no Lora, no DM Sans, no Cormorant, no serif fallback for body)
- **Code blocks:** keep monospace (`code`, `pre`, `kbd`, `samp`, `tt` are exempt from the Jakarta wildcard)

## Brand rules (enforced in the override CSS)

1. **No bookend borders.** No top/bottom border lines on sections. Section differentiation is background contrast only (white / cream / dark navy).
2. **Hover-lift only on real links.** `a[class*="-card"]`, `a[class*="-tile"]`, `details.faq-item` get a 2px translate + 8/16 shadow. Read-only info (`.glance-item`, plain `<div>` panels) never lifts and never changes cursor.
3. **Course at a Glance is one info box** (white background, thin shadow, no per-item card styling). Not eight clickable-looking tiles.
4. **No teal anywhere.** `#2F4F4F`, `#008080`, `#5F9EA0`, etc. all auto-rewrite to navy.
5. **No sage anywhere.** Sage hexes auto-rewrite to gold (which works because sage was only used on dark backgrounds).
6. **WCAG 2.2 AA floor, AAA where achievable.** All structural pairs verified AAA. See `compliance-notes.md`.
7. **Every internal/same-domain link:** `target="_top"`. Every external link: `target="_blank" rel="noopener"`.
8. **iframe height-sender** baked into every page so Canvas embeds resize to content.

## Course structure (canonical, from the syllabus)

- 8 weeks, June 8 – August 2, 2026, fully online, asynchronous
- Weekly rhythm: M/T/Th/F pre-work days, Wednesday catch-up + discussion, Friday→Sunday quiz window
- **Pre-work** = reading + fill-in-the-blank notes + video + flashcards. ONE entry point: `bio304-spaced-recall-prototype.html` (anchored per topic or per week)
- **Grading:** 40% pre-work engagement / 30% lab workbooks / 10% discussions / 20% quizzes. No curves, no extra credit.
- **Hard deadlines:** Friday 11:59 PM (initial discussion post, quiz opens) and Sunday 11:59 PM (replies + workbooks + quiz closes)
- **Carnegie hours:** ~22–24/week total (8–10 instruction equivalent + 12–15 outside study)
- **Textbook:** OpenStax A&P 2e (free)
- **Quizzes:** Honorlock-proctored, 20q in 20min, one attempt
- **AI Honor Contract** due Tuesday, June 9, 2026

---

## What's in the folder (deliverables)

### Hand-built MCAS-native pages (source of truth, NEVER touched by the rebrand script)

| File | Purpose |
|---|---|
| `canvas-home.html` | Canvas course home front door. Brief welcome + one big "Enter the course" button → hub. |
| `index.html` | The hub. 8-week grid (anchored `#week-1`–`#week-8`), weekly rhythm, grading, hard deadlines, tools strip, FAQ, about, footer. Every spoke page links back here at the correct week. |
| `ai_policy.html` | The AI policy explainer. Allowed-vs-not cards, why the policy is strict, four detection methods, link to contract. |
| `ai_honor_contract.html` | The signed agreement. Six numbered commitments, consequences block, working signature form with print stylesheet. |

### Rebranded via script (re-runnable)

| File | Status |
|---|---|
| `biol304_syllabus.html` | Rebranded v5. Lora purged manually. **Has the orphan close-tag bug — needs v6 fix.** |
| `schedule.html` | Rebranded v5. Lora purged manually. **Same orphan close-tag bug.** |
| `week-1-checklist.html` | EXISTS but user said fold into hub instead. Should be deleted (Cowork file-delete permission needed) or marked retired. |

### The rebrand kit

| File | Purpose |
|---|---|
| `rebrand-mcas.py` | v5 bulk script. v6 partially started in the source (marker version bumped, sentinel comments added, `strip_previous_mcas_chrome` added) but the strip regex still uses lazy `.*?</div>` which doesn't handle nested divs correctly. |
| `iframes.md` | Canvas embed snippets — parent-side listener + per-page iframes. |
| `compliance-notes.md` | WCAG 2.2 audit, contrast ratios, sign-off log. |
| `README-rebrand.md` | How to run the script (terminal). User won't run this — zip workflow needed instead. |

---

## Architecture decisions made

1. **Two entry points consolidated.** Pre-work is the only destination for topic clicks (hub week-card buttons, syllabus pre-work pills, schedule pre-work pills) — all point to `bio304-spaced-recall-prototype.html#week=N` or `#topic=t-{slug}`.
2. **Course orientation page being retired.** User agreed. Was duplicating the syllabus. Replaced (or to-be-replaced) with action-only Week 1 onboarding.
3. **Week 1 Checklist folded into the hub.** User's most recent direction. Instead of a separate `week-1-checklist.html` page, integrate the 6 setup tasks (read syllabus, sign AI contract, Honorlock setup, Day 1 pre-work, Day 1 workbook, Week 1 discussion) as a section in `index.html`. **NOT DONE YET.**
4. **AI page split.** One combined page was split into `ai_policy.html` (explainer) + `ai_honor_contract.html` (the signed agreement).
5. **Anchored back-links.** Each spoke page's "← Course home (Week N)" link routes to the right week card on the hub. Mapping in `rebrand-mcas.py`'s `TOPIC_WEEK_MAP` + regex matchers for `workbook_dayNN_*`, `weekNN_*`, `_OBSOLETE_*weekN*`.
6. **`_OBSOLETE_*` files ARE active.** The prefix is misleading. The script rebrands them and routes their back-links correctly.

---

## What's broken (needs fixing in the next chat)

### 1. Chrome-stacking + orphan close tags (URGENT — blocking the syllabus and schedule)

**Symptom:** After multiple `--force` runs, `biol304_syllabus.html` and `schedule.html` have:
- `<body class="mcas-page mcas-page mcas-page mcas-page">` (class duplicated 4x)
- A run of orphan `</div></header></div></header></div>` close tags between the MCAS chrome and the page's own `header.page-head`
- DOM tree is corrupted, brand may appear missing

**Root cause:** `strip_previous_mcas_chrome` in `rebrand-mcas.py` uses regex `<div class="mcas-chrome">.*?</div>` which lazy-matches the FIRST `</div>` (the inner one), leaving the outer wrapper's `</div>` orphaned. Each `--force` run leaves a new orphan layer.

**Fix needed (v6):**
- Wrap ALL injected chrome in sentinel comments (`<!-- mcas-chrome-header --><!-- mcas-chrome-header-end -->`, ditto for footer and height-sender) — STARTED in source
- Strip only by sentinel-pair matching (never by `</div>` lookahead)
- For pre-sentinel legacy chrome: write a counter-based nested-div matcher (manual parser, not regex)
- Add a one-time corrective pass: between `<body...>` and the first `<a class="skip-link">` or `<header class="page-head">` etc., strip any sequence of orphan `</div>` / `</header>` tags
- Fix `ensure_body_class` to only add `mcas-page` if not already present
- Then re-run `--force` on syllabus and schedule

### 2. The other ~160 repo pages still aren't rebranded

The script handles only `biol304_syllabus.html`, `schedule.html`, and `week-1-checklist.html` so far. Every other page (discussions, concept videos, all topic pages, all workbooks, all `_OBSOLETE_*`, all policy pages) is still on the old branding.

**Path forward (user-friendly):**
- User downloads the repo as a ZIP from GitHub (Code button → Download ZIP)
- User drops the zip into the next chat
- Next chat unzips, runs `rebrand-mcas.py` (after v6 fix) on the whole folder, re-zips, hands back
- User drag-and-drops the rebranded files back to GitHub via the web UI

### 3. Standalone `week-1-checklist.html` should be folded into the hub

Per user's direction in this chat. Action:
- Add a "First steps" section to `index.html` between the glance panel and "How to thrive" with the 6 setup tasks as a numbered list (each a real link)
- Delete `week-1-checklist.html` (Cowork file-delete permission needed via `mcp__cowork__allow_cowork_file_delete`)
- Update any references in `iframes.md` and README

### 4. Lora references in compliance-notes.md (low priority — documentation only)

The doc says "Lora is not used in this course" — that's commentary explaining a rule, not a styling issue. Fine to leave or rewrite for clarity.

---

## Iframe embed pattern (Canvas)

Parent-side listener (paste once per Canvas page):

```html
<script>
(function(){
  window.addEventListener('message', function (e) {
    if (!e.data || e.data.type !== 'resize' || !e.data.id) return;
    var f = document.getElementById(e.data.id);
    if (f) f.style.height = e.data.height + 'px';
  }, false);
})();
</script>
```

Per-page iframe template (FRAME_ID = `bio304-{slug}` where slug is the filename without extension, lowercased, hyphens):

```html
<iframe
  id="bio304-{slug}"
  src="https://drsrennie-stack.github.io/nonmajors/{filename}.html"
  title="BIO 304 — {Human Title}"
  loading="lazy"
  style="width:100%; border:0; display:block; min-height:600px;"
  scrolling="no"
></iframe>
```

Full per-keystone snippets are in `iframes.md`.

---

## Open user clarifications (would help to know)

- **Deadline cards (3 dark cards on the hub):** user flagged that they look clickable but aren't. Same fix as the glance section (strip clickable affordance) — not done yet.
- **Course map page (the third entry point with `OPEN SHEET →` topic cards):** user wants every topic link to lead to pre-work. The course-map's individual topic OPEN SHEET buttons should repoint to `bio304-spaced-recall-prototype.html#topic=t-{slug}` — not done yet.
- **Tools cards on the hub** are intentionally clickable (link to study tools); those should keep hover-lift.

---

## Quick-start prompt for the next chat

> I'm continuing the BIO 304 MCAS rebrand for `drsrennie-stack/nonmajors`. Working folder is `/Users/sharilynrennie/Documents/Claude/Projects/Non Majors Branding Course/`. Read `HANDOFF.md` first. The most urgent fix is the orphan close-tag bug in `rebrand-mcas.py` v5 — I need v6 implemented: sentinel-pair chrome stripping, counter-based nested-div matcher for legacy chrome, dedupe on body class, plus a corrective pass for already-broken files. After that, fold the Week 1 Checklist into `index.html` as a section and retire the standalone file. I won't be running terminal commands — process everything in chat. I'll upload the repo as a zip when ready for the bulk rebrand of the remaining ~160 pages.
