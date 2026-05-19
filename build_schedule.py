"""
Generate schedule.html: the full 8-week BIO 304 schedule hub.
- All 8 weeks rendered as cards
- Auto-detect today via JS; highlight current week + today's row
- Status-now banner adapts based on date (pre-term / today / between weeks / post-term)
- Per-topic pills (Pre-work, Lab workbook) + small SR/DR badges
- Pulls topics from course-content.js
- For each topic, Pre-work routes to lecture page (every topic has one now)

Outputs: schedule.html
"""

import json
import os
import subprocess
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_START = date(2026, 6, 8)  # Monday week 1
# Slot index (0-3) → (label, monday-offset)
SCHED_PATTERN = [
    ("Monday",   0),
    ("Tuesday",  1),
    ("Thursday", 3),
    ("Friday",   4),
]


def load_course():
    proc = subprocess.run(
        ["node", "-e",
         "const w={};new Function('window',require('fs').readFileSync('course-content.js','utf8'))(w);"
         "console.log(JSON.stringify(w.BIO304_COURSE_CONTENT))"],
        cwd=HERE, capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


WEEK_THEMES = {
    1: "Foundations . Cell . Tissues start",
    2: "Tissues . Integumentary",
    3: "Skeletal system",
    4: "Muscle . Nervous start",
    5: "Nervous . Special senses . Endocrine start",
    6: "Endocrine . Blood . Cardiovascular",
    7: "Lymphatic . Immune . Respiratory . GI",
    8: "Urinary . Reproductive",
}


def fmt_date(d):
    return d.strftime("%b %-d")


def fmt_iso(d):
    return d.isoformat()


def workbook_filename(day_num, topic):
    slug = topic["id"].replace("t-", "").replace("_", "-")
    # Match the workbook filename convention used in /workbook_dayNN_<slug>.html
    # Some topic IDs differ from workbook slugs. The repo's workbook filenames
    # follow: workbook_day{NN}_{slugified-title}.html
    title_slug = topic["title"].lower()
    title_slug = title_slug.replace("&", "and")
    import re as _re
    title_slug = _re.sub(r"[^a-z0-9]+", "-", title_slug).strip("-")
    return f"workbook_day{day_num:02d}_{title_slug}.html"


def prework_url(topic):
    if topic.get("lecturePageUrl"):
        return topic["lecturePageUrl"]
    return f"bio304-spaced-recall-prototype.html#topic={topic['id']}"


def render_topic_block(topic, day_num, is_secondary=False):
    """Render one topic's title + pills (Pre-work + SR + Lab workbook)."""
    title = topic["title"]
    pre = prework_url(topic)
    sr = f"bio304-spaced-recall-prototype.html#topic={topic['id']}"
    lab = workbook_filename(day_num, topic)
    safe_title = title.replace('"', '&quot;')
    wrapper_open = '<div class="topic-pair">' if is_secondary else ''
    wrapper_close = '</div>' if is_secondary else ''
    return f"""{wrapper_open}
              <span class="topic-title">{title}</span>
              <div class="pill-row">
                <a class="act-pill pill-prework" href="{pre}" target="_blank" rel="noopener">Pre-work <span class="arrow">&rarr;</span></a>
                <a class="act-badge badge-sr" href="{sr}" target="_blank" rel="noopener" title="Spaced recall cards" aria-label="Spaced recall cards for {safe_title}">SR</a>
                <a class="act-pill pill-lab" href="{lab}" target="_blank" rel="noopener">Lab workbook <span class="arrow">&rarr;</span></a>
              </div>{wrapper_close}"""


def render_week_card(week, by_day, today=None):
    """Render one week card. `today` is optional date object for highlighting."""
    monday = COURSE_START + timedelta(weeks=week - 1)
    sunday = monday + timedelta(days=6)
    week_id = f"week-{week}"
    aria_label = f"Week {week}, {fmt_date(monday)} to {fmt_date(sunday)}"

    rows = []
    is_dr_url = "bio304-spaced-recall-prototype.html#review"

    # 4 pre-work day rows
    for slot_idx, (dow, offset) in enumerate(SCHED_PATTERN):
        day_num = (week - 1) * 4 + slot_idx + 1
        d = monday + timedelta(days=offset)
        topics = by_day.get(day_num, [])
        today_class = ' class="is-today"' if (today and d == today) else ''
        is_today = today and d == today

        primary = topics[0] if topics else None
        secondary = topics[1:] if len(topics) > 1 else []

        if primary:
            primary_block = render_topic_block(primary, day_num, is_secondary=False)
        else:
            primary_block = '<span class="topic-title">No topic scheduled</span>'

        secondary_blocks = "\n".join(
            render_topic_block(t, day_num, is_secondary=True) for t in secondary
        )

        today_label_html = ' <span class="today-label">Today</span>' if is_today else ''
        dt_arrow = '<span class="today-arrow" aria-hidden="true">&#9654;</span>' if is_today else ''

        rows.append(f"""          <dt{today_class}>{dt_arrow}<strong>{dow[:3]}</strong>Day {day_num}</dt>
          <dd{today_class}>
            {primary_block.strip()}{today_label_html}
            {secondary_blocks}
            <div class="pill-row" style="margin-top:10px">
              <a class="act-badge badge-dr" href="{is_dr_url}" target="_blank" rel="noopener" title="Daily review" aria-label="Daily review">DR</a>
            </div>
          </dd>""")

    # Wednesday catch-up row
    wed = monday + timedelta(days=2)
    wed_today = ' class="is-today"' if (today and wed == today) else ''
    wed_is_today = today and wed == today
    wed_arrow = '<span class="today-arrow" aria-hidden="true">&#9654;</span>' if wed_is_today else ''
    wed_today_label = ' <span class="today-label">Today</span>' if wed_is_today else ''
    week_disc = f"week{week:02d}_discussion.html"
    rows.insert(2, f"""          <dt{wed_today}>{wed_arrow}<strong>Wed</strong>Catch-up</dt>
          <dd{wed_today}>
            <span class="topic-title">Daily review + discussion{wed_today_label}</span>
            <span class="row-note">No new pre-work. Run Daily Review, post your initial discussion thoughts, finish any lab workbook still open.</span>
            <div class="pill-row">
              <a class="act-badge badge-dr" href="{is_dr_url}" target="_blank" rel="noopener" title="Daily review" aria-label="Daily review">DR</a>
              <a class="act-pill pill-discussion" href="{week_disc}" target="_blank" rel="noopener">Discussion <span class="arrow">&rarr;</span></a>
            </div>
          </dd>""")

    # Weekend row
    sat = monday + timedelta(days=5)
    sun = monday + timedelta(days=6)
    weekend_is_today = today and today in (sat, sun)
    weekend_today_class = ' class="is-today"' if weekend_is_today else ''
    weekend_arrow = '<span class="today-arrow" aria-hidden="true">&#9654;</span>' if weekend_is_today else ''
    weekend_today_label = ' <span class="today-label">Today</span>' if weekend_is_today else ''
    rows.append(f"""          <dt{weekend_today_class}>{weekend_arrow}<strong>Sat-Sun</strong>Quiz window</dt>
          <dd{weekend_today_class}>
            <span class="topic-title">Lock in the week{weekend_today_label}</span>
            <span class="row-note">Run Daily Review, take the quiz earlier rather than later, submit discussion replies and lab workbooks before Sun 11:59 PM.</span>
            <div class="pill-row">
              <a class="act-badge badge-dr" href="{is_dr_url}" target="_blank" rel="noopener" title="Daily review" aria-label="Daily review">DR</a>
              <a class="act-pill pill-quiz" href="bio304-spaced-recall-prototype.html" target="_blank" rel="noopener">Quiz check <span class="arrow">&rarr;</span></a>
            </div>
          </dd>""")

    day_list = "\n".join(rows)
    return f"""    <li class="week-card" id="{week_id}" aria-label="{aria_label}" data-week="{week}" data-start="{fmt_iso(monday)}" data-end="{fmt_iso(sunday)}">
      <div class="week-tab" aria-hidden="true">Wk {week:02d}</div>
      <div class="week-body">
        <div class="week-header" role="button" tabindex="0" aria-expanded="false" aria-controls="day-list-week-{week}">
          <div class="week-number" aria-hidden="true">{week:02d}</div>
          <div class="week-meta">
            <h2 class="week-dates">{fmt_date(monday)} to {fmt_date(sunday)}</h2>
            <p class="week-theme">{WEEK_THEMES.get(week, '')}</p>
            <div class="week-status-slot"></div>
          </div>
          <div class="week-toggle" aria-hidden="true">+</div>
        </div>
        <dl class="day-list" id="day-list-week-{week}" aria-label="Daily schedule for week {week}">
{day_list}
        </dl>
      </div>
    </li>"""


def main():
    course = load_course()
    by_day = {}
    for mod in course["modules"]:
        for t in mod["topics"]:
            by_day.setdefault(t["dayInCourse"], []).append(t)

    # Build all 8 week cards (no client-side date for the static SSR, the JS at
    # bottom of the page applies today highlighting and status banner on load)
    week_cards = "\n\n".join(render_week_card(w, by_day, today=None) for w in range(1, 9))

    html = HEAD + BANNER + OVERVIEW + STATUS_NOW + f"""
  <ol id="schedule-list" class="schedule-list" aria-label="Weekly schedule">

{week_cards}

  </ol>
""" + FOOTER + SCRIPT + TAIL

    out = os.path.join(HERE, "schedule.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    # Defensive em-dash check
    if "—" in html or "–" in html:
        raise SystemExit("Em/en dash detected in schedule.html")
    print(f"Wrote {out} ({len(html):,} bytes)")


# ============================================================================
# Static template chunks
# ============================================================================

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 Schedule . American River College</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
  --navy:#1E3D4C;--navy-deep:#142A36;
  --gold:#B8924A;--gold-deep:#9A7838;
  --terra:#D45A36;--terra-dark:#B8442B;
  --sage-dark:#4F6B57;--sage-deeper:#3F5B47;
  --white:#FFFFFF;--off-white:#FAFAF9;
  --gray-line:#CFD6DA;--gray-soft:#5C6970;
  --shadow-rest:0 1px 3px rgba(0,0,0,.08);
  --shadow-hover:0 8px 16px rgba(0,0,0,.10);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--off-white)}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:16px;color:var(--navy);line-height:1.6;-webkit-font-smoothing:antialiased}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600}
