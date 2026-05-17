"""
Redesign the legacy biol304_* pages to match the unified syllabus hub style.
Strategy: extract each page's main content (title, eyebrow, h1, subhead, and
section content), then re-wrap in a unified template that uses the PRIMARY
palette and matches biol304_syllabus.html visual language.
"""

import os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# The legacy files we redesign (keeping all content, swapping the chrome)
TARGETS = [
    ("biol304_textbook.html",      "RESOURCE",   "Free OpenStax textbook for BIO 304"),
    ("biol304_reading_map.html",   "RESOURCE",   "Which textbook sections support each course topic"),
    ("biol304_tech_setup.html",    "GETTING STARTED", "What you need to participate online"),
    ("biol304_accessibility.html", "POLICY",     "Accommodations and accessibility commitments"),
    ("biol304_how_to_reach_me.html","FACULTY",   "Office hours, email, response times, Zoom"),
    ("biol304_rsi_statement.html", "POLICY",     "Regular substantive interaction you can expect each week"),
    ("nonmajors_ap_rhythm_card.html","CLINICAL TOOL", "A&P rhythm card for quick reference"),
]

# Legacy week1 files: orphan and superseded by week01_* + the new syllabus hub.
# Archive them.
ARCHIVE_AS_OBSOLETE = [
    "biol304_week1_overview.html",
    "biol304_week1_trainer.html",
    "biol304_week1_discussion.html",
]


