"""
Build canvas-modules-1-8.md: paste-ready Canvas snippets for Weeks 1 through 8.

Lean version: 3 items per week.
- 1 Lab Workbooks Assignment (single submission with per-day rubric rows)
- 1 Discussion (native, with prompt)
- 1 Quiz (native, with sampled questions from cards)

The weekly hub iframe was removed. Students access each day's pre-work and
workbook through the document-style syllabus at biol304_syllabus.html, which
has the full 8-week schedule with day-by-day pill links.

Total: 24 Canvas items across 8 weeks (down from 88).
"""

import json, os, re, subprocess
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://drsrennie-stack.github.io/nonmajors/"
COURSE_START = date(2026, 6, 8)  # Monday of Week 1

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
    """Day 1 = Mon week 1. Days 2-4 = Tue, Thu, Fri week 1 (skipping Wed)."""
    week = (day_num - 1) // 4 + 1  # 1..8
    weekday = (day_num - 1) % 4    # 0=Mon, 1=Tue, 2=Thu, 3=Fri
    offset_within_week = [0, 1, 3, 4][weekday]  # Mon, Tue, Thu, Fri
    return COURSE_START + timedelta(days=(week - 1) * 7 + offset_within_week)


def date_of_week_event(week_num, weekday_str):
    """weekday_str in {'Mon','Tue','Wed','Thu','Fri','Sat','Sun'}"""
    offsets = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    return COURSE_START + timedelta(days=(week_num - 1) * 7 + offsets[weekday_str])


def fmt_date(d):
    return d.strftime("%a %b %-d")


