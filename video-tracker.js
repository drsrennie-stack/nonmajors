/* ============================================================
   BIO 304 YouTube watch tracker
   Dr. Sharilyn Rennie

   WHAT IT DOES
   Embeds a YouTube video and measures how much of it a student
   GENUINELY watched, then records that to the engagement report.
   Because it samples real playback, dragging the scrubber to the
   end does NOT count as watched. Skipped seconds are never filled.

   It writes two same-origin localStorage values per topic:
     bio304-video-<topicId>     = "true" once the watch threshold is met
     bio304-videopct-<topicId>  = highest true percentage watched (0..100)
   The cards page reads these for the report and the 5%-per-video policy.

   HOW TO USE
   Put a mount element wherever the video should appear, then load
   this script once:

     <div class="video-tracker"
          data-youtube="B2ww2P8itW4"
          data-topic="t-cell-membrane-transport"
          data-threshold="95"
          data-title="Cell membrane and transport"></div>
     <script src="video-tracker.js" defer></script>

   You can place several mounts on one page; each tracks its own
   topic. data-threshold is optional (default 95).
   ============================================================ */
(function () {
  "use strict";
  if (window.__bio304VideoTracker) return;
  window.__bio304VideoTracker = true;

  var instances = [];

  function parseId(v) {
    if (!v) return "";
    v = String(v).trim();
    if (v.indexOf("http") !== 0 && v.indexOf("/") === -1) return v; // already an id
    var m = v.match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([A-Za-z0-9_-]{6,})/);
    return m ? m[1] : v;
  }
  function readPct(topicId) {
    try { return parseInt(localStorage.getItem("bio304-videopct-" + topicId) || "0", 10) || 0; } catch (e) { return 0; }
  }
  function writePct(topicId, pct) {
    try { localStorage.setItem("bio304-videopct-" + topicId, String(pct)); } catch (e) {}
  }
  function markWatched(topicId) {
    try { localStorage.setItem("bio304-video-" + topicId, "true"); } catch (e) {}
    try { localStorage.setItem("bio304-gate-" + topicId, "true"); } catch (e) {} // backward compat
  }

  /* ---- Styles (injected once) ---- */
  function injectCSS() {
    if (document.getElementById("video-tracker-css")) return;
    var css =
      '.video-tracker{font-family:"Plus Jakarta Sans Variable","Plus Jakarta Sans",system-ui,sans-serif;margin:0 0 20px;}' +
      '.video-tracker .vt-frame{position:relative;width:100%;aspect-ratio:16/9;background:#060A18;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px rgba(11,21,48,0.10);}' +
      '.video-tracker .vt-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0;}' +
      '.video-tracker .vt-readout{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:10px;}' +
      '.video-tracker .vt-bar{flex:1 1 200px;min-width:160px;height:10px;border-radius:999px;background:rgba(11,21,48,0.12);overflow:hidden;}' +
      '.video-tracker .vt-fill{height:100%;width:0%;background:#C9A14A;transition:width 300ms ease;}' +
      '.video-tracker .vt-pct{font-weight:800;font-size:15px;color:#0B1530;font-variant-numeric:tabular-nums;min-width:3.2em;}' +
      '.video-tracker .vt-state{font-size:12.5px;font-weight:700;letter-spacing:0.04em;color:#8B3A2E;flex-basis:100%;}' +
      '.video-tracker .vt-state.is-done{color:#0B1530;}' +
      '@media (prefers-reduced-motion: reduce){.video-tracker .vt-fill{transition:none;}}' +
      '@media print{.video-tracker{display:none !important;}}';
    var st = document.createElement("style");
    st.id = "video-tracker-css";
    st.textContent = css;
    document.head.appendChild(st);
  }

  /* ---- Build one tracker ---- */
  function build(mount) {
    var youtubeId = parseId(mount.getAttribute("data-youtube"));
    var topicId   = (mount.getAttribute("data-topic") || "").trim();
    var threshold = parseInt(mount.getAttribute("data-threshold") || "95", 10);
    var title     = mount.getAttribute("data-title") || "Lecture video";
    if (!youtubeId || !topicId) return null;

    var frameId = "vt-frame-" + topicId.replace(/[^a-z0-9]+/gi, "-");
    mount.innerHTML =
      '<div class="vt-frame"><iframe id="' + frameId + '" src="https://www.youtube.com/embed/' + youtubeId + '?enablejsapi=1&rel=0&playsinline=1" title="' + title + '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>' +
      '<div class="vt-readout">' +
        '<div class="vt-bar" role="progressbar" aria-label="Percent of video watched" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="vt-fill"></div></div>' +
        '<span class="vt-pct">0%</span>' +
        '<span class="vt-state" role="status" aria-live="polite"></span>' +
      '</div>';

    var inst = {
      frameId: frameId, topicId: topicId, threshold: threshold,
      player: null, duration: 0, watched: {}, watchedCount: 0,
      lastSec: null, timer: null,
      fill: mount.querySelector(".vt-fill"),
      pctEl: mount.querySelector(".vt-pct"),
      bar: mount.querySelector(".vt-bar"),
      stateEl: mount.querySelector(".vt-state"),
      best: readPct(topicId)
    };
    paint(inst, inst.best);
    if (localStorage.getItem("bio304-video-" + topicId) === "true") {
      setDone(inst);
    } else if (inst.best > 0) {
      inst.stateEl.textContent = "Last time you watched " + inst.best + "%. Pick up where you left off.";
    } else {
      inst.stateEl.textContent = "Press play. We will record how much you watch.";
    }
    instances.push(inst);
    return inst;
  }

  function paint(inst, pct) {
    pct = Math.max(0, Math.min(100, Math.round(pct)));
    if (inst.fill) inst.fill.style.width = pct + "%";
    if (inst.pctEl) inst.pctEl.textContent = pct + "%";
    if (inst.bar) inst.bar.setAttribute("aria-valuenow", String(pct));
  }
  function setDone(inst) {
    inst.stateEl.textContent = "Recorded. Counts toward your engagement report. You can rewatch any time.";
    inst.stateEl.classList.add("is-done");
  }

  function sample(inst) {
    if (!inst.player || !inst.duration) return;
    var cur;
    try { cur = Math.floor(inst.player.getCurrentTime()); } catch (e) { return; }
    if (isNaN(cur) || cur < 0) return;
    // Count this second. Fill only small, forward, continuous gaps (normal
    // playback at our 1s sample rate). A jump (scrub) of more than 2s, or
    // backward, adds only the single landed second, never the skipped span.
    if (inst.lastSec != null && cur > inst.lastSec && (cur - inst.lastSec) <= 2) {
      for (var s = inst.lastSec + 1; s <= cur; s++) {
        if (!inst.watched[s]) { inst.watched[s] = 1; inst.watchedCount++; }
      }
    } else {
      if (!inst.watched[cur]) { inst.watched[cur] = 1; inst.watchedCount++; }
    }
    inst.lastSec = cur;

    var pct = Math.min(100, Math.round(inst.watchedCount / Math.max(1, Math.floor(inst.duration)) * 100));
    paint(inst, pct);
    if (pct > inst.best) { inst.best = pct; writePct(inst.topicId, pct); }
    if (pct >= inst.threshold && localStorage.getItem("bio304-video-" + inst.topicId) !== "true") {
      markWatched(inst.topicId);
      setDone(inst);
      try { window.dispatchEvent(new Event("bio304-video-recorded")); } catch (e) {}
    }
  }

  function startTimer(inst) {
    if (inst.timer) return;
    inst.lastSec = null; // resync after a play/seek
    inst.timer = setInterval(function () { sample(inst); }, 1000);
  }
  function stopTimer(inst) {
    if (inst.timer) { clearInterval(inst.timer); inst.timer = null; }
  }

  function makePlayer(inst) {
    inst.player = new YT.Player(inst.frameId, {  // attaches to the iframe already in the page
      events: {
        onReady: function () {
          try { inst.duration = inst.player.getDuration() || 0; } catch (e) {}
        },
        onStateChange: function (e) {
          // 1 PLAYING, 2 PAUSED, 0 ENDED, 3 BUFFERING, 5 CUED
          if (!inst.duration) { try { inst.duration = inst.player.getDuration() || 0; } catch (er) {} }
          if (e.data === 1) { startTimer(inst); }
          else { stopTimer(inst); sample(inst); }
        }
      }
    });
  }

  /* ---- Boot ---- */
  function boot() {
    var mounts = document.querySelectorAll(".video-tracker");
    if (!mounts.length) return;
    injectCSS();
    for (var i = 0; i < mounts.length; i++) build(mounts[i]);
    if (!instances.length) return;

    function initAll() { instances.forEach(makePlayer); }
    if (window.YT && window.YT.Player) {
      initAll();
    } else {
      var prev = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = function () {
        if (typeof prev === "function") { try { prev(); } catch (e) {} }
        initAll();
      };
      if (!document.getElementById("yt-iframe-api")) {
        var tag = document.createElement("script");
        tag.id = "yt-iframe-api";
        tag.src = "https://www.youtube.com/iframe_api";
        document.head.appendChild(tag);
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
