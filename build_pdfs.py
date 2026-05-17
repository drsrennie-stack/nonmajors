"""
Build 17 per-module teaching PDFs from course-content.js + teaching_content.py.
Output: BIO-304-Module-XX-<slug>.pdf in this directory.
"""

import json
import os
import re
import subprocess
import sys
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, HRFlowable, ListFlowable, ListItem
)
from reportlab.pdfgen import canvas
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


# --- Reusable styles ---

styles = getSampleStyleSheet()

S = {
    "eyebrow": ParagraphStyle(
        "eyebrow", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=8, leading=10,
        textColor=TERRA_DARK, spaceAfter=4, alignment=TA_LEFT
    ),
    "cover_title": ParagraphStyle(
        "cover_title", parent=styles["Title"],
        fontName="Helvetica-Bold", fontSize=28, leading=34,
        textColor=NAVY, spaceAfter=10, alignment=TA_LEFT
    ),
    "cover_subtitle": ParagraphStyle(
        "cover_subtitle", parent=styles["Heading2"],
        fontName="Helvetica-Bold", fontSize=16, leading=22,
        textColor=TERRA_DARK, spaceAfter=20, alignment=TA_LEFT
    ),
    "cover_intro": ParagraphStyle(
        "cover_intro", parent=styles["Normal"],
        fontName="Times-Italic", fontSize=11, leading=16,
        textColor=GRAY_SOFT, spaceAfter=20, alignment=TA_LEFT
    ),
    "cover_topic": ParagraphStyle(
        "cover_topic", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=12, leading=16,
        textColor=NAVY, spaceAfter=4, leftIndent=8
    ),
    "cover_topic_sub": ParagraphStyle(
        "cover_topic_sub", parent=styles["Normal"],
        fontName="Times-Italic", fontSize=10, leading=14,
        textColor=GRAY_SOFT, spaceAfter=10, leftIndent=8
    ),
    "topic_eyebrow": ParagraphStyle(
        "topic_eyebrow", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=8, leading=10,
        textColor=TERRA_DARK, spaceAfter=4, alignment=TA_LEFT
    ),
    "topic_title": ParagraphStyle(
        "topic_title", parent=styles["Heading1"],
        fontName="Helvetica-Bold", fontSize=20, leading=24,
        textColor=NAVY, spaceAfter=6, alignment=TA_LEFT
    ),
    "topic_summary": ParagraphStyle(
        "topic_summary", parent=styles["Normal"],
        fontName="Times-Italic", fontSize=11, leading=16,
        textColor=GRAY_SOFT, spaceAfter=14, alignment=TA_LEFT
    ),
    "section_header": ParagraphStyle(
        "section_header", parent=styles["Heading2"],
        fontName="Helvetica-Bold", fontSize=14, leading=18,
        textColor=TERRA_DARK, spaceBefore=10, spaceAfter=8, alignment=TA_LEFT
    ),
    "sub_header": ParagraphStyle(
        "sub_header", parent=styles["Heading3"],
        fontName="Helvetica-Bold", fontSize=11, leading=14,
        textColor=NAVY, spaceBefore=8, spaceAfter=4, alignment=TA_LEFT
    ),
    "body": ParagraphStyle(
        "body", parent=styles["Normal"],
        fontName="Times-Roman", fontSize=11, leading=16,
        textColor=NAVY, spaceAfter=8, alignment=TA_LEFT
    ),
    "bullet": ParagraphStyle(
        "bullet", parent=styles["Normal"],
        fontName="Times-Roman", fontSize=10.5, leading=15,
        textColor=NAVY, leftIndent=22, bulletIndent=8,
        spaceBefore=2, spaceAfter=2, alignment=TA_LEFT
    ),
}


# --- Header and footer ---

def _header_footer(canv, doc, module_label):
    canv.saveState()
    page_num = canv.getPageNumber()
    # Skip header on the cover page (page 1)
    if page_num > 1:
        # Top: small module label, navy
        canv.setFont("Helvetica-Bold", 8)
        canv.setFillColor(TERRA_DARK)
        canv.drawString(0.75 * inch, letter[1] - 0.45 * inch, module_label.upper())
        # Top rule
        canv.setStrokeColor(GRAY_LINE)
        canv.setLineWidth(0.5)
        canv.line(0.75 * inch, letter[1] - 0.55 * inch,
                  letter[0] - 0.75 * inch, letter[1] - 0.55 * inch)
    # Footer
    canv.setFont("Times-Italic", 9)
    canv.setFillColor(GRAY_SOFT)
    canv.drawString(0.75 * inch, 0.5 * inch, "Dr. Sharilyn Rennie  .  BIO 304 Teaching Guide")
    canv.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"Page {page_num}")
    canv.restoreState()


# --- Build helpers ---

