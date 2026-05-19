"""
Build the 5 missing lecture one-pagers for BIO 304:
  - skin-layers.html             (t-skin-layers, Day 7)
  - skin-functions.html          (t-skin-functions, Day 8)
  - skeletal-muscle-microanatomy.html (t-skeletal-muscle-microanatomy, Day 13)
  - vision.html                  (t-vision, Day 19)
  - tubular-function.html        (t-tubular-function, Day 30)

Each page follows the same visual structure as the existing 39 lecture pages
(PRIMARY palette, Plus Jakarta + Lora fonts, banner, resource bar with video
toggle and gated prework button, reference content built from course-content.js
notes, clinical tie-in, sketch space, footer).

After this generator runs, _apply_option_a.py will inject the inline
explain-back gate into each new page (same as it does for the other 39).
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_5():
    with open(os.path.join(HERE, "_5topic_data.json")) as f:
        return json.load(f)


# Map topic id -> filename + clinical tie-in copy
CLINICAL = {
    "t-skin-layers": {
        "filename": "skin-layers.html",
        "module": "Module 4 . Integumentary System",
        "clinical_title": "Why the layers matter at the bedside",
        "clinical_body": (
            "An IV line goes into the <strong>dermis</strong>, not the epidermis. "
            "A first-degree burn affects only the <strong>epidermis</strong> and heals "
            "without scarring. A second-degree burn extends into the <strong>dermis</strong> "
            "and heals from the hair follicles and sweat glands embedded in the dermis. "
            "A third-degree burn destroys the dermis entirely, which is why those wounds "
            "need grafting. Knowing what lives in each layer tells you what is intact "
            "and what is not."
        ),
    },
    "t-skin-functions": {
        "filename": "skin-functions.html",
        "module": "Module 4 . Integumentary System",
        "clinical_title": "When skin functions fail",
        "clinical_body": (
            "A patient with extensive burns is at high risk of <strong>dehydration</strong> "
            "(barrier loss) and <strong>infection</strong> (immune barrier loss). A patient "
            "who cannot sweat (anhidrosis) overheats during exercise. A patient on a long "
            "course of corticosteroids has thinned skin that bruises easily because dermal "
            "connective tissue is being broken down. The skin's job list is the assessment "
            "checklist."
        ),
    },
    "t-skeletal-muscle-microanatomy": {
        "filename": "skeletal-muscle-microanatomy.html",
        "module": "Module 6 . Muscular System",
        "clinical_title": "Where the microanatomy shows up clinically",
        "clinical_body": (
            "Duchenne muscular dystrophy is a defect in the protein <strong>dystrophin</strong>, "
            "which anchors the sarcomere's contractile machinery to the sarcolemma. Without "
            "it, every contraction tears the muscle fiber. Statin-induced myopathy disrupts "
            "the <strong>sarcoplasmic reticulum's</strong> calcium handling. The CK lab value "
            "rises when sarcolemma is breached. Microanatomy is what fails first, even when "
            "the patient just feels weak."
        ),
    },
    "t-vision": {
        "filename": "vision.html",
        "module": "Module 8 . Special Senses",
        "clinical_title": "Vision pathway clinical handles",
        "clinical_body": (
            "Cataracts cloud the <strong>lens</strong>: surgical replacement restores vision. "
            "Glaucoma damages the <strong>optic nerve</strong> through elevated intraocular "
            "pressure. Age-related macular degeneration kills the <strong>cones</strong> at "
            "the fovea: patients lose central vision but keep peripheral. Diabetic retinopathy "
            "damages retinal capillaries before symptoms appear. Where the lesion sits "
            "predicts what the patient cannot see."
        ),
    },
    "t-tubular-function": {
        "filename": "tubular-function.html",
        "module": "Module 15 . Urinary System",
        "clinical_title": "Where tubular function meets the chart",
        "clinical_body": (
            "<strong>Loop diuretics</strong> (furosemide) block NKCC2 in the thick ascending "
            "limb: the medullary gradient collapses, water follows sodium out, and the patient "
            "diureses heavily. <strong>Thiazides</strong> block NCC in the early DCT: milder, "
            "longer-acting diuresis. <strong>Spironolactone</strong> blocks aldosterone in the "
            "late DCT and collecting duct: potassium-sparing. <strong>SIADH</strong> floods the "
            "system with ADH: collecting duct aquaporins go wide open and the patient retains "
            "free water until serum sodium drops dangerously. The drug list maps onto the nephron."
        ),
    },
}


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title} . BIO 304 . One-Pager</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;1,400;1,500&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --navy: #1E3D4C;
    --navy-deep: #142a36;
    --navy-tint: #EDF1F3;
    --gold: #B8924A;
    --terra: #C2734D;
    --terra-dark: #A0522D;
    --white: #FFFFFF;
    --offwhite: #FAFAF9;
    --rule: rgba(30,61,76,0.18);
    --rule-soft: rgba(30,61,76,0.10);
    --card-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 14px rgba(30,61,76,0.06);
    --card: #FFFFFF;
    --ink: #1E3D4C;
    --ink-soft: #5C6970;
    --focus-ring: #B8924A;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; padding: 0; }}
  body {{
    background: var(--offwhite);
    color: var(--ink);
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    font-size: 15px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  .skip {{ position: absolute; left: -9999px; }}
  .skip:focus {{ position: static; padding: 8px 12px; background: var(--navy); color: var(--white); }}
  a:focus-visible, button:focus-visible {{ outline: 3px solid var(--focus-ring); outline-offset: 3px; border-radius: 4px; }}
  @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }} }}

  .sheet {{ max-width: 8.5in; margin: 28px auto; background: var(--white); padding: 0.55in 0.6in; box-shadow: var(--card-shadow); border-radius: 4px; }}
  .eyebrow {{ font-family: 'DM Sans',system-ui,sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--terra-dark); margin: 0 0 8px 0; }}
  h1.title {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 800; font-size: 34px; line-height: 1.1; color: var(--navy); margin: 0 0 4px 0; letter-spacing: -0.01em; }}
  .subhead {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 600; font-size: 18px; color: var(--terra-dark); margin: 0 0 10px 0; }}
  .usage {{ font-family: 'Lora',Georgia,serif; font-style: italic; font-size: 14px; color: var(--ink-soft); margin: 0 0 18px 0; max-width: 62ch; }}
  hr.rule {{ border: 0; border-top: 1px solid var(--rule); margin: 18px 0; }}

  .resource-bar {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 18px 0; align-items: center; }}
  .resource-btn {{ display: inline-flex; align-items: center; gap: 8px; background: var(--white); color: var(--navy); padding: 10px 18px; border: 1px solid var(--navy); border-radius: 999px; font-family: 'DM Sans',system-ui,sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; text-decoration: none; cursor: pointer; }}
  .resource-btn:hover {{ background: var(--navy-tint); }}
  .resource-btn.primary {{ background: var(--navy); color: var(--white); }}
  .resource-btn.primary:hover {{ background: var(--navy-deep); }}
  .resource-btn .arrow {{ font-size: 14px; }}

  .video-panel {{ margin: 0 0 18px 0; aspect-ratio: 16 / 9; background: var(--navy); border-radius: 8px; overflow: hidden; }}
  .video-panel[hidden] {{ display: none; }}
  .video-panel iframe {{ width: 100%; height: 100%; border: 0; }}

  .objectives {{ display: grid; grid-template-columns: 110px 1fr; gap: 14px; margin: 0 0 22px 0; align-items: start; }}
  .objectives .label {{ font-family: 'DM Sans',system-ui,sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--terra-dark); padding-top: 2px; }}
  .objectives ol {{ margin: 0; padding-left: 18px; }}
  .objectives li {{ margin: 0 0 6px 0; }}

  .columns {{ display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }}
  @media (max-width: 720px) {{ .columns {{ grid-template-columns: 1fr; }} }}
  .col h2 {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 700; font-size: 15px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--navy); margin: 0 0 8px 0; padding-bottom: 6px; border-bottom: 2px solid var(--navy); }}
  .col h3 {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 700; font-size: 13.5px; letter-spacing: 0.02em; color: var(--terra-dark); margin: 14px 0 6px 0; }}
  .col ul {{ margin: 0; padding-left: 20px; }}
  .col li {{ font-family: 'Lora',Georgia,serif; font-size: 14.5px; line-height: 1.55; margin: 4px 0; color: var(--ink); }}
  .col li strong {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; color: var(--navy); font-weight: 700; font-size: 13.5px; }}

  .tie-in {{ margin-top: 20px; padding: 16px 20px; background: var(--white); border: 1.5px solid var(--terra-dark); border-radius: 4px; box-shadow: 0 6px 14px rgba(160,82,45,0.10), 0 1px 2px rgba(0,0,0,0.06); }}
  .tie-in .eyebrow {{ color: var(--terra-dark); margin-bottom: 6px; }}
  .tie-in h3 {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 700; font-size: 15px; color: var(--navy); margin: 0 0 8px 0; }}
  .tie-in p {{ margin: 0 0 8px 0; font-family: 'Lora',Georgia,serif; font-size: 14px; color: var(--ink); }}
  .tie-in p:last-child {{ margin: 0; }}
  .tie-in strong {{ color: var(--terra-dark); }}

  .notes-block {{ margin-top: 24px; }}
  .notes-block h2 {{ font-family: 'Plus Jakarta Sans',system-ui,sans-serif; font-weight: 700; font-size: 16px; color: var(--navy); margin: 0 0 8px 0; }}
  .sketch-space {{ min-height: 2.2in; background: var(--white); border: 1px dashed var(--rule); border-radius: 4px; }}

  .foot {{ margin-top: 22px; padding-top: 12px; border-top: 1px solid var(--rule); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; font-family: 'DM Sans',system-ui,sans-serif; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-soft); }}

  @media print {{
    body {{ background: var(--white); }}
    .resource-bar, .video-panel, .skip {{ display: none !important; }}
    .sheet {{ box-shadow: none; padding: 0; }}
  }}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>

<main class="sheet" id="main">
  <p class="eyebrow">BIO 304 . Human Anatomy &amp; Physiology . American River College</p>
  <h1 class="title">{title}</h1>
  <p class="subhead">{module}</p>
  <p class="usage">{summary} Watch the video, then complete the retrieval check below to unlock your spaced-recall cards.</p>

  <div class="resource-bar" role="region" aria-label="Topic resources">
    <button type="button" class="resource-btn" id="video-toggle" aria-expanded="false" aria-controls="video-panel">
      <span class="arrow" aria-hidden="true">&#9654;</span> Watch the video
    </button>
    <a class="resource-btn primary" id="prework-link" href="#" target="_top" rel="noopener">
      Go to the pre-work <span class="arrow" aria-hidden="true">&rarr;</span>
    </a>
  </div>
  <div class="video-panel" id="video-panel" hidden>
    <iframe id="video-iframe" src="about:blank" title="{title} video" loading="lazy"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
  </div>

  <hr class="rule" />

  <div class="objectives">
    <span class="label">By the end</span>
    <ol>
{objectives_html}
    </ol>
  </div>

  <hr class="rule" />

  <div class="columns">
    <section class="col">
{col1_html}
    </section>
    <section class="col">
{col2_html}

      <aside class="tie-in" role="note" aria-label="Clinical tie-in">
        <p class="eyebrow">Clinical tie-in</p>
        <h3>{clinical_title}</h3>
        <p>{clinical_body}</p>
      </aside>
    </section>
  </div>

  <section class="notes-block" aria-labelledby="sketch-h">
    <p class="eyebrow">Given, not Googled</p>
    <h2 id="sketch-h">Sketch &amp; synthesis</h2>
    <p class="usage" style="margin-bottom:10px;">Sketch the structure from memory. Label every part. Write one sentence about why this structure matters at the bedside.</p>
    <div class="sketch-space" aria-hidden="true"></div>
  </section>

  <div class="foot">
    <span>Dr. Sharilyn Rennie</span>
    <span>BIO 304 . {module}</span>
  </div>
</main>

<script>
  window.SHEET_CONFIG = {{
    video:   'https://www.youtube.com/embed/REPLACE_WITH_{video_key}_VIDEO_ID',
    prework: 'https://REPLACE_WITH_YOUR_SR_DOMAIN/prework/{slug}',
  }};
  (function wireResources() {{
    var cfg = window.SHEET_CONFIG || {{}};
    var pre = document.getElementById('prework-link');
    if (pre && cfg.prework) pre.href = cfg.prework;
    var toggle = document.getElementById('video-toggle');
    var panel  = document.getElementById('video-panel');
    var iframe = document.getElementById('video-iframe');
    if (!toggle || !panel || !iframe) return;
    toggle.addEventListener('click', function () {{
      var expanded = toggle.getAttribute('aria-expanded') === 'true';
      if (expanded) {{
        panel.hidden = true;
        iframe.src = 'about:blank';
        toggle.setAttribute('aria-expanded', 'false');
      }} else {{
        iframe.src = cfg.video || 'about:blank';
        panel.hidden = false;
        toggle.setAttribute('aria-expanded', 'true');
      }}
    }});
  }})();
</script>
</body>
</html>
"""