# Discussion prompts: one per week, clinical-leaning, tied to the week's content
DISCUSSION_PROMPTS = {
    1: {
        "title": "Week 1 Discussion: Finding homeostasis in your own life",
        "prompt": """
<p>This week we built the four-part negative feedback loop (stimulus → receptor → control center → effector) and saw how the body keeps variables like body temperature, blood glucose, and pH near a set point.</p>
<p>Pick <strong>one variable in your own life</strong> that you actively regulate, but that is NOT a body variable. Examples: the temperature of your bedroom, your bank account balance, the amount of caffeine you drink in a day, the brightness of your phone screen.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the variable</strong> and its set point (your target).</li>
  <li><strong>Identify each of the four feedback components</strong> in YOUR system (what is the receptor? control center? effector? response?).</li>
  <li><strong>Describe a time the system worked</strong> and a time it failed.</li>
  <li><strong>Then tie it to the body</strong>: what physiological feedback loop is the closest analog?</li>
</ol>
<p>Reply to at least two classmates by Sunday. Look for someone whose system mirrors yours and someone whose differs.</p>
"""
    },
    2: {
        "title": "Week 2 Discussion: Tissue, location, function",
        "prompt": """
<p>This week we covered four tissue types (epithelial, connective, muscle, nervous) and how skin layers them together into a complete organ.</p>
<p>Pick <strong>one location in the human body</strong> — a small region (e.g., the lining of the trachea, the inside of a knee joint, the bottom of your foot, the surface of an alveolus).</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the location.</strong></li>
  <li><strong>Identify every tissue type you would find there</strong> in cross-section. Be specific (e.g., "pseudostratified ciliated columnar with goblet cells").</li>
  <li><strong>Explain why each tissue is exactly the right tool</strong> for that job. Why isn't the trachea lined with stratified squamous? Why isn't the bottom of your foot lined with simple columnar?</li>
</ol>
<p>Reply to at least two classmates by Sunday, ideally to people who chose locations you wouldn't have thought to compare.</p>
"""
    },
    3: {
        "title": "Week 3 Discussion: A fracture story",
        "prompt": """
<p>This week we covered bone biology, axial and appendicular skeletal anatomy, and joints.</p>
<p>Find a real-world fracture story — yours, a family member's, a famous athlete's, a news article. (Anonymize names if it's not your own story.)</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the bone(s) fractured</strong> and the type of fracture if known.</li>
  <li><strong>Locate it precisely</strong> using directional terms and the axial/appendicular distinction.</li>
  <li><strong>Identify any joints involved.</strong> Was it intra-articular? Did mobility return fully or partially?</li>
  <li><strong>Predict the healing course</strong> based on what you know about bone biology: which cells took over, how long was the cast/immobilization, how was function restored?</li>
</ol>
<p>Reply to at least two classmates by Sunday. If you see a fracture story that puzzles you, ask a question.</p>
"""
    },
    4: {
        "title": "Week 4 Discussion: When the message fails",
        "prompt": """
<p>This week we built the sliding filament theory of muscle contraction and the action potential. Both depend on a precise chemical signal arriving at the right place at the right time.</p>
<p>Pick <strong>one disease or toxin</strong> that disrupts either muscle contraction or nervous conduction. Examples: myasthenia gravis, organophosphate poisoning, multiple sclerosis, botulinum toxin, malignant hyperthermia, tetanus, Lambert-Eaton syndrome.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the condition</strong> and a one-sentence summary.</li>
  <li><strong>Identify the exact step in the cycle</strong> where it disrupts function. Be precise (e.g., "blocks nicotinic ACh receptors at the neuromuscular junction"; "prevents synaptic vesicle release").</li>
  <li><strong>Predict the patient's symptoms</strong> from first principles, not from a list you found online.</li>
  <li><strong>Note one treatment</strong> and why it targets that step.</li>
</ol>
<p>Reply to at least two classmates by Sunday. Try to find someone whose condition affects the OPPOSITE node of the cycle.</p>
"""
    },
    5: {
        "title": "Week 5 Discussion: A sense or a hormone you took for granted",
        "prompt": """
<p>This week we covered the central and peripheral nervous systems, the special senses, and the endocrine system.</p>
<p>Pick <strong>one special sense or one hormone</strong> that you take for granted until something disrupts it. Examples: depth perception, balance, color vision, the smell of your own home, thyroid hormone, insulin, cortisol.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Describe the normal mechanism</strong> in a sentence or two. Where does the signal originate? Where does it travel? What's the effect?</li>
  <li><strong>Describe a specific situation</strong> where this sense or hormone was disrupted — yours, someone you know, or a clinical scenario from a credible source.</li>
  <li><strong>Map the disruption to the mechanism</strong>: which step failed, and how did that produce the symptoms?</li>
  <li><strong>Reflect</strong>: what surprised you about how invisible this system is until it fails?</li>
</ol>
<p>Reply to at least two classmates by Sunday.</p>
"""
    },
    6: {
        "title": "Week 6 Discussion: Blood pressure as a story",
        "prompt": """
<p>This week we covered blood, the heart, the conduction system, and blood vessels. Blood pressure is the integrated readout of all of them.</p>
<p>For your initial post, work through the following scenario. (200-300 words.)</p>
<blockquote>A 68-year-old patient walks into clinic. BP today is 158/94. Heart rate 76, regular. They report feeling fine. They are on no medications. They are about 30 lbs above their ideal weight.</blockquote>
<ol>
  <li><strong>What does each number mean?</strong> (systolic, diastolic, units, what physiologic event each captures)</li>
  <li><strong>Which compartments of the cardiovascular system</strong> are contributing to elevated pressure?</li>
  <li><strong>If you could change ONE thing about this patient's physiology</strong> to lower BP first, what would you pick and why?</li>
  <li><strong>What would you want to ask the patient</strong> before making any recommendation?</li>
</ol>
<p>Reply to at least two classmates by Sunday. Aim for one reply that builds on someone's reasoning and one that respectfully challenges it.</p>
"""
    },
    7: {
        "title": "Week 7 Discussion: A barrier breached",
        "prompt": """
<p>This week we covered the lymphatic and immune systems, the respiratory system, and the digestive system. Each is a barrier between your body and the outside world.</p>
<p>Pick <strong>one situation where one of these barriers was breached</strong> — illness, infection, allergy, food poisoning, asthma attack, choking incident, anything where the line between "outside" and "inside" got crossed.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Describe the situation briefly.</strong></li>
  <li><strong>Identify the barrier that failed</strong> (anatomically and at the tissue level).</li>
  <li><strong>Trace the body's response</strong>: what innate defenses fired first? Did the adaptive immune system get involved? How?</li>
  <li><strong>What healed it</strong>, and how would you predict the body would respond to the same insult next time?</li>
</ol>
<p>Reply to at least two classmates by Sunday.</p>
"""
    },
    8: {
        "title": "Week 8 Discussion: Looking back across eight weeks",
        "prompt": """
<p>Last week of the course. This is a synthesis discussion.</p>
<p>Pick <strong>one body system you came in already familiar with</strong> and <strong>one body system you came in knowing little about</strong>.</p>
<p>In your initial post (300-400 words):</p>
<ol>
  <li><strong>For the familiar system</strong>: what's one concept you now understand differently than you did on day one? Be specific.</li>
  <li><strong>For the unfamiliar system</strong>: what's one moment from this term where the lightbulb went on?</li>
  <li><strong>Across the whole course</strong>: pick one connection between two systems that you didn't expect when you started. (Examples: the connection between kidney filtration and blood pressure; between the nervous system and the muscle action potential; between digestion and immunity.)</li>
  <li><strong>Forward look</strong>: what's one question about the human body you'd want to chase next?</li>
</ol>
<p>Reply to at least two classmates by Sunday. Be generous — this is your last chance to learn from each other before the final.</p>
"""
    },
}


