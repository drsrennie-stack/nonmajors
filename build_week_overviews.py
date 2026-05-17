"""
Build 8 weekly overview HTML pages matching the syllabus hub design system.
Each file is `weekNN_overview.html` and gets iframed from the Canvas Page.
"""

import json, os, re, subprocess
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_START = date(2026, 6, 8)


def load_course():
    proc = subprocess.run(
        ['node', '-e',
         "const w={};new Function('window',require('fs').readFileSync('course-content.js','utf8'))(w);"
         "console.log(JSON.stringify(w.BIO304_COURSE_CONTENT))"],
        cwd=HERE, capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


def slugify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()


def date_of_course_day(day_num):
    week = (day_num - 1) // 4 + 1
    weekday = (day_num - 1) % 4
    offset_within_week = [0, 1, 3, 4][weekday]
    return COURSE_START + timedelta(days=(week - 1) * 7 + offset_within_week)


def date_of_week_event(week_num, weekday_str):
    offsets = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    return COURSE_START + timedelta(days=(week_num - 1) * 7 + offsets[weekday_str])


def fmt(d):
    return d.strftime("%a, %b %-d")


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 . Week {week_num} Overview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--navy:#1E3D4C;--navy-deep:#142A36;--navy-tint:#EDF1F3;--gold:#B8924A;--gold-deep:#9A7838;--terra:#C2734D;--terra-dark:#A0522D;--white:#FFFFFF;--off-white:#FAFAF9;--gray-line:#CFD6DA;--gray-soft:#5C6970;--shadow-rest:0 1px 3px rgba(0,0,0,.08);--shadow-hover:0 8px 16px rgba(0,0,0,.10)}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.55}}
.skip-link{{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600;border-radius:0 0 6px 0}}
.skip-link:focus{{left:0}}
:focus-visible{{outline:3px solid var(--gold);outline-offset:2px}}
@media (prefers-reduced-motion: reduce){{*,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}}}
header.page-header{{background:var(--white);border-bottom:1px solid var(--gray-line);padding:28px 32px 22px}}
.eyebrow{{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}}
h1{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(28px,3.5vw,38px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}}
.subhead{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:clamp(15px,1.6vw,18px);color:var(--terra-dark);margin:0 0 8px}}
.usage{{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0;max-width:70ch}}
main{{max-width:1000px;margin:0 auto;padding:24px}}
h2{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:22px;margin:24px 0 12px}}
h3{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);font-size:16px;margin:0 0 8px}}
.card{{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:var(--shadow-rest);margin-bottom:18px}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 14px}}
.btn{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:14px;padding:10px 18px;border-radius:6px;border:1px solid transparent;cursor:pointer;text-decoration:none;display:inline-block;color:var(--white);background:var(--navy)}}
.btn:hover{{background:var(--navy-deep);color:var(--white)}}
.btn-ghost{{background:transparent;color:var(--navy);border-color:var(--gray-line)}}
.btn-ghost:hover{{background:var(--navy-tint);border-color:var(--navy);color:var(--navy)}}
.btn-gold{{background:var(--navy);color:var(--white);border:2px solid var(--gold)}}
.btn-gold:hover{{background:var(--navy-deep);color:var(--white)}}
.day-grid{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-top:8px}}
@media (max-width:1080px){{.day-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:600px){{.day-grid{{grid-template-columns:1fr}}}}
.day-tile{{background:var(--off-white);border:1px solid var(--gray-line);border-radius:8px;padding:14px}}
.day-tile.wed{{background:var(--off-white);border-style:dashed;border-color:var(--gold-deep)}}
.day-label{{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}}
.day-date{{font-family:'DM Sans',system-ui,sans-serif;font-size:11px;color:var(--gray-soft);margin:0 0 8px}}
.day-topic{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--navy);font-size:14px;line-height:1.35;margin:0 0 10px}}
.day-tile a{{display:inline-block;font-family:'Plus Jakarta Sans',sans-serif;font-size:12.5px;color:var(--navy);text-decoration:none;padding:3px 0}}
.day-tile a:hover{{color:var(--gold-deep);text-decoration:underline}}
.deadline-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:10px}}
.deadline{{background:var(--white);border:1px solid var(--gray-line);border-left:4px solid var(--terra);border-radius:6px;padding:14px 16px}}
.deadline .lbl{{font-family:'DM Sans',sans-serif;font-weight:700;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}}
.deadline .when{{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:var(--navy);font-size:15px}}
.deadline .what{{font-size:13px;color:var(--gray-soft);font-style:italic;margin-top:4px}}
footer{{text-align:center;color:var(--gray-soft);padding:24px;font-style:italic;font-size:13px}}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header class="page-header">
  <p class="eyebrow">BIO 304 . WEEK {week_num} OF 8 . {week_date_range}</p>
  <h1>Week {week_num} overview</h1>
  <p class="subhead">{week_theme}</p>
  <p class="usage">Tonight's pre-work, this week's lab workbooks, the discussion prompt, and the quiz window are all listed below.</p>
</header>
<main id="main" tabindex="-1">
  <div class="toolbar">
    <a class="btn" href="bio304-spaced-recall-prototype.html" target="_top">Open pre-work hub</a>
    <a class="btn btn-ghost" href="biol304_syllabus.html" target="_top">&larr; Back to syllabus hub</a>
  </div>

  <h2>Pre-work and lab workbooks</h2>
  <div class="day-grid">
    {day_tiles}
  </div>

  <h2>This week's deadlines</h2>
  <div class="deadline-grid">
    <div class="deadline">
      <p class="lbl">Discussion</p>
      <p class="when">Initial post: {fri_date}</p>
      <p class="what">Prompt opens Wed {wed_date}. Final replies due Sun {sun_date}.</p>
    </div>
    <div class="deadline">
      <p class="lbl">Quiz</p>
      <p class="when">Opens {fri_date}</p>
      <p class="what">Closes Sun {sun_date} at 11:59 PM.</p>
    </div>
    <div class="deadline">
      <p class="lbl">Lab workbooks</p>
      <p class="when">{lab_workbook_count} due this week</p>
      <p class="what">Print, label by hand, photograph or scan, upload to Canvas.</p>
    </div>
  </div>