# Topic-specific reference content. Each entry maps to a topic id.
# col1 and col2 are HTML fragments inserted into the two reference columns.
# objectives is a list of 3 short bullets.
TOPIC_CONTENT = {
    "t-skin-layers": {
        "video_key": "SKIN_LAYERS",
        "slug": "skin-layers",
        "objectives": [
            "Name the layers of the epidermis from deepest to most superficial and the cell type that dominates each.",
            "Distinguish the papillary and reticular layers of the dermis and what each layer contains.",
            "Place hair follicles, sweat glands, blood vessels, and sensory receptors in the correct skin layer.",
        ],
        "col1": """      <h2>Epidermis (top down)</h2>
      <h3>Stratum corneum</h3>
      <ul><li><strong>Anucleate keratin sheets</strong>: dead keratinocytes packed with keratin. Waterproof barrier.</li></ul>
      <h3>Stratum lucidum</h3>
      <ul><li><strong>Thick skin only</strong>: palms and soles. Translucent dead cells.</li></ul>
      <h3>Stratum granulosum</h3>
      <ul><li><strong>Keratohyalin granules</strong>: keratinocytes start dying here, releasing lipids that seal the barrier.</li></ul>
      <h3>Stratum spinosum</h3>
      <ul><li><strong>"Prickly" desmosomes</strong>: keratinocyte cohesion plus dendritic cells (immune surveillance).</li></ul>
      <h3>Stratum basale</h3>
      <ul><li><strong>Mitotic engine</strong>: new keratinocytes born here. Melanocytes (pigment) and Merkel cells (touch) sit at this layer.</li></ul>""",
        "col2": """      <h2>Dermis &amp; hypodermis</h2>
      <h3>Papillary dermis (superficial)</h3>
      <ul><li><strong>Loose areolar tissue</strong>: dermal papillae interlock with epidermis. Holds the capillary network that feeds the epidermis (which has no blood vessels of its own).</li><li><strong>Meissner corpuscles</strong>: light touch receptors.</li></ul>
      <h3>Reticular dermis (deep)</h3>
      <ul><li><strong>Dense irregular connective tissue</strong>: collagen and elastin web that gives skin its strength and rebound.</li><li><strong>Hair follicles, sebaceous glands, sweat glands</strong> all live here.</li><li><strong>Pacinian corpuscles</strong>: deep pressure and vibration receptors.</li></ul>
      <h3>Hypodermis (subcutaneous)</h3>
      <ul><li><strong>Adipose + loose connective tissue</strong>: anchors skin to underlying fascia. Insulation, energy reserve, shock absorption.</li><li><strong>Not technically part of skin</strong> but everything in skin attaches to it.</li></ul>""",
    },
    "t-skin-functions": {
        "video_key": "SKIN_FUNCTIONS",
        "slug": "skin-functions",
        "objectives": [
            "List the seven major functions of the integumentary system and identify the structure responsible for each.",
            "Trace the role of sweat glands and dermal vasculature in thermoregulation.",
            "Identify the accessory structures (hair, glands, nails) and the layer of skin each is anchored in.",
        ],
        "col1": """      <h2>Major functions</h2>
      <h3>Barrier (physical, chemical, biological)</h3>
      <ul><li>Keratin and lipids in the epidermis block water loss and pathogen entry.</li><li>Acid mantle (pH 4 to 6) discourages microbial growth.</li></ul>
      <h3>Thermoregulation</h3>
      <ul><li><strong>Sweat glands</strong>: evaporation cools the body.</li><li><strong>Dermal vessels dilate or constrict</strong>: dump heat or conserve it.</li></ul>
      <h3>Sensation</h3>
      <ul><li>Meissner (light touch), Pacinian (pressure), Ruffini (stretch), free nerve endings (pain, temperature).</li></ul>
      <h3>Vitamin D synthesis</h3>
      <ul><li>UV-B converts 7-dehydrocholesterol in the epidermis to cholecalciferol (D3).</li></ul>
      <h3>Limited excretion</h3>
      <ul><li>Sweat carries small amounts of urea, salts, and water.</li></ul>""",
        "col2": """      <h2>Accessory structures</h2>
      <h3>Hair follicle</h3>
      <ul><li><strong>Anchored in dermis</strong>. Arrector pili muscle pulls hair upright (goosebumps). Sensory function via root hair plexus.</li></ul>
      <h3>Sebaceous gland</h3>
      <ul><li><strong>Connected to hair follicle</strong>. Secretes sebum (oily, antimicrobial). Acne starts when these clog.</li></ul>
      <h3>Eccrine sweat gland</h3>
      <ul><li><strong>Throughout body surface</strong>. Watery sweat for thermoregulation. Independent of hair follicles.</li></ul>
      <h3>Apocrine sweat gland</h3>
      <ul><li><strong>Axillae, groin, areolae</strong>. Develops at puberty. Thicker secretion, bacterially modified to produce body odor.</li></ul>
      <h3>Nail</h3>
      <ul><li>Hard keratin plate over the nail bed. Protects the distal phalanx and improves fine motor function.</li></ul>""",
    },
    "t-skeletal-muscle-microanatomy": {
        "video_key": "SKEL_MUSCLE_MICRO",
        "slug": "skeletal-muscle-microanatomy",
        "objectives": [
            "Trace the connective tissue hierarchy from epimysium down to a single myofibril.",
            "Label every band, line, and zone of the sarcomere and state which filament dominates each.",
            "Identify T-tubules and sarcoplasmic reticulum and explain why they sit where they sit.",
        ],
        "col1": """      <h2>Structural hierarchy (big to small)</h2>
      <h3>Whole muscle</h3>
      <ul><li>Wrapped in <strong>epimysium</strong> (dense irregular CT).</li></ul>
      <h3>Fascicle</h3>
      <ul><li>Bundle of muscle fibers wrapped in <strong>perimysium</strong>.</li></ul>
      <h3>Muscle fiber (cell)</h3>
      <ul><li>Single multinucleate cell wrapped in <strong>endomysium</strong>.</li><li>Plasma membrane = <strong>sarcolemma</strong>. Cytoplasm = sarcoplasm.</li></ul>
      <h3>Myofibril</h3>
      <ul><li>Rod-shaped contractile organelle inside the fiber. Hundreds per fiber.</li></ul>
      <h3>Sarcomere</h3>
      <ul><li>Functional unit. Z-line to Z-line. Hundreds end-to-end down each myofibril.</li></ul>""",
        "col2": """      <h2>The sarcomere</h2>
      <h3>Z-line</h3>
      <ul><li>Sarcomere boundary. Thin filaments anchor here.</li></ul>
      <h3>I band</h3>
      <ul><li><strong>Thin filaments only</strong> (light under microscopy). Shortens during contraction.</li></ul>
      <h3>A band</h3>
      <ul><li><strong>Full length of thick filament</strong> (dark band). Width never changes during contraction.</li></ul>
      <h3>H zone</h3>
      <ul><li><strong>Thick filaments only</strong>, no overlap. Shortens during contraction.</li></ul>
      <h3>M line</h3>
      <ul><li>Center of sarcomere. Thick filaments anchor here.</li></ul>
      <h2>Excitation machinery</h2>
      <h3>T-tubules</h3>
      <ul><li>Invaginations of sarcolemma. Carry the action potential deep into the fiber.</li></ul>
      <h3>Sarcoplasmic reticulum</h3>
      <ul><li>Smooth ER specialized for Ca2+ storage. Releases Ca2+ when the T-tubule signal arrives.</li></ul>""",
    },
    "t-vision": {
        "video_key": "VISION",
        "slug": "vision",
        "objectives": [
            "Trace a ray of light from cornea to optic nerve and name every structure it passes through.",
            "Explain accommodation: how the ciliary muscle and lens change shape for near and far vision.",
            "Compare rods and cones (location, sensitivity, color, acuity).",
        ],
        "col1": """      <h2>Eye anatomy</h2>
      <h3>Cornea</h3>
      <ul><li><strong>Transparent dome</strong> on the front. Provides about two-thirds of the eye's refractive power. Avascular.</li></ul>
      <h3>Iris &amp; pupil</h3>
      <ul><li>Iris muscle controls <strong>pupil diameter</strong>: more light in or less. Sphincter pupillae (parasympathetic) constricts, dilator pupillae (sympathetic) dilates.</li></ul>
      <h3>Lens</h3>
      <ul><li><strong>Adjustable focus</strong> via ciliary muscle. Shape changes for accommodation.</li></ul>
      <h3>Aqueous humor</h3>
      <ul><li>Watery fluid in anterior chamber. Produced by ciliary body, drained at the canal of Schlemm. Pressure regulator.</li></ul>
      <h3>Vitreous humor</h3>
      <ul><li>Gelatinous fluid in posterior chamber. Maintains eye shape.</li></ul>
      <h3>Retina</h3>
      <ul><li>Posterior neural layer. Contains photoreceptors, bipolar cells, ganglion cells.</li></ul>
      <h3>Fovea centralis</h3>
      <ul><li>Cones only. Highest visual acuity. What you focus on lands here.</li></ul>
      <h3>Optic disc</h3>
      <ul><li>Where axons exit the eye as the optic nerve. No photoreceptors, hence the blind spot.</li></ul>""",
        "col2": """      <h2>Accommodation</h2>
      <h3>Distance vision</h3>
      <ul><li>Ciliary muscle <strong>relaxed</strong>. Suspensory ligaments taut. Lens flattens. Light from far objects converges on the retina.</li></ul>
      <h3>Near vision</h3>
      <ul><li>Ciliary muscle <strong>contracts</strong>. Suspensory ligaments slacken. Lens rounds up (more refractive power). Light from close objects converges on the retina.</li></ul>
      <h3>Presbyopia</h3>
      <ul><li>Lens stiffens with age and cannot round up. Reading glasses needed.</li></ul>

      <h2>Phototransduction</h2>
      <h3>Rods</h3>
      <ul><li>~120 million per eye. Outside the fovea. Rhodopsin. <strong>Sensitive to low light</strong>, no color, low acuity.</li></ul>
      <h3>Cones</h3>
      <ul><li>~6 million per eye. Concentrated at fovea. Three types: S (blue), M (green), L (red). <strong>Color and high acuity</strong>, needs bright light.</li></ul>
      <h3>Signal path</h3>
      <ul><li>Photoreceptor &rarr; bipolar cell &rarr; ganglion cell &rarr; optic nerve &rarr; thalamus (LGN) &rarr; primary visual cortex (occipital lobe).</li></ul>""",
    },
    "t-tubular-function": {
        "video_key": "TUBULAR_FUNCTION",
        "slug": "tubular-function",
        "objectives": [
            "For each nephron segment, name what is reabsorbed, what is secreted, and which transporters do the work.",
            "Explain how the loop of Henle builds the medullary concentration gradient.",
            "Describe how ADH and aldosterone fine-tune water and sodium at the collecting duct.",
        ],
        "col1": """      <h2>PCT and Loop of Henle</h2>
      <h3>Proximal convoluted tubule (PCT)</h3>
      <ul><li><strong>Bulk reabsorption</strong>: about 65% of filtered Na+, water, glucose, amino acids reabsorbed here.</li><li>SGLT2 cotransporter reabsorbs glucose with sodium. (SGLT2 inhibitors are diabetes drugs.)</li><li>Brush border maximizes surface area.</li></ul>
      <h3>Descending limb of Henle</h3>
      <ul><li><strong>Permeable to water, not solute</strong>. Water exits into the increasingly hypertonic medulla. Filtrate becomes more concentrated as it descends.</li></ul>
      <h3>Thick ascending limb</h3>
      <ul><li><strong>Permeable to solute, not water</strong>. NKCC2 cotransporter pumps Na+, K+, and 2 Cl- out into the interstitium. Filtrate becomes more dilute. Builds the medullary gradient.</li><li>This is where <strong>loop diuretics</strong> (furosemide) act.</li></ul>""",
        "col2": """      <h2>DCT and collecting duct</h2>
      <h3>Early DCT</h3>
      <ul><li>NCC (Na-Cl cotransporter) reabsorbs sodium and chloride. <strong>Thiazide diuretics</strong> block this.</li></ul>
      <h3>Late DCT and collecting duct</h3>
      <ul><li><strong>Principal cells</strong>: ENaC channels for Na+ reabsorption (under aldosterone control); aquaporin-2 channels for water (under ADH control).</li><li><strong>Intercalated cells</strong>: handle acid-base by secreting H+ or HCO3-.</li></ul>

      <h2>Hormonal control</h2>
      <h3>ADH (antidiuretic hormone)</h3>
      <ul><li>Released from posterior pituitary when plasma osmolarity rises.</li><li>Inserts <strong>aquaporin-2</strong> into collecting duct cells. Water reabsorbed, urine concentrated.</li></ul>
      <h3>Aldosterone</h3>
      <ul><li>Released from adrenal cortex (zona glomerulosa) when blood pressure or Na+ drops.</li><li>Acts on principal cells: <strong>Na+ in, K+ out, water follows Na+</strong>. Blood volume and pressure rise.</li></ul>
      <h3>ANP</h3>
      <ul><li>Released from atrial myocytes when stretched. <strong>Opposes aldosterone</strong>: promotes Na+ excretion and lowers blood pressure.</li></ul>""",
    },
}


def build_one(topic, content, clinical):
    obj_html = "\n".join(f"      <li>{o}</li>" for o in content["objectives"])
    html = PAGE_TEMPLATE.format(
        title=topic["title"],
        module=clinical["module"],
        summary=topic["summary"],
        objectives_html=obj_html,
        col1_html=content["col1"],
        col2_html=content["col2"],
        clinical_title=clinical["clinical_title"],
        clinical_body=clinical["clinical_body"],
        video_key=content["video_key"],
        slug=content["slug"],
    )
    # Defensive em-dash scrub
    html = html.replace("—", ", ").replace("–", "-")
    out_path = os.path.join(HERE, "_lecture_src", clinical["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return clinical["filename"], len(html) // 1024


def main():
    topics = load_5()
    for t in topics:
        content = TOPIC_CONTENT[t["id"]]
        clinical = CLINICAL[t["id"]]
        fname, kb = build_one(t, content, clinical)
        print(f"  Wrote _lecture_src/{fname}  ({kb} KB)")


if __name__ == "__main__":
    main()