def build_quiz_questions(topics_in_week, week_num):
    """Sample DOK 1 cards from the week's topics as quiz questions."""
    questions = []
    for t in topics_in_week:
        # Take up to 2 DOK 1 cards per topic as auto-graded short-answer/multi-choice
        dok1 = [c for c in t["cards"] if c["dok"] == 1][:2]
        for card in dok1:
            questions.append({
                "topic": t["title"],
                "q": card["q"],
                "a": card["a"],
            })
    return questions


def render_quiz_section(week_num, topics_in_week):
    """Render quiz instructions + sampled questions for instructor reference."""
    questions = build_quiz_questions(topics_in_week, week_num)
    quiz_open = fmt_date(date_of_week_event(week_num, 'Fri'))
    quiz_close = fmt_date(date_of_week_event(week_num, 'Sun'))
    lines = [
        f"## 3. Week {week_num} Quiz (Canvas Quiz)",
        "",
        "Set this up as a Canvas Classic Quiz or New Quiz.",
        "",
        "**Settings:**",
        f"- Available from: {quiz_open} 12:00 AM",
        f"- Due by: {quiz_close} 11:59 PM",
        "- Time limit: 30 minutes (suggested)",
        "- Allowed attempts: 1 (or 2 with score-keep-highest)",
        "- Show one question at a time: instructor preference",
        "- Lock questions after answering: optional",
        "- Shuffle answers: Yes",
        "- Show correct answers: only after the quiz closes",
        "- Points possible: 10-15 (1 point per question)",
        "",
        f"**Question pool** ({len(questions)} short-answer / multi-choice prompts pulled from this week's DOK 1 cards):",
        "",
    ]
    for i, q in enumerate(questions, start=1):
        lines.append(f"{i}. **[{q['topic']}]** {q['q']}")
        lines.append(f"   *Answer:* {q['a']}")
        lines.append("")
    return "\n".join(lines)


def page_snippet(title_intro, url, height, iframe_title):
    """Generate a paste-ready iframe page snippet."""
    return f"""```html
<p>{title_intro}</p>
<p><a href="{url}" target="_blank" rel="noopener"><strong>Open in a new window &#8599;</strong></a></p>
<p><iframe src="{url}" width="100%" height="{height}" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="{iframe_title}"></iframe></p>
```"""


def workbook_snippet(workbook_filename, topic_title, day_num):
    url = BASE_URL + workbook_filename
    intro = (f"Open the unlabeled diagram below. Print this workbook, label every "
             f"structure by hand using the structure list, then photograph or scan "
             f"your finished page and upload it as your submission to this assignment.")
    return f"""```html
<p>{intro}</p>
<p><a href="{url}" target="_blank" rel="noopener"><strong>Open the workbook in a new window &#8599;</strong></a></p>
<p><iframe src="{url}" width="100%" height="1400" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Lab workbook: {topic_title}"></iframe></p>
```"""