def safe_html(text):
    """Escape characters that ReportLab's Paragraph parser treats as markup."""
    if text is None:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def split_into_paragraphs(text):
    """Split body text into paragraphs on blank lines (after \\n\\n)."""
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def topic_flowables(topic, idx, total, module_week):
    teach = TEACHING.get(topic["id"], {})
    if not teach:
        return [Paragraph(f"[No teaching content yet for {topic['id']}]", S["body"])]

    flow = []
    eyebrow = f"TOPIC {idx} OF {total}  .  WEEK {module_week}  .  {len(topic['cards'])} CARDS  ({sum(1 for c in topic['cards'] if c['dok']==1)} DOK 1  /  {sum(1 for c in topic['cards'] if c['dok']==2)} DOK 2  /  {sum(1 for c in topic['cards'] if c['dok']==3)} DOK 3)"
    flow.append(Paragraph(eyebrow, S["topic_eyebrow"]))
    flow.append(Paragraph(safe_html(topic["title"]), S["topic_title"]))
    if topic.get("summary"):
        flow.append(Paragraph(safe_html(topic["summary"]), S["topic_summary"]))
    flow.append(HRFlowable(width="100%", thickness=1, color=GOLD_DEEP, spaceBefore=2, spaceAfter=10))

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
    miscon_items = [ListItem(Paragraph(safe_html(m), S["bullet"]), leftIndent=12, bulletColor=GOLD_DEEP)
                    for m in teaching["misconceptions"]]
    flow.append(ListFlowable(miscon_items, bulletType="bullet", start="circle", leftIndent=18))

    flow.append(Paragraph("Order of operations (what to teach first)", S["sub_header"]))
    flow.append(Paragraph(safe_html(teaching["order"]), S["body"]))

    flow.append(Paragraph("Self-test prompts (for students before the recall deck)", S["sub_header"]))
    test_items = [ListItem(Paragraph(safe_html(t), S["bullet"]), leftIndent=12, bulletColor=NAVY)
                  for t in teaching["self_test"]]
    flow.append(ListFlowable(test_items, bulletType="bullet", start="circle", leftIndent=18))

    # Section 3: Why This Matters (clinical)
    flow.append(Paragraph("Why This Matters to Your Patients", S["section_header"]))
    for p in split_into_paragraphs(teach["clinical"]):
        flow.append(Paragraph(safe_html(p), S["body"]))

    flow.append(Spacer(1, 14))
    flow.append(HRFlowable(width="100%", thickness=0.5, color=GRAY_LINE, spaceBefore=4, spaceAfter=4))
    flow.append(PageBreak())
    return flow


def cover_flowables(module, module_idx, total_modules):
    flow = []
    flow.append(Spacer(1, 60))
    flow.append(Paragraph("BIO 304  .  HUMAN ANATOMY &amp; PHYSIOLOGY  .  MEDMASTERS COLLABORATIVE", S["eyebrow"]))
    flow.append(Paragraph(f"Module {module_idx}: {safe_html(module['title'])}", S["cover_title"]))
    flow.append(Paragraph(f"Week {module['week']} teaching guide  .  {len(module['topics'])} topic{'s' if len(module['topics']) != 1 else ''}", S["cover_subtitle"]))
    flow.append(Paragraph(
        "This is the instructor-facing companion to the student pre-work hub. For every topic, "
        "you have the science to teach, the recommended approach to learning that material, and "
        "why it matters to your students' future patients. Lecture order, common misconceptions, "
        "and pre-video drawing prompts are baked in so each video lesson can hit the same "
        "pedagogical beats.",
        S["cover_intro"]
    ))
    flow.append(Spacer(1, 18))
    flow.append(Paragraph("Topics in this module", S["section_header"]))
    for i, t in enumerate(module["topics"], start=1):
        flow.append(Paragraph(f"{i}. {safe_html(t['title'])}", S["cover_topic"]))
        flow.append(Paragraph(safe_html(t.get("summary", "")), S["cover_topic_sub"]))
    flow.append(Spacer(1, 30))
    flow.append(HRFlowable(width=2.5 * inch, thickness=2, color=GOLD_DEEP, spaceBefore=10, spaceAfter=10))
    flow.append(Paragraph(
        f"Module {module_idx} of {total_modules}  .  Dr. Sharilyn Rennie",
        S["topic_eyebrow"]
    ))
    flow.append(PageBreak())
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
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.75 * inch,
        title=f"BIO 304 Module {module_idx}: {module['title']}",
        author="Dr. Sharilyn Rennie",
        subject="BIO 304 Teaching Guide",
    )

    story = []
    story.extend(cover_flowables(module, module_idx, total_modules))

    total_topics = len(module["topics"])
    for i, topic in enumerate(module["topics"], start=1):
        story.extend(topic_flowables(topic, i, total_topics, module["week"]))

    # Drop the trailing PageBreak from the last topic to avoid an empty final page
    while story and isinstance(story[-1], PageBreak):
        story.pop()

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
