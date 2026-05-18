"""
Build biol304_syllabus.html as a single document-style syllabus with a sticky
table of contents. Every section is an anchor target.

This is the canonical syllabus. Sections include:
  - Welcome
  - Course at a glance
  - What you will learn
  - Required materials
  - How the course works (weekly rhythm)
  - Assessments and grading
  - Hard deadlines and late policy
  - Habits that work
  - 8-week schedule (pulled from course-content.js)
  - How to reach me
  - Academic integrity and AI policy
  - Accessibility and accommodations
  - Tech setup and submissions
  - Regular substantive interaction
  - Resources index

Brand: PRIMARY palette. No sage or cream. Byline "Dr. Sharilyn Rennie" with no
credential suffix. Em dashes banned. Iframe height-sender + target="_top" baked in.
"""

import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def load_course():
    proc = subprocess.run(
        ["node", "-e",
         "const w={};new Function('window',require('fs').readFileSync('course-content.js','utf8'))(w);"
         "console.log(JSON.stringify(w.BIO304_COURSE_CONTENT))"],
        cwd=HERE, capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


def slugify(text):
    return re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 Syllabus . American River College</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
  --navy:#1E3D4C;--navy-deep:#142A36;--navy-tint:#EDF1F3;
  --gold:#B8924A;--gold-deep:#9A7838;
  --terra:#C2734D;--terra-dark:#A0522D;
  --sage-dark:#4F6B57;--sage-deeper:#3F5B47;
  --white:#FFFFFF;--off-white:#FAFAF9;
  --gray-line:#CFD6DA;--gray-soft:#5C6970;
  --shadow-rest:0 1px 3px rgba(0,0,0,.08);
  --shadow-hover:0 8px 16px rgba(0,0,0,.10);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:80px}
@media (prefers-reduced-motion: reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
body{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.6;font-size:16px}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600;border-radius:0 0 6px 0}
.skip-link:focus{left:0}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:3px}

/* Page header */
header.page-head{background:var(--white);border-bottom:1px solid var(--gray-line);padding:36px 32px 28px}
.eyebrow{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 8px}
h1.doc-title{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(28px,3.8vw,40px);color:var(--navy);margin:0 0 6px;letter-spacing:-.01em}
.doc-sub{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:clamp(15px,1.6vw,18px);color:var(--terra-dark);margin:0 0 6px}
.doc-meta{font-style:italic;color:var(--gray-soft);font-size:14px;margin:0;max-width:78ch}

/* Two-column layout */
.shell{max-width:1240px;margin:0 auto;padding:24px;display:grid;grid-template-columns:240px 1fr;gap:36px;align-items:start}
@media (max-width: 920px){.shell{grid-template-columns:1fr;gap:18px}}

/* Sticky TOC */
nav.toc{position:sticky;top:18px;align-self:start;background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:18px 16px;box-shadow:var(--shadow-rest);max-height:calc(100vh - 36px);overflow-y:auto}
nav.toc h2{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 12px;padding:0 4px}
nav.toc ol{list-style:none;margin:0;padding:0;counter-reset:tocstep}
nav.toc li{counter-increment:tocstep;margin:0}
nav.toc a{display:flex;gap:10px;align-items:baseline;padding:7px 10px;border-radius:6px;text-decoration:none;color:var(--navy);font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:13.5px;line-height:1.3;border-left:2px solid transparent}
nav.toc a::before{content:counter(tocstep,decimal-leading-zero);color:var(--terra-dark);font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.06em;min-width:18px}
nav.toc a:hover{background:var(--navy-tint)}
nav.toc a:focus-visible{outline-offset:0}
nav.toc a.is-active{background:var(--navy-tint);border-left-color:var(--navy);color:var(--navy-deep)}
@media (max-width: 920px){nav.toc{position:static;max-height:none}}

/* Main document */
main.doc{min-width:0}
section.band{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:24px 28px;margin:0 0 18px;box-shadow:var(--shadow-rest);scroll-margin-top:24px}
section.band:first-child{margin-top:0}
section.band h2{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;color:var(--navy);font-size:clamp(20px,2.4vw,26px);margin:0 0 4px;letter-spacing:-.005em}
section.band .section-eyebrow{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}
section.band h3{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--terra-dark);font-size:17px;margin:22px 0 8px}
section.band h4{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:14px;margin:14px 0 4px;letter-spacing:.01em}
section.band p{margin:0 0 12px}
section.band ul,section.band ol{padding-left:22px;margin:6px 0 14px}
section.band li{margin:6px 0}
section.band strong{color:var(--navy);font-weight:700}
section.band hr{border:none;border-top:1px solid var(--gray-line);margin:18px 0}

a{color:var(--navy);text-decoration:underline;text-decoration-color:var(--gold);text-underline-offset:2px}
a:hover{color:var(--gold-deep)}

/* Definition list for course-at-a-glance */
.glance{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:14px 0 4px}
.glance-item{background:var(--off-white);border:1px solid var(--gray-line);border-radius:8px;padding:12px 14px}
.glance-label{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}
.glance-value{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--navy);font-size:15px;margin:0;line-height:1.35}

