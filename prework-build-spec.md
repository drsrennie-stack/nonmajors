# BIO 304 Pre-Work Build Spec

The single standard for building every week's pre-work, so weeks 2 through 8 are assembled exactly like Week 1. Author: Dr. Sharilyn Rennie. Course: BIO 304, American River College (online). Repo: drsrennie-stack/nonmajors.

---

## 1. The model in one paragraph

Cards are never locked behind watching a video. Access is controlled by date: a topic opens on its assigned day, the same way the index already opens each week (the `data-unlock` date stamp). Watching is handled separately, by the grade: each topic's YouTube video is measured for how much was genuinely watched, and that feeds the engagement report. No student ever gets locked out for switching devices, because a date is the same on every device.

---

## 2. Two things kept separate

**Access = the calendar.** A topic's pages and cards open on its release date and stay open after (so anyone catching up still gets in). Nothing about watching gates access.

**Accountability = the grade.** The video tracker records the true percentage watched per video. The engagement report turns that, plus card practice, into a participation score.

---

## 3. Video rules

- Host on **YouTube, unlisted** (not Loom). Loom cannot report watch percentage to the page; YouTube can. Unlisted means link-only, not searchable.
- Embed with **`video-tracker.js`** using a mount div per video:
  ```html
  <div class="video-tracker" data-youtube="VIDEO_ID" data-topic="t-TOPIC-ID" data-threshold="98"></div>
  <script src="video-tracker.js" defer></script>
  ```
- **Threshold = 98%.** At or above 98% watched counts as fully watched.
- **Multi-video topics** (e.g. Homeostasis, 5 videos): one mount div per video, each with its own `data-topic` sub-id. Each video is measured and graded on its own.
- The tracker is **scrub-proof**: dragging to the end does not fill the skipped part.
- It writes two values per video to the browser: `bio304-video-<id>` (met threshold yes/no) and `bio304-videopct-<id>` (highest true percent).

### Which topics are tracked

| Topic | Tracked? | Reason |
|-------|----------|--------|
| Day 1 (Levels of Organization; Terminology, Regions & Cavities) | No | Catch-up window; already covered |
| Homeostasis & Feedback (Day 2, today's assignment) | No | Catch-up day |
| Cell Structure onward, and every later week | Yes | Tracked from here to end of course |

Untracked pages set `track: false` in their `SHEET_CONFIG` (no watch gate, no measurement). Tracked pages omit it (default on) and use `video-tracker.js`.

---

## 4. Grading model (per unit)

Each unit is worth a set number of points, split into two portions:

- **Video portion** = `____%` of the unit (fill in your split, e.g. 40%).
- **Spaced-recall portion** = `____%` of the unit (e.g. 60%). The two add to 100%.

**Video credit.** The video portion is divided evenly across that unit's videos. Each video watched to **98% or above** earns its slice; each one below 98% forfeits its slice.
> Example: video portion 40%, unit has 5 videos, student hits 98%+ on 4 of them, video credit = 40% × (4 / 5) = 32%.

**Cards credit.** At end of week, take the percentage the student earned on that unit's cards and multiply by the spaced-recall portion.
> Example: spaced-recall portion 60%, student earned 80% on the cards, cards credit = 60% × 80% = 48%.

**Unit participation score = video credit + cards credit.** (Example total: 32% + 48% = 80%.)

> To finalize: tell me the video/cards split (and whether it's the same for every unit), and how "percentage earned on the cards" is defined (cards completed ÷ total, or mastery to a DOK level). I'll wire the report to compute it exactly.

---

## 5. Spoke (topic) page checklist

Every topic page is built the same way:

1. **No hard lock.** Prework and workbook buttons are always live links.
2. **Video:** tracked topics use `video-tracker.js` (section 3); untracked set `track: false`.
3. **Optional explain-back** stays as ungraded retrieval practice, never a gate.
4. **Prework button** links to the cards page with the topic anchor: `bio304-spaced-recall-prototype.html#topic=t-TOPIC-ID`.
5. **Schedule back-link** points to that week's hub (`weekNN_prework.html`).
6. House rules (from global instructions): MCAS palette only (no sage/cream), WCAG 2.2 AA minimum, no em dashes, student-facing byline "Dr. Sharilyn Rennie", iframe height-sender before `</body>`, `target="_top"` on internal links, external links `target="_blank" rel="noopener"`.

---

## 6. Weekly hub (`weekNN_prework.html`) checklist

- One day card per teaching day; each topic row has an "Open topic" pill to its spoke page and a "Submit lab" pill to the Canvas assignment.
- Topic pill `href` matches the spoke page's actual filename.
- (Optional, date-release) give each day card a `data-unlock` date so topics open on their day, mirroring the index.

---

## 7. Index (`index.html`)

Already done and working: each week card carries a `data-unlock` date and locks until then. Add new weeks the same way. This is the date-release mechanism, extended downward where wanted.

---

## 8. Reusable assets (build once, reuse everywhere)

| File | Purpose |
|------|---------|
| `video-tracker.js` | YouTube watch-percentage tracker (scrub-proof). Drop-in per video. |
| `sync.js` | Cross-device backup/restore of card progress (no server, no stored PII). Optional, for the "lost my progress on another device" case. |
| `bio304-spaced-recall-prototype.html` | The cards app + engagement report. One small change pending so it reads the per-video percentages. |

---

## 9. Per-topic config table (fill in as videos are recorded)

| Week | Day | Topic | `t-` id | YouTube ID(s) | Tracked | Release date |
|------|-----|-------|---------|---------------|---------|--------------|
| 1 | 1 | Levels of Organization | t-levels-of-organization | ZBAMA73bjaw | No | 2026-06-08 |
| 1 | 1 | Terminology, Regions & Cavities | t-... | (none / notes) | No | 2026-06-08 |
| 1 | 2 | Homeostasis & Feedback | t-homeostasis | ONrXuf-ayXs, hXCHCodDwSw, Z_eIHsdQILY, Uyo0z0XIllo, vyGXjbd4qPk | Yes | 2026-06-09 |
| 1 | 3 | Cell Structure & Organelles | t-cell-structure | tNmaROCmMxM | Yes | 2026-06-11 |
| 1 | 4 | Membrane Transport | t-membrane-transport | B2ww2P8itW4 | Yes | 2026-06-12 |
| 2+ | … | … | … | (drop in when recorded) | Yes | … |

When a later-week video is recorded, the page can already be live with the tracker wired; just paste the new YouTube ID into its mount div.

---

*Last updated as part of the Week 1 build. Revise the grading split (section 4) and the report will follow.*
