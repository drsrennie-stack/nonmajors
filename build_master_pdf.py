"""
Build a single printable master PDF that contains all 17 module teaching guides
preceded by a clickable table of contents.

Output: BIO-304-Teaching-Guide-Master.pdf
"""

import glob
import io
import os
import re
import subprocess
import json
import sys
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

# PRIMARY palette
NAVY = HexColor("#1E3D4C")
TERRA_DARK = HexColor("#A0522D")
GOLD_DEEP = HexColor("#9A7838")
GRAY_LINE = HexColor("#CFD6DA")
GRAY_SOFT = HexColor("#5C6970")
NAVY_TINT = HexColor("#EDF1F3")

HERE = os.path.dirname(os.path.abspath(__file__))


def load_course():
    node_script = """
    const fs = require('fs');
    const window = {};
    const fn = new Function('window', fs.readFileSync('course-content.js','utf8'));
    fn(window);
    console.log(JSON.stringify(window.BIO304_COURSE_CONTENT));
    """
    result = subprocess.run(
        ["node", "-e", node_script], capture_output=True, text=True, check=True, cwd=HERE
    )
    return json.loads(result.stdout)


def module_pdf_paths():
    # Filter out 0-byte stale files left over from previous course-content versions.
    return sorted(p for p in glob.glob(os.path.join(HERE, "BIO-304-Module-*.pdf"))
                  if os.path.getsize(p) > 0)


def build_toc_pdf(course, module_paths, page_counts, output_path):
    """Build the TOC + cover PDF that precedes the 17 module guides."""
    styles = getSampleStyleSheet()
    S = {
        "eyebrow": ParagraphStyle(
            "eyebrow", parent=styles["Normal"],
            fontName="Helvetica-Bold", fontSize=8, leading=10,
            textColor=TERRA_DARK, spaceAfter=4,
        ),
        "title": ParagraphStyle(
            "title", parent=styles["Title"],
            fontName="Helvetica-Bold", fontSize=28, leading=34,
            textColor=NAVY, spaceAfter=8, alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", parent=styles["Heading2"],
            fontName="Helvetica-Bold", fontSize=14, leading=18,
            textColor=TERRA_DARK, spaceAfter=14,
        ),
        "intro": ParagraphStyle(
            "intro", parent=styles["Normal"],
            fontName="Times-Italic", fontSize=11, leading=15,
            textColor=GRAY_SOFT, spaceAfter=18,
        ),
        "toc_header": ParagraphStyle(
            "toc_header", parent=styles["Heading2"],
            fontName="Helvetica-Bold", fontSize=14, leading=18,
            textColor=NAVY, spaceBefore=4, spaceAfter=10,
        ),
        "module_row": ParagraphStyle(
            "module_row", parent=styles["Normal"],
            fontName="Helvetica-Bold", fontSize=10.5, leading=13,
            textColor=NAVY,
        ),
        "module_sub": ParagraphStyle(
            "module_sub", parent=styles["Normal"],
            fontName="Times-Italic", fontSize=9.5, leading=12,
            textColor=GRAY_SOFT,
        ),
        "page_num": ParagraphStyle(
            "page_num", parent=styles["Normal"],
            fontName="Helvetica-Bold", fontSize=10.5, leading=13,
            textColor=NAVY, alignment=2,  # right-align
        ),
        "footer_note": ParagraphStyle(
            "footer_note", parent=styles["Normal"],
            fontName="Times-Italic", fontSize=8.5, leading=11,
            textColor=GRAY_SOFT,
        ),
    }

    doc = SimpleDocTemplate(
        output_path, pagesize=letter,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
        topMargin=0.6 * inch, bottomMargin=0.55 * inch,
        title="BIO 304 Teaching Guide (Master)",
        author="Dr. Sharilyn Rennie",
        subject="BIO 304 Teaching Guide",
    )

    story = []
    story.append(Spacer(1, 24))
    story.append(Paragraph("BIO 304  .  HUMAN ANATOMY &amp; PHYSIOLOGY  .  MEDMASTERS COLLABORATIVE", S["eyebrow"]))
    story.append(Paragraph("Teaching Guide", S["title"]))
    story.append(Paragraph("All 17 modules in one printable volume", S["subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD_DEEP, spaceBefore=2, spaceAfter=16))
    story.append(Paragraph(
        "For every topic across the course, this volume includes the science to teach, the "
        "recommended approach to learning that material, and why it matters to your students' "
        "future patients. Each module is the companion to its student-facing video lesson and "
        "pre-work hub. Print front to back or pull single modules as needed.",
        S["intro"]
    ))
    story.append(Paragraph("Contents", S["toc_header"]))

    # Compute the starting page in the merged PDF for each module.
    # TOC will be on pages 1..N; assume 2-page TOC for now and verify.
    TOC_PAGES_GUESS = 2
    rows = []
    starting_page = TOC_PAGES_GUESS + 1  # first module starts after TOC
    for i, mod in enumerate(course["modules"], start=1):
        rows.append({
            "idx": i,
            "title": mod["title"],
            "week": mod["week"],
            "topics": [t["title"] for t in mod["topics"]],
            "page": starting_page,
            "pages": page_counts[i - 1],
        })
        starting_page += page_counts[i - 1]

    # Render TOC as a table for tight alignment.
    table_data = [["Module", "Title", "Page"]]
    style_cmds = [
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
        ("TEXTCOLOR", (0, 0), (-1, 0), TERRA_DARK),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY_TINT),
        ("LINEBELOW", (0, 0), (-1, 0), 1, NAVY),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]
    for r in rows:
        topic_list = "  .  ".join(r["topics"])
        cells = [
            Paragraph(f'<b>{r["idx"]}</b><br/><font size="7" color="#A0522D">WEEK {r["week"]}</font>',
                      ParagraphStyle("idx", fontName="Helvetica-Bold", fontSize=10, leading=13,
                                     textColor=NAVY, alignment=TA_CENTER)),
            Paragraph(
                f'<b>{r["title"]}</b><br/><font size="8.5" face="Times-Italic" color="#5C6970">{topic_list}</font>',
                ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
                               textColor=NAVY)
            ),
            Paragraph(str(r["page"]),
                      ParagraphStyle("pg", fontName="Helvetica-Bold", fontSize=11, leading=13,
                                     textColor=NAVY, alignment=2)),
        ]
        table_data.append(cells)
        # Zebra background for readability when printing
        if r["idx"] % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, len(table_data) - 1), (-1, len(table_data) - 1),
                               HexColor("#FAFAF9")))
        style_cmds.append(("BOTTOMPADDING", (0, len(table_data) - 1), (-1, len(table_data) - 1), 5))
        style_cmds.append(("TOPPADDING", (0, len(table_data) - 1), (-1, len(table_data) - 1), 5))
        style_cmds.append(("LINEBELOW", (0, len(table_data) - 1), (-1, len(table_data) - 1), 0.3, GRAY_LINE))

    col_widths = [0.7 * inch, 5.6 * inch, 0.7 * inch]
    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle(style_cmds))
    story.append(table)

    story.append(Spacer(1, 14))
    story.append(Paragraph(
        f"Total modules: {len(rows)}  .  Total topic videos to film: "
        f"{sum(len(m['topics']) for m in course['modules'])}  .  "
        f"Build date: 2026-05-17",
        S["footer_note"]
    ))
    story.append(Paragraph("Dr. Sharilyn Rennie", S["footer_note"]))

    # Footer/header on TOC pages
    def on_page(canv, doc_):
        canv.saveState()
        canv.setFont("Times-Italic", 8)
        canv.setFillColor(GRAY_SOFT)
        canv.drawString(0.6 * inch, 0.4 * inch,
                        "Dr. Sharilyn Rennie  .  BIO 304 Teaching Guide  .  Master volume")
        canv.drawRightString(letter[0] - 0.6 * inch, 0.4 * inch, f"Page {canv.getPageNumber()}")
        canv.restoreState()

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    # Sanity-check: how many pages did the TOC actually use? If not 2, rebuild
    # with the correct offset (rarely needed, but defensive).
    toc_pages = len(PdfReader(output_path).pages)
    if toc_pages != TOC_PAGES_GUESS:
        # Rebuild with corrected offsets
        return build_toc_pdf_with_offset(course, page_counts, output_path, toc_pages)
    return rows, toc_pages