/* Rhythm table */
.rhythm{border-left:4px solid var(--gold);padding:6px 18px;margin:14px 0;background:var(--off-white);border-radius:0 8px 8px 0}
.rhythm-row{display:flex;gap:14px;padding:9px 0;border-bottom:1px dotted var(--gray-line);flex-wrap:wrap;align-items:baseline}
.rhythm-row:last-child{border-bottom:none}
.rhythm-day{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);min-width:96px;font-size:14.5px}
.rhythm-body{flex:1;min-width:240px;color:var(--navy);font-size:14.5px}

/* Grading table */
table.grading{width:100%;border-collapse:collapse;margin:10px 0}
table.grading th,table.grading td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--gray-line);font-size:14.5px}
table.grading th{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);background:var(--navy-tint);font-size:13px;letter-spacing:.02em}
table.grading td.pct{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;color:var(--terra-dark);width:80px}

/* Deadline strip */
.deadlines{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}
@media (max-width: 720px){.deadlines{grid-template-columns:1fr}}
.deadline-card{padding:14px 16px;border-radius:8px;color:var(--white);box-shadow:var(--shadow-rest)}
.deadline-card .when{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 6px;opacity:.95}
.deadline-card .what{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;font-size:15px;margin:0;line-height:1.3}
.deadline-card.disc{background:var(--terra-dark)}
.deadline-card.quiz{background:var(--sage-dark)}
.deadline-card.lab{background:#7D5F2C}

/* Do / Don't grid */
.habits{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0}
@media (max-width: 720px){.habits{grid-template-columns:1fr}}
.habits .do,.habits .dont{padding:16px 18px;border-radius:8px;border:1px solid var(--gray-line);background:var(--off-white)}
.habits .do{border-left:4px solid var(--gold)}
.habits .dont{border-left:4px solid var(--terra-dark)}
.habits h4{margin:0 0 8px}
.habits .tag{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px;display:block}
.habits ul{padding-left:18px;margin:0}
.habits li{margin:5px 0;font-size:14.5px}

/* Week groups */
details.week-group{background:var(--off-white);border:1px solid var(--gray-line);border-radius:8px;margin-bottom:10px;overflow:hidden}
details.week-group>summary{list-style:none;cursor:pointer;padding:12px 18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-family:'Plus Jakarta Sans',system-ui,sans-serif;border-bottom:1px solid transparent}
details.week-group>summary::-webkit-details-marker{display:none}
details.week-group[open]>summary{border-bottom-color:var(--gray-line);background:var(--navy-tint)}
details.week-group>summary:hover,details.week-group>summary:focus-visible{background:var(--navy-tint)}
details.week-group>summary::before{content:"+";display:inline-block;width:22px;height:22px;border-radius:50%;border:1px solid var(--navy);color:var(--navy);text-align:center;line-height:20px;font-weight:700;font-size:14px;flex-shrink:0}
details.week-group[open]>summary::before{content:"-"}
.week-label{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark)}
.week-title{font-weight:700;font-size:15px;color:var(--navy);flex:1;min-width:160px}
.week-body{padding:14px 18px 18px}
.flow-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
@media (max-width: 1080px){.flow-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 600px){.flow-grid{grid-template-columns:1fr}}
.day-tile{background:var(--white);border:1px solid var(--gray-line);border-radius:8px;padding:12px;box-shadow:var(--shadow-rest)}
.day-tile.lab-day{background:#F7F5EE;border-style:dashed;border-color:var(--gold-deep)}
.day-label{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}
.day-tile .topic{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--navy);font-size:13.5px;margin:0 0 8px;line-height:1.35}