.skip-link:focus{left:0}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:4px}
@media (prefers-reduced-motion: reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}

.banner{background:var(--navy);color:var(--white);padding:48px 32px 40px}
.banner-inner{max-width:1040px;margin:0 auto;text-align:center}
.banner-eyebrow{font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 12px}
.banner-eyebrow-sep{display:inline-block;width:18px;height:1px;background:var(--gold);margin:0 12px;vertical-align:middle;opacity:.6}
.banner-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(34px,5vw,48px);font-weight:800;color:var(--white);line-height:1.05;letter-spacing:-.03em;margin:0 0 12px}
.banner-subtitle{font-family:'Lora',Georgia,serif;font-style:italic;font-size:clamp(15px,1.8vw,18px);color:#DCE3E6;max-width:640px;margin:0 auto;line-height:1.55}

main.container{max-width:1040px;margin:0 auto;padding:32px 24px 56px}

.overview-strip{background:var(--white);border:1px solid var(--gray-line);border-radius:12px;padding:16px 24px;margin:0 0 24px;box-shadow:var(--shadow-rest);display:flex;flex-wrap:wrap;justify-content:center;gap:12px 24px;font-size:13px;color:var(--navy);text-align:center;font-weight:500}
.overview-strip strong{color:var(--terra-dark);font-weight:800;font-variant-numeric:tabular-nums}
.overview-divider{color:var(--gray-line)}

.status-now{background:var(--navy);color:var(--white);border:none;border-radius:12px;padding:18px 22px;margin:0 0 28px;box-shadow:var(--shadow-rest);display:flex;align-items:center;gap:16px;flex-wrap:wrap;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.status-now[hidden]{display:none}
.status-now:hover{transform:translateY(-1px);box-shadow:var(--shadow-hover)}
.status-now-label{background:var(--gold);color:var(--navy);font-family:'DM Sans',sans-serif;font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:6px 12px;border-radius:999px;flex-shrink:0}
.status-now-text{flex:1;min-width:200px;font-size:15px;font-weight:500;line-height:1.5;color:var(--white)}
.status-now-text strong{color:var(--gold);font-weight:700}
.status-now-arrow{font-size:20px;color:var(--white);opacity:.85;flex-shrink:0;line-height:1}

.schedule-list{display:flex;flex-direction:column;gap:20px;list-style:none;padding:0;margin:0}
.week-card{background:var(--white);border:1px solid var(--gray-line);border-radius:14px;box-shadow:var(--shadow-rest);overflow:hidden;display:flex;position:relative}
.week-card.is-current{border-color:var(--terra-dark);box-shadow:0 6px 18px rgba(184,68,43,.14),0 2px 4px rgba(20,41,64,.08)}
.week-card.is-past{opacity:.6}
.week-card.is-past:hover,.week-card.is-past:focus-within{opacity:1}

.week-tab{background:var(--gold);color:var(--navy);padding:24px 14px;font-family:'DM Sans',sans-serif;font-size:11px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;writing-mode:vertical-rl;transform:rotate(180deg);text-align:center;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
.week-card.is-current .week-tab{background:var(--terra-dark);color:var(--white)}
@media (max-width:640px){.week-tab{writing-mode:horizontal-tb;transform:none;padding:10px 16px;width:100%;text-align:left}.week-card{flex-direction:column}}

.week-body{flex:1;padding:24px 28px;min-width:0}
@media (max-width:640px){.week-body{padding:20px}}

.week-header{display:flex;align-items:flex-start;gap:18px;margin:0 0 16px;flex-wrap:wrap;cursor:pointer;user-select:none}
.week-header:hover{background:transparent}
.week-header:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:6px}
.week-toggle{margin-left:auto;align-self:center;width:32px;height:32px;border-radius:50%;border:1px solid var(--gray-line);display:flex;align-items:center;justify-content:center;font-family:'DM Sans',sans-serif;font-weight:800;font-size:20px;color:var(--navy);background:var(--white);flex-shrink:0;transition:background 150ms ease,transform 150ms ease}
.week-card.is-expanded .week-toggle{background:var(--navy);color:var(--white);border-color:var(--navy)}
.week-card.is-current .week-toggle{background:var(--terra-dark);color:var(--white);border-color:var(--terra-dark)}
.week-card:not(.is-expanded) .day-list{display:none}
.week-card:not(.is-expanded) .week-header{margin-bottom:0}
.week-card:not(.is-expanded) .week-body{padding-bottom:24px}
.week-number{font-family:'Plus Jakarta Sans',sans-serif;font-size:38px;font-weight:800;color:var(--terra-dark);line-height:.95;letter-spacing:-.03em;font-variant-numeric:tabular-nums;flex-shrink:0}
.week-meta{flex:1;min-width:200px}
.week-dates{font-family:'Plus Jakarta Sans',sans-serif;font-size:22px;font-weight:700;color:var(--navy);line-height:1.2;letter-spacing:-.015em;margin:0 0 4px}
.week-theme{font-family:'DM Sans',sans-serif;font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gray-soft);margin:0}
.week-status-slot{margin-top:8px}
.week-status-pill{display:inline-block;font-family:'DM Sans',sans-serif;font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:5px 11px;border-radius:999px;font-variant-numeric:tabular-nums}
.week-status-pill.is-current{background:var(--terra-dark);color:var(--white)}
.week-status-pill.is-next{background:var(--gold);color:var(--navy)}

.day-list{display:grid;grid-template-columns:auto 1fr;column-gap:18px;row-gap:14px;padding:16px 0;border-top:1px solid var(--gray-line);border-bottom:1px solid var(--gray-line)}
.day-list dt{font-family:'DM Sans',sans-serif;font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gray-soft);padding-top:6px;font-variant-numeric:tabular-nums;line-height:1.3}
.day-list dt strong{display:block;color:var(--navy);font-size:13px;font-weight:800;letter-spacing:.1em;margin-bottom:2px}
.day-list dd{font-size:15px;color:var(--navy);line-height:1.45;font-weight:500;margin:0}
.day-list .topic-title{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:var(--navy);font-size:15.5px;display:block;margin-bottom:6px}
.day-list .topic-pair{display:block;margin-top:10px;padding-top:8px;border-top:1px dashed var(--gray-line)}
.day-list .row-note{font-family:'Lora',Georgia,serif;font-style:italic;color:var(--gray-soft);font-size:14px;margin-top:2px;display:block}

