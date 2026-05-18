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

    # 2. Update SHEET_CONFIG.prework. If the page maps to a topic, deep-link
    #    via #topic=t-X so the spaced recall app jumps straight to those cards.
    if topic_id:
        prework_target = PREWORK_URL + "#topic=" + topic_id
    else:
        prework_target = PREWORK_URL
    html = re.sub(
        r"prework:\s*'https://REPLACE_WITH_YOUR_SR_DOMAIN/prework/[^']*'",
        "prework: '" + prework_target + "'",
        html,
    )

    # 3. Inject the gate logic just before </body>. Idempotent.
    #    Two paths:
    #      - Placeholder video (SHEET_CONFIG.video contains REPLACE_WITH_):
    #        soft path. Button stays enabled; click sets flag and navigates.
    #      - Real YouTube video: hard path. Button disabled until YouTube
    #        IFrame API fires onStateChange state 0 (ended), then enable + flag.
    #    Plus iframe height-sender for Canvas embeds.
    sentinel = "<!-- bio304-lecture-gate-wired -->"
    if sentinel in html:
        # Strip any previous injection so we re-inject with the current version.
        html = re.sub(
            r"\n" + re.escape(sentinel) + r"[\s\S]*?</script>\s*",
            "",
            html,
        )

    topic_js_value = "'" + topic_id + "'" if topic_id else "null"

    gate_style = (
        "<style>\n"
        "  /* Gate-locked state for the prework button while video is unwatched */\n"
        "  .resource-btn.gate-locked {\n"
        "    opacity: 0.55;\n"
        "    cursor: not-allowed;\n"
        "    pointer-events: auto;\n"
        "  }\n"
        "  .resource-btn.gate-locked:focus-visible {\n"
        "    outline: 2px solid var(--gold);\n"
        "    outline-offset: 2px;\n"
        "  }\n"
        "  .gate-hint {\n"
        "    display: inline-block;\n"
        "    margin-left: 10px;\n"
        "    font-family: 'DM Sans', system-ui, sans-serif;\n"
        "    font-size: 11.5px;\n"
        "    font-weight: 700;\n"
        "    letter-spacing: 0.08em;\n"
        "    text-transform: uppercase;\n"
        "    color: var(--terra-dark);\n"
        "    vertical-align: middle;\n"
        "  }\n"
        "  .gate-hint[hidden] { display: none; }\n"
        "  /* Post-video unlock modal */\n"
        "  .unlock-modal {\n"
        "    position: fixed; inset: 0; z-index: 2000;\n"
        "    display: flex; align-items: center; justify-content: center;\n"
        "    padding: 24px;\n"
        "  }\n"
        "  .unlock-modal[hidden] { display: none; }\n"
        "  .unlock-modal__backdrop {\n"
        "    position: absolute; inset: 0;\n"
        "    background: rgba(20,42,54,0.78);\n"
        "  }\n"
        "  .unlock-modal__card {\n"
        "    position: relative;\n"
        "    background: var(--white);\n"
        "    color: var(--navy);\n"
        "    padding: 26px 28px 22px 28px;\n"
        "    border-radius: 6px;\n"
        "    max-width: 480px;\n"
        "    width: 100%;\n"
        "    box-shadow: 0 24px 60px rgba(0,0,0,0.35);\n"
        "    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;\n"
        "  }\n"
        "  .unlock-modal__eyebrow {\n"
        "    font-family: 'DM Sans', system-ui, sans-serif;\n"
        "    font-weight: 700;\n"
        "    font-size: 11.5px;\n"
        "    letter-spacing: 0.14em;\n"
        "    text-transform: uppercase;\n"
        "    color: var(--terra-dark);\n"
        "    margin: 0 0 8px 0;\n"
        "  }\n"
        "  .unlock-modal__title {\n"
        "    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;\n"
        "    font-weight: 800;\n"
        "    font-size: 22px;\n"
        "    color: var(--navy);\n"
        "    margin: 0 0 8px 0;\n"
        "  }\n"
        "  .unlock-modal__body {\n"
        "    font-family: 'Lora', Georgia, serif;\n"
        "    font-size: 15.5px;\n"
        "    line-height: 1.55;\n"
        "    color: var(--navy);\n"
        "    margin: 0 0 18px 0;\n"
        "  }\n"
        "  .unlock-modal__actions {\n"
        "    display: flex; gap: 10px; flex-wrap: wrap;\n"
        "  }\n"
        "  .unlock-modal__btn {\n"
        "    font-family: 'DM Sans', system-ui, sans-serif;\n"
        "    font-weight: 700;\n"
        "    font-size: 13px;\n"
        "    letter-spacing: 0.08em;\n"
        "    text-transform: uppercase;\n"
        "    padding: 10px 18px;\n"
        "    border-radius: 999px;\n"
        "    border: 1px solid var(--navy);\n"
        "    cursor: pointer;\n"
        "    text-decoration: none;\n"
        "    display: inline-block;\n"
        "  }\n"
        "  .unlock-modal__btn--primary {\n"
        "    background: var(--navy);\n"
        "    color: var(--white);\n"
        "  }\n"
        "  .unlock-modal__btn--primary:hover { background: var(--navy-deep); }\n"
        "  .unlock-modal__btn--ghost {\n"
        "    background: transparent;\n"
        "    color: var(--navy);\n"
        "  }\n"
        "  .unlock-modal__btn--ghost:hover { background: var(--navy-tint); }\n"
        "  .unlock-modal__btn:focus-visible {\n"
        "    outline: 3px solid var(--gold);\n"
        "    outline-offset: 2px;\n"
        "  }\n"
        "  .unlock-modal__close {\n"
        "    position: absolute; top: -12px; right: -12px;\n"
        "    width: 36px; height: 36px;\n"
        "    border-radius: 50%;\n"
        "    background: var(--navy);\n"
        "    color: var(--white);\n"
        "    border: 2px solid var(--white);\n"
        "    font-size: 20px; font-weight: 700; line-height: 1;\n"
        "    cursor: pointer;\n"
        "    display: flex; align-items: center; justify-content: center;\n"
        "    box-shadow: 0 4px 12px rgba(0,0,0,0.3);\n"
        "  }\n"
        "  .unlock-modal__close:hover { background: var(--navy-deep); }\n"
        "  .unlock-modal__close:focus-visible {\n"
        "    outline: 3px solid var(--gold);\n"
        "    outline-offset: 2px;\n"
        "  }\n"
        "  @media (prefers-reduced-motion: reduce) {\n"
        "    .unlock-modal__card { transition: none; }\n"
        "  }\n"
        "</style>\n"
    )

    gate_script = (
        "<script>\n"
        "// Cross-page video gate + post-video unlock modal.\n"
        "//   Soft path (placeholder video): button always enabled; click sets flag.\n"
        "//   Hard path (real YouTube video): button locked until video 'ended' event,\n"
        "//     then a celebratory unlock modal appears with 'Go to the pre-work' and\n"
        "//     'Maybe later' actions.\n"
        "// The spaced recall app reads localStorage['bio304-video-<topicId>'] = 'true'.\n"
        "(function () {\n"
        "  var TOPIC_ID = " + topic_js_value + ";\n"
        "  var pre = document.getElementById('prework-link');\n"
        "  if (!pre) return;\n"
        "  var cfg = window.SHEET_CONFIG || {};\n"
        "  var rawVideo = (cfg.video || '').trim();\n"
        "  var isPlaceholder = !rawVideo ||\n"
        "                      rawVideo.indexOf('REPLACE_WITH_') !== -1 ||\n"
        "                      rawVideo === 'about:blank';\n"
        "\n"
        "  function setFlag() {\n"
        "    if (!TOPIC_ID) return;\n"
        "    try { window.localStorage.setItem('bio304-video-' + TOPIC_ID, 'true'); } catch (e) {}\n"
        "  }\n"
        "\n"
        "  // ------------- Soft path: placeholder video -------------\n"
        "  if (isPlaceholder) {\n"
        "    pre.addEventListener('click', setFlag);\n"
        "    return;\n"
        "  }\n"
        "\n"
        "  // ------------- Hard path: real video, lock + modal on end -------------\n"
        "  pre.classList.add('gate-locked');\n"
        "  pre.setAttribute('aria-disabled', 'true');\n"
        "  var hint = document.createElement('span');\n"
        "  hint.className = 'gate-hint';\n"
        "  hint.id = 'prework-gate-hint';\n"
        "  hint.textContent = 'Watch the video to unlock';\n"
        "  pre.parentNode && pre.parentNode.insertBefore(hint, pre.nextSibling);\n"
        "\n"
        "  pre.addEventListener('click', function (e) {\n"
        "    if (pre.classList.contains('gate-locked')) {\n"
        "      e.preventDefault();\n"
        "      return;\n"
        "    }\n"
        "    setFlag();\n"
        "  });\n"
        "\n"
        "  if (cfg.video.indexOf('enablejsapi=1') === -1) {\n"
        "    cfg.video = cfg.video + (cfg.video.indexOf('?') !== -1 ? '&' : '?') + 'enablejsapi=1';\n"
        "  }\n"
        "  if (!window.YT) {\n"
        "    var tag = document.createElement('script');\n"
        "    tag.src = 'https://www.youtube.com/iframe_api';\n"
        "    document.head.appendChild(tag);\n"
        "  }\n"
        "\n"
        "  // ------- Build the unlock modal (hidden until video ends) -------\n"
        "  var modal = document.createElement('div');\n"
        "  modal.className = 'unlock-modal';\n"
        "  modal.setAttribute('role', 'dialog');\n"
        "  modal.setAttribute('aria-modal', 'true');\n"
        "  modal.setAttribute('aria-labelledby', 'unlock-modal-title');\n"
        "  modal.hidden = true;\n"
        "  modal.innerHTML =\n"
        "    '<div class=\"unlock-modal__backdrop\" data-modal-close></div>' +\n"
        "    '<div class=\"unlock-modal__card\">' +\n"
        "      '<button type=\"button\" class=\"unlock-modal__close\" aria-label=\"Close\" data-modal-close>&times;</button>' +\n"
        "      '<p class=\"unlock-modal__eyebrow\">Pre-work unlocked</p>' +\n"
        "      '<h2 class=\"unlock-modal__title\" id=\"unlock-modal-title\">Nice work finishing the video.</h2>' +\n"
        "      '<p class=\"unlock-modal__body\">Your spaced-recall cards for this topic are ready. Open the pre-work to activate them and start drilling.</p>' +\n"
        "      '<div class=\"unlock-modal__actions\">' +\n"
        "        '<a class=\"unlock-modal__btn unlock-modal__btn--primary\" id=\"unlock-modal-go\" target=\"_top\" href=\"#\">Go to the pre-work &rarr;</a>' +\n"
        "        '<button type=\"button\" class=\"unlock-modal__btn unlock-modal__btn--ghost\" data-modal-close>Maybe later</button>' +\n"
        "      '</div>' +\n"
        "    '</div>';\n"
        "  document.body.appendChild(modal);\n"
        "\n"
        "  var lastFocus = null;\n"
        "  function unlock() {\n"
        "    pre.classList.remove('gate-locked');\n"
        "    pre.removeAttribute('aria-disabled');\n"
        "    if (hint) hint.hidden = true;\n"
        "    setFlag();\n"
        "  }\n"
        "  function openModal() {\n"
        "    if (!modal.hidden) return;\n"
        "    lastFocus = document.activeElement;\n"
        "    var go = modal.querySelector('#unlock-modal-go');\n"
        "    if (go) go.href = pre.href || cfg.prework || '#';\n"
        "    modal.hidden = false;\n"
        "    document.body.style.overflow = 'hidden';\n"
        "    setTimeout(function () { if (go) go.focus(); }, 0);\n"
        "  }\n"
        "  function closeModal() {\n"
        "    modal.hidden = true;\n"
        "    document.body.style.overflow = '';\n"
        "    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();\n"
        "  }\n"
        "  modal.addEventListener('click', function (e) {\n"
        "    if (e.target.closest('[data-modal-close]')) closeModal();\n"
        "  });\n"
        "  document.addEventListener('keydown', function (e) {\n"
        "    if (!modal.hidden && e.key === 'Escape') closeModal();\n"
        "  });\n"
        "  // Primary CTA in modal sets the flag (button click event also fires the native nav).\n"
        "  modal.querySelector('#unlock-modal-go').addEventListener('click', setFlag);\n"
        "\n"
        "  // ------- Wrap YT player and wait for 'ended' -------\n"
        "  var player = null;\n"
        "  function tryWrap() {\n"
        "    if (player) return;\n"
        "    if (!window.YT || !window.YT.Player) return;\n"
        "    var iframe = document.getElementById('video-iframe');\n"
        "    if (!iframe || !iframe.src || iframe.src === 'about:blank') return;\n"
        "    player = new YT.Player(iframe, {\n"
        "      events: {\n"
        "        onStateChange: function (e) {\n"
        "          if (e.data === 0) {\n"
        "            unlock();\n"
        "            openModal();\n"
        "          }\n"
        "        }\n"
        "      }\n"
        "    });\n"
        "  }\n"
        "  var videoToggle = document.getElementById('video-toggle');\n"
        "  if (videoToggle) {\n"
        "    videoToggle.addEventListener('click', function () {\n"
        "      setTimeout(tryWrap, 400);\n"
        "      setTimeout(tryWrap, 1500);\n"
        "      setTimeout(tryWrap, 3500);\n"
        "    });\n"
        "  }\n"
        "  var prevReady = window.onYouTubeIframeAPIReady;\n"
        "  window.onYouTubeIframeAPIReady = function () {\n"
        "    if (typeof prevReady === 'function') { try { prevReady(); } catch (e) {} }\n"
        "    tryWrap();\n"
        "  };\n"
        "})();\n"
        "\n"
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

    injection = "\n" + sentinel + "\n" + gate_style + gate_script
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
