#!/usr/bin/env python3
"""
Generate the five Week 4 lab workbooks for BIO 304.

Each workbook has:
  Part 1 of 2  Anatomy Lab        student draws their own diagram from
                                  numbered step-by-step directions, then
                                  hand-labels structures from a list.
  Part 2 of 2  Physiology Lab     a topic-specific activity (mechanism
                                  trace, calculation, sequencing, or
                                  table) followed by three synthesis
                                  questions tying anatomy to function
                                  and to a clinical or applied scenario.

Pedagogy:
  Drawing-based synthesis is the integrity mechanism. No diagrams are
  provided. Students draw their own from directions; AI cannot draw on
  paper for them.

Style:
  PRIMARY palette only (navy, gold, terra). No sage. No cream as a card
  background. Off-white is the page background per the palette spec.

Output:
  Five HTML files written next to this script, named to match the
  expected workbook_dayNN_{slug}.html convention used by the Canvas
  punch list and the schedule generator.
"""

from html import escape
from textwrap import dedent
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# Per-workbook content
# ----------------------------------------------------------------------

WORKBOOKS = [
    # ==================================================================
    # WEEK 1
    # ==================================================================
    {
        "filename": "workbook_day01_anatomical-terminology-and-body-regions.html",
        "title": "Anatomical Terminology and Body Regions",
        "subhead": "Directional terms, planes of section, body cavities, and regional names.",
        "eyebrow": "BIO 304 . WEEK 1 . MONDAY . LAB WORKBOOK",
        "day_num": 1,
        "anatomy_intro": (
            "Anatomy is a precise vocabulary. Today you will draw the body "
            "in anatomical position with directional terms labeled, then "
            "sketch the three reference planes. Be deliberate about which "
            "way is up: anatomical position assumes the body upright, "
            "facing forward, with palms facing forward."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Anatomical position with directional terms",
                "instructions": [
                    "Draw a stick figure or simple outline of a person facing you, palms forward, feet shoulder-width apart. This is anatomical position.",
                    "Draw an arrow from the head pointing up. Label it Superior. Draw a downward arrow from the head and label it Inferior.",
                    "Label Anterior (front) and Posterior (back). Use a small note since both faces are not visible.",
                    "Pick one arm. Show Proximal (closer to trunk) at the shoulder and Distal (farther from trunk) at the fingers.",
                    "Mark Medial (toward midline) and Lateral (away from midline) on the legs.",
                    "Label two body regions on your figure: Brachial (arm), Femoral (thigh), Crural (leg), Antecubital (front of elbow), Popliteal (back of knee). Pick at least four.",
                ],
                "height": 420,
            },
            {
                "id": "B",
                "label": "Box B. The three planes of section",
                "instructions": [
                    "Draw three small body outlines side by side.",
                    "On the first, draw a vertical line dividing the body into left and right halves. Label this the Sagittal plane (specifically, midsagittal if exactly down the middle).",
                    "On the second, draw a vertical line dividing the body into front and back halves. Label this the Frontal (coronal) plane.",
                    "On the third, draw a horizontal line dividing the body into upper and lower halves. Label this the Transverse plane.",
                    "Under each outline, list one imaging study that uses that plane (CT, MRI, ultrasound, etc., your choice).",
                ],
                "height": 320,
            },
        ],
        "label_list": [
            "Superior", "Inferior", "Anterior", "Posterior",
            "Medial", "Lateral", "Proximal", "Distal",
            "Sagittal plane", "Frontal (coronal) plane", "Transverse plane",
            "Brachial", "Femoral", "Antecubital", "Popliteal",
        ],
        "physio_activity_title": "2A. Applied terminology: describe the injury",
        "physio_activity_intro": (
            "Below are 5 patient presentations. For each, write a one-"
            "sentence description using ONLY anatomical terminology (the "
            "directional terms, body regions, and planes you labeled "
            "above). Avoid lay language like 'lower' or 'inside.'"
        ),
        "physio_numbered_qs": [
            "A cut runs across the front of the elbow.",
            "A bruise sits on the calf, just behind and below the knee.",
            "A surgeon makes an incision dividing the abdomen into left and right halves.",
            "A child scrapes the bony surface on the outer side of the lower leg.",
            "An IV is placed in the vein closer to the wrist than to the elbow.",
        ],
        "synthesis_questions": [
            "Explain the difference between Proximal and Superior using the elbow as a reference point. Why can't these terms be used interchangeably?",
            "A radiologist sees a tumor on the right kidney, posterior to the abdominal cavity. Translate that location for a patient using everyday language without losing precision.",
            "If a surgeon says they made a parasagittal cut at the level of the right midclavicular line, draw a quick diagram of where that cut would be and which structures it would pass through.",
        ],
    },
    {
        "filename": "workbook_day01_levels-of-organization.html",
        "title": "Levels of Organization",
        "subhead": "From atoms to organism: how living structure builds up in nested levels.",
        "eyebrow": "BIO 304 . WEEK 1 . MONDAY . LAB WORKBOOK",
        "day_num": 1,
        "anatomy_intro": (
            "Living matter is organized in nested levels. Each level has "
            "properties that emerge from the level below but cannot be "
            "predicted from any single component. Today you will draw the "
            "six levels twice: once in the abstract, once for a specific "
            "concrete example."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The six levels (abstract)",
                "instructions": [
                    "Draw six nested or stacked boxes from smallest to largest.",
                    "Label them in order: Chemical level (atoms, molecules), Cellular level (cells), Tissue level, Organ level, Organ system level, Organism level.",
                    "Beside each level, write one to two specific structural examples (e.g., Chemical: water, glucose, protein).",
                    "Draw an arrow up the stack labeled Emergent properties. Note: each level has properties not present at the level below.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. The six levels (worked example: skeletal muscle to movement)",
                "instructions": [
                    "Use skeletal muscle as your example.",
                    "Chemical level: draw an actin or myosin protein molecule. Label.",
                    "Cellular level: draw a single skeletal muscle fiber (long, striated, multinucleate cell).",
                    "Tissue level: draw a small bundle of muscle fibers wrapped together (skeletal muscle tissue).",
                    "Organ level: draw a whole muscle (e.g., biceps brachii) with tendons.",
                    "Organ system level: draw a simple stick figure with the musculoskeletal system highlighted (arrows to bones and muscles).",
                    "Organism level: draw a person performing a movement (e.g., lifting a bag). Note: function emerges only at the organism level.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Chemical level", "Cellular level", "Tissue level",
            "Organ level", "Organ system level", "Organism level",
            "Atom or molecule", "Cell", "Tissue", "Organ",
            "Organ system", "Organism", "Emergent property",
        ],
        "physio_activity_title": "2A. At which level does it happen?",
        "physio_activity_intro": (
            "For each phenomenon below, identify the LOWEST level of "
            "organization where it occurs. Choose from: chemical, cellular, "
            "tissue, organ, organ system, organism. Briefly justify."
        ),
        "physio_numbered_qs": [
            "An enzyme breaks a covalent bond.",
            "A neuron fires an action potential.",
            "A wound heals by laying down new collagen.",
            "The heart pumps blood through the body.",
            "Blood pressure is regulated by the cardiovascular, urinary, and nervous systems working together.",
            "A person feels hungry and decides to eat lunch.",
        ],
        "synthesis_questions": [
            "Explain what an emergent property is using one of your own examples. Why is the property not present at the level just below?",
            "A drug poisons the mitochondria in every cell. Predict which higher levels of organization will be affected and in what order they will fail.",
            "Pick one organ system. Argue, in two or three sentences, why no single cell or tissue could perform that system's function alone.",
        ],
    },
    {
        "filename": "workbook_day02_homeostasis-and-feedback-loops.html",
        "title": "Homeostasis and Feedback Loops",
        "subhead": "How the body maintains a stable internal environment despite outside change.",
        "eyebrow": "BIO 304 . WEEK 1 . TUESDAY . LAB WORKBOOK",
        "day_num": 2,
        "anatomy_intro": (
            "Homeostasis is the maintenance of a stable internal environment. "
            "Negative feedback corrects deviations and is the body's "
            "default. Positive feedback amplifies a signal and only runs "
            "in a few specific cases (birth, blood clotting). Draw the "
            "loop architecture first, then a specific example."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Negative feedback loop (generic)",
                "instructions": [
                    "Draw 5 boxes arranged in a circle, connected by arrows clockwise.",
                    "Box 1: Stimulus (a change away from setpoint). Box 2: Sensor (detects the change). Box 3: Control center (compares to setpoint, decides action). Box 4: Effector (produces the response). Box 5: Response (returns variable toward setpoint).",
                    "Draw an arrow from Box 5 back to Box 1 with a minus sign. Label it Negative feedback: response opposes the original change.",
                    "At the center of the loop, write Setpoint and one example variable (e.g., body temperature, blood glucose, blood pressure).",
                ],
                "height": 420,
            },
            {
                "id": "B",
                "label": "Box B. Worked example: body temperature drops",
                "instructions": [
                    "Use the same 5-box loop. Fill in each box with the body's response to cold.",
                    "Stimulus: cold environment, body temperature drops below 37 C.",
                    "Sensor: thermoreceptors in skin and hypothalamus.",
                    "Control center: hypothalamus.",
                    "Effector: name at least two (e.g., skeletal muscles, smooth muscle in blood vessels, arrector pili muscles).",
                    "Response: shivering, vasoconstriction, piloerection, behavioral changes. Body temperature rises back toward 37 C.",
                    "On the side, draw a small box labeled Positive feedback. Inside, name one example (childbirth, blood clotting, action potential firing). Note the arrow has a PLUS sign.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Stimulus", "Sensor (receptor)", "Control center",
            "Effector", "Response", "Setpoint",
            "Negative feedback", "Positive feedback",
            "Hypothalamus", "Thermoreceptor", "Shivering", "Vasoconstriction",
        ],
        "physio_activity_title": "2A. Trace: blood glucose rises after a meal",
        "physio_activity_intro": (
            "Trace the negative feedback loop that lowers blood glucose "
            "after a meal. Fill in each step. Be specific about cells, "
            "hormones, and target tissues."
        ),
        "physio_activity_rows": 6,
        "synthesis_questions": [
            "Distinguish negative feedback from positive feedback in one sentence each. Why is negative feedback used for most homeostatic variables but positive feedback used for childbirth?",
            "Type 1 diabetes destroys the beta cells of the pancreas. Walk through the blood-glucose loop and explain what happens after a meal in a patient with untreated Type 1 diabetes.",
            "A fever is a temporary upward reset of the hypothalamic setpoint. Predict what a febrile patient will FEEL at the moment the setpoint resets to 39 C, and explain why they shiver even though their body temperature is technically high.",
        ],
    },
    {
        "filename": "workbook_day03_cell-structure-and-organelles.html",
        "title": "Cell Structure and Organelles",
        "subhead": "The machinery of a generic cell and what each organelle contributes.",
        "eyebrow": "BIO 304 . WEEK 1 . THURSDAY . LAB WORKBOOK",
        "day_num": 3,
        "anatomy_intro": (
            "Today you will draw a generic eukaryotic cell with all its "
            "major organelles, then a specialized cell type and explain "
            "which organelles are emphasized. Cells are not all the same: "
            "form follows function."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Generic cell with all organelles",
                "instructions": [
                    "Draw a large irregular cell outline. Label the plasma membrane.",
                    "Draw a round nucleus inside, label it, and add a small darker spot inside labeled Nucleolus. Show the nuclear envelope around it.",
                    "Draw rough endoplasmic reticulum (rough ER) as folded sheets near the nucleus, with small dots on its surface (ribosomes). Label both.",
                    "Draw smooth endoplasmic reticulum (smooth ER) as folded tubes nearby. Label.",
                    "Draw a Golgi apparatus as stacked flattened sacs. Label.",
                    "Draw 3 or 4 mitochondria (oval shapes with internal folds). Label one.",
                    "Draw 2 lysosomes (small spheres). Label.",
                    "Draw a few free ribosomes floating in the cytoplasm. Label.",
                    "Add a cytoskeleton: thin lines crossing the cell. Label.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. A specialized cell type (pick one)",
                "instructions": [
                    "Pick ONE of these specialized cells and draw it: neuron, skeletal muscle fiber, pancreatic secretory cell, or red blood cell.",
                    "Draw it with realistic proportions and shape (e.g., a neuron has long axon and short dendrites; a muscle fiber is long and multinucleate; an RBC is biconcave and has no nucleus).",
                    "Label any organelles present. ALSO label any organelles that are absent or unusual (e.g., the RBC has no nucleus and no mitochondria).",
                    "Write one sentence explaining how the cell's organelle profile matches its function.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Plasma membrane", "Nucleus", "Nuclear envelope", "Nucleolus",
            "Rough endoplasmic reticulum", "Smooth endoplasmic reticulum",
            "Ribosome (free)", "Ribosome (on rough ER)",
            "Golgi apparatus", "Mitochondrion", "Lysosome",
            "Peroxisome", "Cytoskeleton", "Cytoplasm",
        ],
        "physio_activity_title": "2A. Trace a protein from synthesis to secretion",
        "physio_activity_intro": (
            "A pancreatic acinar cell synthesizes digestive enzymes and "
            "secretes them into a duct. Trace the path of ONE enzyme "
            "protein from the moment its gene is read to the moment it "
            "leaves the cell. Number each step and name the organelle "
            "involved."
        ),
        "physio_activity_rows": 7,
        "synthesis_questions": [
            "A drug poisons all lysosomes in a cell. Predict the consequences over hours to days. Name at least two specific cellular processes that fail.",
            "Red blood cells have no nucleus and no mitochondria. Predict (a) their lifespan, (b) their energy source, and (c) one type of damage they cannot repair.",
            "A liver cell exposed to chronic alcohol consumption develops a dramatic expansion of its smooth ER. Explain why, in terms of what smooth ER does.",
        ],
    },
    {
        "filename": "workbook_day04_membrane-transport.html",
        "title": "Membrane Transport",
        "subhead": "How material crosses the plasma membrane: passive, active, and vesicular pathways.",
        "eyebrow": "BIO 304 . WEEK 1 . FRIDAY . LAB WORKBOOK",
        "day_num": 4,
        "anatomy_intro": (
            "Cells live or die by what they let in and out. Today you'll "
            "draw the membrane in detail and the four major transport "
            "modes that operate across it."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The plasma membrane",
                "instructions": [
                    "Draw a horizontal section of plasma membrane: two rows of phospholipid heads (small circles) with their tails (wavy lines) facing each other inside.",
                    "Label phospholipid head (polar, hydrophilic) and phospholipid tail (non-polar, hydrophobic).",
                    "Draw at least 3 integral membrane proteins spanning the bilayer. Label.",
                    "Draw a peripheral protein on one side. Label.",
                    "Embed cholesterol molecules between the phospholipids. Label.",
                    "Add carbohydrate chains on the extracellular surface attached to proteins (glycoproteins) and lipids (glycolipids). Label.",
                ],
                "height": 360,
            },
            {
                "id": "B",
                "label": "Box B. Four transport modes side by side",
                "instructions": [
                    "Draw four panels, each with a small section of membrane.",
                    "Panel 1: Simple diffusion. Show O2 or CO2 passing directly through the bilayer down a gradient. Label.",
                    "Panel 2: Facilitated diffusion. Show glucose passing through a channel/carrier protein, still down its gradient. Label.",
                    "Panel 3: Primary active transport. Draw the Na+/K+ ATPase with 3 Na+ leaving the cell, 2 K+ entering, and ATP being consumed. Show the gradient: against concentration.",
                    "Panel 4: Vesicular transport. Show a vesicle fusing with the membrane (exocytosis) and releasing contents. Label.",
                    "Above each panel write: passive vs active, and whether ATP is required.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Phospholipid bilayer", "Phospholipid head (hydrophilic)",
            "Phospholipid tail (hydrophobic)", "Integral protein",
            "Peripheral protein", "Cholesterol", "Glycoprotein",
            "Simple diffusion", "Facilitated diffusion",
            "Primary active transport (Na+/K+ ATPase)",
            "Exocytosis", "Endocytosis",
        ],
        "physio_activity_title": "2A. Transport comparison table",
        "physio_activity_intro": (
            "Fill in the table below. Use a short phrase per cell. After "
            "the table, answer the two follow-up questions."
        ),
        "physio_table": {
            "headers": ["Property", "Simple diffusion", "Facilitated diffusion", "Primary active transport", "Endocytosis"],
            "rows": [
                ["Uses a membrane protein?", "", "", "", ""],
                ["Moves with or against gradient?", "", "", "", ""],
                ["Requires ATP directly?", "", "", "", ""],
                ["Typical molecule transported", "", "", "", ""],
                ["Rate-limiting factor", "", "", "", ""],
            ],
        },
        "physio_followups": [
            "Why are large polar molecules unable to cross the membrane by simple diffusion, while small non-polar molecules can?",
            "Secondary active transport (e.g., glucose-Na+ symporter) does not directly consume ATP. Explain how it still depends on ATP, indirectly.",
        ],
        "synthesis_questions": [
            "Red blood cells placed in a 0.45% NaCl solution swell and lyse. Explain using tonicity terms (hypertonic, isotonic, hypotonic). Predict what would happen in a 3% NaCl solution.",
            "Ouabain blocks the Na+/K+ ATPase. Predict the effect on a cell's resting Na+ and K+ concentrations over time, and on its ability to perform secondary active transport.",
            "Cystic fibrosis is caused by a defective chloride channel (CFTR). Predict the effect on the watery secretions of the airways, and explain why patients develop thick mucus.",
        ],
    },

    # ==================================================================
    # WEEK 2
    # ==================================================================
    {
        "filename": "workbook_day05_epithelial-tissue-classification.html",
        "title": "Epithelial Tissue Classification",
        "subhead": "Naming epithelia by cell shape and number of layers, plus pseudostratified and transitional.",
        "eyebrow": "BIO 304 . WEEK 2 . MONDAY . LAB WORKBOOK",
        "day_num": 5,
        "anatomy_intro": (
            "Epithelial tissues are named by two features: how many layers "
            "of cells (simple, stratified) and the shape of the surface "
            "cells (squamous, cuboidal, columnar). Plus two special cases: "
            "pseudostratified (looks layered, isn't) and transitional "
            "(changes shape as it stretches). Draw them all."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The six basic epithelial types (3 by 2 matrix)",
                "instructions": [
                    "Draw a 3-by-2 grid. Columns are cell shape: Squamous (flat), Cuboidal (square), Columnar (tall). Rows are layers: Simple (one layer), Stratified (many layers).",
                    "In each cell of the grid, sketch the tissue. Show the basement membrane as a thin dark line at the bottom.",
                    "Inside each sketch, write ONE typical location (e.g., simple squamous: alveoli; simple cuboidal: kidney tubules; simple columnar: small intestine; stratified squamous: skin epidermis; stratified cuboidal: large gland ducts; stratified columnar: rare, parts of male urethra).",
                    "Cell nuclei should reflect the shape: round in cuboidal, oval in columnar, flat in squamous.",
                ],
                "height": 440,
            },
            {
                "id": "B",
                "label": "Box B. Pseudostratified and transitional epithelium",
                "instructions": [
                    "Left half: draw pseudostratified columnar epithelium with cilia at the top. Show cells of different heights all touching the basement membrane. Add nuclei at staggered heights. Label cilia and goblet cells.",
                    "Note: only one layer, but appears layered due to nuclei at different heights. Common in the respiratory tract.",
                    "Right half: draw transitional epithelium in two states. Left side: empty bladder, cells stacked many layers high, surface cells rounded. Right side: full bladder, fewer apparent layers, surface cells flattened.",
                    "Label transitional epithelium and note its location (urinary tract).",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Basement membrane", "Simple squamous", "Simple cuboidal",
            "Simple columnar", "Stratified squamous", "Stratified cuboidal",
            "Stratified columnar", "Pseudostratified columnar",
            "Transitional", "Cilia", "Goblet cell",
            "Apical surface", "Basal surface",
        ],
        "physio_activity_title": "2A. Match tissue to location and function",
        "physio_activity_intro": (
            "For each location below, identify (a) the epithelial type "
            "present, and (b) the function being served by that tissue's "
            "specific structure. Write in complete sentences."
        ),
        "physio_numbered_qs": [
            "The wall of the alveolus in the lung.",
            "The lining of the kidney tubule.",
            "The lining of the small intestine.",
            "The outer surface of the skin.",
            "The lining of the trachea.",
            "The lining of the urinary bladder.",
        ],
        "synthesis_questions": [
            "Predict the tissue type you would find lining a surface where rapid diffusion is essential. Justify, and give an example location.",
            "Transitional epithelium has the unusual property of changing apparent shape. Explain why this is functionally important in the bladder and what would happen if it were stratified squamous instead.",
            "Cigarette smoke damages pseudostratified ciliated columnar epithelium in the airways. Predict the consequences for mucociliary clearance and explain why a chronic smoker's cough is often productive.",
        ],
    },
    {
        "filename": "workbook_day06_connective-tissues.html",
        "title": "Connective Tissues",
        "subhead": "Cells, fibers, and ground substance across loose, dense, cartilage, bone, and blood.",
        "eyebrow": "BIO 304 . WEEK 2 . TUESDAY . LAB WORKBOOK",
        "day_num": 6,
        "anatomy_intro": (
            "Connective tissues bind, support, and protect. They share a "
            "common architecture: cells embedded in an extracellular "
            "matrix of fibers and ground substance. The TYPE of fibers "
            "and the consistency of the ground substance determine the "
            "subtype. Draw the major ones."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Loose vs dense connective tissue",
                "instructions": [
                    "Left: draw loose (areolar) connective tissue. Show widely spaced collagen and elastic fibers, with fibroblasts (spindle-shaped cells), adipocytes (large round cells with displaced nucleus), and a macrophage scattered between fibers.",
                    "Center: draw dense regular connective tissue (tendon or ligament). Show tightly packed parallel collagen fibers with rows of fibroblasts between them.",
                    "Right: draw dense irregular connective tissue (dermis). Show thick collagen fibers in a random meshwork with fibroblasts scattered.",
                    "Label fibroblast, adipocyte, macrophage, collagen fiber, elastic fiber.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. Cartilage, bone, and blood",
                "instructions": [
                    "Left: draw hyaline cartilage. Show chondrocytes inside lacunae (small spaces), embedded in a smooth glassy matrix. Note: no visible fibers under light microscopy.",
                    "Center: draw a piece of compact bone. Show one osteon: concentric rings (lamellae) around a central canal (Haversian canal). Place osteocytes in lacunae, with canaliculi (small connecting channels) between them.",
                    "Right: draw a blood smear. Show many red blood cells (biconcave, no nucleus), one neutrophil (multi-lobed nucleus), one lymphocyte (large round nucleus). The yellow background is plasma (the fluid matrix).",
                    "Label chondrocyte, lacuna, osteocyte, osteon, central canal, canaliculus, red blood cell, white blood cell, plasma.",
                ],
                "height": 360,
            },
        ],
        "label_list": [
            "Fibroblast", "Adipocyte", "Macrophage", "Mast cell",
            "Chondrocyte", "Lacuna", "Osteocyte", "Osteon",
            "Collagen fiber", "Elastic fiber", "Reticular fiber",
            "Ground substance", "Central canal", "Canaliculus",
            "Red blood cell", "White blood cell", "Plasma",
        ],
        "physio_activity_title": "2A. Match the cell to the tissue and the job",
        "physio_activity_intro": (
            "For each connective tissue cell below, name (a) the tissue it "
            "is found in, and (b) one specific function it performs in "
            "that tissue."
        ),
        "physio_numbered_qs": [
            "Fibroblast",
            "Adipocyte",
            "Chondrocyte",
            "Osteoblast",
            "Osteoclast",
            "Macrophage",
            "Mast cell",
        ],
        "synthesis_questions": [
            "A patient tears their anterior cruciate ligament. Describe the connective tissue that was torn (cells, fibers, arrangement). Why does this tissue heal so slowly?",
            "Cartilage has no blood vessels (it's avascular). Predict how this affects healing after an injury, and explain why athletes with cartilage damage often face long recoveries.",
            "Blood is classified as a connective tissue even though it doesn't 'connect' anything visually. Argue, in two or three sentences, why this classification is defensible based on its architecture.",
        ],
    },
    {
        "filename": "workbook_day07_muscle-and-nervous-tissue-overview.html",
        "title": "Muscle and Nervous Tissue Overview",
        "subhead": "Three muscle types and the basic neuron, side by side.",
        "eyebrow": "BIO 304 . WEEK 2 . THURSDAY . LAB WORKBOOK",
        "day_num": 7,
        "anatomy_intro": (
            "Muscle and nervous tissue are the two excitable tissues: both "
            "can generate and respond to electrical signals. Today you'll "
            "draw all three muscle types side by side, then a neuron in "
            "its own panel."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Three muscle types side by side",
                "instructions": [
                    "Left: Skeletal muscle. Draw long parallel cylindrical fibers with visible cross-striations. Place several nuclei at the edge of each fiber (multinucleate). Label striated, multinucleate, voluntary.",
                    "Center: Cardiac muscle. Draw shorter branched cells with cross-striations. Show one or two central nuclei per cell. Show intercalated discs (thick lines at cell junctions). Label striated, branched, intercalated discs, involuntary.",
                    "Right: Smooth muscle. Draw spindle-shaped cells with a single central nucleus. No striations. Label non-striated, single nucleus, involuntary.",
                    "Under each, list one typical location: skeletal = limb muscles; cardiac = heart only; smooth = walls of hollow organs, blood vessels.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. Basic neuron",
                "instructions": [
                    "Draw a neuron. Cell body (soma) with nucleus. Several short branched dendrites. One long axon. Axon terminals at the end.",
                    "Add a myelin sheath wrapping segments of the axon with gaps (nodes of Ranvier) between segments.",
                    "Label cell body, dendrite, axon, myelin sheath, node of Ranvier, axon terminal.",
                    "Note next to the neuron: nervous tissue function = generate and conduct electrical signals; muscle tissue function = contract in response to signals.",
                ],
                "height": 320,
            },
        ],
        "label_list": [
            "Skeletal muscle fiber", "Cardiac muscle cell", "Smooth muscle cell",
            "Cross-striations", "Intercalated disc",
            "Multinucleate", "Single central nucleus",
            "Cell body (soma)", "Dendrite", "Axon",
            "Myelin sheath", "Node of Ranvier", "Axon terminal",
        ],
        "physio_activity_title": "2A. Muscle comparison table",
        "physio_activity_intro": (
            "Fill in the table below comparing the three muscle types. "
            "After the table, answer the follow-up questions."
        ),
        "physio_table": {
            "headers": ["Property", "Skeletal", "Cardiac", "Smooth"],
            "rows": [
                ["Striated?", "", "", ""],
                ["Number of nuclei per cell", "", "", ""],
                ["Voluntary or involuntary?", "", "", ""],
                ["Branched cells?", "", "", ""],
                ["Has intercalated discs?", "", "", ""],
                ["Typical location", "", "", ""],
            ],
        },
        "physio_followups": [
            "Intercalated discs contain gap junctions that allow ions to flow between cardiac cells. Explain why this is functionally critical for the heart.",
            "Both skeletal and cardiac muscle are striated. What does that visible pattern tell us about how they generate force? Why does smooth muscle look different even though it also uses actin and myosin?",
        ],
        "synthesis_questions": [
            "Damaged skeletal muscle can be partly replaced by satellite cell activation; damaged cardiac muscle is replaced by scar (non-contractile) tissue. Predict the long-term consequences of a heart attack on cardiac function, and contrast with recovery from a torn skeletal muscle.",
            "Smooth muscle is found in the wall of the gut and contracts in slow waves (peristalsis). Predict what happens to digestion in a region of gut where the smooth muscle is damaged.",
            "Action potentials in neurons travel at speeds up to 100 meters per second in myelinated axons. Predict what happens to signal speed when myelin is damaged (e.g., multiple sclerosis) and what symptoms might result.",
        ],
    },
    {
        "filename": "workbook_day07_skin-structure-and-layers.html",
        "title": "Skin Structure and Layers",
        "subhead": "Epidermis, dermis, and hypodermis: the largest organ of the body.",
        "eyebrow": "BIO 304 . WEEK 2 . THURSDAY . LAB WORKBOOK",
        "day_num": 7,
        "anatomy_intro": (
            "Skin is built from three layers, each with a different "
            "tissue and a different job. Today you'll draw it twice: "
            "once as a vertical cross-section showing all three layers, "
            "and once zoomed in on the epidermal strata."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Skin in cross-section (three layers)",
                "instructions": [
                    "Draw a vertical rectangle representing a piece of skin in cross-section. The TOP is the surface; the BOTTOM is deep tissue.",
                    "Top third: draw the epidermis. Make it relatively thin. Shade it differently from the layers below.",
                    "Middle third: draw the dermis. Inside, sketch one hair follicle (extending from epidermis down into dermis), one sebaceous gland (attached to the hair follicle), one sweat gland (coiled at the deep end of a duct), and a blood vessel.",
                    "Bottom third: draw the hypodermis (subcutaneous layer). Show large round adipocytes (fat cells).",
                    "Label all three layers and every structure you drew.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Epidermal strata close-up (thick skin)",
                "instructions": [
                    "Draw a tall vertical rectangle representing the epidermis at high magnification.",
                    "From DEEP to SUPERFICIAL, label five strata: Stratum basale, Stratum spinosum, Stratum granulosum, Stratum lucidum (thick skin only), Stratum corneum.",
                    "In stratum basale, draw a row of cuboidal cells with mitotic figures (cells dividing).",
                    "In stratum spinosum, draw polygonal cells with visible cell junctions (desmosomes).",
                    "In stratum granulosum, draw flattening cells with dark granules inside.",
                    "In stratum lucidum, draw a thin clear band (transparent).",
                    "In stratum corneum, draw many thin flat dead cells stacked, with the topmost ones sloughing off.",
                    "On the side, draw an arrow showing the keratinocyte migration: from basale up to corneum, taking 2 to 4 weeks.",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Epidermis", "Dermis", "Hypodermis (subcutaneous)",
            "Stratum basale", "Stratum spinosum", "Stratum granulosum",
            "Stratum lucidum", "Stratum corneum",
            "Hair follicle", "Sebaceous gland", "Sweat gland",
            "Blood vessel", "Adipocyte", "Keratinocyte",
        ],
        "physio_activity_title": "2A. Trace a keratinocyte from birth to death",
        "physio_activity_intro": (
            "A new keratinocyte is born in the stratum basale by mitosis. "
            "Trace its journey to the surface, including what happens at "
            "each stratum. List 5 to 7 numbered steps."
        ),
        "physio_activity_rows": 7,
        "synthesis_questions": [
            "A patient has a second-degree burn that extends into the upper dermis. Predict whether this will heal by regeneration or by scarring, and explain why.",
            "A patient with extensive third-degree burns (full thickness) loses large patches of skin. Predict the two MOST immediate life-threatening consequences and explain the physiology behind each.",
            "Stratum corneum is constantly shed. Calculate roughly how much skin a person sheds in a year if the turnover time is about 4 weeks and the epidermis is about 0.1 mm thick. (You don't need exact numbers; reason in orders of magnitude.)",
        ],
    },
    {
        "filename": "workbook_day08_skin-functions-and-accessory-structures.html",
        "title": "Skin Functions and Accessory Structures",
        "subhead": "Hair, glands, nails, and the integrated functions of the integumentary system.",
        "eyebrow": "BIO 304 . WEEK 2 . FRIDAY . LAB WORKBOOK",
        "day_num": 8,
        "anatomy_intro": (
            "Skin is more than a barrier. Today you'll draw the accessory "
            "structures that give skin its full range of function: hair "
            "follicles, sebaceous glands, two kinds of sweat glands, and "
            "nails."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Hair follicle and associated glands",
                "instructions": [
                    "Draw a hair follicle in cross-section, extending from the epidermal surface deep into the dermis. The shaft of the hair sticks up above the surface.",
                    "Label the hair shaft (above the skin), the hair root (below the surface), the hair bulb (the rounded base, where the hair grows).",
                    "Draw a sebaceous gland attached to the side of the follicle, with its duct opening into the follicle. Label.",
                    "Draw the arrector pili muscle: a thin smooth muscle attached at an angle from the follicle to the underside of the epidermis. Label.",
                    "Note: when arrector pili contracts, the hair stands up (goosebumps) and a small amount of sebum is squeezed from the gland.",
                ],
                "height": 400,
            },
            {
                "id": "B",
                "label": "Box B. Sweat glands and nail",
                "instructions": [
                    "Left half: draw two sweat glands side by side, each deep in the dermis with a duct rising to the surface.",
                    "Label the eccrine sweat gland (smaller, opens directly onto skin surface, found over most of the body) and the apocrine sweat gland (larger, opens into a hair follicle, found in axillae and groin).",
                    "Right half: draw a nail in side view. Show the nail plate (the visible nail), the nail bed (skin beneath the nail), the nail root (under the proximal skin fold), and the lunula (white half-moon at the base).",
                    "Label every structure.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Hair shaft", "Hair root", "Hair bulb", "Hair follicle",
            "Sebaceous gland", "Arrector pili muscle",
            "Eccrine sweat gland", "Apocrine sweat gland",
            "Nail plate", "Nail bed", "Nail root", "Lunula",
        ],
        "physio_activity_title": "2A. Trace: cold exposure to warming response",
        "physio_activity_intro": (
            "A person steps outside into freezing air. Trace the integumentary "
            "system's response in numbered steps. Include receptors, control "
            "center, and effectors from this week. Aim for 6 to 8 steps."
        ),
        "physio_activity_rows": 8,
        "synthesis_questions": [
            "Eccrine sweat is mostly water and electrolytes. Apocrine sweat is rich in lipids and proteins. Predict (a) which type contributes most to body cooling during exercise, and (b) which is responsible for body odor when bacteria are present. Justify each.",
            "A burn patient loses large patches of skin. Beyond fluid loss and infection risk, predict the consequences for thermoregulation in a cool hospital room, and explain why blankets and warmed IV fluids are routine in burn care.",
            "Sebaceous glands secrete sebum, an oily mixture. People with acne often have overactive sebaceous glands. Explain mechanistically why blocked sebaceous ducts plus bacterial colonization produce inflamed pimples.",
        ],
    },

    # ==================================================================
    # WEEK 3
    # ==================================================================
    {
        "filename": "workbook_day09_bone-tissue-and-bone-growth.html",
        "title": "Bone Tissue and Bone Growth",
        "subhead": "From bone cells to whole bones: how the skeleton is built and remodeled.",
        "eyebrow": "BIO 304 . WEEK 3 . MONDAY . LAB WORKBOOK",
        "day_num": 9,
        "anatomy_intro": (
            "Bone is dynamic: it is built, broken down, and remodeled "
            "throughout life by specific cell types. Today you'll draw a "
            "long bone in gross anatomy, then zoom in to a single osteon."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Long bone gross anatomy",
                "instructions": [
                    "Draw a long bone (e.g., humerus) in side view, with bulged ends and a slim middle.",
                    "Label diaphysis (shaft), epiphysis (each rounded end), metaphysis (region between).",
                    "Show the epiphyseal plate (growth plate) as a thin horizontal line within each metaphysis, present in a growing bone.",
                    "Inside the diaphysis, show the medullary cavity (hollow center). Label.",
                    "Show compact bone (dense outer wall) and spongy bone (trabecular meshwork inside the epiphyses). Label.",
                    "Wrap the outside of the diaphysis with the periosteum (thin membrane). Wrap the inside with the endosteum. Label.",
                    "Add articular cartilage at the very tips of the epiphyses. Label.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. Osteon (Haversian system) close-up",
                "instructions": [
                    "Draw a large circle representing one osteon in cross-section.",
                    "Inside, draw concentric rings (concentric lamellae) around a small central circle.",
                    "Label the central canal (Haversian canal) in the center; it carries a blood vessel and nerve.",
                    "Between the lamellae, draw small lens-shaped spaces (lacunae) containing osteocytes (label).",
                    "Connect lacunae with thin lines (canaliculi). Label.",
                    "Beside the osteon, draw a perforating canal (Volkmann's canal) connecting central canals laterally. Label.",
                ],
                "height": 360,
            },
        ],
        "label_list": [
            "Diaphysis", "Epiphysis", "Metaphysis", "Epiphyseal plate",
            "Medullary cavity", "Compact bone", "Spongy bone",
            "Periosteum", "Endosteum", "Articular cartilage",
            "Osteon", "Concentric lamellae", "Central canal",
            "Osteocyte", "Lacuna", "Canaliculus", "Volkmann's canal",
        ],
        "physio_activity_title": "2A. Match the cell to its action",
        "physio_activity_intro": (
            "Bone has four key cell types. For each action below, name "
            "the cell responsible AND state whether the action builds, "
            "breaks down, or maintains bone."
        ),
        "physio_numbered_qs": [
            "Lays down new bone matrix.",
            "Resorbs old bone, releasing calcium into the blood.",
            "Maintains bone tissue from within a lacuna, sensing mechanical stress.",
            "Differentiates into new bone-building cells when bone is injured.",
            "Increases activity in response to parathyroid hormone, raising blood calcium.",
            "Decreases activity in response to calcitonin, allowing blood calcium to fall.",
        ],
        "synthesis_questions": [
            "A teenager fractures the epiphyseal plate of the femur. Predict the long-term consequence and explain the mechanism behind it.",
            "An elderly patient with osteoporosis has lost bone mass over decades. Identify which cell types are over- or under-active in osteoporosis, and explain why bisphosphonate drugs work by targeting one of them.",
            "Blood calcium is tightly regulated around 10 mg/dL. Sketch a brief feedback loop showing what happens when blood calcium DROPS: which hormone is released, which cell type it activates, and how blood calcium returns to setpoint.",
        ],
    },
    {
        "filename": "workbook_day10_axial-skeleton.html",
        "title": "Axial Skeleton",
        "subhead": "Skull, vertebral column, ribs, and sternum: the body's central pillar.",
        "eyebrow": "BIO 304 . WEEK 3 . TUESDAY . LAB WORKBOOK",
        "day_num": 10,
        "anatomy_intro": (
            "The axial skeleton supports the head and trunk and protects "
            "the brain, spinal cord, and thoracic organs. Today you'll "
            "draw the vertebral column with its regions, then the rib "
            "cage with the sternum."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Vertebral column (lateral view)",
                "instructions": [
                    "Draw the vertebral column from the side. Show it curving (the natural S-curve of the spine).",
                    "Label the four regions from top to bottom: Cervical (7 vertebrae), Thoracic (12), Lumbar (5), Sacral (5 fused), Coccygeal (3 to 4 fused).",
                    "Mark each region with its vertebra count.",
                    "Add the primary curves (thoracic, sacral, concave anteriorly) and secondary curves (cervical, lumbar, convex anteriorly).",
                    "Below the drawing, label C1 (atlas, supports head, allows yes nod) and C2 (axis, with the odontoid process, allows no rotation).",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Thoracic cage",
                "instructions": [
                    "Draw the thoracic cage in anterior view: the sternum down the middle, 12 pairs of ribs curving around to the back.",
                    "Label the sternum and its three parts: manubrium (top), body, xiphoid process (bottom).",
                    "Label the costal cartilages connecting ribs to the sternum.",
                    "Identify rib categories with color or labels: True ribs (1 to 7, attach directly via own costal cartilage), False ribs (8 to 10, attach indirectly to costal cartilage of rib 7), Floating ribs (11 to 12, no anterior attachment).",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Cervical vertebrae (7)", "Thoracic vertebrae (12)",
            "Lumbar vertebrae (5)", "Sacrum", "Coccyx",
            "Atlas (C1)", "Axis (C2)", "Odontoid process (dens)",
            "Manubrium", "Sternal body", "Xiphoid process",
            "Costal cartilage", "True ribs", "False ribs", "Floating ribs",
        ],
        "physio_activity_title": "2A. Structure-function reasoning",
        "physio_activity_intro": (
            "For each axial-skeleton feature below, name what it allows "
            "the body to do, and explain why the structure suits that "
            "function."
        ),
        "physio_numbered_qs": [
            "The foramen magnum at the base of the skull.",
            "The vertebral foramen running the length of every vertebra.",
            "The intervertebral discs between adjacent vertebrae.",
            "The articulation between the atlas (C1) and the occipital bone.",
            "The articulation between the atlas (C1) and the axis (C2).",
            "The flexibility of the costal cartilages connecting ribs to sternum.",
        ],
        "synthesis_questions": [
            "A car accident causes a hyperextension injury (head snaps backward). Which axial structure is at highest risk, and what neurological consequence is most dangerous if that structure is damaged?",
            "A patient has a herniated lumbar disc pressing on a spinal nerve root. Predict the symptoms (motor, sensory, reflexes) and explain why disc herniation is more common in the lumbar region than the thoracic region.",
            "Breathing involves the rib cage expanding and contracting. Explain how the costal cartilages and the rib articulations work together to make this possible, and predict what would happen if the costal cartilages ossified (turned to bone).",
        ],
    },
    {
        "filename": "workbook_day11_appendicular-skeleton.html",
        "title": "Appendicular Skeleton",
        "subhead": "Pectoral and pelvic girdles, plus the upper and lower limb bones.",
        "eyebrow": "BIO 304 . WEEK 3 . THURSDAY . LAB WORKBOOK",
        "day_num": 11,
        "anatomy_intro": (
            "The appendicular skeleton hangs off the axial skeleton via "
            "the pectoral and pelvic girdles. Today you'll draw the "
            "upper limb and the lower limb, each with its girdle."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Upper limb (right side, anterior view)",
                "instructions": [
                    "Draw a right shoulder, arm, forearm, and hand in anterior view.",
                    "Pectoral girdle: clavicle (collarbone, horizontal across the top) and scapula (shoulder blade, behind, mostly hidden in anterior view but indicate its position).",
                    "Arm: humerus (single long bone from shoulder to elbow).",
                    "Forearm: radius (lateral, thumb side) and ulna (medial, pinky side). Show that the radius and ulna can rotate around each other (pronation/supination).",
                    "Wrist and hand: 8 carpals (sketch as a cluster), 5 metacarpals (palm), 14 phalanges (3 in each finger, 2 in the thumb).",
                    "Label every bone group.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Lower limb (right side, anterior view)",
                "instructions": [
                    "Draw a right hip, thigh, leg, and foot in anterior view.",
                    "Pelvic girdle: ilium, ischium, and pubis fused into one hip bone (coxal bone). Label all three regions.",
                    "Thigh: femur (single long bone, the longest in the body). Show the femoral head fitting into the acetabulum (hip socket) and the femoral neck (a common fracture site in elderly patients).",
                    "Show the patella (kneecap) in front of the knee.",
                    "Leg: tibia (medial, weight-bearing, shin bone) and fibula (lateral, thinner, non-weight-bearing).",
                    "Ankle and foot: 7 tarsals (cluster), 5 metatarsals (foot arch), 14 phalanges (toes).",
                    "Label every bone group, plus the femoral head, femoral neck, and acetabulum specifically.",
                ],
                "height": 480,
            },
        ],
        "label_list": [
            "Clavicle", "Scapula", "Humerus", "Radius", "Ulna",
            "Carpals", "Metacarpals", "Phalanges (hand)",
            "Ilium", "Ischium", "Pubis", "Acetabulum",
            "Femur", "Femoral head", "Femoral neck",
            "Patella", "Tibia", "Fibula",
            "Tarsals", "Metatarsals", "Phalanges (foot)",
        ],
        "physio_activity_title": "2A. Name that bone",
        "physio_activity_intro": (
            "For each position description below, name the bone. Be specific: "
            "include side (left vs right) and exact bone name."
        ),
        "physio_numbered_qs": [
            "The bone on the thumb side of the forearm.",
            "The bone between the elbow and the shoulder.",
            "The medial bone of the lower leg, which bears most of the body's weight.",
            "The kneecap, a sesamoid bone embedded in the patellar tendon.",
            "The fused hip bones that together form the pelvic girdle.",
            "The bone of the foot that articulates with the tibia and fibula at the ankle joint (talus).",
            "The proximal phalanx of the great toe (hallux).",
        ],
        "synthesis_questions": [
            "An elderly patient falls and is diagnosed with a 'hip fracture.' Anatomically, the fracture is usually NOT at the pelvic bone itself. Where is it most commonly located, and why is this site particularly vulnerable?",
            "A child falls and lands on their outstretched hand. The clavicle is the most commonly fractured bone in this scenario in children. Explain the mechanical reason why force from the hand transmits to the clavicle.",
            "Compare the pectoral girdle to the pelvic girdle: which is more mobile, and which is more stable? Justify with two anatomical features, and predict which one is more often injured.",
        ],
    },
    {
        "filename": "workbook_day12_joints-and-body-movements.html",
        "title": "Joints and Body Movements",
        "subhead": "Synovial joint types and the movements they allow.",
        "eyebrow": "BIO 304 . WEEK 3 . FRIDAY . LAB WORKBOOK",
        "day_num": 12,
        "anatomy_intro": (
            "Synovial joints are the freely movable joints of the body. "
            "Six structural types, each allowing a specific range of "
            "motion. Today you'll draw all six, then sketch the body "
            "movements they enable."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Six types of synovial joints",
                "instructions": [
                    "Draw 6 small sketches, one for each synovial joint type. For each, draw two articulating bones with their joint surfaces and label the joint type and one body example.",
                    "Plane (gliding) joint: flat-on-flat surfaces. Example: intercarpal joints.",
                    "Hinge joint: rounded on cylindrical. Example: elbow.",
                    "Pivot joint: rounded peg in ring. Example: proximal radioulnar joint (allows pronation/supination); atlas-axis (no rotation).",
                    "Condyloid (ellipsoidal): oval-shaped condyle in oval socket. Example: radiocarpal joint (wrist).",
                    "Saddle joint: saddle shapes on each bone, interlocking. Example: thumb carpometacarpal.",
                    "Ball-and-socket: spherical head in cup-shaped socket. Example: shoulder, hip.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Body movements",
                "instructions": [
                    "Draw 8 small stick-figure pictograms, each showing one body movement. Label each.",
                    "Flexion (decreasing angle, e.g., bending the elbow).",
                    "Extension (increasing angle, e.g., straightening the elbow).",
                    "Abduction (moving away from midline, e.g., raising arm to the side).",
                    "Adduction (moving toward midline, e.g., lowering arm to side).",
                    "Rotation (turning around a long axis, e.g., turning the head side to side).",
                    "Circumduction (cone-shaped movement, e.g., big arm circles).",
                    "Pronation (palm faces down) and Supination (palm faces up) at the forearm.",
                    "Dorsiflexion (foot up toward shin) and Plantarflexion (foot down, point toes).",
                ],
                "height": 440,
            },
        ],
        "label_list": [
            "Plane joint", "Hinge joint", "Pivot joint",
            "Condyloid joint", "Saddle joint", "Ball-and-socket joint",
            "Flexion", "Extension", "Abduction", "Adduction",
            "Rotation", "Circumduction",
            "Pronation", "Supination",
            "Dorsiflexion", "Plantarflexion",
        ],
        "physio_activity_title": "2A. Match the joint type to the motion",
        "physio_activity_intro": (
            "For each body motion below, identify (a) the joint where it "
            "happens and (b) the structural joint type that allows it."
        ),
        "physio_numbered_qs": [
            "Bending the knee while sitting.",
            "Raising the arm overhead to the side.",
            "Rotating the forearm so the palm faces up (supination).",
            "Touching your thumb to your pinky finger.",
            "Nodding your head yes.",
            "Shaking your head no.",
            "Pointing your toes (plantarflexion).",
        ],
        "synthesis_questions": [
            "Compare the shoulder and the hip joints. Both are ball-and-socket. Explain in two or three sentences why the shoulder is more mobile but more prone to dislocation, while the hip is more stable but less mobile.",
            "A patient cannot rotate their forearm so the palm faces up. Which joint is most likely impaired, and what is its structural type? Predict one daily activity this patient would find difficult.",
            "Sketch the difference between flexion and extension at three different joints (elbow, knee, neck). Explain why 'flexion' at the neck looks different from flexion at the elbow even though the term is the same.",
        ],
    },

    # ==================================================================
    # WEEK 4 (already authored below)
    # ==================================================================
    {
        "filename": "workbook_day13_skeletal-muscle-microanatomy.html",
        "title": "Skeletal Muscle Microanatomy",
        "subhead": "From whole muscle down to the sarcomere: the structural ladder of contractile tissue.",
        "eyebrow": "BIO 304 . WEEK 4 . MONDAY . LAB WORKBOOK",
        "day_num": 13,
        "anatomy_intro": (
            "Today you will draw the muscle hierarchy from the outside in, then a "
            "single sarcomere in detail. Use two boxes below. Box A is for the "
            "hierarchy. Box B is for the sarcomere close-up. Sketch, do not trace."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Hierarchy (whole muscle to myofibril)",
                "instructions": [
                    "Draw a long oval representing a whole muscle (cross-section). Wrap it in a thin line. Label that line Epimysium.",
                    "Inside the oval, draw three or four smaller circles. Each is a fascicle. Wrap one of them with a thin line. Label that line Perimysium.",
                    "Inside one fascicle, draw several smaller circles. Each is a muscle fiber (cell). Wrap one with a thin line. Label that line Endomysium.",
                    "Inside one muscle fiber, draw a stack of long rods. Each rod is a myofibril. Label one Myofibril.",
                    "Above your hierarchy, write the order of wrappings from outside to inside in one short sentence.",
                ],
                "height": 360,
            },
            {
                "id": "B",
                "label": "Box B. Sarcomere close-up",
                "instructions": [
                    "Draw a long rectangle. Mark the left and right ends with vertical lines. Label both lines Z line.",
                    "In the center, draw a vertical line. Label it M line.",
                    "Between the two Z lines, draw thick filaments (myosin) in the middle and thin filaments (actin) extending from each Z line.",
                    "Bracket and label the A band (the full length of the thick filaments).",
                    "Bracket and label the I band (the region with only thin filaments).",
                    "Bracket and label the H zone (the central thick-only region).",
                    "Draw a T-tubule entering from above and a sarcoplasmic reticulum wrapping the myofibril. Label both.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Epimysium", "Perimysium", "Endomysium",
            "Muscle fiber (cell)", "Myofibril", "Sarcomere",
            "Z line", "M line", "A band", "I band", "H zone",
            "Thick filament (myosin)", "Thin filament (actin)",
            "T-tubule", "Sarcoplasmic reticulum",
        ],
        "physio_activity_title": "2A. Mechanism trace: from action potential to power stroke",
        "physio_activity_intro": (
            "An action potential has just arrived at the sarcolemma of a "
            "muscle fiber. List the next 8 events that lead to a single "
            "power stroke. For each event, name WHERE it happens (which "
            "structure), WHAT moves (ion or molecule), and what changes "
            "STRUCTURALLY at the sarcomere."
        ),
        "physio_activity_rows": 8,
        "synthesis_questions": [
            "The I band shortens dramatically during contraction, but the A band barely changes length. Explain why, in terms of which filaments make up each band.",
            "A toxin disrupts the triad junctions specifically (the points where T-tubules meet the SR). Predict the effect on contraction and explain at which step the cycle fails.",
            "A muscle is stretched so far that thick and thin filaments no longer overlap. Predict the tension the muscle can generate at this length, and justify your answer using the cross-bridge mechanism.",
        ],
    },
    {
        "filename": "workbook_day13_motor-units-and-muscle-mechanics.html",
        "title": "Motor Units and Muscle Mechanics",
        "subhead": "Motor unit organization, recruitment, summation, and fatigue.",
        "eyebrow": "BIO 304 . WEEK 4 . MONDAY . LAB WORKBOOK",
        "day_num": 13,
        "anatomy_intro": (
            "You will draw two motor units side by side. One is small (for "
            "fine control, like an extraocular eye muscle). One is large "
            "(for power, like the quadriceps). The contrast in your drawing "
            "should make the size principle obvious."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Two motor units, side by side",
                "instructions": [
                    "On the LEFT, draw a small circle for a motor neuron cell body in the ventral horn of the spinal cord. Extend an axon downward.",
                    "Branch the axon into 5 short terminals, each ending on a different muscle fiber. Draw 5 short ovals as the muscle fibers.",
                    "Label this side Small motor unit (eye muscle).",
                    "On the RIGHT, draw another cell body and axon. Branch it into many terminals (draw 12 to 20). Draw the same number of muscle fibers.",
                    "Label this side Large motor unit (quadriceps).",
                    "Add labels: Motor neuron cell body, Axon, Axon terminal, Neuromuscular junction, Muscle fiber.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. Twitch summation (force vs time)",
                "instructions": [
                    "Draw an x-axis (time) and a y-axis (force).",
                    "On the same axes, sketch three force traces stacked vertically by frequency.",
                    "Trace 1: single twitches at 1 Hz. Force rises and falls completely between each stimulus. Label Single twitches.",
                    "Trace 2: stimulation at 10 Hz. The second twitch starts before the first finishes; force adds up. Label Wave summation.",
                    "Trace 3: stimulation at 30 Hz. Twitches fuse into a smooth, sustained plateau. Label Complete tetanus.",
                    "Below the graph write one sentence: why does higher frequency produce more force?",
                ],
                "height": 320,
            },
        ],
        "label_list": [
            "Motor neuron cell body", "Axon", "Axon terminal",
            "Neuromuscular junction", "Muscle fiber",
            "Small motor unit", "Large motor unit",
            "Single twitch", "Wave summation", "Complete tetanus",
        ],
        "physio_activity_title": "2A. Fiber type comparison table",
        "physio_activity_intro": (
            "Fill in the table below. Use one short phrase per cell. After "
            "the table, answer the two interpretation questions in complete "
            "sentences."
        ),
        "physio_table": {
            "headers": ["Property", "Type I (slow oxidative)", "Type IIa (fast oxidative)", "Type IIx (fast glycolytic)"],
            "rows": [
                ["Myosin ATPase rate", "", "", ""],
                ["Mitochondria density", "", "", ""],
                ["Capillary supply", "", "", ""],
                ["Fatigue resistance", "", "", ""],
                ["Primary energy system", "", "", ""],
            ],
        },
        "physio_followups": [
            "Which fiber type would dominate the postural muscles of the back? Justify in one sentence.",
            "A 100-meter sprinter and a marathon runner are tested. Whose calves would have a higher percentage of Type IIx fibers? Whose would have the most mitochondria? Justify each.",
        ],
        "synthesis_questions": [
            "Eye muscles are innervated by very small motor units (only a handful of fibers each). Explain why this design works beautifully for precision tracking but would fail for lifting a heavy object.",
            "Apply the size principle. A person picks up a coffee cup. Then the same person attempts a deadlift. Which motor units are recruited in each case, and in what order?",
            "Train a sprinter on explosive jumping and a marathoner on long slow distance for six months. Predict which fiber type each adapts most strongly and the physiological mechanism behind the adaptation.",
        ],
    },
    {
        "filename": "workbook_day14_sliding-filament-and-the-cross-bridge-cycle.html",
        "title": "Sliding Filament and the Cross-Bridge Cycle",
        "subhead": "How calcium, ATP, actin, and myosin convert chemical energy into mechanical force.",
        "eyebrow": "BIO 304 . WEEK 4 . TUESDAY . LAB WORKBOOK",
        "day_num": 14,
        "anatomy_intro": (
            "You will draw the cross-bridge cycle as a 4-step loop. Draw "
            "a large square. At each corner, draw what myosin and actin look "
            "like at that step. Use arrows to show the direction of the "
            "cycle (clockwise)."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The 4-step cross-bridge cycle",
                "instructions": [
                    "Draw a large square that fills the box.",
                    "Top-left corner: COCKING. Draw a myosin head in its high-energy, cocked position. Label it. Note that ATP has just been hydrolyzed to ADP plus Pi, both still bound to myosin.",
                    "Top-right corner: BINDING. Draw the myosin head attached to actin. Note that calcium has bound troponin and tropomyosin has shifted to expose the actin binding site.",
                    "Bottom-right corner: POWER STROKE. Draw the myosin head pivoted, pulling actin toward the M line. Note that ADP and Pi are released.",
                    "Bottom-left corner: DETACHMENT. Draw the myosin head with a NEW ATP bound, released from actin. Note that ATP binding is required for detachment.",
                    "Connect the corners with clockwise arrows. Mark every step where ATP is consumed or required.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Calcium release and reuptake",
                "instructions": [
                    "Draw the sarcolemma at the top of the box, with an action potential arriving (use a small arrow).",
                    "Draw a T-tubule diving down from the sarcolemma into the cell.",
                    "Draw the sarcoplasmic reticulum wrapping a myofibril below.",
                    "Add arrows showing Ca-squared-plus flowing OUT of the SR into the cytoplasm during stimulation.",
                    "Draw a second small panel beside this one labeled Relaxation. Show the SR Ca-squared-plus ATPase pumping calcium BACK into the SR.",
                    "Label every structure: Sarcolemma, T-tubule, Sarcoplasmic reticulum, Triad, SR calcium ATPase.",
                ],
                "height": 360,
            },
        ],
        "label_list": [
            "Myosin head (cocked)", "Myosin head (bound)",
            "Myosin head (post power stroke)", "Actin binding site",
            "Troponin", "Tropomyosin", "Calcium (Ca2+)",
            "ATP", "ADP + Pi", "Power stroke arrow",
            "Sarcolemma", "T-tubule", "Sarcoplasmic reticulum",
            "Triad", "SR Ca2+ ATPase",
        ],
        "physio_activity_title": "2A. Sequencing puzzle: from nerve to power stroke",
        "physio_activity_intro": (
            "Below are 10 events involved in producing a single power stroke. "
            "They are listed in SCRAMBLED order. Rewrite them in the correct "
            "sequence in the numbered space provided. Start with the motor "
            "neuron action potential and end with the power stroke."
        ),
        "physio_scrambled_events": [
            "Voltage-gated calcium channels open at the axon terminal.",
            "Myosin head pivots and pulls actin toward the M line.",
            "Acetylcholine binds nicotinic receptors on the sarcolemma.",
            "Action potential reaches the axon terminal of the motor neuron.",
            "Calcium binds troponin; tropomyosin shifts off the binding site.",
            "Sarcolemma depolarizes; action potential travels along T-tubules.",
            "Sarcoplasmic reticulum releases calcium into the cytoplasm.",
            "Acetylcholine is released into the synaptic cleft.",
            "Myosin head binds the exposed site on actin (cross-bridge forms).",
            "ATP is hydrolyzed; myosin head cocks into its high-energy position.",
        ],
        "synthesis_questions": [
            "Rigor mortis sets in hours after death. Explain the molecular mechanism using your cycle drawing. Which step cannot proceed, and why?",
            "Curare blocks the nicotinic acetylcholine receptor at the neuromuscular junction. At which step does the entire chain stall, and what is the patient's clinical picture?",
            "Malignant hyperthermia is caused by a mutation that makes the SR calcium release channel hyperactive in response to certain anesthetics. Walk through the cycle and explain why body temperature climbs so rapidly.",
        ],
    },
    {
        "filename": "workbook_day15_neurons-and-resting-membrane-potential.html",
        "title": "Neurons and Resting Membrane Potential",
        "subhead": "Neuron anatomy, glia, and how the resting potential is built and maintained.",
        "eyebrow": "BIO 304 . WEEK 4 . THURSDAY . LAB WORKBOOK",
        "day_num": 15,
        "anatomy_intro": (
            "Two drawings today. Box A is a labeled neuron. Box B is a "
            "close-up of a patch of resting membrane showing the pumps, "
            "channels, and ion distribution responsible for the resting "
            "potential."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The neuron",
                "instructions": [
                    "Draw a cell body (soma) as an irregular circle. Show a nucleus inside.",
                    "Add 3 to 5 short branched dendrites projecting from the soma.",
                    "Extend a single long process from the opposite side. Label its base Axon hillock.",
                    "Wrap the axon with discrete myelin segments. Show at least 2 unmyelinated gaps. Label one gap Node of Ranvier.",
                    "Identify which cell type makes the myelin: if CNS, an oligodendrocyte; if PNS, a Schwann cell. Pick one and label it.",
                    "End the axon in several axon terminals (small swellings). Label one.",
                ],
                "height": 320,
            },
            {
                "id": "B",
                "label": "Box B. Resting membrane close-up",
                "instructions": [
                    "Draw a horizontal rectangle representing a patch of plasma membrane. Label the top Outside (extracellular) and the bottom Inside (cytoplasm).",
                    "Draw a Na-K ATPase pump straddling the membrane. Show arrows: 3 Na-plus leaving the cell, 2 K-plus entering, ATP being consumed.",
                    "Draw at least 2 K-plus leak channels in the membrane. Show K-plus leaking OUT down its gradient.",
                    "On the outside, write a large Na-plus and a small K-plus. On the inside, write a small Na-plus and a large K-plus. (Show which ion is more concentrated where.)",
                    "Indicate charge: a row of minus signs lining the inside of the membrane and plus signs lining the outside.",
                    "In the corner, write the resting potential value: about negative 70 millivolts.",
                ],
                "height": 320,
            },
        ],
        "label_list": [
            "Dendrites", "Cell body (soma)", "Nucleus",
            "Axon hillock", "Axon", "Myelin sheath", "Node of Ranvier",
            "Schwann cell or oligodendrocyte", "Axon terminal",
            "Na+/K+ ATPase", "K+ leak channel",
            "Na+ (high outside)", "K+ (high inside)",
            "Resting membrane potential (-70 mV)",
        ],
        "physio_activity_title": "2A. Calculation: who builds the resting potential?",
        "physio_activity_intro": (
            "Use your Box B drawing as the reference. Answer each question. "
            "Show short work where math is involved."
        ),
        "physio_numbered_qs": [
            "Per ATP, the Na+/K+ ATPase moves 3 Na+ out and 2 K+ in. What is the NET charge moved across the membrane per cycle, and in which direction?",
            "Does this NET pump activity make the inside more negative or more positive on its own? Explain.",
            "The membrane is also leaky to K+. Which direction does K+ flow through these leak channels at rest, and why (give the gradient driving it)?",
            "Of the two mechanisms (pump electrogenicity vs K+ leak), which contributes MORE to the -70 mV resting potential? Justify in one or two sentences.",
            "Predict the resting potential of a cell that has lost ALL its K+ leak channels but still has a working Na+/K+ ATPase.",
        ],
        "synthesis_questions": [
            "Ouabain blocks the Na+/K+ ATPase. Predict the resting membrane potential at: (a) 5 seconds, (b) 5 minutes, (c) 5 hours after exposure. Explain the trajectory.",
            "Match each glial cell to one function: astrocyte, oligodendrocyte, microglia, Schwann cell, ependymal cell. Pick from: makes myelin in CNS; makes myelin in PNS; immune surveillance; blood brain barrier support; produces CSF.",
            "A neuron in cold seawater has a resting potential of -90 mV instead of -70 mV. Propose one mechanistic explanation involving the Na+/K+ ATPase or the K+ leak channels.",
        ],
    },
    {
        "filename": "workbook_day16_action-potentials-and-synaptic-transmission.html",
        "title": "Action Potentials and Synaptic Transmission",
        "subhead": "Phases of the action potential, propagation, and how chemical synapses pass the signal on.",
        "eyebrow": "BIO 304 . WEEK 4 . FRIDAY . LAB WORKBOOK",
        "day_num": 16,
        "anatomy_intro": (
            "Two drawings today. Box A is the action potential graph with "
            "channel-state bars. Box B is the chemical synapse. Be precise: "
            "the values on the y-axis matter."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Action potential graph",
                "instructions": [
                    "Draw an x-axis (time, in milliseconds) and a y-axis (membrane voltage, mV, from -90 to +40).",
                    "Plot a single action potential. Start at the resting potential (-70 mV). Rise to threshold (-55 mV). Spike up to about +30 mV. Fall through 0 back down. Dip slightly below -70 mV (afterhyperpolarization) before returning to rest.",
                    "Label each phase on the curve: Resting, Threshold, Depolarization, Peak, Repolarization, Hyperpolarization, Return to rest.",
                    "Below the graph, draw 3 horizontal bars showing when these channels are OPEN, aligned with the curve above: Voltage-gated Na+ (activation gate), Voltage-gated Na+ (inactivation gate closes during peak), Voltage-gated K+.",
                    "Mark the absolute refractory period and the relative refractory period on the time axis.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Chemical synapse",
                "instructions": [
                    "Draw an axon terminal (presynaptic) at the top. Inside it, sketch a cluster of synaptic vesicles. Label them.",
                    "Show voltage-gated Ca-squared-plus channels in the presynaptic membrane, with arrows of Ca-squared-plus entering when an AP arrives.",
                    "Draw the synaptic cleft as a small gap below.",
                    "Draw the postsynaptic membrane below the cleft. Show ligand-gated receptors embedded in it.",
                    "Show neurotransmitter molecules being released into the cleft and binding the postsynaptic receptors.",
                    "Label: Action potential arriving, Voltage-gated Ca2+ channel, Synaptic vesicle, Neurotransmitter, Synaptic cleft, Postsynaptic receptor.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Resting potential (-70 mV)", "Threshold (-55 mV)", "Peak (+30 mV)",
            "Depolarization", "Repolarization", "Hyperpolarization",
            "Absolute refractory period", "Relative refractory period",
            "Voltage-gated Na+ channel", "Voltage-gated K+ channel",
            "Axon terminal", "Voltage-gated Ca2+ channel",
            "Synaptic vesicle", "Neurotransmitter", "Synaptic cleft",
            "Postsynaptic receptor",
        ],
        "physio_activity_title": "2A. Sequence the synapse",
        "physio_activity_intro": (
            "Number the following 7 events in the correct order at a chemical "
            "synapse, starting from the action potential arriving at the axon "
            "terminal and ending with a change in the postsynaptic neuron's "
            "membrane potential."
        ),
        "physio_scrambled_events": [
            "Neurotransmitter binds receptors on the postsynaptic membrane.",
            "Action potential arrives at the axon terminal.",
            "Voltage-gated calcium channels open; calcium flows in.",
            "An EPSP or IPSP is generated in the postsynaptic neuron.",
            "Synaptic vesicles fuse with the presynaptic membrane.",
            "Neurotransmitter diffuses across the synaptic cleft.",
            "Neurotransmitter is released into the synaptic cleft.",
        ],
        "synthesis_questions": [
            "Saltatory conduction is much faster than continuous conduction. Explain the structural reason in terms of where voltage-gated channels cluster and what the action potential actually does between nodes.",
            "Why does a neuron need an inactivation gate on its voltage-gated Na+ channel? Predict what propagation would look like if this gate did not exist. Why is unidirectional conduction important?",
            "SSRIs immediately block serotonin reuptake (within minutes), yet clinical relief from depression takes 4 to 6 weeks. Propose a mechanism for this lag. What downstream changes might account for it?",
        ],
    },

    # ==================================================================
    # WEEK 5
    # ==================================================================
    {
        "filename": "workbook_day17_cns-organization-brain-and-spinal-cord.html",
        "title": "CNS Organization: Brain and Spinal Cord",
        "subhead": "Major brain regions, meninges, ventricles, and the spinal cord.",
        "eyebrow": "BIO 304 . WEEK 5 . MONDAY . LAB WORKBOOK",
        "day_num": 17,
        "anatomy_intro": (
            "Today you'll draw the brain in lateral view with its lobes "
            "and major regions, then a spinal cord cross-section with the "
            "three meningeal layers."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Brain in lateral view",
                "instructions": [
                    "Draw the outline of a brain in left lateral view. Show the convoluted surface (gyri and sulci).",
                    "Divide the cerebrum into four lobes with dashed lines: Frontal (anterior, in front of the central sulcus), Parietal (behind the central sulcus), Temporal (below the lateral sulcus), Occipital (most posterior).",
                    "Label the central sulcus (separates frontal from parietal) and the lateral sulcus (separates temporal).",
                    "Draw the cerebellum below the occipital lobe.",
                    "Draw the brainstem extending down from the center: midbrain, pons, medulla oblongata. Label each.",
                    "Inside the frontal lobe, label the primary motor cortex (just anterior to the central sulcus). Inside the parietal lobe, label the primary somatosensory cortex (just posterior to the central sulcus).",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Spinal cord cross-section with meninges",
                "instructions": [
                    "Draw a round cross-section of the spinal cord.",
                    "Inside, draw a butterfly (H) shape representing gray matter. Label dorsal horn (top), ventral horn (bottom), and central canal (small hole in the middle of the H).",
                    "Around the gray matter, draw the white matter (it surrounds the H). Label.",
                    "Wrap the cord in three meningeal layers. Innermost: pia mater (tight on the cord). Middle: arachnoid mater (with subarachnoid space below it where CSF flows). Outermost: dura mater (thick).",
                    "Label all three layers and the subarachnoid space.",
                    "Outside the dura, draw vertebral bone (the spinal cord sits inside the vertebral canal).",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Frontal lobe", "Parietal lobe", "Temporal lobe", "Occipital lobe",
            "Central sulcus", "Lateral sulcus",
            "Cerebellum", "Midbrain", "Pons", "Medulla oblongata",
            "Primary motor cortex", "Primary somatosensory cortex",
            "Dorsal horn", "Ventral horn", "Central canal",
            "Gray matter", "White matter",
            "Pia mater", "Arachnoid mater", "Dura mater", "Subarachnoid space",
        ],
        "physio_activity_title": "2A. Map the function to the brain region",
        "physio_activity_intro": (
            "For each function below, name the brain region MOST "
            "responsible. Be specific about lobe, gyrus, or subcortical "
            "structure."
        ),
        "physio_numbered_qs": [
            "Voluntary control of skeletal muscle in the right hand.",
            "Conscious sensation of touch from the left foot.",
            "Visual processing of the scene in front of you.",
            "Producing fluent, grammatical speech.",
            "Understanding spoken language.",
            "Balance, posture, and coordination of fine motor movements.",
            "Regulation of heart rate, breathing, and blood pressure (autonomic 'vital signs' centers).",
        ],
        "synthesis_questions": [
            "A patient has a stroke that damages the right primary motor cortex in the region controlling the hand. Predict the side and pattern of weakness, and explain why it's on that side using the concept of decussation.",
            "Bacterial meningitis is an inflammation of the meninges. Explain why a lumbar puncture (collecting CSF from below the spinal cord) is the diagnostic test, and which meningeal space the needle enters.",
            "A car accident causes a spinal cord injury at the C7 level. Predict which functions are lost (motor, sensory, autonomic) and which are preserved, and explain why an injury one level higher would be much more dangerous.",
        ],
    },
    {
        "filename": "workbook_day18_pns-and-autonomic-nervous-system.html",
        "title": "PNS and Autonomic Nervous System",
        "subhead": "Cranial and spinal nerves, reflex arcs, and the sympathetic vs parasympathetic divisions.",
        "eyebrow": "BIO 304 . WEEK 5 . TUESDAY . LAB WORKBOOK",
        "day_num": 18,
        "anatomy_intro": (
            "The peripheral nervous system carries signals to and from the "
            "CNS. The autonomic nervous system handles involuntary "
            "control. Today you'll draw a generic reflex arc, then the "
            "sympathetic vs parasympathetic outflow."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The reflex arc (5 components)",
                "instructions": [
                    "Use the patellar (knee-jerk) reflex as your example. Draw a leg with the patellar tendon being tapped by a reflex hammer.",
                    "Component 1: Receptor. Draw a muscle spindle in the quadriceps. Label.",
                    "Component 2: Sensory (afferent) neuron. Draw an axon going from the muscle spindle up to the spinal cord, entering the dorsal horn.",
                    "Component 3: Integration center. Inside the spinal cord, show a single synapse (this is a monosynaptic reflex). Label.",
                    "Component 4: Motor (efferent) neuron. Draw an axon leaving the ventral horn and going back down to the quadriceps.",
                    "Component 5: Effector. The quadriceps contracts, kicking the leg up. Label.",
                    "Add arrows showing the direction of signal flow.",
                ],
                "height": 440,
            },
            {
                "id": "B",
                "label": "Box B. Sympathetic vs parasympathetic outflow",
                "instructions": [
                    "Draw a side view of the spinal column.",
                    "Sympathetic (thoracolumbar): show preganglionic fibers leaving the spinal cord from T1 through L2. Draw the sympathetic chain ganglia running parallel to the cord. Show short preganglionic fibers ending in chain ganglia, then long postganglionic fibers traveling to target organs.",
                    "Parasympathetic (craniosacral): show preganglionic fibers leaving from the brainstem (via cranial nerves III, VII, IX, and especially X, the vagus) AND from S2-S4 (sacral). Show long preganglionic fibers traveling to ganglia near or on the target organs, then very short postganglionic fibers.",
                    "Label two target organs (e.g., heart, lungs, gut) and note opposing effects: sympathetic increases heart rate, parasympathetic decreases it.",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Receptor (muscle spindle)", "Sensory neuron (afferent)",
            "Dorsal horn", "Integration center (spinal cord synapse)",
            "Motor neuron (efferent)", "Ventral horn", "Effector (skeletal muscle)",
            "Sympathetic chain ganglia",
            "Preganglionic fiber (sympathetic)", "Postganglionic fiber (sympathetic)",
            "Preganglionic fiber (parasympathetic)", "Postganglionic fiber (parasympathetic)",
            "Vagus nerve (CN X)",
        ],
        "physio_activity_title": "2A. Sympathetic vs parasympathetic comparison",
        "physio_activity_intro": (
            "Fill in the table comparing the two autonomic divisions. "
            "Then answer the two follow-up questions."
        ),
        "physio_table": {
            "headers": ["Property", "Sympathetic", "Parasympathetic"],
            "rows": [
                ["Origin in CNS (thoracolumbar / craniosacral)", "", ""],
                ["Preganglionic fiber length (short / long)", "", ""],
                ["Effect on heart rate", "", ""],
                ["Effect on pupil diameter", "", ""],
                ["Effect on GI motility", "", ""],
                ["Effect on bronchial smooth muscle", "", ""],
                ["Effect on sweat glands", "", ""],
            ],
        },
        "physio_followups": [
            "Why are sympathetic effects more widespread (affecting many organs at once) while parasympathetic effects are more targeted? Justify using preganglionic fiber length and ganglion location.",
            "Both divisions release acetylcholine at preganglionic synapses. At postganglionic targets, sympathetic typically releases norepinephrine and parasympathetic releases acetylcholine. Predict what beta-blocker drugs (which block norepinephrine receptors in the heart) do to heart rate, and why.",
        ],
        "synthesis_questions": [
            "A person is startled by a loud noise. List 5 specific sympathetic effects they experience over the next 10 seconds. For each, identify the target organ and the response.",
            "After eating a large meal, parasympathetic activity dominates. Predict at least 3 specific physiological changes in this state and explain how 'rest and digest' is the appropriate metabolic context.",
            "A patient takes an anticholinergic medication for an overactive bladder. Predict the side effects this drug will produce across other organs that also respond to acetylcholine. Why are dry mouth, blurred vision, and constipation common with these drugs?",
        ],
    },
    {
        "filename": "workbook_day19_vision.html",
        "title": "Vision",
        "subhead": "The eye, the retina, and how light becomes a neural signal.",
        "eyebrow": "BIO 304 . WEEK 5 . THURSDAY . LAB WORKBOOK",
        "day_num": 19,
        "anatomy_intro": (
            "Vision starts with light bending through the cornea and lens, "
            "and ends with action potentials traveling up the optic nerve. "
            "Today you'll draw the eye in sagittal section and the retinal "
            "layers in close-up."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Eye in sagittal section",
                "instructions": [
                    "Draw an eye in cross-section as viewed from the side. The front of the eye is on the LEFT, the back is on the RIGHT.",
                    "Draw the cornea (transparent dome at the front).",
                    "Draw the iris (colored ring) and the pupil (opening in the center). Label both.",
                    "Draw the lens behind the iris. Show the ciliary body and suspensory ligaments holding the lens.",
                    "Label the anterior chamber (between cornea and iris, contains aqueous humor) and the posterior chamber.",
                    "Fill the rest of the eye (the large back portion) with vitreous humor. Label.",
                    "Line the back of the eye with the retina. Label.",
                    "Mark the fovea centralis (small pit in the central retina, point of sharpest vision).",
                    "Show the optic nerve leaving the back of the eye. Label the optic disc (blind spot) where the nerve exits.",
                    "Wrap the eye with sclera (white outer layer) and choroid (vascular middle layer).",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Retinal layers (light path)",
                "instructions": [
                    "Draw a horizontal section of retina. The light arrives from the BOTTOM (yes, paradoxically) and the photoreceptors face the TOP (away from the light).",
                    "Layer 1 (bottom): retinal ganglion cells. Their axons form the optic nerve. Label.",
                    "Layer 2: bipolar cells.",
                    "Layer 3 (top): photoreceptors. Draw both rods (long, dim light, peripheral vision) and cones (shorter, bright light, color vision, concentrated at the fovea).",
                    "Above the photoreceptors, draw the retinal pigment epithelium (RPE, a dark layer that absorbs stray light).",
                    "Add arrows showing the path of light entering at the bottom and the path of the neural signal going DOWN from photoreceptors to bipolars to ganglion cells.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Cornea", "Iris", "Pupil", "Lens", "Ciliary body",
            "Suspensory ligaments", "Aqueous humor", "Vitreous humor",
            "Retina", "Fovea centralis", "Optic disc", "Optic nerve",
            "Sclera", "Choroid",
            "Photoreceptor", "Rod", "Cone",
            "Bipolar cell", "Retinal ganglion cell",
            "Retinal pigment epithelium",
        ],
        "physio_activity_title": "2A. Trace: from photon to action potential",
        "physio_activity_intro": (
            "List the 7 steps that occur from a photon entering the eye "
            "to an action potential traveling up the optic nerve. Be "
            "precise about which structures the light passes through and "
            "where signal transduction happens."
        ),
        "physio_activity_rows": 7,
        "synthesis_questions": [
            "A patient with myopia (nearsightedness) has trouble seeing distant objects. Explain the optical defect (eyeball shape or lens shape) and how a corrective lens fixes it.",
            "A patient is diagnosed with macular degeneration (loss of cone-rich foveal retina). Predict which type of vision is lost FIRST (peripheral, central, color, night) and which is preserved longest, with a one-sentence reason.",
            "Why is the optic disc called the blind spot? Predict what happens when an image falls on the optic disc, and explain why we don't normally notice this gap in our visual field.",
        ],
    },
    {
        "filename": "workbook_day19_hearing-and-equilibrium.html",
        "title": "Hearing and Equilibrium",
        "subhead": "From sound waves at the eardrum to hair cells in the cochlea; and how we sense head position and motion.",
        "eyebrow": "BIO 304 . WEEK 5 . THURSDAY . LAB WORKBOOK",
        "day_num": 19,
        "anatomy_intro": (
            "The ear handles two senses: hearing (cochlea) and equilibrium "
            "(vestibular system). Today you'll draw the three regions of "
            "the ear, then the organ of Corti inside the cochlea."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Outer, middle, and inner ear",
                "instructions": [
                    "Draw an ear in cross-section from outside to inside. Divide into three regions with vertical lines.",
                    "Outer ear (left): pinna (the visible external ear) and external auditory canal leading to the tympanic membrane (eardrum). Label.",
                    "Middle ear (center): air-filled space behind the eardrum, containing three tiny bones (the ossicles): malleus, incus, stapes. Label each. Show the stapes contacting the oval window of the cochlea.",
                    "Inner ear (right): draw the cochlea as a snail-shell spiral (fluid-filled, handles hearing). Above it, draw the three semicircular canals (orthogonal loops) and the vestibule (linear motion). Label all four structures.",
                    "Add the Eustachian tube connecting the middle ear to the throat (pressure equalization).",
                ],
                "height": 420,
            },
            {
                "id": "B",
                "label": "Box B. Organ of Corti close-up",
                "instructions": [
                    "Draw a cross-section of the cochlear duct showing the organ of Corti sitting on the basilar membrane.",
                    "Label the basilar membrane (under the hair cells, vibrates at different frequencies along its length).",
                    "Draw hair cells: a single row of inner hair cells (the main sensory cells) and three rows of outer hair cells (amplifiers). Label.",
                    "Show stereocilia (hair-like projections) on top of each hair cell, contacting the tectorial membrane above. Label both.",
                    "Show the cochlear nerve fibers leaving the base of the hair cells.",
                    "Note the principle: when the basilar membrane vibrates, the stereocilia bend against the tectorial membrane, opening ion channels in the hair cell, leading to neurotransmitter release.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Pinna", "External auditory canal", "Tympanic membrane",
            "Malleus", "Incus", "Stapes", "Oval window",
            "Cochlea", "Vestibule", "Semicircular canals",
            "Eustachian tube",
            "Basilar membrane", "Tectorial membrane",
            "Inner hair cell", "Outer hair cell", "Stereocilia",
            "Cochlear nerve",
        ],
        "physio_activity_title": "2A. Trace: sound wave to action potential",
        "physio_activity_intro": (
            "List the 8 steps that occur from a sound wave in air to an "
            "action potential in the cochlear nerve. Identify each "
            "structure the signal passes through and what changes."
        ),
        "physio_activity_rows": 8,
        "synthesis_questions": [
            "A patient has conductive hearing loss (e.g., a fluid-filled middle ear from an infection). Explain mechanistically why sound transmission fails, and contrast with sensorineural hearing loss (damaged hair cells or cochlear nerve).",
            "A passenger gets out of a spinning teacup ride and feels dizzy. Explain what is happening in their semicircular canals during and just after the spin, and why the world appears to keep moving even after they've stopped.",
            "High-frequency sounds are detected near the BASE of the cochlea, while low-frequency sounds are detected near the APEX. Explain how the basilar membrane's structural properties produce this 'tonotopic' map.",
        ],
    },
    {
        "filename": "workbook_day20_hormone-mechanisms.html",
        "title": "Hormone Mechanisms",
        "subhead": "Two pathways: steroid hormones acting on intracellular receptors; peptide hormones acting through membrane receptors and second messengers.",
        "eyebrow": "BIO 304 . WEEK 5 . FRIDAY . LAB WORKBOOK",
        "day_num": 20,
        "anatomy_intro": (
            "Hormones are signaling molecules. The chemistry of the "
            "hormone determines its mechanism: steroids (lipid-soluble) "
            "cross the membrane and act on receptors inside the cell; "
            "peptides (water-soluble) act on receptors at the cell "
            "surface. Draw both pathways."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Steroid hormone mechanism",
                "instructions": [
                    "Draw a target cell with its plasma membrane, cytoplasm, and nucleus visible.",
                    "Outside the cell, draw a steroid hormone (small ring structure, label e.g., cortisol or estrogen).",
                    "Show the hormone crossing the plasma membrane (it's lipid-soluble, so it passes directly through).",
                    "Inside the cytoplasm, show the hormone binding an intracellular receptor protein. Label receptor.",
                    "Show the hormone-receptor complex moving into the nucleus.",
                    "Inside the nucleus, show the complex binding DNA at a specific gene. Label DNA, gene.",
                    "Show transcription starting, then mRNA leaving the nucleus, then a new protein being made on ribosomes in the cytoplasm.",
                    "Note: response takes hours (gene transcription is slow), but effects last long.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Peptide hormone mechanism",
                "instructions": [
                    "Draw a target cell with its plasma membrane and cytoplasm.",
                    "Outside the cell, draw a peptide hormone (chain structure, label e.g., insulin or glucagon).",
                    "Show the hormone binding to a receptor on the OUTSIDE of the plasma membrane (it cannot cross). Label the membrane receptor.",
                    "Show the receptor activating a G-protein on the inside of the membrane. Label G-protein.",
                    "Show the G-protein activating an enzyme (e.g., adenylyl cyclase), which converts ATP to cAMP. Label the second messenger cAMP.",
                    "Show cAMP activating protein kinase A, which phosphorylates target proteins inside the cell, changing their activity.",
                    "Note: response is rapid (seconds to minutes), and amplification means one hormone produces many cellular changes.",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Steroid hormone", "Plasma membrane (lipid-soluble crosses)",
            "Cytoplasmic receptor", "Hormone-receptor complex",
            "Nucleus", "DNA", "Gene transcription", "mRNA",
            "Peptide hormone", "Membrane receptor",
            "G-protein", "Adenylyl cyclase", "cAMP (second messenger)",
            "Protein kinase A",
        ],
        "physio_activity_title": "2A. Steroid vs peptide comparison",
        "physio_activity_intro": (
            "Fill in the table. Then answer the two follow-up questions."
        ),
        "physio_table": {
            "headers": ["Property", "Steroid hormones", "Peptide hormones"],
            "rows": [
                ["Solubility (lipid / water)", "", ""],
                ["Receptor location", "", ""],
                ["Speed of onset (minutes / hours)", "", ""],
                ["Duration of effect", "", ""],
                ["Mechanism of action", "", ""],
                ["Example hormone", "", ""],
            ],
        },
        "physio_followups": [
            "Peptide hormones use second messengers (cAMP, IP3, Ca-squared-plus, etc.) to amplify their signal. Explain why amplification is important for water-soluble hormones acting at low concentrations.",
            "Steroid hormones often produce long-lasting effects (hours to days). Explain mechanistically why steroid effects outlast peptide effects, and why steroid pulses are slower than peptide pulses.",
        ],
        "synthesis_questions": [
            "Cortisol (a steroid) and epinephrine (a peptide-like catecholamine) both raise blood glucose during stress. Compare their speeds of action and durations, and explain why the body uses both.",
            "A patient takes oral prednisone (a synthetic steroid) for several weeks, then suddenly stops. They become very ill (Addisonian crisis). Explain mechanistically why abrupt steroid withdrawal is dangerous, in terms of feedback to the hypothalamus and pituitary.",
            "Insulin is a peptide and CANNOT be taken orally. Explain mechanistically why oral insulin doesn't work, while a steroid hormone like prednisone CAN be taken orally.",
        ],
    },
    {
        "filename": "workbook_day20_major-endocrine-glands.html",
        "title": "Major Endocrine Glands",
        "subhead": "Pituitary, thyroid, adrenal, pancreas: who makes what, who controls them.",
        "eyebrow": "BIO 304 . WEEK 5 . FRIDAY . LAB WORKBOOK",
        "day_num": 20,
        "anatomy_intro": (
            "The major endocrine glands sit at predictable locations in "
            "the body and produce specific hormones with specific targets. "
            "Today you'll draw a body outline locating each gland, then "
            "zoom in on the pituitary and its hypothalamic control."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Endocrine gland locations",
                "instructions": [
                    "Draw a simple body outline (head, trunk, limbs).",
                    "At the base of the brain (deep inside the skull): pituitary gland. Label.",
                    "In the neck (anterior, below the larynx): thyroid gland. Label.",
                    "On top of each kidney (just above the kidneys): adrenal glands. Label.",
                    "In the abdomen, behind the stomach: pancreas. Label.",
                    "In the pelvis: ovaries (in females) or testes (in males). Label.",
                    "In the chest (upper thorax): thymus (label, large in children, smaller in adults).",
                    "Add small notes next to each gland with ONE major hormone it produces.",
                ],
                "height": 440,
            },
            {
                "id": "B",
                "label": "Box B. Pituitary close-up",
                "instructions": [
                    "Draw the hypothalamus (above) connected to the pituitary gland (below) by a stalk (infundibulum).",
                    "Split the pituitary into two parts: ANTERIOR pituitary (larger, glandular) and POSTERIOR pituitary (smaller, nervous tissue).",
                    "Anterior pituitary: hypothalamic neurons release releasing hormones into a portal blood system that travels to the anterior pituitary. The anterior pituitary then releases its OWN hormones into the general circulation. Label hypothalamic-pituitary portal system.",
                    "List 4 anterior pituitary hormones: TSH, ACTH, FSH/LH, GH, Prolactin (pick any 4 and label).",
                    "Posterior pituitary: hypothalamic neurons send axons directly into the posterior pituitary. Their hormones (ADH, oxytocin) are stored there and released directly into circulation.",
                    "Label ADH and oxytocin as posterior pituitary hormones.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Hypothalamus", "Pituitary gland",
            "Anterior pituitary", "Posterior pituitary",
            "Thyroid gland", "Adrenal gland", "Pancreas",
            "Ovary / Testis", "Thymus",
            "TSH", "ACTH", "Growth hormone (GH)", "ADH (vasopressin)",
            "Oxytocin", "Insulin", "Glucagon",
            "Thyroid hormone (T3/T4)", "Cortisol", "Epinephrine",
        ],
        "physio_activity_title": "2A. Gland, hormone, target, effect",
        "physio_activity_intro": (
            "Fill in the table. Pick one major hormone per gland and "
            "complete each row."
        ),
        "physio_table": {
            "headers": ["Gland", "Hormone", "Main target tissue", "Main effect"],
            "rows": [
                ["Anterior pituitary", "", "", ""],
                ["Thyroid (follicular cells)", "", "", ""],
                ["Adrenal cortex", "", "", ""],
                ["Adrenal medulla", "", "", ""],
                ["Pancreas (beta cells)", "", "", ""],
                ["Pancreas (alpha cells)", "", "", ""],
                ["Posterior pituitary", "", "", ""],
            ],
        },
        "physio_followups": [
            "Insulin and glucagon are both made by the pancreas but have opposing effects on blood glucose. Predict which is released after a meal, which during fasting, and explain how their opposing actions stabilize blood glucose.",
            "The anterior pituitary releases trophic hormones (TSH, ACTH, FSH/LH) that act on OTHER endocrine glands. Explain why this multi-step system gives finer regulation than a single hormone acting directly, using the negative feedback concept.",
        ],
        "synthesis_questions": [
            "Type 1 diabetes destroys pancreatic beta cells. Predict the patient's blood glucose level after a meal AND after an overnight fast, and explain mechanistically what is happening in each state.",
            "Cushing's syndrome is caused by excess cortisol. Predict the patient's symptoms (across blood glucose, body fat distribution, immune function, bone density). For each, explain mechanistically why cortisol produces that effect.",
            "A pituitary tumor compresses the posterior pituitary and reduces ADH release (diabetes insipidus). Predict the patient's urine output, blood sodium concentration, and behavior. Why is ADH critical for water homeostasis?",
        ],
    },

    # ==================================================================
    # WEEK 6
    # ==================================================================
    {
        "filename": "workbook_day21_blood-composition-and-hemopoiesis.html",
        "title": "Blood Composition and Hemopoiesis",
        "subhead": "Plasma, erythrocytes, leukocytes, platelets, and where all of them come from.",
        "eyebrow": "BIO 304 . WEEK 6 . MONDAY . LAB WORKBOOK",
        "day_num": 21,
        "anatomy_intro": (
            "Blood is a connective tissue with cells suspended in a fluid "
            "matrix (plasma). Today you'll draw a blood smear with all "
            "the cell types, then a hemopoiesis tree showing where each "
            "cell comes from."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Blood smear",
                "instructions": [
                    "Draw a blood smear field as if seen through a microscope: lots of small biconcave discs and a few larger nucleated cells.",
                    "Draw many red blood cells (erythrocytes): small, round, biconcave (pale center), no nucleus. Label.",
                    "Draw one neutrophil: a leukocyte with a multi-lobed nucleus (3 to 5 lobes) connected by thin strands. Most common WBC. Label.",
                    "Draw one lymphocyte: a leukocyte with a large round dark nucleus filling most of the cell, very thin rim of cytoplasm. Label.",
                    "Draw one monocyte: a leukocyte with a kidney-shaped or horseshoe-shaped nucleus, larger than the others. Label.",
                    "Draw one eosinophil: a leukocyte with a bilobed nucleus and pink-red cytoplasmic granules. Label.",
                    "Draw a few platelets (thrombocytes): tiny irregular cell fragments, no nucleus. Label.",
                    "In the background, write Plasma (the yellow fluid between cells, about 55% of blood volume). Label.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Hemopoiesis tree",
                "instructions": [
                    "Draw a tree diagram starting at the top with a single cell: the hematopoietic stem cell (HSC) in red bone marrow.",
                    "Branch downward into two paths: myeloid lineage (left) and lymphoid lineage (right).",
                    "Myeloid lineage produces: erythrocytes, neutrophils, eosinophils, basophils, monocytes (which become macrophages), and platelets (from megakaryocytes).",
                    "Lymphoid lineage produces: B lymphocytes, T lymphocytes, natural killer (NK) cells.",
                    "Draw arrows pointing down at each branch. Label every cell type.",
                    "At the bottom of the tree, list which cell types END UP IN BLOOD vs which migrate elsewhere (e.g., T cells mature in the thymus, not in marrow).",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Red blood cell (erythrocyte)", "Plasma",
            "Neutrophil", "Lymphocyte", "Monocyte",
            "Eosinophil", "Basophil",
            "Platelet (thrombocyte)",
            "Hematopoietic stem cell (HSC)",
            "Myeloid lineage", "Lymphoid lineage",
            "Megakaryocyte", "Macrophage",
            "B lymphocyte", "T lymphocyte", "Natural killer cell",
        ],
        "physio_activity_title": "2A. Match the cell to its job",
        "physio_activity_intro": (
            "For each function below, name the blood cell type responsible. "
            "Be specific where possible."
        ),
        "physio_numbered_qs": [
            "Carries oxygen from lungs to tissues using hemoglobin.",
            "First responder to a bacterial infection; phagocytoses bacteria.",
            "Long-term, antibody-based immune response.",
            "Direct cell-mediated immunity, including killing virus-infected cells.",
            "Fights parasitic infections and modulates allergic responses.",
            "Releases histamine in allergic and inflammatory responses.",
            "Becomes a tissue macrophage after leaving the bloodstream.",
            "Forms the initial platelet plug at a site of vascular injury.",
        ],
        "synthesis_questions": [
            "Anemia is a deficiency of functional erythrocytes or hemoglobin. Predict the patient's symptoms (energy, exertion tolerance, skin color, heart rate) and explain why each occurs in terms of oxygen delivery.",
            "Leukemia is a cancer of white blood cell precursors in the bone marrow. The marrow produces many non-functional cells, crowding out normal hemopoiesis. Predict consequences across all three blood cell lineages and explain why patients become both immunocompromised AND anemic AND prone to bleeding.",
            "An athlete moves to high altitude (lower oxygen). Within weeks, their hematocrit (proportion of red cells) rises. Explain the mechanism, including which hormone signals this change and which organ produces it.",
        ],
    },
    {
        "filename": "workbook_day21_hemostasis-and-blood-typing.html",
        "title": "Hemostasis and Blood Typing",
        "subhead": "How bleeding stops, and why blood types matter for transfusion.",
        "eyebrow": "BIO 304 . WEEK 6 . MONDAY . LAB WORKBOOK",
        "day_num": 21,
        "anatomy_intro": (
            "Two clinically important topics today. Hemostasis is the "
            "three-step process that stops bleeding after vascular "
            "injury. Blood typing determines which transfusions are safe."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. The three steps of hemostasis",
                "instructions": [
                    "Draw a cut blood vessel in cross-section. Show blood escaping.",
                    "Step 1: Vascular spasm. Draw the vessel constricting at the injury site (smaller diameter). Label.",
                    "Step 2: Platelet plug formation. Draw platelets adhering to exposed collagen at the injury, sticking to each other and forming a soft plug. Label.",
                    "Step 3: Coagulation. Draw a meshwork of fibrin strands trapping platelets and red blood cells. The platelet plug is now reinforced into a stable clot. Label fibrin, clot.",
                    "Below the drawing, write a one-sentence summary of what triggers each step.",
                ],
                "height": 440,
            },
            {
                "id": "B",
                "label": "Box B. ABO blood typing matrix",
                "instructions": [
                    "Draw a 4-by-3 table.",
                    "Rows: blood types A, B, AB, O.",
                    "Columns: antigens present on RBC, antibodies in plasma, can give blood to, can receive blood from.",
                    "Fill in each cell for each blood type.",
                    "Examples: Type A has A antigens on RBCs, anti-B antibodies in plasma, can give to A and AB, can receive from A and O.",
                    "Note Type O is the universal donor (no antigens) and Type AB is the universal recipient (no antibodies).",
                    "Below the matrix, add Rh: Rh-positive has Rh antigen on RBCs; Rh-negative does not. Anti-Rh antibodies only develop after exposure.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Vascular spasm", "Platelet plug", "Fibrin", "Clot",
            "Coagulation cascade", "Collagen (exposed)",
            "Type A", "Type B", "Type AB", "Type O",
            "A antigen", "B antigen", "Anti-A antibody", "Anti-B antibody",
            "Rh antigen", "Universal donor (O-negative)",
            "Universal recipient (AB-positive)",
        ],
        "physio_activity_title": "2A. Transfusion compatibility",
        "physio_activity_intro": (
            "For each patient-donor pair below, determine if the "
            "transfusion is SAFE or DANGEROUS, and explain in one "
            "sentence why."
        ),
        "physio_numbered_qs": [
            "Donor type A blood given to a type B recipient.",
            "Donor type O blood given to a type AB recipient.",
            "Donor type AB blood given to a type O recipient.",
            "Donor Rh-positive blood given to an Rh-negative recipient who has never been transfused before.",
            "Donor Rh-positive blood given to an Rh-negative recipient who has already received Rh-positive blood once before.",
            "Donor type O-negative blood given to a type B-positive recipient.",
        ],
        "synthesis_questions": [
            "Hemophilia A is a deficiency of clotting factor VIII. Walk through hemostasis and explain which step fails, while pointing out which steps are still intact. Why do patients still form initial platelet plugs?",
            "Warfarin (Coumadin) is a common anticoagulant. It blocks the synthesis of vitamin-K-dependent clotting factors. Predict the effect on hemostasis at low and high doses, and explain why patients on warfarin need regular blood tests to monitor clotting time.",
            "An Rh-negative woman has her first child with an Rh-positive man. The first pregnancy is usually fine, but the second can be dangerous. Explain mechanistically what happens between pregnancies and why Rh immunoglobulin (RhoGAM) is given to prevent this complication.",
        ],
    },
    {
        "filename": "workbook_day22_heart-anatomy-and-the-cardiac-cycle.html",
        "title": "Heart Anatomy and the Cardiac Cycle",
        "subhead": "Four chambers, four valves, two circuits, and the rhythm of systole and diastole.",
        "eyebrow": "BIO 304 . WEEK 6 . TUESDAY . LAB WORKBOOK",
        "day_num": 22,
        "anatomy_intro": (
            "The heart is two pumps in one organ: the right side serves "
            "the pulmonary circuit (to lungs), the left side serves the "
            "systemic circuit (to body). Today you'll draw the heart in "
            "frontal section, then walk through one cardiac cycle."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Heart in frontal section",
                "instructions": [
                    "Draw the heart with the apex pointing down and to the patient's left. Show four chambers separated by septa.",
                    "Top right: right atrium (RA). Top left: left atrium (LA). Bottom right: right ventricle (RV). Bottom left: left ventricle (LV). Label each.",
                    "Show the four valves: tricuspid (between RA and RV), pulmonary (between RV and pulmonary trunk), mitral or bicuspid (between LA and LV), aortic (between LV and aorta). Label each valve with arrows showing one-way flow.",
                    "Show the great vessels: superior vena cava + inferior vena cava draining into RA; pulmonary trunk leaving RV (to lungs); pulmonary veins entering LA (from lungs); aorta leaving LV.",
                    "Add arrows tracing blood flow: deoxygenated blood enters RA, through tricuspid into RV, out pulmonary to lungs; oxygenated blood returns to LA, through mitral into LV, out aorta to body.",
                    "Note: the LV wall is thicker than the RV wall. Show this with a thicker line. Label myocardium.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. The cardiac cycle (one beat)",
                "instructions": [
                    "Draw two heart silhouettes side by side, both showing all four chambers.",
                    "Left silhouette: DIASTOLE (ventricles relaxed). Show atria contracting and pushing blood into ventricles. Tricuspid and mitral valves OPEN. Pulmonary and aortic valves CLOSED.",
                    "Right silhouette: SYSTOLE (ventricles contracted). Show ventricles squeezing blood out to lungs and body. Tricuspid and mitral valves CLOSED. Pulmonary and aortic valves OPEN.",
                    "Below the silhouettes, draw a pressure-time graph. Show LV pressure rising sharply during systole, falling during diastole. Show aortic pressure following LV during systole, holding higher during diastole (because of valve closure).",
                    "Label end-diastolic volume (EDV, max ventricle volume), end-systolic volume (ESV, min volume after contraction), and stroke volume (SV = EDV minus ESV).",
                    "Note: the heart sounds 'lub-dub' correspond to valve closure: lub = AV valves close at start of systole; dub = semilunar valves close at start of diastole.",
                ],
                "height": 480,
            },
        ],
        "label_list": [
            "Right atrium", "Left atrium", "Right ventricle", "Left ventricle",
            "Tricuspid valve", "Mitral (bicuspid) valve",
            "Pulmonary semilunar valve", "Aortic semilunar valve",
            "Superior vena cava", "Inferior vena cava",
            "Pulmonary trunk", "Pulmonary veins", "Aorta",
            "Interventricular septum", "Myocardium",
            "Systole", "Diastole",
            "End-diastolic volume (EDV)", "End-systolic volume (ESV)", "Stroke volume",
        ],
        "physio_activity_title": "2A. Trace one drop of blood from RA to body",
        "physio_activity_intro": (
            "Trace one drop of blood starting in the right atrium until it "
            "reaches the systemic capillaries delivering oxygen to body "
            "tissues. List every chamber, valve, and vessel it passes "
            "through, in order. Aim for 10 to 12 steps."
        ),
        "physio_activity_rows": 12,
        "synthesis_questions": [
            "A patient has mitral valve regurgitation (the mitral valve doesn't close fully). Predict the effect on blood flow during left ventricular systole, and predict the symptom the patient most often reports.",
            "A myocardial infarction (heart attack) damages the LV wall. Predict the effect on stroke volume, ejection fraction, and the patient's exercise tolerance. Why does LV damage cause backup of blood into the lungs (pulmonary congestion)?",
            "The LV wall is much thicker than the RV wall. Explain why this difference exists, in terms of the pressure the LV must generate vs the RV. What changes in the RV wall when chronic pulmonary hypertension develops?",
        ],
    },
    {
        "filename": "workbook_day23_cardiac-conduction-system.html",
        "title": "Cardiac Conduction System",
        "subhead": "The intrinsic pacemaker, signal propagation, and how the ECG reads it all.",
        "eyebrow": "BIO 304 . WEEK 6 . THURSDAY . LAB WORKBOOK",
        "day_num": 23,
        "anatomy_intro": (
            "The heart's rhythm is set by specialized cardiac cells, not "
            "by nerves from the brain. Today you'll draw the conduction "
            "pathway through the heart, then a normal ECG with its named "
            "waves."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Conduction pathway",
                "instructions": [
                    "Draw a heart silhouette with all four chambers.",
                    "At the top of the right atrium, draw a small oval: the SA node (sinoatrial node). Label. Note: the natural pacemaker, fires at 60 to 100 bpm.",
                    "Show the signal spreading across both atria (small arrows), causing them to contract.",
                    "At the junction of atria and ventricles (in the interatrial septum, near the tricuspid valve), draw the AV node (atrioventricular node). Label. Note: delays the signal by about 0.1 second to let atria empty.",
                    "From the AV node, draw the bundle of His (AV bundle) descending through the interventricular septum. Label.",
                    "Split into right and left bundle branches.",
                    "End in the Purkinje fibers spreading throughout the ventricular walls. Label.",
                    "Add arrows showing the direction of signal flow: SA node, atria, AV node, bundle of His, bundle branches, Purkinje fibers, ventricles contract.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Normal ECG",
                "instructions": [
                    "Draw a single normal ECG cycle (one heartbeat). x-axis is time, y-axis is voltage.",
                    "Start with a flat baseline. Draw a small upward bump: the P wave. Label.",
                    "After P, a brief flat segment (PR segment), then a tall sharp downward-upward-downward complex: the QRS complex. Label Q, R, S.",
                    "After QRS, another flat segment (ST segment), then a smaller rounded upward bump: the T wave. Label.",
                    "Annotate what each wave represents: P = atrial depolarization (atria contract); QRS = ventricular depolarization (ventricles contract); T = ventricular repolarization (ventricles relax).",
                    "Note: atrial repolarization is hidden inside the QRS complex.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "SA (sinoatrial) node", "AV (atrioventricular) node",
            "Bundle of His", "Right bundle branch", "Left bundle branch",
            "Purkinje fibers",
            "P wave", "QRS complex", "T wave",
            "PR interval", "ST segment",
            "Atrial depolarization", "Ventricular depolarization",
            "Ventricular repolarization",
        ],
        "physio_activity_title": "2A. Match ECG component to electrical event",
        "physio_activity_intro": (
            "For each ECG feature below, identify the electrical event AND "
            "the mechanical event that corresponds to it."
        ),
        "physio_numbered_qs": [
            "The P wave.",
            "The PR interval.",
            "The QRS complex.",
            "The ST segment.",
            "The T wave.",
            "A flat line between heartbeats (the baseline).",
        ],
        "synthesis_questions": [
            "A patient is in third-degree (complete) heart block: the atria fire normally, but the signal does not pass through the AV node to the ventricles. The ventricles develop their own slower rhythm. Predict the ECG pattern (relationship between P waves and QRS complexes), and predict the heart rate and the patient's symptoms.",
            "Atrial fibrillation: the atria depolarize chaotically at 400+ times per minute. The AV node filters most of these signals. Predict (a) what happens to the P wave on the ECG, (b) the regularity of QRS complexes, and (c) why patients are at high risk for stroke.",
            "Ventricular fibrillation: ventricles depolarize chaotically. Unlike atrial fibrillation, this is a cardiac emergency. Explain mechanistically why V-fib is immediately life-threatening but A-fib is not, and why a defibrillator works to reset the heart.",
        ],
    },
    {
        "filename": "workbook_day24_blood-vessels-and-hemodynamics.html",
        "title": "Blood Vessels and Hemodynamics",
        "subhead": "Arteries, veins, capillaries, and the physics of blood pressure and flow.",
        "eyebrow": "BIO 304 . WEEK 6 . FRIDAY . LAB WORKBOOK",
        "day_num": 24,
        "anatomy_intro": (
            "Blood vessels are not just pipes. Each type has structural "
            "features tuned to a specific job. Today you'll draw the "
            "three vessel types in cross-section, then a capillary bed "
            "in action."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Artery, vein, and capillary in cross-section",
                "instructions": [
                    "Draw three round vessels side by side: an artery (left), a vein (middle), and a capillary (right). Make them the right relative sizes (capillary is much smaller).",
                    "Artery: thick wall with three layers. Innermost: tunica intima (endothelium). Middle: tunica media (thick smooth muscle and elastic fibers, this is what makes arteries elastic). Outermost: tunica externa (connective tissue). Lumen is small relative to wall thickness.",
                    "Vein: thinner wall, also with three layers but tunica media is much thinner. Larger lumen relative to wall. Show one-way valves inside the vein (small flaps).",
                    "Capillary: very thin wall, just a single layer of endothelium plus a basement membrane. Lumen barely bigger than a single red blood cell.",
                    "Label all three tunica layers in the artery and vein; label endothelium and basement membrane in the capillary.",
                ],
                "height": 420,
            },
            {
                "id": "B",
                "label": "Box B. Capillary bed",
                "instructions": [
                    "Draw an arteriole entering from the left and branching into a meshwork of capillaries. The capillaries reunite into a venule that exits to the right.",
                    "Label arteriole, capillaries, venule.",
                    "At the arteriole-capillary junction, draw small smooth muscle rings: precapillary sphincters. Label.",
                    "Note: precapillary sphincters open or close to direct blood flow into or away from this capillary bed depending on tissue need.",
                    "In the surrounding tissue, draw 4 to 6 cells. Show arrows of oxygen and nutrients leaving the capillaries to enter the cells, and arrows of carbon dioxide and waste leaving the cells to enter the capillaries.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Tunica intima", "Tunica media", "Tunica externa",
            "Endothelium", "Basement membrane", "Smooth muscle",
            "Elastic fibers", "Vein valves",
            "Arteriole", "Capillary", "Venule",
            "Precapillary sphincter",
        ],
        "physio_activity_title": "2A. Blood pressure relationships",
        "physio_activity_intro": (
            "Use the relationship BP equals cardiac output (CO) times "
            "total peripheral resistance (TPR). Answer each question. "
            "Show short work where math or reasoning is helpful."
        ),
        "physio_numbered_qs": [
            "If cardiac output increases by 20 percent and peripheral resistance stays the same, what happens to blood pressure?",
            "If a patient's peripheral resistance drops by half (e.g., during septic shock vasodilation) and cardiac output stays constant, what happens to blood pressure?",
            "Cardiac output equals heart rate times stroke volume. If heart rate is 70 bpm and stroke volume is 70 mL, what is the cardiac output in liters per minute?",
            "Predict what happens to mean arterial pressure when a person stands up quickly from lying down (consider gravity and venous return).",
            "Explain mechanistically why having one-way valves in veins matters for venous return, especially in the lower limbs.",
            "Capillaries are the site of all exchange between blood and tissues. Explain why capillary walls are so thin and why blood flow through capillaries is slow.",
        ],
        "synthesis_questions": [
            "A patient has chronic hypertension (sustained high blood pressure). Predict the long-term changes in the arterial wall structure, and explain why hypertension increases the risk of stroke, heart attack, and kidney damage.",
            "Varicose veins are dilated, twisted veins, typically in the legs. Explain mechanistically what fails (which structural feature), and why varicose veins are more common in people who stand for long periods.",
            "A patient goes into septic shock: massive systemic vasodilation drops their blood pressure dangerously low. Use the BP equation to explain what is changing and why, then predict the body's compensatory responses (heart rate, sympathetic activity, ADH release).",
        ],
    },

    # ==================================================================
    # WEEK 7
    # ==================================================================
    {
        "filename": "workbook_day25_lymphatic-system-and-innate-immunity.html",
        "title": "Lymphatic System and Innate Immunity",
        "subhead": "Lymph nodes, vessels, spleen, thymus; barriers, phagocytes, NK cells, inflammation, complement, fever.",
        "eyebrow": "BIO 304 . WEEK 7 . MONDAY . LAB WORKBOOK",
        "day_num": 25,
        "anatomy_intro": (
            "The lymphatic system both drains tissue fluid and houses the "
            "first line of immune defense. Today you'll draw the major "
            "lymphatic structures across the body, then a close-up of an "
            "inflammatory response in a tissue."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Major lymphatic structures",
                "instructions": [
                    "Draw a simple body outline.",
                    "Lymph nodes: cluster small ovals at the cervical (neck), axillary (armpit), and inguinal (groin) regions. Label each cluster.",
                    "Thymus: in the upper chest behind the sternum. Label (note: large in childhood, atrophies with age).",
                    "Spleen: in the upper left abdomen, behind the stomach. Label.",
                    "MALT (mucosa-associated lymphoid tissue): mark tonsils in the throat, Peyer's patches in the small intestine, and appendix. Label.",
                    "Draw a network of lymphatic vessels running through the body, with two large terminal ducts emptying into veins near the heart: thoracic duct (drains most of the body, empties into the left subclavian vein) and right lymphatic duct (drains right upper body, empties into the right subclavian vein). Label.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Acute inflammation in a tissue",
                "instructions": [
                    "Draw a section of tissue with a small injury (e.g., a splinter introducing bacteria).",
                    "Show a nearby blood capillary. Add arrows pointing OUT from the capillary indicating vasodilation and increased permeability.",
                    "Show fluid leaking from the capillary into the tissue, causing edema (swelling). Label.",
                    "Draw neutrophils squeezing through the capillary wall (diapedesis or extravasation) and migrating toward the bacteria. Label.",
                    "Draw the neutrophils phagocytosing bacteria. Label.",
                    "Mark the four cardinal signs of inflammation around the site: redness (rubor), heat (calor), swelling (tumor), pain (dolor). Add Latin names if you want.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Lymph node", "Cervical nodes", "Axillary nodes", "Inguinal nodes",
            "Thymus", "Spleen", "Tonsils", "Peyer's patches", "Appendix",
            "Lymphatic vessel", "Thoracic duct", "Right lymphatic duct",
            "Vasodilation", "Increased permeability", "Edema",
            "Neutrophil", "Diapedesis (extravasation)", "Phagocytosis",
            "Redness", "Heat", "Swelling", "Pain",
        ],
        "physio_activity_title": "2A. Innate defense table",
        "physio_activity_intro": (
            "Fill in the table classifying innate immune defenses by "
            "category. After the table, answer the two follow-up "
            "questions."
        ),
        "physio_table": {
            "headers": ["Category", "Example", "Mechanism of defense"],
            "rows": [
                ["Physical barrier", "Skin", ""],
                ["Chemical barrier", "Stomach acid (low pH)", ""],
                ["Phagocyte", "Neutrophil", ""],
                ["Phagocyte", "Macrophage", ""],
                ["Cytotoxic innate cell", "Natural killer (NK) cell", ""],
                ["Chemical mediator", "Complement", ""],
                ["Whole-body response", "Fever", ""],
                ["Local response", "Inflammation", ""],
            ],
        },
        "physio_followups": [
            "Fever is a regulated rise in body temperature in response to infection. Explain mechanistically why a moderate fever is BENEFICIAL during a bacterial infection. Why is very high fever (over 41 C) dangerous?",
            "Complement is a cascade of plasma proteins that can punch holes in bacterial membranes. Explain the term 'cascade' in this context, and how this design lets a small initial signal produce a large response.",
        ],
        "synthesis_questions": [
            "A patient has a breast tumor removed along with several axillary lymph nodes. Predict the long-term consequence in the arm on that side, and explain mechanistically why this complication occurs (lymphedema).",
            "A patient is taking corticosteroids long-term and develops infections easily. Explain mechanistically how corticosteroids suppress the innate immune response (consider phagocyte activity, inflammation, fever response).",
            "Compare innate and adaptive immunity in one paragraph: speed of response, specificity, memory, and which cells are involved. Why does the body need BOTH systems?",
        ],
    },
    {
        "filename": "workbook_day26_adaptive-immunity.html",
        "title": "Adaptive Immunity",
        "subhead": "B cells, T cells, antibodies, antigen presentation, memory.",
        "eyebrow": "BIO 304 . WEEK 7 . TUESDAY . LAB WORKBOOK",
        "day_num": 26,
        "anatomy_intro": (
            "Adaptive immunity is specific (recognizes a particular pathogen) "
            "and has memory (responds faster on second exposure). Today "
            "you'll draw the two main effector cell types side by side, "
            "then an antibody up close."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. B cell vs T cell action",
                "instructions": [
                    "Left half: a B cell encountering a free-floating antigen (e.g., a bacterial toxin). Draw the antigen binding the B cell receptor on the surface. Show the B cell differentiating into a plasma cell (label, with rough ER for antibody synthesis) and a memory B cell. Draw antibodies leaving the plasma cell into the surroundings.",
                    "Right half: a cytotoxic T cell (CD8) encountering an infected host cell. The infected cell presents a viral antigen on its surface bound to MHC class I (draw both). The T cell's T-cell receptor (TCR) binds the MHC-I + antigen complex. The T cell releases perforin and granzymes, punching the infected cell and triggering apoptosis. Draw the infected cell dying.",
                    "Label B cell, plasma cell, memory B cell, antibody on the left. Label cytotoxic T cell, TCR, MHC I, perforin/granzyme, apoptosis on the right.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Antibody structure",
                "instructions": [
                    "Draw a single antibody molecule as a Y shape.",
                    "Show four protein chains: two heavy chains (long) forming the stem and inner arms of the Y, two light chains (short) on the outer arms. Label.",
                    "Draw disulfide bonds (small dashes) connecting the chains.",
                    "Color or shade the TOPS of the two arms differently from the rest: these are the variable regions where antigen binding happens. Label antigen-binding site (two per antibody).",
                    "The rest of the molecule is the constant region. Label.",
                    "Below the antibody, draw a small antigen with surface features (epitopes) that fit the antigen-binding sites. Show the antibody-antigen binding.",
                ],
                "height": 360,
            },
        ],
        "label_list": [
            "B cell", "Plasma cell", "Memory B cell",
            "B cell receptor", "Antibody",
            "Cytotoxic T cell (CD8)", "Helper T cell (CD4)",
            "T cell receptor (TCR)", "MHC class I", "MHC class II",
            "Perforin", "Granzyme", "Apoptosis",
            "Heavy chain", "Light chain",
            "Variable region", "Constant region",
            "Antigen-binding site", "Antigen (epitope)",
        ],
        "physio_activity_title": "2A. Primary vs secondary immune response",
        "physio_activity_intro": (
            "Draw a graph (x-axis = time in days, y-axis = antibody "
            "concentration in blood) showing the primary vs secondary "
            "antibody response. On Day 0, the patient is exposed to "
            "antigen X. On Day 30, exposed again. Then answer the "
            "questions."
        ),
        "physio_activity_rows": 6,
        "synthesis_questions": [
            "Explain how a vaccine works using the primary vs secondary response. Why does a vaccine produce immunity even though no real infection ever occurred?",
            "HIV preferentially infects and destroys helper T cells (CD4). Predict the consequences for both the B cell response and the cytotoxic T cell response, and explain why HIV patients eventually develop opportunistic infections (AIDS).",
            "Autoimmune disease occurs when adaptive immunity targets self tissues. Pick one autoimmune disease (e.g., Type 1 diabetes, rheumatoid arthritis, lupus, multiple sclerosis). Identify which self tissue is targeted and predict the consequences when adaptive immunity attacks that tissue.",
        ],
    },
    {
        "filename": "workbook_day27_respiratory-anatomy-and-mechanics.html",
        "title": "Respiratory Anatomy and Mechanics",
        "subhead": "Upper and lower airways, alveoli, and how the chest moves air.",
        "eyebrow": "BIO 304 . WEEK 7 . THURSDAY . LAB WORKBOOK",
        "day_num": 27,
        "anatomy_intro": (
            "Air follows a specific path from nose to alveolus. The "
            "chest pulls air in and pushes it out by changing its own "
            "volume. Today you'll draw the respiratory tract from above, "
            "then a side view showing inspiration vs expiration."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Respiratory tract from nose to alveoli",
                "instructions": [
                    "Draw a head and chest in front view.",
                    "Label, in order from top to bottom: nasal cavity, pharynx, larynx, trachea, primary bronchi (right and left), secondary bronchi, tertiary bronchi, bronchioles, terminal bronchioles, respiratory bronchioles, alveolar ducts, alveoli.",
                    "At the bottom, draw a cluster of grape-like alveoli wrapped in capillaries.",
                    "Note: conducting zone = nose through terminal bronchioles (no gas exchange, just airflow). Respiratory zone = respiratory bronchioles through alveoli (gas exchange happens here).",
                    "Add the epiglottis at the top of the larynx (closes during swallowing).",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Inspiration vs expiration",
                "instructions": [
                    "Draw two side views of the thorax side by side.",
                    "LEFT silhouette: inspiration. Diaphragm contracts and flattens (moves DOWN). External intercostals contract, lifting the rib cage UP and OUT. Thoracic volume INCREASES, pressure DROPS, air flows IN.",
                    "RIGHT silhouette: expiration (quiet). Diaphragm relaxes and domes upward. Rib cage drops. Thoracic volume DECREASES, pressure RISES, air flows OUT.",
                    "Label diaphragm position, external intercostals, ribs, lung volume change, airflow direction.",
                    "Below the silhouettes, write Boyle's Law: at constant temperature, pressure and volume are inversely related. Note that inspiration is an ACTIVE process (muscle contraction); quiet expiration is PASSIVE (elastic recoil).",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Nasal cavity", "Pharynx", "Larynx", "Epiglottis", "Trachea",
            "Primary bronchus", "Bronchioles", "Terminal bronchiole",
            "Respiratory bronchiole", "Alveolar duct", "Alveolus",
            "Conducting zone", "Respiratory zone",
            "Diaphragm", "External intercostal muscles",
            "Visceral pleura", "Parietal pleura", "Pleural cavity",
        ],
        "physio_activity_title": "2A. Lung volumes and capacities",
        "physio_activity_intro": (
            "Sketch a single spirometry tracing (volume vs time) on the "
            "lines below. Then label the four primary volumes and the "
            "four derived capacities."
        ),
        "physio_numbered_qs": [
            "Tidal volume (TV): the volume of air moved in a single normal quiet breath. Typical value?",
            "Inspiratory reserve volume (IRV): the extra air you can breathe IN above a normal inspiration.",
            "Expiratory reserve volume (ERV): the extra air you can breathe OUT below a normal expiration.",
            "Residual volume (RV): the air remaining in the lungs after maximum expiration. Why is some always left?",
            "Vital capacity (VC = TV + IRV + ERV): the largest volume you can move from a maximum inspiration to a maximum expiration.",
            "Total lung capacity (TLC = VC + RV): everything the lungs can hold.",
        ],
        "synthesis_questions": [
            "A patient has a pneumothorax (air enters the pleural cavity, breaking the seal between visceral and parietal pleura). Predict what happens to the affected lung and explain mechanistically why it collapses.",
            "Compare obstructive (e.g., COPD, asthma) vs restrictive (e.g., pulmonary fibrosis) lung disease. Predict how each affects lung volumes (TV, IRV, FEV1, TLC) and explain the mechanical reason behind each pattern.",
            "Surfactant is a lipid-protein mixture in the alveoli that reduces surface tension. Premature infants often lack adequate surfactant (respiratory distress syndrome). Predict the consequence for alveolar inflation and explain why this is life-threatening.",
        ],
    },
    {
        "filename": "workbook_day27_gas-exchange-and-transport.html",
        "title": "Gas Exchange and Transport",
        "subhead": "External and internal respiration; how O2 and CO2 ride the bloodstream.",
        "eyebrow": "BIO 304 . WEEK 7 . THURSDAY . LAB WORKBOOK",
        "day_num": 27,
        "anatomy_intro": (
            "Gas exchange happens twice in every breath cycle: at the "
            "alveoli (external respiration, lungs pick up O2 and drop "
            "CO2) and at the tissues (internal respiration, tissues "
            "pick up O2 and dump CO2). Draw both interfaces and how "
            "hemoglobin transports the load."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Alveolus and tissue gas exchange",
                "instructions": [
                    "Draw two panels side by side: the alveolus (LEFT) and a body tissue (RIGHT).",
                    "Left panel: an alveolus with air inside. PO2 in alveolus is about 104 mmHg, PCO2 is about 40 mmHg. Wrap the alveolus with a pulmonary capillary. Blood entering the capillary has PO2 about 40, PCO2 about 45. Show O2 diffusing INTO the blood and CO2 diffusing OUT to the alveolus. By the time blood leaves, PO2 is ~100 and PCO2 is ~40.",
                    "Right panel: a tissue cell. Inside the cell, PO2 is about 40 and PCO2 is about 45 (because the cell is consuming O2 and making CO2). Wrap the tissue with a systemic capillary. Blood entering has PO2 ~100, PCO2 ~40. Show O2 diffusing INTO the tissue and CO2 diffusing OUT to the blood. By the time blood leaves, PO2 is ~40, PCO2 is ~45.",
                    "Add labels: external respiration (lungs), internal respiration (tissues). Note: diffusion goes down partial pressure gradients.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Hemoglobin transports O2",
                "instructions": [
                    "Draw a hemoglobin molecule schematically: four globin chains (subunits) clustered, each containing a heme group with a central iron (Fe). Label one heme.",
                    "Show the hemoglobin in two states: deoxyhemoglobin (no O2 bound) and oxyhemoglobin (4 O2 molecules bound, one per heme).",
                    "Draw a hemoglobin LOADING in the pulmonary capillary (high PO2): O2 binds.",
                    "Draw a hemoglobin UNLOADING in a tissue capillary (low PO2): O2 dissociates.",
                    "Note: hemoglobin shows cooperative binding (first O2 makes the next easier to bind), producing the S-shaped saturation curve.",
                    "Below, note three factors that promote unloading: low pH, high PCO2, high temperature (the Bohr effect). These are all features of active tissue.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Alveolus", "Pulmonary capillary",
            "PO2 (high in alveolus, low in tissue)",
            "PCO2 (low in alveolus, high in tissue)",
            "External respiration", "Internal respiration",
            "Hemoglobin", "Globin chain", "Heme group", "Iron (Fe)",
            "Oxyhemoglobin", "Deoxyhemoglobin",
            "Bohr effect",
        ],
        "physio_activity_title": "2A. Oxygen-hemoglobin dissociation curve",
        "physio_activity_intro": (
            "Sketch the oxygen-hemoglobin dissociation curve on a graph. "
            "x-axis: PO2 (0 to 100 mmHg). y-axis: percent hemoglobin "
            "saturation (0 to 100). Then answer the questions below."
        ),
        "physio_numbered_qs": [
            "At PO2 = 100 mmHg (lung capillary), what is hemoglobin saturation?",
            "At PO2 = 40 mmHg (tissue capillary at rest), what is saturation?",
            "Why is the curve S-shaped (sigmoidal) rather than linear?",
            "Predict the direction the curve SHIFTS when blood pH drops, PCO2 rises, or temperature rises. What does the shift accomplish at the tissue?",
            "A patient is given high-FiO2 oxygen therapy, raising arterial PO2 from 100 to 200 mmHg. Predict the change in hemoglobin saturation (it doesn't double).",
        ],
        "synthesis_questions": [
            "Carbon monoxide (CO) binds hemoglobin with about 200 times the affinity of O2 and forms carboxyhemoglobin. Predict the effects on (a) hemoglobin saturation, (b) the dissociation curve, (c) O2 delivery to tissues. Why is CO poisoning so dangerous even at low concentrations?",
            "Most CO2 in the blood is transported as bicarbonate (HCO3-), formed inside red blood cells by carbonic anhydrase. Trace this pathway: CO2 enters the RBC, becomes carbonic acid, then dissociates. Where does the H+ go, and where does HCO3- go?",
            "An athlete in heavy exercise has muscle PCO2 high, pH low, and temperature elevated. Predict (using the Bohr effect) what happens to hemoglobin's affinity for O2 at the muscle, and why this is exactly what the muscle needs.",
        ],
    },
    {
        "filename": "workbook_day28_gi-tract-anatomy-and-motility.html",
        "title": "GI Tract Anatomy and Motility",
        "subhead": "Mouth to anus, plus the accessory organs that empty into the tract.",
        "eyebrow": "BIO 304 . WEEK 7 . FRIDAY . LAB WORKBOOK",
        "day_num": 28,
        "anatomy_intro": (
            "The GI tract is a tube from mouth to anus. Food and chyme "
            "move through it by two main mechanisms: peristalsis "
            "(propulsion) and segmentation (mixing). Today you'll draw "
            "the GI tract with accessory organs, then the wall layers "
            "common to most segments."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. GI tract with accessory organs",
                "instructions": [
                    "Draw a body outline (head and torso).",
                    "Label, in order, the tube of the GI tract: mouth (oral cavity), pharynx, esophagus, stomach (J-shaped, in the upper left abdomen), small intestine (long coiled tube with 3 parts: duodenum, jejunum, ileum), large intestine (frames around the small intestine: cecum/appendix, ascending colon, transverse colon, descending colon, sigmoid colon, rectum), anus.",
                    "Now add accessory organs (they don't carry food but contribute to digestion): salivary glands near the mouth, liver in the upper right abdomen, gallbladder under the liver, pancreas behind the stomach.",
                    "Show ducts: bile duct from liver and gallbladder, pancreatic duct from pancreas, both emptying into the duodenum.",
                    "Label every structure.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. GI wall layers (cross-section)",
                "instructions": [
                    "Draw a cross-section of a typical GI tube (e.g., small intestine). Show the lumen in the center.",
                    "From the lumen outward, label four layers:",
                    "Mucosa (innermost): epithelium + lamina propria + muscularis mucosae. This is the absorptive surface; in the small intestine, show villi projecting into the lumen.",
                    "Submucosa: connective tissue with blood vessels and the submucosal nerve plexus. Label.",
                    "Muscularis externa: usually two layers of smooth muscle, an inner circular and an outer longitudinal. Between them runs the myenteric nerve plexus. These layers produce peristalsis and segmentation. Label.",
                    "Serosa (outermost): thin layer of mesothelium and connective tissue (the visceral peritoneum). Label.",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Oral cavity", "Pharynx", "Esophagus", "Stomach",
            "Duodenum", "Jejunum", "Ileum", "Cecum", "Appendix",
            "Ascending colon", "Transverse colon", "Descending colon",
            "Sigmoid colon", "Rectum", "Anus",
            "Salivary glands", "Liver", "Gallbladder", "Pancreas",
            "Bile duct", "Pancreatic duct",
            "Mucosa", "Submucosa", "Muscularis externa", "Serosa",
            "Circular muscle layer", "Longitudinal muscle layer",
        ],
        "physio_activity_title": "2A. Peristalsis vs segmentation",
        "physio_activity_intro": (
            "Compare the two main GI motility patterns by filling in the "
            "table. Then answer the follow-up questions."
        ),
        "physio_table": {
            "headers": ["Property", "Peristalsis", "Segmentation"],
            "rows": [
                ["Primary function (propulsion / mixing)", "", ""],
                ["Direction of movement", "", ""],
                ["Where dominant in GI tract", "", ""],
                ["Muscle layers involved", "", ""],
                ["Wave pattern", "", ""],
            ],
        },
        "physio_followups": [
            "Trace a bite of food from the moment it enters the mouth to the moment chyme leaves the stomach. Identify which motility patterns dominate at each step and approximately how long each stage takes.",
            "Defecation is a complex motor act involving both involuntary smooth muscle (internal anal sphincter) and voluntary skeletal muscle (external anal sphincter). Explain why a patient with a high spinal cord injury loses voluntary control but may still defecate reflexively.",
        ],
        "synthesis_questions": [
            "Dysphagia (difficulty swallowing) can result from problems with the pharynx, the esophagus, or the lower esophageal sphincter. Predict the symptoms in each case, and which patient population is most affected by each.",
            "Gastroparesis (delayed gastric emptying) is a common complication of diabetes. Predict the patient's symptoms after a meal and explain why dampened autonomic input to the stomach reduces its motility.",
            "Irritable bowel syndrome (IBS) is characterized by altered motility, often producing either diarrhea (too fast) or constipation (too slow). Predict what changes in segmentation and peristalsis would produce each pattern.",
        ],
    },
    {
        "filename": "workbook_day28_digestion-and-absorption.html",
        "title": "Digestion and Absorption",
        "subhead": "What breaks down where, and how nutrients cross into the blood.",
        "eyebrow": "BIO 304 . WEEK 7 . FRIDAY . LAB WORKBOOK",
        "day_num": 28,
        "anatomy_intro": (
            "Digestion happens stepwise: mechanical and chemical. "
            "Absorption is largely the job of the small intestine, whose "
            "villi enormously expand surface area. Today you'll draw a "
            "villus close-up, then the macronutrient digestion pathways."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Intestinal villus close-up",
                "instructions": [
                    "Draw a single intestinal villus: a finger-like projection into the lumen.",
                    "Label the lumen at the top.",
                    "Show the villus surface lined by absorptive epithelial cells (enterocytes), each with microvilli (brush border) facing the lumen. Label both.",
                    "Inside the villus, draw a network of blood capillaries (label) and one central lacteal (a lymphatic capillary running up the center). Label.",
                    "Add a goblet cell (mucus-secreting) in the epithelium. Label.",
                    "Note the principle: water-soluble nutrients (amino acids, monosaccharides) enter the blood capillaries; fat-soluble nutrients (chylomicrons, fatty acids in lipid form) enter the lacteals and travel via lymph.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. Macronutrient digestion pathways",
                "instructions": [
                    "Draw three parallel pathways: Carbohydrates, Proteins, Fats. Each pathway shows where digestion begins, where it continues, and what the final absorbed product is.",
                    "Carbohydrates: starch (mouth, salivary amylase begins) > starch (stomach, no digestion) > maltose (small intestine, pancreatic amylase) > glucose (small intestine, brush-border enzymes like maltase). Absorbed: monosaccharides into blood.",
                    "Proteins: protein (mouth, no digestion) > peptides (stomach, pepsin) > shorter peptides (small intestine, pancreatic proteases) > amino acids (small intestine, brush-border peptidases). Absorbed: amino acids into blood.",
                    "Fats: triglycerides (mouth, no digestion) > triglycerides (stomach, minor lingual lipase) > emulsified fat droplets (small intestine, bile salts from gallbladder) > monoglycerides + fatty acids (small intestine, pancreatic lipase). Absorbed: re-formed triglycerides as chylomicrons into lacteal.",
                    "Label each enzyme, its source (which organ), and the products at each step.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Villus", "Microvilli (brush border)", "Enterocyte",
            "Goblet cell", "Lumen", "Blood capillary", "Lacteal",
            "Salivary amylase", "Pepsin", "Pancreatic amylase",
            "Pancreatic protease (trypsin)", "Pancreatic lipase",
            "Brush-border enzymes", "Bile salts",
            "Glucose", "Amino acid", "Fatty acid + monoglyceride",
            "Chylomicron",
        ],
        "physio_activity_title": "2A. Enzyme, source, substrate, product",
        "physio_activity_intro": (
            "Fill in the table to map each major digestive enzyme."
        ),
        "physio_table": {
            "headers": ["Enzyme", "Source organ", "Substrate", "Product"],
            "rows": [
                ["Salivary amylase", "", "", ""],
                ["Pepsin", "", "", ""],
                ["Pancreatic amylase", "", "", ""],
                ["Trypsin (and other pancreatic proteases)", "", "", ""],
                ["Pancreatic lipase", "", "", ""],
                ["Maltase (brush border)", "", "", ""],
                ["Lactase (brush border)", "", "", ""],
            ],
        },
        "physio_followups": [
            "Lactose intolerance is caused by deficiency of the brush-border enzyme lactase. Predict the patient's symptoms after consuming dairy, and explain why undigested lactose causes osmotic diarrhea and bacterial gas production.",
            "Bile salts are NOT enzymes, yet they are essential for fat digestion. Explain mechanistically how bile salts contribute to fat digestion without breaking any chemical bonds themselves (think: emulsification).",
        ],
        "synthesis_questions": [
            "Celiac disease is an autoimmune reaction to gluten that damages and flattens intestinal villi. Predict the consequences for nutrient absorption and the patient's symptoms (weight loss, anemia, fatigue, diarrhea).",
            "A patient has their gallbladder removed (cholecystectomy). Predict the effect on fat digestion immediately after surgery and over the long term. Why can the patient still digest fats, just less efficiently?",
            "Pancreatic insufficiency (e.g., from cystic fibrosis or chronic pancreatitis) leads to malabsorption of all three macronutrients, but fat malabsorption is most pronounced. Explain mechanistically why fat absorption is hit hardest.",
        ],
    },

    # ==================================================================
    # WEEK 8
    # ==================================================================
    {
        "filename": "workbook_day29_kidney-anatomy-and-glomerular-filtration.html",
        "title": "Kidney Anatomy and Glomerular Filtration",
        "subhead": "Gross kidney structure, the nephron, and how filtration starts.",
        "eyebrow": "BIO 304 . WEEK 8 . MONDAY . LAB WORKBOOK",
        "day_num": 29,
        "anatomy_intro": (
            "The kidney is built of about a million tiny functional units "
            "called nephrons. Each nephron starts by filtering blood at "
            "the glomerulus. Today you'll draw the kidney from outside "
            "in and one nephron in detail."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Kidney in coronal section + nephron schematic",
                "instructions": [
                    "Left half: draw a kidney cut in half (coronal section, kidney bean shape).",
                    "Label the outer cortex (granular, lighter), then the inner medulla containing several renal pyramids (cone-shaped). Tip of each pyramid (renal papilla) points into a minor calyx. Minor calyces converge into major calyces, which empty into the renal pelvis, which empties into the ureter. Label every structure.",
                    "Add the renal artery (entering) and renal vein (leaving) at the hilum.",
                    "Right half: draw a single nephron schematic. Start with the glomerulus inside Bowman's capsule (in the cortex). Continue through the proximal convoluted tubule (PCT, in cortex), down into the loop of Henle (which dips into the medulla, with a thin descending limb and a thick ascending limb), then back up to the distal convoluted tubule (DCT, in cortex), and finally into the collecting duct (which descends through the medulla and empties into the renal papilla).",
                    "Label every nephron segment.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. Glomerulus and Bowman's capsule close-up",
                "instructions": [
                    "Draw the glomerulus as a tuft of capillaries enclosed inside Bowman's capsule (a cup-like structure).",
                    "Show the afferent arteriole (larger diameter) entering the glomerulus, and the efferent arteriole (smaller diameter) leaving the glomerulus. Label both.",
                    "Note: the difference in arteriole diameters creates high pressure inside the glomerular capillaries, which is what drives filtration.",
                    "Draw the filtration barrier: capillary endothelial cells (with pores), the glomerular basement membrane (negatively charged, blocks proteins), and the podocyte foot processes (forming filtration slits). Label all three.",
                    "Show filtered fluid (filtrate) passing into Bowman's space and then into the PCT.",
                    "Note: filtrate contains water, ions, glucose, amino acids, urea (small things). It excludes RBCs, WBCs, platelets, and large proteins (these stay in the blood).",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Renal cortex", "Renal medulla", "Renal pyramid", "Renal papilla",
            "Minor calyx", "Major calyx", "Renal pelvis", "Ureter",
            "Renal artery", "Renal vein", "Hilum",
            "Glomerulus", "Bowman's capsule", "Bowman's space",
            "Afferent arteriole", "Efferent arteriole",
            "Proximal convoluted tubule (PCT)", "Loop of Henle",
            "Distal convoluted tubule (DCT)", "Collecting duct",
            "Podocyte", "Glomerular basement membrane",
        ],
        "physio_activity_title": "2A. Filtration rules: in or out of the filtrate?",
        "physio_activity_intro": (
            "For each substance below, decide whether it is FILTERED (passes "
            "into Bowman's space at the glomerulus) or NOT FILTERED. "
            "Justify in one phrase based on size or charge."
        ),
        "physio_numbered_qs": [
            "Water (H2O).",
            "Sodium ions (Na+).",
            "Glucose.",
            "Urea.",
            "Red blood cells.",
            "Albumin (a small plasma protein, ~67 kDa, negatively charged).",
            "Creatinine (a small molecule, freely filtered, used clinically to estimate GFR).",
        ],
        "synthesis_questions": [
            "Calculate cardiac output to kidney perfusion: at rest, the kidneys receive about 20 to 25 percent of cardiac output. If CO is 5 L/min, what is renal blood flow? Why is the kidney so heavily perfused?",
            "Predict what happens to glomerular filtration rate (GFR) if (a) the afferent arteriole constricts, (b) the efferent arteriole constricts. Explain using the pressure-gradient concept.",
            "A patient with severe hypertension develops kidney damage over years. Predict how chronic high pressure damages the delicate glomerular structures, and explain why proteinuria (protein in the urine) is a hallmark of this damage.",
        ],
    },
    {
        "filename": "workbook_day30_tubular-function-and-urine-concentration.html",
        "title": "Tubular Function and Urine Concentration",
        "subhead": "Reabsorption, secretion, and how the kidney makes concentrated urine.",
        "eyebrow": "BIO 304 . WEEK 8 . TUESDAY . LAB WORKBOOK",
        "day_num": 30,
        "anatomy_intro": (
            "About 180 L of filtrate is produced every day, but only "
            "1 to 2 L of urine leaves the body. The nephron tubules "
            "reclaim everything useful and concentrate the rest. Today "
            "you'll annotate each tubule segment and then draw the "
            "medullary osmotic gradient."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Nephron with segment functions",
                "instructions": [
                    "Draw a nephron in the same orientation as Day 29: glomerulus, PCT (in cortex), loop of Henle (descending and ascending limbs going into medulla), DCT (back in cortex), collecting duct (going down through medulla to papilla).",
                    "Beside each segment, write what is REABSORBED (into blood) and what is SECRETED (into filtrate).",
                    "PCT: ~65 percent of water and Na+, all glucose and amino acids (via co-transport), bicarbonate (HCO3-). Reclaims most filtered nutrients.",
                    "Loop of Henle, descending limb: water reabsorbed (permeable to water, not solute). Loop of Henle, ascending thick limb: Na+ and Cl- reabsorbed (not permeable to water). This creates the medullary gradient.",
                    "DCT: fine-tuning. Na+ reabsorbed (aldosterone-regulated), Ca2+ reabsorbed (PTH-regulated), K+ secreted.",
                    "Collecting duct: water reabsorption controlled by ADH (vasopressin). Urea reabsorbed in deep medulla.",
                    "Label each segment and its key activity.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. Medullary osmotic gradient",
                "instructions": [
                    "Draw the kidney section showing cortex at top and deep medulla at bottom.",
                    "Mark interstitial osmolarity at different depths: 300 mOsm/L at cortex (same as plasma), rising to about 1200 mOsm/L deep in the medulla.",
                    "Show how the loop of Henle creates this gradient (countercurrent multiplier).",
                    "Now show two scenarios for the collecting duct passing through this gradient:",
                    "ADH ABSENT (diabetes insipidus or overhydration): collecting duct is impermeable to water; urine stays dilute (about 50 to 100 mOsm/L); large urine volume.",
                    "ADH PRESENT (dehydration or normal): aquaporins inserted in collecting duct; water leaves to enter the concentrated medullary interstitium; urine becomes concentrated (up to 1200 mOsm/L); small urine volume.",
                    "Note: the medullary gradient is what makes concentrated urine POSSIBLE; ADH controls whether the body USES it.",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Proximal convoluted tubule (PCT)", "Loop of Henle",
            "Descending limb", "Ascending thick limb",
            "Distal convoluted tubule (DCT)", "Collecting duct",
            "Reabsorption", "Secretion",
            "Aldosterone", "ADH (vasopressin)", "Parathyroid hormone (PTH)",
            "Aquaporin (water channel)",
            "Medullary osmotic gradient",
            "Countercurrent multiplier",
        ],
        "physio_activity_title": "2A. Trace one molecule of filtered glucose",
        "physio_activity_intro": (
            "A glucose molecule has just entered Bowman's space at the "
            "glomerulus. Trace what happens to it segment by segment in "
            "a healthy person. Then in someone with diabetes mellitus "
            "and blood glucose of 350 mg/dL."
        ),
        "physio_activity_rows": 8,
        "synthesis_questions": [
            "A patient with diabetes mellitus has blood glucose of 350 mg/dL (well above the renal threshold of ~200). Predict the urine composition and explain why these patients experience polyuria (excessive urine) and polydipsia (excessive thirst).",
            "A patient takes a loop diuretic (e.g., furosemide), which blocks Na+/K+/2Cl- reabsorption in the thick ascending limb. Predict the immediate effects on (a) the medullary gradient, (b) urine volume, (c) serum potassium, and (d) blood pressure. Why is this drug used to treat heart failure?",
            "SIADH (syndrome of inappropriate ADH) causes ADH release even when blood is dilute. Predict the urine osmolarity, blood sodium, and the patient's symptoms. Why is excess water retention more dangerous than excess water loss in terms of brain function?",
        ],
    },
    {
        "filename": "workbook_day31_fluid-electrolyte-and-acid-base-balance.html",
        "title": "Fluid, Electrolyte, and Acid-Base Balance",
        "subhead": "Body water compartments, key electrolytes, and how the body keeps pH at 7.4.",
        "eyebrow": "BIO 304 . WEEK 8 . THURSDAY . LAB WORKBOOK",
        "day_num": 31,
        "anatomy_intro": (
            "Body water is split between intracellular and extracellular "
            "compartments, each with its own electrolyte signature. "
            "Blood pH is maintained near 7.4 by buffers, the lungs, and "
            "the kidneys. Today you'll draw the compartments, then the "
            "compensatory pathways."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Body fluid compartments",
                "instructions": [
                    "Draw a person silhouette. Show total body water as about 60 percent of body weight.",
                    "Divide total body water into two compartments:",
                    "Intracellular fluid (ICF): about 40 percent of body weight, or about 2/3 of total body water. Inside the body's cells. Dominant ions: K+ (high), phosphate (high), proteins (high). Label.",
                    "Extracellular fluid (ECF): about 20 percent of body weight, or about 1/3 of total body water. Subdivide ECF into: plasma (about 1/4 of ECF, inside blood vessels) and interstitial fluid (about 3/4 of ECF, between cells in tissues). Dominant ions in ECF: Na+ (high), Cl- (high), HCO3-.",
                    "Mark the cell membrane separating ICF from ECF, and the capillary endothelium separating plasma from interstitial fluid.",
                    "Note: the Na+/K+ ATPase is what maintains the K+-rich inside and Na+-rich outside.",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Acid-base regulation: lungs and kidneys",
                "instructions": [
                    "Write the central equation at the top: CO2 + H2O <-> H2CO3 <-> H+ + HCO3-. Note: carbonic anhydrase catalyzes the first step.",
                    "Show the LUNGS adjusting CO2: increased ventilation blows off more CO2 (shifts the equation LEFT, removing H+, raising pH). Decreased ventilation retains CO2 (shifts RIGHT, raising H+, lowering pH). Label respiratory compensation.",
                    "Show the KIDNEYS adjusting HCO3- and H+: the kidney can reabsorb HCO3- to raise pH, or excrete H+ into urine to raise pH. Conversely, it can excrete HCO3- and retain H+ to lower pH. Label renal compensation.",
                    "Note the time courses: respiratory compensation is FAST (minutes). Renal compensation is SLOW (days).",
                ],
                "height": 380,
            },
        ],
        "label_list": [
            "Total body water (~60% body weight)",
            "Intracellular fluid (ICF)",
            "Extracellular fluid (ECF)",
            "Plasma", "Interstitial fluid",
            "Na+ (high ECF)", "K+ (high ICF)",
            "HCO3- (bicarbonate)", "H2CO3 (carbonic acid)",
            "Carbonic anhydrase",
            "Respiratory compensation", "Renal compensation",
        ],
        "physio_activity_title": "2A. Acid-base disorders",
        "physio_activity_intro": (
            "For each clinical scenario, identify (a) the primary acid-base "
            "disorder (respiratory acidosis, respiratory alkalosis, "
            "metabolic acidosis, or metabolic alkalosis), and (b) the "
            "expected compensation by the OTHER system."
        ),
        "physio_numbered_qs": [
            "A patient with severe COPD retains CO2 chronically.",
            "An anxious patient hyperventilates after a panic attack.",
            "A diabetic patient in DKA produces ketoacids faster than the kidneys can clear them.",
            "A patient vomits repeatedly for 24 hours, losing large amounts of HCl from the stomach.",
            "A patient with a heroin overdose has slow, shallow breathing (hypoventilation).",
            "A patient at high altitude (low atmospheric O2) hyperventilates to maximize oxygen uptake.",
        ],
        "synthesis_questions": [
            "An ABG (arterial blood gas) shows pH 7.25, PCO2 60 mmHg, HCO3- 28 mEq/L. Identify the disorder and the expected compensation. What clinical condition might produce this picture?",
            "A patient is severely dehydrated from diarrhea. Predict the effects on (a) total body water compartments, (b) serum Na+, (c) blood pressure, (d) the kidney's response (ADH, aldosterone). What IV fluid would you give and why?",
            "Hyperkalemia (high serum K+) is life-threatening because it depolarizes excitable cells. Explain mechanistically why elevated extracellular K+ depolarizes cells, and predict the consequence for cardiac action potentials.",
        ],
    },
    {
        "filename": "workbook_day31_male-reproductive-system.html",
        "title": "Male Reproductive System",
        "subhead": "Testes, accessory glands, spermatogenesis, and hormonal control.",
        "eyebrow": "BIO 304 . WEEK 8 . THURSDAY . LAB WORKBOOK",
        "day_num": 31,
        "anatomy_intro": (
            "The male reproductive system produces sperm in the testes, "
            "matures and stores them in the epididymis, and delivers "
            "them through a series of ducts with contributions from "
            "three accessory glands. Today you'll draw both the gross "
            "anatomy and a seminiferous tubule showing spermatogenesis."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Male reproductive system (sagittal section)",
                "instructions": [
                    "Draw a side view of the male pelvis.",
                    "Show the testis hanging in the scrotum (outside the body cavity to keep cooler).",
                    "Inside the testis, show coiled seminiferous tubules.",
                    "Outside the testis but attached to it, draw the epididymis (a tightly coiled tube on the posterior surface).",
                    "From the epididymis, draw the vas deferens (ductus deferens) ascending up out of the scrotum, looping behind the bladder.",
                    "Show three accessory glands: seminal vesicles (paired, posterior to bladder), prostate gland (encircling the urethra just below the bladder), bulbourethral (Cowper's) glands (small, below the prostate).",
                    "Show the ducts of the seminal vesicle joining the vas deferens to form the ejaculatory duct, which passes through the prostate and joins the urethra.",
                    "Finally, show the urethra exiting through the penis. Label.",
                ],
                "height": 480,
            },
            {
                "id": "B",
                "label": "Box B. Seminiferous tubule with spermatogenesis",
                "instructions": [
                    "Draw a cross-section of one seminiferous tubule (round shape with a lumen).",
                    "Show developing sperm cells in a progression from the OUTSIDE (basement membrane) to the INSIDE (lumen).",
                    "Outermost: spermatogonia (diploid stem cells, 2n). Label.",
                    "Inward: primary spermatocytes (2n, undergoing meiosis I). Label.",
                    "Further inward: secondary spermatocytes (haploid, n, after meiosis I). Label.",
                    "Closer to lumen: spermatids (n, after meiosis II). Label.",
                    "At the lumen edge: spermatozoa (mature sperm with head, midpiece, tail). Label.",
                    "Add Sertoli cells (sustentacular cells) reaching from the basement membrane to the lumen, supporting and nurturing developing sperm. Label.",
                    "Between tubules, add Leydig cells (interstitial cells) which produce testosterone. Label.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Testis", "Seminiferous tubule", "Epididymis",
            "Vas deferens (ductus deferens)", "Ejaculatory duct",
            "Seminal vesicle", "Prostate gland", "Bulbourethral gland",
            "Urethra", "Penis", "Scrotum",
            "Spermatogonium", "Primary spermatocyte",
            "Secondary spermatocyte", "Spermatid", "Spermatozoon",
            "Sertoli cell", "Leydig cell",
        ],
        "physio_activity_title": "2A. Trace a sperm cell from production to ejaculation",
        "physio_activity_intro": (
            "List the path a single sperm cell takes from the moment it "
            "is formed in the seminiferous tubule to the moment it "
            "leaves the body in semen. Aim for 7 to 9 steps."
        ),
        "physio_activity_rows": 9,
        "synthesis_questions": [
            "A vasectomy involves cutting and tying the vas deferens. Predict (a) whether sperm production continues, (b) whether ejaculation still occurs, (c) what is missing from the ejaculate. Why does the procedure not affect testosterone levels?",
            "Hypothalamic-pituitary-gonadal axis: GnRH releases LH and FSH, which act on the testis. LH stimulates Leydig cells (testosterone), FSH stimulates Sertoli cells (sperm maturation). Predict the effects of (a) anabolic steroid abuse, which raises external testosterone, on natural testosterone production and sperm count.",
            "Benign prostatic hyperplasia (BPH) is enlargement of the prostate, common in older men. Given the prostate's anatomical position (encircling the urethra), predict the patient's urinary symptoms and explain the mechanism.",
        ],
    },
    {
        "filename": "workbook_day32_female-reproductive-system.html",
        "title": "Female Reproductive System",
        "subhead": "Ovaries, uterus, the ovarian cycle, and hormonal control.",
        "eyebrow": "BIO 304 . WEEK 8 . FRIDAY . LAB WORKBOOK",
        "day_num": 32,
        "anatomy_intro": (
            "The female reproductive system is built around a monthly "
            "cycle that prepares both an egg and a uterus for possible "
            "fertilization and pregnancy. Today you'll draw the system "
            "in sagittal section, then the hormonal cycle that drives it."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Female reproductive system (sagittal section)",
                "instructions": [
                    "Draw a side view of the female pelvis.",
                    "Center the uterus (pear-shaped, anteverted, lying over the bladder).",
                    "On each side of the uterus, draw a fallopian tube (uterine tube, oviduct) extending laterally and curving toward an ovary. The end of each fallopian tube fans out into fimbriae over the ovary.",
                    "Below the uterus, draw the cervix (lower narrow portion of the uterus) and the vagina extending down to the vaginal opening.",
                    "Label uterus, fallopian tube, fimbriae, ovary, cervix, vagina.",
                    "Inside the uterus wall, label endometrium (inner lining, sheds during menstruation) and myometrium (thick smooth muscle layer).",
                ],
                "height": 460,
            },
            {
                "id": "B",
                "label": "Box B. Ovarian and menstrual cycle",
                "instructions": [
                    "Draw a horizontal timeline across 28 days. Mark Day 1 (start of menstruation) at the left and Day 28 at the right. Mark Day 14 as ovulation.",
                    "Above the timeline, draw the ovarian cycle: Follicular phase (Days 1-13), Ovulation (Day 14), Luteal phase (Days 15-28). Show: developing follicles (small to large) during the follicular phase, ovulation as a small explosion at Day 14, corpus luteum (yellow body) during the luteal phase.",
                    "Below the timeline, draw the uterine cycle: Menstrual phase (Days 1-5, endometrium sheds), Proliferative phase (Days 6-14, endometrium thickens), Secretory phase (Days 15-28, endometrium becomes vascular and gland-rich, ready for implantation).",
                    "Above everything, sketch four hormone curves: FSH (peaks early follicular), LH (sharp surge at Day 14 triggering ovulation), Estrogen (rises late follicular, secondary peak in luteal phase), Progesterone (low during follicular, rises in luteal phase after ovulation).",
                    "Note: if no pregnancy, the corpus luteum degenerates around Day 25-28, progesterone and estrogen drop, the endometrium sheds, and a new cycle begins.",
                ],
                "height": 460,
            },
        ],
        "label_list": [
            "Ovary", "Fallopian tube", "Fimbriae",
            "Uterus", "Endometrium", "Myometrium",
            "Cervix", "Vagina",
            "Follicular phase", "Ovulation", "Luteal phase",
            "Corpus luteum",
            "Menstrual phase", "Proliferative phase", "Secretory phase",
            "FSH", "LH", "Estrogen", "Progesterone",
        ],
        "physio_activity_title": "2A. Hormone-organ-action map",
        "physio_activity_intro": (
            "Fill in the table to map each hormone to its source, target, "
            "and main action during the cycle."
        ),
        "physio_table": {
            "headers": ["Hormone", "Source", "Target", "Main action"],
            "rows": [
                ["FSH", "", "", ""],
                ["LH", "", "", ""],
                ["Estrogen (early/follicular phase)", "", "", ""],
                ["LH (mid-cycle surge)", "", "", ""],
                ["Progesterone (luteal phase)", "", "", ""],
                ["Estrogen + progesterone (high level feedback)", "", "", ""],
            ],
        },
        "physio_followups": [
            "Hormonal contraceptives (e.g., combined estrogen + progestin pills) prevent ovulation. Explain mechanistically: which hormones do they mimic, and how does that prevent the LH surge?",
            "Menopause occurs when the ovaries stop responding to FSH and LH. Predict the changes in estrogen and progesterone, the FSH/LH levels (they go UP, due to loss of negative feedback), and explain why hot flashes and bone loss are common consequences.",
        ],
        "synthesis_questions": [
            "A patient is trying to conceive but has irregular ovulation. Predict the effect on her hormonal cycle and uterine lining, and explain why ovulation predictor kits (which detect LH) help with timing.",
            "Polycystic ovary syndrome (PCOS) involves elevated androgens, irregular ovulation, and insulin resistance. Predict the patient's menstrual pattern and fertility, and explain why follicles fail to mature properly.",
            "Ectopic pregnancy: a fertilized egg implants in the fallopian tube rather than the uterus. Predict the clinical course (early pregnancy symptoms followed by acute abdominal pain and bleeding) and explain mechanistically why the fallopian tube cannot support a growing embryo.",
        ],
    },
    {
        "filename": "workbook_day32_pregnancy-a-p-basics.html",
        "title": "Pregnancy A&P (Basics)",
        "subhead": "Fertilization, implantation, the placenta, and the major changes of pregnancy.",
        "eyebrow": "BIO 304 . WEEK 8 . FRIDAY . LAB WORKBOOK",
        "day_num": 32,
        "anatomy_intro": (
            "Pregnancy is an extraordinary integration of multiple "
            "physiological systems. Today you'll draw the early events "
            "(fertilization, cleavage, implantation), then the mature "
            "placenta as the maternal-fetal interface."
        ),
        "anatomy_panels": [
            {
                "id": "A",
                "label": "Box A. Fertilization to implantation",
                "instructions": [
                    "Draw a horizontal arrow with five labeled stages, left to right.",
                    "Stage 1: Fertilization. A sperm meets the egg in the upper fallopian tube. Draw both with the sperm head entering the egg cytoplasm. Result: zygote (2n).",
                    "Stage 2: Cleavage. Repeated cell divisions, no growth. Show a 2-cell, then 4-cell, then 8-cell embryo.",
                    "Stage 3: Morula. A solid ball of about 16 cells.",
                    "Stage 4: Blastocyst. A hollow ball with an inner cell mass (becomes embryo) and outer trophoblast (becomes placenta). Show a fluid-filled cavity inside.",
                    "Stage 5: Implantation. The blastocyst burrows into the endometrium of the uterus around Day 6 to 7 after fertilization. The trophoblast cells invade and begin forming the placenta.",
                    "Label every stage.",
                ],
                "height": 380,
            },
            {
                "id": "B",
                "label": "Box B. Mature placenta",
                "instructions": [
                    "Draw a cross-section of a mature placenta and the surrounding uterine wall.",
                    "Show maternal blood spaces (lacunae) in the placenta filled with maternal blood. Show the maternal arteries (spiral arteries) supplying these lacunae.",
                    "Show fetal villi projecting into the maternal blood spaces. The villi contain fetal capillaries.",
                    "Critical: maternal and fetal blood DO NOT MIX. They are separated by the placental barrier (trophoblast layer plus fetal capillary endothelium). Gases, nutrients, antibodies, drugs, and wastes diffuse across.",
                    "Show the umbilical cord leaving the placenta, containing two umbilical arteries (carrying deoxygenated blood FROM fetus TO placenta) and one umbilical vein (carrying oxygenated blood FROM placenta TO fetus). Label.",
                    "Note: this is the only place in the body where arteries carry deoxygenated blood and a vein carries oxygenated blood.",
                ],
                "height": 420,
            },
        ],
        "label_list": [
            "Zygote", "Cleavage", "Morula", "Blastocyst",
            "Inner cell mass", "Trophoblast",
            "Implantation", "Endometrium",
            "Placenta", "Maternal blood (lacuna)", "Spiral artery",
            "Fetal villus", "Fetal capillary",
            "Placental barrier",
            "Umbilical cord", "Umbilical artery (2)", "Umbilical vein (1)",
            "hCG", "Estrogen (placental)", "Progesterone (placental)",
        ],
        "physio_activity_title": "2A. Hormonal changes through pregnancy",
        "physio_activity_intro": (
            "Sketch a graph of major pregnancy hormones over 40 weeks "
            "(gestational age) on the lines below. Then answer the "
            "interpretation questions."
        ),
        "physio_numbered_qs": [
            "hCG (human chorionic gonadotropin): peaks at about 8 to 10 weeks, then declines. Source? Function?",
            "Progesterone: rises throughout pregnancy. Source shifts from corpus luteum to placenta around week 10. Function?",
            "Estrogen: rises steadily throughout pregnancy, made by the placenta. Function in the third trimester?",
            "Relaxin: produced by ovary and placenta; rises late in pregnancy. Function at parturition?",
            "Oxytocin: surges at parturition. Source? Mechanism (positive feedback during labor)?",
            "Prolactin: rises through pregnancy and after delivery. Function?",
        ],
        "synthesis_questions": [
            "Home pregnancy tests detect hCG in the urine. Explain why hCG is a reliable early marker, why it peaks at 8 to 10 weeks, and why levels in ectopic pregnancy or miscarriage are often lower than expected for gestational age.",
            "Gestational diabetes develops in some women because placental hormones (especially human placental lactogen) increase insulin resistance. Predict the maternal blood glucose pattern, the consequences for the fetus (macrosomia), and why blood sugar typically normalizes after delivery.",
            "Parturition (labor) involves a positive feedback loop with oxytocin. Identify the stimulus, the receptor, the response, and the amplifying step. Why is positive feedback (rather than negative feedback) the right architecture for this physiological event?",
        ],
    },
]


# ----------------------------------------------------------------------
# Template parts
# ----------------------------------------------------------------------

CSS = dedent("""
:root{
  --navy:#1E3D4C; --navy-deep:#142A36; --navy-tint:#EDF1F3;
  --gold:#B8924A; --gold-deep:#9A7838;
  --terra:#C2734D; --terra-dark:#A0522D;
  --white:#FFFFFF; --off-white:#FAFAF9;
  --gray-line:#CFD6DA; --gray-soft:#5C6970;
}
*{box-sizing:border-box}
body{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.55}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600;border-radius:0 0 6px 0}
.skip-link:focus{left:0}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
@media (prefers-reduced-motion: reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
header{background:var(--white);border-bottom:1px solid var(--gray-line);padding:24px 32px}
.eyebrow{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}
h1{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(22px,3vw,32px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}
.subhead{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);margin:0 0 8px}
.usage{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0}
main{max-width:880px;margin:0 auto;padding:24px}
.card{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:0 1px 3px rgba(0,0,0,.08);margin-bottom:18px}
.section-band{margin:24px 0 8px;padding:14px 18px;border-radius:8px;background:var(--white);border:1px solid var(--gray-line)}
.section-band.anatomy{border-left:6px solid var(--terra-dark)}
.section-band.physiology{border-left:6px solid var(--gold)}
.section-band p.tag{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 4px;color:var(--terra-dark)}
.section-band.physiology p.tag{color:var(--gold-deep)}
.section-band h2{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;color:var(--navy);font-size:22px;margin:0;letter-spacing:-.01em}
h2{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);font-size:18px;margin:0 0 10px}
h3{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--navy);font-size:15px;margin:14px 0 6px}
.draw-box{background:var(--white);border:2px dashed var(--navy);border-radius:8px;padding:18px;margin:10px 0 8px;display:flex;flex-direction:column;justify-content:flex-end}
.draw-box .draw-caption{font-family:'DM Sans',system-ui,sans-serif;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gray-soft);text-align:center;margin-top:auto}
.draw-instructions{background:var(--navy-tint);border-radius:6px;padding:14px 18px;margin:0 0 10px}
.draw-instructions h3{margin-top:0}
.draw-instructions ol{margin:6px 0 0;padding-left:22px}
.draw-instructions li{margin:6px 0}
ol.structure-list{font-family:'Lora',Georgia,serif;font-size:15px;line-height:1.9;padding-left:24px;columns:2;column-gap:28px}
ol.structure-list li{padding:4px 0;border-bottom:1px dotted var(--gray-line);break-inside:avoid}
ol.structure-list li:last-child{border-bottom:none}
.activity-prompt{margin:0 0 10px}
.write-lines{margin:8px 0 0;padding:0;list-style:none}
.write-lines li{border-bottom:1px solid var(--gray-line);min-height:34px;padding:4px 0 0;font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:13px;color:var(--gray-soft)}
.write-lines li:last-child{margin-bottom:0}
.write-lines li::before{content:attr(data-num) ".";font-weight:700;color:var(--navy);margin-right:8px}
.scrambled-list{background:var(--navy-tint);border-radius:6px;padding:12px 18px 12px 36px;margin:6px 0 14px}
.scrambled-list li{margin:6px 0}
.synthesis-q{border-left:3px solid var(--terra-dark);padding:6px 14px;margin:14px 0}
.synthesis-q strong{display:block;font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:var(--navy);margin-bottom:6px}
.answer-space{border-bottom:1px solid var(--gray-line);min-height:30px;margin-top:6px}
.answer-space + .answer-space{margin-top:24px}
table.physio-table{width:100%;border-collapse:collapse;margin:8px 0 12px;font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:14px}
table.physio-table th,table.physio-table td{border:1px solid var(--gray-line);padding:10px 8px;vertical-align:top;text-align:left}
table.physio-table th{background:var(--navy-tint);color:var(--navy);font-weight:700}
table.physio-table td{height:48px}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}
.btn{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:14px;padding:10px 18px;border-radius:6px;border:1px solid transparent;cursor:pointer;text-decoration:none;display:inline-block}
.btn-primary{background:var(--navy);color:var(--white);border-color:var(--navy)}
.btn-primary:hover{background:var(--navy-deep)}
.btn-ghost{background:transparent;color:var(--navy);border-color:var(--gray-line)}
.btn-ghost:hover{background:var(--navy-tint);border-color:var(--navy)}
footer{text-align:center;color:var(--gray-soft);padding:20px;font-style:italic;font-size:13px}
@media print{
  body{background:white;color:black}
  .no-print{display:none!important}
  .card{box-shadow:none;border-color:#888;page-break-inside:avoid}
  header{border-bottom:2px solid #333}
  .draw-box{border-color:#333;background:#fff}
  h1,h2,h3{color:black}
  .scrambled-list{background:#f5f5f5;border:1px solid #999}
  .draw-instructions{background:#f5f5f5;border:1px solid #999}
  ol.structure-list{columns:2}
}
""").strip()


# Iframe height sender plus target=_top safety (matches global rule)
SCRIPT = dedent("""
<script>
(function(){
  if(window.self===window.top)return;
  function sendHeight(){
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{window.parent.postMessage({type:'iframe-height',id:'bio304-workbook',height:h},'*');}catch(e){}
  }
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){new ResizeObserver(sendHeight).observe(document.body);}else{setInterval(sendHeight,800);}
})();
</script>
""").strip()


# ----------------------------------------------------------------------
# Renderers
# ----------------------------------------------------------------------

def render_draw_panel(panel):
    items = "\n".join(f"        <li>{escape(step)}</li>" for step in panel["instructions"])
    height = panel.get("height", 360)
    panel_id = f"draw-panel-{panel['id'].lower()}"
    return dedent(f"""
    <article class="card">
      <h2>{escape(panel['label'])}</h2>
      <div class="draw-instructions" role="region" aria-label="Drawing directions for {escape(panel['label'])}">
        <h3>Directions</h3>
        <ol>
{items}
        </ol>
      </div>
      <div class="draw-box" id="{panel_id}" role="img" aria-label="Blank drawing space for {escape(panel['label'])}" style="min-height:{height}px;">
        <p class="draw-caption">Draw here. Sketch by hand.</p>
      </div>
    </article>
    """).strip()


def render_label_list(items):
    rows = "\n".join(f"      <li>{escape(s)}</li>" for s in items)
    return dedent(f"""
    <article class="card">
      <h2>1C. Structures to label ({len(items)})</h2>
      <p class="usage">After you finish each drawing, label every structure below directly on your sketch.</p>
      <ol class="structure-list">
{rows}
      </ol>
    </article>
    """).strip()


def render_write_lines(n):
    lines = "\n".join(f'        <li data-num="{i+1}"></li>' for i in range(n))
    return dedent(f"""
      <ol class="write-lines">
{lines}
      </ol>
    """).strip()


def render_physio_section(wb):
    parts = [f'<h2>{escape(wb["physio_activity_title"])}</h2>',
             f'<p class="activity-prompt">{escape(wb["physio_activity_intro"])}</p>']

    if "physio_activity_rows" in wb:
        parts.append(render_write_lines(wb["physio_activity_rows"]))

    if "physio_table" in wb:
        t = wb["physio_table"]
        header_cells = "".join(f"<th>{escape(h)}</th>" for h in t["headers"])
        body_rows = []
        for row in t["rows"]:
            cells = "".join(
                f"<th scope='row'>{escape(c)}</th>" if i == 0 else f"<td>{escape(c)}</td>"
                for i, c in enumerate(row)
            )
            body_rows.append(f"<tr>{cells}</tr>")
        body = "\n".join(body_rows)
        parts.append(dedent(f"""
        <table class="physio-table">
          <thead><tr>{header_cells}</tr></thead>
          <tbody>
{body}
          </tbody>
        </table>
        """).strip())
        for q in wb.get("physio_followups", []):
            parts.append(f'<div class="synthesis-q"><strong>{escape(q)}</strong>'
                         f'<div class="answer-space"></div>'
                         f'<div class="answer-space"></div></div>')

    if "physio_scrambled_events" in wb:
        items = "\n".join(f"        <li>{escape(e)}</li>" for e in wb["physio_scrambled_events"])
        parts.append(dedent(f"""
        <p><strong>Scrambled events:</strong></p>
        <ol class="scrambled-list">
{items}
        </ol>
        <p><strong>Your sequence (write the events in correct order):</strong></p>
        """).strip())
        parts.append(render_write_lines(len(wb["physio_scrambled_events"])))

    if "physio_numbered_qs" in wb:
        for i, q in enumerate(wb["physio_numbered_qs"], 1):
            parts.append(f'<div class="synthesis-q"><strong>{i}. {escape(q)}</strong>'
                         f'<div class="answer-space"></div>'
                         f'<div class="answer-space"></div></div>')

    return '<article class="card">' + "\n".join(parts) + '</article>'


def render_synthesis(questions):
    qs = "\n".join(
        f'  <div class="synthesis-q"><strong>{i}. {escape(q)}</strong>'
        f'<div class="answer-space"></div>'
        f'<div class="answer-space"></div>'
        f'<div class="answer-space"></div></div>'
        for i, q in enumerate(questions, 1)
    )
    return dedent(f"""
    <article class="card">
      <h2>2B. Synthesis questions</h2>
      <p class="usage">Answer each in 2 to 4 sentences. Use the language from this week's lecture and your drawings as evidence.</p>
{qs}
    </article>
    """).strip()


def render_workbook(wb):
    panels_html = "\n".join(render_draw_panel(p) for p in wb["anatomy_panels"])
    label_html = render_label_list(wb["label_list"])
    physio_html = render_physio_section(wb)
    synth_html = render_synthesis(wb["synthesis_questions"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 . {escape(wb['title'])} . Lab Workbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header>
  <p class="eyebrow">{escape(wb['eyebrow'])}</p>
  <h1>{escape(wb['title'])}</h1>
  <p class="subhead">{escape(wb['subhead'])}</p>
  <p class="usage">Print this page. You will draw your own diagrams from the directions below, then hand-label the structures listed. Drawing by hand is the integrity mechanism for this course.</p>
</header>
<main id="main" tabindex="-1">
  <div class="toolbar no-print">
    <button type="button" class="btn btn-primary" onclick="window.print()">Print this workbook</button>
    <a class="btn btn-ghost" href="biol304_syllabus.html" target="_top">&larr; Back to syllabus hub</a>
  </div>

  <div class="section-band anatomy">
    <p class="tag">Part 1 of 2</p>
    <h2>Anatomy Lab</h2>
  </div>

  <article class="card">
    <h2>1A. What you will draw</h2>
    <p>{escape(wb['anatomy_intro'])}</p>
  </article>

{panels_html}

{label_html}

  <div class="section-band physiology">
    <p class="tag">Part 2 of 2</p>
    <h2>Physiology Lab</h2>
  </div>

{physio_html}

{synth_html}

  <article class="card">
    <h2>3. What to submit</h2>
    <p>Complete <strong>both</strong> the Anatomy Lab (your own drawings, hand-labeled, plus the structures list) and the Physiology Lab (activity and synthesis questions). Photograph or scan every page and upload to Canvas before the deadline listed on the schedule. Hand-drawn, hand-labeled work is the integrity mechanism for this course. Typed or AI-generated diagrams are not accepted.</p>
  </article>
</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 Lab Workbook . Day {wb['day_num']} of 32</p></footer>
{SCRIPT}
</body>
</html>
"""
    return html


def validate(html):
    """Catch the things her global rules forbid. Be careful with word
    matching: "sage" is a substring of "usage" and "message", so we look
    for token boundaries instead."""
    import re as _re
    issues = []
    if "—" in html:
        issues.append("Em-dash found in output")
    # Sage colors / class names. Match on hex codes (case-insensitive)
    # and on the literal CSS class .sage or var(--sage*).
    forbidden_hex = ("#4F6B57", "#3F5B47", "#F1F4F1")
    for hx in forbidden_hex:
        if hx.lower() in html.lower():
            issues.append(f"Forbidden hex color: {hx}")
    if _re.search(r"\.sage\b|--sage[-\w]*\b|class=['\"][^'\"]*\bsage\b", html):
        issues.append("Sage class or CSS variable in output")
    # Cream as a color token. Allow off-white #FAFAF9 (page bg per palette).
    if _re.search(r"--cream\b|\bcream-\w+\b", html, _re.I):
        issues.append("Cream color token in output")
    # Byline must be Dr. Sharilyn Rennie (no credential suffix).
    if ", ND" in html or ", MD" in html:
        issues.append("Credential suffix on byline")
    return issues


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    all_issues = []
    for wb in WORKBOOKS:
        html = render_workbook(wb)
        issues = validate(html)
        if issues:
            all_issues.append((wb["filename"], issues))
        out = os.path.join(OUT_DIR, wb["filename"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {out} ({len(html)} bytes)")

    if all_issues:
        print("\nVALIDATION ISSUES:")
        for name, issues in all_issues:
            print(f"  {name}: {issues}")
        return 1
    print("\nAll workbooks validated cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