.day-list dt.is-today,.day-list dd.is-today{position:relative}
.day-list dt.is-today{padding-left:12px;border-left:3px solid var(--terra-dark);margin-left:-3px}
.day-list dd.is-today{padding-left:8px}
.today-arrow{display:inline-block;color:var(--terra-dark);font-size:22px;line-height:1;margin-right:8px;vertical-align:middle;transform:translateY(-2px)}
.today-label{display:inline-block;font-family:'DM Sans',sans-serif;font-weight:800;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--terra-dark);margin-left:6px;vertical-align:middle}

.pill-row{display:flex;flex-wrap:wrap;gap:7px;margin-top:8px}
a.act-pill{display:inline-flex;align-items:center;gap:6px;font-family:'DM Sans',sans-serif;font-weight:700;font-size:11.5px;letter-spacing:.04em;padding:8px 14px;border-radius:999px;text-decoration:none;line-height:1.2;border:1px solid transparent;color:var(--white)!important;transition:background 150ms ease,border-color 150ms ease}
a.act-pill .arrow{font-size:12px;color:inherit}
.act-pill.pill-prework{background:var(--navy);border-color:var(--navy)}
.act-pill.pill-prework:hover{background:var(--navy-deep);border-color:var(--navy-deep)}
.act-pill.pill-lab{background:var(--terra-dark);border-color:var(--terra-dark)}
.act-pill.pill-lab:hover{background:#94351F;border-color:#94351F}
.act-pill.pill-discussion{background:#DDB54E;border-color:#B89238;color:var(--navy)!important}
.act-pill.pill-discussion:hover{background:#E8C462;border-color:#B89238;color:var(--navy)!important}
.act-pill.pill-quiz{background:var(--sage-dark);border-color:var(--sage-deeper)}
.act-pill.pill-quiz:hover{background:var(--sage-deeper);border-color:#2F4537}
.act-badge{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;font-family:'DM Sans',sans-serif;font-weight:800;font-size:11.5px;letter-spacing:.04em;text-decoration:none;line-height:1;border:1px solid transparent;color:var(--white)!important;transition:background 150ms ease,transform 150ms ease;flex-shrink:0}
.act-badge:hover{transform:translateY(-1px)}
.act-badge.badge-sr{background:var(--navy);border-color:var(--navy)}
.act-badge.badge-sr:hover{background:var(--navy-deep);border-color:var(--navy-deep)}
.act-badge.badge-dr{background:#3F4A54;border-color:#2E3940}
.act-badge.badge-dr:hover{background:#2E3940;border-color:#1F272D}

footer.course-footer{margin-top:32px;padding:22px 28px;background:var(--white);border:1px solid var(--gray-line);border-radius:12px;box-shadow:var(--shadow-rest);font-family:'Lora',Georgia,serif;font-size:14.5px;color:var(--navy);line-height:1.65}
footer.course-footer strong{color:var(--navy);font-style:italic;font-weight:700}

@media print{
  body{background:var(--white)}
  .skip-link,.status-now{display:none!important}
  .schedule-list{gap:8px}
  .week-card{box-shadow:none;border:1px solid #999;page-break-inside:avoid}
  .pill-row a{color:#000!important;background:var(--white)!important;border:1px solid #555!important}
}
</style>
</head>
<body>
<a href="#schedule-list" class="skip-link">Skip to schedule</a>
"""

BANNER = """
<header class="banner" role="banner">
  <div class="banner-inner">
    <p class="banner-eyebrow">BIO 304 <span class="banner-eyebrow-sep" aria-hidden="true"></span> Summer Session 2026</p>
    <h1 class="banner-title">Course Schedule</h1>
    <p class="banner-subtitle">Eight-week online session, June 8 to August 2. Pre-work Monday, Tuesday, Thursday, Friday. Wednesday catch-up and discussion. Weekend is your quiz window.</p>
  </div>
</header>

<main class="container">
"""

OVERVIEW = """
  <section class="overview-strip" aria-label="Session overview">
    <span><strong>8</strong> weeks</span>
    <span class="overview-divider">.</span>
    <span><strong>16</strong> modules</span>
    <span class="overview-divider">.</span>
    <span><strong>42</strong> topics</span>
    <span class="overview-divider">.</span>
    <span><strong>8</strong> weekly quizzes</span>
    <span class="overview-divider">.</span>
    <span><strong>8</strong> weekly discussions</span>
  </section>
"""

STATUS_NOW = """
  <a class="status-now" id="status-now" href="#" hidden>
    <span class="status-now-label" id="status-now-label">Today</span>
    <span class="status-now-text" id="status-now-text"></span>
    <span class="status-now-arrow" aria-hidden="true">&rsaquo;</span>
  </a>
"""

FOOTER = """
  <footer class="course-footer">
    <strong>How the week runs.</strong> Pre-work Monday, Tuesday, Thursday, Friday. Each pre-work day opens with a short lecture video on the topic's page; finishing the video plus the retrieval check unlocks the cards. Wednesday is catch-up plus discussion. The weekend is your quiz window.
    <br><br>
    <strong>What each button does.</strong> <strong style="color:var(--navy)">Pre-work</strong> opens the lecture page (video first, cards after). The navy <strong style="color:var(--navy)">SR</strong> badge jumps straight to today's spaced-recall cards if you already watched the video. <strong style="color:var(--terra-dark)">Lab workbook</strong> opens the printable workbook for hand-labeling. The dark grey <strong style="color:#3F4A54">DR</strong> badge opens Daily Review for every card that is due across all your topics. <strong style="background:#DDB54E;color:var(--navy);padding:1px 8px;border-radius:4px">Discussion</strong> opens this week's discussion prompt. <strong style="color:var(--sage-deeper)">Quiz check</strong> opens your pre-quiz review. The terra arrow <span style="color:var(--terra-dark);font-size:18px;vertical-align:middle">&#9654;</span> marks today's row.
  </footer>
</main>
"""

SCRIPT = """
<script>
(function () {
  // Course constants (kept in sync with course-content.js + build_schedule.py)
  var COURSE_START_ISO = '2026-06-08'; // Monday Week 1
  var COURSE_END_ISO = '2026-08-02';   // Sunday Week 8
  // Pattern: Monday=0, Tuesday=1, Thursday=3, Friday=4 (relative to that week's Monday)

  function parseLocalDate(iso) {
    var p = iso.split('-');
    return new Date(parseInt(p[0],10), parseInt(p[1],10)-1, parseInt(p[2],10));
  }
  function startOfToday() {
    var t = new Date();
    t.setHours(0,0,0,0);
    return t;
  }
  function fmtLongDate(d) {
    var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    return days[d.getDay()] + ', ' + months[d.getMonth()] + ' ' + d.getDate();
  }
  function daysBetween(a, b) {
    return Math.round((b.getTime() - a.getTime()) / 86400000);
  }

  var today = startOfToday();
  var courseStart = parseLocalDate(COURSE_START_ISO);
  var courseEnd = parseLocalDate(COURSE_END_ISO);

  // Find current week + next week
  var currentWeek = null, nextWeek = null;
  var weekEls = document.querySelectorAll('.week-card');
  weekEls.forEach(function (el) {
    var start = parseLocalDate(el.getAttribute('data-start'));
    var end = parseLocalDate(el.getAttribute('data-end'));
    if (today >= start && today <= end) {
      currentWeek = { num: parseInt(el.getAttribute('data-week'),10), el: el, start: start, end: end };
    } else if (today < start && !nextWeek) {
      nextWeek = { num: parseInt(el.getAttribute('data-week'),10), el: el, start: start, end: end };
    } else if (today > end) {
      el.classList.add('is-past');
    }
  });

  // Wire collapse/expand toggle on each week header
  weekEls.forEach(function (el) {
    var header = el.querySelector('.week-header');
    var toggle = el.querySelector('.week-toggle');
    if (!header) return;
    function setExpanded(expanded) {
      el.classList.toggle('is-expanded', expanded);
      header.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      if (toggle) toggle.textContent = expanded ? '−' : '+';  // minus or plus
    }
    header.addEventListener('click', function () {
      setExpanded(!el.classList.contains('is-expanded'));
    });
    header.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        setExpanded(!el.classList.contains('is-expanded'));
      }
    });
    // expose for the auto-expand below
    el._setExpanded = setExpanded;
  });

  // Auto-expand the right week on load
  if (currentWeek) {
    if (currentWeek.el._setExpanded) currentWeek.el._setExpanded(true);
  } else if (nextWeek) {
    if (nextWeek.el._setExpanded) nextWeek.el._setExpanded(true);
  } else if (weekEls.length) {
    // Post-term: expand the last week so the summary is visible.
    var lastEl = weekEls[weekEls.length - 1];
    if (lastEl._setExpanded) lastEl._setExpanded(true);
  }

  // Add status pills inside week cards
  if (currentWeek) {
    currentWeek.el.classList.add('is-current');
    var slot = currentWeek.el.querySelector('.week-status-slot');
    if (slot) slot.innerHTML = '<span class="week-status-pill is-current">This week</span>';
  } else if (nextWeek) {
    var slot2 = nextWeek.el.querySelector('.week-status-slot');
    if (slot2) slot2.innerHTML = '<span class="week-status-pill is-next">Up next</span>';
  }

  // Highlight today's row inside the current week
  if (currentWeek) {
    var slotOffsets = { 0: 0, 1: 1, 3: 3, 4: 4 };  // Mon, Tue, Thu, Fri offsets from Monday
    var weekDayIdx = (today.getDay() === 0) ? 6 : today.getDay() - 1; // 0=Mon..6=Sun
    var dayList = currentWeek.el.querySelector('.day-list');
    if (dayList) {
      // Row order in the dl: Mon-pre, Tue-pre, Wed-catch, Thu-pre, Fri-pre, Weekend
      var rowMap = { 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5 };  // weekday → row index
      var rowIdx = rowMap[weekDayIdx];
      var dts = dayList.querySelectorAll('dt');
      var dds = dayList.querySelectorAll('dd');
      if (dts[rowIdx]) {
        dts[rowIdx].classList.add('is-today');
        // inject arrow if not already present
        if (!dts[rowIdx].querySelector('.today-arrow')) {
          var arrow = document.createElement('span');
          arrow.className = 'today-arrow';
          arrow.setAttribute('aria-hidden', 'true');
          arrow.innerHTML = '&#9654;';
          dts[rowIdx].insertBefore(arrow, dts[rowIdx].firstChild);
        }
      }
      if (dds[rowIdx]) {
        dds[rowIdx].classList.add('is-today');
        // inject today label after first topic-title
        var firstTitle = dds[rowIdx].querySelector('.topic-title');
        if (firstTitle && !firstTitle.querySelector('.today-label')) {
          var label = document.createElement('span');
          label.className = 'today-label';
          label.textContent = 'Today';
          firstTitle.appendChild(document.createTextNode(' '));
          firstTitle.appendChild(label);
        }
      }
    }
  }

  // Status-now banner
  var statusEl = document.getElementById('status-now');
  var statusLabelEl = document.getElementById('status-now-label');
  var statusTextEl = document.getElementById('status-now-text');
  function showStatus(label, text, href) {
    statusLabelEl.textContent = label;
    statusTextEl.innerHTML = text;
    if (href) statusEl.setAttribute('href', href);
    statusEl.hidden = false;
  }

  if (today < courseStart) {
    var days = daysBetween(today, courseStart);
    var word = (days === 1) ? 'day' : 'days';
    showStatus('Coming up',
      'Term begins <strong>' + fmtLongDate(courseStart) + '</strong>. ' + days + ' ' + word + ' to go. Week 1 opens with Levels of Organization, Anatomical Terminology, Homeostasis, Cell Structure, and Membrane Transport.',
      '#week-1');
  } else if (today > courseEnd) {
    showStatus('Term complete',
      'Summer 2026 term wrapped on ' + fmtLongDate(courseEnd) + '. Nice work.', null);
  } else if (currentWeek) {
    var dayName = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][today.getDay()];
    var dayNameLong = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][today.getDay()];
    var label, text;
    if (dayName === 'Mon' || dayName === 'Tue' || dayName === 'Thu' || dayName === 'Fri') {
      label = 'Today';
      text = '<strong>Week ' + currentWeek.num + ', ' + dayNameLong + '.</strong> Pre-work day. Open the lecture page and the lab workbook for today\\'s topic.';
    } else if (dayName === 'Wed') {
      label = 'Today';
      text = '<strong>Week ' + currentWeek.num + ', Wednesday.</strong> Catch-up day. Run Daily Review, post your discussion thoughts, finish any open lab workbook.';
    } else {
      // Sat or Sun
      label = 'Today';
      text = '<strong>Week ' + currentWeek.num + ', ' + dayNameLong + '.</strong> Quiz window open. Take the quiz before Sunday 11:59 PM.';
    }
    showStatus(label, text, '#week-' + currentWeek.num);
  } else if (nextWeek) {
    var d = daysBetween(today, nextWeek.start);
    var w = (d === 1) ? 'day' : 'days';
    showStatus('Up next',
      '<strong>Week ' + nextWeek.num + '</strong> begins ' + fmtLongDate(nextWeek.start) + ' (' + d + ' ' + w + ').',
      '#week-' + nextWeek.num);
  }

  // Scroll to current week on load if present
  if (currentWeek) {
    setTimeout(function () {
      currentWeek.el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 300);
  }
})();

// Iframe height sender for Canvas embed
(function(){
  if(window.self===window.top)return;
  function send(){
    try{
      var h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);
      window.parent.postMessage({type:'iframe-height',id:'bio304-schedule',height:h},'*');
    }catch(e){}
  }
  window.addEventListener('load',send);
  window.addEventListener('resize',send);
  if('ResizeObserver' in window) new ResizeObserver(send).observe(document.body);
})();
</script>
"""

TAIL = """</body>
</html>
"""


if __name__ == "__main__":
    main()