/* Pill buttons */
.day-tile a.day-pill,a.day-pill{display:inline-flex;align-items:center;gap:6px;font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11.5px;letter-spacing:.04em;padding:8px 14px;border-radius:999px;text-decoration:none;margin:3px 4px 3px 0;transition:background 150ms ease,color 150ms ease,border-color 150ms ease;border:1px solid transparent;line-height:1.2;color:var(--white)!important}
.day-tile a.day-pill.pill-prework,a.day-pill.pill-prework{background:var(--navy);border-color:var(--navy)}
.day-tile a.day-pill.pill-prework:hover,.day-tile a.day-pill.pill-prework:focus-visible{background:var(--navy-deep);border-color:var(--navy-deep)}
.day-tile a.day-pill.pill-lab,a.day-pill.pill-lab{background:#7D5F2C;border-color:#5C4720}
.day-tile a.day-pill.pill-lab:hover,.day-tile a.day-pill.pill-lab:focus-visible{background:#5C4720;border-color:#3F3015}
.day-tile a.day-pill.pill-discussion,a.day-pill.pill-discussion{background:var(--terra-dark);border-color:var(--terra-dark)}
.day-tile a.day-pill.pill-discussion:hover,.day-tile a.day-pill.pill-discussion:focus-visible{background:#7E3F22;border-color:#7E3F22}
.day-tile a.day-pill.pill-quiz,a.day-pill.pill-quiz{background:var(--sage-dark);border-color:var(--sage-deeper)}
.day-tile a.day-pill.pill-quiz:hover,.day-tile a.day-pill.pill-quiz:focus-visible{background:var(--sage-deeper);border-color:#2F4537}
.day-pill .arrow{font-size:12px;color:inherit}

/* Resources index */
.resource-group-title{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--terra-dark);font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:18px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--gray-line)}
.resource-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:14px}
.resource-tile{background:var(--off-white);border:1px solid var(--gray-line);border-radius:8px;padding:14px;transition:transform 200ms ease,box-shadow 200ms ease}
.resource-tile:hover{transform:translateY(-2px);box-shadow:var(--shadow-hover);background:var(--white)}
.resource-tile a{text-decoration:none;color:var(--navy);display:block}
.resource-tile h4{margin:0 0 4px;font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;font-size:14.5px;color:var(--navy)}
.resource-tile p{margin:0;font-size:13px;color:var(--gray-soft);font-style:italic}

/* Print: hide TOC, expand details */
@media print{
  body{background:var(--white)}
  nav.toc,.skip-link{display:none}
  .shell{grid-template-columns:1fr;padding:0;max-width:none}
  section.band{box-shadow:none;border:none;page-break-inside:avoid;padding:12px 0;border-bottom:1px solid var(--gray-line);border-radius:0}
  details{open:true}
  details[open]>summary{background:transparent}
  details>summary::before{display:none}
  a{color:var(--navy);text-decoration:underline}
}

/* Back-to-top */
.back-top{position:fixed;right:18px;bottom:18px;background:var(--navy);color:var(--white);border:none;width:44px;height:44px;border-radius:50%;font-size:18px;cursor:pointer;box-shadow:var(--shadow-hover);display:none;font-family:'DM Sans',sans-serif;font-weight:700}
.back-top:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
.back-top.show{display:block}

footer{text-align:center;color:var(--gray-soft);padding:24px;font-style:italic;font-size:13px}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header class="page-head">
  <p class="eyebrow">BIO 304 . Human Anatomy and Physiology . American River College</p>
  <h1 class="doc-title">BIO 304 Syllabus</h1>
  <p class="doc-sub">8-week non-majors A&amp;P essentials. Online, summer 2026.</p>
  <p class="doc-meta">A single document with everything you need: weekly rhythm, deadlines, grading, the 8-week schedule, and course policies. Use the table of contents to jump to any section.</p>
</header>
<div class="shell">
"""

# Static prose sections. Schedule is generated dynamically.

NAV = """<nav class="toc" aria-label="Syllabus contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#welcome">Welcome</a></li>
    <li><a href="#glance">Course at a Glance</a></li>
    <li><a href="#outcomes">What You Will Learn</a></li>
    <li><a href="#materials">Required Materials</a></li>
    <li><a href="#rhythm">How the Course Works</a></li>
    <li><a href="#grading">Assessments and Grading</a></li>
    <li><a href="#deadlines">Hard Deadlines</a></li>
    <li><a href="#habits">Habits That Work</a></li>
    <li><a href="#schedule">8-Week Schedule</a></li>
    <li><a href="#reach">How to Reach Me</a></li>
    <li><a href="#integrity">Academic Integrity and AI</a></li>
    <li><a href="#access">Accessibility</a></li>
    <li><a href="#rsi">Regular Substantive Interaction</a></li>
    <li><a href="#tech">Tech, Submissions, Honorlock</a></li>
    <li><a href="#resources">Resource Index</a></li>
  </ol>
</nav>
<main class="doc" id="main" tabindex="-1">
"""

WELCOME = """<section class="band" id="welcome" aria-labelledby="welcome-h">
  <p class="section-eyebrow">Section 1</p>
  <h2 id="welcome-h">Welcome</h2>
  <p>Welcome to BIO 304. In eight weeks you will learn how a human body works, top to bottom. The pace is real and the design is built to make it possible. You will watch a short pre-work video each Monday, Tuesday, Thursday, and Friday, then practice the same concepts in a spaced-recall app and a hand-labeled lab workbook. Wednesdays are for catching up and joining the discussion. The weekend is for the quiz.</p>
  <p>This course is for students heading toward nursing, EMT, paramedic, dental hygiene, respiratory therapy, surgical tech, mortuary science, and other allied health pathways. Every topic is paired with a clinical reason you will care about it later.</p>
  <p>You will get out what you put in. The system here is built to scaffold the effort, not replace it.</p>
  <p style="margin-top:14px"><em>Dr. Sharilyn Rennie</em><br><span style="color:var(--gray-soft);font-size:14px;">Instructor of record, BIO 304</span></p>
</section>
"""

GLANCE = """<section class="band" id="glance" aria-labelledby="glance-h">
  <p class="section-eyebrow">Section 2</p>
  <h2 id="glance-h">Course at a Glance</h2>
  <div class="glance">
    <div class="glance-item"><p class="glance-label">Course</p><p class="glance-value">BIO 304: Human Anatomy and Physiology</p></div>
    <div class="glance-item"><p class="glance-label">Institution</p><p class="glance-value">American River College</p></div>
    <div class="glance-item"><p class="glance-label">Format</p><p class="glance-value">Fully online. Asynchronous.</p></div>
    <div class="glance-item"><p class="glance-label">Term</p><p class="glance-value">Summer 2026, 8 weeks</p></div>
    <div class="glance-item"><p class="glance-label">First day</p><p class="glance-value">Monday, June 8, 2026</p></div>
    <div class="glance-item"><p class="glance-label">Last day</p><p class="glance-value">Sunday, August 2, 2026</p></div>
    <div class="glance-item"><p class="glance-label">Instructor</p><p class="glance-value">Dr. Sharilyn Rennie</p></div>
    <div class="glance-item"><p class="glance-label">Textbook</p><p class="glance-value">OpenStax A&amp;P 2e (free)</p></div>
  </div>
</section>
"""

OUTCOMES = """<section class="band" id="outcomes" aria-labelledby="outcomes-h">
  <p class="section-eyebrow">Section 3</p>
  <h2 id="outcomes-h">What You Will Learn</h2>
  <p>BIO 304 is a non-majors survey of human anatomy and physiology. By the end of the course, you will be able to:</p>
  <ol>
    <li>Identify major anatomical structures across the eleven organ systems and describe their basic functions.</li>
    <li>Explain core physiological processes including homeostasis, membrane transport, action potentials, the cardiac cycle, gas exchange, filtration, and reproduction.</li>
    <li>Trace the relationship between structure and function at the cellular, tissue, organ, and system levels.</li>
    <li>Use anatomical and physiological vocabulary correctly in speech and writing.</li>
    <li>Apply A&amp;P concepts to short clinical scenarios that mirror the situations you will encounter in allied health practice.</li>
  </ol>
  <p style="font-size:14px;color:var(--gray-soft);font-style:italic">This is a survey course. It is not the full A&amp;P sequence required for nursing programs that mandate a separate two-semester anatomy and physiology series. Check your transfer program's requirements before enrolling.</p>
</section>
"""

MATERIALS = """<section class="band" id="materials" aria-labelledby="materials-h">
  <p class="section-eyebrow">Section 4</p>
  <h2 id="materials-h">Required Materials</h2>
  <ul>
    <li><strong>Textbook (free).</strong> OpenStax <em>Anatomy and Physiology 2e</em>. You can read it online or download a PDF. No purchase, no access code. The reading map on Canvas points you to the exact sections that support each topic.</li>
    <li><strong>A computer or tablet with a current browser.</strong> Chrome, Edge, Firefox, or Safari, all recent versions. The pre-work hub and the lab workbooks run in the browser.</li>
    <li><strong>A printer or a way to print at the campus library.</strong> Each day's lab workbook is meant to be printed and labeled by hand. Hand drawing is part of how this course is graded.</li>
    <li><strong>Pen, pencil, and a ruler.</strong> Yes, a ruler. Anatomy drawings come out cleaner with one.</li>
    <li><strong>A webcam and a quiet space for Honorlock.</strong> Quizzes are proctored. The setup is in section 14.</li>
  </ul>
</section>
"""

RHYTHM = """<section class="band" id="rhythm" aria-labelledby="rhythm-h">
  <p class="section-eyebrow">Section 5</p>
  <h2 id="rhythm-h">How the Course Works</h2>
  <p>Every week has the same shape. Four pre-work days on lecture topics, one Wednesday lab-and-discussion day, and a quiz that opens Friday and closes Sunday. Spaced recall practice runs in the background every day.</p>
  <div class="rhythm">
    <div class="rhythm-row"><span class="rhythm-day">Monday</span><span class="rhythm-body">Pre-work video and spaced recall on one topic. Print and label that day's lab workbook.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Tuesday</span><span class="rhythm-body">Pre-work video and spaced recall on the next topic. Print and label that day's lab workbook.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Wednesday</span><span class="rhythm-body">No new pre-work. Catch up on labs and join the week's discussion thread.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Thursday</span><span class="rhythm-body">Pre-work video and spaced recall. Lab workbook.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Friday</span><span class="rhythm-body">Pre-work video and lab workbook. <strong>Initial discussion post due. Quiz opens.</strong></span></div>
    <div class="rhythm-row"><span class="rhythm-day">Saturday</span><span class="rhythm-body">Spaced recall review. Work on the quiz and your discussion replies.</span></div>
    <div class="rhythm-row"><span class="rhythm-day">Sunday</span><span class="rhythm-body"><strong>Discussion replies and lab workbooks due. Quiz closes at 11:59 PM.</strong></span></div>
  </div>
  <h3>The Carnegie expectation: roughly 22 to 24 hours per week, total</h3>
  <p>This is a 4-credit course delivered in 8 weeks, which doubles the weekly pace of a regular 16-week semester. Federal Carnegie Unit standards expect approximately 22 to 24 hours of total student engagement per week for that format. That total is split into two buckets:</p>
  <ul>
    <li><strong>Scheduled lecture and lab equivalent: about 8 to 10 hours per week.</strong> This is your pre-work video viewing (4 days a week), the Wednesday lab block, and time inside the lab workbooks. Because the course is asynchronous, you choose when to do this work, but it counts as your scheduled instruction time.</li>
    <li><strong>Outside-of-class study: about 12 to 15 hours per week.</strong> This is the work on top of scheduled instruction: spaced recall practice in the pre-work hub, OpenStax reading, the synthesis questions on the workbooks, discussion writing and replies, and quiz preparation.</li>
  </ul>
  <p>Some weeks will run lighter, some heavier (the cardiovascular and renal weeks have more moving parts). Block both buckets on your calendar before week 1 starts. Treat them like work shifts.</p>
</section>
"""

GRADING = """<section class="band" id="grading" aria-labelledby="grading-h">
  <p class="section-eyebrow">Section 6</p>
  <h2 id="grading-h">Assessments and Grading</h2>
  <p>Your grade is built from four components. Each one targets a different kind of learning.</p>
  <table class="grading" aria-label="Grading components">
    <thead><tr><th>Component</th><th>What it measures</th><th class="pct">Weight</th></tr></thead>
    <tbody>
      <tr><td><strong>Pre-work engagement</strong></td><td>Daily video viewing plus spaced recall practice. Logged automatically in the pre-work hub. Export your engagement report each week.</td><td class="pct">40%</td></tr>
      <tr><td><strong>Lab workbooks</strong></td><td>Hand-labeled anatomy diagrams and short-answer synthesis. One workbook per pre-work day, submitted as a scanned PDF.</td><td class="pct">30%</td></tr>
      <tr><td><strong>Weekly discussions</strong></td><td>One initial post (Friday) plus two substantive replies (Sunday). Evidence-based, your own words.</td><td class="pct">10%</td></tr>
      <tr><td><strong>Weekly quizzes</strong></td><td>20 questions, 20 minutes, Honorlock proctored, one attempt. Opens Friday, closes Sunday at 11:59 PM.</td><td class="pct">20%</td></tr>
    </tbody>
  </table>
  <h3>Letter grade scale</h3>
  <p>90 to 100 = A &nbsp;.&nbsp; 80 to 89 = B &nbsp;.&nbsp; 70 to 79 = C &nbsp;.&nbsp; 60 to 69 = D &nbsp;.&nbsp; below 60 = F</p>
  <p style="font-size:14px;color:var(--gray-soft);font-style:italic">No curves and no extra credit. Your grade reflects your work.</p>
</section>
"""

DEADLINES = """<section class="band" id="deadlines" aria-labelledby="deadlines-h">
  <p class="section-eyebrow">Section 7</p>
  <h2 id="deadlines-h">Hard Deadlines</h2>
  <p>Three hard deadlines every week. Mark them on your calendar before week 1.</p>
  <div class="deadlines">
    <div class="deadline-card disc">
      <p class="when">Friday 11:59 PM</p>
      <p class="what">Initial discussion post</p>
    </div>
    <div class="deadline-card quiz">
      <p class="when">Sunday 11:59 PM</p>
      <p class="what">Weekly quiz closes</p>
    </div>
    <div class="deadline-card lab">
      <p class="when">Sunday 11:59 PM</p>
      <p class="what">All lab workbooks + discussion replies</p>
    </div>
  </div>
  <h3>Late policy</h3>
  <p>Late work earns zero points. No exceptions. DSPS accommodations are honored if registered before week 1 begins. If life is hitting hard, email me <strong>before</strong> a deadline. Solutions exist before the deadline. They do not exist after.</p>
  <p>In an 8-week course, falling one week behind is roughly equivalent to falling two weeks behind in a regular semester. The late policy exists to protect your pace, not to punish you.</p>
</section>
"""

HABITS = """<section class="band" id="habits" aria-labelledby="habits-h">
  <p class="section-eyebrow">Section 8</p>
  <h2 id="habits-h">Habits That Work</h2>
  <p>The students who succeed in this format are not necessarily the smartest ones. They are the ones who built and protected a weekly rhythm. Here is what works and what does not.</p>
  <div class="habits">
    <div class="do">
      <span class="tag">Do</span>
      <h4>What successful students do</h4>
      <ul>
        <li>Block both buckets on your calendar (instruction time and outside study) and protect them like work shifts.</li>
        <li>Run spaced recall in 15 to 25 minute sessions. More sessions, less length each.</li>
        <li>Print the lab workbook before you sit down to do it. Do not break flow to print.</li>
        <li>Take the quiz fresh, not exhausted. Schedule it earlier on Sunday if possible.</li>
        <li>Email me before missing a deadline if life is hitting hard. Solutions exist before, not after.</li>
        <li>Show up in the discussion thread by Wednesday so you have time to reply thoughtfully.</li>
      </ul>
    </div>
    <div class="dont">
      <span class="tag">Don't</span>
      <h4>Patterns that hurt students</h4>
      <ul>
        <li>Trying to do all 22 to 24 hours in a single weekend push. Spacing is core to retention.</li>
        <li>Skipping the pre-work video to "save time" before the workbook. The workbook builds on the video.</li>
        <li>Leaving the quiz for late Sunday night. Honorlock issues happen at the worst times.</li>
        <li>Pasting AI text into discussion posts or workbook synthesis answers. They are designed to be detectable.</li>
        <li>Treating the workbook as fill-in-the-blanks. The drawings and synthesis questions are where the points live.</li>
        <li>Assuming "I'll catch up next week." In an 8-week course, falling behind compounds fast.</li>
      </ul>
    </div>
  </div>
</section>
"""

REACH = """<section class="band" id="reach" aria-labelledby="reach-h">
  <p class="section-eyebrow">Section 10</p>
  <h2 id="reach-h">How to Reach Me</h2>
  <p>Three channels. Three different purposes. Pick the right one and you will get a faster, better answer.</p>
  <h3>1. Virtual Office Hours forum (preferred for most questions)</h3>
  <p>Course content questions, assignment clarifications, technical questions about Canvas or Honorlock, study strategies. Anything not confidential goes here. Other students benefit when your question gets answered in public. Response within 24 to 48 hours on weekdays.</p>
  <h3>2. Email or Canvas Inbox (confidential matters)</h3>
  <p>Grade questions, accommodation needs, personal circumstances, anything you would not want classmates to see. Response within 24 to 48 hours on weekdays.</p>
  <h3>3. One-on-one Zoom (deep conversations, by appointment)</h3>
  <p>Complex situations that need back-and-forth, study coaching, going over feedback, or getting unstuck on a difficult concept. Schedule by email. Typically within 1 to 3 days.</p>
  <p style="margin-top:14px;font-size:14px"><a href="biol304_how_to_reach_me.html" target="_top">Full contact guide and channel examples &rarr;</a></p>
</section>
"""

INTEGRITY = """<section class="band" id="integrity" aria-labelledby="integrity-h">
  <p class="section-eyebrow">Section 11</p>
  <h2 id="integrity-h">Academic Integrity and AI Policy</h2>
  <p>You are training for a career where integrity has direct consequences for human lives. The habits you build now are the habits you carry into clinical practice. All submitted work must be your own.</p>
  <h3>The integrity standard</h3>
  <p>Academic dishonesty includes copying answers, sharing quiz questions, submitting AI-generated content as your own, plagiarizing text or images, and using unauthorized references during a proctored exam. See the official ARC policy at <a href="https://arc.losrios.edu/student-resources/student-conduct" target="_blank" rel="noopener">arc.losrios.edu/student-resources/student-conduct</a>.</p>
  <h3>The AI policy in one paragraph</h3>
  <p>AI is allowed as a study tool. It is not allowed to write your work. You can use AI to clarify concepts, quiz yourself, organize your thinking, generate practice questions, or check your reasoning <em>after</em> you have done your own work. You cannot use AI to generate workbook drawings, discussion posts, synthesis answers, portfolio content, or any quiz answer. Honorlock-proctored quizzes treat any AI use as a violation automatically.</p>
  <h3>AI Honor Contract</h3>
  <p>Every student signs the AI Use Honor Contract in week 1. The contract spells out responsible AI use in A&amp;P coursework. Look for it in the Week 1 module on Canvas. <strong>Due Tuesday, June 9, 2026.</strong></p>
  <h3>How AI use is detected</h3>
  <p>AI-generated content has predictable signatures: uniform style, certain phrasing patterns, factual hallucinations that conflict with the textbook, and structures that do not match the prompt. The hand-labeled lab workbook is the primary detection mechanism. A digital workbook with no handwriting and no revision history is treated as AI-generated by default.</p>
  <p style="margin-top:14px;font-size:14px"><a href="integrity.html" target="_top">Full integrity and AI policy, with examples &rarr;</a></p>
</section>
"""

ACCESS = """<section class="band" id="access" aria-labelledby="access-h">
  <p class="section-eyebrow">Section 12</p>
  <h2 id="access-h">Accessibility and Accommodations</h2>
  <p>Accessibility is non-negotiable in this course. For online students it is the difference between access and exclusion. Every page in the course is built to WCAG 2.2 AA standards as a floor, with AAA-level color contrast on most text.</p>
  <h3>If you have a DSPS accommodation</h3>
  <p>Email me your DSPS letter before week 1 begins, or as soon as your accommodation is approved. I will set up the testing-time extensions in Honorlock and any other adjustments you need.</p>
  <h3>If something on a course page is hard to use</h3>
  <p>Tell me. The pre-work hub, the lab workbooks, the discussion pages, the syllabus, all of it should work with a keyboard alone, with a screen reader, with reduced motion, and with text scaled up. If something fails any of those, that is a bug in my course, not in you.</p>
  <p style="margin-top:14px;font-size:14px"><a href="biol304_accessibility.html" target="_top">Full accessibility statement and how to request accommodations &rarr;</a></p>
</section>
"""

RSI = """<section class="band" id="rsi" aria-labelledby="rsi-h">
  <p class="section-eyebrow">Section 13</p>
  <h2 id="rsi-h">Regular Substantive Interaction</h2>
  <p>This course meets federal regular substantive interaction (RSI) requirements for online courses. Here is what you can expect from me, every week:</p>
  <ul>
    <li><strong>Weekly announcement.</strong> Posted Monday morning with the week's focus, anything that shifted from the syllabus, and one teaching note tied to clinical practice.</li>
    <li><strong>Substantive participation in the discussion thread.</strong> I respond to questions, redirect tangents, and push back on weak claims with evidence. I am there, not just watching.</li>
    <li><strong>Personalized feedback on lab workbooks and quizzes.</strong> Not just a score. Comments on what you got, what you missed, and what to do next.</li>
    <li><strong>Forum monitoring within 24 to 48 hours on weekdays.</strong> Email within the same window.</li>
    <li><strong>Office hours by appointment.</strong> Zoom or in-person at the college as scheduled.</li>
  </ul>
  <p style="margin-top:14px;font-size:14px"><a href="biol304_rsi_statement.html" target="_top">Full RSI statement &rarr;</a></p>
</section>
"""

TECH = """<section class="band" id="tech" aria-labelledby="tech-h">
  <p class="section-eyebrow">Section 14</p>
  <h2 id="tech-h">Tech, Submissions, and Honorlock</h2>
  <h3>Browser and internet</h3>
  <p>Chrome, Edge, Firefox, or Safari, all current versions. Stable internet for quiz day. If your internet is unreliable, plan to take the quiz from the campus library or another known-good location.</p>
  <h3>Submissions</h3>
  <p>Lab workbooks are submitted as a single scanned PDF per day. Filename convention: <code>LastName_DayNN_Topic.pdf</code>. Discussion posts go in the Canvas discussion thread. The weekly quiz is launched from inside the Canvas Quizzes tab through Honorlock.</p>
  <h3>Honorlock</h3>
  <p>Quizzes are proctored by Honorlock. You will need a webcam, microphone, and a quiet space. The first time you launch Honorlock, allow extra time for the browser extension installation. After that, launch is fast.</p>
  <p style="margin-top:14px;font-size:14px"><a href="biol304_tech_setup.html" target="_top">Full tech setup guide &rarr;</a> &nbsp;.&nbsp; <a href="submission-directions.html" target="_top">Submission directions &rarr;</a></p>
</section>
"""


SCHED_HEAD = """<section class="band" id="schedule" aria-labelledby="schedule-h">
  <p class="section-eyebrow">Section 9</p>
  <h2 id="schedule-h">8-Week Schedule</h2>
  <p>Click any day to open its pre-work hub or its lab workbook. Wednesday is for catching up and joining the discussion. The quiz opens Friday and closes Sunday.</p>
"""

SCHED_FOOT = "</section>\n"


def topics_by_day(course):
    """Group topics by day number for fast lookup."""
    by_day = {}
    for mod in course["modules"]:
        for t in mod["topics"]:
            by_day.setdefault(t["dayInCourse"], []).append(t)
    return by_day


# Map dayInCourse (1..32) to (week, day-of-week-label).
# Course runs Mon Tue Thu Fri (skip Wed and weekend) for 32 weekdays across 8 weeks.
SCHED_PATTERN = [("Monday", 1), ("Tuesday", 2), ("Thursday", 3), ("Friday", 4)]


def week_and_dow(day_in_course):
    """Return (week_number, day_of_week_label, slot_1to4) for a day."""
    week = (day_in_course - 1) // 4 + 1
    slot = (day_in_course - 1) % 4
    return week, SCHED_PATTERN[slot][0], slot + 1


def render_schedule(course):
    by_day = topics_by_day(course)
    out = [SCHED_HEAD]
    for week in range(1, 9):
        first_day = (week - 1) * 4 + 1
        last_day = first_day + 3
        is_open = " open" if week == 1 else ""
        out.append(f'<details class="week-group"{is_open}>')
        out.append(f'  <summary>')
        out.append(f'    <span class="week-label">Week {week}</span>')
        out.append(f'    <span class="week-title">Pre-work days, lab workbook, and discussion</span>')
        out.append(f'  </summary>')
        out.append(f'  <div class="week-body">')
        out.append(f'    <div class="flow-grid">')

        # Tiles: Mon, Tue, Wed (lab block), Thu, Fri
        for slot_idx in range(4):
            day = first_day + slot_idx
            dow = SCHED_PATTERN[slot_idx][0]
            topics = by_day.get(day, [])
            out.append(f'      <div class="day-tile">')
            out.append(f'        <p class="day-label">{dow} . Day {day}</p>')
            for t in topics:
                slug = t["id"]
                title = t["title"]
                out.append(f'        <p class="topic">{title}</p>')
                out.append(f'        <a class="day-pill pill-prework" href="bio304-spaced-recall-prototype.html" target="_top">Pre-work <span class="arrow">&rarr;</span></a>')
                out.append(f'        <a class="day-pill pill-lab" href="workbook_day{day:02d}_{slug}.html" target="_top">Lab workbook <span class="arrow">&rarr;</span></a>')
            out.append(f'      </div>')

            # Insert the Wed lab-day tile after Tuesday (slot_idx == 1)
            if slot_idx == 1:
                out.append(f'      <div class="day-tile lab-day">')
                out.append(f'        <p class="day-label">Wednesday . Lab + Discussion</p>')
                out.append(f'        <p class="topic">No new pre-work. Catch up on lab workbooks and join this week\'s discussion thread.</p>')
                out.append(f'        <a class="day-pill pill-discussion" href="week{week:02d}_discussion.html" target="_top">Discussion <span class="arrow">&rarr;</span></a>')
                out.append(f'      </div>')

        out.append(f'    </div>')  # flow-grid
        out.append(f'    <p style="margin-top:12px;font-size:13.5px;color:var(--gray-soft);font-style:italic;">Discussion: prompt opens Wednesday, initial post due Friday, replies due Sunday. Quiz opens Friday and closes Sunday.</p>')
        out.append(f'  </div>')  # week-body
        out.append(f'</details>')

    out.append(SCHED_FOOT)
    return "\n".join(out)


RESOURCES = """<section class="band" id="resources" aria-labelledby="resources-h">
  <p class="section-eyebrow">Section 15</p>
  <h2 id="resources-h">Resource Index</h2>
  <p>Quick links to every working surface in the course.</p>
  <h3 class="resource-group-title">Where you do your work</h3>
  <div class="resource-grid">
    <div class="resource-tile"><a href="bio304-spaced-recall-prototype.html" target="_top"><h4>Pre-work hub</h4><p>Daily videos and spaced recall. Pick a week from inside the app.</p></a></div>
    <div class="resource-tile"><a href="discussions.html" target="_top"><h4>Discussions</h4><p>All eight weekly discussion prompts in one place.</p></a></div>
  </div>
  <h3 class="resource-group-title">Reference materials</h3>
  <div class="resource-grid">
    <div class="resource-tile"><a href="biol304_textbook.html" target="_top"><h4>Textbook</h4><p>OpenStax A&amp;P 2e (free).</p></a></div>
    <div class="resource-tile"><a href="biol304_reading_map.html" target="_top"><h4>Reading map</h4><p>Which textbook section supports each topic.</p></a></div>
  </div>
  <h3 class="resource-group-title">Getting things done</h3>
  <div class="resource-grid">
    <div class="resource-tile"><a href="biol304_tech_setup.html" target="_top"><h4>Tech setup</h4><p>Browser, Honorlock, internet.</p></a></div>
    <div class="resource-tile"><a href="submission-directions.html" target="_top"><h4>Submission directions</h4><p>How and where to turn things in.</p></a></div>
    <div class="resource-tile"><a href="biol304_how_to_reach_me.html" target="_top"><h4>How to reach me</h4><p>Forum, email, Zoom.</p></a></div>
  </div>
  <h3 class="resource-group-title">Course policies</h3>
  <div class="resource-grid">
    <div class="resource-tile"><a href="biol304_accessibility.html" target="_top"><h4>Accessibility</h4><p>How to request accommodations.</p></a></div>
    <div class="resource-tile"><a href="biol304_rsi_statement.html" target="_top"><h4>Regular substantive interaction</h4><p>What you can expect from me.</p></a></div>
    <div class="resource-tile"><a href="integrity.html" target="_top"><h4>Academic integrity</h4><p>Full AI and integrity policy.</p></a></div>
  </div>
</section>
"""

FOOTER = """</main>
</div>
<button class="back-top" type="button" aria-label="Back to top" id="backTop">^</button>
<footer><p>Dr. Sharilyn Rennie . BIO 304 Syllabus . American River College . Summer 2026</p></footer>
<script>
// TOC active-section highlighting via IntersectionObserver
(function(){
  var links = document.querySelectorAll('nav.toc a[href^="#"]');
  if(!links.length || !('IntersectionObserver' in window)) return;
  var map = {};
  links.forEach(function(a){
    var id = a.getAttribute('href').slice(1);
    map[id] = a;
  });
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        Object.values(map).forEach(function(l){l.classList.remove('is-active');});
        var link = map[e.target.id];
        if(link) link.classList.add('is-active');
      }
    });
  }, {rootMargin: '-30% 0px -60% 0px', threshold: 0});
  Object.keys(map).forEach(function(id){
    var el = document.getElementById(id);
    if(el) io.observe(el);
  });
})();

// Back-to-top button
(function(){
  var btn = document.getElementById('backTop');
  if(!btn) return;
  window.addEventListener('scroll', function(){
    btn.classList.toggle('show', window.scrollY > 600);
  }, {passive:true});
  btn.addEventListener('click', function(){
    window.scrollTo({top:0, behavior:'smooth'});
  });
})();

// Iframe height sender (for Canvas embed)
(function(){
  if(window.self===window.top)return;
  function sendHeight(){
    var h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{window.parent.postMessage({type:'iframe-height',id:'bio304-syllabus',height:h},'*');}catch(e){}
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
    html_parts = [
        HEAD,
        NAV,
        WELCOME,
        GLANCE,
        OUTCOMES,
        MATERIALS,
        RHYTHM,
        GRADING,
        DEADLINES,
        HABITS,
        render_schedule(course),
        REACH,
        INTEGRITY,
        ACCESS,
        RSI,
        TECH,
        RESOURCES,
        FOOTER,
    ]
    html = "".join(html_parts)

    # Defensive: strip any stray em dashes that might have snuck in.
    if "—" in html or "–" in html:
        raise SystemExit("Em dash detected in output. Fix the source.")

    out_path = os.path.join(HERE, "biol304_syllabus.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out_path} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
