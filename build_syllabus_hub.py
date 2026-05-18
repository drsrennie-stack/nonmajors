"""
Build biol304_syllabus.html as the unified course hub.

This page is the single point of reference for BIO 304. It orchestrates the
daily flow (lecture pre-work, lab workbook, Wed discussion/lab, Fri-Sun quiz,
Fri initial + Sun final discussion posts) and links out to all support pages.
"""

import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


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


HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 . Syllabus Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--navy:#1E3D4C;--navy-deep:#142A36;--navy-tint:#EDF1F3;--gold:#B8924A;--gold-deep:#9A7838;--terra:#C2734D;--terra-dark:#A0522D;--white:#FFFFFF;--off-white:#FAFAF9;--gray-line:#CFD6DA;--gray-soft:#5C6970;--shadow-rest:0 1px 3px rgba(0,0,0,.08);--shadow-hover:0 8px 16px rgba(0,0,0,.10)}
*{box-sizing:border-box}
body{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.55}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600;border-radius:0 0 6px 0}
.skip-link:focus{left:0}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
@media (prefers-reduced-motion: reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
header{background:var(--white);border-bottom:1px solid var(--gray-line);padding:32px 32px 24px}
.eyebrow{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}
h1{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(28px,4vw,42px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}
.subhead{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:clamp(15px,1.6vw,18px);color:var(--terra-dark);margin:0 0 8px}
.usage{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0;max-width:70ch}
main{max-width:1100px;margin:0 auto;padding:28px 24px 60px}
h2{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:22px;margin:32px 0 12px}
h3{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);font-size:18px;margin:0 0 8px}
h4{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:14px;margin:0 0 4px}
.card{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:var(--shadow-rest);margin-bottom:18px}
.card-tinted{background:var(--navy-tint);border-color:var(--navy)}
.card-list{padding-left:20px}
.card-list li{margin:6px 0}
.flow-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
/* Inside a week body, force 5 columns across (Mon, Tue, Wed, Thu, Fri) at full width. */
.week-body .flow-grid{grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
@media (max-width: 1080px){.week-body .flow-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 600px){.week-body .flow-grid{grid-template-columns:1fr}}
.week-body .day-tile{font-size:14px;padding:14px}
.week-body .day-tile .topic{font-size:14px;line-height:1.35;margin-bottom:8px}
.week-body .day-tile .day-label{font-size:11px;letter-spacing:.08em}
/* Pill buttons inside day tiles. High-specificity selectors so .day-tile a:not(.btn) doesn't override. */
.day-tile a.day-pill,a.day-pill{display:inline-flex;align-items:center;gap:4px;font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11.5px;letter-spacing:.04em;padding:7px 13px;border-radius:999px;text-decoration:none;margin:3px 4px 3px 0;transition:background 150ms ease,color 150ms ease,border-color 150ms ease;border:1px solid transparent;line-height:1.2}
.day-tile a.day-pill.pill-prework,a.day-pill.pill-prework{background:var(--navy);color:var(--white);border-color:var(--navy)}
.day-tile a.day-pill.pill-prework:hover,.day-tile a.day-pill.pill-prework:focus-visible,a.day-pill.pill-prework:hover{background:var(--navy-deep);color:var(--white);border-color:var(--navy-deep)}
.day-tile a.day-pill.pill-lab,a.day-pill.pill-lab{background:#B8924A;color:#142A36;border-color:#9A7838}
.day-tile a.day-pill.pill-lab:hover,.day-tile a.day-pill.pill-lab:focus-visible,a.day-pill.pill-lab:hover{background:#9A7838;color:#142A36;border-color:#7D5F2C}
.day-tile a.day-pill.pill-discussion,a.day-pill.pill-discussion{background:var(--terra-dark);color:var(--white);border-color:var(--terra-dark)}
.day-tile a.day-pill.pill-discussion:hover,.day-tile a.day-pill.pill-discussion:focus-visible,a.day-pill.pill-discussion:hover{background:#7E3F22;color:var(--white);border-color:#7E3F22}
.day-tile a.day-pill.pill-quiz,a.day-pill.pill-quiz{background:#4F6B57;color:var(--white);border-color:#3F5B47}
.day-tile a.day-pill.pill-quiz:hover,.day-tile a.day-pill.pill-quiz:focus-visible,a.day-pill.pill-quiz:hover{background:#3F5B47;color:var(--white);border-color:#2F4537}
.day-pill .arrow{font-size:13px}
.day-tile{background:var(--white);border:1px solid var(--gray-line);border-radius:8px;padding:16px;box-shadow:var(--shadow-rest)}
.day-tile.lab-day{background:var(--off-white);border-style:dashed;border-color:var(--gold-deep)}
.day-label{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}
.day-tile .topic{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--navy);font-size:14px;margin:0 0 8px;line-height:1.35}
.day-tile a:not(.btn){font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:13px;color:var(--navy);text-decoration:none;display:inline-block;padding:4px 0}
.day-tile a:not(.btn):hover{color:var(--gold-deep);text-decoration:underline}
.day-tile a.btn{text-decoration:none}
.day-tile a.btn-primary{color:var(--white)}
.day-tile a.btn-primary:hover{color:var(--white)}
.btn{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:14px;padding:10px 18px;border-radius:6px;border:1px solid transparent;cursor:pointer;text-decoration:none;display:inline-block}
.btn-primary{background:var(--navy);color:var(--white);border-color:var(--navy)}
.btn-primary:hover{background:var(--navy-deep)}
.btn-gold{background:var(--navy);color:var(--white);border:2px solid var(--gold)}
.btn-gold:hover{background:var(--navy-deep)}
.btn-ghost{background:transparent;color:var(--navy);border-color:var(--gray-line)}
.btn-ghost:hover{background:var(--navy-tint);border-color:var(--navy)}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0 14px}
details.week-group{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;box-shadow:var(--shadow-rest);margin-bottom:12px;overflow:hidden}
details.week-group>summary{list-style:none;cursor:pointer;padding:14px 22px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;font-family:'Plus Jakarta Sans',system-ui,sans-serif;border-bottom:1px solid transparent}
details.week-group>summary::-webkit-details-marker{display:none}
details.week-group[open]>summary{border-bottom-color:var(--gray-line)}
details.week-group>summary:hover,details.week-group>summary:focus-visible{background:var(--navy-tint)}
details.week-group>summary::before{content:"+";display:inline-block;width:22px;height:22px;border-radius:50%;border:1px solid var(--navy);color:var(--navy);text-align:center;line-height:20px;font-weight:700;font-size:14px;flex-shrink:0}
details.week-group[open]>summary::before{content:"-"}
.week-label{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark)}
.week-title{font-weight:700;font-size:16px;color:var(--navy);flex:1;min-width:200px}
.week-body{padding:14px 22px 22px}
.weekly-rhythm{background:var(--white);border-left:4px solid var(--gold);padding:14px 20px;border-radius:0 8px 8px 0;margin:14px 0}
.rhythm-row{display:flex;gap:14px;padding:8px 0;border-bottom:1px dotted var(--gray-line);flex-wrap:wrap;align-items:baseline}
.rhythm-row:last-child{border-bottom:none}
.rhythm-day{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);min-width:90px}
.resource-group-title{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--terra-dark);font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:20px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--gray-line)}
.resource-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:18px}
.resource-tile{background:var(--white);border:1px solid var(--gray-line);border-radius:8px;padding:16px;box-shadow:var(--shadow-rest);transition:transform 200ms ease,box-shadow 200ms ease}
.resource-tile:hover{transform:translateY(-2px);box-shadow:var(--shadow-hover)}
.resource-tile a{text-decoration:none;color:var(--navy);display:block}
.resource-tile h4{margin-bottom:4px}
.resource-tile p{margin:0;font-size:13px;color:var(--gray-soft);font-style:italic}
footer{text-align:center;color:var(--gray-soft);padding:24px;font-style:italic;font-size:13px}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header>
  <p class="eyebrow">BIO 304 . HUMAN ANATOMY AND PHYSIOLOGY . AMERICAN RIVER COLLEGE</p>
  <h1>BIO 304 Syllabus Hub</h1>
  <p class="subhead">8-week non-majors A&amp;P essentials. Your single point of reference.</p>
  <p class="usage">Find today's pre-work, lab workbook, discussion, and quiz from here. Everything else builds out from this page.</p>
