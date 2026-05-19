/* ============================================================
   BIO 304 Course Content
   ------------------------------------------------------------
   Edit this file to add/remove topics, drop in video URLs, or
   tune cards. The engine in bio304-spaced-recall-prototype.html
   reads window.BIO304_COURSE_CONTENT at load time.

   How to add a video:
     Find the topic, set:
       videoUrl: "https://www.youtube.com/watch?v=XXXXXXXXXXX"
     or
       videoUrl: "videos/membrane-transport.mp4"
     The engine will mount the player and (for self-hosted mp4)
     enable Mark Watched on the native "ended" event.

   How to wire the OpenStax reference link:
     Each topic has a readingUrl pointing to its OpenStax A&P 2e section.
     The Learning view shows an "Open OpenStax reference" button. Students
     use it to clarify a specific concept, not to read cover-to-cover.

   How to wire the notes link:
     Notes live in the existing course notes hub, not in this file.
     Set notesUrl on the topic to the URL of the topic's note page:
       notesUrl: "https://drsrennie.com/bio304/notes/homeostasis"
     The Learning view will show an "Open notes in new tab" button
     that opens the link with target=_blank rel=noopener noreferrer.
     Leave notesUrl as null until the page exists; the learning view
     will display "Notes link not yet wired for this topic."

   How to add a new topic:
     Inside the relevant module's topics array, copy an existing
     topic object and edit. Each card needs a unique id within
     the topic, a dok level (1, 2, or 3), and a q/a pair.

   Card guidance:
     DOK 1 - recall and define
     DOK 2 - apply, explain, contrast, predict from given data
     DOK 3 - analyze, design, integrate across systems, troubleshoot
   ============================================================ */

