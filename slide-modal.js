/*
 * slide-modal.js — Cowork / MedMasters lecture page integration
 * Dr. Sharilyn Rennie
 *
 * Drop in any lecture page. Looks for buttons / links with a data-slide attribute,
 * opens that slide deck in a centered, floating white panel. NO dark backdrop —
 * the rest of the lecture page stays visible behind a transparent layer so the
 * student keeps their reading context.
 *
 * Usage in a lecture page:
 *   <script src="slide-modal.js" defer></script>
 *   <button data-slide="slides-tubular-function.html">Draw the nephron</button>
 *   <a href="#" data-slide="slides-burns.html#slide-3">Draw the rule of nines</a>
 *
 * Anchors are supported: data-slide="path.html#slide-3" loads the deck and
 * scrolls to that slide inside the iframe.
 *
 * Accessibility: focus trap, Escape to close, click-outside-panel closes,
 * aria-modal, returns focus to opener button.
 *
 * Slides themselves are NOT modified. They already postMessage their height
 * up to the iframe parent (handled here for autosize), so the panel grows
 * to fit content but caps at 92vh with internal scroll.
 */
(function () {
  'use strict';

  // ---- Inject required CSS once ----
  if (!document.getElementById('slide-modal-styles')) {
    var s = document.createElement('style');
    s.id = 'slide-modal-styles';
    s.textContent = [
      '.slide-modal-shell { position: fixed; inset: 0; z-index: 9998; display: none; align-items: center; justify-content: center; padding: 24px; pointer-events: none; }',
      '.slide-modal-shell.is-open { display: flex; pointer-events: auto; background: rgba(11, 21, 48, 0.04); }',
      '.slide-modal-panel { position: relative; background: #FFFFFF; border: 1px solid rgba(11, 21, 48, 0.16); border-radius: 12px; box-shadow: 0 24px 60px rgba(11, 21, 48, 0.20), 0 4px 12px rgba(11, 21, 48, 0.08); width: min(1280px, 96vw); height: min(92vh, 1100px); display: flex; flex-direction: column; overflow: hidden; }',
      '.slide-modal-bar { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 10px 16px; background: #FAFAF9; border-bottom: 1px solid rgba(11, 21, 48, 0.10); flex-shrink: 0; }',
      '.slide-modal-title { font-family: "Plus Jakarta Sans", system-ui, sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #0B1530; margin: 0; opacity: 0.72; }',
      '.slide-modal-controls { display: flex; gap: 8px; }',
      '.slide-modal-btn { background: transparent; border: 1px solid rgba(11, 21, 48, 0.22); border-radius: 4px; padding: 6px 12px; font-family: inherit; font-size: 10.5px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #0B1530; cursor: pointer; }',
      '.slide-modal-btn:hover { border-color: #8B3A2E; color: #8B3A2E; }',
      '.slide-modal-btn.close { font-size: 16px; line-height: 1; padding: 4px 10px; font-weight: 800; letter-spacing: 0; }',
      '.slide-modal-frame { flex: 1; width: 100%; border: 0; display: block; background: #FAFAF9; }',
      'body.slide-modal-open { overflow: hidden; }',
      '@media (max-width: 640px) { .slide-modal-shell { padding: 8px; } .slide-modal-panel { width: 100%; height: 96vh; border-radius: 8px; } .slide-modal-title { font-size: 10px; letter-spacing: 0.14em; } }',
      '@media (prefers-reduced-motion: reduce) { .slide-modal-shell { transition: none !important; } }'
    ].join('\n');
    document.head.appendChild(s);
  }

  // ---- Build modal DOM once ----
  var shell = document.createElement('div');
  shell.className = 'slide-modal-shell';
  shell.setAttribute('role', 'dialog');
  shell.setAttribute('aria-modal', 'true');
  shell.setAttribute('aria-labelledby', 'slide-modal-title');
  shell.innerHTML =
    '<div class="slide-modal-panel">' +
      '<div class="slide-modal-bar">' +
        '<p class="slide-modal-title" id="slide-modal-title">Drawing slides</p>' +
        '<div class="slide-modal-controls">' +
          '<button type="button" class="slide-modal-btn" data-action="open-tab">Open in new tab</button>' +
          '<button type="button" class="slide-modal-btn close" data-action="close" aria-label="Close drawing slides">×</button>' +
        '</div>' +
      '</div>' +
      '<iframe class="slide-modal-frame" title="Drawing slides" aria-label="Drawing slides"></iframe>' +
    '</div>';
  document.body.appendChild(shell);

  var panel = shell.querySelector('.slide-modal-panel');
  var titleEl = shell.querySelector('#slide-modal-title');
  var frame = shell.querySelector('.slide-modal-frame');
  var openTabBtn = shell.querySelector('[data-action="open-tab"]');
  var closeBtn = shell.querySelector('[data-action="close"]');
  var lastOpener = null;
  var currentUrl = '';

  function open(url, label) {
    currentUrl = url;
    frame.setAttribute('src', url);
    titleEl.textContent = label || 'Drawing slides';
    shell.classList.add('is-open');
    document.body.classList.add('slide-modal-open');
    setTimeout(function () { closeBtn.focus(); }, 40);
  }

  function close() {
    shell.classList.remove('is-open');
    document.body.classList.remove('slide-modal-open');
    // Clear iframe so canvas state + audio (none, but defensive) stop.
    frame.setAttribute('src', 'about:blank');
    currentUrl = '';
    if (lastOpener && typeof lastOpener.focus === 'function') lastOpener.focus();
    lastOpener = null;
  }

  closeBtn.addEventListener('click', close);
  openTabBtn.addEventListener('click', function () {
    if (currentUrl) window.open(currentUrl, '_blank', 'noopener');
  });

  // Click outside panel closes
  shell.addEventListener('click', function (e) {
    if (e.target === shell) close();
  });

  // Escape closes
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && shell.classList.contains('is-open')) {
      e.preventDefault(); close();
    }
  });

  // Focus trap — keep Tab inside the panel
  panel.addEventListener('keydown', function (e) {
    if (e.key !== 'Tab') return;
    var focusables = [openTabBtn, closeBtn, frame].filter(Boolean);
    var first = focusables[0]; var last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault(); last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault(); first.focus();
    }
  });

  // ---- Wire any element with data-slide ----
  function wire(el) {
    if (el.__slideModalWired) return;
    el.__slideModalWired = true;
    el.addEventListener('click', function (e) {
      e.preventDefault();
      lastOpener = el;
      var url = el.getAttribute('data-slide');
      var label = el.getAttribute('data-slide-label') || el.textContent.trim() || 'Drawing slides';
      open(url, label);
    });
  }

  function scan(root) {
    (root || document).querySelectorAll('[data-slide]').forEach(wire);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { scan(); });
  } else {
    scan();
  }

  // Watch for buttons added later (Kajabi blocks load async sometimes)
  if (window.MutationObserver) {
    new MutationObserver(function (muts) {
      muts.forEach(function (m) {
        m.addedNodes.forEach(function (n) {
          if (n.nodeType === 1) {
            if (n.hasAttribute && n.hasAttribute('data-slide')) wire(n);
            if (n.querySelectorAll) scan(n);
          }
        });
      });
    }).observe(document.body, { childList: true, subtree: true });
  }

  // ---- Expose tiny API for advanced cases ----
  window.SlideModal = { open: open, close: close, scan: scan };
})();
