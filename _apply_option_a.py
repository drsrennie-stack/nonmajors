"""
Apply Option A to every lecture one-pager:
  - Move the explain-back gate from the spaced recall app to the lecture page.
  - The lecture page becomes: video → inline explain gate → unlock cards.
  - The spaced recall app becomes: cards only (no gate UI).

For each lecture page:
  1. Strip any previous injection (the old post-video modal block).
  2. Rebrand: MedMasters → American River College. Em/en dashes scrubbed.
  3. Update SHEET_CONFIG.prework to the spaced recall app deep-linked to that topic.
  4. Inject CSS for the new gate section.
  5. Inject the gate HTML before </main>.
  6. Inject the gate JS that:
       - Listens for YouTube video end (state 0)
       - Reveals the gate section
       - Validates 60+ words AND >=60% of topic's gateKeywords
       - On submit: writes localStorage['bio304-gate-{topicId}'] = 'true'
                    AND localStorage['bio304-video-{topicId}'] = 'true'
                    AND enables the prework button
       - Prework button click navigates to the spaced recall app's topic deep link.
  7. Iframe height-sender stays.
"""

import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "_lecture_src")

# filename -> topic_id (None means supplementary, no flag-setting)
MAPPING = {
    "levels-of-organization.html":     "t-levels-of-organization",
    "anatomical-position.html":        "t-anatomical-terminology",
    "body-regions.html":               None,
    "body-cavities.html":              None,
    "homeostasis-feedback.html":       "t-homeostasis",
    "cell-structure.html":             "t-cell-structure",
    "membrane-transport.html":         "t-membrane-transport",
    "epithelial-tissue.html":          "t-epithelial-tissue",
    "connective-tissues.html":         "t-connective-tissue",
    "muscle-nervous-tissue.html":      "t-muscle-nervous-tissue",
    "bone-tissue.html":                "t-bone-tissue",
    "axial-skeleton.html":             "t-axial-skeleton",
    "appendicular-skeleton.html":      "t-appendicular-skeleton",
    "joints-and-movements.html":       "t-joints-movements",
    "cross-bridge-cycle.html":         "t-sliding-filament",
    "motor-units.html":                "t-motor-units",
    "neurons-resting-potential.html":  "t-neurons-rmp",
    "action-potentials-synapses.html": "t-action-potentials",
    "cns-organization.html":           "t-cns-organization",
    "pns-autonomic.html":              "t-pns-autonomic",
    "hearing-equilibrium.html":        "t-hearing-equilibrium",
    "hormone-mechanisms.html":         "t-hormone-mechanisms",
    "major-endocrine-glands.html":     "t-major-glands",
    "blood-composition.html":          "t-blood-composition",
    "hemostasis-blood-typing.html":    "t-hemostasis-blood-typing",
    "heart-anatomy.html":              "t-heart-cardiac-cycle",
    "cardiac-conduction.html":         "t-conduction-ecg",
    "blood-vessels-hemodynamics.html": "t-vessels-hemodynamics",
    "lymphatic-innate-immunity.html":  "t-lymphatic-innate",
    "adaptive-immunity.html":          "t-adaptive-immunity",
    "respiratory-anatomy.html":        "t-resp-anatomy-mechanics",
    "gas-exchange-transport.html":     "t-gas-exchange-transport",
    "gi-anatomy-motility.html":        "t-gi-anatomy-motility",
    "digestion-absorption.html":       "t-digestion-absorption",
    "kidney-anatomy-gfr.html":         "t-kidney-filtration",
    "fluid-electrolyte-acid-base.html": "t-fluid-acid-base",
    "male-reproductive.html":          "t-male-reproductive",
    "female-reproductive.html":        "t-female-reproductive",
    "pregnancy-basics.html":           "t-pregnancy-development",
}

PREWORK_URL = "bio304-spaced-recall-prototype.html"


