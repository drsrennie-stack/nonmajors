"""
Build 8 branded weekly discussion pages: week01_discussion.html through
week08_discussion.html. Each contains the prompt plus reply requirements,
styled to match the syllabus hub. Canvas Discussions iframe these pages
in the prompt body so the prompt looks branded while the discussion itself
still lives natively in Canvas.
"""

import os
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_START = date(2026, 6, 8)


def date_of_week_event(week_num, weekday_str):
    offsets = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    return COURSE_START + timedelta(days=(week_num - 1) * 7 + offsets[weekday_str])


def fmt(d):
    return d.strftime("%a, %b %-d")


PROMPTS = {
    1: {
        "title": "Finding homeostasis in your own life",
        "lede": "How a feedback loop works in something you control every day, then how that maps to body physiology.",
        "body": """
<p>This week we built the four-part negative feedback loop: stimulus, receptor, control center, effector. We saw how the body keeps variables like body temperature, blood glucose, and pH near a set point.</p>
<p>Pick <strong>one variable in your own life</strong> that you actively regulate, but that is NOT a body variable. Examples: the temperature of your bedroom, your bank account balance, your daily caffeine intake, the brightness of your phone screen.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the variable</strong> and its set point (your target).</li>
  <li><strong>Identify each of the four feedback components</strong> in YOUR system (what is the receptor? control center? effector? response?).</li>
  <li><strong>Describe a time the system worked</strong> and a time it failed.</li>
  <li><strong>Then tie it to the body</strong>: what physiological feedback loop is the closest analog?</li>
</ol>
"""
    },
    2: {
        "title": "Tissue, location, function",
        "lede": "Predict what's at a real body location, then explain why those tissues are exactly the right tools.",
        "body": """
<p>This week we covered four tissue types (epithelial, connective, muscle, nervous) and how skin layers them together into a complete organ.</p>
<p>Pick <strong>one specific location in the human body</strong> — a small region (e.g., the lining of the trachea, the inside of a knee joint, the bottom of your foot, the surface of an alveolus).</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the location.</strong></li>
  <li><strong>Identify every tissue type you would find there</strong> in cross-section. Be specific (e.g., "pseudostratified ciliated columnar with goblet cells").</li>
  <li><strong>Explain why each tissue is exactly the right tool</strong> for that job. Why isn't the trachea lined with stratified squamous? Why isn't the bottom of your foot lined with simple columnar?</li>
</ol>
"""
    },
    3: {
        "title": "A fracture story",
        "lede": "Locate a real fracture anatomically, then predict its healing course from bone biology.",
        "body": """
<p>This week we covered bone biology, axial and appendicular skeletal anatomy, and joints.</p>
<p>Find a real-world fracture story — yours, a family member's, a famous athlete's, a news article. (Anonymize names if it's not your own story.)</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the bone(s) fractured</strong> and the type of fracture if known.</li>
  <li><strong>Locate it precisely</strong> using directional terms and the axial/appendicular distinction.</li>
  <li><strong>Identify any joints involved.</strong> Was it intra-articular? Did mobility return fully or partially?</li>
  <li><strong>Predict the healing course</strong> based on what you know about bone biology: which cells took over, how long was the cast/immobilization, how was function restored?</li>
</ol>
"""
    },
    4: {
        "title": "When the message fails",
        "lede": "Pick a disease or toxin that disrupts muscle contraction or nervous conduction, locate where in the cycle it strikes, then predict the symptoms from first principles.",
        "body": """
<p>This week we built the sliding filament theory of muscle contraction and the action potential. Both depend on a precise chemical signal arriving at the right place at the right time.</p>
<p>Pick <strong>one disease or toxin</strong> that disrupts either muscle contraction or nervous conduction. Examples: myasthenia gravis, organophosphate poisoning, multiple sclerosis, botulinum toxin, malignant hyperthermia, tetanus, Lambert-Eaton syndrome.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Name the condition</strong> and a one-sentence summary.</li>
  <li><strong>Identify the exact step in the cycle</strong> where it disrupts function. Be precise (e.g., "blocks nicotinic ACh receptors at the neuromuscular junction"; "prevents synaptic vesicle release").</li>
  <li><strong>Predict the patient's symptoms</strong> from first principles, not from a list you found online.</li>
  <li><strong>Note one treatment</strong> and why it targets that step.</li>
</ol>
"""
    },
    5: {
        "title": "A sense or a hormone you took for granted",
        "lede": "Until something disrupts it, you don't notice this system at all. Tell us about a time you noticed.",
        "body": """
<p>This week we covered the central and peripheral nervous systems, the special senses, and the endocrine system.</p>
<p>Pick <strong>one special sense or one hormone</strong> that you take for granted until something disrupts it. Examples: depth perception, balance, color vision, the smell of your own home, thyroid hormone, insulin, cortisol.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Describe the normal mechanism</strong> in a sentence or two. Where does the signal originate? Where does it travel? What's the effect?</li>
  <li><strong>Describe a specific situation</strong> where this sense or hormone was disrupted — yours, someone you know, or a clinical scenario from a credible source.</li>
  <li><strong>Map the disruption to the mechanism</strong>: which step failed, and how did that produce the symptoms?</li>
  <li><strong>Reflect</strong>: what surprised you about how invisible this system is until it fails?</li>
</ol>
"""
    },
    6: {
        "title": "Blood pressure as a story",
        "lede": "A real clinical scenario. Reason from the cardiovascular physiology you built this week.",
        "body": """
<p>This week we covered blood, the heart, the conduction system, and blood vessels. Blood pressure is the integrated readout of all of them.</p>
<p>For your initial post, work through the following scenario. (200-300 words.)</p>
<blockquote>A 68-year-old patient walks into clinic. BP today is 158/94. Heart rate 76, regular. They report feeling fine. They are on no medications. They are about 30 lbs above their ideal weight.</blockquote>
<ol>
  <li><strong>What does each number mean?</strong> (systolic, diastolic, units, what physiologic event each captures)</li>
  <li><strong>Which compartments of the cardiovascular system</strong> are contributing to elevated pressure?</li>
  <li><strong>If you could change ONE thing about this patient's physiology</strong> to lower BP first, what would you pick and why?</li>
  <li><strong>What would you want to ask the patient</strong> before making any recommendation?</li>
</ol>
"""
    },
    7: {
        "title": "A barrier breached",
        "lede": "Tell the story of a time an immune, respiratory, or digestive barrier failed.",
        "body": """
<p>This week we covered the lymphatic and immune systems, the respiratory system, and the digestive system. Each is a barrier between your body and the outside world.</p>
<p>Pick <strong>one situation where one of these barriers was breached</strong> — illness, infection, allergy, food poisoning, asthma attack, choking incident, anything where the line between "outside" and "inside" got crossed.</p>
<p>In your initial post (200-300 words):</p>
<ol>
  <li><strong>Describe the situation briefly.</strong></li>
  <li><strong>Identify the barrier that failed</strong> (anatomically and at the tissue level).</li>
  <li><strong>Trace the body's response</strong>: what innate defenses fired first? Did the adaptive immune system get involved? How?</li>
  <li><strong>What healed it</strong>, and how would you predict the body would respond to the same insult next time?</li>
</ol>
"""
    },
    8: {
        "title": "Looking back across eight weeks",
        "lede": "Final week. Synthesize across systems, reflect on what changed, and look forward.",
        "body": """
<p>Last week of the course. This is a synthesis discussion.</p>
<p>Pick <strong>one body system you came in already familiar with</strong> and <strong>one body system you came in knowing little about</strong>.</p>
<p>In your initial post (300-400 words):</p>
<ol>
  <li><strong>For the familiar system</strong>: what's one concept you now understand differently than you did on day one? Be specific.</li>
  <li><strong>For the unfamiliar system</strong>: what's one moment from this term where the lightbulb went on?</li>
  <li><strong>Across the whole course</strong>: pick one connection between two systems that you didn't expect when you started. (Examples: the connection between kidney filtration and blood pressure; between the nervous system and the muscle action potential; between digestion and immunity.)</li>
  <li><strong>Forward look</strong>: what's one question about the human body you'd want to chase next?</li>
</ol>
"""
    },
}


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 . Week {week_num} Discussion</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--navy:#1E3D4C;--navy-deep:#142A36;--navy-tint:#EDF1F3;--gold:#B8924A;--gold-deep:#9A7838;--terra:#C2734D;--terra-dark:#A0522D;--white:#FFFFFF;--off-white:#FAFAF9;--gray-line:#CFD6DA;--gray-soft:#5C6970;--shadow-rest:0 1px 3px rgba(0,0,0,.08)}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.6}}
.skip-link{{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600}}
.skip-link:focus{{left:0}}
:focus-visible{{outline:3px solid var(--gold);outline-offset:2px}}
@media (prefers-reduced-motion: reduce){{*,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}}}
header.page-header{{background:var(--white);border-bottom:1px solid var(--gray-line);padding:28px 32px 22px}}
.eyebrow{{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 6px}}
h1{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(24px,3vw,34px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}}
.subhead{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:clamp(15px,1.6vw,18px);color:var(--terra-dark);margin:0 0 6px}}
.usage{{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0;max-width:70ch}}
main{{max-width:820px;margin:0 auto;padding:24px}}
h2{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:20px;margin:20px 0 10px}}
.card{{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:var(--shadow-rest);margin-bottom:16px}}
.prompt-card{{border-left:4px solid var(--terra-dark)}}
.prompt-card ol{{padding-left:22px;margin:8px 0}}
.prompt-card li{{margin:8px 0}}
.prompt-card blockquote{{margin:14px 0;padding:12px 18px;background:var(--off-white);border-left:3px solid var(--gold);font-style:italic;color:var(--navy)}}
.deadlines{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:14px 0}}
.deadline-pill{{background:var(--white);border:1px solid var(--gray-line);border-left:4px solid var(--terra-dark);border-radius:6px;padding:12px 16px}}
.deadline-pill .lbl{{font-family:'DM Sans',sans-serif;font-weight:700;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}}
.deadline-pill .when{{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:var(--navy);font-size:15px;margin:0}}
.deadline-pill .what{{font-size:12.5px;color:var(--gray-soft);font-style:italic;margin:4px 0 0}}
footer{{text-align:center;color:var(--gray-soft);padding:24px;font-style:italic;font-size:13px}}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header class="page-header">
  <p class="eyebrow">BIO 304 . WEEK {week_num} OF 8 . DISCUSSION</p>
  <h1>{prompt_title}</h1>
  <p class="subhead">{lede}</p>
  <p class="usage">Initial post due Friday. Replies due Sunday. Substantive replies build on or respectfully challenge a classmate's thinking.</p>
