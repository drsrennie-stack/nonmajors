"""
Build 17 per-module teaching PDFs from course-content.js + teaching_content.py.
Compact, dense layout. No cover page. Topics flow into each other.
"""

import json
import os
import re
import subprocess
import sys
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    HRFlowable, ListFlowable, ListItem, KeepTogether
)
from reportlab.lib import colors

sys.path.insert(0, os.path.dirname(__file__))
from teaching_content import TEACHING

# --- PRIMARY palette ---
NAVY = HexColor("#1E3D4C")
NAVY_DEEP = HexColor("#142A36")
NAVY_TINT = HexColor("#EDF1F3")
GOLD = HexColor("#B8924A")
GOLD_DEEP = HexColor("#9A7838")
TERRA = HexColor("#C2734D")
TERRA_DARK = HexColor("#A0522D")
OFF_WHITE = HexColor("#FAFAF9")
WHITE = colors.white
GRAY_LINE = HexColor("#CFD6DA")
GRAY_SOFT = HexColor("#5C6970")


# --- Pull course data from course-content.js via Node ---

def load_course():
    node_script = """
    const fs = require('fs');
    const window = {};
    const fn = new Function('window', fs.readFileSync('course-content.js','utf8'));
    fn(window);
    console.log(JSON.stringify(window.BIO304_COURSE_CONTENT));
    """
    result = subprocess.run(
        ["node", "-e", node_script],
        capture_output=True, text=True, check=True,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    return json.loads(result.stdout)


COURSE = load_course()


# --- Compact styles ---

styles = getSampleStyleSheet()

S = {
    "module_eyebrow": ParagraphStyle(
        "module_eyebrow", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=7.5, leading=9,
        textColor=TERRA_DARK, spaceAfter=2,
    ),
    "module_title": ParagraphStyle(
        "module_title", parent=styles["Title"],
        fontName="Helvetica-Bold", fontSize=16, leading=20,
        textColor=NAVY, spaceAfter=2, alignment=TA_LEFT,
    ),
    "module_sub": ParagraphStyle(
        "module_sub", parent=styles["Normal"],
        fontName="Times-Italic", fontSize=9.5, leading=12,
        textColor=GRAY_SOFT, spaceAfter=6,
    ),
    "topic_eyebrow": ParagraphStyle(
        "topic_eyebrow", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=7.5, leading=9,
        textColor=TERRA_DARK, spaceAfter=1,
    ),
    "topic_title": ParagraphStyle(
        "topic_title", parent=styles["Heading1"],
        fontName="Helvetica-Bold", fontSize=14, leading=17,
        textColor=NAVY, spaceBefore=2, spaceAfter=2,
    ),
    "topic_summary": ParagraphStyle(
        "topic_summary", parent=styles["Normal"],
        fontName="Times-Italic", fontSize=9.5, leading=12,
        textColor=GRAY_SOFT, spaceAfter=4,
    ),
    "section_header": ParagraphStyle(
        "section_header", parent=styles["Heading2"],
        fontName="Helvetica-Bold", fontSize=10.5, leading=13,
        textColor=TERRA_DARK, spaceBefore=6, spaceAfter=2,
        keepWithNext=1,
    ),
    "sub_header": ParagraphStyle(
        "sub_header", parent=styles["Heading3"],
        fontName="Helvetica-Bold", fontSize=9.5, leading=12,
        textColor=NAVY, spaceBefore=4, spaceAfter=1,
        keepWithNext=1,
    ),
    "body": ParagraphStyle(
        "body", parent=styles["Normal"],
        fontName="Times-Roman", fontSize=9.5, leading=12.5,
        textColor=NAVY, spaceAfter=3, alignment=TA_LEFT,
    ),
    "bullet": ParagraphStyle(
        "bullet", parent=styles["Normal"],
        fontName="Times-Roman", fontSize=9.5, leading=12.5,
        textColor=NAVY, leftIndent=14, bulletIndent=2,
        spaceBefore=0, spaceAfter=1,
    ),
}


# --- Header and footer ---

def _header_footer(canv, doc, module_label):
    canv.saveState()
    page_num = canv.getPageNumber()
    # Top: running header on every page (including the first; helpful for grab-and-go reference)
    canv.setFont("Helvetica-Bold", 7.5)
    canv.setFillColor(TERRA_DARK)
    canv.drawString(0.55 * inch, letter[1] - 0.35 * inch, module_label.upper())
    canv.setStrokeColor(GRAY_LINE)
    canv.setLineWidth(0.5)
    canv.line(0.55 * inch, letter[1] - 0.42 * inch,
              letter[0] - 0.55 * inch, letter[1] - 0.42 * inch)
    # Footer
    canv.setFont("Times-Italic", 8)
    canv.setFillColor(GRAY_SOFT)
    canv.drawString(0.55 * inch, 0.38 * inch, "Dr. Sharilyn Rennie  .  BIO 304 Teaching Guide")
    canv.drawRightString(letter[0] - 0.55 * inch, 0.38 * inch, f"Page {page_num}")
    canv.restoreState()


# --- Build helpers ---

def safe_html(text):
    if text is None:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def split_into_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def module_header_flowables(module, module_idx, total_modules):
    flow = []
    flow.append(Paragraph(
        f"BIO 304  .  HUMAN ANATOMY &amp; PHYSIOLOGY  .  WEEK {module['week']}  .  MODULE {module_idx} OF {total_modules}",
        S["module_eyebrow"]
    ))
    flow.append(Paragraph(f"Module {module_idx}: {safe_html(module['title'])}", S["module_title"]))
    topic_names = ", ".join(t["title"] for t in module["topics"])
    flow.append(Paragraph(
        f"Topics: {safe_html(topic_names)}",
        S["module_sub"]
    ))
    flow.append(HRFlowable(width="100%", thickness=1.2, color=GOLD_DEEP, spaceBefore=2, spaceAfter=6))
    return flow


def topic_flowables(topic, idx, total, module_week, is_first):
    teach = TEACHING.get(topic["id"], {})
    if not teach:
        return [Paragraph(f"[No teaching content yet for {topic['id']}]", S["body"])]

    flow = []
    if not is_first:
        # Light divider between topics on the same page
        flow.append(HRFlowable(width="40%", thickness=0.8, color=GRAY_LINE,
                               spaceBefore=10, spaceAfter=6, hAlign="LEFT"))

    dok1 = sum(1 for c in topic["cards"] if c["dok"] == 1)
    dok2 = sum(1 for c in topic["cards"] if c["dok"] == 2)
    dok3 = sum(1 for c in topic["cards"] if c["dok"] == 3)
    eyebrow = (f"TOPIC {idx} OF {total}  .  WEEK {module_week}  .  "
               f"{len(topic['cards'])} CARDS  ({dok1} DOK 1 / {dok2} DOK 2 / {dok3} DOK 3)")
    # Keep the topic title block together so it never strands the heading at the bottom of a page
    title_block = [
        Paragraph(eyebrow, S["topic_eyebrow"]),
        Paragraph(safe_html(topic["title"]), S["topic_title"]),
    ]
    if topic.get("summary"):
        title_block.append(Paragraph(safe_html(topic["summary"]), S["topic_summary"]))
    flow.append(KeepTogether(title_block))

    # Section 1: The Science
    flow.append(Paragraph("The Science", S["section_header"]))
    for p in split_into_paragraphs(teach["science"]):
        flow.append(Paragraph(safe_html(p), S["body"]))

    # Section 2: Teaching This Topic
    flow.append(Paragraph("Teaching This Topic", S["section_header"]))

    teaching = teach["teaching"]
    flow.append(Paragraph("Before the video (drawing prompt)", S["sub_header"]))
    flow.append(Paragraph(safe_html(teaching["before_video"]), S["body"]))

    flow.append(Paragraph("Common misconceptions to address", S["sub_header"]))
    miscon_items = [ListItem(Paragraph(safe_html(m), S["bullet"]), leftIndent=10, bulletColor=GOLD_DEEP)
                    for m in teaching["misconceptions"]]
    flow.append(ListFlowable(miscon_items, bulletType="bullet", start="circle", leftIndent=14))

    flow.append(Paragraph("Order of operations (what to teach first)", S["sub_header"]))
    flow.append(Paragraph(safe_html(teaching["order"]), S["body"]))

    flow.append(Paragraph("Self-test prompts", S["sub_header"]))
    test_items = [ListItem(Paragraph(safe_html(t), S["bullet"]), leftIndent=10, bulletColor=NAVY)
                  for t in teaching["self_test"]]
    flow.append(ListFlowable(test_items, bulletType="bullet", start="circle", leftIndent=14))

    # Section 3: Why This Matters (clinical)
    flow.append(Paragraph("Why This Matters to Your Patients", S["section_header"]))
    for p in split_into_paragraphs(teach["clinical"]):
        flow.append(Paragraph(safe_html(p), S["body"]))

    return flow


def slugify(text):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return s


def build_module_pdf(module, module_idx, total_modules, out_dir):
    module_slug = slugify(module["title"])
    filename = f"BIO-304-Module-{module_idx:02d}-{module_slug}.pdf"
    out_path = os.path.join(out_dir, filename)

    label = f"Module {module_idx}: {module['title']}  .  Week {module['week']}"

    doc = SimpleDocTemplate(
        out_path,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title=f"BIO 304 Module {module_idx}: {module['title']}",
        author="Dr. Sharilyn Rennie",
        subject="BIO 304 Teaching Guide",
    )

    story = []
    story.extend(module_header_flowables(module, module_idx, total_modules))

    total_topics = len(module["topics"])
    for i, topic in enumerate(module["topics"], start=1):
        story.extend(topic_flowables(topic, i, total_topics, module["week"], is_first=(i == 1)))

    def on_page(canv, doc_):
        _header_footer(canv, doc_, label)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return out_path, filename


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    total = len(COURSE["modules"])
    built = []
    for i, m in enumerate(COURSE["modules"], start=1):
        path, name = build_module_pdf(m, i, total, out_dir)
        size_kb = os.path.getsize(path) // 1024
        built.append((name, size_kb))
        print(f"  built: {name}  ({size_kb} KB)")
    print(f"\nbuilt {len(built)} PDFs.")
    return built


if __name__ == "__main__":
    main()
