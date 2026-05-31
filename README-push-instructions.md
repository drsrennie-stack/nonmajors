# BIO 304 — Phase B v2 (corrective push)

**Problem found after v1 push:** Buttons were added to workbooks, lab sprints, weekly trainers, portfolio templates, and obsolete archive pages — not just lecture pages. You only want buttons on lecture pages (the ones that match your videos).

**This bundle fixes it.** Push it as a new commit; the bad buttons disappear from non-lecture pages and the good buttons stay on lecture pages.

## What's in this bundle (112 files)

- **110 non-lecture pages** restored to their original (pre-v1) state. Pushing these overwrites the buttoned versions on GitHub, removing the misplaced buttons from workbooks, sprints, trainers, portfolio templates, weekly worksheets, and `_OBSOLETE_*` archives.
- **2 lecture pages** that v1 missed (`workbook-index.html` and `_OBSOLETE_biol304_week1_overview.html`) — they get just the script tag with no buttons. Edge case, not critical.
- Lecture pages that were correctly wired in v1 are NOT in this bundle. They stay as they are on GitHub.

## What this push does on GitHub

| Page type | v1 state | v2 effect |
|---|---|---|
| Lecture pages (109) | Had correct buttons | **Unchanged** (not in this bundle) |
| Workbooks, sprints, trainers, portfolios (110) | Had wrong buttons | **Buttons removed** |
| Admin pages (93) | Unchanged | **Still unchanged** |

## Push commands

```bash
cd /path/to/nonmajors
git checkout main
git pull origin main

cp "/Users/sharilynrennie/Documents/Claude/Projects/Lecture Slides/_PUSH-TO-GITHUB/BIO-304-PhaseB-v2/"*.html .

git status        # should show ~112 modified files
git add *.html
git commit -m "Phase B v2: remove drawing buttons from workbooks/sprints/trainers (keep on lecture pages)"
git push origin main
```

## Verify after push

Wait ~2 min, then check ONE workbook and ONE lecture:

**A workbook page (should NOT have a button after this push):**
https://drsrennie-stack.github.io/nonmajors/workbook_day30_tubular-function-and-urine-concentration.html
→ No "Drawing tools" box. Page looks like it always did.

**A lecture page (should STILL have a button — untouched by this push):**
https://drsrennie-stack.github.io/nonmajors/tubular-function.html
→ "Draw the nephron tubular function" button still there.

If both check out, the correction worked.