def render_week(week_num, topics_in_week):
    """Option B (lean) layout: 4 Canvas items per week.
       1. Week N Hub (iframes weekNN_overview.html)
       2. Week N Lab Workbooks (single assignment with 4-row rubric)
       3. Week N Discussion (native)
       4. Week N Quiz (native)
    """
    week_mon = fmt_date(date_of_week_event(week_num, 'Mon'))
    week_sun = fmt_date(date_of_week_event(week_num, 'Sun'))
    week_wed = fmt_date(date_of_week_event(week_num, 'Wed'))
    week_fri = fmt_date(date_of_week_event(week_num, 'Fri'))

    # Group by day-in-course
    days = {}
    for t in topics_in_week:
        days.setdefault(t["dayInCourse"], []).append(t)

    out = []
    out.append(f"\n---\n\n# Module {week_num} — Week {week_num}\n")
    out.append(f"**Calendar:** {week_mon} through {week_sun}")
    out.append(f"**Discussion prompt posts:** {week_wed}")
    out.append(f"**Initial discussion post due:** {week_fri} (11:59 PM)")
    out.append(f"**Final discussion replies due:** {week_sun} (11:59 PM)")
    out.append(f"**Quiz window:** {week_fri} 12:00 AM through {week_sun} 11:59 PM")
    out.append("")

    # ---- 1. Week N Lab Workbooks (single assignment with rubric) ----
    out.append(f"## 1. Week {week_num} Lab Workbooks (Canvas Assignment, one submission per week)")
    out.append("")
    out.append("**Assignment settings:**")
    out.append(f"- Due: {week_sun} 11:59 PM")
    out.append("- Points: 20 (5 per workbook, 4 workbooks)")
    out.append("- Submission type: Online → File uploads (allow multiple files: PDF, JPG, PNG)")
    out.append("- Allowed attempts: unlimited (until due)")
    out.append("- Use a **rubric** with 4 rows (one per workbook day) so each daily workbook can be graded independently:")
    sorted_days_list = sorted(days.keys())
    day_names = ['Monday', 'Tuesday', 'Thursday', 'Friday']
    for di, day_num in enumerate(sorted_days_list):
        day_topics = days[day_num]
        topic_titles = " + ".join(t['title'] for t in day_topics)
        out.append(f"  - **Row {di+1}** | {day_names[di]} ({fmt_date(date_of_course_day(day_num))}): {topic_titles} | 5 points")
    out.append("")
    # Assignment instruction snippet
    workbook_links = []
    for di, day_num in enumerate(sorted_days_list):
        day_topics = days[day_num]
        for t in day_topics:
            slug = slugify(t['title'])
            file = f"workbook_day{day_num:02d}_{slug}.html"
            workbook_links.append(
                f'  <li><strong>{day_names[di]} ({fmt_date(date_of_course_day(day_num))})</strong>: '
                f'<a href="{BASE_URL}{file}" target="_blank" rel="noopener">{t["title"]} workbook &#8599;</a></li>'
            )
    out.append("**Assignment instructions (paste into the Assignment body in Canvas HTML editor):**")
    out.append("")
    out.append(f"""```html
<p>This week you will hand-label four (4) lab workbooks, one per pre-work day. Print each workbook the night it is assigned, label every structure by hand using the structure list, then photograph or scan all four pages and upload them as a single submission to this assignment by Sunday at 11:59 PM.</p>
<h3>Workbooks for Week {week_num}</h3>
<ul>
{chr(10).join(workbook_links)}
</ul>
<p><strong>Submission tips:</strong> upload as a single PDF if you can (combine pages), or upload separate JPG/PNG files for each day. Either is accepted.</p>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```""")
    out.append("")

    # ---- 2. Discussion ----
    out.append(f"## 2. Week {week_num} Discussion (posts {week_wed}, replies due {week_sun})")
    out.append("")
    disc = DISCUSSION_PROMPTS.get(week_num, {})
    out.append(f"**Title:** {disc.get('title', f'Week {week_num} Discussion')}")
    out.append("")
    out.append("**Settings:**")
    out.append("- Discussion type: Threaded")
    out.append(f"- Available from: {week_wed} 12:00 AM")
    out.append(f"- Initial post due: {week_fri} 11:59 PM")
    out.append(f"- Replies due: {week_sun} 11:59 PM")
    out.append("- Points: 10")
    out.append("- Require initial post before viewing replies: Yes")
    out.append("- Must reply to at least 2 classmates")
    out.append("")
    out.append("**Prompt (paste into the discussion body):**")
    out.append("")
    out.append("```html")
    out.append(disc.get('prompt', f'<p>Week {week_num} discussion prompt to be drafted.</p>').strip())
    out.append("```")
    out.append("")

    # ---- 4. Quiz ----
    out.append(render_quiz_section(week_num, topics_in_week))

    return "\n".join(out)


def main():
    course = load_course()
    out_lines = [
        "# Canvas Modules 1–8 — Paste-Ready Snippets",
        "",
        f"**Base URL:** `{BASE_URL}`",
        f"**Course start (Mon, Week 1):** {fmt_date(COURSE_START)} ({COURSE_START.isoformat()})",
        f"**Course end (Sun, Week 8):** {fmt_date(COURSE_START + timedelta(weeks=8, days=-1))} ({(COURSE_START + timedelta(weeks=8, days=-1)).isoformat()})",
        "",
        "## How to use",
        "",
        "1. Open the Canvas Module for the week you're building.",
        "2. For each item below, create the matching Canvas item (Page, Assignment, Discussion, or Quiz).",
        "3. For Pages and Assignments with iframes, paste the code block into Canvas's HTML editor.",
        "4. For Discussions, copy the prompt HTML into the discussion message body.",
        "5. For Quizzes, create each question manually in Canvas using the provided prompt and answer.",
        "6. Set the dates listed under each item.",
        "",
        "**Note:** Every iframe assumes GitHub Pages is publishing at the base URL above. Test one link in your browser before mass-pasting.",
        "",
    ]

    # Group topics by week
    all_topics = []
    for m in course["modules"]:
        for t in m["topics"]:
            all_topics.append(t)
    by_week = {}
    for t in all_topics:
        d = t.get("dayInCourse")
        if d:
            wk = (d - 1) // 4 + 1
            by_week.setdefault(wk, []).append(t)

    for wk in range(1, 9):
        topics = by_week.get(wk, [])
        out_lines.append(render_week(wk, topics))

    out_path = os.path.join(HERE, "canvas-modules-1-8.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(out_lines))
    print(f"Built {out_path}: {os.path.getsize(out_path)//1024} KB, {sum(1 for _ in open(out_path))} lines")


if __name__ == "__main__":
    main()