</header>
<main id="main" tabindex="-1">
"""

INTRO_SECTIONS = """
<section aria-labelledby="welcome-heading">
  <h2 id="welcome-heading">Welcome from Dr. Rennie</h2>
  <div class="card">
    <p>Welcome. You are about to learn how a human body works, top to bottom, in eight weeks. The pace is real, but the design is built to make it possible. Watch every lecture pre-work video. Label every lab diagram by hand. Show up for discussions on Wednesday. Take the quiz between Friday and Sunday. Repeat for eight weeks, and you will leave this course able to read clinical scenarios with an anatomist's eyes.</p>
    <p>You will get out what you put in. The system is here to scaffold the effort.</p>
  </div>
</section>

<section aria-labelledby="rhythm-heading">
  <h2 id="rhythm-heading">Your weekly rhythm</h2>
  <p class="usage">Four lecture pre-work nights, one Wednesday lab + discussion day, one quiz window. Spaced recall practice runs every day.</p>
  <div class="weekly-rhythm">
    <div class="rhythm-row"><span class="rhythm-day">Monday</span><span>Lecture pre-work (one topic). Lab workbook for that topic. Spaced recall practice.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Tuesday</span><span>Lecture pre-work (one topic). Lab workbook for that topic. Spaced recall practice.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Wednesday</span><span>Discussion prompt posts. Lab catch-up and spaced recall. No new pre-work releases.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Thursday</span><span>Lecture pre-work (one topic). Lab workbook for that topic. Spaced recall practice.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Friday</span><span>Lecture pre-work (one topic). Lab workbook for that topic. <strong>Initial discussion post due. Quiz opens.</strong></span></div>
    <div class="rhythm-row"><span class="rhythm-day">Saturday</span><span>Spaced recall practice. Work on quiz and discussion replies.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Sunday</span><span><strong>Final discussion replies due. Quiz closes.</strong></span></div>
  </div>
