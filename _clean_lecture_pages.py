"""
One-shot cleaner for the 5 uploaded lecture one-pagers.

For each file:
  1. Replace MedMasters Collaborative branding with American River College.
  2. Update SHEET_CONFIG.prework to point at bio304-spaced-recall-prototype.html.
  3. Inject a small <script> just before </body> that wires the prework link:
     when clicked, set localStorage["bio304-video-{topicId}"] = "true" before
     navigating, so the spaced recall app's video gate unlocks for that topic.

Lecture pages without a direct course-content.js topic mapping (body-regions,
body-cavities) keep the rebrand and prework link, but do NOT set a flag — they
are supplementary deep-dives, not the primary gate-setting lecture page.
"""

import os
import re
import shutil

UPLOADS = "/sessions/gallant-busy-fermat/mnt/uploads"
OUTPUTS = "/sessions/gallant-busy-fermat/mnt/outputs"

# Map filename -> course-content.js topic id (or None if supplementary).
MAPPING = {
    "levels-of-organization.html":   "t-levels-of-organization",
    "anatomical-position.html":      "t-anatomical-terminology",
    "homeostasis-feedback.html":     "t-homeostasis",
    "body-regions.html":             None,  # supplementary to t-anatomical-terminology
    "body-cavities.html":            None,  # supplementary to t-anatomical-terminology
}

PREWORK_URL = "bio304-spaced-recall-prototype.html"


def clean_one(fname, topic_id):
    src = os.path.join(UPLOADS, fname)
    dst = os.path.join(OUTPUTS, fname)
    with open(src, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Rebrand: MedMasters Collaborative -> American River College
    html = html.replace("MEDMASTERS COLLABORATIVE", "AMERICAN RIVER COLLEGE")
    html = html.replace("MedMasters Collaborative", "American River College")
    html = html.replace("MedMasters", "American River College")

    # 1b. Replace em/en dashes with commas (per Scrubs's global rule).
    html = html.replace("—", ", ")
    html = html.replace("–", "-")

    # 2. Update SHEET_CONFIG.prework
    html = re.sub(
        r"prework:\s*'https://REPLACE_WITH_YOUR_SR_DOMAIN/prework/[^']*'",
        "prework: '" + PREWORK_URL + "'",
        html,
    )

    # 3. Inject the flag-setting + iframe height-sender + target="_top" script
    #    just before </body>. Idempotent: skip if already injected.
    sentinel = "<!-- bio304-lecture-gate-wired -->"
    if sentinel not in html:
        topic_js = (
            "    var TOPIC_ID = " + (
                "'" + topic_id + "'" if topic_id else "null"
            ) + ";\n"
        )
        injection = (
            "\n" + sentinel + "\n"
            "<script>\n"
            "// Cross-page video gate: when a student clicks 'Go to the pre-work',\n"
            "// set the localStorage flag the spaced recall app reads to unlock Step 2.\n"
            "(function () {\n"
            + topic_js +
            "  var pre = document.getElementById('prework-link');\n"
            "  if (!pre) return;\n"
            "  pre.addEventListener('click', function () {\n"
            "    if (!TOPIC_ID) return;\n"
            "    try { window.localStorage.setItem('bio304-video-' + TOPIC_ID, 'true'); } catch (e) {}\n"
            "  });\n"
            "})();\n"
            "// Iframe height-sender for Canvas/Kajabi embeds (no-op if loaded top-level).\n"
            "(function () {\n"
            "  if (window.self === window.top) return;\n"
            "  function send() {\n"
            "    try {\n"
            "      var h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);\n"
            "      window.parent.postMessage({ id: 'bio304-lecture-page', type: 'resize', height: h }, '*');\n"
            "    } catch (e) {}\n"
            "  }\n"
            "  window.addEventListener('load', send);\n"
            "  window.addEventListener('resize', send);\n"
            "  if ('ResizeObserver' in window) new ResizeObserver(send).observe(document.body);\n"
            "})();\n"
            "</script>\n"
        )
        html = html.replace("</body>", injection + "</body>", 1)

    # 4. Defensive em-dash check (should be zero after step 1b)
    if "—" in html or "–" in html:
        raise SystemExit("Em/en dash STILL present in " + fname)

    with open(dst, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(dst)


def main():
    for fname, tid in MAPPING.items():
        size = clean_one(fname, tid)
        kb = size // 1024
        flag = "(flag: " + tid + ")" if tid else "(no flag)"
        print(f"  {fname:34s}  {kb:5d} KB  {flag}")
    print("\nDone.")


if __name__ == "__main__":
    main()