def template(title, eyebrow_kind, subhead, h1, intro_html, body_html):
    """Wrap content in the unified PRIMARY-palette template."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
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
h1{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(26px,3.2vw,38px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}}
.subhead{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:clamp(15px,1.6vw,18px);color:var(--terra-dark);margin:0 0 8px}}
.usage,p.usage{{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0;max-width:70ch}}
main{{max-width:880px;margin:0 auto;padding:24px}}
h2{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:22px;margin:28px 0 10px}}
h3{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);font-size:17px;margin:0 0 8px}}
h4{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:14px;margin:0 0 4px}}
p{{margin:0 0 12px}}
.card{{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:var(--shadow-rest);margin-bottom:18px}}
.card-tinted{{background:var(--navy-tint);border-color:var(--navy)}}
.card-gold{{border-left:4px solid var(--gold-deep);padding-left:20px}}
.card ul,.card ol{{padding-left:22px;margin:8px 0}}
.card li{{margin:6px 0}}
hr{{border:none;border-top:1px solid var(--gray-line);margin:24px 0}}
.btn{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:14px;padding:10px 18px;border-radius:6px;border:1px solid transparent;cursor:pointer;text-decoration:none;display:inline-block}}
.btn-primary{{background:var(--navy);color:var(--white);border-color:var(--navy)}}
.btn-primary:hover{{background:var(--navy-deep)}}
.btn-ghost{{background:transparent;color:var(--navy);border-color:var(--gray-line)}}
.btn-ghost:hover{{background:var(--navy-tint);border-color:var(--navy)}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 14px}}
a{{color:var(--navy);text-decoration:underline;text-decoration-color:var(--gold)}}
a:hover{{color:var(--gold-deep)}}
table{{width:100%;border-collapse:collapse;margin:8px 0}}
th,td{{padding:8px 10px;text-align:left;border-bottom:1px solid var(--gray-line)}}
th{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);background:var(--navy-tint)}}
blockquote{{margin:14px 0;padding:12px 18px;background:var(--off-white);border-left:3px solid var(--gold);font-style:italic;color:var(--gray-soft)}}
strong{{color:var(--navy);font-weight:700}}
footer{{text-align:center;color:var(--gray-soft);padding:24px;font-style:italic;font-size:13px}}
/* Legacy compatibility layer: style the inline class names from older pages */
.lede,.lead,.section-lede{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:500;color:var(--navy);font-size:16px;margin-bottom:14px}}
[class$="-grid"]{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:12px 0}}
[class$="-card"],.tier,.channel,.format-card,.skim-card,.req-card,.read-card,.contact-card,.callout,.summary-card,.week-card,.category-card,.contact-callout,.feature-item,.legend-item,.auditor-box,.help-block,.compliance-stat,.tracks .track,.note,.tip,.info,.field,.focus,.examples{{background:var(--white);border:1px solid var(--gray-line);border-radius:8px;padding:16px 18px;box-shadow:var(--shadow-rest)}}
.preferred,.recommended{{border:2px solid var(--gold);background:var(--off-white)}}
.required{{border-left:4px solid var(--terra-dark)}}
.optional{{border-left:4px solid var(--gold)}}
.channel-rank,.cat-status,.tier-tag,.day-tag,.track-label,.section-num,.label,.lbl,.detail-label,.contact-label{{display:inline-block;font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--terra-dark);margin-bottom:6px}}
.preferred .channel-rank{{color:var(--gold-deep)}}
.channel-name,.cat-name,.contact-item h4,.track-name,.format-card h3,.skim-card h3,.req-card h3,.read-card h3,.section-title,.week-number,.read-body h3{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:700;color:var(--navy);font-size:16px;margin:0 0 6px}}
.channel-when,.detail-value,.contact-value,.tier-tag,.day-tag,.pill,.deadline,.commitment,.evidence-list .ref{{display:inline-block;font-family:'DM Sans',system-ui,sans-serif;font-size:11px;font-weight:600;color:var(--navy);background:var(--navy-tint);padding:3px 10px;border-radius:999px;margin:2px 4px 6px 0}}
.channel-time,.deadline,.cat-status,.tier-tag,.commitment{{font-style:italic;color:var(--gray-soft);font-size:12px;margin-top:8px}}
.channel-desc,.read-body,.cat-body p,.format-card p{{font-family:'Lora',Georgia,serif;font-size:14px;color:var(--navy);margin:6px 0;line-height:1.55}}
.callout,.note,.tip{{border-left:4px solid var(--gold);padding-left:16px;background:var(--off-white)}}
.callout-label{{display:block;font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:4px}}
.legend-swatch{{display:inline-block;width:14px;height:14px;border-radius:3px;border:1px solid var(--gray-line);vertical-align:middle;margin-right:6px}}
.steps{{counter-reset:step;padding-left:0;list-style:none}}
.steps li{{counter-increment:step;position:relative;padding:10px 12px 10px 44px;border-radius:8px;border:1px solid var(--gray-line);background:var(--white);margin:6px 0}}
.steps li::before{{content:counter(step);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--navy);color:var(--white);font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}}
.rhythm-table{{border-collapse:collapse;width:100%}}
.day-cell,.day-name,.instructor-cell,.student-cell{{padding:8px 10px}}
.compliance-stat .stat-num{{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:28px;color:var(--navy);line-height:1}}
.compliance-stat .stat-text{{font-family:'DM Sans',sans-serif;font-size:11px;color:var(--gray-soft);text-transform:uppercase;letter-spacing:.08em}}
.section-head{{display:flex;align-items:baseline;gap:10px;margin:18px 0 10px}}
.section-num{{background:var(--navy);color:var(--white);padding:4px 10px;border-radius:4px;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:13px}}
.systems{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:10px 0}}
.systems > *{{padding:10px 12px;background:var(--off-white);border-radius:6px;border:1px solid var(--gray-line)}}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header class="page-header">
  <p class="eyebrow">BIO 304 . {eyebrow_kind} . MEDMASTERS COLLABORATIVE</p>
  <h1>{h1}</h1>
  <p class="subhead">{subhead}</p>
  {intro_html}
</header>
<main id="main" tabindex="-1">
  <div class="toolbar">
    <a class="btn btn-ghost" href="biol304_syllabus.html" target="_top">&larr; Back to syllabus hub</a>
  </div>
{body_html}
</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 . American River College</p></footer>
<script>
(function(){{
  if(window.self===window.top)return;
  function sendHeight(){{
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{{window.parent.postMessage({{type:'iframe-height',id:'bio304-page',height:h}},'*');}}catch(e){{}}
  }}
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){{new ResizeObserver(sendHeight).observe(document.body);}}else{{setInterval(sendHeight,800);}}
}})();
</script>
</body>
</html>
"""


