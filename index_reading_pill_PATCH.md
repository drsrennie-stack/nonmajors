# Hub patch: add a "Reading" pill to each week card

Two changes to `index.html`. Both are additive. Nothing existing is removed, and the
date-gating JavaScript is untouched (the new pill is a `.week-pill`, so it locks and
unlocks with its week automatically, exactly like Workbook / Pre-work / Discussion / Notes).

---

## Change 1 of 2 — add the pill style

Find the `.week-pill-notes` hover rule (around line 303 to 308). Paste this block
immediately **after** it:

```css
/* Reading pill: white with a gold outline, marks the week's textbook reading */
.week-pill-reading {
  background: #FFFFFF;
  color: #0B1530;
  border: 1px solid #C9A14A;
}
.week-pill-reading:hover, .week-pill-reading:focus-visible {
  background: #C9A14A;
  color: #0B1530;
}
```

---

## Change 2 of 2 — add one pill to each week card

In each week card, add the matching line below as the **last** pill inside that week's
`<div class="week-actions"> ... </div>` (right after the existing `Notes` pill).
The href week number must match the card, so each line is different.

```html
<!-- Week 1 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-1" target="_top">Reading</a>

<!-- Week 2 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-2" target="_top">Reading</a>

<!-- Week 3 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-3" target="_top">Reading</a>

<!-- Week 4 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-4" target="_top">Reading</a>

<!-- Week 5 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-5" target="_top">Reading</a>

<!-- Week 6 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-6" target="_top">Reading</a>

<!-- Week 7 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-7" target="_top">Reading</a>

<!-- Week 8 -->
<a class="week-pill week-pill-reading" href="biol304_reading_map.html#week-8" target="_top">Reading</a>
```

That is the whole change. Each Reading pill opens the reading map scrolled to that
week's card, and each week card on the reading map links back to `index.html#week-N`.

Dr. Sharilyn Rennie