</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 . Week {week_num} of 8</p></footer>
<script>
(function(){{
  if(window.self===window.top)return;
  function sendHeight(){{
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{{window.parent.postMessage({{type:'iframe-height',id:'bio304-week-overview',height:h}},'*');}}catch(e){{}}
  }}
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){{new ResizeObserver(sendHeight).observe(document.body);}}else{{setInterval(sendHeight,800);}}
}})();
</script>
</body>
</html>
"""

WEEK_THEMES = {
    1: "Foundations: how the body is organized, the vocabulary you'll use to describe it, and the homeostatic feedback loops that keep everything stable.",
    2: "The cell up close, then how cells assemble into the four tissue types and into your largest organ, skin.",
    3: "The skeletal framework: bone biology, the axial skeleton, the appendicular skeleton, and the joints that connect them.",
    4: "How muscles actually contract (sliding filament) and how nerves actually fire (action potential). Two anchor concepts in one week.",
    5: "Nervous system finish, special senses, and the endocrine glands that talk to the whole body in slow motion.",
    6: "Blood and the cardiovascular system: from the cells that fill it to the heart that pumps it to the vessels that deliver it.",
    7: "Three barrier systems: the immune defenses that guard you, the lungs that breathe for you, and the gut that fuels you.",
    8: "Closing the loop: the kidneys that balance everything, plus the reproductive systems and basic pregnancy A&P.",
}


def render_day_tiles(week_num, days_in_week, wed_date_str):
    """days_in_week: dict day_num -> list of topic dicts, sorted by day_num."""
    day_names_short = ['Monday', 'Tuesday', 'Thursday', 'Friday']
    tiles = []
    sorted_day_nums = sorted(days_in_week.keys())

    for di, day_num in enumerate(sorted_day_nums):
        day_topics = days_in_week[day_num]
        date_label = fmt(date_of_course_day(day_num))  # "Mon, Jun 8"
        topic_html = "<br>".join(t['title'] for t in day_topics)

        # Build pre-work + workbook links per topic; pre-work is the hub
        workbook_links = []
        for t in day_topics:
            slug = slugify(t['title'])
            wb_file = f"workbook_day{day_num:02d}_{slug}.html"
            short = t['title'] if len(day_topics) == 1 else t['title'][:24] + "..."
            workbook_links.append(f'<a href="{wb_file}" target="_top">Lab workbook &rarr;</a>')

        wb_html = "<br>".join(workbook_links)

        tiles.append(f'''<div class="day-tile">
      <p class="day-label">{day_names_short[di]} . Day {day_num}</p>
      <p class="day-date">{date_label}</p>
      <p class="day-topic">{topic_html}</p>
      <a href="bio304-spaced-recall-prototype.html" target="_top">Lecture pre-work &rarr;</a><br>
      {wb_html}
    </div>''')

        # Insert Wed tile after Tuesday (di == 1)
        if di == 1:
            tiles.append(f'''<div class="day-tile wed">
      <p class="day-label">Wednesday . Lab + Discussion</p>
      <p class="day-date">{wed_date_str}</p>
      <p class="day-topic">No new pre-work today. Wednesday is for the lab block, the discussion prompt, and spaced recall.</p>
      <a href="discussions.html" target="_top">Discussion page &rarr;</a>
    </div>''')

    return "\n    ".join(tiles)


def build_week(week_num, days_in_week):
    week_mon = date_of_week_event(week_num, 'Mon')
    week_sun = date_of_week_event(week_num, 'Sun')
    week_wed = date_of_week_event(week_num, 'Wed')
    week_fri = date_of_week_event(week_num, 'Fri')

    wed_date_str = fmt(week_wed)
    fri_date_str = fmt(week_fri)
    sun_date_str = fmt(week_sun)

    week_date_range = f"{fmt(week_mon)} through {fmt(week_sun)}".upper()
    week_theme = WEEK_THEMES.get(week_num, "Week overview.")

    lab_workbook_count = sum(len(ts) for ts in days_in_week.values())

    day_tiles = render_day_tiles(week_num, days_in_week, wed_date_str)

    return TEMPLATE.format(
        week_num=week_num,
        week_date_range=week_date_range,
        week_theme=week_theme,
        day_tiles=day_tiles,
        wed_date=wed_date_str,
        fri_date=fri_date_str,
        sun_date=sun_date_str,
        lab_workbook_count=lab_workbook_count,
    )


def main():
    course = load_course()
    by_week_day = {}
    for m in course["modules"]:
        for t in m["topics"]:
            d = t.get("dayInCourse")
            if d:
                wk = (d - 1) // 4 + 1
                by_week_day.setdefault(wk, {}).setdefault(d, []).append(t)

    built = 0
    for wk in range(1, 9):
        days = by_week_day.get(wk, {})
        html = build_week(wk, days)
        out = os.path.join(HERE, f"week{wk:02d}_overview.html")
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        built += 1
        print(f"  built: week{wk:02d}_overview.html ({len(html)//1024} KB)")
    print(f"\nTotal: {built} week overview pages.")


if __name__ == "__main__":
    main()