def extract_content(html, h1_text):
    """Extract the content blocks (after the original h1) up through the footer/end of body.
    Wrap each existing <section> in a .card to match the new design language."""
    # Find <main> if present, else use body content after h1
    main_m = re.search(r'<main[^>]*>([\s\S]*?)</main>', html, re.IGNORECASE)
    if main_m:
        content = main_m.group(1)
    else:
        body_m = re.search(r'<body[^>]*>([\s\S]*?)</body>', html, re.IGNORECASE)
        content = body_m.group(1) if body_m else html

    # Strip the original <header> if present so we don't double up
    content = re.sub(r'<header[^>]*>[\s\S]*?</header>', '', content, count=1, flags=re.IGNORECASE)
    # Strip the original <footer> if present
    content = re.sub(r'<footer[^>]*>[\s\S]*?</footer>', '', content, flags=re.IGNORECASE)
    # Strip skip-link anchor if present
    content = re.sub(r'<a[^>]*class=["\']skip-link[^>]*>[\s\S]*?</a>', '', content, flags=re.IGNORECASE)
    # Strip iframe-height script blocks
    content = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', content, flags=re.IGNORECASE)
    # Drop any leftover h1 (we render h1 in the new header)
    content = re.sub(r'<h1[^>]*>[\s\S]*?</h1>', '', content, count=1, flags=re.IGNORECASE)

    # Wrap each <section> as a .card so styling is consistent
    def wrap_section(m):
        inner = m.group(2)
        # If the section already has class attribute, leave it; else add card
        attrs = m.group(1)
        if 'class=' in attrs:
            return f'<section{attrs}>{inner}</section>'
        return f'<section{attrs} class="card">{inner}</section>'

    content = re.sub(r'<section([^>]*)>([\s\S]*?)</section>', wrap_section, content)

    # If no <section> exists, wrap remaining content in a card to give it a visual frame
    if '<section' not in content.lower():
        content = f'<article class="card">{content.strip()}</article>'

    return content.strip()


def extract_subhead(html):
    """Pull the first subhead-like paragraph from the original (if any)."""
    # Try to find a class="subhead" element
    m = re.search(r'<p[^>]*class=["\'][^"\']*subhead[^"\']*["\'][^>]*>([\s\S]*?)</p>', html, re.IGNORECASE)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    # Else first <p> right after h1
    h1_pos = re.search(r'</h1>', html, re.IGNORECASE)
    if h1_pos:
        rest = html[h1_pos.end():]
        m = re.search(r'<p[^>]*>([\s\S]*?)</p>', rest, re.IGNORECASE)
        if m:
            text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if 30 <= len(text) <= 220:
                return text
    return ""


def main():
    # Step 1: redesign each target file
    for filename, eyebrow_kind, default_subhead in TARGETS:
        path = os.path.join(HERE, filename)
        if not os.path.exists(path):
            print(f"  MISSING: {filename}")
            continue
        original = open(path, encoding='utf-8').read()

        title_m = re.search(r'<title>([\s\S]*?)</title>', original, re.IGNORECASE)
        title = title_m.group(1).strip() if title_m else f"BIO 304 . {filename}"
        # Strip middot/dot encoding noise
        title = re.sub(r'\s*[·•]\s*', ' . ', title)

        h1_m = re.search(r'<h1[^>]*>([\s\S]*?)</h1>', original, re.IGNORECASE)
        h1 = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else filename
        # Decode common entities
        h1 = h1.replace('&amp;', '&').replace('&rsquo;', "’").replace('&nbsp;', ' ')

        existing_subhead = extract_subhead(original)
        subhead = existing_subhead or default_subhead

        content = extract_content(original, h1)
        new_html = template(title, eyebrow_kind, subhead, h1, "", content)
        open(path, 'w', encoding='utf-8').write(new_html)
        print(f"  redesigned: {filename} ({len(new_html)//1024} KB)")

    # Step 2: archive the obsolete biol304_week1_* files
    for old in ARCHIVE_AS_OBSOLETE:
        old_path = os.path.join(HERE, old)
        if os.path.exists(old_path):
            new_path = os.path.join(HERE, "_OBSOLETE_" + old)
            os.rename(old_path, new_path)
            print(f"  archived: {old} -> _OBSOLETE_{old}")


if __name__ == "__main__":
    main()