</header>
<main id="main" tabindex="-1">

  <article class="card prompt-card">
    <h2>Prompt</h2>
    {body}
  </article>

  <h2>Deadlines and expectations</h2>
  <div class="deadlines">
    <div class="deadline-pill">
      <p class="lbl">Prompt opens</p>
      <p class="when">{wed_date}</p>
      <p class="what">Wednesday, 12:00 AM</p>
    </div>
    <div class="deadline-pill">
      <p class="lbl">Initial post due</p>
      <p class="when">{fri_date}</p>
      <p class="what">Friday, 11:59 PM</p>
    </div>
    <div class="deadline-pill">
      <p class="lbl">Replies due</p>
      <p class="when">{sun_date}</p>
      <p class="what">Sunday, 11:59 PM</p>
    </div>
  </div>

  <article class="card">
    <h2>How replies are evaluated</h2>
    <ul>
      <li><strong>Substantive</strong>: at least 75 words. Goes beyond "I agree" or "nice post."</li>
      <li><strong>Builds or challenges</strong>: extend a classmate's idea with new information, OR respectfully push back with reasoning.</li>
      <li><strong>Cite or apply</strong>: reference the OpenStax section, your textbook reading, or a topic from this week's pre-work.</li>
      <li><strong>At least two replies</strong> to different classmates by Sunday.</li>
    </ul>
  </article>

</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 . American River College . Week {week_num} of 8</p></footer>
<script>
(function(){{
  if(window.self===window.top)return;
  function sendHeight(){{
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{{window.parent.postMessage({{type:'iframe-height',id:'bio304-discussion',height:h}},'*');}}catch(e){{}}
  }}
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){{new ResizeObserver(sendHeight).observe(document.body);}}else{{setInterval(sendHeight,800);}}
}})();
</script>
</body>
</html>
"""


def main():
    built = 0
    for wk in range(1, 9):
        p = PROMPTS[wk]
        html = TEMPLATE.format(
            week_num=wk,
            prompt_title=p["title"],
            lede=p["lede"],
            body=p["body"].strip(),
            wed_date=fmt(date_of_week_event(wk, 'Wed')),
            fri_date=fmt(date_of_week_event(wk, 'Fri')),
            sun_date=fmt(date_of_week_event(wk, 'Sun')),
        )
        out = os.path.join(HERE, f"week{wk:02d}_discussion.html")
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        built += 1
        print(f"  built: week{wk:02d}_discussion.html ({len(html)//1024} KB)")
    print(f"\nTotal: {built} branded discussion pages.")


if __name__ == "__main__":
    main()