def load_course():
    proc = subprocess.run(
        ["node", "-e",
         "const w={};new Function('window',require('fs').readFileSync('course-content.js','utf8'))(w);"
         "console.log(JSON.stringify(w.BIO304_COURSE_CONTENT))"],
        cwd=HERE, capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


def gate_keywords_for(topic_id, course):
    if not topic_id:
        return []
    for mod in course["modules"]:
        for t in mod["topics"]:
            if t["id"] == topic_id:
                return t.get("gateKeywords", [])
    return []


GATE_CSS = """
  /* Option A: inline explain-back gate (was post-video modal) */
  #explain-gate { background: var(--card); border: 1px solid var(--rule); border-radius: 12px; padding: 26px 30px; margin: 32px 0 0; box-shadow: var(--card-shadow); }
  #explain-gate[hidden] { display: none; }
  #explain-gate .gate-eyebrow { font-family: 'DM Sans', system-ui, sans-serif; font-size: 11.5px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--terra-dark); margin: 0 0 6px; }
  #explain-gate h2 { font-family: 'Plus Jakarta Sans', system-ui, sans-serif; font-weight: 800; font-size: 22px; color: var(--navy); margin: 0 0 8px; letter-spacing: -0.01em; }
  #explain-gate p.gate-instr { font-family: 'Lora', Georgia, serif; font-size: 15.5px; color: var(--ink); line-height: 1.55; margin: 0 0 14px; }
  #gate-input { width: 100%; min-height: 140px; padding: 12px 14px; font-family: 'Lora', Georgia, serif; font-size: 15.5px; color: var(--ink); line-height: 1.55; border: 1px solid var(--rule); border-radius: 8px; background: #FFFFFF; resize: vertical; }
  #gate-input:focus-visible { outline: 3px solid var(--focus-ring); outline-offset: 1px; border-color: var(--navy); }
  #gate-meter { display: flex; gap: 18px; flex-wrap: wrap; margin: 12px 0 14px; font-family: 'DM Sans', system-ui, sans-serif; font-size: 13px; color: var(--ink-soft); }
  #gate-meter strong { color: var(--navy); font-weight: 700; font-variant-numeric: tabular-nums; }
  #gate-meter .met { color: var(--navy); }
  #gate-submit { font-family: 'DM Sans', system-ui, sans-serif; font-weight: 800; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; padding: 12px 22px; border-radius: 999px; border: 1px solid var(--navy); background: var(--navy); color: #FFFFFF; cursor: pointer; }
  #gate-submit:disabled { opacity: 0.5; cursor: not-allowed; }
  #gate-submit:not(:disabled):hover { background: var(--navy-deep, #142a36); }
  #gate-submit:focus-visible { outline: 3px solid var(--focus-ring); outline-offset: 3px; }
  #gate-status { font-family: 'DM Sans', system-ui, sans-serif; font-size: 12.5px; color: var(--terra); margin: 10px 0 0; min-height: 18px; }
  #gate-status.passed { color: var(--navy); font-weight: 700; }
  .video-watch-prompt { font-family: 'Lora', Georgia, serif; font-style: italic; color: var(--ink-soft); font-size: 14px; margin: 0; }
  /* Prework button locked state */
  .resource-btn.gate-locked { opacity: 0.55; cursor: not-allowed; pointer-events: auto; }
  .gate-hint { display: inline-block; margin-left: 10px; font-family: 'DM Sans', system-ui, sans-serif; font-size: 11.5px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--terra-dark); vertical-align: middle; }
  .gate-hint[hidden] { display: none; }
"""

GATE_HTML_TEMPLATE = """
  <!-- bio304-explain-gate (Option A) -->
  <section id="explain-gate" hidden aria-labelledby="explain-gate-h">
    <p class="gate-eyebrow">Step 2 . Retrieval check</p>
    <h2 id="explain-gate-h">Now explain it back, in your own words.</h2>
    <p class="gate-instr">In 60 words or more, pull together what the video just taught you. Include the key concepts. This is the point where the learning actually sticks. After you submit, your spaced-recall cards for this topic unlock.</p>
    <textarea id="gate-input" aria-describedby="gate-meter" placeholder="What did this video teach you?"></textarea>
    <div id="gate-meter" aria-live="polite">
      <span>Words: <strong id="gate-word-count">0</strong> / 60</span>
      <span>Concepts found: <strong id="gate-keyword-count">0</strong> / <span id="gate-keyword-target">0</span></span>
    </div>
    <button type="button" id="gate-submit" disabled>Unlock pre-work cards</button>
    <p id="gate-status" role="status"></p>
  </section>
"""


def build_gate_script(topic_id, gate_keywords, prework_target):
    """Return the JS block that wires the gate logic for one lecture page."""
    topic_js = "'" + topic_id + "'" if topic_id else "null"
    kw_js = json.dumps(gate_keywords)
    return f"""
<script>
// bio304-option-a: inline explain-back gate on the lecture page.
(function () {{
  var TOPIC_ID = {topic_js};
  var GATE_KEYWORDS = {kw_js};
  var PREWORK_TARGET = {json.dumps(prework_target)};
  var MIN_WORDS = 60;
  var MIN_KEYWORDS = GATE_KEYWORDS.length ? Math.max(2, Math.ceil(GATE_KEYWORDS.length * 0.6)) : 0;

  var pre = document.getElementById('prework-link');
  var gateSection = document.getElementById('explain-gate');
  var input = document.getElementById('gate-input');
  var submitBtn = document.getElementById('gate-submit');
  var statusEl = document.getElementById('gate-status');
  var wordCountEl = document.getElementById('gate-word-count');
  var kwCountEl = document.getElementById('gate-keyword-count');
  var kwTargetEl = document.getElementById('gate-keyword-target');
  if (kwTargetEl) kwTargetEl.textContent = String(MIN_KEYWORDS);

  // Lock the prework button by default. If this lecture page has no topic
  // mapping (supplementary pages like body-regions, body-cavities), leave
  // the prework button as a normal link with no flag-setting.
  if (!TOPIC_ID) {{
    // Supplementary page: hide the gate section entirely.
    if (gateSection) gateSection.remove();
    if (pre) pre.href = PREWORK_TARGET;
    return;
  }}

  if (pre) {{
    pre.classList.add('gate-locked');
    pre.setAttribute('aria-disabled', 'true');
    var hint = document.createElement('span');
    hint.className = 'gate-hint';
    hint.id = 'prework-gate-hint';
    hint.textContent = 'Watch the video and complete the retrieval check to unlock';
    if (pre.parentNode) pre.parentNode.insertBefore(hint, pre.nextSibling);
    pre.href = PREWORK_TARGET;
    pre.addEventListener('click', function (e) {{
      if (pre.classList.contains('gate-locked')) {{
        e.preventDefault();
        if (gateSection && gateSection.hidden) {{
          alert('Watch the video first. Then complete the retrieval check below.');
        }} else if (gateSection) {{
          gateSection.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          if (input) input.focus();
        }}
      }} else {{
        try {{ window.localStorage.setItem('bio304-gate-' + TOPIC_ID, 'true'); }} catch (er) {{}}
        try {{ window.localStorage.setItem('bio304-video-' + TOPIC_ID, 'true'); }} catch (er) {{}}
      }}
    }});
  }}

  // Validate the input
  function updateMeter() {{
    if (!input) return;
    var text = input.value.trim();
    var wordCount = text ? text.split(/\\s+/).filter(Boolean).length : 0;
    var lower = text.toLowerCase();
    var matched = GATE_KEYWORDS.filter(function (k) {{ return lower.indexOf(k.toLowerCase()) !== -1; }});
    if (wordCountEl) wordCountEl.textContent = String(wordCount);
    if (kwCountEl) kwCountEl.textContent = String(matched.length);
    if (wordCountEl) wordCountEl.parentElement.classList.toggle('met', wordCount >= MIN_WORDS);
    if (kwCountEl) kwCountEl.parentElement.classList.toggle('met', matched.length >= MIN_KEYWORDS);
    var passed = wordCount >= MIN_WORDS && matched.length >= MIN_KEYWORDS;
    if (submitBtn) submitBtn.disabled = !passed;
  }}
  if (input) input.addEventListener('input', updateMeter);

  // Submit handler
  if (submitBtn) {{
    submitBtn.addEventListener('click', function () {{
      try {{ window.localStorage.setItem('bio304-gate-' + TOPIC_ID, 'true'); }} catch (e) {{}}
      try {{ window.localStorage.setItem('bio304-video-' + TOPIC_ID, 'true'); }} catch (e) {{}}
      if (pre) {{
        pre.classList.remove('gate-locked');
        pre.removeAttribute('aria-disabled');
      }}
      var hintEl = document.getElementById('prework-gate-hint');
      if (hintEl) hintEl.hidden = true;
      if (statusEl) {{
        statusEl.textContent = 'Unlocked. Your pre-work cards are ready.';
        statusEl.classList.add('passed');
      }}
      submitBtn.disabled = true;
      submitBtn.textContent = 'Unlocked';
      // Auto-scroll back up to the prework button so they can act
      if (pre) {{
        pre.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        pre.focus();
      }}
    }});
  }}

  // ---- YouTube IFrame API: reveal gate when video ends ----
  var cfg = window.SHEET_CONFIG || {{}};
  var rawVideo = (cfg.video || '').trim();
  var isPlaceholder = !rawVideo || rawVideo.indexOf('REPLACE_WITH_') !== -1 || rawVideo === 'about:blank';

  function revealGate() {{
    if (gateSection && gateSection.hidden) {{
      gateSection.hidden = false;
      gateSection.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      if (input) setTimeout(function () {{ input.focus(); }}, 600);
    }}
  }}

  if (isPlaceholder) {{
    // No real video yet: reveal the gate immediately so the page is testable.
    revealGate();
    return;
  }}

  // Ensure enablejsapi on the iframe URL
  if (cfg.video.indexOf('enablejsapi=1') === -1) {{
    cfg.video = cfg.video + (cfg.video.indexOf('?') !== -1 ? '&' : '?') + 'enablejsapi=1';
  }}
  if (!window.YT) {{
    var tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    document.head.appendChild(tag);
  }}

  var player = null;
  function tryWrap() {{
    if (player || !window.YT || !window.YT.Player) return;
    var iframe = document.getElementById('video-iframe');
    if (!iframe || !iframe.src || iframe.src === 'about:blank') return;
    player = new YT.Player(iframe, {{
      events: {{
        onStateChange: function (e) {{
          if (e.data === 0) revealGate();
        }}
      }}
    }});
  }}
  var videoToggle = document.getElementById('video-toggle');
  if (videoToggle) {{
    videoToggle.addEventListener('click', function () {{
      setTimeout(tryWrap, 400);
      setTimeout(tryWrap, 1500);
      setTimeout(tryWrap, 3500);
    }});
  }}
  var prevReady = window.onYouTubeIframeAPIReady;
  window.onYouTubeIframeAPIReady = function () {{
    if (typeof prevReady === 'function') {{ try {{ prevReady(); }} catch (er) {{}} }}
    tryWrap();
  }};
}})();

// Iframe height-sender for Canvas/Kajabi embeds.
(function () {{
  if (window.self === window.top) return;
  function send() {{
    try {{
      var h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
      window.parent.postMessage({{ id: 'bio304-lecture-page', type: 'resize', height: h }}, '*');
    }} catch (e) {{}}
  }}
  window.addEventListener('load', send);
  window.addEventListener('resize', send);
  if ('ResizeObserver' in window) new ResizeObserver(send).observe(document.body);
}})();
</script>
"""


def clean_one(fname, topic_id, course):
    src_path = os.path.join(SRC, fname)
    dst_path = os.path.join(HERE, fname)
    if not os.path.exists(src_path):
        print(f"  SKIP {fname} (source missing)")
        return None
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Rebrand + dash scrub
    html = html.replace("MEDMASTERS COLLABORATIVE", "AMERICAN RIVER COLLEGE")
    html = html.replace("MedMasters Collaborative", "American River College")
    html = html.replace("MedMasters", "American River College")
    html = html.replace("—", ", ").replace("–", "-")

    # 2. Update SHEET_CONFIG.prework
    if topic_id:
        prework_target = PREWORK_URL + "#topic=" + topic_id
    else:
        prework_target = PREWORK_URL
    html = re.sub(
        r"prework:\s*'https://REPLACE_WITH_YOUR_SR_DOMAIN/prework/[^']*'",
        "prework: '" + prework_target + "'",
        html,
    )
    # Also fix prework if it was already wired to spaced-recall but without hash
    html = re.sub(
        r"prework:\s*'bio304-spaced-recall-prototype\.html(#topic=[^']*)?'",
        "prework: '" + prework_target + "'",
        html,
    )

    # 3. Strip any prior injection blocks from earlier cleaner runs
    for sentinel in [
        "<!-- bio304-lecture-gate-wired -->",
        "<!-- bio304-option-a -->",
    ]:
        if sentinel in html:
            html = re.sub(
                r"\n?" + re.escape(sentinel) + r"[\s\S]*?</script>\s*",
                "",
                html,
            )
    # Also strip the prior gate-style block if injected
    html = re.sub(r"<style>\s*/\* Gate-locked state[\s\S]*?</style>\s*", "", html)

    # 4. Inject CSS into <head> just before </style> closer or before </head>
    sentinel = "<!-- bio304-option-a -->"
    style_block = f"<style>\n{GATE_CSS}\n</style>\n"
    if "</head>" in html and sentinel not in html:
        html = html.replace("</head>", style_block + "</head>", 1)

    # 5. Inject the gate HTML before </main>
    if "</main>" in html and "id=\"explain-gate\"" not in html:
        html = html.replace("</main>", GATE_HTML_TEMPLATE + "</main>", 1)

    # 6. Inject the gate JS just before </body>
    gate_keywords = gate_keywords_for(topic_id, course)
    script_block = "\n" + sentinel + build_gate_script(topic_id, gate_keywords, prework_target)
    if "</body>" in html:
        html = html.replace("</body>", script_block + "</body>", 1)

    # 7. Final em-dash check
    if "—" in html or "–" in html:
        raise SystemExit("Em/en dash STILL present in " + fname)

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(dst_path) // 1024


def main():
    course = load_course()
    counts = {"mapped": 0, "supplementary": 0, "skipped": 0}
    for fname, tid in MAPPING.items():
        size_kb = clean_one(fname, tid, course)
        if size_kb is None:
            counts["skipped"] += 1
            continue
        if tid:
            counts["mapped"] += 1
            tag = f"(flag: {tid})"
        else:
            counts["supplementary"] += 1
            tag = "(no flag)"
        print(f"  {fname:38s}  {size_kb:5d} KB  {tag}")
    print()
    print(f"Mapped (gate flag set): {counts['mapped']}")
    print(f"Supplementary (no flag): {counts['supplementary']}")
    print(f"Skipped (source missing): {counts['skipped']}")


if __name__ == "__main__":
    main()