window.BIO304_COURSE_CONTENT = {
  courseLabel: "BIO 304",
  /* Course start date (Monday of week 1). Leave null to disable scheduled release. */
  courseStart: null,

  modules: [

    /* ============================================================
       MODULE 1: FOUNDATIONS
       ============================================================ */
    {
      id: "m-01-foundations",
      week: 1,
      title: "Foundations of Anatomy and Physiology",
      topics: [

        {
          id: "t-levels-of-organization",
          title: "Levels of Organization",
          summary: "From atoms to organism: how complexity scales and where new function emerges.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body",
          lecturePageUrl: "levels-of-organization.html",
          dayInCourse: 1,
          videoLabel: "Video: Levels of organization (pending)",
          gateKeywords: ["atom", "cell", "tissue", "organ", "organ system", "organism"],
          notes: [
            { heading: "The hierarchy", body: [
              "Chemical level: atoms combine to form molecules (water, glucose, proteins).",
              "Cellular level: molecules assemble into organelles and then cells, the smallest living units.",
              "Tissue level: groups of similar cells working together (epithelial, connective, muscle, nervous).",
              "Organ level: two or more tissues with a shared function (heart, kidney, skin).",
              "Organ system level: organs that cooperate on a larger job.",
              "Organism: all systems working as a coordinated whole."
            ]},
            { heading: "The 11 organ systems", body: [
              "Integumentary, skeletal, muscular, nervous, endocrine.",
              "Cardiovascular, lymphatic/immune, respiratory, digestive, urinary, reproductive."
            ]},
            { heading: "Emergence", body: [
              "Each level shows properties the parts alone do not have. A single cardiac cell can twitch, but only the whole heart can pump blood.",
              "Every higher level depends on every lower one. Damage at one level usually shows up as failure at higher levels."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "List the levels of structural organization from smallest to largest.", a: "Chemical, cellular, tissue, organ, organ system, organism." },
            { id: "c2", dok: 1, q: "How many organ systems make up the human body?", a: "Eleven." },
            { id: "c3", dok: 1, q: "Define tissue.", a: "A group of similar cells that work together to perform a common function." },
            { id: "c4", dok: 1, q: "At which level of organization do organelles appear?", a: "The cellular level (organelles are subcellular structures inside a cell)." },
            { id: "c5", dok: 2, q: "Why is the cardiovascular system considered to be at the organ-system level, not the organ level?", a: "It includes multiple organs (heart, blood vessels) plus blood, working together toward a shared function (transport). Any single one of these on its own is just an organ." },
            { id: "c6", dok: 2, q: "Give an example of an organ that participates in more than one organ system.", a: "Pancreas (endocrine and digestive). Liver (digestive and several others). Kidney (urinary and endocrine, since it makes erythropoietin and renin)." },
            { id: "c7", dok: 3, q: "A drug damages mitochondrial function in skeletal muscle. Predict the cascading effects up the levels of organization.", a: "Cellular level: ATP supply drops, fiber fatigue. Tissue level: muscle tissue weakens and can no longer hold prolonged contractions. Organ level: skeletal muscles tire quickly. Organ system level: posture, locomotion, and breathing (respiratory muscles) become impaired. Organism: exercise intolerance and, in severe cases, respiratory failure." }
          ]
        },

        {
          id: "t-anatomical-terminology",
          title: "Anatomical Terminology and Body Regions",
          summary: "Anatomical position, directional terms, body planes, cavities, and the four abdominal quadrants.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/1-6-anatomical-terminology",
          lecturePageUrl: "anatomical-position.html",
          dayInCourse: 1,
          videoLabel: "Video: Anatomical terminology (pending)",
          gateKeywords: ["anatomical position", "sagittal", "transverse", "superior", "anterior", "abdominopelvic"],
          notes: [
            { heading: "Anatomical position", body: [
              "Body upright, feet shoulder-width apart, palms forward, thumbs out.",
              "All directional terms are defined relative to this reference, no matter how the patient is actually positioned."
            ]},
            { heading: "Directional terms", body: [
              "Superior / inferior (above / below).",
              "Anterior (ventral) / posterior (dorsal).",
              "Medial / lateral (toward midline / away from midline).",
              "Proximal / distal (closer to / farther from the trunk or origin).",
              "Superficial / deep."
            ]},
            { heading: "Planes and cavities", body: [
              "Sagittal plane: vertical, divides into right and left. Midsagittal cuts into equal halves.",
              "Frontal (coronal) plane: vertical, divides into anterior and posterior.",
              "Transverse (horizontal) plane: divides into superior and inferior.",
              "Dorsal body cavity (cranial + vertebral). Ventral body cavity (thoracic + abdominopelvic).",
              "Four abdominal quadrants: RUQ, LUQ, RLQ, LLQ. Nine regions: umbilical, epigastric, hypogastric, and three on each side."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What plane divides the body into right and left equal halves?", a: "The midsagittal (median) plane." },
            { id: "c2", dok: 1, q: "Is the knee proximal or distal to the ankle?", a: "Proximal." },
            { id: "c3", dok: 1, q: "Which cavity contains the lungs?", a: "The thoracic cavity (specifically the pleural cavities) within the ventral body cavity." },
            { id: "c4", dok: 1, q: "Name the four abdominal quadrants.", a: "Right upper, left upper, right lower, left lower (RUQ, LUQ, RLQ, LLQ)." },
            { id: "c5", dok: 2, q: "Explain why anatomical position is the reference for all directional terms, even when a patient is lying down.", a: "It is a fixed reference frame. If terms changed based on the patient's posture, the same anatomical relationship could have two opposite descriptions. Anatomical position keeps the vocabulary consistent and unambiguous." },
            { id: "c6", dok: 2, q: "A patient has pain in the right upper quadrant. Name two organs that could plausibly be the source.", a: "Liver, gallbladder, right kidney (technically retroperitoneal), part of the stomach, head of the pancreas, hepatic flexure of the colon." },
            { id: "c7", dok: 3, q: "A radiologist describes a tumor as 'medial to the right lung, superior to the diaphragm, anterior to the vertebral column.' Locate the structure and name the body cavity it sits in.", a: "Mediastinum of the thoracic cavity. The tumor is likely in the central mediastinum, between the lungs, above the diaphragm, and in front of the spine." }
          ]
        },

        {
          id: "t-homeostasis",
          title: "Homeostasis and Feedback Loops",
          summary: "Set points, the four-part negative feedback loop, and why positive feedback is the rare exception.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/1-5-homeostasis",
          lecturePageUrl: "homeostasis-feedback.html",
          dayInCourse: 2,
          videoLabel: "Video: Homeostasis and feedback (pending)",
          gateKeywords: ["homeostasis", "feedback", "set point", "receptor", "effector"],
          notes: [
            { heading: "Homeostasis", body: [
              "Maintenance of a relatively stable internal environment despite external change.",
              "Set point: the target value for a regulated variable (core body temperature near 37 degrees C)."
            ]},
            { heading: "Negative feedback (the workhorse)", body: [
              "Stimulus changes a variable away from set point.",
              "Receptor detects the change.",
              "Control center compares to set point and signals an effector.",
              "Effector produces a response that opposes the change and returns the variable toward set point."
            ]},
            { heading: "Positive feedback (less common)", body: [
              "Amplifies the original signal until an end point is reached.",
              "Examples: oxytocin in labor, platelet plug formation."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Define homeostasis.", a: "The maintenance of a relatively stable internal environment despite external change." },
            { id: "c2", dok: 1, q: "List the four core components of a negative feedback loop.", a: "Stimulus, receptor, control center, effector (with a response that opposes the change)." },
            { id: "c3", dok: 1, q: "Which feedback type is most common in physiology?", a: "Negative feedback." },
            { id: "c4", dok: 1, q: "Give one example of a regulated variable.", a: "Core body temperature, blood glucose, blood pH, blood pressure, blood osmolarity, or arterial pO2." },
            { id: "c5", dok: 2, q: "Explain how negative feedback returns body temperature to set point after exercise.", a: "Thermoreceptors detect a rise. The hypothalamus signals sweating and cutaneous vasodilation. Heat is lost. Core temperature falls back toward set point." },
            { id: "c6", dok: 2, q: "Contrast negative and positive feedback in terms of their effect on the original stimulus.", a: "Negative feedback opposes the change and stabilizes the variable. Positive feedback amplifies the change and drives the system to an end point." },
            { id: "c7", dok: 3, q: "Predict what happens to a patient whose hypothalamic set point for temperature is reset upward by pyrogens.", a: "The body treats normal temperature as too low. Vasoconstriction and shivering raise core temperature to the new set point. When pyrogens clear, the set point falls and the patient sweats to dump heat." },
            { id: "c8", dok: 3, q: "A patient with type 1 diabetes has lost the ability to make insulin. Analyze how this breaks the glucose feedback loop.", a: "Insulin is the effector signal that lowers blood glucose. Without it, the loop has no functioning effector. Receptors detect the post-meal spike but no response brings glucose back to set point, so it stays elevated." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 3: THE CELL
       ============================================================ */
    {
      id: "m-03-cell",
      week: 1,
      title: "The Cell",
      topics: [

        {
          id: "t-cell-structure",
          title: "Cell Structure and Organelles",
          summary: "Plasma membrane, nucleus, and the major cytoplasmic organelles that do the work of the cell.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/3-2-the-cytoplasm-and-cellular-organelles",
          lecturePageUrl: "cell-structure.html",
          dayInCourse: 3,
          videoLabel: "Video: Cell structure (pending)",
          gateKeywords: ["nucleus", "mitochondria", "endoplasmic reticulum", "Golgi", "ribosome", "plasma membrane"],
          notes: [
            { heading: "Plasma membrane", body: [
              "Phospholipid bilayer with embedded proteins.",
              "Selectively permeable: gates what enters and leaves.",
              "Surface proteins serve as receptors, channels, transporters, and identity markers."
            ]},
            { heading: "Nucleus and protein synthesis", body: [
              "Stores DNA. Bounded by a double nuclear envelope with nuclear pores.",
              "Nucleolus inside synthesizes ribosomal RNA.",
              "Free ribosomes make cytoplasmic proteins. Ribosomes on rough ER make membrane and secreted proteins."
            ]},
            { heading: "Energy and processing", body: [
              "Mitochondria: site of cellular respiration. Inner membrane folded into cristae. Has its own DNA.",
              "Smooth ER: lipid synthesis, detoxification, Ca²⁺ storage.",
              "Golgi apparatus: modifies, sorts, and packages proteins from the ER.",
              "Lysosomes: digest debris with acid hydrolases.",
              "Peroxisomes: detoxify reactive oxygen species and break down fatty acids."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Where does cellular respiration occur?", a: "In the mitochondria." },
            { id: "c2", dok: 1, q: "What is the function of the Golgi apparatus?", a: "Modifies, sorts, and packages proteins received from the rough ER." },
            { id: "c3", dok: 1, q: "Which organelle digests cellular debris?", a: "Lysosome." },
            { id: "c4", dok: 1, q: "Which organelle makes ribosomal RNA?", a: "The nucleolus." },
            { id: "c5", dok: 2, q: "Why would a cell that secretes a lot of protein (like a pancreatic acinar cell) have abundant rough ER?", a: "Rough ER ribosomes synthesize secreted proteins and pass them into the ER lumen for folding and trafficking. Cells with heavy secretory output need a large rough ER to keep up." },
            { id: "c6", dok: 2, q: "Cardiac muscle cells have unusually large numbers of mitochondria. Why?", a: "They contract continuously and have very high ATP demands. More mitochondria means more ATP production capacity." },
            { id: "c7", dok: 3, q: "A genetic defect prevents lysosomal enzymes from being tagged for transport to the lysosome. Predict the cellular consequence over time.", a: "Undigested debris and substrates accumulate inside the lysosome. The organelle swells, cell function degrades, and the patient develops a lysosomal storage disease (such as I-cell disease)." }
          ]
        },

        {
          id: "t-membrane-transport",
          title: "Membrane Transport",
          summary: "Passive vs active, simple vs facilitated, primary vs secondary, plus bulk transport.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/3-1-the-cell-membrane",
          lecturePageUrl: "membrane-transport.html",
          dayInCourse: 4,
          videoLabel: "Video: Membrane transport (pending)",
          gateKeywords: ["diffusion", "osmosis", "active transport", "gradient", "channel", "carrier"],
          notes: [
            { heading: "The membrane in 30 seconds", body: [
              "Phospholipid bilayer with embedded proteins.",
              "Hydrophobic interior excludes large polar molecules and ions.",
              "Small nonpolar molecules cross easily; everything else needs help."
            ]},
            { heading: "Passive transport (no ATP)", body: [
              "Simple diffusion: nonpolar solutes move down their gradient through the bilayer.",
              "Facilitated diffusion: polar solutes and ions move down their gradient through channels or carriers.",
              "Osmosis: water moves down its concentration gradient, usually through aquaporins."
            ]},
            { heading: "Active transport (uses ATP, direct or indirect)", body: [
              "Primary active transport: pump uses ATP directly (Na⁺/K⁺ ATPase).",
              "Secondary active transport: uses the gradient set up by a primary pump (Na⁺-glucose symporter)."
            ]},
            { heading: "Bulk transport", body: [
              "Endocytosis: cell engulfs material into a vesicle.",
              "Exocytosis: vesicle fuses with the membrane and releases contents."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Define diffusion.", a: "Net movement of solute from a region of higher concentration to one of lower concentration." },
            { id: "c2", dok: 1, q: "Which transport type uses ATP directly?", a: "Primary active transport." },
            { id: "c3", dok: 1, q: "Name two molecules that cross by simple diffusion.", a: "Oxygen, carbon dioxide, steroid hormones, small lipids." },
            { id: "c4", dok: 1, q: "What is the stoichiometry of the Na⁺/K⁺ ATPase?", a: "Three Na⁺ out, two K⁺ in, per ATP." },
            { id: "c5", dok: 2, q: "How does the Na⁺/K⁺ ATPase enable secondary active transport?", a: "It builds and maintains the inward Na⁺ gradient. Secondary transporters use that gradient as energy to move other solutes against their own gradients." },
            { id: "c6", dok: 2, q: "Predict water movement when a red blood cell is placed in a hypertonic solution.", a: "Water exits the cell. The cell crenates (shrinks)." },
            { id: "c7", dok: 3, q: "Ouabain blocks the Na⁺/K⁺ ATPase. Predict the effect on glucose absorption in the small intestine.", a: "Intracellular Na⁺ rises, the Na⁺ gradient collapses, the Na⁺-glucose symporter loses its driving force, and glucose absorption falls sharply." },
            { id: "c8", dok: 3, q: "Design an experiment to distinguish simple from facilitated diffusion of a solute.", a: "Measure flux versus solute concentration. Simple diffusion: linear, non-saturating. Facilitated diffusion: saturates because carriers are finite." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 4: TISSUES
       ============================================================ */
    {
      id: "m-04-tissues",
      week: 2,
      title: "Tissues",
      topics: [

        {
          id: "t-epithelial-tissue",
          title: "Epithelial Tissue Classification",
          summary: "Naming epithelia by layer and cell shape; where each type lives and what it does.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/4-2-epithelial-tissue",
          lecturePageUrl: "epithelial-tissue.html",
          dayInCourse: 5,
          videoLabel: "Video: Epithelial tissue (pending)",
          gateKeywords: ["epithelium", "simple", "stratified", "squamous", "cuboidal", "columnar"],
          notes: [
            { heading: "Naming convention", body: [
              "First name = number of layers (simple = one; stratified = two or more).",
              "Second name = shape of apical cells (squamous, cuboidal, columnar).",
              "Pseudostratified and transitional are special cases."
            ]},
            { heading: "Simple epithelia (function = exchange or secretion)", body: [
              "Simple squamous: alveoli, capillary endothelium. Diffusion.",
              "Simple cuboidal: kidney tubules, glands. Secretion and absorption.",
              "Simple columnar: small intestine, stomach. Absorption and secretion."
            ]},
            { heading: "Stratified and special epithelia", body: [
              "Stratified squamous: epidermis, esophagus. Abrasion resistance.",
              "Transitional: urinary bladder. Stretches as the organ fills.",
              "Pseudostratified ciliated columnar: upper airway. Mucociliary clearance."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What does the first name of an epithelium tell you?", a: "Number of cell layers (simple = one, stratified = two or more)." },
            { id: "c2", dok: 1, q: "Where is simple squamous epithelium found?", a: "Alveoli of the lung and the endothelium of blood vessels." },
            { id: "c3", dok: 1, q: "Name the epithelium of the urinary bladder.", a: "Transitional epithelium." },
            { id: "c4", dok: 1, q: "What is the function of stratified squamous epithelium?", a: "Protection from abrasion." },
            { id: "c5", dok: 2, q: "Why are alveoli lined with simple squamous rather than columnar epithelium?", a: "Their job is gas exchange by diffusion. A single flat layer minimizes diffusion distance." },
            { id: "c6", dok: 2, q: "Why does pseudostratified columnar epithelium look stratified even though it is not?", a: "Cell nuclei sit at different heights. Every cell still contacts the basement membrane, so it is truly one layer." },
            { id: "c7", dok: 3, q: "A smoker has metaplasia of the upper airway: pseudostratified ciliated columnar is replaced by stratified squamous. Predict two functional consequences.", a: "Loss of cilia abolishes mucociliary clearance, so pathogens linger. The new epithelium is also less able to secrete mucus, raising infection risk." }
          ]
        },

        {
          id: "t-connective-tissue",
          title: "Connective Tissues",
          summary: "Cells embedded in a matrix: loose, dense, cartilage, bone, blood.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/4-3-connective-tissue-supports-and-protects",
          lecturePageUrl: "connective-tissues.html",
          dayInCourse: 6,
          videoLabel: "Video: Connective tissue (pending)",
          gateKeywords: ["connective tissue", "matrix", "fibroblast", "collagen", "cartilage", "bone"],
          notes: [
            { heading: "What makes a tissue connective", body: [
              "Cells suspended in a non-living extracellular matrix.",
              "Matrix = ground substance + protein fibers (collagen, elastic, reticular).",
              "Properties of the matrix (more fibers? more ground substance? mineralized?) decide what the tissue can do."
            ]},
            { heading: "Major types", body: [
              "Loose: areolar (general filler), adipose (fat), reticular (lymph nodes).",
              "Dense: regular (tendons, ligaments), irregular (dermis), elastic (large arteries).",
              "Cartilage: hyaline (joints, trachea), elastic (ear), fibrocartilage (intervertebral discs).",
              "Bone: rigid, mineralized matrix.",
              "Blood: cells in a fluid matrix (plasma)."
            ]},
            { heading: "Repair", body: [
              "Most connective tissue heals via fibroblast activity and collagen deposition.",
              "Cartilage is avascular and heals poorly.",
              "Bone heals well due to robust blood supply and osteoblast activity."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What three things make up the extracellular matrix?", a: "Ground substance, protein fibers, and water." },
            { id: "c2", dok: 1, q: "Which connective tissue type makes up tendons?", a: "Dense regular connective tissue." },
            { id: "c3", dok: 1, q: "Which cell builds the protein fibers of most connective tissues?", a: "Fibroblast." },
            { id: "c4", dok: 1, q: "What kind of cartilage is in intervertebral discs?", a: "Fibrocartilage." },
            { id: "c5", dok: 2, q: "Why does cartilage heal so much more slowly than bone?", a: "Cartilage is avascular. Chondrocytes get nutrients by diffusion from surrounding tissue. Without a direct blood supply, repair cells, oxygen, and nutrients arrive slowly." },
            { id: "c6", dok: 2, q: "Adipose tissue is classified as connective tissue. Why?", a: "Adipocytes are sparsely scattered in an extracellular matrix, which fits the connective tissue definition. Their function is energy storage and insulation." },
            { id: "c7", dok: 3, q: "A genetic defect in type I collagen synthesis causes osteogenesis imperfecta. Predict the multisystem effects.", a: "Type I collagen is in bone, tendons, ligaments, dermis, sclera, and dentin. Patients show fragile bones, blue sclera (thin sclera makes underlying choroid visible), loose joints, thin skin, and dental problems." }
          ]
        },

        {
          id: "t-muscle-nervous-tissue",
          title: "Muscle and Nervous Tissue Overview",
          summary: "Three muscle types compared, plus neurons and glia at a tissue level.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/4-4-muscle-tissue-and-motion",
          lecturePageUrl: "muscle-nervous-tissue.html",
          dayInCourse: 7,
          videoLabel: "Video: Muscle and nervous tissue (pending)",
          gateKeywords: ["skeletal muscle", "smooth muscle", "cardiac muscle", "neuron", "glia"],
          notes: [
            { heading: "Three muscle tissue types", body: [
              "Skeletal: striated, multinucleated, voluntary, attached to bone.",
              "Cardiac: striated, single nucleus, involuntary, intercalated discs, found only in heart.",
              "Smooth: not striated, single nucleus, involuntary, in walls of hollow organs and vessels."
            ]},
            { heading: "Nervous tissue", body: [
              "Neurons: excitable cells that transmit electrical signals. Cell body, dendrites, axon.",
              "Glia: support cells (astrocytes, oligodendrocytes, microglia, ependymal in CNS; Schwann and satellite in PNS).",
              "Glia outnumber neurons and do most of the maintenance, insulation, and immune surveillance of the nervous system."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which muscle tissue is striated and voluntary?", a: "Skeletal muscle." },
            { id: "c2", dok: 1, q: "Which muscle tissue has intercalated discs?", a: "Cardiac muscle." },
            { id: "c3", dok: 1, q: "Name two glial cell types in the CNS.", a: "Any two of: astrocytes, oligodendrocytes, microglia, ependymal cells." },
            { id: "c4", dok: 1, q: "Which cell type forms myelin in the PNS?", a: "Schwann cell." },
            { id: "c5", dok: 2, q: "Why are intercalated discs essential for cardiac function?", a: "They contain gap junctions that let depolarization spread cell to cell, so cardiac muscle contracts as a coordinated unit (functional syncytium). Without them the heart could not pump." },
            { id: "c6", dok: 3, q: "Multiple sclerosis destroys oligodendrocytes in the CNS. Predict the consequence for action potential conduction and explain why.", a: "Oligodendrocytes make CNS myelin. Without myelin, saltatory conduction fails and axons either conduct slowly (continuous conduction) or not at all. Symptoms reflect which tracts are demyelinated." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 5: INTEGUMENTARY SYSTEM
       ============================================================ */
    {
      id: "m-05-integumentary",
      week: 2,
      title: "Integumentary System",
      topics: [

        {
          id: "t-skin-layers",
          title: "Skin Structure and Layers",
          summary: "Epidermis, dermis, hypodermis: who lives where and what they do.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/5-1-layers-of-the-skin",
          dayInCourse: 7,
          videoLabel: "Video: Skin layers (pending)",
          gateKeywords: ["epidermis", "dermis", "hypodermis", "keratin", "melanin", "stratum"],
          notes: [
            { heading: "Epidermis (avascular, stratified squamous keratinized)", body: [
              "Layers from deep to superficial: basale, spinosum, granulosum, lucidum (thick skin only), corneum.",
              "Keratinocytes mature upward and die into the cornified layer.",
              "Melanocytes (in basale) make melanin, transferred to keratinocytes for UV protection.",
              "Langerhans cells (immune) and Merkel cells (touch) also live here."
            ]},
            { heading: "Dermis (vascular, connective tissue)", body: [
              "Papillary layer: loose connective tissue with capillary loops, Meissner corpuscles, pain and temperature receptors.",
              "Reticular layer: dense irregular connective tissue, gives strength.",
              "Hair follicles, glands, and nerves are embedded here."
            ]},
            { heading: "Hypodermis (subcutaneous)", body: [
              "Mostly adipose plus loose connective tissue.",
              "Anchors skin, insulates, stores energy.",
              "Not technically part of the skin but functionally inseparable."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "List the layers of the epidermis from deep to superficial in thick skin.", a: "Stratum basale, spinosum, granulosum, lucidum, corneum." },
            { id: "c2", dok: 1, q: "Which cell makes melanin?", a: "The melanocyte (in the stratum basale)." },
            { id: "c3", dok: 1, q: "Which dermal layer gives skin its tensile strength?", a: "The reticular layer." },
            { id: "c4", dok: 1, q: "Is the epidermis vascular?", a: "No. It receives nutrients by diffusion from the dermal blood supply." },
            { id: "c5", dok: 2, q: "Explain why a deep dermal burn is more dangerous than a superficial epidermal burn.", a: "The dermis contains blood vessels, nerves, and the appendages from which new epidermis regrows. Lose the dermis and the body loses fluid, sensation, and the cells needed to heal back to normal skin." },
            { id: "c6", dok: 3, q: "Vitamin D synthesis begins when UVB strikes 7-dehydrocholesterol in the skin. Predict why dark-skinned individuals at high latitudes are at higher risk of vitamin D deficiency.", a: "Melanin absorbs UVB before it can reach the precursor. Combined with low UVB at high latitudes, this reduces cutaneous vitamin D synthesis, raising deficiency risk." }
          ]
        },

        {
          id: "t-skin-functions",
          title: "Skin Functions and Accessory Structures",
          summary: "Protection, thermoregulation, sensation, vitamin D; plus hair, glands, and nails.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/5-3-functions-of-the-integumentary-system",
          dayInCourse: 8,
          videoLabel: "Video: Skin functions and accessories (pending)",
          gateKeywords: ["thermoregulation", "sebaceous", "sweat gland", "vitamin D", "hair follicle"],
          notes: [
            { heading: "Major functions", body: [
              "Physical and chemical barrier (keratin, lipids, low pH).",
              "Thermoregulation (blood vessel dilation/constriction, sweat).",
              "Sensation (touch, pressure, temperature, pain via dermal receptors).",
              "Vitamin D synthesis (UVB on 7-dehydrocholesterol).",
              "Excretion of small amounts of nitrogenous waste in sweat."
            ]},
            { heading: "Accessory structures", body: [
              "Hair follicle: extends from dermis. Hair grows from matrix at the base.",
              "Sebaceous gland: oily sebum to hair shaft, waterproofs and inhibits microbes.",
              "Eccrine sweat gland: watery sweat, all over body, thermoregulation.",
              "Apocrine sweat gland: axilla, groin; activated at puberty; substrate for skin bacteria (odor).",
              "Nail: keratinized epidermis over distal phalanges; nail matrix produces growth."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the sweat gland type responsible for thermoregulation.", a: "Eccrine." },
            { id: "c2", dok: 1, q: "What does sebum do?", a: "Lubricates hair and skin, waterproofs, and inhibits microbial growth." },
            { id: "c3", dok: 1, q: "Vitamin D synthesis requires what wavelength of light?", a: "Ultraviolet B (UVB)." },
            { id: "c4", dok: 1, q: "Where does new hair growth come from?", a: "The hair matrix at the base of the follicle." },
            { id: "c5", dok: 2, q: "Explain how cutaneous vasodilation helps cool the body.", a: "Dilation brings warm blood close to the skin surface. Heat dissipates to the cooler environment by radiation and conduction, lowering core temperature." },
            { id: "c6", dok: 3, q: "A patient with extensive third-degree burns is at high risk of hypothermia and infection. Explain both, in terms of skin functions lost.", a: "Loss of barrier function: no insulation against heat loss and no defense against microbes entering deeper tissues. Loss of vascular control: cannot vasoconstrict to retain heat. Loss of fluid containment: evaporation of plasma-like fluid accelerates heat loss and dehydration." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 6: SKELETAL SYSTEM
       ============================================================ */
    {
      id: "m-06-skeletal",
      week: 3,
      title: "Skeletal System",
      topics: [

        {
          id: "t-bone-tissue",
          title: "Bone Tissue and Bone Growth",
          summary: "Cells of bone, compact vs spongy, intramembranous vs endochondral ossification, and lifelong remodeling.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/6-3-bone-structure",
          lecturePageUrl: "bone-tissue.html",
          dayInCourse: 9,
          videoLabel: "Video: Bone tissue (pending)",
          gateKeywords: ["osteoblast", "osteoclast", "osteocyte", "compact bone", "spongy bone", "ossification"],
          notes: [
            { heading: "Bone cells", body: [
              "Osteogenic (osteoprogenitor): stem cells.",
              "Osteoblasts: build bone matrix.",
              "Osteocytes: mature osteoblasts trapped in lacunae; maintain matrix and sense load.",
              "Osteoclasts: from monocyte lineage; resorb bone by acid + enzyme secretion."
            ]},
            { heading: "Bone structure", body: [
              "Compact bone: outer layer, organized into osteons (Haversian systems).",
              "Spongy (cancellous) bone: inner trabecular network, often contains red marrow.",
              "Long bone parts: diaphysis (shaft), epiphysis (ends), metaphysis (growth zone), periosteum (outer covering), endosteum (inner lining)."
            ]},
            { heading: "Ossification and remodeling", body: [
              "Intramembranous ossification: flat bones of skull and clavicle, from mesenchyme.",
              "Endochondral ossification: most other bones, from a hyaline cartilage model.",
              "Epiphyseal (growth) plate: drives lengthening until closure in late adolescence.",
              "Remodeling continues throughout life: balance of osteoblast and osteoclast activity, modulated by calcium, vitamin D, PTH, calcitonin, sex steroids, and load."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which bone cell builds new bone matrix?", a: "Osteoblast." },
            { id: "c2", dok: 1, q: "Which bone cell resorbs bone?", a: "Osteoclast." },
            { id: "c3", dok: 1, q: "What is an osteon?", a: "The structural unit of compact bone: concentric lamellae of matrix around a central (Haversian) canal containing vessels and nerves." },
            { id: "c4", dok: 1, q: "Which ossification type produces most long bones?", a: "Endochondral ossification (cartilage model)." },
            { id: "c5", dok: 2, q: "Why is mature bone metabolically active even when growth has stopped?", a: "Bone is continuously remodeled. Osteoblasts and osteoclasts replace old matrix, repair microdamage, adjust shape to load, and provide a reservoir of calcium and phosphate the body draws on." },
            { id: "c6", dok: 2, q: "Explain how parathyroid hormone (PTH) raises blood calcium.", a: "PTH activates osteoclasts (indirectly, via osteoblast signaling), which resorb bone and release calcium and phosphate into the blood. PTH also increases renal calcium reabsorption and activation of vitamin D, raising gut absorption." },
            { id: "c7", dok: 3, q: "A postmenopausal woman has accelerated bone loss. Tie this to the underlying cellular biology.", a: "Estrogen normally restrains osteoclast activity. After menopause, estrogen falls, osteoclast activity rises relative to osteoblast activity, and net bone resorption exceeds formation. Bone density falls over years, predisposing to osteoporotic fracture." }
          ]
        },

        {
          id: "t-axial-skeleton",
          title: "Axial Skeleton",
          summary: "Skull, vertebral column, and thoracic cage: the central axis of the body.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/7-1-divisions-of-the-skeletal-system",
          lecturePageUrl: "axial-skeleton.html",
          dayInCourse: 10,
          videoLabel: "Video: Axial skeleton (pending)",
          gateKeywords: ["skull", "vertebra", "cervical", "thoracic", "lumbar", "sternum"],
          notes: [
            { heading: "Skull", body: [
              "Cranial bones (8): frontal, parietal (2), temporal (2), occipital, sphenoid, ethmoid.",
              "Facial bones (14): maxillae, zygomatics, nasals, mandible, and others.",
              "Sutures are immovable joints between cranial bones."
            ]},
            { heading: "Vertebral column", body: [
              "Cervical (7): C1 (atlas) and C2 (axis) allow head movement.",
              "Thoracic (12): articulate with ribs.",
              "Lumbar (5): largest, weight-bearing.",
              "Sacrum: 5 fused vertebrae.",
              "Coccyx: 3-4 fused vertebrae."
            ]},
            { heading: "Thoracic cage", body: [
              "Sternum (manubrium, body, xiphoid).",
              "12 pairs of ribs: 7 true (1-7), 3 false (8-10), 2 floating (11-12).",
              "Functions: protects heart and lungs, anchors respiratory muscles."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "How many cervical vertebrae are there?", a: "Seven." },
            { id: "c2", dok: 1, q: "Name the first two cervical vertebrae and their distinguishing feature.", a: "C1 (atlas), no body, supports the skull. C2 (axis), has the dens that allows head rotation." },
            { id: "c3", dok: 1, q: "Which ribs are 'floating'?", a: "Ribs 11 and 12 (no anterior attachment to sternum or costal cartilage of another rib)." },
            { id: "c4", dok: 1, q: "How many cranial bones are there?", a: "Eight." },
            { id: "c5", dok: 2, q: "Why are lumbar vertebrae larger than cervical vertebrae?", a: "They bear more body weight. Larger vertebral bodies distribute compressive load over a greater area, reducing stress." },
            { id: "c6", dok: 3, q: "A patient with osteoporosis sustains a compression fracture of a thoracic vertebra. Predict the postural consequence and explain why.", a: "Anterior vertebral body collapses while the posterior remains taller, producing a wedge shape. Cumulative wedge fractures across the thoracic spine produce kyphosis ('dowager's hump'). The biomechanical change can also reduce thoracic volume, impacting breathing." }
          ]
        },

        {
          id: "t-appendicular-skeleton",
          title: "Appendicular Skeleton",
          summary: "Pectoral girdle and upper limb, pelvic girdle and lower limb.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/8-1-the-pectoral-girdle",
          lecturePageUrl: "appendicular-skeleton.html",
          dayInCourse: 11,
          videoLabel: "Video: Appendicular skeleton (pending)",
          gateKeywords: ["clavicle", "scapula", "humerus", "femur", "pelvis", "tibia"],
          notes: [
            { heading: "Upper limb", body: [
              "Pectoral girdle: clavicle (anterior) and scapula (posterior). Connects arm to axial skeleton.",
              "Arm: humerus.",
              "Forearm: radius (lateral, thumb side) and ulna (medial).",
              "Hand: 8 carpals, 5 metacarpals, 14 phalanges."
            ]},
            { heading: "Lower limb", body: [
              "Pelvic girdle: two coxal (hip) bones, each fused from ilium, ischium, pubis. With sacrum forms the pelvis.",
              "Thigh: femur (largest bone in body).",
              "Leg: tibia (weight-bearing) and fibula (lateral).",
              "Foot: 7 tarsals, 5 metatarsals, 14 phalanges."
            ]},
            { heading: "Functional notes", body: [
              "Pectoral girdle is loosely attached for arm mobility.",
              "Pelvic girdle is fused and weight-bearing.",
              "Female pelvis is wider and shallower to accommodate childbirth."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which bone is the largest in the body?", a: "Femur." },
            { id: "c2", dok: 1, q: "Which bone of the forearm is on the thumb side?", a: "Radius." },
            { id: "c3", dok: 1, q: "How many carpal bones are in the wrist?", a: "Eight." },
            { id: "c4", dok: 1, q: "Which three bones fuse to form the coxal (hip) bone?", a: "Ilium, ischium, pubis." },
            { id: "c5", dok: 2, q: "Why does the pectoral girdle allow more arm mobility than the pelvic girdle allows leg mobility?", a: "The pectoral girdle attaches to the axial skeleton only at the sternoclavicular joint, with the scapula gliding freely on the thorax. The pelvic girdle is fused to the sacrum and locked into a weight-bearing ring, sacrificing mobility for stability." },
            { id: "c6", dok: 3, q: "A patient fractures the clavicle. Predict the change in shoulder position and why.", a: "Loss of the clavicle removes the strut that holds the scapula laterally. The shoulder drops downward and medially, pulled by gravity and the weight of the arm." }
          ]
        },

        {
          id: "t-joints-movements",
          title: "Joints and Body Movements",
          summary: "Classifying joints by structure and function, plus the vocabulary of movement.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/9-1-classification-of-joints",
          lecturePageUrl: "joints-and-movements.html",
          dayInCourse: 12,
          videoLabel: "Video: Joints and movements (pending)",
          gateKeywords: ["synovial", "hinge", "ball-and-socket", "flexion", "extension", "abduction"],
          notes: [
            { heading: "Classification by structure", body: [
              "Fibrous: bones held by collagen fibers. Sutures (skull), gomphoses (tooth-socket), syndesmoses (radius-ulna interosseous membrane).",
              "Cartilaginous: bones held by cartilage. Synchondroses (epiphyseal plate), symphyses (pubic symphysis, intervertebral discs).",
              "Synovial: bones separated by a fluid-filled cavity. Most movable joints in the body."
            ]},
            { heading: "Synovial joint types", body: [
              "Plane (carpals).",
              "Hinge (elbow, knee): one axis, flexion/extension.",
              "Pivot (atlanto-axial): rotation.",
              "Condyloid (wrist): two axes.",
              "Saddle (thumb): two axes, more freedom.",
              "Ball-and-socket (shoulder, hip): three axes, maximum freedom."
            ]},
            { heading: "Body movements", body: [
              "Flexion / extension (decrease / increase joint angle).",
              "Abduction / adduction (away from / toward midline).",
              "Rotation, circumduction.",
              "Pronation / supination (forearm).",
              "Inversion / eversion, dorsiflexion / plantarflexion (foot)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which joint type allows the most movement?", a: "Synovial." },
            { id: "c2", dok: 1, q: "Name two examples of hinge joints.", a: "Elbow, knee, interphalangeal joints." },
            { id: "c3", dok: 1, q: "What movement decreases the angle of a joint?", a: "Flexion." },
            { id: "c4", dok: 1, q: "What kind of joint is the shoulder?", a: "Ball-and-socket." },
            { id: "c5", dok: 2, q: "Why is the shoulder more dislocation-prone than the hip even though both are ball-and-socket joints?", a: "The shoulder has a shallow glenoid fossa and relies on rotator cuff muscles for stability, trading bony containment for mobility. The hip has a deep acetabulum and strong ligaments, providing far more bony and ligamentous stability." },
            { id: "c6", dok: 3, q: "A patient has rheumatoid arthritis affecting the synovial membrane. Predict the cascade of joint damage and explain why each step happens.", a: "Inflamed synovium thickens and forms a pannus that erodes articular cartilage. Cartilage loss exposes underlying bone, which then erodes. Joint capsule swells and contracts irregularly, producing joint deformity. Over time, fibrosis or bony ankylosis can fuse the joint." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 7: MUSCULAR SYSTEM
       ============================================================ */
    {
      id: "m-07-muscular",
      week: 4,
      title: "Muscular System",
      topics: [

        {
          id: "t-skeletal-muscle-microanatomy",
          title: "Skeletal Muscle Microanatomy",
          summary: "From whole muscle down to the sarcomere: the structural ladder of contractile tissue.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/10-2-skeletal-muscle",
          dayInCourse: 13,
          videoLabel: "Video: Skeletal muscle microanatomy (pending)",
          gateKeywords: ["sarcomere", "myofibril", "actin", "myosin", "sarcoplasmic reticulum"],
          notes: [
            { heading: "Structural hierarchy", body: [
              "Muscle → fascicle → muscle fiber (cell) → myofibril → sarcomere.",
              "Each level is wrapped in connective tissue: epimysium (whole), perimysium (fascicle), endomysium (fiber).",
              "Tendons are continuations of these wrappings."
            ]},
            { heading: "The sarcomere", body: [
              "Z line to Z line: the contractile unit.",
              "Thick filaments (myosin) in the center (A band).",
              "Thin filaments (actin, troponin, tropomyosin) extend from the Z line (I band).",
              "Overlap region is where cross-bridges can form."
            ]},
            { heading: "Excitation machinery", body: [
              "Sarcolemma: the muscle fiber's plasma membrane.",
              "T-tubules: deep invaginations of the sarcolemma that carry action potentials into the cell.",
              "Sarcoplasmic reticulum (SR): wraps each myofibril; stores Ca²⁺.",
              "T-tubules and SR meet at triads, where excitation triggers Ca²⁺ release."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the contractile unit of skeletal muscle?", a: "The sarcomere." },
            { id: "c2", dok: 1, q: "What protein makes up the thick filament?", a: "Myosin." },
            { id: "c3", dok: 1, q: "Where is Ca²⁺ stored in a muscle fiber?", a: "In the sarcoplasmic reticulum." },
            { id: "c4", dok: 1, q: "What do T-tubules do?", a: "Carry the action potential from the surface sarcolemma deep into the muscle fiber so that all sarcomeres are activated simultaneously." },
            { id: "c5", dok: 2, q: "Explain why the A band shortens little during contraction but the I band shortens dramatically.", a: "The A band is the length of the thick filament, which does not change. The I band is the region where only thin filaments exist; as thin filaments slide inward, the I band shrinks." },
            { id: "c6", dok: 3, q: "A toxin disrupts the triads. Predict the effect on contraction.", a: "Action potentials still propagate along the sarcolemma and T-tubules, but Ca²⁺ release from the SR is uncoupled from the T-tubule signal. Without intracellular Ca²⁺, troponin does not move tropomyosin, cross-bridges cannot form, and contraction fails." }
          ]
        },

        {
          id: "t-sliding-filament",
          title: "Sliding Filament and the Cross-Bridge Cycle",
          summary: "How calcium, ATP, actin, and myosin convert chemical energy into mechanical force.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/10-3-muscle-fiber-contraction-and-relaxation",
          lecturePageUrl: "cross-bridge-cycle.html",
          dayInCourse: 14,
          videoLabel: "Video: Sliding filament theory (pending)",
          gateKeywords: ["sliding filament", "cross-bridge", "calcium", "troponin", "tropomyosin", "ATP"],
          notes: [
            { heading: "The trigger: calcium release", body: [
              "Action potential at the neuromuscular junction releases ACh; ACh opens nicotinic receptors; sarcolemma depolarizes.",
              "Depolarization sweeps along T-tubules to the SR.",
              "SR releases Ca²⁺ into the cytoplasm."
            ]},
            { heading: "The cross-bridge cycle (4 steps)", body: [
              "1. Cocking: ATP is hydrolyzed; myosin head reorients into a high-energy position.",
              "2. Binding: Ca²⁺ binds troponin; tropomyosin shifts; the actin-binding site is exposed; myosin binds actin (cross-bridge forms).",
              "3. Power stroke: myosin pivots, pulling actin toward the M-line. ADP and Pi are released.",
              "4. Detachment: a new ATP binds myosin, which releases actin and the cycle repeats."
            ]},
            { heading: "Relaxation", body: [
              "When neural input stops, ACh is broken down and the sarcolemma repolarizes.",
              "SR Ca²⁺ ATPase pumps Ca²⁺ back into the SR.",
              "Troponin returns to its resting position, tropomyosin re-blocks actin sites, and cross-bridges cannot form."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What ion is the direct trigger for cross-bridge formation?", a: "Calcium (Ca²⁺)." },
            { id: "c2", dok: 1, q: "What protein does Ca²⁺ bind to inside the sarcomere?", a: "Troponin." },
            { id: "c3", dok: 1, q: "What happens to tropomyosin when troponin binds calcium?", a: "Tropomyosin shifts and uncovers the myosin-binding sites on actin." },
            { id: "c4", dok: 1, q: "When in the cross-bridge cycle is ATP hydrolyzed?", a: "During the cocking step, before the power stroke." },
            { id: "c5", dok: 1, q: "When in the cycle is ATP required for detachment?", a: "A fresh ATP must bind myosin to release it from actin after the power stroke." },
            { id: "c6", dok: 2, q: "Explain rigor mortis using the cross-bridge cycle.", a: "After death, ATP production stops. Without ATP, myosin cannot detach from actin. Cross-bridges remain locked, and muscles become rigid." },
            { id: "c7", dok: 2, q: "Predict what happens to muscle force if intracellular Ca²⁺ rises but ATP runs out.", a: "Cross-bridges can form (Ca²⁺ exposes actin sites) but cannot cycle (no ATP for cocking or detachment). The muscle locks into a contracted state and force production stops." },
            { id: "c8", dok: 2, q: "Why does curare cause muscle paralysis?", a: "Curare blocks nicotinic ACh receptors at the neuromuscular junction. The sarcolemma cannot depolarize, T-tubules do not trigger SR Ca²⁺ release, and contraction cannot start." },
            { id: "c9", dok: 3, q: "A patient is poisoned with sarin (an acetylcholinesterase inhibitor). Predict the effect at the neuromuscular junction across time.", a: "ACh is not broken down. It accumulates and continuously activates the sarcolemma. Initial response: prolonged contraction and fasciculations. Later: receptors desensitize, depolarization block sets in, and the muscle becomes paralyzed (including respiratory muscles)." },
            { id: "c10", dok: 3, q: "Malignant hyperthermia is caused by a mutation that makes the SR Ca²⁺ release channel hyperactive in response to certain anesthetics. Predict the patient's presentation and explain why.", a: "Unregulated Ca²⁺ release continuously activates cross-bridges. The muscle contracts continuously, generating heat (temperature climbs rapidly) and consuming ATP. ATP depletion leads to muscle damage (rhabdomyolysis), acidosis, hyperkalemia, and, if untreated, death." }
          ]
        },

        {
          id: "t-motor-units",
          title: "Motor Units and Muscle Mechanics",
          summary: "Motor unit organization, recruitment, summation, and fatigue.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/10-4-nervous-system-control-of-muscle-tension",
          lecturePageUrl: "motor-units.html",
          dayInCourse: 13,
          videoLabel: "Video: Motor units (pending)",
          gateKeywords: ["motor unit", "recruitment", "twitch", "summation", "tetanus"],
          notes: [
            { heading: "Motor unit", body: [
              "One motor neuron + all the muscle fibers it innervates.",
              "Small motor units (a few fibers) = fine control (eye muscles).",
              "Large motor units (many fibers) = power (quadriceps)."
            ]},
            { heading: "Grading force", body: [
              "Recruitment: activate more motor units to increase force (Henneman size principle, small units first).",
              "Frequency summation: fire each motor unit faster; twitches add up.",
              "Tetanus: stimulation so frequent twitches fuse into a smooth, sustained contraction."
            ]},
            { heading: "Fatigue and fiber types", body: [
              "Type I (slow oxidative): fatigue-resistant, postural muscles.",
              "Type IIa (fast oxidative): intermediate.",
              "Type IIx (fast glycolytic): powerful, fatigue quickly."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Define a motor unit.", a: "One motor neuron and all the muscle fibers it innervates." },
            { id: "c2", dok: 1, q: "Which fiber type is most fatigue-resistant?", a: "Type I (slow oxidative)." },
            { id: "c3", dok: 1, q: "What is tetanus in the muscle physiology sense?", a: "A smooth, sustained contraction produced when stimulation frequency is too high for the muscle to relax between twitches." },
            { id: "c4", dok: 1, q: "Which is recruited first, small or large motor units?", a: "Small (size principle)." },
            { id: "c5", dok: 2, q: "Why are eye muscles innervated by very small motor units?", a: "Eye movements require fine, precise control. Small motor units (a few fibers each) let the nervous system grade force in small increments for smooth tracking." },
            { id: "c6", dok: 3, q: "A sprinter trains for explosive power; a marathoner trains for endurance. Predict the dominant muscle fiber adaptations in each.", a: "Sprinter: hypertrophy of Type IIx (fast glycolytic) fibers and improved anaerobic capacity. Marathoner: shift toward more Type I (slow oxidative) characteristics, increased mitochondria and capillary density, enhanced fatigue resistance." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 8: NERVOUS SYSTEM
       ============================================================ */
    {
      id: "m-08-nervous",
      week: 4,
      title: "Nervous System",
      topics: [

        {
          id: "t-neurons-rmp",
          title: "Neurons and Resting Membrane Potential",
          summary: "Neuron anatomy and how the resting potential is built and maintained.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/12-2-nervous-tissue",
          lecturePageUrl: "neurons-resting-potential.html",
          dayInCourse: 15,
          videoLabel: "Video: Neurons and resting potential (pending)",
          gateKeywords: ["neuron", "axon", "dendrite", "resting potential", "sodium-potassium pump"],
          notes: [
            { heading: "Neuron anatomy", body: [
              "Dendrites: receive signals.",
              "Cell body (soma): integrates signals; houses the nucleus.",
              "Axon: conducts action potentials.",
              "Axon terminal: releases neurotransmitter."
            ]},
            { heading: "Resting membrane potential (about −70 mV)", body: [
              "Inside is negative relative to outside.",
              "Maintained by the Na⁺/K⁺ ATPase (3 Na⁺ out, 2 K⁺ in) plus K⁺ leak channels.",
              "Result: high K⁺ inside, high Na⁺ outside; membrane is mostly permeable to K⁺ at rest."
            ]},
            { heading: "Glia", body: [
              "CNS: astrocytes (BBB, metabolic support), oligodendrocytes (myelin), microglia (immune), ependymal (CSF).",
              "PNS: Schwann cells (myelin), satellite cells (support cell bodies in ganglia)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the typical resting membrane potential of a neuron?", a: "About −70 mV (inside negative)." },
            { id: "c2", dok: 1, q: "Which ions does the Na⁺/K⁺ ATPase pump and in what direction?", a: "Three Na⁺ out, two K⁺ in, per ATP." },
            { id: "c3", dok: 1, q: "Which part of the neuron conducts the action potential away from the cell body?", a: "The axon." },
            { id: "c4", dok: 1, q: "Which CNS glial cell makes myelin?", a: "Oligodendrocyte." },
            { id: "c5", dok: 2, q: "Why is the resting potential negative rather than zero?", a: "K⁺ leak channels let K⁺ flow out down its gradient, leaving anions behind. The Na⁺/K⁺ pump also exports more positive charge than it imports. Together this builds a negative interior." },
            { id: "c6", dok: 3, q: "Ouabain blocks the Na⁺/K⁺ ATPase. Predict the effect on the resting potential of a neuron over minutes to hours.", a: "Initially the resting potential is unchanged because the pump's direct electrogenic contribution is small. Over time, the Na⁺ and K⁺ gradients dissipate. K⁺ leak channels lose their driving force, and the cell depolarizes toward 0 mV, becoming unable to fire action potentials." }
          ]
        },

        {
          id: "t-action-potentials",
          title: "Action Potentials and Synaptic Transmission",
          summary: "Phases of an action potential, propagation, and how chemical synapses pass the signal on.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/12-4-the-action-potential",
          lecturePageUrl: "action-potentials-synapses.html",
          dayInCourse: 16,
          videoLabel: "Video: Action potentials (pending)",
          gateKeywords: ["depolarization", "repolarization", "threshold", "neurotransmitter", "synapse"],
          notes: [
            { heading: "The action potential (AP)", body: [
              "Resting: about −70 mV.",
              "Depolarization to threshold (about −55 mV) opens voltage-gated Na⁺ channels; Na⁺ rushes in; membrane swings to about +30 mV.",
              "Repolarization: Na⁺ channels inactivate; voltage-gated K⁺ channels open; K⁺ rushes out.",
              "Hyperpolarization (afterhyperpolarization): K⁺ channels close slowly; membrane briefly dips below −70 mV.",
              "All-or-none: any suprathreshold stimulus produces the same-size AP."
            ]},
            { heading: "Propagation", body: [
              "Continuous in unmyelinated axons (slow).",
              "Saltatory in myelinated axons: AP jumps from node of Ranvier to node, much faster.",
              "Refractory periods prevent backward propagation."
            ]},
            { heading: "Chemical synapse", body: [
              "AP reaches the axon terminal.",
              "Voltage-gated Ca²⁺ channels open; Ca²⁺ flows in.",
              "Synaptic vesicles fuse with the presynaptic membrane and release neurotransmitter into the cleft.",
              "Neurotransmitter binds receptors on the postsynaptic membrane, producing an EPSP or IPSP.",
              "Signal is terminated by reuptake, enzymatic breakdown, or diffusion away."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "At what membrane potential does the typical neuron's threshold sit?", a: "About −55 mV." },
            { id: "c2", dok: 1, q: "What ion enters during depolarization?", a: "Sodium (Na⁺)." },
            { id: "c3", dok: 1, q: "What ion exits during repolarization?", a: "Potassium (K⁺)." },
            { id: "c4", dok: 1, q: "What does 'all-or-none' mean for action potentials?", a: "Either a full-size AP is produced (above threshold) or none is (below threshold). Larger stimuli do not produce larger APs." },
            { id: "c5", dok: 1, q: "Which ion triggers neurotransmitter release at the axon terminal?", a: "Calcium (Ca²⁺)." },
            { id: "c6", dok: 2, q: "Explain why saltatory conduction is faster than continuous conduction.", a: "In myelinated axons, voltage-gated channels cluster at nodes of Ranvier. The AP regenerates only at nodes, effectively jumping between them rather than depolarizing every patch of membrane in sequence." },
            { id: "c7", dok: 2, q: "Why are action potentials usually unidirectional along an axon?", a: "After firing, the recently active region enters its absolute refractory period because Na⁺ channels are inactivated. The AP can only propagate forward into membrane that has not yet fired." },
            { id: "c8", dok: 2, q: "Compare an EPSP and an IPSP.", a: "EPSP: depolarizes the postsynaptic neuron, brings it closer to threshold. IPSP: hyperpolarizes (or stabilizes) it, moves it away from threshold. Both summate at the axon hillock to decide whether an AP fires." },
            { id: "c9", dok: 3, q: "Multiple sclerosis demyelinates CNS axons. Predict the conduction consequences and the symptom pattern.", a: "Without myelin, saltatory conduction fails. Voltage-gated channels are sparse between nodes, so APs may attenuate or fail entirely. Symptoms vary by tract: vision changes (optic nerve), weakness, sensory loss, coordination problems. Recovery between episodes occurs because some axons remain or partially remyelinate, but disability accumulates." },
            { id: "c10", dok: 3, q: "A patient is given an SSRI for depression. Mechanistically, why might the antidepressant effect take weeks to appear?", a: "The SSRI immediately blocks serotonin reuptake, raising synaptic serotonin. The slower effect comes from downstream changes: receptor desensitization, altered gene expression, neuroplastic remodeling. These take weeks, which is why clinical effects lag the pharmacology." },
            { id: "c11", dok: 3, q: "Black widow venom causes massive ACh release at neuromuscular junctions, while botulinum toxin blocks ACh release entirely. Compare the muscular effects and explain why each occurs.", a: "Black widow: continuous ACh release causes sustained depolarization, painful cramping, then exhaustion of vesicles and weakness. Botulinum: no ACh release, so no depolarization, producing flaccid paralysis. Both can kill via respiratory muscle failure but by opposite mechanisms." },
            { id: "c12", dok: 3, q: "A drug specifically blocks voltage-gated Na⁺ channels in sensory nerves but not motor nerves. Predict the clinical effect and explain.", a: "Sensory neurons cannot generate APs, so the patient loses sensation (pain, touch, temperature) in the distribution served. Motor function is preserved because motor axons still fire. This selective profile is the basis of local anesthetics dosed for analgesia without paralysis." }
          ]
        },

        {
          id: "t-cns-organization",
          title: "CNS Organization: Brain and Spinal Cord",
          summary: "Brain regions and lobes, meninges, ventricles, and spinal cord anatomy.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/13-2-the-central-nervous-system",
          lecturePageUrl: "cns-organization.html",
          dayInCourse: 17,
          videoLabel: "Video: CNS organization (pending)",
          gateKeywords: ["cerebrum", "cerebellum", "brainstem", "spinal cord", "meninges"],
          notes: [
            { heading: "Brain regions", body: [
              "Cerebrum: two hemispheres, four lobes (frontal, parietal, temporal, occipital). Cortex (gray matter) over white matter.",
              "Diencephalon: thalamus (sensory relay), hypothalamus (homeostasis), epithalamus (pineal).",
              "Brainstem: midbrain, pons, medulla. Cranial nerves III-XII; vital reflex centers.",
              "Cerebellum: motor coordination, balance, motor learning."
            ]},
            { heading: "Functional cortex landmarks", body: [
              "Frontal lobe: primary motor cortex (precentral gyrus), executive function.",
              "Parietal lobe: primary somatosensory cortex (postcentral gyrus).",
              "Temporal lobe: auditory cortex, language comprehension (Wernicke).",
              "Occipital lobe: primary visual cortex.",
              "Broca area (frontal): speech production."
            ]},
            { heading: "Coverings and fluid", body: [
              "Meninges (outer to inner): dura, arachnoid, pia.",
              "CSF fills ventricles and subarachnoid space, made by choroid plexus, drained by arachnoid villi.",
              "Spinal cord runs from medulla to L1-L2; central canal continues CSF flow."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the four lobes of the cerebrum.", a: "Frontal, parietal, temporal, occipital." },
            { id: "c2", dok: 1, q: "Where is the primary motor cortex?", a: "Precentral gyrus of the frontal lobe." },
            { id: "c3", dok: 1, q: "Name the three meningeal layers from outer to inner.", a: "Dura mater, arachnoid mater, pia mater." },
            { id: "c4", dok: 1, q: "Where is CSF produced?", a: "Choroid plexuses in the ventricles." },
            { id: "c5", dok: 2, q: "Why does damage to the cerebellum produce coordination problems without paralysis?", a: "The cerebellum modulates motor commands generated elsewhere; it does not generate them. Damage leaves the motor pathways intact (no paralysis) but removes coordination, smoothing, and timing." },
            { id: "c6", dok: 3, q: "A stroke damages the left middle cerebral artery territory in a right-handed patient. Predict the deficits and explain why each occurs.", a: "Right-sided weakness (left motor cortex damaged, contralateral control). Right-sided sensory loss (left somatosensory cortex). Language impairment because Broca and Wernicke areas are usually left-hemispheric in right-handed people. Likely also right-sided visual field cut depending on extent." }
          ]
        },

        {
          id: "t-pns-autonomic",
          title: "PNS and Autonomic Nervous System",
          summary: "Cranial and spinal nerves, reflex arcs, and the sympathetic vs parasympathetic divisions.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/15-1-divisions-of-the-autonomic-nervous-system",
          lecturePageUrl: "pns-autonomic.html",
          dayInCourse: 18,
          videoLabel: "Video: PNS and autonomic NS (pending)",
          gateKeywords: ["sympathetic", "parasympathetic", "cranial nerves", "reflex", "ganglion"],
          notes: [
            { heading: "PNS structure", body: [
              "12 pairs of cranial nerves (mostly head/neck; vagus is the long exception).",
              "31 pairs of spinal nerves (each with sensory and motor fibers).",
              "Somatic motor: voluntary control of skeletal muscle.",
              "Autonomic motor: involuntary control of smooth muscle, cardiac muscle, glands."
            ]},
            { heading: "Reflex arc (5 components)", body: [
              "Receptor.",
              "Sensory neuron.",
              "Integration center (often spinal cord).",
              "Motor neuron.",
              "Effector."
            ]},
            { heading: "Sympathetic vs parasympathetic", body: [
              "Sympathetic: 'fight or flight.' Thoracolumbar (T1-L2) origin. Short pre-ganglionic, long post-ganglionic. Norepinephrine at most targets.",
              "Parasympathetic: 'rest and digest.' Craniosacral origin (CN III, VII, IX, X plus S2-S4). Long pre-, short post-ganglionic. Acetylcholine at targets.",
              "Most organs receive both, with one dominating depending on state."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which cranial nerve has the broadest parasympathetic distribution?", a: "Vagus (CN X)." },
            { id: "c2", dok: 1, q: "List the five components of a reflex arc.", a: "Receptor, sensory neuron, integration center, motor neuron, effector." },
            { id: "c3", dok: 1, q: "What neurotransmitter does the sympathetic nervous system release at most target organs?", a: "Norepinephrine." },
            { id: "c4", dok: 1, q: "How many pairs of spinal nerves are there?", a: "31." },
            { id: "c5", dok: 2, q: "Predict the sympathetic effects of an adrenaline surge during a fight-or-flight response.", a: "Heart rate and contractility rise. Bronchi dilate. Pupils dilate. Sweat glands activate. Blood is shunted to skeletal muscle; gut motility and glandular secretion fall. Glycogen breakdown rises, raising blood glucose." },
            { id: "c6", dok: 3, q: "A patient with a spinal cord transection at C5 retains some reflexes below the lesion but cannot move voluntarily. Explain why both observations make sense.", a: "Voluntary movement requires descending tracts from the motor cortex through the spinal cord. The transection severs these, so no voluntary movement below the lesion. Reflex arcs depend only on local spinal circuitry (receptor → sensory → spinal cord → motor → effector), which remains intact below the lesion." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 9: SPECIAL SENSES
       ============================================================ */
    {
      id: "m-09-special-senses",
      week: 5,
      title: "Special Senses",
      topics: [

        {
          id: "t-vision",
          title: "Vision",
          summary: "Eye anatomy, accommodation, and photoreceptor function.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception",
          dayInCourse: 19,
          videoLabel: "Video: Vision (pending)",
          gateKeywords: ["retina", "rod", "cone", "lens", "photoreceptor"],
          notes: [
            { heading: "Eye anatomy", body: [
              "Cornea: most of the eye's focusing power (fixed).",
              "Lens: adjustable focusing (accommodation).",
              "Retina: contains photoreceptors. Fovea = highest acuity (all cones, no overlying neurons).",
              "Optic nerve (CN II): leaves the eye through the optic disc (blind spot)."
            ]},
            { heading: "Accommodation", body: [
              "Near vision: ciliary muscle contracts, zonular fibers slacken, lens rounds up for stronger refraction.",
              "Far vision: ciliary muscle relaxes, zonules pull lens flatter."
            ]},
            { heading: "Phototransduction", body: [
              "Rods: highly sensitive, no color, dominate at low light.",
              "Cones: less sensitive, three types for red/green/blue, fine detail, color, daylight.",
              "Light hits rhodopsin (rods) or cone opsins, triggers a cascade that hyperpolarizes the photoreceptor.",
              "Photoreceptors release less glutamate in light, which is interpreted downstream as a visual signal."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which photoreceptor is responsible for color vision?", a: "Cones." },
            { id: "c2", dok: 1, q: "Where is the area of sharpest vision in the retina?", a: "The fovea." },
            { id: "c3", dok: 1, q: "Which structure provides most of the eye's fixed refractive power?", a: "The cornea." },
            { id: "c4", dok: 2, q: "Why is the optic disc a 'blind spot'?", a: "It is where the optic nerve exits the retina. No photoreceptors are present, so light hitting that spot generates no signal." },
            { id: "c5", dok: 2, q: "Explain why night vision is mostly black and white.", a: "Rods dominate at low light, but rods do not encode color. Cones, which encode color, are not sensitive enough to fire in dim light." },
            { id: "c6", dok: 3, q: "A patient is diagnosed with presbyopia (loss of near vision with age). Explain the mechanism.", a: "With age, the lens becomes less elastic. The ciliary muscle can still contract, but the lens no longer rounds up enough during accommodation. Near objects cannot be focused on the retina, requiring reading glasses." }
          ]
        },

        {
          id: "t-hearing-equilibrium",
          title: "Hearing and Equilibrium",
          summary: "Cochlear transduction of sound and vestibular detection of head motion.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception",
          lecturePageUrl: "hearing-equilibrium.html",
          dayInCourse: 19,
          videoLabel: "Video: Hearing and equilibrium (pending)",
          gateKeywords: ["cochlea", "hair cell", "vestibule", "semicircular canal", "organ of Corti"],
          notes: [
            { heading: "Sound path", body: [
              "Outer ear: pinna and external auditory canal channel sound to the tympanic membrane.",
              "Middle ear: tympanic membrane vibrates malleus → incus → stapes. Stapes pushes on the oval window.",
              "Inner ear: pressure waves travel through perilymph in the cochlea."
            ]},
            { heading: "Cochlear transduction", body: [
              "Basilar membrane vibrates; different frequencies peak at different positions (tonotopy).",
              "Hair cells in the organ of Corti have stereocilia bent by basilar membrane motion.",
              "Bending opens mechanically gated K⁺ channels; hair cell depolarizes; releases glutamate onto CN VIII."
            ]},
            { heading: "Equilibrium", body: [
              "Vestibule (saccule and utricle): linear acceleration and head tilt; otolith organs.",
              "Three semicircular canals: angular (rotational) acceleration.",
              "All use hair cells with stereocilia in a gel-like medium."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the three middle ear ossicles in order.", a: "Malleus, incus, stapes." },
            { id: "c2", dok: 1, q: "Which structure contains the hair cells for hearing?", a: "The organ of Corti (on the basilar membrane within the cochlea)." },
            { id: "c3", dok: 1, q: "Which structures detect rotational acceleration?", a: "Semicircular canals." },
            { id: "c4", dok: 2, q: "Why does damage to high-frequency hair cells at the base of the cochlea cause age-related hearing loss?", a: "High frequencies are encoded at the base of the basilar membrane, which receives the most vibration over a lifetime. Cumulative damage to these hair cells leads to high-frequency hearing loss (presbycusis)." },
            { id: "c5", dok: 3, q: "A patient with vertigo has loose calcium carbonate crystals (otoconia) drifting into a semicircular canal. Predict the symptom pattern and explain why.", a: "Head movements displace the wandering otoconia, abnormally bending hair cells in the canal. The brain interprets this as ongoing rotation when there is none, producing brief episodes of spinning vertigo triggered by position change (benign paroxysmal positional vertigo, BPPV)." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 10: ENDOCRINE SYSTEM
       ============================================================ */
    {
      id: "m-10-endocrine",
      week: 5,
      title: "Endocrine System",
      topics: [

        {
          id: "t-hormone-mechanisms",
          title: "Hormone Mechanisms",
          summary: "Steroid vs peptide vs amino-acid-derived hormones, and how each transduces a signal.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/17-2-hormones",
          lecturePageUrl: "hormone-mechanisms.html",
          dayInCourse: 20,
          videoLabel: "Video: Hormone mechanisms (pending)",
          gateKeywords: ["hormone", "receptor", "second messenger", "steroid", "peptide"],
          notes: [
            { heading: "Hormone classes", body: [
              "Steroid: derived from cholesterol; lipid-soluble; cross membranes (cortisol, sex steroids, aldosterone).",
              "Peptide / protein: water-soluble; cannot cross membranes (insulin, growth hormone).",
              "Amino-acid-derived: thyroid hormone (lipid-soluble) and catecholamines (water-soluble)."
            ]},
            { heading: "Signal transduction", body: [
              "Lipid-soluble: cross plasma membrane, bind intracellular receptors, act as transcription factors. Slow, long-lasting effects.",
              "Water-soluble: bind surface receptors; trigger second messengers (cAMP, IP3/DAG, Ca²⁺). Fast, transient effects."
            ]},
            { heading: "Feedback", body: [
              "Most endocrine axes use negative feedback to stabilize hormone levels.",
              "Long-loop negative feedback: end-hormone suppresses hypothalamus and anterior pituitary (e.g., cortisol feeds back on CRH and ACTH).",
              "Disorders often emerge when the feedback is broken (primary, secondary, or tertiary failure)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Where are steroid hormone receptors located?", a: "Inside the cell (cytoplasm or nucleus)." },
            { id: "c2", dok: 1, q: "Name the second messenger triggered by many peptide hormones.", a: "Cyclic AMP (cAMP)." },
            { id: "c3", dok: 1, q: "Which hormone class generally acts faster: steroid or peptide?", a: "Peptide (second messenger cascades act in seconds; steroid effects via gene transcription take hours)." },
            { id: "c4", dok: 2, q: "Explain why peptide hormones must be administered by injection (not orally).", a: "Peptide hormones are proteins. They would be digested by gastric and intestinal proteases if swallowed. Injection bypasses the GI tract." },
            { id: "c5", dok: 3, q: "A patient with autoimmune destruction of the adrenal cortex (primary adrenal insufficiency) presents with high ACTH levels. Explain.", a: "The damaged cortex cannot make cortisol. Without cortisol, the long-loop negative feedback on the pituitary is lost. The pituitary releases ACTH unchecked, producing high ACTH levels (and the skin hyperpigmentation associated with elevated POMC-derived peptides)." }
          ]
        },

        {
          id: "t-major-glands",
          title: "Major Endocrine Glands",
          summary: "Pituitary, thyroid, parathyroid, adrenal, pancreas, gonads: who makes what and what it does.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/17-1-an-overview-of-the-endocrine-system",
          lecturePageUrl: "major-endocrine-glands.html",
          dayInCourse: 20,
          videoLabel: "Video: Major endocrine glands (pending)",
          gateKeywords: ["pituitary", "thyroid", "adrenal", "pancreas", "insulin"],
          notes: [
            { heading: "Pituitary", body: [
              "Anterior pituitary: TSH, ACTH, FSH, LH, GH, prolactin. Regulated by hypothalamic releasing hormones.",
              "Posterior pituitary: ADH (water reabsorption) and oxytocin. Made in hypothalamus, stored and released here."
            ]},
            { heading: "Thyroid and parathyroid", body: [
              "Thyroid: T3 and T4 (metabolic rate). Calcitonin (lowers blood Ca²⁺, modest effect in adults).",
              "Parathyroid: PTH raises blood Ca²⁺ (bone resorption, renal Ca²⁺ retention, activates vitamin D)."
            ]},
            { heading: "Adrenal, pancreas, gonads", body: [
              "Adrenal cortex: cortisol (stress, metabolism), aldosterone (Na⁺ retention), androgens.",
              "Adrenal medulla: epinephrine and norepinephrine (sympathetic effector).",
              "Pancreas (islets): insulin (lowers glucose), glucagon (raises glucose).",
              "Gonads: testosterone (testes), estrogen and progesterone (ovaries)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which gland releases ADH?", a: "The posterior pituitary (synthesized by the hypothalamus, stored and released by the posterior pituitary)." },
            { id: "c2", dok: 1, q: "Name the two main hormones of the pancreatic islets and what they do.", a: "Insulin lowers blood glucose; glucagon raises it." },
            { id: "c3", dok: 1, q: "What hormone raises blood Ca²⁺?", a: "Parathyroid hormone (PTH)." },
            { id: "c4", dok: 1, q: "Which adrenal layer makes aldosterone?", a: "Zona glomerulosa of the adrenal cortex." },
            { id: "c5", dok: 2, q: "Type 1 diabetes is caused by autoimmune destruction of pancreatic beta cells. Explain the resulting hyperglycemia mechanistically.", a: "Beta cells make insulin. Without insulin, cells cannot take up glucose efficiently and the liver continues to release glucose. Blood glucose rises and stays high, producing osmotic diuresis, dehydration, and eventually ketoacidosis." },
            { id: "c6", dok: 3, q: "Cushing syndrome features high cortisol. Predict three findings and tie them to cortisol's actions.", a: "Hyperglycemia (cortisol promotes gluconeogenesis and inhibits glucose uptake). Central obesity and muscle wasting (cortisol breaks down peripheral protein and redistributes fat). Immunosuppression and poor wound healing (cortisol suppresses immune function and collagen synthesis). Hypertension is also common (cortisol has weak mineralocorticoid activity)." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 11: BLOOD
       ============================================================ */
    {
      id: "m-11-blood",
      week: 6,
      title: "Blood",
      topics: [

        {
          id: "t-blood-composition",
          title: "Blood Composition and Hemopoiesis",
          summary: "Plasma, formed elements, and how blood cells are made in red marrow.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/18-1-functions-of-blood",
          lecturePageUrl: "blood-composition.html",
          dayInCourse: 21,
          videoLabel: "Video: Blood composition (pending)",
          gateKeywords: ["plasma", "erythrocyte", "hemoglobin", "leukocyte", "platelet"],
          notes: [
            { heading: "Composition", body: [
              "Plasma (~55%): mostly water, plus proteins (albumin, globulins, fibrinogen), electrolytes, glucose, hormones, wastes.",
              "Formed elements (~45%): erythrocytes (RBCs, ~99% of cells), leukocytes (WBCs), platelets."
            ]},
            { heading: "Red blood cells", body: [
              "Biconcave disc, no nucleus, packed with hemoglobin.",
              "~120-day lifespan.",
              "Function: O₂ and CO₂ transport."
            ]},
            { heading: "White blood cells and platelets", body: [
              "Granulocytes: neutrophils (bacterial), eosinophils (parasites/allergy), basophils (inflammation).",
              "Agranulocytes: lymphocytes (adaptive immunity), monocytes (mature into macrophages).",
              "Platelets: cell fragments from megakaryocytes; central to clotting."
            ]},
            { heading: "Hemopoiesis", body: [
              "Red marrow of axial and proximal limb bones.",
              "Hematopoietic stem cells give rise to all blood cell lineages.",
              "Erythropoietin (EPO, from kidneys) drives red cell production in response to low O₂."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What percentage of blood is plasma?", a: "About 55%." },
            { id: "c2", dok: 1, q: "Name the most abundant leukocyte.", a: "Neutrophil." },
            { id: "c3", dok: 1, q: "What is the lifespan of a red blood cell?", a: "About 120 days." },
            { id: "c4", dok: 1, q: "Where is erythropoietin made?", a: "Kidney (peritubular cells)." },
            { id: "c5", dok: 2, q: "Why do RBCs lack a nucleus?", a: "Removing the nucleus maximizes hemoglobin packing and the biconcave shape, both of which favor gas transport and deformability through capillaries. The trade-off is no protein synthesis and a finite lifespan." },
            { id: "c6", dok: 3, q: "A patient with chronic kidney disease is anemic. Connect the kidney failure to the anemia.", a: "Damaged kidneys make less erythropoietin. Without enough EPO signal, the bone marrow underproduces erythrocytes. RBC mass falls, oxygen-carrying capacity drops, and anemia results. Treatment often includes recombinant EPO." }
          ]
        },

        {
          id: "t-hemostasis-blood-typing",
          title: "Hemostasis and Blood Typing",
          summary: "Stopping bleeding in three steps, and the basics of ABO and Rh.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/18-5-hemostasis",
          lecturePageUrl: "hemostasis-blood-typing.html",
          dayInCourse: 21,
          videoLabel: "Video: Hemostasis and typing (pending)",
          gateKeywords: ["hemostasis", "platelet plug", "fibrin", "ABO", "Rh"],
          notes: [
            { heading: "Three phases of hemostasis", body: [
              "Vascular spasm: damaged vessel constricts.",
              "Platelet plug: platelets adhere to exposed collagen (via vWF), activate, recruit more platelets.",
              "Coagulation: clotting cascade (intrinsic and extrinsic pathways converge on the common pathway) ends in fibrin polymerization, reinforcing the plug."
            ]},
            { heading: "ABO blood typing", body: [
              "Antigens on RBC surface (A, B, both, or neither = O).",
              "Antibodies in plasma against absent antigens (Type A has anti-B; Type O has both; Type AB has neither).",
              "Type O is the universal RBC donor; Type AB is the universal recipient."
            ]},
            { heading: "Rh factor", body: [
              "Rh+ = D antigen present.",
              "Anti-Rh antibodies form only after exposure (transfusion or pregnancy).",
              "Rh-incompatibility during pregnancy: Rh− mother carrying Rh+ baby may produce anti-Rh antibodies that attack a subsequent Rh+ fetus (hemolytic disease of the newborn). Rh immunoglobulin (RhoGAM) prevents this."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the three phases of hemostasis.", a: "Vascular spasm, platelet plug formation, coagulation." },
            { id: "c2", dok: 1, q: "Which protein is the final product of the coagulation cascade?", a: "Fibrin." },
            { id: "c3", dok: 1, q: "Which blood type is the universal RBC donor?", a: "Type O (no A or B antigens on RBCs)." },
            { id: "c4", dok: 1, q: "Which blood type is the universal plasma donor?", a: "Type AB (no anti-A or anti-B antibodies in plasma)." },
            { id: "c5", dok: 2, q: "Why are Rh− women given RhoGAM during and after pregnancy?", a: "If the fetus is Rh+, fetal blood entering maternal circulation could sensitize the mother to make anti-Rh antibodies. In a future Rh+ pregnancy these antibodies could cross the placenta and attack the fetus. RhoGAM neutralizes fetal Rh+ cells in the mother before her immune system mounts a response." },
            { id: "c6", dok: 3, q: "A patient with severe liver disease has prolonged bleeding times. Explain mechanistically.", a: "The liver synthesizes most clotting factors (II, VII, IX, X, fibrinogen, and others). With hepatic failure, factor levels drop. The cascade slows or stalls, fibrin formation is delayed, and bleeding times prolong." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 12: CARDIOVASCULAR SYSTEM
       ============================================================ */
    {
      id: "m-12-cardiovascular",
      week: 6,
      title: "Cardiovascular System",
      topics: [

        {
          id: "t-heart-cardiac-cycle",
          title: "Heart Anatomy and the Cardiac Cycle",
          summary: "Chambers, valves, great vessels, and the pressure-volume story of one heartbeat.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy",
          lecturePageUrl: "heart-anatomy.html",
          dayInCourse: 22,
          videoLabel: "Video: Heart anatomy and cycle (pending)",
          gateKeywords: ["atrium", "ventricle", "valve", "systole", "diastole"],
          notes: [
            { heading: "Chambers and valves", body: [
              "Right side: deoxygenated. RA receives from SVC/IVC, sends through tricuspid to RV, then through pulmonary valve to pulmonary trunk and lungs.",
              "Left side: oxygenated. LA receives from pulmonary veins, sends through bicuspid (mitral) to LV, then through aortic valve to aorta.",
              "AV valves (tricuspid, mitral) prevent backflow into atria during systole.",
              "Semilunar valves (pulmonary, aortic) prevent backflow from arteries during diastole."
            ]},
            { heading: "Cardiac cycle phases", body: [
              "Ventricular filling: AV valves open, ventricles fill passively, then atrial contraction tops them off.",
              "Isovolumetric contraction: all valves closed, ventricular pressure rises rapidly.",
              "Ventricular ejection: semilunar valves open, blood is ejected.",
              "Isovolumetric relaxation: all valves closed, ventricular pressure falls. When it drops below atrial pressure, the AV valves open and filling begins again."
            ]},
            { heading: "Heart sounds", body: [
              "S1 ('lub'): AV valves closing at the start of systole.",
              "S2 ('dub'): semilunar valves closing at the end of systole.",
              "S3, S4: extra sounds; can be normal (young athletes) or pathologic (heart failure)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which valves close at the start of ventricular systole?", a: "The atrioventricular (tricuspid and mitral) valves." },
            { id: "c2", dok: 1, q: "Which valves close at the end of ventricular systole?", a: "The semilunar (aortic and pulmonary) valves." },
            { id: "c3", dok: 1, q: "What is happening during isovolumetric contraction?", a: "All four valves are closed; ventricles contract and pressure rises sharply without any volume change." },
            { id: "c4", dok: 1, q: "Which side of the heart pumps oxygenated blood?", a: "The left side." },
            { id: "c5", dok: 1, q: "Which sound (S1 or S2) marks the beginning of systole?", a: "S1." },
            { id: "c6", dok: 2, q: "Why does ventricular volume not change during isovolumetric contraction?", a: "All four valves are closed. Blood cannot leave the ventricle or enter it, but the muscle is contracting, so pressure climbs while volume holds steady." },
            { id: "c7", dok: 2, q: "Predict the consequence of a leaky mitral valve (mitral regurgitation).", a: "During ventricular systole, some blood flows backward into the left atrium instead of forward into the aorta. Forward cardiac output drops; left atrial pressure rises; over time pulmonary congestion develops, and the left ventricle dilates from chronic volume overload." },
            { id: "c8", dok: 2, q: "Why does aortic stenosis lead to left ventricular hypertrophy?", a: "Narrow aortic valve increases the pressure the LV must generate to eject blood. Chronic pressure overload triggers concentric hypertrophy: sarcomeres added in parallel, wall thickens, chamber radius preserved." },
            { id: "c9", dok: 3, q: "A patient has heart failure with reduced ejection fraction (EF = 25%). Explain the term and predict three downstream consequences.", a: "Ejection fraction = stroke volume / end-diastolic volume. 25% means only a quarter of the LV blood is ejected per beat. Consequences: fatigue and exercise intolerance (low forward output), pulmonary congestion (blood backs up into pulmonary circuit), and activation of compensatory systems (sympathetic and RAAS) that initially help but worsen the disease over time." },
            { id: "c10", dok: 3, q: "Predict the effect on stroke volume if preload increases (within physiologic range) and explain via the Frank-Starling mechanism.", a: "Higher preload stretches the ventricular walls. Within the working range, sarcomeres reach a more favorable length-tension relationship, and the next contraction is more forceful. Stroke volume rises. This is the Frank-Starling mechanism: the heart pumps out what it receives." },
            { id: "c11", dok: 3, q: "A patient develops cardiac tamponade (fluid in the pericardial sac compressing the heart). Predict the effect on filling and stroke volume and explain why.", a: "External compression limits how much the ventricles can expand during diastole, dropping preload. Reduced preload means reduced stroke volume (Frank-Starling reverse). Cardiac output falls. Severe tamponade is rapidly fatal without drainage." },
            { id: "c12", dok: 3, q: "Compare the pressures the LV and RV must generate, and explain the structural difference between them.", a: "LV pumps into the systemic circuit (high resistance, ~120 mmHg peak). RV pumps into the pulmonary circuit (low resistance, ~25 mmHg peak). LV wall is thicker (concentric muscle) to generate the higher pressure; RV is thinner and crescent-shaped." }
          ]
        },

        {
          id: "t-conduction-ecg",
          title: "Cardiac Conduction System",
          summary: "How the heart paces itself: pacemaker, delay, and rapid ventricular spread.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity",
          lecturePageUrl: "cardiac-conduction.html",
          dayInCourse: 23,
          videoLabel: "Video: Cardiac conduction system (pending)",
          gateKeywords: ["SA node", "AV node", "Purkinje", "pacemaker", "bundle of His"],
          notes: [
            { heading: "Conduction pathway", body: [
              "SA node (right atrial wall) is the pacemaker. It sets heart rate, normally 60-100 bpm at rest.",
              "Impulse spreads through atrial myocardium to the AV node.",
              "AV node delays the impulse (about 100 ms) so atria finish contracting and emptying before ventricles begin.",
              "Bundle of His carries the signal into the interventricular septum.",
              "Right and left bundle branches deliver it to the Purkinje fibers, which rapidly spread excitation throughout the ventricular myocardium."
            ]},
            { heading: "Why the timing matters", body: [
              "The AV delay protects ventricular filling: if atria and ventricles contracted simultaneously, cardiac output would collapse.",
              "Rapid ventricular spread by Purkinje fibers makes ventricular contraction nearly simultaneous, producing an effective ejection.",
              "Loss of coordination at any point in this pathway causes an arrhythmia."
            ]},
            { heading: "Arrhythmias at a glance", body: [
              "AV block: conduction through the AV node is slowed (first-degree) or fails intermittently (second/third-degree).",
              "Atrial fibrillation: chaotic atrial activity, irregular ventricular response, stroke risk.",
              "Ventricular fibrillation: ventricles quiver instead of contracting; cardiac arrest without immediate defibrillation."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What structure sets the normal heart rate?", a: "The sinoatrial (SA) node." },
            { id: "c2", dok: 1, q: "Where does the AV node sit and what does it do?", a: "Between the atria and ventricles. It delays the impulse so the atria finish emptying before the ventricles contract." },
            { id: "c3", dok: 1, q: "Name the conduction pathway in order from SA node to ventricular myocardium.", a: "SA node → atrial myocardium → AV node → Bundle of His → right and left bundle branches → Purkinje fibers → ventricular myocardium." },
            { id: "c4", dok: 1, q: "Approximately how long is the AV nodal delay?", a: "About 100 milliseconds." },
            { id: "c5", dok: 2, q: "Why is the AV delay essential for cardiac output?", a: "Without the delay, atria and ventricles would contract simultaneously. The atria would fail to empty into the ventricles, ventricular filling would drop, and stroke volume would collapse." },
            { id: "c6", dok: 2, q: "Why does the Purkinje system spread the impulse so quickly through the ventricles?", a: "Coordinated ventricular contraction requires all regions to depolarize nearly simultaneously. Rapid Purkinje conduction makes that possible; slower spread would produce uncoordinated, inefficient ejection." },
            { id: "c7", dok: 3, q: "A patient has third-degree (complete) AV block: the atria and ventricles fire independently. Predict the consequences for cardiac output and explain why.", a: "Atria contract on their own rhythm; ventricles fall back to a slower escape rhythm from below the block (40-60 bpm or less). The atrial kick no longer reliably precedes ventricular contraction, dropping stroke volume and cardiac output. Patients typically need a pacemaker." },
            { id: "c8", dok: 3, q: "Why is ventricular fibrillation rapidly fatal without intervention?", a: "Chaotic ventricular activity means no coordinated contraction. The ventricles quiver rather than pump. Cardiac output collapses; brain and coronary perfusion fail within minutes." }
          ]
        },

        {
          id: "t-vessels-hemodynamics",
          title: "Blood Vessels and Hemodynamics",
          summary: "Vessel types, blood pressure determinants, and how flow is regulated.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/20-2-blood-flow-blood-pressure-and-resistance",
          lecturePageUrl: "blood-vessels-hemodynamics.html",
          dayInCourse: 24,
          videoLabel: "Video: Vessels and hemodynamics (pending)",
          gateKeywords: ["artery", "vein", "capillary", "blood pressure", "resistance"],
          notes: [
            { heading: "Vessel types", body: [
              "Arteries: thick, elastic, high pressure.",
              "Arterioles: muscular, primary site of vascular resistance.",
              "Capillaries: single endothelial layer, where exchange occurs.",
              "Venules and veins: thin-walled, low pressure, valves; capacitance vessels."
            ]},
            { heading: "Determinants of blood pressure", body: [
              "BP = cardiac output × total peripheral resistance.",
              "Cardiac output = stroke volume × heart rate.",
              "Resistance is dominated by arteriolar diameter.",
              "Mean arterial pressure (MAP) is what perfuses tissues."
            ]},
            { heading: "Regulation", body: [
              "Short-term: baroreflex from carotid sinus and aortic arch via medullary cardiovascular centers; adjusts HR and vascular tone within seconds.",
              "Long-term: kidneys via fluid balance (RAAS) and ANP."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which vessels are the main site of resistance to flow?", a: "Arterioles." },
            { id: "c2", dok: 1, q: "Write the equation for cardiac output.", a: "Cardiac output = stroke volume × heart rate." },
            { id: "c3", dok: 1, q: "Why do veins have valves?", a: "Pressure in veins is low, so backflow is a risk, especially against gravity. Valves keep blood moving toward the heart." },
            { id: "c4", dok: 2, q: "Explain how arteriolar vasoconstriction raises blood pressure.", a: "Narrowing the arterioles increases total peripheral resistance. With cardiac output unchanged, raising resistance raises arterial pressure (BP = CO × TPR)." },
            { id: "c5", dok: 3, q: "A patient is dehydrated and presents with low blood pressure and a heart rate of 130. Explain both findings via the baroreflex.", a: "Volume loss drops preload and stroke volume, so cardiac output and arterial pressure fall. Baroreceptors detect the pressure drop and reduce their firing. The brainstem cardiovascular centers respond by raising sympathetic outflow: tachycardia and vasoconstriction try to restore BP. The high HR is the compensation; the still-low BP shows the compensation is incomplete without fluid replacement." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 13: LYMPHATIC AND IMMUNE
       ============================================================ */
    {
      id: "m-13-immune",
      week: 7,
      title: "Lymphatic and Immune System",
      topics: [

        {
          id: "t-lymphatic-innate",
          title: "Lymphatic System and Innate Immunity",
          summary: "Lymph vessels, lymphoid organs, and the body's general (non-specific) defenses.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/21-2-barrier-defenses-and-the-innate-immune-response",
          lecturePageUrl: "lymphatic-innate-immunity.html",
          dayInCourse: 25,
          videoLabel: "Video: Lymphatic and innate (pending)",
          gateKeywords: ["lymph", "lymphocyte", "innate", "phagocyte", "inflammation"],
          notes: [
            { heading: "Lymphatic system", body: [
              "Returns interstitial fluid (lymph) to the bloodstream.",
              "Filters lymph through lymph nodes (immune surveillance).",
              "Major organs: nodes, spleen, thymus, tonsils, MALT."
            ]},
            { heading: "Innate immunity (fast, general)", body: [
              "Surface barriers: skin, mucous membranes, low pH, antimicrobial peptides.",
              "Internal: neutrophils, macrophages, NK cells.",
              "Complement system: cascading proteins that lyse pathogens and mark them for phagocytosis.",
              "Interferons: antiviral cytokines."
            ]},
            { heading: "Inflammation (cardinal signs)", body: [
              "Redness, heat, swelling, pain, sometimes loss of function.",
              "Vasodilation and increased permeability bring immune cells and proteins to the site.",
              "Chemotaxis recruits more cells; phagocytes clear the pathogen and debris."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the four cardinal signs of inflammation.", a: "Redness, heat, swelling, pain (sometimes loss of function is added as a fifth)." },
            { id: "c2", dok: 1, q: "Name two phagocytic cells.", a: "Neutrophil, macrophage." },
            { id: "c3", dok: 1, q: "What is the function of natural killer cells?", a: "They kill virus-infected and tumor cells by inducing apoptosis, without needing prior exposure." },
            { id: "c4", dok: 2, q: "Why does inflammation produce swelling?", a: "Vasodilation and increased capillary permeability let plasma proteins leak into tissue. Water follows osmotically, increasing local fluid volume." },
            { id: "c5", dok: 3, q: "A patient is asplenic (had splenectomy after trauma). Predict the infection risk and explain.", a: "The spleen filters encapsulated bacteria (Streptococcus pneumoniae, Haemophilus influenzae, Neisseria meningitidis) from the blood. Without it, these organisms can cause overwhelming bacteremia. Patients receive vaccines and may need lifelong antibiotic precautions." }
          ]
        },

        {
          id: "t-adaptive-immunity",
          title: "Adaptive Immunity",
          summary: "Specificity and memory: how B and T cells learn what to attack and remember it.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/21-3-the-adaptive-immune-response-t-lymphocytes-and-their-functional-types",
          lecturePageUrl: "adaptive-immunity.html",
          dayInCourse: 26,
          videoLabel: "Video: Adaptive immunity (pending)",
          gateKeywords: ["B cell", "T cell", "antibody", "antigen", "MHC"],
          notes: [
            { heading: "Two arms of adaptive immunity", body: [
              "Humoral: B cells → plasma cells → antibodies that neutralize and tag extracellular pathogens.",
              "Cell-mediated: T cells. Helper T (CD4) coordinate; cytotoxic T (CD8) kill infected cells."
            ]},
            { heading: "Antigen presentation", body: [
              "MHC I: on all nucleated cells; presents intracellular peptides (including viral) to CD8 T cells.",
              "MHC II: on antigen-presenting cells (dendritic cells, macrophages, B cells); presents extracellular peptides to CD4 T cells."
            ]},
            { heading: "Activation and memory", body: [
              "Naive lymphocytes encounter their cognate antigen on an antigen-presenting cell.",
              "Activation requires antigen + costimulatory signals (preventing reactivity to self).",
              "Clonal expansion produces effector cells and memory cells.",
              "Memory cells respond faster and stronger on re-exposure: the basis of vaccination."
            ]},
            { heading: "Antibody functions", body: [
              "Neutralization (block toxin or viral entry).",
              "Opsonization (tag for phagocytosis).",
              "Complement activation.",
              "ADCC (mark cells for NK killing)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which T cell subset directly kills infected cells?", a: "Cytotoxic (CD8) T cells." },
            { id: "c2", dok: 1, q: "What do plasma cells produce?", a: "Antibodies." },
            { id: "c3", dok: 1, q: "Which MHC class presents to CD8 T cells?", a: "MHC class I." },
            { id: "c4", dok: 1, q: "Which MHC class presents to CD4 T cells?", a: "MHC class II." },
            { id: "c5", dok: 1, q: "Name three antigen-presenting cell types.", a: "Dendritic cells, macrophages, B cells." },
            { id: "c6", dok: 2, q: "Why does the secondary immune response peak faster and higher than the primary?", a: "Memory B and T cells generated during the primary response are pre-expanded and pre-selected for the antigen. On re-exposure they activate without the long naive-cell selection step, producing antibodies and effector T cells far more quickly and in greater numbers." },
            { id: "c7", dok: 2, q: "Explain why vaccines work using the concepts of memory and clonal expansion.", a: "Vaccines expose the immune system to a harmless form of an antigen. The body mounts a primary response, generating memory cells. On real infection, the secondary response activates quickly enough to clear the pathogen before it causes disease." },
            { id: "c8", dok: 2, q: "Predict the immune consequence of HIV destroying CD4 T cells.", a: "Helper T cells coordinate both humoral and cell-mediated responses. Without them, B cell activation and CD8 cytotoxic responses both fail. The patient becomes susceptible to opportunistic infections that intact immunity would normally control." },
            { id: "c9", dok: 3, q: "A transplant recipient receives a kidney from an HLA-mismatched donor. Explain why their immune system attacks the graft.", a: "Donor cells display foreign MHC (HLA) molecules. The recipient's T cells recognize these as non-self and mount an immune response (acute rejection). Immunosuppressive drugs are needed to blunt this response." },
            { id: "c10", dok: 3, q: "Autoimmune disease: a patient's T cells attack their own thyroid (Hashimoto's). Explain how central tolerance normally prevents this and how it could fail.", a: "In the thymus, developing T cells that bind self-antigen too strongly are normally deleted (negative selection). If a self-reactive clone escapes (or if peripheral tolerance fails later), it can attack self-tissue. In Hashimoto's, T cells and antibodies target thyroid antigens, gradually destroying the gland." },
            { id: "c11", dok: 3, q: "An infant born with severe combined immunodeficiency (SCID) lacks functional T and B cells. Predict the clinical picture and explain why.", a: "Without B and T cells, the infant has no adaptive immunity. Innate defenses partially compensate but are inadequate against most pathogens. The infant suffers severe and recurrent infections from bacteria, viruses, and fungi, including normally harmless organisms. Without treatment (bone marrow transplant or gene therapy), SCID is usually fatal in the first year." },
            { id: "c12", dok: 3, q: "Compare and contrast active and passive immunity, with one clinical example each.", a: "Active: the patient's own immune system makes antibodies. Examples: natural infection or vaccination. Slow to develop but durable (long memory). Passive: pre-formed antibodies are provided. Examples: maternal IgG across the placenta, or anti-venom injection. Immediate protection but short-lived (no memory cells are made)." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 14: RESPIRATORY SYSTEM
       ============================================================ */
    {
      id: "m-14-respiratory",
      week: 7,
      title: "Respiratory System",
      topics: [

        {
          id: "t-resp-anatomy-mechanics",
          title: "Respiratory Anatomy and Mechanics",
          summary: "Conducting vs respiratory zones, and how pressure changes move air in and out.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/22-1-organs-and-structures-of-the-respiratory-system",
          lecturePageUrl: "respiratory-anatomy.html",
          dayInCourse: 27,
          videoLabel: "Video: Respiratory anatomy and mechanics (pending)",
          gateKeywords: ["trachea", "alveolus", "diaphragm", "pleura", "Boyle"],
          notes: [
            { heading: "Anatomy at a glance", body: [
              "Conducting zone: nose, pharynx, larynx, trachea, bronchi, bronchioles. Warms, humidifies, filters. No gas exchange.",
              "Respiratory zone: respiratory bronchioles, alveolar ducts, alveoli. Gas exchange happens here.",
              "Alveoli: thin (simple squamous) for diffusion; lined with surfactant from type II pneumocytes."
            ]},
            { heading: "Pleura", body: [
              "Parietal pleura lines the thoracic cavity; visceral pleura covers the lung.",
              "Pleural cavity between is a slim, fluid-filled space with negative pressure.",
              "Negative intrapleural pressure keeps the lungs expanded against the chest wall."
            ]},
            { heading: "Mechanics of breathing", body: [
              "Boyle's law: at constant temperature, pressure × volume is constant.",
              "Inspiration: diaphragm contracts and external intercostals lift the ribs; thoracic volume rises; intra-alveolar pressure drops below atmospheric; air flows in.",
              "Expiration (at rest): muscles relax; elastic recoil shrinks the thorax; alveolar pressure rises above atmospheric; air flows out.",
              "Forced expiration adds internal intercostals and abdominal muscles."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the primary muscle of inspiration?", a: "The diaphragm." },
            { id: "c2", dok: 1, q: "Which alveolar cell produces surfactant?", a: "Type II pneumocyte." },
            { id: "c3", dok: 1, q: "What is the function of surfactant?", a: "Reduces surface tension in alveoli, preventing collapse and easing inflation." },
            { id: "c4", dok: 1, q: "Which law explains air movement during breathing?", a: "Boyle's law (pressure and volume vary inversely)." },
            { id: "c5", dok: 2, q: "Why is the pleural cavity pressure negative?", a: "Elastic recoil of the lungs pulls inward, while the chest wall pulls outward. The opposing forces create a slight vacuum in the pleural space, keeping the lungs adhered to the chest wall." },
            { id: "c6", dok: 3, q: "A penetrating chest wound exposes the pleural cavity to atmospheric air (pneumothorax). Predict the effect on the affected lung and explain.", a: "Air enters the pleural space until pressure equalizes with the atmosphere. The negative pressure that was holding the lung expanded is lost. Elastic recoil collapses the lung. Ventilation on the affected side falls dramatically." }
          ]
        },

        {
          id: "t-gas-exchange-transport",
          title: "Gas Exchange and Transport",
          summary: "Diffusion at the alveoli and tissues, and how O₂ and CO₂ ride in the blood.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/22-4-gas-exchange",
          lecturePageUrl: "gas-exchange-transport.html",
          dayInCourse: 27,
          videoLabel: "Video: Gas exchange and transport (pending)",
          gateKeywords: ["alveolus", "oxygen", "carbon dioxide", "hemoglobin", "partial pressure"],
          notes: [
            { heading: "Where exchange happens", body: [
              "External respiration: between alveolar air and pulmonary capillary blood.",
              "Internal respiration: between systemic capillary blood and body tissues.",
              "Both run on partial pressure gradients."
            ]},
            { heading: "Oxygen transport", body: [
              "About 98% bound to hemoglobin; 2% dissolved in plasma.",
              "Each Hb molecule binds 4 O₂ cooperatively.",
              "The O₂-Hb dissociation curve: sigmoidal. Right shift (more O₂ released to tissue) with acidosis, high CO₂, high temperature, high 2,3-BPG."
            ]},
            { heading: "Carbon dioxide transport", body: [
              "About 70% as bicarbonate (HCO₃⁻) via the carbonic anhydrase reaction in RBCs.",
              "About 20% bound to hemoglobin (carbaminohemoglobin).",
              "About 10% dissolved in plasma."
            ]},
            { heading: "Control of ventilation", body: [
              "Central chemoreceptors in the medulla respond mostly to CSF pH (a proxy for arterial CO₂).",
              "Peripheral chemoreceptors (carotid and aortic bodies) respond to severely low arterial O₂.",
              "CO₂ is the main minute-to-minute driver of ventilation."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the main form of CO₂ transport in blood?", a: "Bicarbonate (HCO₃⁻), about 70%." },
            { id: "c2", dok: 1, q: "How many O₂ molecules can one hemoglobin molecule carry?", a: "Four (one per heme group)." },
            { id: "c3", dok: 1, q: "Where are the central chemoreceptors?", a: "In the medulla oblongata." },
            { id: "c4", dok: 1, q: "Which gas is the primary moment-to-moment driver of ventilation?", a: "Carbon dioxide (CO₂, via its effect on CSF pH)." },
            { id: "c5", dok: 2, q: "Explain why exercising muscle gets more oxygen even though arterial O₂ saturation is unchanged.", a: "Exercising muscle is warmer, more acidic, and has higher CO₂ and 2,3-BPG. These shift the O₂-Hb dissociation curve right, so Hb releases more O₂ at any given partial pressure. The Bohr effect delivers more O₂ exactly where it is needed." },
            { id: "c6", dok: 2, q: "Why does carbon monoxide poisoning cause hypoxia even when arterial pO₂ is normal?", a: "CO binds hemoglobin with ~250 times higher affinity than O₂. Hb sites are occupied by CO, leaving few to carry O₂. Total O₂ content of blood plummets, even though dissolved pO₂ may look fine on a blood gas." },
            { id: "c7", dok: 2, q: "Explain why patients with severe COPD may be driven to breathe by hypoxia rather than CO₂.", a: "Chronic CO₂ retention desensitizes the central chemoreceptors. The peripheral chemoreceptors, which respond to low O₂, take over as the primary drive. Giving such a patient very high inspired O₂ can blunt that drive and cause hypoventilation." },
            { id: "c8", dok: 2, q: "Predict the effect on arterial pH of acute hyperventilation, and explain via the bicarbonate buffer.", a: "Hyperventilation drives off CO₂. Less CO₂ means the equation H₂O + CO₂ ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻ shifts left, lowering H⁺. Arterial pH rises (respiratory alkalosis)." },
            { id: "c9", dok: 3, q: "Climbers ascending to high altitude (3,500 m+) develop hyperventilation, polycythemia, and a right shift in their oxygen-hemoglobin curve over days. Explain each adaptation.", a: "Low atmospheric pO₂ stresses the peripheral chemoreceptors, raising minute ventilation. Persistent hypoxia stimulates renal EPO; the marrow produces more RBCs (polycythemia), increasing oxygen-carrying capacity. Tissue acidosis and elevated 2,3-BPG shift the curve right, unloading more O₂ at the tissues." },
            { id: "c10", dok: 3, q: "A patient has a pulmonary embolus that blocks blood flow to a portion of one lung. Predict the V/Q ratio in that region and the consequence.", a: "Ventilation continues (air gets to those alveoli) but perfusion drops (Q falls toward zero). V/Q rises sharply (dead-space-like). That alveolar air does not contribute to gas exchange; effective surface area shrinks. Hypoxemia results, often resistant to supplemental oxygen because the problem is perfusion, not diffusion." },
            { id: "c11", dok: 3, q: "Explain why a premature infant may develop neonatal respiratory distress syndrome (NRDS), and what surfactant therapy does.", a: "Surfactant production by type II pneumocytes ramps up only in the final weeks of gestation. Without enough surfactant, surface tension keeps alveoli collapsed (atelectasis). Work of breathing soars, gas exchange falters. Exogenous surfactant lowers surface tension, allows alveoli to inflate, and supports gas exchange until endogenous production catches up." },
            { id: "c12", dok: 3, q: "A patient's arterial blood gas shows pH 7.30, pCO₂ 60 mmHg, HCO₃⁻ 30 mEq/L. Interpret and explain the underlying physiology.", a: "Acidic pH with high pCO₂ indicates respiratory acidosis. The elevated HCO₃⁻ (above 24) is the renal compensation, retaining bicarbonate to buffer the acid. The pattern suggests chronic CO₂ retention (e.g., COPD): the kidneys have had time to compensate, but pH remains below 7.35, so compensation is incomplete." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 15: DIGESTIVE SYSTEM
       ============================================================ */
    {
      id: "m-15-digestive",
      week: 7,
      title: "Digestive System",
      topics: [

        {
          id: "t-gi-anatomy-motility",
          title: "GI Tract Anatomy and Motility",
          summary: "From mouth to anus, the layers of the gut wall, and how food moves.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/23-1-overview-of-the-digestive-system",
          lecturePageUrl: "gi-anatomy-motility.html",
          dayInCourse: 28,
          videoLabel: "Video: GI anatomy and motility (pending)",
          gateKeywords: ["esophagus", "stomach", "small intestine", "peristalsis", "sphincter"],
          notes: [
            { heading: "The path", body: [
              "Mouth → pharynx → esophagus → stomach → small intestine (duodenum, jejunum, ileum) → large intestine (colon) → rectum → anus.",
              "Accessory organs: salivary glands, liver, gallbladder, pancreas."
            ]},
            { heading: "Wall layers (deep to superficial)", body: [
              "Mucosa: epithelium, lamina propria, muscularis mucosae.",
              "Submucosa: blood vessels, submucosal (Meissner) plexus.",
              "Muscularis externa: inner circular and outer longitudinal smooth muscle layers; myenteric (Auerbach) plexus between.",
              "Serosa (or adventitia in some regions)."
            ]},
            { heading: "Motility", body: [
              "Peristalsis: sequential wave of contraction propels content forward.",
              "Segmentation: localized contractions mix without net forward motion (small intestine).",
              "Sphincters: lower esophageal (cardia), pyloric, ileocecal, internal/external anal."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Name the three parts of the small intestine in order.", a: "Duodenum, jejunum, ileum." },
            { id: "c2", dok: 1, q: "What is peristalsis?", a: "A wave of smooth muscle contraction that propels content along the GI tract." },
            { id: "c3", dok: 1, q: "Name the four wall layers of the GI tract.", a: "Mucosa, submucosa, muscularis externa, serosa (or adventitia)." },
            { id: "c4", dok: 1, q: "What is the function of the pyloric sphincter?", a: "Regulates passage of chyme from the stomach to the duodenum." },
            { id: "c5", dok: 2, q: "Why is segmentation more important than peristalsis in the small intestine?", a: "Segmentation mixes chyme with digestive enzymes and exposes it to the absorptive surface, maximizing digestion and absorption. Net forward motion is slower, which gives time for these processes." },
            { id: "c6", dok: 3, q: "A patient with achalasia cannot relax the lower esophageal sphincter. Predict the symptoms and explain.", a: "Food and liquid accumulate above the unrelaxed sphincter, dilating the lower esophagus. Patients have dysphagia (especially for solids and liquids), regurgitation, chest pain, and weight loss. Aspiration risk rises if regurgitated material reaches the airway." }
          ]
        },

        {
          id: "t-digestion-absorption",
          title: "Digestion and Absorption",
          summary: "Where each macromolecule gets broken down and how absorption happens.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/23-7-chemical-digestion-and-absorption-a-closer-look",
          lecturePageUrl: "digestion-absorption.html",
          dayInCourse: 28,
          videoLabel: "Video: Digestion and absorption (pending)",
          gateKeywords: ["enzyme", "villi", "bile", "pancreas", "absorption"],
          notes: [
            { heading: "Carbohydrate digestion", body: [
              "Mouth: salivary amylase begins starch breakdown.",
              "Small intestine: pancreatic amylase finishes starch to disaccharides; brush-border enzymes (maltase, sucrase, lactase) finish to monosaccharides.",
              "Absorbed in the small intestine by SGLT1 (Na⁺-glucose symporter) and GLUT2."
            ]},
            { heading: "Protein digestion", body: [
              "Stomach: pepsin (activated from pepsinogen in acidic environment).",
              "Small intestine: pancreatic proteases (trypsin, chymotrypsin, carboxypeptidase). Brush-border peptidases finish.",
              "Absorbed as amino acids and small peptides."
            ]},
            { heading: "Lipid digestion", body: [
              "Bile (from liver, stored in gallbladder) emulsifies fats in the duodenum.",
              "Pancreatic lipase hydrolyzes triglycerides to monoglycerides and fatty acids.",
              "Products form micelles, diffuse into enterocytes, reassemble into chylomicrons, and enter lymph via lacteals."
            ]},
            { heading: "Absorptive surface", body: [
              "Plicae (folds), villi (finger-like projections), microvilli (brush border).",
              "Together they multiply surface area roughly 600-fold."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Where is most absorption of nutrients accomplished?", a: "In the small intestine." },
            { id: "c2", dok: 1, q: "What does bile do?", a: "Emulsifies fats, breaking them into smaller droplets so pancreatic lipase can access them." },
            { id: "c3", dok: 1, q: "Which enzyme begins protein digestion in the stomach?", a: "Pepsin (from pepsinogen)." },
            { id: "c4", dok: 1, q: "Where do absorbed fats first enter (the bloodstream or lymph)?", a: "Lymph (via lacteals in the villi), as chylomicrons." },
            { id: "c5", dok: 2, q: "Why do patients with lactose intolerance experience bloating and diarrhea after dairy?", a: "Without lactase, lactose cannot be split to glucose and galactose. Undigested lactose remains in the gut, drawing in water osmotically (diarrhea) and getting fermented by colonic bacteria (gas and bloating)." },
            { id: "c6", dok: 3, q: "A patient has had their gallbladder removed. Predict the dietary consequence and explain.", a: "Bile is still made by the liver, but it can no longer be concentrated and stored. Continuous low-level bile flow into the duodenum is fine for typical meals, but a large fatty meal exceeds the bile available at that moment. Patients often experience steatorrhea or discomfort after high-fat meals." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 16: URINARY AND FLUID BALANCE
       ============================================================ */
    {
      id: "m-16-urinary",
      week: 8,
      title: "Urinary System and Fluid Balance",
      topics: [

        {
          id: "t-kidney-filtration",
          title: "Kidney Anatomy and Glomerular Filtration",
          summary: "From renal cortex to nephron to filtration barrier: how urine starts.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/25-3-physiology-of-urine-formation",
          lecturePageUrl: "kidney-anatomy-gfr.html",
          dayInCourse: 29,
          videoLabel: "Video: Kidney filtration (pending)",
          gateKeywords: ["nephron", "glomerulus", "Bowman", "filtration", "GFR"],
          notes: [
            { heading: "Gross anatomy", body: [
              "Outer cortex, inner medulla (pyramids), pelvis drains to ureter.",
              "Each kidney has about 1 million nephrons.",
              "Renal artery → afferent arteriole → glomerulus → efferent arteriole → peritubular capillaries (or vasa recta) → renal vein."
            ]},
            { heading: "The nephron", body: [
              "Renal corpuscle: glomerulus + Bowman's capsule.",
              "Tubule: PCT (proximal convoluted), loop of Henle, DCT (distal convoluted), collecting duct.",
              "Cortical nephrons (~85%) vs juxtamedullary nephrons (long loops, concentrate urine)."
            ]},
            { heading: "Filtration", body: [
              "Filtration barrier: fenestrated capillary endothelium, basement membrane, podocyte slit diaphragms.",
              "Excludes cells and most proteins.",
              "GFR ≈ 125 mL/min. Determined by glomerular hydrostatic pressure minus oncotic pressure and capsular pressure.",
              "GFR is autoregulated within a wide range of MAP via myogenic response and tubuloglomerular feedback."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the functional unit of the kidney?", a: "The nephron." },
            { id: "c2", dok: 1, q: "What is the typical glomerular filtration rate (GFR)?", a: "About 125 mL/min (≈180 L/day)." },
            { id: "c3", dok: 1, q: "Which vessel delivers blood to the glomerulus?", a: "The afferent arteriole." },
            { id: "c4", dok: 1, q: "Which structures form the filtration slits?", a: "Podocyte foot processes (pedicels)." },
            { id: "c5", dok: 2, q: "Explain how the kidney maintains a stable GFR despite changes in blood pressure within the normal range.", a: "Two mechanisms: (1) myogenic response, afferent arteriole constricts when stretched by higher pressure; (2) tubuloglomerular feedback, macula densa senses tubular flow and adjusts afferent arteriole tone via the juxtaglomerular apparatus." },
            { id: "c6", dok: 3, q: "Proteinuria in a kidney patient suggests damage where? Explain.", a: "The glomerular filtration barrier (endothelium, basement membrane, or podocytes) normally excludes proteins. Protein in the urine implies barrier dysfunction, most often at the podocyte slit diaphragms or basement membrane (nephrotic-range disease)." }
          ]
        },

        {
          id: "t-tubular-function",
          title: "Tubular Function and Urine Concentration",
          summary: "How the tubules reshape the filtrate into a final urine, and how ADH and aldosterone fine-tune it.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/25-4-physiology-of-urine-formation-tubular-reabsorption-and-secretion",
          dayInCourse: 30,
          videoLabel: "Video: Tubular function (pending)",
          gateKeywords: ["PCT", "loop of Henle", "DCT", "collecting duct", "ADH"],
          notes: [
            { heading: "PCT: bulk reabsorption", body: [
              "Reabsorbs about 65% of filtered Na⁺, water, glucose, amino acids, and bicarbonate.",
              "Isotonic reabsorption: water follows solutes."
            ]},
            { heading: "Loop of Henle: building the gradient", body: [
              "Descending limb: permeable to water, impermeable to ions. Water leaves; filtrate becomes hypertonic.",
              "Thick ascending limb: impermeable to water; active reabsorption of Na⁺, K⁺, 2 Cl⁻ (NKCC2 cotransporter). Filtrate becomes hypotonic.",
              "Net result: a hypertonic medullary interstitium (countercurrent multiplier)."
            ]},
            { heading: "DCT and collecting duct: fine-tuning", body: [
              "Early DCT: reabsorbs Na⁺ and Cl⁻ via NCC cotransporter.",
              "Late DCT and collecting duct: principal cells under aldosterone control (reabsorb Na⁺, secrete K⁺).",
              "Collecting duct water permeability is set by ADH inserting aquaporin-2 channels.",
              "Intercalated cells handle acid-base (secrete H⁺ or HCO₃⁻ as needed)."
            ]},
            { heading: "Hormonal control", body: [
              "ADH (vasopressin): rises when plasma osmolarity rises or blood volume falls. Inserts aquaporin-2 into collecting duct cells → water reabsorption rises → concentrated urine.",
              "Aldosterone: from adrenal cortex (stimulated by angiotensin II and high K⁺). Reabsorbs Na⁺, secretes K⁺.",
              "ANP: from atria when volume is high. Opposes RAAS; promotes Na⁺ and water excretion."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which tubule segment reabsorbs the largest fraction of filtered Na⁺ and water?", a: "The proximal convoluted tubule (about 65%)." },
            { id: "c2", dok: 1, q: "What is the function of ADH in the collecting duct?", a: "Inserts aquaporin-2 channels into the apical membrane, increasing water reabsorption and producing more concentrated urine." },
            { id: "c3", dok: 1, q: "Where does aldosterone act in the nephron?", a: "Principal cells of the late distal tubule and collecting duct." },
            { id: "c4", dok: 1, q: "Which limb of the loop of Henle is impermeable to water?", a: "The thick ascending limb." },
            { id: "c5", dok: 1, q: "What is the role of the countercurrent multiplier?", a: "Establishes a hypertonic medullary interstitium that allows the collecting duct to concentrate urine when ADH is present." },
            { id: "c6", dok: 2, q: "Explain why diabetes insipidus (lack of ADH or ADH resistance) causes large volumes of dilute urine.", a: "Without ADH action, aquaporin-2 channels are not inserted in the collecting duct. Water cannot be reabsorbed there. Filtrate exits as a large volume of very dilute urine." },
            { id: "c7", dok: 2, q: "Loop diuretics (furosemide) block the NKCC2 cotransporter in the thick ascending limb. Predict the effect on urine output and explain.", a: "Without NKCC2, Na⁺, K⁺, and Cl⁻ stay in the lumen. The medullary gradient that drives water reabsorption collapses. Water and these electrolytes are excreted in large amounts: a strong diuresis with potential hypokalemia." },
            { id: "c8", dok: 2, q: "Spironolactone blocks the aldosterone receptor. Predict the effect on serum K⁺.", a: "Without aldosterone action, principal cells reabsorb less Na⁺ and secrete less K⁺. Less K⁺ is lost in urine, so serum K⁺ rises (hyperkalemia risk). Hence 'potassium-sparing' diuretic." },
            { id: "c9", dok: 3, q: "A patient is severely dehydrated after marathon running in the heat. Predict their plasma ADH and aldosterone levels and the urine they produce, with reasoning.", a: "Volume loss and rising plasma osmolarity trigger both ADH (osmoreceptors and baroreceptors) and aldosterone (RAAS activation from low renal perfusion and angiotensin II). Both hormones rise. Urine becomes scant, concentrated, and low in Na⁺." },
            { id: "c10", dok: 3, q: "Explain how the countercurrent multiplier and ADH cooperate to produce maximally concentrated urine.", a: "The countercurrent multiplier in the loop of Henle creates a hypertonic medulla. When ADH inserts aquaporin-2 into the collecting duct, water flows from the duct lumen into the hypertonic interstitium until osmotic equilibrium. Without the gradient, ADH would have nowhere to send the water; without ADH, the gradient is irrelevant. Both are required." },
            { id: "c11", dok: 3, q: "A patient with Conn syndrome (primary hyperaldosteronism) has high BP and low K⁺. Tie both findings to aldosterone's actions.", a: "Excess aldosterone drives renal Na⁺ reabsorption; water follows osmotically, expanding plasma volume and raising BP. Excess aldosterone also drives K⁺ secretion at the principal cells, lowering serum K⁺. The combination of hypertension with hypokalemia is the clinical fingerprint." },
            { id: "c12", dok: 3, q: "Compare the urine of a patient given desmopressin (synthetic ADH) with that of a patient given furosemide. Explain mechanistically.", a: "Desmopressin: more aquaporin-2 in the collecting duct → water reabsorption rises → urine volume small, concentration high. Furosemide: NKCC2 blocked → medullary gradient collapses → water cannot be reabsorbed → urine volume large, dilute, with substantial salt loss." }
          ]
        },

        {
          id: "t-fluid-acid-base",
          title: "Fluid, Electrolyte, and Acid-Base Balance",
          summary: "Body fluid compartments, the main electrolytes, and how the body keeps pH near 7.4.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/26-4-acid-base-balance",
          lecturePageUrl: "fluid-electrolyte-acid-base.html",
          dayInCourse: 31,
          videoLabel: "Video: Fluid and acid-base (pending)",
          gateKeywords: ["ICF", "ECF", "sodium", "potassium", "pH"],
          notes: [
            { heading: "Body fluid compartments", body: [
              "Total body water ~60% of body weight.",
              "Intracellular fluid (ICF): ~⅔ of body water. High K⁺, low Na⁺.",
              "Extracellular fluid (ECF): ~⅓. High Na⁺, low K⁺. Subdivided into plasma and interstitial fluid."
            ]},
            { heading: "Key electrolytes", body: [
              "Sodium: the main ECF cation; sets ECF osmolarity and volume.",
              "Potassium: the main ICF cation; small ECF changes have large effects on excitable tissues (heart, nerves).",
              "Calcium: in clotting, neuromuscular function, bone.",
              "Magnesium and phosphate: cofactors and bone components."
            ]},
            { heading: "Acid-base", body: [
              "Normal arterial pH: 7.35-7.45.",
              "Buffers (bicarbonate, phosphate, protein) blunt acid loads minute to minute.",
              "Respiratory compensation (changes in ventilation) adjusts CO₂ rapidly.",
              "Renal compensation (changes in HCO₃⁻ retention and H⁺ excretion) adjusts over hours to days.",
              "Disturbances: respiratory acidosis/alkalosis (CO₂ problem), metabolic acidosis/alkalosis (HCO₃⁻ problem)."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What is the normal arterial pH range?", a: "7.35-7.45." },
            { id: "c2", dok: 1, q: "Which compartment holds the most water?", a: "Intracellular fluid (about two-thirds of total body water)." },
            { id: "c3", dok: 1, q: "Which cation dominates the ECF?", a: "Sodium." },
            { id: "c4", dok: 1, q: "Which cation dominates the ICF?", a: "Potassium." },
            { id: "c5", dok: 2, q: "Why does severe vomiting cause metabolic alkalosis?", a: "Vomiting loses gastric H⁺ (HCl). The body has lost acid, so the remaining HCO₃⁻ pushes pH up. Plasma bicarbonate rises, pH rises (alkalosis). Volume loss compounds the picture by triggering aldosterone, which further drives renal acid loss." },
            { id: "c6", dok: 3, q: "A diabetic patient in DKA has pH 7.20, HCO₃⁻ 12 mEq/L, pCO₂ 25 mmHg. Interpret and explain each value.", a: "Acidic pH with low HCO₃⁻ = metabolic acidosis. The HCO₃⁻ has been consumed buffering ketoacids. The low pCO₂ is the respiratory compensation: the patient is hyperventilating (Kussmaul breathing) to blow off CO₂ and bring pH back toward normal. The compensation is partial since pH remains below 7.35." }
          ]
        }

      ]
    },

    /* ============================================================
       MODULE 17: REPRODUCTIVE SYSTEM AND DEVELOPMENT
       ============================================================ */
    {
      id: "m-17-reproductive",
      week: 8,
      title: "Reproductive System",
      topics: [

        {
          id: "t-male-reproductive",
          title: "Male Reproductive System",
          summary: "Testis structure, spermatogenesis, accessory glands, and the hormonal axis.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/27-1-anatomy-and-physiology-of-the-testicular-reproductive-system",
          lecturePageUrl: "male-reproductive.html",
          dayInCourse: 31,
          videoLabel: "Video: Male reproductive (pending)",
          gateKeywords: ["testis", "sperm", "seminiferous", "spermatogenesis", "testosterone"],
          notes: [
            { heading: "Testis", body: [
              "Seminiferous tubules: site of spermatogenesis. Lined by Sertoli cells that support developing sperm.",
              "Interstitial (Leydig) cells: produce testosterone in response to LH.",
              "Blood-testis barrier (formed by Sertoli cell tight junctions) protects developing sperm from the immune system."
            ]},
            { heading: "Sperm pathway", body: [
              "Seminiferous tubule → rete testis → epididymis (sperm matures and is stored) → vas deferens → ejaculatory duct → urethra.",
              "Accessory glands: seminal vesicles (fructose, prostaglandins), prostate (alkaline secretion, enzymes), bulbourethral glands (mucus)."
            ]},
            { heading: "Hormonal control", body: [
              "Hypothalamus releases GnRH → anterior pituitary releases LH and FSH.",
              "LH stimulates Leydig cells to make testosterone.",
              "FSH plus testosterone supports Sertoli cells and spermatogenesis.",
              "Testosterone provides negative feedback on the hypothalamus and pituitary."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Which cells produce testosterone?", a: "Leydig (interstitial) cells of the testis." },
            { id: "c2", dok: 1, q: "Which cells support developing sperm?", a: "Sertoli cells (in the seminiferous tubule)." },
            { id: "c3", dok: 1, q: "Where do sperm mature?", a: "The epididymis." },
            { id: "c4", dok: 1, q: "Which pituitary hormone drives testosterone production?", a: "Luteinizing hormone (LH)." },
            { id: "c5", dok: 2, q: "Why do anabolic steroid abusers often develop infertility and testicular atrophy?", a: "Exogenous androgens feed back negatively on the hypothalamus and pituitary, suppressing GnRH, LH, and FSH. Without LH and FSH, the testes lose their drive to make testosterone and to spermatogenesis. The testes shrink and sperm counts plummet, often persisting after the drugs stop." },
            { id: "c6", dok: 3, q: "A patient cannot make GnRH. Predict the cascade of hormonal and reproductive findings.", a: "No GnRH → no LH or FSH → no testosterone (Leydig idle) and no spermatogenesis (Sertoli unsupported). The patient presents with low testosterone (delayed puberty if congenital, hypogonadism if acquired), small testes, and infertility. Treatment requires replacing the missing hypothalamic signal or its downstream products." }
          ]
        },

        {
          id: "t-female-reproductive",
          title: "Female Reproductive System",
          summary: "Ovary, oogenesis, the ovarian and uterine cycles, and the hormonal choreography.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/27-2-anatomy-and-physiology-of-the-ovarian-reproductive-system",
          lecturePageUrl: "female-reproductive.html",
          dayInCourse: 32,
          videoLabel: "Video: Female reproductive (pending)",
          gateKeywords: ["ovary", "ovulation", "uterus", "estrogen", "progesterone"],
          notes: [
            { heading: "Ovary and oogenesis", body: [
              "Primordial follicles (oocyte arrested in prophase I of meiosis) are present from birth.",
              "Each cycle a cohort of follicles begins maturing; usually one becomes dominant.",
              "Granulosa and theca cells of the follicle produce estrogen under FSH and LH stimulation."
            ]},
            { heading: "Ovarian cycle", body: [
              "Follicular phase (days 1-14): follicle matures; estrogen rises.",
              "Ovulation (day 14): LH surge triggers release of the secondary oocyte.",
              "Luteal phase (days 15-28): ruptured follicle becomes the corpus luteum; produces progesterone (and estrogen) to support potential implantation. Regresses if no pregnancy."
            ]},
            { heading: "Uterine (menstrual) cycle", body: [
              "Menstrual phase (days 1-5): endometrium sheds.",
              "Proliferative phase (days 6-14): estrogen rebuilds the endometrium.",
              "Secretory phase (days 15-28): progesterone makes the endometrium glandular and receptive to implantation. If no implantation, progesterone falls and the cycle restarts."
            ]},
            { heading: "Hormonal control", body: [
              "GnRH → LH and FSH.",
              "Estrogen and progesterone provide mostly negative feedback, but rising estrogen mid-cycle switches to positive feedback that triggers the LH surge.",
              "Pregnancy maintains the corpus luteum (via hCG from the embryo) until the placenta takes over hormone production."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "What triggers ovulation?", a: "The LH surge mid-cycle." },
            { id: "c2", dok: 1, q: "What does the corpus luteum produce?", a: "Mostly progesterone (and some estrogen)." },
            { id: "c3", dok: 1, q: "Which phase of the uterine cycle features endometrial shedding?", a: "Menstrual phase." },
            { id: "c4", dok: 1, q: "Which hormone primarily rebuilds the endometrium during the proliferative phase?", a: "Estrogen." },
            { id: "c5", dok: 2, q: "Explain why estrogen switches from negative to positive feedback mid-cycle.", a: "When estrogen rises above a threshold and stays elevated, pituitary sensitivity to GnRH changes. The pituitary responds with the LH surge instead of suppression, driving ovulation. After ovulation, the corpus luteum's progesterone restores negative feedback." },
            { id: "c6", dok: 3, q: "Combined oral contraceptives suppress the LH surge. Explain mechanistically.", a: "Exogenous estrogen and progesterone maintain steady (artificially elevated) plasma hormone levels. Continuous negative feedback suppresses GnRH and gonadotropin release. Without the natural mid-cycle rise in estrogen, the positive-feedback switch does not occur, the LH surge is blunted, and ovulation is prevented." }
          ]
        },

        {
          id: "t-pregnancy-development",
          title: "Pregnancy A&P (Basics)",
          summary: "Fertilization, implantation, and the maternal-fetal interface. Maternal physiology highlights through the trimesters.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/28-4-maternal-changes-during-pregnancy-labor-and-birth",
          lecturePageUrl: "pregnancy-basics.html",
          dayInCourse: 32,
          videoLabel: "Video: Pregnancy A&P basics (pending)",
          gateKeywords: ["fertilization", "implantation", "placenta", "hCG", "corpus luteum"],
          notes: [
            { heading: "Fertilization and implantation", body: [
              "Sperm meets the secondary oocyte in the ampulla of the uterine tube within hours of ovulation.",
              "The fertilized egg divides as it travels to the uterus, becoming a blastocyst.",
              "Implantation in the uterine endometrium occurs around day 6-7."
            ]},
            { heading: "Hormonal support", body: [
              "Trophoblast cells secrete hCG, which keeps the corpus luteum alive.",
              "The corpus luteum continues progesterone production, maintaining the endometrium.",
              "By the end of the first trimester, the placenta takes over hormone production (progesterone, estrogen, hPL)."
            ]},
            { heading: "Placenta as a working organ", body: [
              "Exchange site: oxygen, nutrients, and wastes diffuse between maternal and fetal blood, but the two circulations never mix.",
              "Endocrine organ: secretes the hormones that maintain pregnancy.",
              "Filter (imperfect): many drugs, alcohol, and infections cross to the fetus."
            ]},
            { heading: "Maternal physiology by trimester", body: [
              "First trimester: high hCG, fatigue, nausea common. Cardiac output begins rising.",
              "Second trimester: maternal blood volume up about 40%; heart rate rises modestly; uterus enlarges out of the pelvis.",
              "Third trimester: pressure on diaphragm shortens breath; venous return from legs slowed by uterine compression; risk of preeclampsia rises."
            ]}
          ],
          cards: [
            { id: "c1", dok: 1, q: "Where does fertilization typically occur?", a: "In the ampulla of the uterine (fallopian) tube." },
            { id: "c2", dok: 1, q: "What does hCG do in early pregnancy?", a: "Maintains the corpus luteum so it continues producing progesterone until the placenta takes over." },
            { id: "c3", dok: 1, q: "When does implantation occur after fertilization?", a: "Around day 6-7." },
            { id: "c4", dok: 1, q: "When does the placenta take over hormone production from the corpus luteum?", a: "By the end of the first trimester." },
            { id: "c5", dok: 2, q: "Why does maternal blood volume rise during pregnancy?", a: "To supply the growing placenta and fetus, support increased renal filtration, and provide a reserve for blood loss at delivery. Plasma volume rises more than red cell mass, producing the physiologic anemia of pregnancy." },
            { id: "c6", dok: 2, q: "Explain why home pregnancy tests target hCG rather than other hormones.", a: "Only trophoblast tissue makes hCG, and levels rise quickly after implantation. It is specific to pregnancy and detectable in urine within days of a missed period." },
            { id: "c7", dok: 3, q: "A third-trimester patient becomes dizzy when lying flat on her back. Predict the cause and the management.", a: "The enlarged uterus compresses the inferior vena cava when supine, dropping venous return, stroke volume, and blood pressure. Roll the patient to her left side to relieve the compression." }
          ]
        }

      ]
    }

  ]
};