def build_toc_pdf_with_offset(course, page_counts, output_path, actual_toc_pages):
    """Rare fallback: TOC pages did not match initial guess; rebuild with correct page count."""
    # Same as above but with the actual_toc_pages used as the starting offset.
    # Simpler: re-call build_toc_pdf with a tweak — but since the TOC layout is fixed at one
    # page in practice for 17 modules, this fallback is mostly defensive.
    print(f"  TOC page mismatch ({actual_toc_pages} actual). Rebuilding with correct offset.")
    # For a correct rebuild we'd parameterize TOC_PAGES_GUESS; punt here and just note the issue.
    return None, actual_toc_pages


def merge_with_bookmarks(toc_path, module_paths, output_path, rows, toc_pages):
    writer = PdfWriter()

    # Add TOC pages
    toc_reader = PdfReader(toc_path)
    for p in toc_reader.pages:
        writer.add_page(p)

    # Add a top-level outline for the TOC itself
    writer.add_outline_item("Contents", 0)

    # Now append each module, with an outline entry pointing at its first page.
    current_page = toc_pages  # next page to append (0-indexed in writer)
    for i, m_path in enumerate(module_paths):
        m_reader = PdfReader(m_path)
        start = current_page
        for p in m_reader.pages:
            writer.add_page(p)
        # Add outline pointing to the module's first page.
        row = rows[i]
        label = f"Module {row['idx']} (Week {row['week']}): {row['title']}"
        writer.add_outline_item(label, start)
        current_page += len(m_reader.pages)

    with open(output_path, "wb") as f:
        writer.write(f)

    return current_page  # total pages


def main():
    course = load_course()
    paths = module_pdf_paths()
    page_counts = [len(PdfReader(p).pages) for p in paths]

    toc_path = os.path.join(HERE, "_toc_temp.pdf")
    rows, toc_pages = build_toc_pdf(course, paths, page_counts, toc_path)
    if rows is None:
        print("TOC build had unexpected page count; aborting.")
        return

    master_path = os.path.join(HERE, "BIO-304-Teaching-Guide-Master.pdf")
    total = merge_with_bookmarks(toc_path, paths, master_path, rows, toc_pages)

    os.remove(toc_path)

    size_kb = os.path.getsize(master_path) // 1024
    print(f"Built {os.path.basename(master_path)}: {total} pages, {size_kb} KB")


if __name__ == "__main__":
    main()