</section>

<section aria-labelledby="today-heading">
  <h2 id="today-heading">Start here</h2>
  <div class="flow-grid">
    <div class="day-tile">
      <p class="day-label">Step 1 . Tonight</p>
      <p class="topic">Open the pre-work hub</p>
      <a href="bio304-spaced-recall-prototype.html" target="_top" class="btn btn-primary">Open pre-work</a>
    </div>
    <div class="day-tile">
      <p class="day-label">Step 2 . Tonight</p>
      <p class="topic">Print today's lab workbook</p>
      <a href="#week-schedule" target="_top">Jump to today's workbook below &#8595;</a>
    </div>
    <div class="day-tile">
      <p class="day-label">Step 3 . By Sunday</p>
      <p class="topic">Discussion + quiz on Canvas</p>
      <a href="discussions.html" target="_top">Discussion page</a>
    </div>
  </div>
</section>
"""


def build_week_block(week_num, days):
    """days is a list of (day_in_course, day_name, topics) tuples for Mon, Tue, Thu, Fri."""
    rows = []
    for day_num, day_name, topics in days:
        if not topics:
            rows.append(f'''<div class="day-tile"><p class="day-label">{day_name} . Day {day_num}</p><p class="topic" style="color:var(--gray-soft);font-style:italic;">No topic scheduled</p></div>''')
            continue
        topic_links = []
        for t in topics:
            slug = slugify(t["title"])
            workbook = f"workbook_day{day_num:02d}_{slug}.html"
            topic_links.append(
                f'<p class="topic">{t["title"]}</p>'
                f'<a class="day-pill pill-prework" href="bio304-spaced-recall-prototype.html" target="_top">Pre-work <span class="arrow">&rarr;</span></a>'
                f'<a class="day-pill pill-lab" href="{workbook}" target="_top">Lab workbook <span class="arrow">&rarr;</span></a>'
            )
        inner = ''.join(topic_links)
        rows.append(f'<div class="day-tile"><p class="day-label">{day_name} . Day {day_num}</p>{inner}</div>')

    # Wed lab + discussion divider
    wed_tile = '''<div class="day-tile lab-day">
      <p class="day-label">Wednesday . Lab + Discussion</p>
      <p class="topic">No new pre-work. Use this day for the Wednesday lab block and the discussion prompt.</p>
      <a class="day-pill pill-discussion" href="discussions.html" target="_top">Discussion <span class="arrow">&rarr;</span></a>
    </div>'''

    # Insert Wed between Tue (index 1) and Thu (index 2)
    all_tiles = rows[:2] + [wed_tile] + rows[2:]
    return f'''<details class="week-group"{' open' if week_num == 1 else ''}>
  <summary>
    <span class="week-label">Week {week_num}</span>
    <span class="week-title">Pre-work days, lab workbooks, and discussion</span>
  </summary>
  <div class="week-body">
    <div class="flow-grid">{''.join(all_tiles)}</div>
    <p class="usage" style="margin-top:14px;">Discussion: prompt opens Wednesday, initial post due Friday, replies due Sunday. Quiz opens Friday and closes Sunday.</p>
  </div>
</details>'''


def build_schedule_section(course):
    by_day = {}
    for m in course["modules"]:
        for t in m["topics"]:
            d = t.get("dayInCourse")
            if d:
                by_day.setdefault(d, []).append(t)
    # Build per-week blocks: weeks 1-8, each containing days for Mon/Tue/Thu/Fri
    blocks = []
    for wk in range(1, 9):
        day_indices = [(wk - 1) * 4 + i + 1 for i in range(4)]
        day_names = ["Monday", "Tuesday", "Thursday", "Friday"]
        days = list(zip(day_indices, day_names, [by_day.get(d, []) for d in day_indices]))
        blocks.append(build_week_block(wk, days))
    return f'''
<section aria-labelledby="schedule-heading" id="week-schedule">
  <h2 id="schedule-heading">Full 8-week schedule</h2>
  <p class="usage">Each week shows the four pre-work days plus the Wednesday lab and discussion block. Click any day to open its lecture pre-work or print its lab workbook.</p>
  {''.join(blocks)}
</section>
'''


RESOURCE_GROUPS = [
    ("Where to do your work", "study", [
        ("bio304-spaced-recall-prototype.html", "Pre-work hub", "Daily lecture pre-work with spaced recall practice."),
        ("dashboard.html",                       "Dashboard",     "Your progress at a glance."),
        ("discussions.html",                     "Discussions",   "Weekly prompts and post submissions on Canvas."),
        ("clinical_portfolio_hub.html",          "Clinical Portfolio", "Apply concepts to real patient scenarios."),
    ]),
    ("Reference materials", "reference", [
        ("biol304_textbook.html",     "Textbook",    "OpenStax A&amp;P 2e (free)."),
        ("biol304_reading_map.html",  "Reading map", "Which textbook sections support each topic."),
    ]),
    ("Getting things done", "logistics", [
        ("biol304_tech_setup.html",      "Tech setup",            "What you need to participate online."),
        ("submission-directions.html",   "Submission directions", "How and where to turn in work."),
        ("biol304_how_to_reach_me.html", "How to reach me",       "Office hours, email, response times, and Zoom."),
    ]),
    ("Course policies", "policies", [
        ("biol304_accessibility.html",  "Accessibility",                   "How to request accommodations."),
        ("biol304_rsi_statement.html",  "Regular substantive interaction", "What you can expect from me each week."),
        ("integrity.html",              "Academic integrity",              "The hand-labeling rule and other expectations."),
    ]),
]


def build_resources_section():
    out = ['<section aria-labelledby="resources-heading">',
           '  <h2 id="resources-heading">Course resources</h2>',
           '  <p class="usage">Grouped by what you would use each one for.</p>']
    for group_title, group_id, tiles in RESOURCE_GROUPS:
        out.append(f'  <h3 class="resource-group-title">{group_title}</h3>')
        out.append('  <div class="resource-grid">')
        for href, name, desc in tiles:
            out.append(f'    <div class="resource-tile"><a href="{href}" target="_top"><h4>{name}</h4><p>{desc}</p></a></div>')
        out.append('  </div>')
    out.append('</section>')
    return "\n".join(out)


RESOURCES_SECTION = build_resources_section()

FOOTER = """
</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 Syllabus Hub . American River College</p></footer>
<script>
(function(){
  if(window.self===window.top)return;
  function sendHeight(){
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{window.parent.postMessage({type:'iframe-height',id:'bio304-syllabus-hub',height:h},'*');}catch(e){}
  }
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){new ResizeObserver(sendHeight).observe(document.body);}else{setInterval(sendHeight,800);}
})();
</script>
</body>
</html>
"""


def main():
    course = load_course()
    html = HEADER + INTRO_SECTIONS + build_schedule_section(course) + RESOURCES_SECTION + FOOTER
    out = os.path.join(HERE, "biol304_syllabus.html")
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Built {out} ({len(html)//1024} KB)")


if __name__ == "__main__":
    main()
