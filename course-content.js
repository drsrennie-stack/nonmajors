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
            { id: "c1", dok: 1, q: "List the levels of structural organization from smallest to largest.", a: "Chemical, cellular, tissue, organ, organ system, organism.", options: ["Cellular, chemical, organ, tissue, organism, organ system.", "Chemical, cellular, tissue, organ, organ system, organism.", "Atomic, molecular, organelle, cell, organ, body.", "Cell, tissue, organ system, organ, organism, population."], correctIndex: 1, explanation: "The standard hierarchy from smallest to largest is chemical, cellular, tissue, organ, organ system, organism. The first option scrambles the order, swapping chemical and cellular and placing organ before tissue. The third option uses non-standard labels (atomic/molecular/organelle) that are not the recognized A&P levels. The fourth option puts organ system before organ and tacks on 'population,' which belongs to ecology, not human A&P." },
            { id: "c2", dok: 1, q: "How many organ systems make up the human body?", a: "Eleven.", options: ["Ten.", "Twelve.", "Eleven.", "Nine."], correctIndex: 2, explanation: "There are eleven organ systems in the human body (integumentary, skeletal, muscular, nervous, endocrine, cardiovascular, lymphatic, respiratory, digestive, urinary, reproductive). Ten and nine undercount, often by collapsing lymphatic into cardiovascular or omitting endocrine. Twelve overcounts, usually by splitting one system into two." },
            { id: "c3", dok: 1, q: "Define tissue.", a: "A group of similar cells that work together to perform a common function.", options: ["A single specialized cell that performs a unique function on its own.", "A group of similar cells that work together to perform a common function.", "A collection of organs working together toward a shared physiological goal.", "Any non-cellular material that fills spaces between cells in the body."], correctIndex: 1, explanation: "A tissue is a group of similar cells (often with their extracellular matrix) that work together to perform a common function. A single cell, no matter how specialized, is not a tissue. A group of organs working together is an organ system, the level above organ. Non-cellular material between cells is extracellular matrix, a component of some tissues but not the definition of tissue itself." },
            { id: "c4", dok: 1, q: "At which level of organization do organelles appear?", a: "The cellular level (organelles are subcellular structures inside a cell).", options: ["The chemical level, since organelles are made of molecules.", "The tissue level, since organelles are shared among neighboring cells.", "The organ level, since organelles function like miniature organs.", "The cellular level, since organelles are subcellular structures inside a cell."], correctIndex: 3, explanation: "Organelles appear at the cellular level because they are subcellular structures that live inside a single cell. They are made of molecules but the level of organization refers to where the structure exists as a functional unit, which is the cell. Organelles are not shared between cells, so they are not a tissue feature. Calling them 'miniature organs' is a useful analogy but does not place them at the organ level." },
            { id: "c5", dok: 2, q: "Why is the cardiovascular system considered to be at the organ-system level, not the organ level?", a: "It includes multiple organs (heart, blood vessels) plus blood, working together toward a shared function (transport). Any single one of these on its own is just an organ.", options: ["Because the heart by itself contains all the tissue types of the body, so it qualifies as a system on its own.", "Because blood vessels are not considered organs, so any group containing them is automatically a system.", "Because it includes multiple organs (heart, blood vessels) plus blood, working together toward a shared transport function.", "Because the cardiovascular system is the largest by volume, and size determines the level of organization."], correctIndex: 2, explanation: "The cardiovascular system is at the organ-system level because multiple organs (heart and blood vessels) plus the fluid tissue blood work together toward a shared function (transport). The heart alone is just one organ, regardless of how many tissue types it contains. Blood vessels are organs (they contain multiple tissue types). Size is not the criterion for level of organization, integration of multiple organs toward a common function is." },
            { id: "c6", dok: 2, q: "Give an example of an organ that participates in more than one organ system.", a: "Pancreas (endocrine and digestive). Liver (digestive and several others). Kidney (urinary and endocrine, since it makes erythropoietin and renin).", options: ["Spleen (only in the lymphatic system).", "Pancreas (endocrine and digestive).", "Trachea (respiratory only).", "Urinary bladder (urinary only)."], correctIndex: 1, explanation: "The pancreas participates in both the endocrine system (insulin, glucagon) and the digestive system (pancreatic enzymes and bicarbonate). The spleen is primarily a lymphatic organ and is not a strong multi-system example. The trachea is part of the respiratory system only. The urinary bladder is part of the urinary system only." },
            { id: "c7", dok: 3, q: "A drug damages mitochondrial function in skeletal muscle. Predict the cascading effects up the levels of organization.", a: "Cellular level: ATP supply drops, fiber fatigue. Tissue level: muscle tissue weakens and can no longer hold prolonged contractions. Organ level: skeletal muscles tire quickly. Organ system level: posture, locomotion, and breathing (respiratory muscles) become impaired. Organism: exercise intolerance and, in severe cases, respiratory failure.", options: ["No effect, since mitochondria function only at the chemical level and do not influence tissues or organs.", "Cellular ATP supply drops, muscle fibers fatigue, skeletal muscles weaken, and at the system level posture, locomotion, and breathing become impaired.", "Only the affected muscle cells die, with no ripple effects to the organ or organism level.", "Cardiac muscle fails first because skeletal muscle damage propagates to the heart through shared mitochondria."], correctIndex: 1, explanation: "Mitochondrial damage cuts ATP supply at the cellular level, which causes fiber fatigue in the tissue, weakness at the organ level, and impaired posture/locomotion/respiration at the system and organism levels. The first option ignores that lower-level changes always cascade upward. Cells do more than die when ATP drops, they fatigue and dysfunction across the hierarchy. Skeletal and cardiac muscle have separate mitochondria, so damage does not transfer between them through shared organelles." }
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
            { id: "c1", dok: 1, q: "What plane divides the body into right and left equal halves?", a: "The midsagittal (median) plane.", options: ["The frontal (coronal) plane.", "The transverse (horizontal) plane.", "The midsagittal (median) plane.", "The oblique plane."], correctIndex: 2, explanation: "The midsagittal (median) plane is the vertical plane that passes through the midline and divides the body into equal right and left halves. The frontal plane separates anterior from posterior, not right from left. The transverse plane separates superior from inferior. An oblique plane runs at an angle and does not produce equal halves." },
            { id: "c2", dok: 1, q: "Is the knee proximal or distal to the ankle?", a: "Proximal.", options: ["Distal.", "Proximal.", "Superficial.", "Inferior."], correctIndex: 1, explanation: "The knee is proximal to the ankle because it sits closer to the point of attachment of the limb to the trunk. Distal means farther from that attachment, which describes the ankle relative to the knee. Superficial refers to depth, not limb position. Inferior is a whole-body directional term used in anatomical position, not the preferred limb term." },
            { id: "c3", dok: 1, q: "Which cavity contains the lungs?", a: "The thoracic cavity (specifically the pleural cavities) within the ventral body cavity.", options: ["The abdominal cavity, just below the diaphragm.", "The pericardial cavity, surrounding the heart.", "The cranial cavity, posterior to the sternum.", "The thoracic cavity, within the pleural cavities of the ventral body cavity."], correctIndex: 3, explanation: "The lungs sit in the thoracic cavity, each enclosed in its own pleural cavity, which is part of the ventral body cavity. The abdominal cavity holds digestive organs, not the lungs. The pericardial cavity surrounds the heart only. The cranial cavity holds the brain and is in the skull, not behind the sternum." },
            { id: "c4", dok: 1, q: "Name the four abdominal quadrants.", a: "Right upper, left upper, right lower, left lower (RUQ, LUQ, RLQ, LLQ).", options: ["Right upper, left upper, right lower, left lower (RUQ, LUQ, RLQ, LLQ).", "Epigastric, umbilical, hypogastric, and pelvic.", "Thoracic, abdominal, pelvic, and perineal.", "Anterior, posterior, lateral, and medial."], correctIndex: 0, explanation: "The four abdominal quadrants are RUQ, LUQ, RLQ, and LLQ, formed by one vertical and one horizontal line crossing at the umbilicus. The epigastric/umbilical/hypogastric labels belong to the nine-region system, not the quadrant system. Thoracic/abdominal/pelvic/perineal name body regions or cavities, not abdominal subdivisions. Anterior/posterior/lateral/medial are directional terms, not regions." },
            { id: "c5", dok: 2, q: "Explain why anatomical position is the reference for all directional terms, even when a patient is lying down.", a: "It is a fixed reference frame. If terms changed based on the patient's posture, the same anatomical relationship could have two opposite descriptions. Anatomical position keeps the vocabulary consistent and unambiguous.", options: ["Because every clinical setting uses the same imaging equipment, so terms are tied to the scanner orientation.", "Because anatomical position is a fixed reference frame, so the same anatomical relationship has only one description regardless of how the patient is lying.", "Because anatomical position matches how patients naturally stand during exams, making it the most realistic posture.", "Because directional terms only apply to standing patients and lose meaning when a patient lies down."], correctIndex: 1, explanation: "Anatomical position works as a fixed reference frame so that terms like superior, anterior, and medial keep a single meaning regardless of posture. Imaging equipment does not standardize the vocabulary, the vocabulary standardizes the imaging. The position is not chosen for realism, since most patients are not standing during exams. Directional terms still apply when patients lie down, precisely because they are anchored to anatomical position." },
            { id: "c6", dok: 2, q: "A patient has pain in the right upper quadrant. Name two organs that could plausibly be the source.", a: "Liver, gallbladder, right kidney (technically retroperitoneal), part of the stomach, head of the pancreas, hepatic flexure of the colon.", options: ["Spleen and descending colon.", "Sigmoid colon and urinary bladder.", "Appendix and right ovary.", "Liver and gallbladder."], correctIndex: 3, explanation: "The liver and gallbladder both sit in the right upper quadrant and are the most common RUQ pain sources. The spleen and descending colon are in the LUQ and LLQ. The sigmoid colon and bladder sit in the lower quadrants and pelvis. The appendix and right ovary localize to the RLQ, not the RUQ." },
            { id: "c7", dok: 3, q: "A radiologist describes a tumor as 'medial to the right lung, superior to the diaphragm, anterior to the vertebral column.' Locate the structure and name the body cavity it sits in.", a: "Mediastinum of the thoracic cavity. The tumor is likely in the central mediastinum, between the lungs, above the diaphragm, and in front of the spine.", options: ["Pleural cavity, on the surface of the right lung.", "Pericardial cavity, inside the heart sac.", "Mediastinum of the thoracic cavity, between the lungs and above the diaphragm.", "Abdominal cavity, just below the diaphragm."], correctIndex: 2, explanation: "A structure medial to the right lung, superior to the diaphragm, and anterior to the vertebral column is in the mediastinum, the central compartment of the thoracic cavity. The pleural cavity hugs the lung itself, not the central space between lungs. The pericardial cavity is inside the mediastinum but is a much smaller subspace around the heart. The abdominal cavity is inferior to the diaphragm, not superior." }
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
            { id: "c1", dok: 1, q: "Define homeostasis.", a: "The maintenance of a relatively stable internal environment despite external change.", options: ["The maintenance of a relatively stable internal environment despite external change.", "The continuous growth and increase in complexity of an organism over time.", "The ability of cells to divide rapidly in response to injury or stress.", "The transfer of genetic information from one generation to the next."], correctIndex: 0, explanation: "Homeostasis is the maintenance of a relatively stable internal environment (temperature, pH, glucose, osmolarity) despite changing external conditions. Growth and increasing complexity describe development, not homeostasis. Rapid cell division in response to injury is part of wound healing or hyperplasia. Transfer of genetic information across generations is heredity, a separate concept." },
            { id: "c2", dok: 1, q: "List the four core components of a negative feedback loop.", a: "Stimulus, receptor, control center, effector (with a response that opposes the change).", options: ["Set point, hormone, target tissue, response.", "Stimulus, receptor, control center, effector.", "Input, processor, output, feedback delay.", "Sensor, amplifier, hormone, organ."], correctIndex: 1, explanation: "A negative feedback loop has four components: a stimulus (the change), a receptor that detects it, a control center that processes the signal, and an effector that produces the response. Hormones and target tissues are common effectors but are not the universal labels. Engineering language like 'processor' and 'feedback delay' is not the standard physiology vocabulary. Amplification belongs to positive feedback, not the canonical negative-feedback components." },
            { id: "c3", dok: 1, q: "Which feedback type is most common in physiology?", a: "Negative feedback.", options: ["Positive feedback.", "Feed-forward regulation.", "Tonic control.", "Negative feedback."], correctIndex: 3, explanation: "Negative feedback is the most common type in physiology because it stabilizes regulated variables around a set point. Positive feedback is rare and reserved for processes that need a definitive end point (childbirth, blood clotting). Feed-forward regulation is anticipatory and not the dominant mode. Tonic control describes baseline activity, not the predominant feedback architecture." },
            { id: "c4", dok: 1, q: "Give one example of a regulated variable.", a: "Core body temperature, blood glucose, blood pH, blood pressure, blood osmolarity, or arterial pO2.", options: ["Eye color.", "Number of fingers.", "Core body temperature.", "Height in adulthood."], correctIndex: 2, explanation: "Core body temperature is a classic regulated variable, held near 37 C by negative feedback. Eye color is genetically determined and not actively regulated minute to minute. Finger number is anatomical and fixed after development. Adult height is the end state of growth and is not held to a set point by feedback loops." },
            { id: "c5", dok: 2, q: "Explain how negative feedback returns body temperature to set point after exercise.", a: "Thermoreceptors detect a rise. The hypothalamus signals sweating and cutaneous vasodilation. Heat is lost. Core temperature falls back toward set point.", options: ["Pyrogens reset the hypothalamic set point upward, so the body produces fever by shivering.", "Thermoreceptors detect the rise, the hypothalamus triggers sweating and cutaneous vasodilation, heat is lost, and temperature falls back toward set point.", "Skeletal muscle stops producing heat entirely until temperature returns to baseline.", "Positive feedback amplifies the temperature rise until exercise ends."], correctIndex: 1, explanation: "After exercise raises core temperature, thermoreceptors detect the rise, the hypothalamus (control center) drives sweating and skin vasodilation (effectors), heat dissipates, and temperature returns to set point. Pyrogens describe fever, not exercise recovery. Skeletal muscle does not stop producing heat on demand. Positive feedback would worsen the rise, the opposite of what negative feedback achieves." },
            { id: "c6", dok: 2, q: "Contrast negative and positive feedback in terms of their effect on the original stimulus.", a: "Negative feedback opposes the change and stabilizes the variable. Positive feedback amplifies the change and drives the system to an end point.", options: ["Both oppose the original stimulus, but positive feedback does so more quickly.", "Negative feedback opposes the change and stabilizes the variable, while positive feedback amplifies the change and drives the system to an end point.", "Both amplify the original stimulus, but negative feedback uses hormones and positive feedback uses nerves.", "Negative feedback only operates in healthy people, while positive feedback only appears in disease."], correctIndex: 1, explanation: "Negative feedback reverses the change to keep a variable near set point, while positive feedback amplifies the change to drive a process to completion (such as childbirth or clotting). Both do not oppose the stimulus, positive feedback amplifies it. Both do not amplify, that is positive feedback only. Positive feedback is a normal physiological mechanism, not a disease signature." },
            { id: "c7", dok: 3, q: "Predict what happens to a patient whose hypothalamic set point for temperature is reset upward by pyrogens.", a: "The body treats normal temperature as too low. Vasoconstriction and shivering raise core temperature to the new set point. When pyrogens clear, the set point falls and the patient sweats to dump heat.", options: ["The body sweats and vasodilates as if temperature were too high, lowering core temperature dangerously.", "Nothing changes, because the set point is not adjustable.", "The body treats normal temperature as too low, so vasoconstriction and shivering raise core temperature to the new set point (fever). When pyrogens clear, the set point falls and the patient sweats.", "Positive feedback amplifies the change until temperature reaches a lethal level regardless of pyrogen status."], correctIndex: 2, explanation: "Pyrogens raise the hypothalamic set point, so the previously normal temperature is now read as too low, triggering vasoconstriction and shivering to drive temperature up (fever). When pyrogens clear, the set point drops and the body sheds the extra heat by sweating. The body does not sweat at the start of fever, that comes during defervescence. Set points are adjustable, that is exactly what pyrogens exploit. Negative feedback, not unbounded positive feedback, regulates the new fever set point." },
            { id: "c8", dok: 3, q: "A patient with type 1 diabetes has lost the ability to make insulin. Analyze how this breaks the glucose feedback loop.", a: "Insulin is the effector signal that lowers blood glucose. Without it, the loop has no functioning effector. Receptors detect the post-meal spike but no response brings glucose back to set point, so it stays elevated.", options: ["Insulin receptors disappear, so glucose never enters the loop, and blood glucose stays at zero.", "Glucagon stops working too, so blood glucose drops below set point.", "Insulin is the effector signal that lowers blood glucose. Without it, the loop has no functioning effector, so glucose stays elevated after meals.", "Receptors fail to detect glucose changes, so the patient never feels post-meal symptoms."], correctIndex: 2, explanation: "In type 1 diabetes, the pancreas cannot make insulin, which is the effector signal that lowers blood glucose. Receptors still detect the post-meal rise but no effector response is delivered, so glucose stays elevated (hyperglycemia). Insulin receptors are present (just unreached), and glucose is high, not zero. Glucagon is a separate hormone made by alpha cells and is not destroyed in type 1 diabetes. The detection step is intact, the effector step is missing." }
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
            { id: "c1", dok: 1, q: "Where does cellular respiration occur?", a: "In the mitochondria.", options: ["In the nucleus.", "In the rough endoplasmic reticulum.", "In the mitochondria.", "In the Golgi apparatus."], correctIndex: 2, explanation: "Cellular respiration (the oxygen-using ATP-producing pathways, the citric acid cycle and oxidative phosphorylation) occurs in the mitochondria. The nucleus stores DNA and produces RNA, not ATP. The rough ER makes and folds proteins for secretion. The Golgi modifies and sorts those proteins, neither does respiration." },
            { id: "c2", dok: 1, q: "What is the function of the Golgi apparatus?", a: "Modifies, sorts, and packages proteins received from the rough ER.", options: ["Modifies, sorts, and packages proteins received from the rough ER.", "Synthesizes the cell's ATP supply through oxidative phosphorylation.", "Digests cellular debris and worn-out organelles inside the cell.", "Stores DNA and controls gene expression for the cell."], correctIndex: 0, explanation: "The Golgi apparatus receives proteins from the rough ER, then modifies them (adding sugars and other tags), sorts them by destination, and packages them into vesicles. ATP production is the job of mitochondria. Intracellular digestion is the job of lysosomes. DNA storage and gene-expression control belong to the nucleus." },
            { id: "c3", dok: 1, q: "Which organelle digests cellular debris?", a: "Lysosome.", options: ["Peroxisome.", "Lysosome.", "Centriole.", "Smooth ER."], correctIndex: 1, explanation: "Lysosomes are membrane-bound sacs of hydrolytic enzymes that digest cellular debris, damaged organelles, and engulfed material. Peroxisomes do break down some molecules (fatty acids, hydrogen peroxide) but are not the main cellular debris digesters. Centrioles organize microtubules during cell division. Smooth ER synthesizes lipids and detoxifies, it does not digest debris." },
            { id: "c4", dok: 1, q: "Which organelle makes ribosomal RNA?", a: "The nucleolus.", options: ["The rough endoplasmic reticulum.", "The mitochondrion.", "The Golgi apparatus.", "The nucleolus."], correctIndex: 3, explanation: "The nucleolus, a dense region inside the nucleus, makes ribosomal RNA and assembles ribosome subunits. The rough ER hosts ribosomes once assembled, but does not make rRNA. Mitochondria have their own small ribosomes and rRNA, but cellular rRNA production is a nucleolar job. The Golgi works on proteins, not on rRNA." },
            { id: "c5", dok: 2, q: "Why would a cell that secretes a lot of protein (like a pancreatic acinar cell) have abundant rough ER?", a: "Rough ER ribosomes synthesize secreted proteins and pass them into the ER lumen for folding and trafficking. Cells with heavy secretory output need a large rough ER to keep up.", options: ["Because rough ER stores all the cell's ATP, and secretion is energy-intensive.", "Because rough ER ribosomes synthesize secreted proteins and pass them into the ER lumen for folding and trafficking, so heavy secretory output needs a large rough ER.", "Because rough ER digests waste from neighboring cells and secretion produces a lot of waste.", "Because rough ER replaces the nucleus in highly active cells."], correctIndex: 1, explanation: "Rough ER ribosomes synthesize proteins destined for secretion, threading them into the ER lumen for folding and forwarding to the Golgi. Cells that secrete heavily (pancreatic acinar, plasma cells) expand their rough ER to keep up. The rough ER does not store ATP, that comes from mitochondria. It does not digest waste, that is the lysosome. It never replaces the nucleus, which all cells (except mature red blood cells) retain." },
            { id: "c6", dok: 2, q: "Cardiac muscle cells have unusually large numbers of mitochondria. Why?", a: "They contract continuously and have very high ATP demands. More mitochondria means more ATP production capacity.", options: ["Cardiac cells store oxygen in their mitochondria for use during diving reflexes.", "Mitochondria are needed to hold the cell together physically in a beating heart.", "Cardiac cells use mitochondria to make new heart cells continuously.", "Cardiac cells contract continuously and have very high ATP demands, so more mitochondria means more ATP capacity."], correctIndex: 3, explanation: "Cardiac muscle never rests, so ATP demand is high and sustained. More mitochondria per cell means more aerobic ATP production to keep up. Mitochondria do not store oxygen, hemoglobin and myoglobin do. They do not provide structural support, the cytoskeleton does. Cardiac cells generally do not divide to make new heart cells, so mitochondria are not for replication." },
            { id: "c7", dok: 3, q: "A genetic defect prevents lysosomal enzymes from being tagged for transport to the lysosome. Predict the cellular consequence over time.", a: "Undigested debris and substrates accumulate inside the lysosome. The organelle swells, cell function degrades, and the patient develops a lysosomal storage disease (such as I-cell disease).", options: ["The cell stops making lysosomal enzymes entirely.", "Enzymes accumulate in the nucleus and stop DNA replication.", "Undigested debris and substrates build up inside the lysosome, the organelle swells, cell function degrades, and a lysosomal storage disease develops.", "Lysosomes rupture immediately, releasing enzymes that kill the cell within minutes."], correctIndex: 2, explanation: "Without the tag that targets enzymes to the lysosome, the enzymes are secreted instead. Substrates inside the lysosome are not digested, so they accumulate, the organelle swells, and over time cells and tissues fail (lysosomal storage disease, for example I-cell disease). Enzymes are still made, they are just mis-routed. The nucleus is not the destination. Lysosomes do not rupture immediately, the damage is slow accumulation, not rapid lysis." }
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
            { id: "c1", dok: 1, q: "Define diffusion.", a: "Net movement of solute from a region of higher concentration to one of lower concentration.", options: ["Movement of solute from high to low concentration that always requires ATP.", "Movement of water across a membrane down its osmotic gradient.", "Net movement of solute from a region of higher concentration to one of lower concentration.", "Movement of solute against its concentration gradient using a carrier protein."], correctIndex: 2, explanation: "Diffusion is the net movement of solute from higher to lower concentration, driven by random molecular motion and the concentration gradient. It does not require ATP, that distinguishes it from active transport. Movement of water across a membrane is osmosis, not diffusion of solute. Movement against the gradient with a carrier defines active transport, the opposite of diffusion." },
            { id: "c2", dok: 1, q: "Which transport type uses ATP directly?", a: "Primary active transport.", options: ["Facilitated diffusion.", "Osmosis.", "Simple diffusion.", "Primary active transport."], correctIndex: 3, explanation: "Primary active transport uses ATP directly to move solutes against their gradients (the Na+/K+ ATPase is the classic example). Facilitated diffusion uses carriers or channels but moves solutes down their gradient without ATP. Osmosis is passive water movement. Simple diffusion uses no protein and no ATP, just the gradient." },
            { id: "c3", dok: 1, q: "Name two molecules that cross by simple diffusion.", a: "Oxygen, carbon dioxide, steroid hormones, small lipids.", options: ["Glucose and amino acids.", "Sodium and potassium ions.", "Oxygen and carbon dioxide.", "Large proteins and nucleic acids."], correctIndex: 2, explanation: "Small, nonpolar molecules like O2 and CO2 cross the lipid bilayer by simple diffusion. Glucose and amino acids are polar and need carrier proteins (facilitated diffusion or secondary active transport). Charged ions like Na+ and K+ require channels or pumps. Large proteins and nucleic acids are too big for simple diffusion and require vesicular transport." },
            { id: "c4", dok: 1, q: "What is the stoichiometry of the Na⁺/K⁺ ATPase?", a: "Three Na⁺ out, two K⁺ in, per ATP.", options: ["Two Na+ out, three K+ in, per ATP.", "Three Na+ in, two K+ out, per ATP.", "One Na+ out, one K+ in, per ATP.", "Three Na+ out, two K+ in, per ATP."], correctIndex: 3, explanation: "The Na+/K+ ATPase moves three Na+ out and two K+ in for every ATP hydrolyzed, producing the electrochemical gradient that powers many secondary transporters. The first option reverses the numbers (2 out, 3 in). The second option reverses the direction (Na+ in, K+ out), which is the opposite of how the pump works. A 1-to-1 stoichiometry is incorrect and would not generate the net charge separation the cell needs." },
            { id: "c5", dok: 2, q: "How does the Na⁺/K⁺ ATPase enable secondary active transport?", a: "It builds and maintains the inward Na⁺ gradient. Secondary transporters use that gradient as energy to move other solutes against their own gradients.", options: ["It directly transports glucose into cells, so glucose absorption is its main job.", "It builds and maintains the inward Na+ gradient, and secondary transporters use that gradient as energy to move other solutes against their own gradients.", "It produces ATP that powers all other transporters in the cell.", "It hydrolyzes the substrate molecules so they can cross the membrane more easily."], correctIndex: 1, explanation: "The Na+/K+ ATPase keeps intracellular Na+ low, maintaining a steep inward Na+ gradient. Secondary active transporters (such as the Na+-glucose symporter) tap that gradient as energy to co-transport other solutes against their own gradients. The pump does not transport glucose directly. It uses ATP, it does not produce it. It does not hydrolyze substrates, it hydrolyzes ATP." },
            { id: "c6", dok: 2, q: "Predict water movement when a red blood cell is placed in a hypertonic solution.", a: "Water exits the cell. The cell crenates (shrinks).", options: ["Water enters the cell, which swells and may lyse.", "Water exits the cell, which crenates (shrinks).", "No net water movement occurs, because RBC membranes are impermeable to water.", "Water enters the cell but solutes also leave, so volume stays constant."], correctIndex: 1, explanation: "A hypertonic solution has a higher solute concentration than the cytoplasm, so water moves out of the cell by osmosis and the RBC crenates (shrivels). Water entry and lysis occur in hypotonic solutions, the opposite scenario. RBC membranes are highly water-permeable due to aquaporins. Solute movement does not balance water loss here, the net effect is shrinkage." },
            { id: "c7", dok: 3, q: "Ouabain blocks the Na⁺/K⁺ ATPase. Predict the effect on glucose absorption in the small intestine.", a: "Intracellular Na⁺ rises, the Na⁺ gradient collapses, the Na⁺-glucose symporter loses its driving force, and glucose absorption falls sharply.", options: ["Glucose absorption rises because the symporter no longer faces competition from Na+.", "Intracellular Na+ rises, the Na+ gradient collapses, the Na+-glucose symporter loses its driving force, and glucose absorption falls sharply.", "Glucose absorption is unaffected because it does not depend on the Na+/K+ ATPase.", "Glucose is pumped out of the cell instead of in, due to reversed gradients."], correctIndex: 1, explanation: "Ouabain blocks the Na+/K+ ATPase, so intracellular Na+ rises, the inward Na+ gradient collapses, and the Na+-glucose symporter loses the energy source that lets it move glucose against its gradient. Glucose absorption falls. The symporter needs the Na+ gradient (it is not competition). Glucose absorption in enterocytes does depend on the pump indirectly through that gradient. Glucose is not actively pumped out, the transporter just stops working." },
            { id: "c8", dok: 3, q: "Design an experiment to distinguish simple from facilitated diffusion of a solute.", a: "Measure flux versus solute concentration. Simple diffusion: linear, non-saturating. Facilitated diffusion: saturates because carriers are finite.", options: ["Add a metabolic inhibitor and see whether the solute still crosses.", "Measure membrane voltage at different solute concentrations.", "Measure flux versus solute concentration: simple diffusion is linear and non-saturating, while facilitated diffusion saturates because carriers are finite.", "Compare uptake at 37 C versus 4 C and call any temperature effect facilitated."], correctIndex: 2, explanation: "Plotting flux against solute concentration is the cleanest discriminator. Simple diffusion gives a straight line because there is no carrier to saturate. Facilitated diffusion plateaus once all carriers are occupied. A metabolic inhibitor mainly distinguishes active from passive transport, not the two passive types. Membrane voltage tracks charged solutes, not all solutes. Temperature affects both processes, so it cannot uniquely identify facilitated diffusion." }
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
            { id: "c1", dok: 1, q: "What does the first name of an epithelium tell you?", a: "Number of cell layers (simple = one, stratified = two or more).", options: ["Number of cell layers (simple means one layer, stratified means two or more).", "The shape of the cells (squamous, cuboidal, columnar).", "Whether the tissue is secretory or absorptive in function.", "Whether the tissue rests on a basement membrane."], correctIndex: 0, explanation: "The first name (simple or stratified) tells you the number of cell layers. The shape of the cells is the second name in the label (squamous, cuboidal, columnar). Secretory/absorptive function is not part of the naming convention. All epithelia rest on a basement membrane, so that fact cannot distinguish types." },
            { id: "c2", dok: 1, q: "Where is simple squamous epithelium found?", a: "Alveoli of the lung and the endothelium of blood vessels.", options: ["The lining of the urinary bladder.", "The epidermis of the skin.", "Alveoli of the lung and endothelium of blood vessels.", "The lining of the small intestine."], correctIndex: 2, explanation: "Simple squamous epithelium is found where rapid diffusion or filtration is the priority: alveoli (gas exchange) and endothelium of vessels (exchange and smooth blood flow). The bladder is lined with transitional epithelium that stretches. The epidermis is stratified squamous for protection. The small intestine is simple columnar with microvilli for absorption." },
            { id: "c3", dok: 1, q: "Name the epithelium of the urinary bladder.", a: "Transitional epithelium.", options: ["Stratified squamous epithelium.", "Pseudostratified columnar epithelium.", "Simple cuboidal epithelium.", "Transitional epithelium."], correctIndex: 3, explanation: "The urinary bladder is lined with transitional epithelium, which can change shape to accommodate stretch as the bladder fills. Stratified squamous lines surfaces facing abrasion (skin, esophagus). Pseudostratified columnar lines parts of the airway. Simple cuboidal lines kidney tubules and small ducts, not the bladder." },
            { id: "c4", dok: 1, q: "What is the function of stratified squamous epithelium?", a: "Protection from abrasion.", options: ["Filtration of plasma.", "Active transport of nutrients.", "Secretion of hormones into blood.", "Protection from abrasion."], correctIndex: 3, explanation: "Stratified squamous epithelium specializes in protection from abrasion, which is why it covers the skin, esophagus, and vagina. Filtration is the job of very thin epithelia like Bowman's capsule (simple squamous). Active transport of nutrients suits simple columnar epithelium with microvilli. Hormone secretion is handled by glandular epithelial cells, often in endocrine organs, not by stratified squamous sheets." },
            { id: "c5", dok: 2, q: "Why are alveoli lined with simple squamous rather than columnar epithelium?", a: "Their job is gas exchange by diffusion. A single flat layer minimizes diffusion distance.", options: ["A thicker layer would secrete more mucus, which would block gas exchange.", "Their job is gas exchange by diffusion, so a single flat layer minimizes diffusion distance.", "Columnar epithelium cannot survive the high oxygen environment of the alveoli.", "Squamous cells are the only cell type that can divide fast enough to repair alveoli."], correctIndex: 1, explanation: "Alveoli exchange oxygen and carbon dioxide by simple diffusion, and a thin single layer of flat (squamous) cells keeps the diffusion path short. Mucus production is not the limiting factor (alveoli themselves do not produce mucus). Columnar cells are not poisoned by oxygen, they are just too thick. Squamous cells are not uniquely good at repair, in fact alveolar repair comes largely from type II pneumocytes (cuboidal)." },
            { id: "c6", dok: 2, q: "Why does pseudostratified columnar epithelium look stratified even though it is not?", a: "Cell nuclei sit at different heights. Every cell still contacts the basement membrane, so it is truly one layer.", options: ["Some of its cells lack a basement membrane, which makes it look layered.", "It loses cells in a layered pattern during desquamation.", "Cell nuclei sit at different heights, but every cell still contacts the basement membrane, so it is truly one layer.", "It alternates between simple and stratified arrangements depending on the time of day."], correctIndex: 2, explanation: "Pseudostratified columnar looks layered because the nuclei sit at different heights in cells of different sizes. Every cell still touches the basement membrane, so anatomically it is one layer (pseudo means 'false'). All cells share the basement membrane in this tissue, so missing basement membrane is incorrect. Desquamation is not the reason for the layered look. The tissue does not switch architectures with time of day." },
            { id: "c7", dok: 3, q: "A smoker has metaplasia of the upper airway: pseudostratified ciliated columnar is replaced by stratified squamous. Predict two functional consequences.", a: "Loss of cilia abolishes mucociliary clearance, so pathogens linger. The new epithelium is also less able to secrete mucus, raising infection risk.", options: ["Vitamin D production rises, raising calcium absorption.", "Loss of cilia abolishes mucociliary clearance so pathogens linger, and the new epithelium secretes less mucus, raising infection risk.", "Gas exchange improves because squamous is thinner than columnar.", "The airway becomes more flexible, improving lung compliance."], correctIndex: 1, explanation: "Stratified squamous lacks cilia and goblet cells, so mucociliary clearance fails and mucus output drops, leaving the airway vulnerable to pathogens and particulates. Vitamin D production is a skin function, unrelated to airway epithelium. Gas exchange happens in alveoli, not the upper airway, so the change does not improve it. Compliance is set by elastic tissue, not by epithelial type." }
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
            { id: "c1", dok: 1, q: "What three things make up the extracellular matrix?", a: "Ground substance, protein fibers, and water.", options: ["Ground substance, protein fibers, and water.", "Cells, nucleus, and cytoplasm.", "Collagen, elastin, and reticulin only.", "Basement membrane, lamina propria, and capsule."], correctIndex: 0, explanation: "The extracellular matrix has three components: ground substance (a gel of proteoglycans and glycoproteins), protein fibers (collagen, elastic, reticular), and water. Cells, nucleus, and cytoplasm describe what is inside a cell, not the matrix. Collagen, elastin, and reticulin name only the fiber subtypes, missing ground substance and water. Basement membrane and lamina propria are layers found at epithelial interfaces, not the universal ECM components." },
            { id: "c2", dok: 1, q: "Which connective tissue type makes up tendons?", a: "Dense regular connective tissue.", options: ["Loose areolar connective tissue.", "Dense regular connective tissue.", "Reticular connective tissue.", "Elastic cartilage."], correctIndex: 1, explanation: "Tendons are dense regular connective tissue, packed with parallel collagen fibers that resist tensile load along one axis. Loose areolar is the all-purpose packing tissue between organs, not built for tension. Reticular connective tissue forms the supportive mesh of lymphoid organs. Elastic cartilage gives shape to the ear and epiglottis, not strength to a tendon." },
            { id: "c3", dok: 1, q: "Which cell builds the protein fibers of most connective tissues?", a: "Fibroblast.", options: ["Macrophage.", "Osteoclast.", "Fibroblast.", "Mast cell."], correctIndex: 2, explanation: "Fibroblasts are the resident cell of most connective tissues and produce the collagen, elastic, and reticular fibers along with ground substance components. Macrophages are immune cells that engulf debris and pathogens. Osteoclasts resorb bone, they do not build fibers. Mast cells release histamine and other mediators in inflammation." },
            { id: "c4", dok: 1, q: "What kind of cartilage is in intervertebral discs?", a: "Fibrocartilage.", options: ["Hyaline cartilage.", "Elastic cartilage.", "Fibrocartilage.", "Articular cartilage."], correctIndex: 2, explanation: "Intervertebral discs contain fibrocartilage in their outer rings, designed to resist compression and tensile load between vertebrae. Hyaline cartilage covers joint surfaces and the ends of long bones, but is not the disc tissue. Elastic cartilage is in the ear and epiglottis. 'Articular cartilage' is the hyaline cartilage on joint surfaces, not the disc." },
            { id: "c5", dok: 2, q: "Why does cartilage heal so much more slowly than bone?", a: "Cartilage is avascular. Chondrocytes get nutrients by diffusion from surrounding tissue. Without a direct blood supply, repair cells, oxygen, and nutrients arrive slowly.", options: ["Because cartilage cells divide more slowly than bone cells by genetic programming.", "Because cartilage is avascular: chondrocytes get nutrients by diffusion, so repair cells, oxygen, and nutrients arrive slowly.", "Because cartilage is innervated densely and pain blocks the healing response.", "Because cartilage has no extracellular matrix to support new growth."], correctIndex: 1, explanation: "Cartilage is avascular: chondrocytes receive nutrients by diffusion through the matrix, so repair cells, oxygen, and nutrients arrive slowly compared to vascularized bone. The cell division rate is not the rate-limiting issue, blood supply is. Cartilage actually has very little innervation, not dense innervation. Cartilage has an abundant matrix (it is mostly matrix), so lack of matrix is incorrect." },
            { id: "c6", dok: 2, q: "Adipose tissue is classified as connective tissue. Why?", a: "Adipocytes are sparsely scattered in an extracellular matrix, which fits the connective tissue definition. Their function is energy storage and insulation.", options: ["Adipocytes are surrounded by epithelial cells in tightly packed sheets.", "Adipose tissue is a type of muscle because it can contract slightly when cold.", "Adipocytes are sparsely scattered in an extracellular matrix, fitting the connective tissue definition. Its function is energy storage and insulation.", "Adipose is classified as nervous tissue because it communicates with the hypothalamus."], correctIndex: 2, explanation: "Adipose tissue has cells (adipocytes) scattered in an extracellular matrix, which matches the connective tissue blueprint. Its functions include energy storage, insulation, and cushioning. Adipocytes are not arranged in epithelial sheets and have no basement membrane. They do not contract like muscle. Although adipose does signal the hypothalamus (via leptin), endocrine signaling does not reclassify it as nervous tissue." },
            { id: "c7", dok: 3, q: "A genetic defect in type I collagen synthesis causes osteogenesis imperfecta. Predict the multisystem effects.", a: "Type I collagen is in bone, tendons, ligaments, dermis, sclera, and dentin. Patients show fragile bones, blue sclera (thin sclera makes underlying choroid visible), loose joints, thin skin, and dental problems.", options: ["Only the long bones are affected, because type I collagen is specific to long-bone matrix.", "Patients show fragile bones, blue sclera (thin sclera lets the underlying choroid show through), loose joints, thin skin, and dental problems.", "Only the joints are affected, since cartilage is the main type I collagen tissue.", "Symptoms are limited to the skin and hair, because collagen is mainly cosmetic."], correctIndex: 1, explanation: "Type I collagen is widespread (bone, tendons, ligaments, dermis, sclera, dentin), so a defect produces multisystem effects: brittle bones, blue sclera, joint laxity, thin skin, and dental issues. It is not restricted to long bones, since type I collagen is in many tissues. Cartilage is mostly type II collagen, not type I. Collagen is structural, not cosmetic, and the disease is not limited to skin and hair." }
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
            { id: "c1", dok: 1, q: "Which muscle tissue is striated and voluntary?", a: "Skeletal muscle.", options: ["Smooth muscle.", "Skeletal muscle.", "Cardiac muscle.", "Visceral muscle."], correctIndex: 1, explanation: "Skeletal muscle is striated (organized sarcomeres produce visible banding) and voluntary (under conscious motor control). Smooth muscle is non-striated and involuntary, lining hollow organs. Cardiac muscle is striated but involuntary (autorhythmic). 'Visceral muscle' is another name for smooth muscle and shares its involuntary, non-striated traits." },
            { id: "c2", dok: 1, q: "Which muscle tissue has intercalated discs?", a: "Cardiac muscle.", options: ["Skeletal muscle.", "Smooth muscle.", "Cardiac muscle.", "Both skeletal and cardiac muscle."], correctIndex: 2, explanation: "Intercalated discs are unique to cardiac muscle. They contain gap junctions (for electrical coupling) and desmosomes (for mechanical strength) that link adjacent cardiomyocytes into a functional syncytium. Skeletal muscle has long multinucleated fibers but no intercalated discs. Smooth muscle has gap junctions in places but no discs. Only cardiac muscle has the discs." },
            { id: "c3", dok: 1, q: "Name two glial cell types in the CNS.", a: "Any two of: astrocytes, oligodendrocytes, microglia, ependymal cells.", options: ["Astrocytes and oligodendrocytes.", "Schwann cells and satellite cells.", "Neurons and axons.", "Erythrocytes and platelets."], correctIndex: 0, explanation: "Astrocytes (support, blood-brain barrier) and oligodendrocytes (CNS myelin) are two CNS glial cell types. Schwann cells and satellite cells are PNS glia, not CNS. Neurons and axons are the conducting cells and their processes, not glia. Erythrocytes and platelets are blood cells, not nervous tissue at all." },
            { id: "c4", dok: 1, q: "Which cell type forms myelin in the PNS?", a: "Schwann cell.", options: ["Oligodendrocyte.", "Schwann cell.", "Astrocyte.", "Microglial cell."], correctIndex: 1, explanation: "Schwann cells form myelin in the peripheral nervous system, wrapping a single axon segment per cell. Oligodendrocytes form myelin, but in the CNS, not the PNS. Astrocytes provide structural and metabolic support in the CNS without making myelin. Microglia are CNS immune cells, not myelin producers." },
            { id: "c5", dok: 2, q: "Why are intercalated discs essential for cardiac function?", a: "They contain gap junctions that let depolarization spread cell to cell, so cardiac muscle contracts as a coordinated unit (functional syncytium). Without them the heart could not pump.", options: ["They store calcium for muscle contraction.", "They contain gap junctions that let depolarization spread cell to cell, so cardiac muscle contracts as a coordinated unit (functional syncytium).", "They generate action potentials in place of the SA node.", "They prevent any electrical signal from traveling between cardiomyocytes, so each cell beats independently."], correctIndex: 1, explanation: "Intercalated discs include gap junctions that pass ions directly from cell to cell, so an electrical signal travels through the myocardium and triggers coordinated contraction (a functional syncytium). The discs do not store calcium, that is the sarcoplasmic reticulum's job. The SA node generates the pacemaker signal, and discs propagate it, not replace it. Discs spread the signal, they do not block it." },
            { id: "c6", dok: 3, q: "Multiple sclerosis destroys oligodendrocytes in the CNS. Predict the consequence for action potential conduction and explain why.", a: "Oligodendrocytes make CNS myelin. Without myelin, saltatory conduction fails and axons either conduct slowly (continuous conduction) or not at all. Symptoms reflect which tracts are demyelinated.", options: ["Saltatory conduction speeds up because demyelinated axons have less resistance.", "Action potentials stop generating, because oligodendrocytes are responsible for the depolarization itself.", "Oligodendrocytes make CNS myelin. Without myelin, saltatory conduction fails, so axons conduct slowly (continuous conduction) or not at all. Symptoms reflect which tracts are demyelinated.", "Only peripheral nerves are affected, because oligodendrocytes operate exclusively in the PNS."], correctIndex: 2, explanation: "Oligodendrocytes produce CNS myelin, and myelin is what enables saltatory conduction (signal jumping between nodes of Ranvier). When myelin is destroyed, conduction slows or fails, and symptoms map to the demyelinated tracts. Saltatory conduction requires myelin and slows, not speeds up, without it. Neurons generate action potentials, not oligodendrocytes. Oligodendrocytes work in the CNS, not the PNS (Schwann cells do PNS)." }
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
          lecturePageUrl: "skin-layers.html",
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
            { id: "c1", dok: 1, q: "List the layers of the epidermis from deep to superficial in thick skin.", a: "Stratum basale, spinosum, granulosum, lucidum, corneum.", options: ["Stratum corneum, lucidum, granulosum, spinosum, basale.", "Stratum basale, spinosum, granulosum, lucidum, corneum.", "Stratum spinosum, basale, granulosum, corneum, lucidum.", "Stratum granulosum, basale, lucidum, corneum, spinosum."], correctIndex: 1, explanation: "From deep to superficial in thick skin: basale, spinosum, granulosum, lucidum, corneum (mnemonic: 'Bears Smell Grandma's Lemon Cake'). The first option lists the layers in reverse (superficial to deep). The third and fourth options scramble the sequence. Lucidum is only present in thick skin, and corneum is always outermost." },
            { id: "c2", dok: 1, q: "Which cell makes melanin?", a: "The melanocyte (in the stratum basale).", options: ["The keratinocyte.", "The Langerhans cell.", "The Merkel cell.", "The melanocyte (in the stratum basale)."], correctIndex: 3, explanation: "Melanocytes, scattered along the stratum basale, synthesize melanin and transfer it to neighboring keratinocytes. Keratinocytes receive melanin but do not make it. Langerhans cells are antigen-presenting immune cells in the epidermis. Merkel cells are touch receptors associated with sensory nerve endings, not pigment producers." },
            { id: "c3", dok: 1, q: "Which dermal layer gives skin its tensile strength?", a: "The reticular layer.", options: ["The papillary layer.", "The reticular layer.", "The hypodermis.", "The stratum corneum."], correctIndex: 1, explanation: "The reticular layer is the deeper, thicker dermal layer packed with dense irregular connective tissue, giving skin its tensile strength and resistance to tearing in multiple directions. The papillary layer is the thinner, more superficial dermis with loose connective tissue and capillaries. The hypodermis (subcutaneous fat) is below the dermis and is not part of it. The stratum corneum is the outer epidermis, not dermis." },
            { id: "c4", dok: 1, q: "Is the epidermis vascular?", a: "No. It receives nutrients by diffusion from the dermal blood supply.", options: ["Yes, with extensive capillary networks throughout.", "Yes, but only the stratum corneum has blood supply.", "No. It receives nutrients by diffusion from the dermal blood supply.", "Yes, the epidermis has its own arteries supplying each layer."], correctIndex: 2, explanation: "The epidermis is avascular and gets oxygen and nutrients by diffusion from blood vessels in the underlying dermis. That is why deep epidermal layers (basale) are more metabolically active than superficial layers, where diffusion distance grows. The first, second, and fourth options are all wrong because no part of the epidermis contains blood vessels." },
            { id: "c5", dok: 2, q: "Explain why a deep dermal burn is more dangerous than a superficial epidermal burn.", a: "The dermis contains blood vessels, nerves, and the appendages from which new epidermis regrows. Lose the dermis and the body loses fluid, sensation, and the cells needed to heal back to normal skin.", options: ["Because dermal burns are less painful, patients delay treatment and infections worsen.", "The dermis contains blood vessels, nerves, and the appendages from which new epidermis regrows. Losing the dermis means fluid loss, sensation loss, and loss of cells needed to heal back to normal skin.", "Because the dermis is the only layer that produces melanin, and pigment loss is the main danger.", "Because dermal burns expose muscle and bone directly to the environment."], correctIndex: 1, explanation: "The dermis houses vessels, nerves, and the appendages (hair follicles, sweat glands) that regenerate new epidermis. Lose it, and the body loses fluid containment, sensation, and the cellular source of healthy regrowth. Dermal burns are often more painful initially because of intact nerves. Melanin is produced in the epidermis (by melanocytes in the basale), not the dermis. Dermal burns do not necessarily reach muscle or bone, that is full-thickness or deeper." },
            { id: "c6", dok: 3, q: "Vitamin D synthesis begins when UVB strikes 7-dehydrocholesterol in the skin. Predict why dark-skinned individuals at high latitudes are at higher risk of vitamin D deficiency.", a: "Melanin absorbs UVB before it can reach the precursor. Combined with low UVB at high latitudes, this reduces cutaneous vitamin D synthesis, raising deficiency risk.", options: ["Dark skin blocks vitamin D ingestion from food, regardless of sunlight exposure.", "Melanin absorbs UVB before it reaches 7-dehydrocholesterol. Combined with low UVB at high latitudes, this reduces cutaneous vitamin D synthesis and raises deficiency risk.", "Dark skin lacks 7-dehydrocholesterol entirely, so the precursor is not available.", "Vitamin D is destroyed faster in melanated skin once it has been synthesized."], correctIndex: 1, explanation: "Melanin acts as a UVB filter, so less UVB reaches the precursor (7-dehydrocholesterol) in pigmented skin. Combined with reduced UVB at high latitudes (sun angle, winter), the cutaneous synthesis pathway slows and deficiency risk rises. Melanin does not affect dietary vitamin D absorption. All skin types contain 7-dehydrocholesterol, the difference is UVB reaching it. The vitamin is not preferentially degraded in melanated skin, the bottleneck is at the synthesis step." }
          ]
        },

        {
          id: "t-skin-functions",
          title: "Skin Functions and Accessory Structures",
          summary: "Protection, thermoregulation, sensation, vitamin D; plus hair, glands, and nails.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/5-3-functions-of-the-integumentary-system",
          lecturePageUrl: "skin-functions.html",
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
            { id: "c1", dok: 1, q: "Name the sweat gland type responsible for thermoregulation.", a: "Eccrine.", options: ["Apocrine.", "Sebaceous.", "Eccrine.", "Ceruminous."], correctIndex: 2, explanation: "Eccrine sweat glands produce watery sweat distributed widely across the body and are the primary glands for thermoregulation through evaporative cooling. Apocrine glands open into hair follicles in the axilla and groin and produce a thicker secretion linked to body odor, not main thermoregulation. Sebaceous glands secrete oily sebum, not sweat. Ceruminous glands produce earwax in the external ear canal." },
            { id: "c2", dok: 1, q: "What does sebum do?", a: "Lubricates hair and skin, waterproofs, and inhibits microbial growth.", options: ["Detects pressure changes on the skin surface.", "Lubricates hair and skin, waterproofs, and inhibits microbial growth.", "Produces melanin and protects skin from UV damage.", "Cools the body through evaporation during exercise."], correctIndex: 1, explanation: "Sebum is the oily secretion of sebaceous glands. It lubricates hair shafts and skin, helps waterproof the surface, and contains antimicrobial components that inhibit bacterial and fungal growth. Pressure detection is a sensory job done by mechanoreceptors. Melanin is produced by melanocytes, not by sebaceous glands. Evaporative cooling comes from eccrine sweat, not from sebum." },
            { id: "c3", dok: 1, q: "Vitamin D synthesis requires what wavelength of light?", a: "Ultraviolet B (UVB).", options: ["Ultraviolet A (UVA).", "Visible blue light.", "Ultraviolet B (UVB).", "Infrared (IR)."], correctIndex: 2, explanation: "UVB photons convert 7-dehydrocholesterol in the epidermis into previtamin D3, the first step in cutaneous vitamin D synthesis. UVA penetrates more deeply but does not drive this conversion efficiently. Visible blue light is not the active wavelength. Infrared transfers heat but lacks the photon energy for the vitamin D photochemistry." },
            { id: "c4", dok: 1, q: "Where does new hair growth come from?", a: "The hair matrix at the base of the follicle.", options: ["The sebaceous gland associated with the follicle.", "The arrector pili muscle at the side of the follicle.", "The hair matrix at the base of the follicle.", "The free edge of the existing hair shaft."], correctIndex: 2, explanation: "New hair grows from the hair matrix at the base of the follicle, where actively dividing cells push older cells upward, keratinize, and form the shaft. Sebaceous glands secrete sebum into the follicle but do not generate new hair. Arrector pili muscles raise the hair (goosebumps) but do not produce it. The free edge of the existing shaft is dead keratin, not a site of growth." },
            { id: "c5", dok: 2, q: "Explain how cutaneous vasodilation helps cool the body.", a: "Dilation brings warm blood close to the skin surface. Heat dissipates to the cooler environment by radiation and conduction, lowering core temperature.", options: ["Vasodilation traps heat in the core, lowering peripheral temperature.", "Vasodilation brings warm blood close to the skin surface, where heat dissipates to the cooler environment by radiation and conduction, lowering core temperature.", "Vasodilation triggers shivering to convert kinetic energy into cooling.", "Vasodilation increases melanin production, blocking solar heat gain."], correctIndex: 1, explanation: "Dilation of cutaneous arterioles routes warm blood near the surface, where heat is lost by radiation, conduction, and convection (with sweat evaporation as a major adjunct), cooling the core. Vasodilation does not trap heat, vasoconstriction does. Shivering generates heat, not cooling. Vasodilation does not change melanin production." },
            { id: "c6", dok: 3, q: "A patient with extensive third-degree burns is at high risk of hypothermia and infection. Explain both, in terms of skin functions lost.", a: "Loss of barrier function: no insulation against heat loss and no defense against microbes entering deeper tissues. Loss of vascular control: cannot vasoconstrict to retain heat. Loss of fluid containment: evaporation of plasma-like fluid accelerates heat loss and dehydration.", options: ["Burns destroy bone marrow first, so anemia is the main risk; hypothermia and infection are secondary.", "Loss of the barrier means no insulation against heat loss and no defense against microbes; loss of vascular control means no vasoconstriction to retain heat; loss of fluid containment accelerates evaporative heat loss and dehydration.", "Hypothermia happens because burned skin transmits cold faster, and infection happens because antibodies leak out through the wound.", "The risk is mainly from immune overactivity attacking burned tissue, with hypothermia caused by fever exhaustion."], correctIndex: 1, explanation: "Third-degree burns destroy the skin barrier (insulation and microbial defense), the cutaneous vasculature (cannot vasoconstrict to retain heat), and the fluid envelope (rapid evaporative loss of plasma-like fluid). Result: hypothermia from heat and fluid loss, infection from microbial entry. Burns do not destroy bone marrow first. Burned skin does not actively transmit cold, the issue is loss of insulation and fluid; antibody leakage is a minor factor versus barrier loss. Immune overactivity and fever exhaustion are not the primary mechanism." }
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
            { id: "c1", dok: 1, q: "Which bone cell builds new bone matrix?", a: "Osteoblast.", options: ["Osteoclast", "Osteoblast", "Osteocyte", "Chondroblast"], correctIndex: 1, explanation: "Osteoblasts secrete osteoid (new bone matrix) and initiate mineralization. Osteoclasts resorb bone rather than build it. Osteocytes are mature, embedded cells that maintain matrix but do not actively build new matrix. Chondroblasts build cartilage, not bone." },
            { id: "c2", dok: 1, q: "Which bone cell resorbs bone?", a: "Osteoclast.", options: ["Osteocyte", "Osteoblast", "Osteoclast", "Chondrocyte"], correctIndex: 2, explanation: "Osteoclasts are large multinucleated cells that secrete acid and enzymes to dissolve bone matrix. Osteocytes maintain existing matrix but do not resorb it. Osteoblasts build new matrix. Chondrocytes are cartilage cells, not bone cells." },
            { id: "c3", dok: 1, q: "What is an osteon?", a: "The structural unit of compact bone: concentric lamellae of matrix around a central (Haversian) canal containing vessels and nerves.", options: ["A trabecula of spongy bone made of irregular plates of matrix", "A canal that connects osteocytes to one another through the matrix", "The structural unit of compact bone with concentric lamellae around a central canal", "The cartilage model that precedes endochondral bone formation"], correctIndex: 2, explanation: "An osteon (Haversian system) is the cylindrical structural unit of compact bone, with concentric lamellae surrounding a central canal that carries vessels and nerves. Trabeculae are the irregular plates of spongy bone, not osteons. Canaliculi connect osteocytes but are not the unit itself. The cartilage model is a developmental stage, not a tissue unit." },
            { id: "c4", dok: 1, q: "Which ossification type produces most long bones?", a: "Endochondral ossification (cartilage model).", options: ["Intramembranous ossification", "Appositional growth", "Endochondral ossification", "Interstitial growth"], correctIndex: 2, explanation: "Endochondral ossification uses a hyaline cartilage model that is gradually replaced by bone, and it forms most long bones. Intramembranous ossification builds flat bones of the skull directly from mesenchyme. Appositional growth widens bones after they form. Interstitial growth happens in cartilage, not bone formation pathways." },
            { id: "c5", dok: 2, q: "Why is mature bone metabolically active even when growth has stopped?", a: "Bone is continuously remodeled. Osteoblasts and osteoclasts replace old matrix, repair microdamage, adjust shape to load, and provide a reservoir of calcium and phosphate the body draws on.", options: ["Bone is continuously remodeled to repair microdamage and serve as a calcium reservoir", "Bone matrix continuously breaks down faster than it is built once adult height is reached", "Bone marrow is the only active part of bone after growth stops", "Bone cells stop dividing but continue to deposit calcium passively"], correctIndex: 0, explanation: "Osteoblasts and osteoclasts continuously remodel bone to repair microdamage, adapt to load, and balance blood calcium. Resorption normally matches formation in healthy adults, not exceeds it. Marrow is active but is not the only metabolically active part. Bone deposition is enzyme-driven, not passive." },
            { id: "c6", dok: 2, q: "Explain how parathyroid hormone (PTH) raises blood calcium.", a: "PTH activates osteoclasts (indirectly, via osteoblast signaling), which resorb bone and release calcium and phosphate into the blood. PTH also increases renal calcium reabsorption and activation of vitamin D, raising gut absorption.", options: ["PTH activates osteoblasts to deposit calcium phosphate into the blood", "PTH activates osteoclasts to resorb bone, releasing calcium into the blood", "PTH directly pulls calcium from dietary sources in the gut wall", "PTH causes the kidney to excrete more calcium into the urine"], correctIndex: 1, explanation: "PTH stimulates osteoclast activity (indirectly through osteoblast signaling), which resorbs bone matrix and releases calcium into the blood. It also boosts renal calcium reabsorption and vitamin D activation. Osteoblasts build bone and store calcium, the opposite effect. PTH does not act directly on the gut; it works through vitamin D. PTH conserves urinary calcium, it does not waste it." },
            { id: "c7", dok: 3, q: "A postmenopausal woman has accelerated bone loss. Tie this to the underlying cellular biology.", a: "Estrogen normally restrains osteoclast activity. After menopause, estrogen falls, osteoclast activity rises relative to osteoblast activity, and net bone resorption exceeds formation. Bone density falls over years, predisposing to osteoporotic fracture.", options: ["Estrogen loss removes restraint on osteoclasts, so resorption outpaces formation", "Estrogen loss kills osteoblasts directly, halting all new bone formation", "Estrogen loss causes calcium to be excreted faster than it can be absorbed", "Estrogen loss prevents vitamin D activation in the kidneys"], correctIndex: 0, explanation: "Estrogen normally restrains osteoclast activity. After menopause, falling estrogen allows osteoclast activity to outpace osteoblast activity, producing net bone loss. Osteoblasts continue functioning; the issue is imbalance. Calcium absorption and vitamin D activation are not the primary lesion in postmenopausal osteoporosis." }
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
            { id: "c1", dok: 1, q: "How many cervical vertebrae are there?", a: "Seven.", options: ["Five", "Seven", "Twelve", "Thirty-three"], correctIndex: 1, explanation: "All mammals, including humans, have seven cervical vertebrae (C1 to C7). Five is the lumbar count. Twelve is the thoracic count. Thirty-three is the total approximate vertebral count including fused sacral and coccygeal segments." },
            { id: "c2", dok: 1, q: "Name the first two cervical vertebrae and their distinguishing feature.", a: "C1 (atlas), no body, supports the skull. C2 (axis), has the dens that allows head rotation.", options: ["C1 axis with the dens; C2 atlas supporting the skull", "C1 atlas, no body, supports the skull; C2 axis, has the dens for rotation", "C1 atlas with the dens; C2 axis supports the skull", "C1 and C2 are both called the atlas and share the dens"], correctIndex: 1, explanation: "C1 is the atlas; it lacks a body and cradles the skull (yes/no nod). C2 is the axis; its dens projects upward and allows the atlas (and head) to rotate (no/no shake). The other options swap the names, misplace the dens, or invent a shared label that does not exist." },
            { id: "c3", dok: 1, q: "Which ribs are 'floating'?", a: "Ribs 11 and 12 (no anterior attachment to sternum or costal cartilage of another rib).", options: ["Ribs 8 to 10 (attach via shared costal cartilage)", "Ribs 1 to 7 (true ribs attaching directly to the sternum)", "Ribs 11 and 12 (no anterior attachment)", "Ribs 1 and 2 (attach near the clavicle)"], correctIndex: 2, explanation: "Floating ribs (11 and 12) have no anterior attachment to the sternum or to another rib's cartilage. Ribs 8 to 10 are false ribs that share costal cartilage. Ribs 1 to 7 are true ribs with direct sternal attachment. Ribs 1 and 2 are true ribs, not floating." },
            { id: "c4", dok: 1, q: "How many cranial bones are there?", a: "Eight.", options: ["Six", "Eight", "Fourteen", "Twenty-two"], correctIndex: 1, explanation: "There are eight cranial bones: frontal, two parietal, two temporal, occipital, sphenoid, ethmoid. Fourteen is the number of facial bones. Twenty-two is the total skull bone count (cranial plus facial). Six is too few." },
            { id: "c5", dok: 2, q: "Why are lumbar vertebrae larger than cervical vertebrae?", a: "They bear more body weight. Larger vertebral bodies distribute compressive load over a greater area, reducing stress.", options: ["They bear more body weight; larger bodies spread compressive load", "They protect the spinal cord, which is widest in the lumbar region", "They allow more rotation than cervical vertebrae do", "They have larger bodies because they contain more red marrow"], correctIndex: 0, explanation: "Lumbar vertebrae support more body weight than cervical vertebrae, and larger bodies distribute compressive load over a greater surface area. The spinal cord actually narrows in the lumbar region (ends around L1 to L2). Lumbar vertebrae permit less rotation than cervical ones. Marrow content does not drive vertebral body size." },
            { id: "c6", dok: 3, q: "A patient with osteoporosis sustains a compression fracture of a thoracic vertebra. Predict the postural consequence and explain why.", a: "Anterior vertebral body collapses while the posterior remains taller, producing a wedge shape. Cumulative wedge fractures across the thoracic spine produce kyphosis ('dowager's hump'). The biomechanical change can also reduce thoracic volume, impacting breathing.", options: ["The disc bulges and causes lordosis (sway-back)", "The anterior body collapses into a wedge, producing kyphosis", "The posterior arch collapses, producing scoliosis", "The vertebra rotates, producing torticollis"], correctIndex: 1, explanation: "In osteoporotic compression fractures, the anterior vertebral body collapses while the posterior remains taller, producing a wedge. Stacked wedge fractures across the thoracic spine create kyphosis (dowager's hump). Lordosis is increased lumbar curve, not from thoracic compression. Scoliosis is lateral curvature from different causes. Torticollis is a neck-muscle issue." }
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
            { id: "c1", dok: 1, q: "Which bone is the largest in the body?", a: "Femur.", options: ["Tibia", "Humerus", "Femur", "Sternum"], correctIndex: 2, explanation: "The femur (thigh bone) is the longest, heaviest, and strongest bone in the body. The tibia is the second longest but shorter than the femur. The humerus is the longest upper-limb bone but shorter than the femur. The sternum is flat and not among the long bones." },
            { id: "c2", dok: 1, q: "Which bone of the forearm is on the thumb side?", a: "Radius.", options: ["Ulna", "Humerus", "Radius", "Carpal"], correctIndex: 2, explanation: "In anatomical position (palms forward), the radius sits on the lateral (thumb) side of the forearm. The ulna is on the medial (pinky) side. The humerus is the upper arm bone, not in the forearm. Carpals are wrist bones, not forearm bones." },
            { id: "c3", dok: 1, q: "How many carpal bones are in the wrist?", a: "Eight.", options: ["Five", "Seven", "Eight", "Fourteen"], correctIndex: 2, explanation: "There are eight carpal bones arranged in two rows of four. Five is the number of metacarpals (palm bones). Seven is the number of tarsals in the ankle. Fourteen is the number of phalanges in the hand." },
            { id: "c4", dok: 1, q: "Which three bones fuse to form the coxal (hip) bone?", a: "Ilium, ischium, pubis.", options: ["Ilium, ischium, pubis", "Ilium, sacrum, coccyx", "Femur, ischium, pubis", "Ilium, pubis, sacrum"], correctIndex: 0, explanation: "Three bones fuse at the acetabulum to form each coxal bone: ilium (superior), ischium (posteroinferior), pubis (anteroinferior). The sacrum and coccyx are part of the axial skeleton. The femur is a leg bone that articulates with the coxal bone but is not part of it." },
            { id: "c5", dok: 2, q: "Why does the pectoral girdle allow more arm mobility than the pelvic girdle allows leg mobility?", a: "The pectoral girdle attaches to the axial skeleton only at the sternoclavicular joint, with the scapula gliding freely on the thorax. The pelvic girdle is fused to the sacrum and locked into a weight-bearing ring, sacrificing mobility for stability.", options: ["The pectoral girdle is fused to the axial skeleton; the pelvic girdle is not", "The pectoral girdle attaches only at the sternoclavicular joint; the pelvic girdle is fused to the sacrum", "The pectoral girdle has deeper sockets than the pelvic girdle", "The pectoral girdle has more bones than the pelvic girdle"], correctIndex: 1, explanation: "The pectoral girdle attaches to the axial skeleton only at the sternoclavicular joint, leaving the scapula free to glide. The pelvic girdle is locked to the sacrum, trading mobility for weight-bearing stability. The pectoral girdle is not fused; that is the pelvic girdle. The shoulder socket (glenoid) is actually shallower than the acetabulum. Bone count does not explain mobility." },
            { id: "c6", dok: 3, q: "A patient fractures the clavicle. Predict the change in shoulder position and why.", a: "Loss of the clavicle removes the strut that holds the scapula laterally. The shoulder drops downward and medially, pulled by gravity and the weight of the arm.", options: ["The shoulder drops down and medially because the scapular strut is lost", "The shoulder lifts up and laterally because the muscles pull harder", "The arm rotates internally because the humerus loses its anchor", "The scapula fuses to the rib cage to compensate"], correctIndex: 0, explanation: "The clavicle is the strut that holds the scapula laterally and away from the trunk. Without it, gravity and the weight of the arm pull the shoulder downward and medially. The muscles cannot lift the shoulder higher without the bony strut. Humeral rotation is not the primary change. Scapular fusion does not occur." }
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
            { id: "c1", dok: 1, q: "Which joint type allows the most movement?", a: "Synovial.", options: ["Fibrous", "Cartilaginous", "Synovial", "Sutural"], correctIndex: 2, explanation: "Synovial joints have a fluid-filled cavity and articular cartilage that permit a wide range of motion. Fibrous joints (such as sutures of the skull) are largely immobile. Cartilaginous joints allow only slight movement. Sutural joints are a type of fibrous joint, so they are nearly immobile." },
            { id: "c2", dok: 1, q: "Name two examples of hinge joints.", a: "Elbow, knee, interphalangeal joints.", options: ["Shoulder, hip", "Wrist, ankle", "Elbow, knee", "Atlas-axis, radioulnar"], correctIndex: 2, explanation: "Hinge joints (elbow, knee, interphalangeal joints) allow motion in one plane (flexion and extension). Shoulder and hip are ball-and-socket. Wrist and ankle are condyloid or include multiple joint types. Atlas-axis and radioulnar are pivot joints." },
            { id: "c3", dok: 1, q: "What movement decreases the angle of a joint?", a: "Flexion.", options: ["Extension", "Flexion", "Abduction", "Rotation"], correctIndex: 1, explanation: "Flexion decreases the angle between two bones at a joint (bending the elbow). Extension increases the angle (straightening). Abduction moves a limb away from midline in the frontal plane. Rotation turns a bone around its long axis." },
            { id: "c4", dok: 1, q: "What kind of joint is the shoulder?", a: "Ball-and-socket.", options: ["Hinge", "Pivot", "Saddle", "Ball-and-socket"], correctIndex: 3, explanation: "The shoulder (glenohumeral) is a ball-and-socket joint, allowing motion in all three planes plus rotation. Hinge joints permit motion in only one plane. Pivot joints allow rotation only. Saddle joints (like the thumb carpometacarpal) allow two planes but not full rotation." },
            { id: "c5", dok: 2, q: "Why is the shoulder more dislocation-prone than the hip even though both are ball-and-socket joints?", a: "The shoulder has a shallow glenoid fossa and relies on rotator cuff muscles for stability, trading bony containment for mobility. The hip has a deep acetabulum and strong ligaments, providing far more bony and ligamentous stability.", options: ["The shoulder has a deeper socket than the hip but weaker muscles", "The shoulder has a shallow glenoid and relies on rotator cuff muscles; the hip has a deep acetabulum and strong ligaments", "The shoulder has more bones in the joint, increasing dislocation risk", "The shoulder lacks synovial fluid, which the hip has"], correctIndex: 1, explanation: "The shoulder trades stability for mobility: its shallow glenoid fossa offers little bony containment, and stability depends on the rotator cuff. The hip has a deep acetabulum and strong ligaments, giving far more bony and ligamentous stability. The shoulder socket is shallower (not deeper) than the hip. Joint bone count does not drive dislocation. Both joints have synovial fluid." },
            { id: "c6", dok: 3, q: "A patient has rheumatoid arthritis affecting the synovial membrane. Predict the cascade of joint damage and explain why each step happens.", a: "Inflamed synovium thickens and forms a pannus that erodes articular cartilage. Cartilage loss exposes underlying bone, which then erodes. Joint capsule swells and contracts irregularly, producing joint deformity. Over time, fibrosis or bony ankylosis can fuse the joint.", options: ["Inflamed synovium forms a pannus that erodes cartilage, then bone, then deforms or fuses the joint", "Synovial fluid thickens and crystallizes inside the joint, scratching cartilage", "Articular cartilage spontaneously hardens into bone, locking the joint", "Bone spurs form first, then the synovium swells in response"], correctIndex: 0, explanation: "In rheumatoid arthritis, the inflamed synovium thickens into a pannus that erodes cartilage. Cartilage loss exposes bone, which then erodes, and the capsule scars into deformity or bony fusion. Synovial fluid does not crystallize in RA (that resembles gout). Cartilage does not spontaneously ossify. Bone spurs are more characteristic of osteoarthritis, and they follow rather than precede the synovial inflammation in RA." }
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
          lecturePageUrl: "skeletal-muscle-microanatomy.html",
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
            { id: "c1", dok: 1, q: "What is the contractile unit of skeletal muscle?", a: "The sarcomere.", options: ["The myofibril", "The muscle fiber", "The sarcomere", "The fascicle"], correctIndex: 2, explanation: "The sarcomere is the smallest contractile unit, defined by the region between two Z discs. A myofibril is a chain of sarcomeres. A muscle fiber (cell) contains many myofibrils. A fascicle is a bundle of fibers, a higher-level structure." },
            { id: "c2", dok: 1, q: "What protein makes up the thick filament?", a: "Myosin.", options: ["Actin", "Tropomyosin", "Myosin", "Troponin"], correctIndex: 2, explanation: "Myosin makes up the thick filament; its heads form cross-bridges with actin. Actin is the thin filament. Tropomyosin and troponin are regulatory proteins on the thin filament, not the thick filament itself." },
            { id: "c3", dok: 1, q: "Where is Ca²⁺ stored in a muscle fiber?", a: "In the sarcoplasmic reticulum.", options: ["In the mitochondria", "In the T-tubules", "In the sarcoplasmic reticulum", "In the sarcolemma"], correctIndex: 2, explanation: "The sarcoplasmic reticulum is the muscle cell's specialized smooth ER that stores Ca2+ and releases it when triggered. Mitochondria do not serve as a Ca2+ release store for contraction. T-tubules carry the AP inward but do not store Ca2+. The sarcolemma is the surface membrane, not a storage site." },
            { id: "c4", dok: 1, q: "What do T-tubules do?", a: "Carry the action potential from the surface sarcolemma deep into the muscle fiber so that all sarcomeres are activated simultaneously.", options: ["Store calcium for release into the sarcomere", "Carry the action potential deep into the fiber so all sarcomeres activate together", "Connect adjacent muscle fibers electrically", "Anchor thin filaments to the Z disc"], correctIndex: 1, explanation: "T-tubules are inward extensions of the sarcolemma that carry the AP deep into the fiber, ensuring that all sarcomeres receive the signal simultaneously. Ca2+ storage is the job of the SR. Skeletal muscle fibers are not electrically coupled to each other (that's cardiac). The Z disc anchors thin filaments, not the T-tubule." },
            { id: "c5", dok: 2, q: "Explain why the A band shortens little during contraction but the I band shortens dramatically.", a: "The A band is the length of the thick filament, which does not change. The I band is the region where only thin filaments exist; as thin filaments slide inward, the I band shrinks.", options: ["The A band is the thick-filament length and does not change; the I band has only thin filaments and shortens as they slide in", "The A band is only thin filaments and shortens; the I band stays fixed", "Both bands shorten equally because the whole sarcomere shrinks", "The A band stretches while the I band shortens"], correctIndex: 0, explanation: "The A band equals the length of the thick filament, which itself does not shorten. The I band is the region of thin filaments only; as thin filaments slide inward over the thick filaments, the I band shrinks. The A band is the thick-filament region, not the thin-filament region. Bands do not shorten equally, and the A band does not stretch." },
            { id: "c6", dok: 3, q: "A toxin disrupts the triads. Predict the effect on contraction.", a: "Action potentials still propagate along the sarcolemma and T-tubules, but Ca²⁺ release from the SR is uncoupled from the T-tubule signal. Without intracellular Ca²⁺, troponin does not move tropomyosin, cross-bridges cannot form, and contraction fails.", options: ["Action potentials cannot reach the surface membrane, so contraction never starts", "Ca2+ release from the SR is uncoupled from the T-tubule signal, so cross-bridges cannot form", "Myosin heads bind actin but cannot detach", "ATP cannot reach the cross-bridges, so they freeze"], correctIndex: 1, explanation: "Triads connect T-tubules to SR terminal cisternae so that the AP triggers Ca2+ release. Disrupt them and APs still propagate, but Ca2+ release is uncoupled, troponin cannot move tropomyosin, and cross-bridges cannot form. The surface AP itself is unaffected. The myosin-detachment problem describes rigor. ATP supply is not the triad's role." }
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
            { id: "c1", dok: 1, q: "What ion is the direct trigger for cross-bridge formation?", a: "Calcium (Ca²⁺).", options: ["Sodium (Na+)", "Potassium (K+)", "Calcium (Ca2+)", "Chloride (Cl-)"], correctIndex: 2, explanation: "Ca2+ binds troponin, which moves tropomyosin off the myosin-binding sites on actin and allows cross-bridge formation. Na+ depolarizes the sarcolemma but does not directly trigger cross-bridges. K+ repolarizes the membrane. Cl- is not the trigger ion for contraction." },
            { id: "c2", dok: 1, q: "What protein does Ca²⁺ bind to inside the sarcomere?", a: "Troponin.", options: ["Actin", "Tropomyosin", "Troponin", "Myosin"], correctIndex: 2, explanation: "Troponin is the Ca2+-binding regulatory protein on the thin filament; binding causes a conformational change that shifts tropomyosin. Actin is the binding partner for myosin, not the Ca2+ receptor. Tropomyosin moves in response to troponin but does not itself bind Ca2+. Myosin is on the thick filament and binds ATP and actin." },
            { id: "c3", dok: 1, q: "What happens to tropomyosin when troponin binds calcium?", a: "Tropomyosin shifts and uncovers the myosin-binding sites on actin.", options: ["It binds Ca2+ directly and contracts the sarcomere", "It shifts to uncover the myosin-binding sites on actin", "It releases ATP for the power stroke", "It dissolves to expose the thin filament"], correctIndex: 1, explanation: "When troponin binds Ca2+, tropomyosin shifts position on the actin filament and uncovers the myosin-binding sites. Tropomyosin does not bind Ca2+ directly (troponin does). It does not release ATP; myosin hydrolyzes ATP. Tropomyosin does not dissolve; it moves." },
            { id: "c4", dok: 1, q: "When in the cross-bridge cycle is ATP hydrolyzed?", a: "During the cocking step, before the power stroke.", options: ["At detachment, after the power stroke", "During the power stroke itself", "During the cocking step, before the power stroke", "When Ca2+ binds troponin"], correctIndex: 2, explanation: "ATP is hydrolyzed during the cocking step: myosin binds ATP, splits it to ADP and Pi, and uses the energy to re-cock the head into the high-energy position. ATP itself binds at detachment but is not hydrolyzed then. Hydrolysis precedes the power stroke. Ca2+ binding to troponin does not hydrolyze ATP." },
            { id: "c5", dok: 1, q: "When in the cycle is ATP required for detachment?", a: "A fresh ATP must bind myosin to release it from actin after the power stroke.", options: ["A fresh ATP must bind myosin to release it from actin", "ADP must bind myosin to release it from actin", "Ca2+ binding to myosin causes detachment", "Phosphate binding causes detachment"], correctIndex: 0, explanation: "After the power stroke, myosin is tightly bound to actin. A new ATP molecule must bind to the myosin head to break this bond and release it. ADP rebinding does not detach myosin. Ca2+ does not bind myosin directly in skeletal muscle. Phosphate release happens earlier in the cycle and does not cause detachment." },
            { id: "c6", dok: 2, q: "Explain rigor mortis using the cross-bridge cycle.", a: "After death, ATP production stops. Without ATP, myosin cannot detach from actin. Cross-bridges remain locked, and muscles become rigid.", options: ["Ca2+ pumps stop working, so cross-bridges keep cycling", "ATP production stops, so myosin cannot detach from actin and cross-bridges lock", "Tropomyosin permanently covers the binding sites", "The sarcolemma depolarizes endlessly"], correctIndex: 1, explanation: "After death, ATP production halts. Without ATP, myosin cannot detach from actin, so cross-bridges stay locked and muscles stiffen. SR pumps also fail, but the rigidity is from locked cross-bridges, not from continued cycling. Tropomyosin is actually off the binding sites (Ca2+ leaks out and binds troponin). The sarcolemma is not endlessly depolarizing." },
            { id: "c7", dok: 2, q: "Predict what happens to muscle force if intracellular Ca²⁺ rises but ATP runs out.", a: "Cross-bridges can form (Ca²⁺ exposes actin sites) but cannot cycle (no ATP for cocking or detachment). The muscle locks into a contracted state and force production stops.", options: ["The muscle relaxes because there is no ATP for the power stroke", "The muscle locks in a contracted state because cross-bridges cannot detach", "The muscle vibrates between contraction and relaxation", "Ca2+ is pumped back into the SR and contraction stops"], correctIndex: 1, explanation: "Ca2+ exposes the binding sites so cross-bridges can form, but cycling requires ATP for cocking and detachment. With Ca2+ present and ATP absent, cross-bridges lock, just as in rigor. Relaxation requires both Ca2+ removal and ATP. Vibration does not occur. SR pumps need ATP, so Ca2+ is not removed." },
            { id: "c8", dok: 2, q: "Why does curare cause muscle paralysis?", a: "Curare blocks nicotinic ACh receptors at the neuromuscular junction. The sarcolemma cannot depolarize, T-tubules do not trigger SR Ca²⁺ release, and contraction cannot start.", options: ["It destroys ACh in the synaptic cleft before it can act", "It blocks Na+ channels on the sarcolemma directly", "It blocks nicotinic ACh receptors so the sarcolemma cannot depolarize", "It binds tropomyosin and prevents binding-site exposure"], correctIndex: 2, explanation: "Curare is a competitive antagonist at nicotinic ACh receptors at the neuromuscular junction. The sarcolemma cannot depolarize, the T-tubule signal does not reach the SR, and contraction never starts. ACh is not destroyed (that's acetylcholinesterase). Curare does not block Na+ channels directly. It does not act on tropomyosin." },
            { id: "c9", dok: 3, q: "A patient is poisoned with sarin (an acetylcholinesterase inhibitor). Predict the effect at the neuromuscular junction across time.", a: "ACh is not broken down. It accumulates and continuously activates the sarcolemma. Initial response: prolonged contraction and fasciculations. Later: receptors desensitize, depolarization block sets in, and the muscle becomes paralyzed (including respiratory muscles).", options: ["ACh builds up; first prolonged contraction, then desensitization and flaccid paralysis", "ACh is destroyed faster, causing immediate flaccid paralysis", "Ca2+ floods the SR, causing rigor-like contracture only", "Sodium channels close permanently, blocking the AP"], correctIndex: 0, explanation: "Sarin inhibits acetylcholinesterase, so ACh accumulates in the synaptic cleft. Initially the muscle contracts and fasciculates from continuous stimulation. Over time, receptors desensitize, depolarization block develops, and paralysis (including respiratory) results. ACh is not destroyed faster; it is destroyed slower. SR Ca2+ flooding is the malignant hyperthermia mechanism. Sarin does not directly close Na+ channels." },
            { id: "c10", dok: 3, q: "Malignant hyperthermia is caused by a mutation that makes the SR Ca²⁺ release channel hyperactive in response to certain anesthetics. Predict the patient's presentation and explain why.", a: "Unregulated Ca²⁺ release continuously activates cross-bridges. The muscle contracts continuously, generating heat (temperature climbs rapidly) and consuming ATP. ATP depletion leads to muscle damage (rhabdomyolysis), acidosis, hyperkalemia, and, if untreated, death.", options: ["Unregulated Ca2+ release causes continuous contraction, heat, and ATP depletion", "Ca2+ release is blocked, so the muscle goes flaccid and cools rapidly", "ACh release is blocked, producing paralysis without heat", "Na+ channels open continuously, producing sustained depolarization but no contraction"], correctIndex: 0, explanation: "The mutated SR channel releases Ca2+ uncontrollably when triggered by certain anesthetics. Cross-bridges cycle continuously, heat builds (temperature rises rapidly), ATP runs out, muscle damage and acidosis follow, and death can result if untreated. Reduced Ca2+ release would produce weakness, not hyperthermia. ACh block and pure Na+ effects do not match the clinical picture." }
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
            { id: "c1", dok: 1, q: "Define a motor unit.", a: "One motor neuron and all the muscle fibers it innervates.", options: ["One motor neuron and all the muscle fibers it innervates", "One muscle fiber and all the motor neurons that contact it", "A bundle of muscle fibers wrapped in connective tissue", "A motor neuron and the sensory neuron paired with it"], correctIndex: 0, explanation: "A motor unit is one motor neuron plus every muscle fiber that neuron innervates. The fibers act together when the neuron fires. A fiber is contacted by only one motor neuron in adults, not many. A fiber bundle is a fascicle, not a motor unit. A reflex arc pairs sensory and motor neurons, but that is a different concept." },
            { id: "c2", dok: 1, q: "Which fiber type is most fatigue-resistant?", a: "Type I (slow oxidative).", options: ["Type IIx (fast glycolytic)", "Type IIa (fast oxidative)", "Type I (slow oxidative)", "All types fatigue equally"], correctIndex: 2, explanation: "Type I fibers rely on oxidative metabolism with abundant mitochondria and high capillary density, so they fatigue slowly. Type IIx fibers fatigue fastest because they rely on anaerobic glycolysis. Type IIa fibers are intermediate. Fiber types differ substantially in fatigue resistance, so they do not fatigue equally." },
            { id: "c3", dok: 1, q: "What is tetanus in the muscle physiology sense?", a: "A smooth, sustained contraction produced when stimulation frequency is too high for the muscle to relax between twitches.", options: ["A single maximal twitch in response to one stimulus", "A smooth, sustained contraction from high-frequency stimulation", "A jerky alternation between contraction and relaxation", "The complete inability of muscle to contract due to disease"], correctIndex: 1, explanation: "In muscle physiology, tetanus is the smooth, sustained contraction produced when stimuli arrive faster than the muscle can fully relax between twitches. A single twitch is not tetanus. Jerky alternation describes incomplete summation. Inability to contract describes paralysis. (The disease 'tetanus' is named for the spasms it produces, but the physiology term means high-frequency summation.)" },
            { id: "c4", dok: 1, q: "Which is recruited first, small or large motor units?", a: "Small (size principle).", options: ["Large", "Small", "Random order", "Largest first, then smallest"], correctIndex: 1, explanation: "The size principle says small motor units (small motor neurons innervating few fibers) are recruited first because they have lower activation thresholds. Larger units join as more force is needed. Recruitment is not random; it follows size. Largest first would defeat the purpose of fine force grading at low effort." },
            { id: "c5", dok: 2, q: "Why are eye muscles innervated by very small motor units?", a: "Eye movements require fine, precise control. Small motor units (a few fibers each) let the nervous system grade force in small increments for smooth tracking.", options: ["Eye muscles need lots of force, so small units provide rapid summation", "Eye movements need fine precision, and small units allow small force increments", "Small units protect eye muscles from fatigue", "Small units allow eye muscles to contract more slowly"], correctIndex: 1, explanation: "Eye movement requires extremely precise control. Small motor units (a few fibers each) let the nervous system grade force in tiny steps for smooth tracking. Eye muscles do not require high force. Small units are not primarily about fatigue protection in this case. Eye muscles are actually very fast, not slow." },
            { id: "c6", dok: 3, q: "A sprinter trains for explosive power; a marathoner trains for endurance. Predict the dominant muscle fiber adaptations in each.", a: "Sprinter: hypertrophy of Type IIx (fast glycolytic) fibers and improved anaerobic capacity. Marathoner: shift toward more Type I (slow oxidative) characteristics, increased mitochondria and capillary density, enhanced fatigue resistance.", options: ["Sprinter: more Type I; marathoner: more Type IIx", "Sprinter: hypertrophy of Type IIx; marathoner: shift toward Type I characteristics with more mitochondria", "Both shift toward Type IIa fibers exclusively", "Neither changes; fiber type is fixed at birth"], correctIndex: 1, explanation: "Sprinters develop and hypertrophy fast glycolytic (Type IIx) fibers and anaerobic capacity. Endurance training shifts fiber characteristics toward Type I (slow oxidative), with more mitochondria and capillaries and better fatigue resistance. The first option swaps the two. Fiber type is somewhat plastic, so it is not fixed at birth and does not collapse to only Type IIa." }
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
            { id: "c1", dok: 1, q: "What is the typical resting membrane potential of a neuron?", a: "About −70 mV (inside negative).", options: ["About 0 mV", "About +30 mV", "About -55 mV", "About -70 mV"], correctIndex: 3, explanation: "A typical neuron rests near -70 mV (inside negative relative to outside). 0 mV would mean no charge separation, which is not resting. +30 mV is near the peak of the action potential. -55 mV is the typical threshold, not the resting potential." },
            { id: "c2", dok: 1, q: "Which ions does the Na⁺/K⁺ ATPase pump and in what direction?", a: "Three Na⁺ out, two K⁺ in, per ATP.", options: ["Two Na+ out, three K+ in, per ATP", "Three Na+ in, two K+ out, per ATP", "Three Na+ out, two K+ in, per ATP", "One Na+ out, one K+ in, per ATP"], correctIndex: 2, explanation: "The Na+/K+ ATPase exports three Na+ and imports two K+ for each ATP. The other options reverse the stoichiometry, reverse the direction, or invent a 1:1 ratio that does not exist." },
            { id: "c3", dok: 1, q: "Which part of the neuron conducts the action potential away from the cell body?", a: "The axon.", options: ["Dendrite", "Axon", "Soma (cell body)", "Synaptic cleft"], correctIndex: 1, explanation: "The axon conducts the action potential away from the cell body toward the axon terminals. Dendrites receive input and conduct toward the cell body. The soma integrates input but does not conduct the AP. The synaptic cleft is the gap between neurons, not part of a single neuron." },
            { id: "c4", dok: 1, q: "Which CNS glial cell makes myelin?", a: "Oligodendrocyte.", options: ["Schwann cell", "Astrocyte", "Microglia", "Oligodendrocyte"], correctIndex: 3, explanation: "Oligodendrocytes myelinate CNS axons (one cell can wrap multiple axons). Schwann cells make myelin in the PNS, not the CNS. Astrocytes support neurons and form the blood-brain barrier but do not myelinate. Microglia are the immune cells of the CNS." },
            { id: "c5", dok: 2, q: "Why is the resting potential negative rather than zero?", a: "K⁺ leak channels let K⁺ flow out down its gradient, leaving anions behind. The Na⁺/K⁺ pump also exports more positive charge than it imports. Together this builds a negative interior.", options: ["Na+ leak channels let Na+ in, making the inside positive", "K+ leak channels let K+ out, leaving anions behind, and the pump exports net positive charge", "The membrane is impermeable to all ions at rest", "Cl- pumps actively load the cell with negative charge"], correctIndex: 1, explanation: "At rest, the membrane is much more permeable to K+ than to Na+. K+ leaks out down its gradient, leaving behind intracellular anions (proteins, phosphates). The Na+/K+ pump also exports more positive charge than it imports, adding a small electrogenic contribution. Na+ leak is small. The membrane is not impermeable. Cl- is not actively pumped in to set RMP." },
            { id: "c6", dok: 3, q: "Ouabain blocks the Na⁺/K⁺ ATPase. Predict the effect on the resting potential of a neuron over minutes to hours.", a: "Initially the resting potential is unchanged because the pump's direct electrogenic contribution is small. Over time, the Na⁺ and K⁺ gradients dissipate. K⁺ leak channels lose their driving force, and the cell depolarizes toward 0 mV, becoming unable to fire action potentials.", options: ["Immediate large depolarization to 0 mV within seconds", "Initially unchanged; over time gradients dissipate and the cell depolarizes toward 0 mV", "Immediate hyperpolarization toward -90 mV", "No change at all because leak channels maintain the gradient"], correctIndex: 1, explanation: "The pump's direct electrogenic contribution is small, so resting potential is initially nearly unchanged. Over minutes to hours, Na+ and K+ gradients dissipate. K+ loses its outward driving force, and the cell drifts toward 0 mV, eventually unable to fire. Immediate large changes do not match the pump's slow gradient-building role. Leak channels need gradients to work, so they cannot rescue the cell." }
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
            { id: "c1", dok: 1, q: "At what membrane potential does the typical neuron's threshold sit?", a: "About −55 mV.", options: ["About -90 mV", "About -70 mV", "About -55 mV", "About 0 mV"], correctIndex: 2, explanation: "Threshold sits near -55 mV in a typical neuron. Reaching it opens enough voltage-gated Na+ channels to start the regenerative depolarization. -90 mV is near the K+ equilibrium potential, more negative than rest. -70 mV is the resting potential. 0 mV is well past threshold." },
            { id: "c2", dok: 1, q: "What ion enters during depolarization?", a: "Sodium (Na⁺).", options: ["Potassium (K+)", "Sodium (Na+)", "Calcium (Ca2+)", "Chloride (Cl-)"], correctIndex: 1, explanation: "Voltage-gated Na+ channels open at threshold; Na+ floods in and depolarizes the membrane. K+ exits during repolarization, not depolarization. Ca2+ enters at the axon terminal to trigger neurotransmitter release, not during the rising phase of the AP. Cl- typically inhibits, not depolarizes." },
            { id: "c3", dok: 1, q: "What ion exits during repolarization?", a: "Potassium (K⁺).", options: ["Sodium (Na+)", "Calcium (Ca2+)", "Chloride (Cl-)", "Potassium (K+)"], correctIndex: 3, explanation: "Voltage-gated K+ channels open after the peak, K+ flows out down its gradient, and the membrane repolarizes. Na+ enters during depolarization, not repolarization. Ca2+ entry is at the axon terminal. Cl- movement is not the main repolarizing current." },
            { id: "c4", dok: 1, q: "What does 'all-or-none' mean for action potentials?", a: "Either a full-size AP is produced (above threshold) or none is (below threshold). Larger stimuli do not produce larger APs.", options: ["A larger stimulus produces a larger action potential", "Either a full-size AP fires (above threshold) or none fires (below)", "Action potentials gradually decay along the axon", "Multiple action potentials sum to produce a bigger one"], correctIndex: 1, explanation: "Above threshold, the AP is always full-size; below threshold, none fires. Stimulus strength is encoded by frequency, not by AP size. APs do not decay along a healthy axon; they regenerate. Single APs do not sum into a bigger AP; only graded potentials sum." },
            { id: "c5", dok: 1, q: "Which ion triggers neurotransmitter release at the axon terminal?", a: "Calcium (Ca²⁺).", options: ["Sodium (Na+)", "Potassium (K+)", "Calcium (Ca2+)", "Magnesium (Mg2+)"], correctIndex: 2, explanation: "When the AP reaches the axon terminal, voltage-gated Ca2+ channels open. Ca2+ entry triggers synaptic vesicles to fuse with the membrane and release neurotransmitter. Na+ depolarizes the membrane but does not trigger release. K+ repolarizes. Mg2+ can modulate channels but does not trigger release." },
            { id: "c6", dok: 2, q: "Explain why saltatory conduction is faster than continuous conduction.", a: "In myelinated axons, voltage-gated channels cluster at nodes of Ranvier. The AP regenerates only at nodes, effectively jumping between them rather than depolarizing every patch of membrane in sequence.", options: ["Myelin amplifies the AP, making each cycle stronger", "Voltage-gated channels cluster at nodes; the AP regenerates only at nodes, effectively jumping", "Myelin increases the membrane capacitance, speeding up conduction", "Myelinated axons have more Na+ channels along their entire length"], correctIndex: 1, explanation: "Myelin insulates internodal segments. Voltage-gated Na+ channels cluster at nodes of Ranvier, so the AP regenerates only at nodes, jumping between them. Myelin reduces membrane capacitance (not increases it) and decreases current leak. Channels are concentrated at nodes, not spread along the entire axon." },
            { id: "c7", dok: 2, q: "Why are action potentials usually unidirectional along an axon?", a: "After firing, the recently active region enters its absolute refractory period because Na⁺ channels are inactivated. The AP can only propagate forward into membrane that has not yet fired.", options: ["Na+ channels behind the AP are inactivated, so the AP can only move into fresh membrane", "K+ channels close behind the AP, preventing backward propagation", "The myelin sheath only allows forward conduction", "Ca2+ blocks backward Na+ channel opening"], correctIndex: 0, explanation: "Just-fired membrane enters the absolute refractory period because Na+ channels are inactivated. The AP can only propagate into membrane that has not yet fired. K+ channel closure repolarizes the membrane but does not by itself enforce direction. Myelin is not directional. Ca2+ is not the mechanism for refractoriness." },
            { id: "c8", dok: 2, q: "Compare an EPSP and an IPSP.", a: "EPSP: depolarizes the postsynaptic neuron, brings it closer to threshold. IPSP: hyperpolarizes (or stabilizes) it, moves it away from threshold. Both summate at the axon hillock to decide whether an AP fires.", options: ["EPSP hyperpolarizes the neuron; IPSP depolarizes it", "EPSP depolarizes (closer to threshold); IPSP hyperpolarizes or stabilizes (farther from threshold)", "EPSP fires an AP every time; IPSP blocks all APs", "Both depolarize but EPSP is faster than IPSP"], correctIndex: 1, explanation: "EPSPs depolarize the postsynaptic neuron, moving it closer to threshold. IPSPs hyperpolarize or stabilize it, moving it away from threshold. They summate at the axon hillock to determine whether an AP fires. EPSP and IPSP have opposite effects, so the first option reverses them. A single EPSP does not always fire an AP; many often summate." },
            { id: "c9", dok: 3, q: "Multiple sclerosis demyelinates CNS axons. Predict the conduction consequences and the symptom pattern.", a: "Without myelin, saltatory conduction fails. Voltage-gated channels are sparse between nodes, so APs may attenuate or fail entirely. Symptoms vary by tract: vision changes (optic nerve), weakness, sensory loss, coordination problems. Recovery between episodes occurs because some axons remain or partially remyelinate, but disability accumulates.", options: ["Saltatory conduction is enhanced; symptoms are mild and brief", "Saltatory conduction fails; APs attenuate or fail, producing variable deficits by tract", "Only motor tracts are affected, with no sensory or visual deficits", "All axons completely stop firing immediately"], correctIndex: 1, explanation: "Demyelination causes saltatory conduction to fail because internodal channels are sparse. APs slow, attenuate, or fail. Symptoms vary by tract: optic neuritis, weakness, sensory loss, ataxia. MS does not enhance conduction. It affects sensory, visual, and coordination tracts, not motor only. Conduction does not fail uniformly or all at once." },
            { id: "c10", dok: 3, q: "A patient is given an SSRI for depression. Mechanistically, why might the antidepressant effect take weeks to appear?", a: "The SSRI immediately blocks serotonin reuptake, raising synaptic serotonin. The slower effect comes from downstream changes: receptor desensitization, altered gene expression, neuroplastic remodeling. These take weeks, which is why clinical effects lag the pharmacology.", options: ["Serotonin synthesis must increase, which takes weeks", "Synaptic serotonin rises quickly, but downstream receptor and gene-expression changes take weeks", "SSRIs must accumulate in the bloodstream to reach a threshold dose", "Antidepressant effects come only from placebo response over time"], correctIndex: 1, explanation: "SSRIs immediately raise synaptic serotonin by blocking reuptake. The delayed clinical effect reflects slow downstream changes: receptor desensitization, altered gene expression, and neuroplastic remodeling. Serotonin synthesis does not need to increase as the limiting step. Drug levels reach steady state in days, not weeks. Placebo is real but not the main explanation for the delay." },
            { id: "c11", dok: 3, q: "Black widow venom causes massive ACh release at neuromuscular junctions, while botulinum toxin blocks ACh release entirely. Compare the muscular effects and explain why each occurs.", a: "Black widow: continuous ACh release causes sustained depolarization, painful cramping, then exhaustion of vesicles and weakness. Botulinum: no ACh release, so no depolarization, producing flaccid paralysis. Both can kill via respiratory muscle failure but by opposite mechanisms.", options: ["Black widow: flaccid paralysis from no ACh release; botulinum: cramping from too much ACh", "Black widow: massive ACh release causes cramping then weakness; botulinum: no ACh release causes flaccid paralysis", "Both cause spastic paralysis through the same mechanism", "Both block ACh receptors directly without changing release"], correctIndex: 1, explanation: "Black widow venom triggers massive ACh release, producing sustained depolarization, painful cramping, and then weakness as vesicles deplete. Botulinum toxin blocks ACh release entirely, producing flaccid paralysis. They produce opposite presynaptic effects. Neither acts by blocking postsynaptic receptors as the primary mechanism." },
            { id: "c12", dok: 3, q: "A drug specifically blocks voltage-gated Na⁺ channels in sensory nerves but not motor nerves. Predict the clinical effect and explain.", a: "Sensory neurons cannot generate APs, so the patient loses sensation (pain, touch, temperature) in the distribution served. Motor function is preserved because motor axons still fire. This selective profile is the basis of local anesthetics dosed for analgesia without paralysis.", options: ["Loss of sensation in the region served, with preserved motor function", "Loss of motor function with preserved sensation", "Complete paralysis and complete numbness in the region", "No clinical effect because both nerves remain intact"], correctIndex: 0, explanation: "Blocking voltage-gated Na+ channels in sensory nerves stops sensory APs, producing loss of pain, touch, and temperature sense in the served region. Motor axons keep firing because they are not blocked, so movement is preserved. This selective block is the principle behind local anesthetics dosed for analgesia without paralysis. Complete paralysis and no-effect options do not match the selectivity described." }
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
            { id: "c1", dok: 1, q: "Name the four lobes of the cerebrum.", a: "Frontal, parietal, temporal, occipital.", options: ["Frontal, parietal, temporal, occipital", "Frontal, parietal, temporal, cerebellar", "Frontal, central, temporal, occipital", "Frontal, parietal, occipital, brainstem"], correctIndex: 0, explanation: "The cerebrum has four named lobes: frontal, parietal, temporal, and occipital. The cerebellum and brainstem are separate structures, not cerebral lobes. There is no lobe called central; the central sulcus is a groove between the frontal and parietal lobes." },
            { id: "c2", dok: 1, q: "Where is the primary motor cortex?", a: "Precentral gyrus of the frontal lobe.", options: ["Postcentral gyrus of the parietal lobe", "Precentral gyrus of the temporal lobe", "Precentral gyrus of the frontal lobe", "Postcentral gyrus of the frontal lobe"], correctIndex: 2, explanation: "The primary motor cortex sits on the precentral gyrus of the frontal lobe, just in front of the central sulcus. The postcentral gyrus (parietal) is the primary somatosensory cortex. The temporal lobe handles hearing and aspects of memory, not voluntary motor output." },
            { id: "c3", dok: 1, q: "Name the three meningeal layers from outer to inner.", a: "Dura mater, arachnoid mater, pia mater.", options: ["Pia mater, arachnoid mater, dura mater", "Dura mater, pia mater, arachnoid mater", "Dura mater, arachnoid mater, pia mater", "Arachnoid mater, dura mater, pia mater"], correctIndex: 2, explanation: "From outer to inner the meninges are dura (tough, outermost), arachnoid (web-like middle), and pia (delicate layer hugging the brain surface). The other orderings rearrange these layers and reverse the outer-to-inner direction." },
            { id: "c4", dok: 1, q: "Where is CSF produced?", a: "Choroid plexuses in the ventricles.", options: ["Pituitary gland at the base of the brain", "Choroid plexuses in the ventricles", "Arachnoid granulations in the dural sinuses", "Central canal of the spinal cord"], correctIndex: 1, explanation: "CSF is produced by the choroid plexuses, capillary networks lining the ventricles. Arachnoid granulations reabsorb CSF, not make it. The central canal carries CSF but does not produce it. The pituitary makes hormones, not CSF." },
            { id: "c5", dok: 2, q: "Why does damage to the cerebellum produce coordination problems without paralysis?", a: "The cerebellum modulates motor commands generated elsewhere; it does not generate them. Damage leaves the motor pathways intact (no paralysis) but removes coordination, smoothing, and timing.", options: ["The cerebellum generates voluntary movement directly, so damage stops new movements but leaves old ones intact", "The cerebellum stores motor memories; damage erases learned movements while reflexes still work", "The cerebellum only handles balance, so damage affects standing but not arm movements", "The cerebellum modulates motor commands generated elsewhere, so damage leaves motor pathways intact but disrupts coordination and timing"], correctIndex: 3, explanation: "The cerebellum fine-tunes movements that originate in the motor cortex; the descending motor pathways still work, so strength is preserved while smoothing and timing are lost. The motor cortex (not cerebellum) generates voluntary movement. The cerebellum coordinates more than balance, including arm and hand movements. It is not a simple storage site for motor memories." },
            { id: "c6", dok: 3, q: "A stroke damages the left middle cerebral artery territory in a right-handed patient. Predict the deficits and explain why each occurs.", a: "Right-sided weakness (left motor cortex damaged, contralateral control). Right-sided sensory loss (left somatosensory cortex). Language impairment because Broca and Wernicke areas are usually left-hemispheric in right-handed people. Likely also right-sided visual field cut depending on extent.", options: ["Right-sided weakness, right-sided sensory loss, and language impairment because the left hemisphere controls the right side and houses language areas in most right-handers", "Left-sided weakness, left-sided sensory loss, and language impairment because motor and sensory control are ipsilateral", "Right-sided weakness only, with no sensory or language deficits because the MCA supplies only motor cortex", "Bilateral weakness and language impairment because the MCA supplies both hemispheres"], correctIndex: 0, explanation: "Motor and sensory control are contralateral, so a left hemisphere stroke produces right-sided weakness and sensory loss. Language areas (Broca and Wernicke) are typically left-hemispheric in right-handers, so language is affected. The MCA supplies one hemisphere, not both, and supplies more than just motor cortex." }
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
            { id: "c1", dok: 1, q: "Which cranial nerve has the broadest parasympathetic distribution?", a: "Vagus (CN X).", options: ["Trigeminal (CN V)", "Facial (CN VII)", "Vagus (CN X)", "Glossopharyngeal (CN IX)"], correctIndex: 2, explanation: "The vagus nerve carries parasympathetic fibers to the heart, lungs, and most of the GI tract, giving it the broadest distribution. CN VII and IX carry parasympathetic fibers but only to head and neck targets. CN V is primarily sensory to the face and motor to muscles of mastication, not parasympathetic." },
            { id: "c2", dok: 1, q: "List the five components of a reflex arc.", a: "Receptor, sensory neuron, integration center, motor neuron, effector.", options: ["Stimulus, sensory neuron, brain, motor neuron, response", "Receptor, sensory neuron, integration center, motor neuron, effector", "Receptor, interneuron, sensory neuron, motor neuron, muscle", "Sensory neuron, integration center, interneuron, motor neuron, effector"], correctIndex: 1, explanation: "A reflex arc has five components: receptor (detects), sensory neuron (carries signal in), integration center (processes, usually in the spinal cord), motor neuron (carries signal out), and effector (responds). Many reflexes never reach the brain. Stimulus and response are events, not anatomical components." },
            { id: "c3", dok: 1, q: "What neurotransmitter does the sympathetic nervous system release at most target organs?", a: "Norepinephrine.", options: ["Acetylcholine", "Norepinephrine", "Dopamine", "Epinephrine"], correctIndex: 1, explanation: "Most sympathetic postganglionic fibers release norepinephrine at their target organs. Acetylcholine is the parasympathetic and preganglionic neurotransmitter (and at sweat glands). Epinephrine comes from the adrenal medulla into the bloodstream, not from typical sympathetic nerve endings. Dopamine is not the main autonomic transmitter at target organs." },
            { id: "c4", dok: 1, q: "How many pairs of spinal nerves are there?", a: "31.", options: ["12", "24", "31", "33"], correctIndex: 2, explanation: "There are 31 pairs of spinal nerves: 8 cervical, 12 thoracic, 5 lumbar, 5 sacral, and 1 coccygeal. 12 is the number of cranial nerve pairs. 33 is approximately the number of vertebrae (including fused sacral/coccygeal). 24 has no anatomical match here." },
            { id: "c5", dok: 2, q: "Predict the sympathetic effects of an adrenaline surge during a fight-or-flight response.", a: "Heart rate and contractility rise. Bronchi dilate. Pupils dilate. Sweat glands activate. Blood is shunted to skeletal muscle; gut motility and glandular secretion fall. Glycogen breakdown rises, raising blood glucose.", options: ["Heart rate falls, bronchi constrict, pupils constrict, and blood is shunted to the gut", "Heart rate rises, bronchi dilate, pupils dilate, blood shunts to skeletal muscle, and blood glucose rises", "Heart rate rises, bronchi constrict, pupils dilate, and gut motility increases", "Heart rate falls, bronchi dilate, pupils dilate, and glucose uptake into cells rises"], correctIndex: 1, explanation: "Sympathetic activation prepares the body for action: faster, harder heartbeat; airways open; pupils widen to take in more visual information; blood diverts from gut to working muscle; glycogen breaks down to fuel activity. The other options mix in parasympathetic effects (slowed heart, constricted bronchi, increased gut motility) that belong to rest-and-digest." },
            { id: "c6", dok: 3, q: "A patient with a spinal cord transection at C5 retains some reflexes below the lesion but cannot move voluntarily. Explain why both observations make sense.", a: "Voluntary movement requires descending tracts from the motor cortex through the spinal cord. The transection severs these, so no voluntary movement below the lesion. Reflex arcs depend only on local spinal circuitry (receptor → sensory → spinal cord → motor → effector), which remains intact below the lesion.", options: ["Voluntary movement is impossible because descending tracts are severed, but local reflex arcs below the lesion still work since they only need spinal circuitry", "Voluntary movement is impossible because muscles atrophy immediately, but reflexes use a separate muscle system", "Voluntary movement is impossible because the brain stops sending signals entirely, and any reflex below the lesion is a sign of recovery", "Voluntary movement is impossible because sensory neurons are cut, but motor neurons keep firing reflexively on their own"], correctIndex: 0, explanation: "Voluntary movement needs intact descending tracts from the motor cortex through the cord; the transection cuts them. Reflex arcs only need a working loop at the spinal level (receptor, sensory neuron, cord, motor neuron, effector), which is preserved below the lesion. Muscles do not atrophy immediately, and motor neurons do not fire on their own without sensory input." }
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
          lecturePageUrl: "vision.html",
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
            { id: "c1", dok: 1, q: "Which photoreceptor is responsible for color vision?", a: "Cones.", options: ["Rods", "Cones", "Bipolar cells", "Ganglion cells"], correctIndex: 1, explanation: "Cones contain three pigment types tuned to different wavelengths and are responsible for color vision. Rods are sensitive in dim light but do not encode color. Bipolar and ganglion cells are downstream relay neurons in the retina, not photoreceptors." },
            { id: "c2", dok: 1, q: "Where is the area of sharpest vision in the retina?", a: "The fovea.", options: ["The optic disc", "The peripheral retina", "The fovea", "The macula lutea edge"], correctIndex: 2, explanation: "The fovea is the small central pit packed with cones and has the sharpest acuity. The optic disc has no photoreceptors and is the blind spot. The peripheral retina is rod-dominated and lower in acuity. The fovea sits within the macula but the edge of the macula is not the point of sharpest vision." },
            { id: "c3", dok: 1, q: "Which structure provides most of the eye's fixed refractive power?", a: "The cornea.", options: ["The lens", "The iris", "The pupil", "The cornea"], correctIndex: 3, explanation: "The cornea provides about two-thirds of the eye's fixed refractive power because of the large change in refractive index at the air-cornea interface. The lens fine-tunes focus through accommodation but contributes less total power. The iris and pupil control how much light enters; they do not refract it." },
            { id: "c4", dok: 2, q: "Why is the optic disc a 'blind spot'?", a: "It is where the optic nerve exits the retina. No photoreceptors are present, so light hitting that spot generates no signal.", options: ["It is covered by blood vessels that block incoming light", "It is where the optic nerve exits the retina and has no photoreceptors", "It contains only rods, which cannot fire in normal daylight", "It is shadowed by the lens during normal eye movement"], correctIndex: 1, explanation: "The optic disc is the point where ganglion cell axons exit the eye as the optic nerve. No rods or cones sit there, so light hitting that spot generates no signal. Blood vessels do cross the retina but are not the reason for the blind spot. The disc is not rod-only, and the lens does not shadow it." },
            { id: "c5", dok: 2, q: "Explain why night vision is mostly black and white.", a: "Rods dominate at low light, but rods do not encode color. Cones, which encode color, are not sensitive enough to fire in dim light.", options: ["Rods dominate at low light but do not encode color, and cones are not sensitive enough to fire in dim light", "Cones shut off completely at night to save energy, leaving only black and white vision", "The pupil constricts at night, blocking the wavelengths needed for color", "Color pigments are bleached by darkness and need light to reset"], correctIndex: 0, explanation: "Rods take over in dim light and are colorblind; cones need brighter light to fire, so color washes out at night. Cones do not actively shut off; they simply lack the sensitivity to respond. The pupil dilates (not constricts) in low light. Pigments are bleached by light, not by darkness." },
            { id: "c6", dok: 3, q: "A patient is diagnosed with presbyopia (loss of near vision with age). Explain the mechanism.", a: "With age, the lens becomes less elastic. The ciliary muscle can still contract, but the lens no longer rounds up enough during accommodation. Near objects cannot be focused on the retina, requiring reading glasses.", options: ["The cornea flattens with age, reducing refractive power for near objects", "The retina thickens with age, blocking light from reaching photoreceptors", "The lens becomes less elastic with age, so it cannot round up enough during accommodation to focus near objects", "The ciliary muscle weakens with age and can no longer pull the lens flat for near vision"], correctIndex: 2, explanation: "With age the lens stiffens and cannot round up enough during accommodation, so the focal point for near objects falls behind the retina. The ciliary muscle still contracts; the problem is the lens, not the muscle, and the muscle relaxes (not pulls flat) to round the lens. The cornea does not significantly change shape with age, and retinal thickening is not the cause." }
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
            { id: "c1", dok: 1, q: "Name the three middle ear ossicles in order.", a: "Malleus, incus, stapes.", options: ["Malleus, incus, stapes", "Incus, malleus, stapes", "Stapes, incus, malleus", "Malleus, stapes, incus"], correctIndex: 0, explanation: "From the tympanic membrane inward, the ossicles are malleus (hammer), incus (anvil), then stapes (stirrup), which contacts the oval window. The other orderings rearrange the chain. Remembering MIS in order matches sound traveling from outer to inner ear." },
            { id: "c2", dok: 1, q: "Which structure contains the hair cells for hearing?", a: "The organ of Corti (on the basilar membrane within the cochlea).", options: ["The tympanic membrane", "The semicircular canals", "The organ of Corti on the basilar membrane within the cochlea", "The vestibule between the cochlea and semicircular canals"], correctIndex: 2, explanation: "The organ of Corti sits on the basilar membrane inside the cochlea and contains the hair cells that transduce vibration into auditory signals. The tympanic membrane vibrates but is not a hair cell site. Semicircular canals and the vestibule contain hair cells for balance, not hearing." },
            { id: "c3", dok: 1, q: "Which structures detect rotational acceleration?", a: "Semicircular canals.", options: ["The cochlea", "The semicircular canals", "The utricle and saccule", "The tympanic membrane"], correctIndex: 1, explanation: "The three semicircular canals are oriented in different planes and detect rotational (angular) acceleration of the head. The utricle and saccule detect linear acceleration and head tilt. The cochlea is for hearing. The tympanic membrane transmits sound vibration." },
            { id: "c4", dok: 2, q: "Why does damage to high-frequency hair cells at the base of the cochlea cause age-related hearing loss?", a: "High frequencies are encoded at the base of the basilar membrane, which receives the most vibration over a lifetime. Cumulative damage to these hair cells leads to high-frequency hearing loss (presbycusis).", options: ["Low frequencies are encoded at the base of the cochlea, where most vibration occurs", "All frequencies are encoded everywhere; aging hair cells just lose their connection to the brain", "High frequencies are encoded at the base of the basilar membrane, which receives the most cumulative vibration over a lifetime", "High frequencies are encoded at the apex of the cochlea, which is most exposed to loud sounds"], correctIndex: 2, explanation: "The basilar membrane is tonotopically organized: high frequencies map to the stiff base, low frequencies to the flexible apex. Base hair cells receive vibration from every sound, accumulating wear, which is why presbycusis hits high frequencies first. Frequencies are not encoded everywhere, and the apex handles low (not high) frequencies." },
            { id: "c5", dok: 3, q: "A patient with vertigo has loose calcium carbonate crystals (otoconia) drifting into a semicircular canal. Predict the symptom pattern and explain why.", a: "Head movements displace the wandering otoconia, abnormally bending hair cells in the canal. The brain interprets this as ongoing rotation when there is none, producing brief episodes of spinning vertigo triggered by position change (benign paroxysmal positional vertigo, BPPV).", options: ["Head movements displace the loose otoconia, abnormally bending hair cells in the canal, so the brain perceives spinning that is not happening", "The otoconia block sound from reaching the cochlea, producing dizziness from hearing loss", "The otoconia stop hair cells from bending at all, so the brain receives no balance signal and the patient feels weightless", "The otoconia trigger inflammation in the brainstem, causing constant spinning vertigo regardless of position"], correctIndex: 0, explanation: "In BPPV, displaced otoconia drift into a semicircular canal and shift with head position, bending hair cells when they should not. The brain reads this as ongoing rotation, producing brief positional vertigo. The otoconia do not block sound or shut off hair cells entirely, and the issue is mechanical inside the inner ear, not brainstem inflammation." }
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
            { id: "c1", dok: 1, q: "Where are steroid hormone receptors located?", a: "Inside the cell (cytoplasm or nucleus).", options: ["On the cell membrane, where they trigger second messengers", "Inside the cell, in the cytoplasm or nucleus", "In the extracellular matrix near target cells", "On the membranes of organelles only, not in the cytoplasm"], correctIndex: 1, explanation: "Steroid hormones are lipid-soluble and pass through the plasma membrane to bind intracellular receptors in the cytoplasm or nucleus, where they modulate gene transcription. Membrane-bound receptors are characteristic of peptide hormones, not steroids. The extracellular matrix is not the receptor site." },
            { id: "c2", dok: 1, q: "Name the second messenger triggered by many peptide hormones.", a: "Cyclic AMP (cAMP).", options: ["Calcium directly entering the nucleus", "Cyclic AMP (cAMP)", "Cortisol bound to nuclear receptors", "Adenosine triphosphate (ATP) on its own"], correctIndex: 1, explanation: "Many peptide hormones bind G-protein-coupled receptors, activating adenylyl cyclase to convert ATP into cAMP, the classic second messenger. ATP is the source molecule, not the messenger itself. Cortisol is a steroid hormone, not a second messenger. Ca2+ is a second messenger in some pathways but does not act by entering the nucleus." },
            { id: "c3", dok: 1, q: "Which hormone class generally acts faster: steroid or peptide?", a: "Peptide (second messenger cascades act in seconds; steroid effects via gene transcription take hours).", options: ["Steroid, because lipid-soluble hormones cross membranes instantly", "They act at the same speed because both bind receptors directly", "Steroid, because gene transcription is faster than enzyme cascades", "Peptide, because second messenger cascades act in seconds while steroid effects via gene transcription take hours"], correctIndex: 3, explanation: "Peptide hormones trigger pre-made enzyme cascades and produce effects in seconds to minutes. Steroid hormones change gene expression, which requires transcription and translation, taking hours. Crossing the membrane quickly is not the same as producing a fast cellular response." },
            { id: "c4", dok: 2, q: "Explain why peptide hormones must be administered by injection (not orally).", a: "Peptide hormones are proteins. They would be digested by gastric and intestinal proteases if swallowed. Injection bypasses the GI tract.", options: ["They are too large to dissolve in water and would precipitate in the stomach", "They are proteins and would be digested by gastric and intestinal proteases if swallowed", "They are inactivated by stomach acid only and would work fine if given with antacids", "They are absorbed too quickly orally and reach toxic levels"], correctIndex: 1, explanation: "Peptide hormones are made of amino acids, so digestive proteases would break them down into inactive fragments before absorption. Acid alone is not the limiting factor, and antacids would not solve the proteolysis problem. They do not precipitate or absorb too quickly; they would never get into the bloodstream intact." },
            { id: "c5", dok: 3, q: "A patient with autoimmune destruction of the adrenal cortex (primary adrenal insufficiency) presents with high ACTH levels. Explain.", a: "The damaged cortex cannot make cortisol. Without cortisol, the long-loop negative feedback on the pituitary is lost. The pituitary releases ACTH unchecked, producing high ACTH levels (and the skin hyperpigmentation associated with elevated POMC-derived peptides).", options: ["The damaged cortex cannot make cortisol, so negative feedback on the pituitary is lost and ACTH rises unchecked", "The damaged cortex overproduces ACTH directly to compensate for missing cortisol", "ACTH is made by the adrenal cortex, so destruction releases stored ACTH into the blood", "The pituitary detects high cortisol and ramps up ACTH in response"], correctIndex: 0, explanation: "Cortisol normally feeds back negatively on the pituitary to limit ACTH release. When the adrenal cortex cannot make cortisol, that brake is gone and the pituitary keeps releasing ACTH. ACTH comes from the pituitary, not the adrenal cortex. The pituitary responds to low (not high) cortisol with more ACTH." }
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
            { id: "c1", dok: 1, q: "Which gland releases ADH?", a: "The posterior pituitary (synthesized by the hypothalamus, stored and released by the posterior pituitary).", options: ["The anterior pituitary", "The hypothalamus directly into the bloodstream", "The posterior pituitary, after synthesis in the hypothalamus", "The adrenal medulla under hypothalamic control"], correctIndex: 2, explanation: "ADH is made by hypothalamic neurons, transported down their axons, and stored in the posterior pituitary, which releases it into the blood. The anterior pituitary makes its own hormones (ACTH, TSH, GH, etc.). The hypothalamus does not release ADH directly; the posterior pituitary does. The adrenal medulla releases catecholamines, not ADH." },
            { id: "c2", dok: 1, q: "Name the two main hormones of the pancreatic islets and what they do.", a: "Insulin lowers blood glucose; glucagon raises it.", options: ["Insulin raises blood glucose; glucagon lowers it", "Insulin lowers blood glucose; glucagon raises it", "Insulin and glucagon both lower blood glucose through different pathways", "Insulin stores fat; glucagon stores protein"], correctIndex: 1, explanation: "Beta cells release insulin, which drives glucose into cells and lowers blood glucose. Alpha cells release glucagon, which raises blood glucose by stimulating hepatic glucose release. Their actions are opposing, not parallel, and the directions are not reversed." },
            { id: "c3", dok: 1, q: "What hormone raises blood Ca²⁺?", a: "Parathyroid hormone (PTH).", options: ["Calcitonin", "Aldosterone", "Parathyroid hormone (PTH)", "Cortisol"], correctIndex: 2, explanation: "PTH raises blood Ca2+ by mobilizing bone calcium, increasing renal reabsorption, and activating vitamin D for gut absorption. Calcitonin does the opposite, lowering blood Ca2+. Aldosterone regulates Na+ and K+, not Ca2+. Cortisol is a stress hormone with broad metabolic effects, not a primary Ca2+ regulator." },
            { id: "c4", dok: 1, q: "Which adrenal layer makes aldosterone?", a: "Zona glomerulosa of the adrenal cortex.", options: ["Zona fasciculata of the adrenal cortex", "Zona reticularis of the adrenal cortex", "Adrenal medulla", "Zona glomerulosa of the adrenal cortex"], correctIndex: 3, explanation: "The adrenal cortex has three zones from outer to inner: glomerulosa (aldosterone), fasciculata (cortisol), reticularis (androgens). The medulla makes catecholamines like epinephrine, not aldosterone. Remember GFR matches salt, sugar, sex." },
            { id: "c5", dok: 2, q: "Type 1 diabetes is caused by autoimmune destruction of pancreatic beta cells. Explain the resulting hyperglycemia mechanistically.", a: "Beta cells make insulin. Without insulin, cells cannot take up glucose efficiently and the liver continues to release glucose. Blood glucose rises and stays high, producing osmotic diuresis, dehydration, and eventually ketoacidosis.", options: ["Without insulin, cells cannot take up glucose efficiently and the liver keeps releasing glucose, so blood glucose climbs and stays high", "Beta cell destruction releases stored glucose directly into the blood, causing the rise", "Loss of beta cells leads to glucagon deficiency, raising blood glucose", "Without insulin, the kidneys reabsorb extra glucose, raising blood levels"], correctIndex: 0, explanation: "Insulin is the main signal that pushes glucose into cells and tells the liver to stop releasing more. Without it, uptake fails and hepatic output continues, so glucose accumulates. Beta cells do not store glucose. Glucagon comes from alpha cells, which are intact. Without insulin, kidneys actually spill glucose into urine, not reabsorb extra." },
            { id: "c6", dok: 3, q: "Cushing syndrome features high cortisol. Predict three findings and tie them to cortisol's actions.", a: "Hyperglycemia (cortisol promotes gluconeogenesis and inhibits glucose uptake). Central obesity and muscle wasting (cortisol breaks down peripheral protein and redistributes fat). Immunosuppression and poor wound healing (cortisol suppresses immune function and collagen synthesis). Hypertension is also common (cortisol has weak mineralocorticoid activity).", options: ["Hypoglycemia, muscle gain, and improved wound healing because cortisol enhances anabolism", "Hyperglycemia from gluconeogenesis, muscle wasting from peripheral protein breakdown, and immunosuppression with poor wound healing", "Low blood pressure, weight loss, and increased immune response because cortisol depletes peripheral fat", "Hyperglycemia, dehydration, and enhanced collagen production because cortisol favors glucose and tissue repair"], correctIndex: 1, explanation: "Cortisol raises blood glucose (gluconeogenesis, decreased uptake), breaks down peripheral protein causing muscle wasting and central fat redistribution, and suppresses immune function and collagen synthesis, slowing wound healing. The other options reverse cortisol's known catabolic and immunosuppressive effects." }
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
            { id: "c1", dok: 1, q: "What percentage of blood is plasma?", a: "About 55%.", options: ["About 25%", "About 45%", "About 55%", "About 75%"], correctIndex: 2, explanation: "Plasma makes up about 55% of blood by volume. Red blood cells (hematocrit) account for about 45%, with white cells and platelets forming a thin buffy coat. The other values do not match the standard plasma fraction." },
            { id: "c2", dok: 1, q: "Name the most abundant leukocyte.", a: "Neutrophil.", options: ["Lymphocyte", "Monocyte", "Neutrophil", "Eosinophil"], correctIndex: 2, explanation: "Neutrophils are the most abundant white blood cells (roughly 50 to 70% of leukocytes) and are first responders in bacterial infection. Lymphocytes are the next most common but fewer. Monocytes and eosinophils are present in smaller numbers." },
            { id: "c3", dok: 1, q: "What is the lifespan of a red blood cell?", a: "About 120 days.", options: ["About 24 hours", "About 30 days", "About 120 days", "About 1 year"], correctIndex: 2, explanation: "Red blood cells circulate for about 120 days before being removed by macrophages in the spleen and liver. 24 hours is closer to the lifespan of a circulating neutrophil. 30 days and 1 year do not match RBC physiology." },
            { id: "c4", dok: 1, q: "Where is erythropoietin made?", a: "Kidney (peritubular cells).", options: ["Liver (hepatocytes)", "Bone marrow (stromal cells)", "Spleen (red pulp)", "Kidney (peritubular cells)"], correctIndex: 3, explanation: "Peritubular cells in the kidney sense oxygen levels and secrete erythropoietin (EPO), which drives bone marrow to make red cells. The bone marrow is the target of EPO, not the source. The liver makes a small amount in fetal life but the kidney is the main adult source. The spleen recycles old RBCs." },
            { id: "c5", dok: 2, q: "Why do RBCs lack a nucleus?", a: "Removing the nucleus maximizes hemoglobin packing and the biconcave shape, both of which favor gas transport and deformability through capillaries. The trade-off is no protein synthesis and a finite lifespan.", options: ["Removing the nucleus maximizes hemoglobin packing and the biconcave shape, favoring gas transport and deformability, at the cost of no protein synthesis and a finite lifespan", "RBCs lose the nucleus to fit through capillaries; this also lets them make new hemoglobin on demand", "RBCs never had a nucleus because they are not true cells, just hemoglobin sacs", "Removing the nucleus prevents RBCs from carrying genetic material to other tissues"], correctIndex: 0, explanation: "Losing the nucleus frees space for hemoglobin and supports the flexible biconcave shape, which is ideal for gas exchange and squeezing through capillaries. The trade-off is that RBCs cannot synthesize new proteins and must be replaced regularly. RBCs are real cells that start with a nucleus and extrude it during development." },
            { id: "c6", dok: 3, q: "A patient with chronic kidney disease is anemic. Connect the kidney failure to the anemia.", a: "Damaged kidneys make less erythropoietin. Without enough EPO signal, the bone marrow underproduces erythrocytes. RBC mass falls, oxygen-carrying capacity drops, and anemia results. Treatment often includes recombinant EPO.", options: ["Damaged kidneys filter out red blood cells into the urine, dropping RBC mass", "Damaged kidneys make less erythropoietin, so the marrow underproduces RBCs and oxygen-carrying capacity falls", "Damaged kidneys destroy red blood cells directly through immune attack", "Damaged kidneys retain iron, preventing the marrow from using it for hemoglobin"], correctIndex: 1, explanation: "Healthy kidneys make EPO to stimulate RBC production. In chronic kidney disease, EPO output falls, the marrow underproduces red cells, and anemia results. Often treated with recombinant EPO. Kidneys do not destroy RBCs or normally lose them into urine, and iron retention is not the mechanism." }
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
            { id: "c1", dok: 1, q: "Name the three phases of hemostasis.", a: "Vascular spasm, platelet plug formation, coagulation.", options: ["Vascular spasm, platelet plug formation, coagulation", "Coagulation, platelet plug formation, vascular spasm", "Platelet plug, fibrinolysis, vascular spasm", "Vascular spasm, fibrinolysis, coagulation"], correctIndex: 0, explanation: "Hemostasis proceeds in order: vessel constricts (spasm), platelets aggregate at the injury (platelet plug), then the coagulation cascade forms fibrin to stabilize the clot. Fibrinolysis is clot breakdown afterward, not a hemostasis phase. The other orderings reverse the sequence." },
            { id: "c2", dok: 1, q: "Which protein is the final product of the coagulation cascade?", a: "Fibrin.", options: ["Thrombin", "Plasmin", "Prothrombin", "Fibrin"], correctIndex: 3, explanation: "Fibrin is the insoluble protein mesh that traps cells and stabilizes the clot, and it is the cascade's final structural product. Thrombin is the enzyme that converts fibrinogen to fibrin. Prothrombin is the inactive precursor of thrombin. Plasmin breaks fibrin down later during fibrinolysis." },
            { id: "c3", dok: 1, q: "Which blood type is the universal RBC donor?", a: "Type O (no A or B antigens on RBCs).", options: ["Type A", "Type B", "Type AB", "Type O"], correctIndex: 3, explanation: "Type O RBCs have neither A nor B antigens, so they are unlikely to trigger antibody attack in recipients regardless of recipient blood type. Type AB is the universal plasma donor (no anti-A or anti-B antibodies) but is the worst RBC donor because both antigens are present. Types A and B carry their respective antigens." },
            { id: "c4", dok: 1, q: "Which blood type is the universal plasma donor?", a: "Type AB (no anti-A or anti-B antibodies in plasma).", options: ["Type O", "Type A", "Type B", "Type AB"], correctIndex: 3, explanation: "Type AB plasma has neither anti-A nor anti-B antibodies, so it will not attack a recipient's RBCs regardless of their type. Type O plasma contains both antibodies and is the worst plasma donor. Type A plasma carries anti-B antibodies, and type B plasma carries anti-A." },
            { id: "c5", dok: 2, q: "Why are Rh− women given RhoGAM during and after pregnancy?", a: "If the fetus is Rh+, fetal blood entering maternal circulation could sensitize the mother to make anti-Rh antibodies. In a future Rh+ pregnancy these antibodies could cross the placenta and attack the fetus. RhoGAM neutralizes fetal Rh+ cells in the mother before her immune system mounts a response.", options: ["RhoGAM treats fetal anemia directly by replacing fetal red cells with maternal ones", "RhoGAM raises the mother's Rh+ antigen levels so her body learns to tolerate the fetus", "RhoGAM neutralizes any fetal Rh+ cells in the mother before her immune system makes anti-Rh antibodies that could attack a future Rh+ fetus", "RhoGAM is given to the fetus through the placenta to prevent it from making anti-Rh antibodies"], correctIndex: 2, explanation: "RhoGAM is anti-Rh antibody given to the Rh- mother. It binds and clears any fetal Rh+ cells in her blood before her own immune system can mount a memory response, protecting future Rh+ pregnancies. It does not treat the fetus directly, raise maternal antigen levels, or get given to the fetus." },
            { id: "c6", dok: 3, q: "A patient with severe liver disease has prolonged bleeding times. Explain mechanistically.", a: "The liver synthesizes most clotting factors (II, VII, IX, X, fibrinogen, and others). With hepatic failure, factor levels drop. The cascade slows or stalls, fibrin formation is delayed, and bleeding times prolong.", options: ["Liver disease destroys platelets directly, slowing the platelet plug phase", "Liver disease blocks vitamin K absorption, which is the only mechanism for slow clotting", "Liver disease raises fibrinogen levels, which paradoxically slows clotting", "The liver synthesizes most clotting factors; with liver failure, factor levels drop, the cascade stalls, and bleeding times prolong"], correctIndex: 3, explanation: "Hepatocytes make most clotting factors (II, VII, IX, X, fibrinogen, and others). In hepatic failure, these factors fall, slowing fibrin formation and prolonging bleeding. Vitamin K activation is also liver-dependent but is not the only mechanism. The liver does not directly destroy platelets, and fibrinogen actually drops in liver failure." }
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
            { id: "c1", dok: 1, q: "Which valves close at the start of ventricular systole?", a: "The atrioventricular (tricuspid and mitral) valves.", options: ["The semilunar (aortic and pulmonary) valves", "Only the mitral valve", "The atrioventricular (tricuspid and mitral) valves", "All four valves simultaneously"], correctIndex: 2, explanation: "At the start of ventricular systole, rising ventricular pressure slams the AV valves shut, producing S1. The semilunar valves close at the END of systole, producing S2. Only the mitral closing would be a one-sided event; both AV valves close together." },
            { id: "c2", dok: 1, q: "Which valves close at the end of ventricular systole?", a: "The semilunar (aortic and pulmonary) valves.", options: ["The atrioventricular valves", "The semilunar (aortic and pulmonary) valves", "Only the aortic valve", "All four valves at once"], correctIndex: 1, explanation: "As the ventricles relax and pressure falls below aortic and pulmonary pressures, the semilunar valves close, producing S2. The AV valves closed earlier, at the start of systole (S1). Only the aortic would not account for the pulmonary side." },
            { id: "c3", dok: 1, q: "What is happening during isovolumetric contraction?", a: "All four valves are closed; ventricles contract and pressure rises sharply without any volume change.", options: ["AV valves are open, blood flows in, and ventricles fill while pressure stays low", "Semilunar valves are open and blood is ejected into the great arteries", "All four valves are closed; ventricles contract and pressure rises sharply without any volume change", "Atria contract and push blood into ventricles while semilunar valves stay closed"], correctIndex: 2, explanation: "Isovolumetric contraction is the brief phase after AV valves close but before semilunar valves open. No blood moves in or out, so volume is fixed while pressure climbs. Filling and ejection happen in other phases of the cycle, and atrial contraction is not isovolumetric." },
            { id: "c4", dok: 1, q: "Which side of the heart pumps oxygenated blood?", a: "The left side.", options: ["The right side", "The left side", "Both sides equally", "Only the left atrium"], correctIndex: 1, explanation: "The left side receives oxygenated blood from the lungs (via pulmonary veins) and pumps it to the systemic circulation. The right side handles deoxygenated blood and pumps it to the lungs. The two sides pump in series, not equally to the same circuit." },
            { id: "c5", dok: 1, q: "Which sound (S1 or S2) marks the beginning of systole?", a: "S1.", options: ["S1, from closure of the AV valves", "S2, from closure of the semilunar valves", "S3, from rapid ventricular filling", "S4, from atrial contraction against a stiff ventricle"], correctIndex: 0, explanation: "S1 (lub) marks closure of the AV valves at the start of ventricular systole. S2 (dub) marks the end of systole. S3 and S4 are extra heart sounds tied to filling phases and are not normal markers of systole onset." },
            { id: "c6", dok: 2, q: "Why does ventricular volume not change during isovolumetric contraction?", a: "All four valves are closed. Blood cannot leave the ventricle or enter it, but the muscle is contracting, so pressure climbs while volume holds steady.", options: ["The AV valves are open, allowing blood to leave the ventricle while it contracts", "All four valves are closed, so blood cannot leave or enter while the muscle contracts", "The semilunar valves open early to release pressure without volume change", "The atria contract simultaneously, balancing inflow and outflow"], correctIndex: 1, explanation: "All four valves are shut during isovolumetric contraction. Blood is trapped in the ventricle; the muscle squeezes, and pressure rises, but volume is fixed because nothing can move in or out. Open AV or semilunar valves would allow flow, breaking the isovolumetric condition." },
            { id: "c7", dok: 2, q: "Predict the consequence of a leaky mitral valve (mitral regurgitation).", a: "During ventricular systole, some blood flows backward into the left atrium instead of forward into the aorta. Forward cardiac output drops; left atrial pressure rises; over time pulmonary congestion develops, and the left ventricle dilates from chronic volume overload.", options: ["Forward cardiac output rises because the heart pumps blood through two paths", "Some blood flows backward into the left atrium during systole, dropping forward output, raising left atrial pressure, and over time causing pulmonary congestion and LV dilation", "Blood backs up into the right ventricle, causing right-sided heart failure first", "Mitral regurgitation has no effect because the aortic valve compensates"], correctIndex: 1, explanation: "A leaky mitral valve lets blood regurgitate into the left atrium during systole, reducing forward stroke volume. Left atrial pressure rises, eventually congesting the pulmonary circuit, and chronic volume overload dilates the LV. Forward output does not rise, and the right side is not the first to fail." },
            { id: "c8", dok: 2, q: "Why does aortic stenosis lead to left ventricular hypertrophy?", a: "Narrow aortic valve increases the pressure the LV must generate to eject blood. Chronic pressure overload triggers concentric hypertrophy: sarcomeres added in parallel, wall thickens, chamber radius preserved.", options: ["The narrow valve reduces afterload, so the LV shrinks over time", "The narrow valve raises the pressure the LV must generate; chronic pressure overload triggers concentric hypertrophy with thicker walls", "The narrow valve lets blood flow backward into the LV, dilating it", "Aortic stenosis only affects the right ventricle"], correctIndex: 1, explanation: "A stenotic aortic valve forces the LV to generate higher pressure to eject blood. Chronic pressure overload adds sarcomeres in parallel, thickening the wall (concentric hypertrophy). Stenosis raises afterload, not reduces it. Backflow describes regurgitation, not stenosis. The right ventricle is not directly affected." },
            { id: "c9", dok: 3, q: "A patient has heart failure with reduced ejection fraction (EF = 25%). Explain the term and predict three downstream consequences.", a: "Ejection fraction = stroke volume / end-diastolic volume. 25% means only a quarter of the LV blood is ejected per beat. Consequences: fatigue and exercise intolerance (low forward output), pulmonary congestion (blood backs up into pulmonary circuit), and activation of compensatory systems (sympathetic and RAAS) that initially help but worsen the disease over time.", options: ["EF = stroke volume divided by end-diastolic volume; 25% means low forward output causing fatigue, pulmonary congestion as blood backs up, and compensatory sympathetic and RAAS activation that worsens disease over time", "EF = cardiac output divided by heart rate; 25% means the heart skips three of every four beats", "EF = end-diastolic volume divided by stroke volume; 25% means the ventricle holds four times what it ejects, but output is normal", "EF = stroke volume divided by cardiac output; 25% means the ventricle is in early disease with no symptoms expected"], correctIndex: 0, explanation: "Ejection fraction is the fraction of end-diastolic volume pumped out per beat, normally about 55 to 70%. At 25%, forward output is low (fatigue), blood backs up into the lungs (congestion), and compensatory neurohormonal systems activate but ultimately accelerate decline. The other formulas and interpretations are incorrect." },
            { id: "c10", dok: 3, q: "Predict the effect on stroke volume if preload increases (within physiologic range) and explain via the Frank-Starling mechanism.", a: "Higher preload stretches the ventricular walls. Within the working range, sarcomeres reach a more favorable length-tension relationship, and the next contraction is more forceful. Stroke volume rises. This is the Frank-Starling mechanism: the heart pumps out what it receives.", options: ["Stroke volume falls because higher preload over-stretches the ventricle past its working range", "Stroke volume stays exactly the same because the heart auto-regulates to a set value", "Stroke volume rises because higher preload stretches sarcomeres to a more favorable length-tension point, producing a more forceful contraction", "Stroke volume rises because higher preload speeds up the heart rate directly"], correctIndex: 2, explanation: "Within the physiologic range, more filling stretches sarcomeres closer to optimal overlap, increasing contractile force on the next beat. The heart pumps out what it receives (Frank-Starling). Preload does not change heart rate directly, and stroke volume is not auto-fixed to a set point. Over-stretch only matters beyond physiologic range." },
            { id: "c11", dok: 3, q: "A patient develops cardiac tamponade (fluid in the pericardial sac compressing the heart). Predict the effect on filling and stroke volume and explain why.", a: "External compression limits how much the ventricles can expand during diastole, dropping preload. Reduced preload means reduced stroke volume (Frank-Starling reverse). Cardiac output falls. Severe tamponade is rapidly fatal without drainage.", options: ["Filling rises because the fluid pushes blood into the ventricles, raising stroke volume", "External compression limits ventricular expansion, dropping preload and stroke volume by Frank-Starling, so cardiac output falls", "Filling is normal but ejection is blocked, so stroke volume stays the same and cardiac output rises", "Tamponade affects the atria only, leaving stroke volume unchanged"], correctIndex: 1, explanation: "Pericardial fluid squeezes the heart from outside, so the ventricles cannot expand fully during diastole. Lower preload means lower stroke volume (Frank-Starling in reverse), and cardiac output falls. Fluid in the pericardial sac does not push blood into the ventricles, and the effect involves the whole heart, not the atria alone." },
            { id: "c12", dok: 3, q: "Compare the pressures the LV and RV must generate, and explain the structural difference between them.", a: "LV pumps into the systemic circuit (high resistance, ~120 mmHg peak). RV pumps into the pulmonary circuit (low resistance, ~25 mmHg peak). LV wall is thicker (concentric muscle) to generate the higher pressure; RV is thinner and crescent-shaped.", options: ["Both ventricles generate the same pressure and have identical wall thickness", "LV pumps into the high-resistance systemic circuit (about 120 mmHg peak); RV pumps into the low-resistance pulmonary circuit (about 25 mmHg peak), so LV walls are thicker", "RV pumps into the systemic circuit and has thicker walls than the LV", "LV and RV pump in series with identical pressures; thickness reflects chamber size only"], correctIndex: 1, explanation: "The LV generates high pressure for the systemic circuit, while the RV pumps against the low-resistance pulmonary circuit. The LV wall is much thicker to handle higher pressure; RV is thinner and crescent-shaped. They pump in series but at very different pressures, and the LV is the high-pressure side, not the RV." }
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
            { id: "c1", dok: 1, q: "What structure sets the normal heart rate?", a: "The sinoatrial (SA) node.", options: ["The AV node", "The Bundle of His", "The sinoatrial (SA) node", "The Purkinje fibers"], correctIndex: 2, explanation: "The SA node has the fastest intrinsic rate and sets the heart's normal pace (about 60 to 100 bpm). The AV node is a backup pacemaker (about 40 to 60 bpm). The Bundle of His and Purkinje fibers conduct impulses but are slower intrinsic pacemakers used only when higher sites fail." },
            { id: "c2", dok: 1, q: "Where does the AV node sit and what does it do?", a: "Between the atria and ventricles. It delays the impulse so the atria finish emptying before the ventricles contract.", options: ["Inside the right atrium near the SA node; speeds up conduction to the ventricles", "Between the atria and ventricles; it delays the impulse so the atria finish emptying before the ventricles contract", "In the ventricular apex; it generates the heart's main rhythm", "In the interventricular septum; it splits the impulse between right and left ventricles"], correctIndex: 1, explanation: "The AV node sits at the AV junction and slows the impulse so atrial contraction can complete ventricular filling before the ventricles fire. The SA node is in the right atrium, but it speeds up rhythm, not delays it. The septum hosts the bundle branches, not the AV node." },
            { id: "c3", dok: 1, q: "Name the conduction pathway in order from SA node to ventricular myocardium.", a: "SA node → atrial myocardium → AV node → Bundle of His → right and left bundle branches → Purkinje fibers → ventricular myocardium.", options: ["SA node, AV node, Purkinje fibers, Bundle of His, bundle branches, ventricular myocardium", "AV node, SA node, atrial myocardium, Bundle of His, Purkinje fibers, ventricular myocardium", "SA node, atrial myocardium, AV node, Bundle of His, right and left bundle branches, Purkinje fibers, ventricular myocardium", "SA node, atrial myocardium, Bundle of His, AV node, Purkinje fibers, bundle branches, ventricular myocardium"], correctIndex: 2, explanation: "Correct order: SA node fires, depolarizes atrial muscle, reaches AV node (delay), travels down the Bundle of His into right and left bundle branches, spreads via Purkinje fibers to ventricular myocardium. The other orderings rearrange steps so the AV delay or bundle branches come in the wrong place." },
            { id: "c4", dok: 1, q: "Approximately how long is the AV nodal delay?", a: "About 100 milliseconds.", options: ["About 10 milliseconds", "About 100 milliseconds", "About 500 milliseconds", "About 1 second"], correctIndex: 1, explanation: "The AV nodal delay is about 100 ms (one-tenth of a second), long enough for the atria to push the last bit of blood into the ventricles. 10 ms is too short to allow atrial emptying. 500 ms or 1 second would be far longer than a full normal cardiac cycle of contraction." },
            { id: "c5", dok: 2, q: "Why is the AV delay essential for cardiac output?", a: "Without the delay, atria and ventricles would contract simultaneously. The atria would fail to empty into the ventricles, ventricular filling would drop, and stroke volume would collapse.", options: ["Without the delay, atria and ventricles would contract simultaneously, atrial emptying would fail, ventricular filling would drop, and stroke volume would collapse", "Without the delay, the ventricles would beat too fast, raising cardiac output dangerously", "Without the delay, the SA node would lose control of the rhythm to the AV node", "Without the delay, the Purkinje fibers would conduct too slowly to the ventricles"], correctIndex: 0, explanation: "The delay separates atrial and ventricular contraction so the atria can top off ventricular filling before the ventricles squeeze. Without it, the chambers would fire together, filling would drop, and stroke volume would collapse. The other answers misattribute the delay's role to rhythm control or Purkinje conduction speed." },
            { id: "c6", dok: 2, q: "Why does the Purkinje system spread the impulse so quickly through the ventricles?", a: "Coordinated ventricular contraction requires all regions to depolarize nearly simultaneously. Rapid Purkinje conduction makes that possible; slower spread would produce uncoordinated, inefficient ejection.", options: ["Coordinated ventricular contraction requires near-simultaneous depolarization of all regions; rapid Purkinje conduction makes that possible", "Rapid spread keeps the AV node from firing on its own and overriding the SA node", "Fast conduction prevents the atria from contracting too late in the cycle", "Fast Purkinje conduction is needed to delay ventricular contraction relative to the atria"], correctIndex: 0, explanation: "Purkinje fibers conduct very quickly so that the entire ventricular myocardium depolarizes nearly together, producing one strong coordinated squeeze. Slower spread would mean some regions fire out of sync and ejection would be inefficient. Purkinje speed does not control pacemaker hierarchy or atrial timing." },
            { id: "c7", dok: 3, q: "A patient has third-degree (complete) AV block: the atria and ventricles fire independently. Predict the consequences for cardiac output and explain why.", a: "Atria contract on their own rhythm; ventricles fall back to a slower escape rhythm from below the block (40-60 bpm or less). The atrial kick no longer reliably precedes ventricular contraction, dropping stroke volume and cardiac output. Patients typically need a pacemaker.", options: ["Atrial kick is preserved, so cardiac output rises despite the block", "Atria and ventricles fire independently, atrial kick is no longer reliably timed to ventricular filling, ventricular rate falls to an escape rhythm, and stroke volume and cardiac output drop", "The block speeds up ventricular contraction, increasing cardiac output dangerously", "Only the atria are affected; ventricular function is normal"], correctIndex: 1, explanation: "In complete AV block, atria and ventricles fire on separate rhythms. The atrial contribution no longer reliably tops off filling, and ventricles run on a slow escape rhythm (40 to 60 bpm or less). Stroke volume and cardiac output drop, and a pacemaker is typically needed. The block does not speed ventricles up or spare them." },
            { id: "c8", dok: 3, q: "Why is ventricular fibrillation rapidly fatal without intervention?", a: "Chaotic ventricular activity means no coordinated contraction. The ventricles quiver rather than pump. Cardiac output collapses; brain and coronary perfusion fail within minutes.", options: ["Ventricular fibrillation is harmless because the atria still pump effectively", "Chaotic ventricular activity means no coordinated contraction; the ventricles quiver instead of pumping, and cardiac output collapses, ending brain and coronary perfusion within minutes", "Ventricular fibrillation slows the heart so much that organs gradually fail over hours", "Ventricular fibrillation traps blood in the ventricles but maintains some forward output"], correctIndex: 1, explanation: "V-fib is disorganized electrical activity; the ventricles quiver without coordinated squeezing, so no blood is ejected. Cardiac output drops to zero, and the brain and heart lose perfusion within minutes. The atria cannot rescue forward flow, and V-fib is fast and disorganized, not slow." }
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
            { id: "c1", dok: 1, q: "Which vessels are the main site of resistance to flow?", a: "Arterioles.", options: ["Capillaries", "Large arteries", "Venules", "Arterioles"], correctIndex: 3, explanation: "Arterioles have thick smooth muscle layers and small radii; they are the main resistance vessels and the primary site where total peripheral resistance is adjusted. Capillaries are exchange vessels with very thin walls. Large arteries are conducting vessels with low resistance. Venules are low-pressure return vessels." },
            { id: "c2", dok: 1, q: "Write the equation for cardiac output.", a: "Cardiac output = stroke volume × heart rate.", options: ["Cardiac output = blood pressure divided by total peripheral resistance", "Cardiac output = stroke volume times heart rate", "Cardiac output = end-diastolic volume minus end-systolic volume", "Cardiac output = heart rate divided by stroke volume"], correctIndex: 1, explanation: "Cardiac output is the volume of blood the heart pumps per minute: CO = SV times HR. End-diastolic minus end-systolic volume defines stroke volume, not cardiac output. BP divided by resistance is rearranged from BP = CO times TPR but is not the standard formula. Dividing HR by SV is not a real formula." },
            { id: "c3", dok: 1, q: "Why do veins have valves?", a: "Pressure in veins is low, so backflow is a risk, especially against gravity. Valves keep blood moving toward the heart.", options: ["Vein walls are too thick to push blood on their own", "Pressure in veins is low, so backflow is a risk (especially against gravity); valves keep blood moving toward the heart", "Valves let veins generate their own pressure pulses like arteries", "Valves prevent oxygen from leaking out of venous blood"], correctIndex: 1, explanation: "Venous pressure is low and gravity opposes return from the legs, so valves prevent backflow and help blood move toward the heart, especially with skeletal muscle pumping. Vein walls are actually thinner than arterial walls, valves do not generate pulses, and oxygen exchange happens in capillaries, not veins." },
            { id: "c4", dok: 2, q: "Explain how arteriolar vasoconstriction raises blood pressure.", a: "Narrowing the arterioles increases total peripheral resistance. With cardiac output unchanged, raising resistance raises arterial pressure (BP = CO × TPR).", options: ["Vasoconstriction lowers cardiac output, which raises BP indirectly", "Vasoconstriction widens the arterioles, lowering resistance and raising flow", "Narrowing arterioles raises total peripheral resistance; with cardiac output unchanged, higher resistance raises arterial pressure (BP = CO times TPR)", "Vasoconstriction only affects venous pressure, not arterial BP"], correctIndex: 2, explanation: "BP = CO times TPR. Tightening arterioles raises TPR, so with the same cardiac output, arterial pressure rises. Vasoconstriction narrows (not widens) vessels, and it acts on arterial side resistance, not just venous pressure. Cardiac output is not lowered by simple arteriolar narrowing in this scenario." },
            { id: "c5", dok: 3, q: "A patient is dehydrated and presents with low blood pressure and a heart rate of 130. Explain both findings via the baroreflex.", a: "Volume loss drops preload and stroke volume, so cardiac output and arterial pressure fall. Baroreceptors detect the pressure drop and reduce their firing. The brainstem cardiovascular centers respond by raising sympathetic outflow: tachycardia and vasoconstriction try to restore BP. The high HR is the compensation; the still-low BP shows the compensation is incomplete without fluid replacement.", options: ["Volume loss drops preload and stroke volume, BP falls, baroreceptors fire less, and the brainstem boosts sympathetic outflow, producing tachycardia and vasoconstriction; the high HR is compensation, the still-low BP shows it is incomplete", "Dehydration directly slows the heart and lowers BP because there is less blood to move", "Baroreceptors detect high BP and respond by raising HR to dilute it", "Volume loss raises preload and stroke volume, which raises HR through Frank-Starling"], correctIndex: 0, explanation: "Less volume means less preload, lower stroke volume, and falling BP. Baroreceptors detect the drop and fire less, prompting the brainstem to increase sympathetic output, raising HR (tachycardia) and constricting vessels to try to restore BP. The still-low BP shows the compensation cannot fully replace lost volume. Dehydration speeds (not slows) HR through this reflex." }
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
            { id: "c1", dok: 1, q: "Name the four cardinal signs of inflammation.", a: "Redness, heat, swelling, pain (sometimes loss of function is added as a fifth).", options: ["Itching, bruising, numbness, fever", "Redness, heat, swelling, pain", "Pallor, coolness, dryness, weakness", "Bleeding, clotting, scarring, stiffness"], correctIndex: 1, explanation: "The four cardinal signs of inflammation are redness, heat, swelling, and pain (rubor, calor, tumor, dolor). Itching and bruising are not part of the classic tetrad. Pallor and coolness describe poor perfusion, the opposite of inflammation. Bleeding and clotting describe hemostasis, a separate process." },
            { id: "c2", dok: 1, q: "Name two phagocytic cells.", a: "Neutrophil, macrophage.", options: ["Neutrophil and macrophage", "Red blood cell and platelet", "B cell and T cell", "Mast cell and basophil"], correctIndex: 0, explanation: "Neutrophils and macrophages are the two main phagocytes that engulf and digest pathogens. Red blood cells carry oxygen and platelets aid clotting; neither phagocytoses. B and T cells are lymphocytes of adaptive immunity, not phagocytes. Mast cells and basophils release histamine and other mediators rather than phagocytosing." },
            { id: "c3", dok: 1, q: "What is the function of natural killer cells?", a: "They kill virus-infected and tumor cells by inducing apoptosis, without needing prior exposure.", options: ["They produce antibodies against extracellular bacteria", "They kill virus-infected and tumor cells without prior exposure", "They present antigens to helper T cells in lymph nodes", "They release histamine to drive allergic responses"], correctIndex: 1, explanation: "Natural killer cells are innate lymphocytes that induce apoptosis in virus-infected and tumor cells without requiring prior exposure. Antibody production is the job of plasma cells (B cell lineage). Antigen presentation is done by dendritic cells, macrophages, and B cells. Histamine release is the role of mast cells and basophils." },
            { id: "c4", dok: 2, q: "Why does inflammation produce swelling?", a: "Vasodilation and increased capillary permeability let plasma proteins leak into tissue. Water follows osmotically, increasing local fluid volume.", options: ["Lymph vessels constrict, trapping fluid in the tissue", "Red blood cells migrate into tissue and rupture there", "Vasodilation and capillary leak let plasma into tissue, drawing water", "Local cells stop making ATP, so the Na+/K+ pump fails"], correctIndex: 2, explanation: "Inflammation causes vasodilation and increased capillary permeability, letting plasma proteins leak into tissue; water follows osmotically, producing swelling. Lymphatics actually dilate to drain extra fluid, not constrict. Red blood cells do not normally migrate; white cells do. Pump failure is not the mechanism of acute inflammatory edema." },
            { id: "c5", dok: 3, q: "A patient is asplenic (had splenectomy after trauma). Predict the infection risk and explain.", a: "The spleen filters encapsulated bacteria (Streptococcus pneumoniae, Haemophilus influenzae, Neisseria meningitidis) from the blood. Without it, these organisms can cause overwhelming bacteremia. Patients receive vaccines and may need lifelong antibiotic precautions.", options: ["Higher risk of viral hepatitis from loss of liver filtering", "Higher risk of autoimmune disease from loss of self-tolerance", "Higher risk of allergic reactions from loss of mast cell control", "Higher risk of overwhelming infection by encapsulated bacteria"], correctIndex: 3, explanation: "The spleen filters encapsulated bacteria (pneumococcus, H. influenzae, meningococcus) from blood, so asplenic patients face higher risk of overwhelming infection with these organisms. The liver, not the spleen, handles hepatitis defense. The spleen does not set self-tolerance, which is the thymus's job. Mast cells are not regulated by the spleen." }
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
            { id: "c1", dok: 1, q: "Which T cell subset directly kills infected cells?", a: "Cytotoxic (CD8) T cells.", options: ["Helper (CD4) T cells", "Regulatory T cells", "Cytotoxic (CD8) T cells", "Memory B cells"], correctIndex: 2, explanation: "Cytotoxic (CD8) T cells directly kill infected cells by triggering apoptosis. Helper (CD4) T cells coordinate the response but do not kill targets directly. Regulatory T cells dampen immune responses. Memory B cells make antibodies on re-exposure but do not kill cells directly." },
            { id: "c2", dok: 1, q: "What do plasma cells produce?", a: "Antibodies.", options: ["Cytokines", "Antibodies", "Perforin", "Complement proteins"], correctIndex: 1, explanation: "Plasma cells are the antibody factories of the immune system, derived from activated B cells. Cytokines are made by many cell types, especially helper T cells. Perforin is released by cytotoxic T cells and NK cells. Complement proteins are made mainly by the liver." },
            { id: "c3", dok: 1, q: "Which MHC class presents to CD8 T cells?", a: "MHC class I.", options: ["MHC class I", "MHC class II", "MHC class III", "Both MHC class I and II"], correctIndex: 0, explanation: "MHC class I presents endogenous (intracellular) peptides to CD8 cytotoxic T cells. MHC class II presents to CD4 helper T cells. MHC class III refers to genes for complement proteins, not antigen presentation. CD8 cells only read class I." },
            { id: "c4", dok: 1, q: "Which MHC class presents to CD4 T cells?", a: "MHC class II.", options: ["MHC class I", "MHC class II", "MHC class III", "Both MHC class I and II"], correctIndex: 1, explanation: "MHC class II presents exogenous (extracellular) peptides to CD4 helper T cells and is found on professional antigen-presenting cells. Class I presents to CD8 cytotoxic T cells. Class III is a complement gene region, not a presenter. CD4 cells only read class II." },
            { id: "c5", dok: 1, q: "Name three antigen-presenting cell types.", a: "Dendritic cells, macrophages, B cells.", options: ["Neutrophils, eosinophils, basophils", "Plasma cells, mast cells, NK cells", "Dendritic cells, macrophages, B cells", "Red blood cells, platelets, fibroblasts"], correctIndex: 2, explanation: "Dendritic cells, macrophages, and B cells are the three professional antigen-presenting cells that express MHC class II. Granulocytes (neutrophils, eosinophils, basophils) act in innate immunity but do not normally present antigen on MHC II. Plasma cells secrete antibody; mast and NK cells are not APCs. Red cells lack a nucleus and do not present antigen." },
            { id: "c6", dok: 2, q: "Why does the secondary immune response peak faster and higher than the primary?", a: "Memory B and T cells generated during the primary response are pre-expanded and pre-selected for the antigen. On re-exposure they activate without the long naive-cell selection step, producing antibodies and effector T cells far more quickly and in greater numbers.", options: ["Antibodies from the primary response remain in circulation forever", "The pathogen mutates during the secondary response, making it easier to kill", "Memory B and T cells are already expanded and antigen-specific", "Innate immunity is suppressed during the primary response and rebounds in the secondary"], correctIndex: 2, explanation: "The secondary response is fast and large because memory B and T cells generated in the primary response are pre-selected for the antigen and ready to expand quickly. Antibodies do decay over time; it is the memory cells, not residual antibody, that drive the secondary response. The pathogen mutating would make things harder, not easier. Innate immunity is not the reason for the boosted secondary response." },
            { id: "c7", dok: 2, q: "Explain why vaccines work using the concepts of memory and clonal expansion.", a: "Vaccines expose the immune system to a harmless form of an antigen. The body mounts a primary response, generating memory cells. On real infection, the secondary response activates quickly enough to clear the pathogen before it causes disease.", options: ["They give passive immunity by transferring pre-made antibodies", "They expose the immune system to antigen so memory cells form", "They stimulate phagocytes only, without involving lymphocytes", "They permanently alter the genome so cells make antibodies forever"], correctIndex: 1, explanation: "Vaccines present a harmless form of antigen so the immune system mounts a primary response and generates memory cells; on real infection, the secondary response clears the pathogen before disease develops. Passive immunity gives pre-made antibodies and is not how vaccines work. Vaccines activate lymphocytes, not just phagocytes. Vaccines do not alter the genome (mRNA vaccines produce a transient antigen template, not permanent change)." },
            { id: "c8", dok: 2, q: "Predict the immune consequence of HIV destroying CD4 T cells.", a: "Helper T cells coordinate both humoral and cell-mediated responses. Without them, B cell activation and CD8 cytotoxic responses both fail. The patient becomes susceptible to opportunistic infections that intact immunity would normally control.", options: ["Antibody production rises but T cell function is normal", "Both humoral and cell-mediated responses fail, leading to opportunistic infections", "Innate immunity is destroyed but adaptive immunity is preserved", "Only allergic responses are blunted; baseline immunity is intact"], correctIndex: 1, explanation: "CD4 helper T cells coordinate both B cell antibody production and CD8 cytotoxic responses; losing them cripples both arms of adaptive immunity, exposing the patient to opportunistic infections. Antibody responses depend on T cell help, so they also suffer. HIV mainly affects adaptive, not innate, immunity. The failure is not limited to allergic responses." },
            { id: "c9", dok: 3, q: "A transplant recipient receives a kidney from an HLA-mismatched donor. Explain why their immune system attacks the graft.", a: "Donor cells display foreign MHC (HLA) molecules. The recipient's T cells recognize these as non-self and mount an immune response (acute rejection). Immunosuppressive drugs are needed to blunt this response.", options: ["Donor antigens leak into the bloodstream and are toxic", "Recipient T cells recognize donor MHC molecules as foreign", "The kidney releases enzymes that digest recipient tissue", "Recipient antibodies coat the donor kidney and starve it of oxygen"], correctIndex: 1, explanation: "Donor cells display foreign MHC (HLA) molecules that recipient T cells recognize as non-self, triggering acute rejection. The reaction is immunologic, not toxic. The donor organ does not digest recipient tissue. While antibodies can play a role in some rejection types, the dominant mechanism in HLA mismatch is T cell recognition of foreign MHC." },
            { id: "c10", dok: 3, q: "Autoimmune disease: a patient's T cells attack their own thyroid (Hashimoto's). Explain how central tolerance normally prevents this and how it could fail.", a: "In the thymus, developing T cells that bind self-antigen too strongly are normally deleted (negative selection). If a self-reactive clone escapes (or if peripheral tolerance fails later), it can attack self-tissue. In Hashimoto's, T cells and antibodies target thyroid antigens, gradually destroying the gland.", options: ["Self-reactive T cells are normally deleted in the thymus, but some escape", "Self-reactive T cells are normally made in the spleen and the spleen fails", "All T cells start self-reactive and are taught tolerance after infection", "Self-tolerance is purely set by B cells; T cells are never tested"], correctIndex: 0, explanation: "In the thymus, developing T cells that bind self-antigen too strongly are deleted (negative selection); if a self-reactive clone escapes, autoimmunity can result, as in Hashimoto's. The spleen is not where central tolerance occurs. T cells are not all self-reactive at the start; only some are, and those are weeded out. Both T and B cells are tested for self-reactivity." },
            { id: "c11", dok: 3, q: "An infant born with severe combined immunodeficiency (SCID) lacks functional T and B cells. Predict the clinical picture and explain why.", a: "Without B and T cells, the infant has no adaptive immunity. Innate defenses partially compensate but are inadequate against most pathogens. The infant suffers severe and recurrent infections from bacteria, viruses, and fungi, including normally harmless organisms. Without treatment (bone marrow transplant or gene therapy), SCID is usually fatal in the first year.", options: ["Mild seasonal infections only, since innate immunity compensates fully", "Severe, recurrent infections including from normally harmless organisms", "Excessive allergy and autoimmunity from unopposed lymphocyte activity", "Normal infections until adolescence, then sudden immunodeficiency"], correctIndex: 1, explanation: "Without B and T cells, the infant has no adaptive immunity; innate defenses cannot cover the gap, so even ordinarily harmless organisms cause severe, recurrent infections. SCID does not produce excess allergy or autoimmunity, since the responsible lymphocytes are absent. The defect is present from birth and becomes apparent as maternal antibodies wane in the first months." },
            { id: "c12", dok: 3, q: "Compare and contrast active and passive immunity, with one clinical example each.", a: "Active: the patient's own immune system makes antibodies. Examples: natural infection or vaccination. Slow to develop but durable (long memory). Passive: pre-formed antibodies are provided. Examples: maternal IgG across the placenta, or anti-venom injection. Immediate protection but short-lived (no memory cells are made).", options: ["Active gives immediate but short protection; passive gives slow but lasting protection", "Active makes the patient's own antibodies (slow, durable); passive transfers pre-made antibodies (fast, short)", "Active and passive both make memory cells, just on different timelines", "Active is from infection only; passive is from vaccination only"], correctIndex: 1, explanation: "Active immunity is the patient's own antibody response (from infection or vaccination): slow to develop but durable because memory cells form. Passive immunity transfers pre-made antibodies (maternal IgG, anti-venom): immediate but short-lived because no memory is generated. Passive immunity does not create memory cells. Vaccination is active immunity, not passive." }
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
            { id: "c1", dok: 1, q: "What is the primary muscle of inspiration?", a: "The diaphragm.", options: ["The external intercostals", "The diaphragm", "The sternocleidomastoid", "The internal intercostals"], correctIndex: 1, explanation: "The diaphragm is the primary muscle of inspiration, providing about two-thirds of the volume change during quiet breathing. The external intercostals assist by raising the ribs. The sternocleidomastoid is an accessory muscle used only during forced breathing. The internal intercostals help with forced expiration, not inspiration." },
            { id: "c2", dok: 1, q: "Which alveolar cell produces surfactant?", a: "Type II pneumocyte.", options: ["Type I pneumocyte", "Alveolar macrophage", "Type II pneumocyte", "Goblet cell"], correctIndex: 2, explanation: "Type II pneumocytes produce surfactant, the lipid-protein mixture that lowers alveolar surface tension. Type I pneumocytes are the thin cells where gas exchange occurs but do not make surfactant. Alveolar macrophages clear debris and pathogens. Goblet cells produce mucus in the upper airways, not surfactant in the alveoli." },
            { id: "c3", dok: 1, q: "What is the function of surfactant?", a: "Reduces surface tension in alveoli, preventing collapse and easing inflation.", options: ["Reduces surface tension and prevents alveolar collapse", "Increases surface tension to keep alveoli small", "Acts as a barrier to gas exchange across the alveolus", "Stores oxygen for use when ventilation drops"], correctIndex: 0, explanation: "Surfactant reduces surface tension at the air-water interface inside alveoli, preventing collapse and making the lungs easier to inflate. Higher surface tension would collapse alveoli, not stabilize them. Surfactant assists gas exchange by keeping alveoli open, not blocking diffusion. It does not store oxygen." },
            { id: "c4", dok: 1, q: "Which law explains air movement during breathing?", a: "Boyle's law (pressure and volume vary inversely).", options: ["Dalton's law", "Henry's law", "Boyle's law", "Fick's law"], correctIndex: 2, explanation: "Boyle's law states that pressure and volume vary inversely at constant temperature; expanding the thorax lowers alveolar pressure and pulls air in. Dalton's law concerns partial pressures in gas mixtures. Henry's law describes gas solubility in liquids. Fick's law applies to diffusion rate across a membrane, not bulk air movement." },
            { id: "c5", dok: 2, q: "Why is the pleural cavity pressure negative?", a: "Elastic recoil of the lungs pulls inward, while the chest wall pulls outward. The opposing forces create a slight vacuum in the pleural space, keeping the lungs adhered to the chest wall.", options: ["Atmospheric air is constantly pulled into the pleural space", "Lung elastic recoil pulls inward while the chest wall pulls outward", "The diaphragm actively sucks fluid out of the pleural space", "Pleural cells continuously pump gas out of the cavity"], correctIndex: 1, explanation: "Lung elastic recoil pulls inward while the chest wall pulls outward; the opposing forces create a slight negative pressure that keeps the lungs adhered to the chest wall. Atmospheric air entering the pleural space would equalize pressure and collapse the lung (pneumothorax). The diaphragm changes thoracic volume but does not pump pleural fluid. There is no active gas pump in the pleura." },
            { id: "c6", dok: 3, q: "A penetrating chest wound exposes the pleural cavity to atmospheric air (pneumothorax). Predict the effect on the affected lung and explain.", a: "Air enters the pleural space until pressure equalizes with the atmosphere. The negative pressure that was holding the lung expanded is lost. Elastic recoil collapses the lung. Ventilation on the affected side falls dramatically.", options: ["The lung overinflates because outside air pushes it open", "The lung collapses because the negative pleural pressure is lost", "Ventilation improves because more air can reach the alveoli", "Blood flow to the lung increases to compensate for the open chest"], correctIndex: 1, explanation: "When the pleural cavity opens to the atmosphere, pressure equalizes and the negative pressure holding the lung expanded is lost; elastic recoil collapses the lung. Outside air does not push the lung open; it eliminates the gradient that kept it expanded. Ventilation falls dramatically on the affected side. Blood flow does not rescue the collapse; in fact, the body usually shunts blood away from poorly ventilated areas." }
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
            { id: "c1", dok: 1, q: "What is the main form of CO₂ transport in blood?", a: "Bicarbonate (HCO₃⁻), about 70%.", options: ["Dissolved in plasma", "Bound to hemoglobin as carbaminohemoglobin", "Bicarbonate (HCO3-)", "Bound to plasma albumin"], correctIndex: 2, explanation: "About 70% of CO2 travels as bicarbonate (HCO3-), formed by carbonic anhydrase in red blood cells. About 7% dissolves in plasma and about 23% binds hemoglobin as carbaminohemoglobin. Albumin is not a primary CO2 transporter." },
            { id: "c2", dok: 1, q: "How many O₂ molecules can one hemoglobin molecule carry?", a: "Four (one per heme group).", options: ["One", "Two", "Four", "Eight"], correctIndex: 2, explanation: "Each hemoglobin molecule has four heme groups, each able to bind one O2, for a total of four O2 molecules per hemoglobin. One or two would under-count the heme groups. Eight would double-count, perhaps confusing heme groups with subunits." },
            { id: "c3", dok: 1, q: "Where are the central chemoreceptors?", a: "In the medulla oblongata.", options: ["In the carotid bodies", "In the aortic arch", "In the medulla oblongata", "In the alveoli"], correctIndex: 2, explanation: "Central chemoreceptors sit in the medulla oblongata and respond mainly to CSF pH, which reflects arterial CO2. The carotid bodies and aortic arch host peripheral chemoreceptors, which respond mostly to low O2. The alveoli do not contain chemoreceptors." },
            { id: "c4", dok: 1, q: "Which gas is the primary moment-to-moment driver of ventilation?", a: "Carbon dioxide (CO₂, via its effect on CSF pH).", options: ["Oxygen", "Carbon dioxide", "Nitrogen", "Carbon monoxide"], correctIndex: 1, explanation: "Moment-to-moment ventilation is driven mainly by arterial CO2, which alters CSF pH and stimulates central chemoreceptors. Oxygen drives breathing only when it falls quite low, via peripheral chemoreceptors. Nitrogen is inert and does not control ventilation. Carbon monoxide is a toxin, not a normal ventilatory signal." },
            { id: "c5", dok: 2, q: "Explain why exercising muscle gets more oxygen even though arterial O₂ saturation is unchanged.", a: "Exercising muscle is warmer, more acidic, and has higher CO₂ and 2,3-BPG. These shift the O₂-Hb dissociation curve right, so Hb releases more O₂ at any given partial pressure. The Bohr effect delivers more O₂ exactly where it is needed.", options: ["Arterial blood picks up more O2 in the lungs during exercise", "Hemoglobin concentration rises within minutes of exercise", "Plasma can dissolve far more oxygen during exercise", "Local conditions in exercising muscle shift the curve right, releasing more O2"], correctIndex: 3, explanation: "Exercising muscle is warmer, more acidic, and has more CO2 and 2,3-BPG; these shift the O2-Hb curve right, so hemoglobin releases more O2 at the tissues (Bohr effect). Arterial saturation is already near maximum at rest, so it does not rise meaningfully. Hemoglobin concentration does not rapidly change during a workout. Plasma dissolved O2 is a small fraction and does not surge." },
            { id: "c6", dok: 2, q: "Why does carbon monoxide poisoning cause hypoxia even when arterial pO₂ is normal?", a: "CO binds hemoglobin with ~250 times higher affinity than O₂. Hb sites are occupied by CO, leaving few to carry O₂. Total O₂ content of blood plummets, even though dissolved pO₂ may look fine on a blood gas.", options: ["CO binds hemoglobin with high affinity, displacing O2 from binding sites", "CO blocks gas exchange across the alveolar membrane", "CO destroys red blood cells, lowering hemoglobin levels", "CO causes severe vasoconstriction that prevents O2 delivery"], correctIndex: 0, explanation: "Carbon monoxide binds hemoglobin about 250 times more tightly than O2, occupying the sites and slashing oxygen-carrying capacity even when dissolved pO2 is normal. Alveolar gas exchange itself is not blocked. CO does not lyse red cells. Vasoconstriction is not the main mechanism of CO hypoxia." },
            { id: "c7", dok: 2, q: "Explain why patients with severe COPD may be driven to breathe by hypoxia rather than CO₂.", a: "Chronic CO₂ retention desensitizes the central chemoreceptors. The peripheral chemoreceptors, which respond to low O₂, take over as the primary drive. Giving such a patient very high inspired O₂ can blunt that drive and cause hypoventilation.", options: ["Their CO2 chemoreceptors become hypersensitive and overdrive breathing", "Their peripheral chemoreceptors stop working entirely", "Their central chemoreceptors are blunted by chronic CO2, so low O2 takes over as the driver", "Their lungs cannot sense CO2 at all and rely on stretch receptors"], correctIndex: 2, explanation: "Chronic CO2 retention desensitizes central chemoreceptors; peripheral chemoreceptors responding to low O2 become the primary drive. CO2 sensitivity is blunted, not heightened. Peripheral chemoreceptors remain active; in fact, they take over. Stretch receptors regulate breath depth, not the chemical drive." },
            { id: "c8", dok: 2, q: "Predict the effect on arterial pH of acute hyperventilation, and explain via the bicarbonate buffer.", a: "Hyperventilation drives off CO₂. Less CO₂ means the equation H₂O + CO₂ ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻ shifts left, lowering H⁺. Arterial pH rises (respiratory alkalosis).", options: ["pH rises because less CO2 shifts the buffer equation toward less H+", "pH falls because less CO2 means more acid", "pH is unchanged because the kidneys instantly compensate", "pH falls because oxygen levels rise and oxygen is acidic"], correctIndex: 0, explanation: "Hyperventilation blows off CO2, so the bicarbonate buffer equation shifts toward less H+, raising pH (respiratory alkalosis). Less CO2 means less acid, not more. Renal compensation takes hours to days, not instants. Oxygen does not acidify blood." },
            { id: "c9", dok: 3, q: "Climbers ascending to high altitude (3,500 m+) develop hyperventilation, polycythemia, and a right shift in their oxygen-hemoglobin curve over days. Explain each adaptation.", a: "Low atmospheric pO₂ stresses the peripheral chemoreceptors, raising minute ventilation. Persistent hypoxia stimulates renal EPO; the marrow produces more RBCs (polycythemia), increasing oxygen-carrying capacity. Tissue acidosis and elevated 2,3-BPG shift the curve right, unloading more O₂ at the tissues.", options: ["Hyperventilation lowers blood viscosity, polycythemia keeps blood thin, and the curve shift releases more O2", "Hyperventilation produces alkalosis to fight infection, polycythemia hardens cell walls, and a left shift protects the brain", "All three are unrelated coincidences of altitude living", "Hyperventilation raises arterial pO2, polycythemia adds more carriers, and a right shift unloads more O2 at tissues"], correctIndex: 3, explanation: "Low atmospheric pO2 drives peripheral chemoreceptor-mediated hyperventilation, raising alveolar and arterial pO2. Hypoxia stimulates renal EPO, growing red cell mass (polycythemia) and oxygen-carrying capacity. Tissue acidosis and elevated 2,3-BPG shift the curve right, unloading more O2 at tissues. The other options invert mechanisms or deny the connection." },
            { id: "c10", dok: 3, q: "A patient has a pulmonary embolus that blocks blood flow to a portion of one lung. Predict the V/Q ratio in that region and the consequence.", a: "Ventilation continues (air gets to those alveoli) but perfusion drops (Q falls toward zero). V/Q rises sharply (dead-space-like). That alveolar air does not contribute to gas exchange; effective surface area shrinks. Hypoxemia results, often resistant to supplemental oxygen because the problem is perfusion, not diffusion.", options: ["V/Q falls toward zero; the area acts like a shunt", "V/Q stays normal because ventilation matches automatically", "V/Q rises sharply; the area acts like dead space", "V/Q becomes negative because flow reverses"], correctIndex: 2, explanation: "A pulmonary embolus blocks perfusion (Q) while ventilation (V) continues, so V/Q rises sharply and that lung region behaves like dead space, contributing little to gas exchange. A shunt is the opposite (perfusion without ventilation). Compensation does not perfectly restore V/Q. V/Q does not go negative; flow does not reverse." },
            { id: "c11", dok: 3, q: "Explain why a premature infant may develop neonatal respiratory distress syndrome (NRDS), and what surfactant therapy does.", a: "Surfactant production by type II pneumocytes ramps up only in the final weeks of gestation. Without enough surfactant, surface tension keeps alveoli collapsed (atelectasis). Work of breathing soars, gas exchange falters. Exogenous surfactant lowers surface tension, allows alveoli to inflate, and supports gas exchange until endogenous production catches up.", options: ["The fetus has not started breathing in utero, so the lungs are underdeveloped", "The diaphragm is too small to inflate the lungs in a premature infant", "Too little surfactant raises surface tension, alveoli collapse, and gas exchange fails", "Premature infants make too much surfactant and the alveoli overinflate"], correctIndex: 2, explanation: "Surfactant production by type II pneumocytes ramps up only in late gestation; insufficient surfactant raises surface tension, alveoli collapse (atelectasis), work of breathing rises, and gas exchange falters. Exogenous surfactant lowers surface tension. Fetal breathing movements occur in utero. Diaphragm size is not the limiting factor. Too much surfactant is not the problem in NRDS." },
            { id: "c12", dok: 3, q: "A patient's arterial blood gas shows pH 7.30, pCO₂ 60 mmHg, HCO₃⁻ 30 mEq/L. Interpret and explain the underlying physiology.", a: "Acidic pH with high pCO₂ indicates respiratory acidosis. The elevated HCO₃⁻ (above 24) is the renal compensation, retaining bicarbonate to buffer the acid. The pattern suggests chronic CO₂ retention (e.g., COPD): the kidneys have had time to compensate, but pH remains below 7.35, so compensation is incomplete.", options: ["Metabolic alkalosis with respiratory compensation", "Metabolic acidosis with respiratory compensation", "Mixed respiratory and metabolic alkalosis", "Respiratory acidosis with renal compensation (chronic CO2 retention)"], correctIndex: 3, explanation: "Acidic pH with high pCO2 indicates a respiratory acidosis. Elevated HCO3- above 24 reflects renal compensation retaining bicarbonate, a process that takes days, consistent with chronic CO2 retention (e.g., COPD). Compensation is partial because pH is still below 7.35. Metabolic acidosis would show low HCO3-. Alkalosis would show pH above 7.45." }
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
            { id: "c1", dok: 1, q: "Name the three parts of the small intestine in order.", a: "Duodenum, jejunum, ileum.", options: ["Jejunum, ileum, duodenum", "Ileum, duodenum, jejunum", "Duodenum, jejunum, ileum", "Duodenum, ileum, jejunum"], correctIndex: 2, explanation: "From the stomach, chyme enters the duodenum, then the jejunum, then the ileum, which connects to the large intestine. The other orderings shuffle the segments incorrectly. Memorize: D-J-I going downstream." },
            { id: "c2", dok: 1, q: "What is peristalsis?", a: "A wave of smooth muscle contraction that propels content along the GI tract.", options: ["A storage pouch in the stomach that holds chyme", "A wave of smooth muscle contraction that propels content along the tract", "A reflex that triggers vomiting when the gut is irritated", "A localized mixing motion in the small intestine"], correctIndex: 1, explanation: "Peristalsis is the wave of smooth muscle contraction that pushes content forward along the GI tract. A storage pouch describes the stomach itself, not a motility pattern. Vomiting is a protective reflex, not the definition of peristalsis. Localized mixing without forward propulsion is segmentation, a different motility pattern." },
            { id: "c3", dok: 1, q: "Name the four wall layers of the GI tract.", a: "Mucosa, submucosa, muscularis externa, serosa (or adventitia).", options: ["Mucosa, submucosa, muscularis externa, serosa", "Endothelium, intima, media, adventitia", "Epidermis, dermis, hypodermis, fascia", "Cortex, medulla, pelvis, capsule"], correctIndex: 0, explanation: "The GI wall has four layers from lumen outward: mucosa, submucosa, muscularis externa, and serosa (or adventitia where not in the peritoneum). The vascular-style layers (intima, media, adventitia) apply to blood vessels. Epidermis, dermis, hypodermis are skin. Cortex, medulla, pelvis, capsule are kidney layers." },
            { id: "c4", dok: 1, q: "What is the function of the pyloric sphincter?", a: "Regulates passage of chyme from the stomach to the duodenum.", options: ["Controls swallowing from the mouth into the esophagus", "Regulates the passage of chyme from the stomach to the duodenum", "Prevents reflux of intestinal contents into the stomach only", "Controls bile release from the gallbladder"], correctIndex: 1, explanation: "The pyloric sphincter at the stomach-duodenum junction regulates how fast chyme leaves the stomach, allowing the duodenum to handle small portions at a time. Swallowing is controlled by the upper esophageal sphincter. Reflux prevention is the lower esophageal sphincter's job. Bile release is managed by the sphincter of Oddi." },
            { id: "c5", dok: 2, q: "Why is segmentation more important than peristalsis in the small intestine?", a: "Segmentation mixes chyme with digestive enzymes and exposes it to the absorptive surface, maximizing digestion and absorption. Net forward motion is slower, which gives time for these processes.", options: ["Peristalsis is too fast for absorption to keep up", "Segmentation mixes chyme with enzymes and exposes it to the absorptive surface", "The small intestine has no peristalsis at all", "Peristalsis only occurs after a meal is fully digested"], correctIndex: 1, explanation: "Segmentation mixes chyme back and forth with enzymes and exposes it to the absorptive surface, maximizing digestion and absorption; net forward motion is slower so there is time for those processes. Peristalsis does occur in the small intestine, just less prominently than segmentation. Peristalsis is not absent or limited to post-digestion only." },
            { id: "c6", dok: 3, q: "A patient with achalasia cannot relax the lower esophageal sphincter. Predict the symptoms and explain.", a: "Food and liquid accumulate above the unrelaxed sphincter, dilating the lower esophagus. Patients have dysphagia (especially for solids and liquids), regurgitation, chest pain, and weight loss. Aspiration risk rises if regurgitated material reaches the airway.", options: ["Sudden diarrhea and rapid weight gain", "Dysphagia, regurgitation, chest pain, and weight loss", "Severe constipation with no esophageal symptoms", "Hunger without symptoms during meals"], correctIndex: 1, explanation: "Achalasia traps food above an unrelaxed lower esophageal sphincter; patients develop dysphagia, regurgitation, chest pain, and weight loss, with aspiration risk if regurgitated material reaches the airway. Diarrhea and rapid weight gain are not features. Constipation is a colonic issue. Eating triggers symptoms, not relief." }
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
            { id: "c1", dok: 1, q: "Where is most absorption of nutrients accomplished?", a: "In the small intestine.", options: ["The stomach", "The small intestine", "The large intestine", "The esophagus"], correctIndex: 1, explanation: "Most nutrient absorption occurs in the small intestine, where villi and microvilli create a huge surface area. The stomach absorbs only small molecules like alcohol and some drugs. The large intestine mainly absorbs water and electrolytes. The esophagus is a transport tube and does not absorb nutrients." },
            { id: "c2", dok: 1, q: "What does bile do?", a: "Emulsifies fats, breaking them into smaller droplets so pancreatic lipase can access them.", options: ["Breaks proteins into amino acids in the duodenum", "Emulsifies fats into smaller droplets so lipase can work", "Neutralizes stomach acid as it enters the duodenum", "Activates pancreatic enzymes from their inactive forms"], correctIndex: 1, explanation: "Bile emulsifies dietary fats into smaller droplets, increasing surface area so pancreatic lipase can digest them. Protein digestion is done by enzymes like pepsin and trypsin, not bile. Acid neutralization is the job of pancreatic bicarbonate. Enzyme activation in the duodenum is the role of enterokinase and trypsin." },
            { id: "c3", dok: 1, q: "Which enzyme begins protein digestion in the stomach?", a: "Pepsin (from pepsinogen).", options: ["Salivary amylase", "Pepsin", "Trypsin", "Lipase"], correctIndex: 1, explanation: "Pepsin, activated from pepsinogen by stomach acid, begins protein digestion in the stomach. Salivary amylase digests starch, starting in the mouth. Trypsin works in the small intestine, not the stomach. Lipase digests fats, primarily in the small intestine." },
            { id: "c4", dok: 1, q: "Where do absorbed fats first enter (the bloodstream or lymph)?", a: "Lymph (via lacteals in the villi), as chylomicrons.", options: ["Directly into the hepatic portal vein", "Into systemic capillaries within the villus", "Into lymph via lacteals as chylomicrons", "Into the stomach wall before entering circulation"], correctIndex: 2, explanation: "Absorbed dietary fats are packaged as chylomicrons and enter lymph through the lacteals in each villus, bypassing the hepatic portal route. Most other nutrients (sugars, amino acids) take the portal vein. Fats only reach systemic blood after passing through the lymphatic system to the thoracic duct. They do not enter through the stomach wall." },
            { id: "c5", dok: 2, q: "Why do patients with lactose intolerance experience bloating and diarrhea after dairy?", a: "Without lactase, lactose cannot be split to glucose and galactose. Undigested lactose remains in the gut, drawing in water osmotically (diarrhea) and getting fermented by colonic bacteria (gas and bloating).", options: ["Lactose triggers an autoimmune reaction in the intestinal wall", "Undigested lactose pulls water into the gut and is fermented by bacteria", "Lactose damages villi, blocking nutrient absorption entirely", "The pancreas overproduces enzymes when lactose is present"], correctIndex: 1, explanation: "Without lactase, lactose stays in the gut, draws water osmotically (causing diarrhea), and is fermented by colonic bacteria (causing gas and bloating). The reaction is osmotic and microbial, not autoimmune. Villi are not damaged. The pancreas does not overrespond to lactose." },
            { id: "c6", dok: 3, q: "A patient has had their gallbladder removed. Predict the dietary consequence and explain.", a: "Bile is still made by the liver, but it can no longer be concentrated and stored. Continuous low-level bile flow into the duodenum is fine for typical meals, but a large fatty meal exceeds the bile available at that moment. Patients often experience steatorrhea or discomfort after high-fat meals.", options: ["Bile production stops, so all fats are excreted undigested", "Bile is still made by the liver but cannot be concentrated and released in surges", "The liver enlarges and produces ten times more bile to compensate", "Patients can no longer absorb water-soluble vitamins"], correctIndex: 1, explanation: "After cholecystectomy, the liver still makes bile, but it cannot be stored or released in a large bolus; continuous low-level bile flow handles typical meals but may not match a high-fat meal, causing post-meal discomfort or steatorrhea. Bile production does not stop. The liver does not massively over-produce. Water-soluble vitamin absorption does not depend on bile (fat-soluble vitamin absorption may suffer)." }
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
            { id: "c1", dok: 1, q: "What is the functional unit of the kidney?", a: "The nephron.", options: ["The glomerulus", "The nephron", "The renal pyramid", "The collecting duct"], correctIndex: 1, explanation: "The nephron is the functional unit of the kidney, comprising the renal corpuscle and the tubule system that processes filtrate. The glomerulus is part of the nephron, not the whole unit. Renal pyramids are anatomical regions of the medulla. Collecting ducts receive output from many nephrons and are not themselves the unit." },
            { id: "c2", dok: 1, q: "What is the typical glomerular filtration rate (GFR)?", a: "About 125 mL/min (≈180 L/day).", options: ["About 5 mL/min", "About 25 mL/min", "About 125 mL/min", "About 500 mL/min"], correctIndex: 2, explanation: "GFR averages around 125 mL/min, or about 180 L/day filtered. Much lower values would indicate renal failure. 500 mL/min would exceed renal plasma flow in most adults. The 125 mL/min figure is the standard reference." },
            { id: "c3", dok: 1, q: "Which vessel delivers blood to the glomerulus?", a: "The afferent arteriole.", options: ["The efferent arteriole", "The afferent arteriole", "The peritubular capillary", "The vasa recta"], correctIndex: 1, explanation: "The afferent arteriole delivers blood to the glomerulus. The efferent arteriole drains it. Peritubular capillaries surround the tubules for reabsorption. The vasa recta serve the medulla and support the countercurrent system." },
            { id: "c4", dok: 1, q: "Which structures form the filtration slits?", a: "Podocyte foot processes (pedicels).", options: ["Endothelial fenestrations", "Mesangial cell processes", "Podocyte foot processes (pedicels)", "Basement membrane pores"], correctIndex: 2, explanation: "Podocyte foot processes (pedicels) interdigitate to form the filtration slits, bridged by slit diaphragms that exclude proteins. Endothelial fenestrations are in the capillary endothelium, a separate barrier layer. Mesangial cells provide structural support, not slits. The basement membrane is one of the three barriers but does not form the slits." },
            { id: "c5", dok: 2, q: "Explain how the kidney maintains a stable GFR despite changes in blood pressure within the normal range.", a: "Two mechanisms: (1) myogenic response, afferent arteriole constricts when stretched by higher pressure; (2) tubuloglomerular feedback, macula densa senses tubular flow and adjusts afferent arteriole tone via the juxtaglomerular apparatus.", options: ["ADH levels are continuously adjusted to maintain GFR", "The myogenic response and tubuloglomerular feedback adjust afferent arteriole tone", "Renal nerves directly hold GFR constant by varying glomerular pressure", "The bladder reflexively signals the kidney to slow filtration when full"], correctIndex: 1, explanation: "Renal autoregulation uses the myogenic response (afferent arteriole constricts when stretched) and tubuloglomerular feedback (macula densa adjusts afferent tone via the juxtaglomerular apparatus). ADH controls water reabsorption, not GFR. Renal nerves modulate but do not constitute autoregulation. Bladder filling is not a GFR regulator." },
            { id: "c6", dok: 3, q: "Proteinuria in a kidney patient suggests damage where? Explain.", a: "The glomerular filtration barrier (endothelium, basement membrane, or podocytes) normally excludes proteins. Protein in the urine implies barrier dysfunction, most often at the podocyte slit diaphragms or basement membrane (nephrotic-range disease).", options: ["The collecting duct, since that is where ADH acts", "The glomerular filtration barrier (podocytes, basement membrane)", "The loop of Henle, since that creates the medullary gradient", "The renal pelvis, where urine accumulates before drainage"], correctIndex: 1, explanation: "The glomerular filtration barrier normally excludes plasma proteins; proteinuria implies that barrier is damaged, most often at the podocyte slit diaphragms or basement membrane. The collecting duct controls water reabsorption, not protein filtration. The loop of Henle handles osmolarity, not protein. The renal pelvis is a drainage area, not a filter." }
          ]
        },

        {
          id: "t-tubular-function",
          title: "Tubular Function and Urine Concentration",
          summary: "How the tubules reshape the filtrate into a final urine, and how ADH and aldosterone fine-tune it.",
          videoUrl: null,
          notesUrl: null,
          readingUrl: "https://openstax.org/books/anatomy-and-physiology-2e/pages/25-4-physiology-of-urine-formation-tubular-reabsorption-and-secretion",
          lecturePageUrl: "tubular-function.html",
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
            { id: "c1", dok: 1, q: "Which tubule segment reabsorbs the largest fraction of filtered Na⁺ and water?", a: "The proximal convoluted tubule (about 65%).", options: ["The proximal convoluted tubule (about 65%)", "The descending loop of Henle (about 50%)", "The distal convoluted tubule (about 65%)", "The collecting duct (about 80%)"], correctIndex: 0, explanation: "The PCT reabsorbs about 65% of filtered Na+ and water, isosmotically. The descending loop reabsorbs water but not Na+. The DCT handles fine-tuning, not bulk reabsorption. The collecting duct adjusts the final water content under ADH, but only the small remaining fraction." },
            { id: "c2", dok: 1, q: "What is the function of ADH in the collecting duct?", a: "Inserts aquaporin-2 channels into the apical membrane, increasing water reabsorption and producing more concentrated urine.", options: ["Inserts Na+ channels to drive Na+ reabsorption", "Inserts aquaporin-2 channels to increase water reabsorption", "Blocks Na+ channels to allow more water excretion", "Inserts urea transporters in the loop of Henle"], correctIndex: 1, explanation: "ADH increases collecting duct water reabsorption by inserting aquaporin-2 water channels into the apical membrane of principal cells, concentrating urine. Aldosterone, not ADH, regulates ENaC sodium channels. ADH does not block Na+ channels. While urea recycling matters for the medullary gradient, that is not ADH's defining action." },
            { id: "c3", dok: 1, q: "Where does aldosterone act in the nephron?", a: "Principal cells of the late distal tubule and collecting duct.", options: ["Proximal convoluted tubule cells", "Thick ascending limb cells", "Principal cells of the late distal tubule and collecting duct", "Glomerular podocytes"], correctIndex: 2, explanation: "Aldosterone acts on principal cells in the late distal tubule and collecting duct to increase Na+ reabsorption and K+ secretion. The PCT does most bulk reabsorption but is not the aldosterone target. The thick ascending limb uses NKCC2, not aldosterone. Podocytes are filtration cells, not hormone targets here." },
            { id: "c4", dok: 1, q: "Which limb of the loop of Henle is impermeable to water?", a: "The thick ascending limb.", options: ["The descending limb", "The thin ascending limb only", "The thick ascending limb", "The hairpin tip"], correctIndex: 2, explanation: "The thick ascending limb is impermeable to water but actively pumps out Na+, K+, Cl-, diluting the tubular fluid and contributing to the medullary gradient. The descending limb is permeable to water and impermeable to solute. The thin ascending limb is permeable to solute movement. The hairpin tip is part of the descending segment." },
            { id: "c5", dok: 1, q: "What is the role of the countercurrent multiplier?", a: "Establishes a hypertonic medullary interstitium that allows the collecting duct to concentrate urine when ADH is present.", options: ["Establishes a hypertonic medullary interstitium to allow concentrated urine", "Filters proteins out of the blood at the glomerulus", "Pumps urea directly into the bladder", "Triggers ADH release from the kidney"], correctIndex: 0, explanation: "The countercurrent multiplier in the loop of Henle establishes the hypertonic medullary interstitium that lets the collecting duct concentrate urine when ADH inserts aquaporin-2 channels. Protein exclusion happens at the glomerular barrier. The loop does not pump urea to the bladder. ADH is released from the posterior pituitary, not the kidney." },
            { id: "c6", dok: 2, q: "Explain why diabetes insipidus (lack of ADH or ADH resistance) causes large volumes of dilute urine.", a: "Without ADH action, aquaporin-2 channels are not inserted in the collecting duct. Water cannot be reabsorbed there. Filtrate exits as a large volume of very dilute urine.", options: ["Without ADH, aquaporin-2 is not inserted and water cannot be reabsorbed in the collecting duct", "Without ADH, Na+ reabsorption fails and salt is lost in urine", "Without ADH, the glomerulus cannot filter properly", "Without ADH, aldosterone is overproduced and forces water out"], correctIndex: 0, explanation: "Diabetes insipidus lacks ADH action; without aquaporin-2 channels, the collecting duct cannot reabsorb water, so a large volume of dilute urine is excreted. ADH targets water, not Na+ reabsorption. The glomerulus is not the affected site. Aldosterone is regulated separately and does not flip into overdrive in DI." },
            { id: "c7", dok: 2, q: "Loop diuretics (furosemide) block the NKCC2 cotransporter in the thick ascending limb. Predict the effect on urine output and explain.", a: "Without NKCC2, Na⁺, K⁺, and Cl⁻ stay in the lumen. The medullary gradient that drives water reabsorption collapses. Water and these electrolytes are excreted in large amounts: a strong diuresis with potential hypokalemia.", options: ["Strong diuresis with risk of hypokalemia", "Severe water retention with rising urine output blocked", "Mild diuresis with rising serum K+", "No change in urine output but acidosis develops"], correctIndex: 0, explanation: "Loop diuretics block NKCC2 in the thick ascending limb; Na+, K+, and Cl- stay in the lumen, the medullary gradient collapses, and large volumes of urine with electrolyte loss are excreted, including K+ (hence hypokalemia risk). Water retention is the opposite of what happens. K+ is lost, not gained. Urine output rises sharply, not stays steady." },
            { id: "c8", dok: 2, q: "Spironolactone blocks the aldosterone receptor. Predict the effect on serum K⁺.", a: "Without aldosterone action, principal cells reabsorb less Na⁺ and secrete less K⁺. Less K⁺ is lost in urine, so serum K⁺ rises (hyperkalemia risk). Hence 'potassium-sparing' diuretic.", options: ["Serum K+ falls because aldosterone normally retains K+", "Serum K+ rises because aldosterone normally drives K+ secretion in urine", "Serum K+ is unchanged because aldosterone only acts on Na+", "Serum Na+ rises but K+ does not change"], correctIndex: 1, explanation: "Aldosterone normally promotes K+ secretion by principal cells, so blocking the receptor reduces K+ loss in urine, raising serum K+ (hyperkalemia risk, hence 'potassium-sparing'). Aldosterone drives K+ out, not retains it. The hormone affects both Na+ and K+ handling, not Na+ alone. Sodium reabsorption decreases too." },
            { id: "c9", dok: 3, q: "A patient is severely dehydrated after marathon running in the heat. Predict their plasma ADH and aldosterone levels and the urine they produce, with reasoning.", a: "Volume loss and rising plasma osmolarity trigger both ADH (osmoreceptors and baroreceptors) and aldosterone (RAAS activation from low renal perfusion and angiotensin II). Both hormones rise. Urine becomes scant, concentrated, and low in Na⁺.", options: ["Low ADH and low aldosterone; dilute urine high in Na+", "High ADH and high aldosterone; scant concentrated urine low in Na+", "High ADH and low aldosterone; large volume of concentrated urine", "Low ADH and high aldosterone; scant dilute urine"], correctIndex: 1, explanation: "Dehydration and rising plasma osmolarity stimulate ADH; volume loss activates RAAS and aldosterone. Both hormones rise, producing scant concentrated urine that is also Na+ poor (because aldosterone retains Na+). The opposite pattern would worsen dehydration. The mixed patterns are internally inconsistent with the physiology of volume loss." },
            { id: "c10", dok: 3, q: "Explain how the countercurrent multiplier and ADH cooperate to produce maximally concentrated urine.", a: "The countercurrent multiplier in the loop of Henle creates a hypertonic medulla. When ADH inserts aquaporin-2 into the collecting duct, water flows from the duct lumen into the hypertonic interstitium until osmotic equilibrium. Without the gradient, ADH would have nowhere to send the water; without ADH, the gradient is irrelevant. Both are required.", options: ["Either alone is enough; they work as backups", "ADH first creates a gradient, then the loop concentrates urine", "The loop creates a hypertonic medulla; ADH lets water exit the duct into that medulla", "Both act only in the proximal convoluted tubule"], correctIndex: 2, explanation: "The countercurrent multiplier in the loop builds a hypertonic medullary interstitium; ADH then opens aquaporin-2 in the collecting duct so water flows out of the duct lumen into the hypertonic medulla. Without the gradient ADH has nowhere to send the water; without ADH the gradient is unused. The loop builds the gradient, not ADH. Neither acts mainly in the PCT for urine concentration." },
            { id: "c11", dok: 3, q: "A patient with Conn syndrome (primary hyperaldosteronism) has high BP and low K⁺. Tie both findings to aldosterone's actions.", a: "Excess aldosterone drives renal Na⁺ reabsorption; water follows osmotically, expanding plasma volume and raising BP. Excess aldosterone also drives K⁺ secretion at the principal cells, lowering serum K⁺. The combination of hypertension with hypokalemia is the clinical fingerprint.", options: ["Aldosterone retains Na+ (raising BP) and drives K+ out (lowering serum K+)", "Aldosterone wastes Na+ (lowering BP) and retains K+ (raising serum K+)", "Aldosterone raises BP by direct vasoconstriction only; K+ effect is unrelated", "Aldosterone has no direct effect on BP; the findings come from another hormone"], correctIndex: 0, explanation: "Excess aldosterone drives renal Na+ reabsorption with water following, expanding plasma volume and raising BP; it also drives K+ secretion, lowering serum K+. The combination is the clinical fingerprint of Conn syndrome. The opposite pattern would not match the syndrome. Vasoconstriction is not aldosterone's main route to BP." },
            { id: "c12", dok: 3, q: "Compare the urine of a patient given desmopressin (synthetic ADH) with that of a patient given furosemide. Explain mechanistically.", a: "Desmopressin: more aquaporin-2 in the collecting duct → water reabsorption rises → urine volume small, concentration high. Furosemide: NKCC2 blocked → medullary gradient collapses → water cannot be reabsorbed → urine volume large, dilute, with substantial salt loss.", options: ["Both produce small, concentrated urine but by different routes", "Desmopressin gives small concentrated urine; furosemide gives large dilute urine with salt loss", "Both produce large dilute urine; only the side effects differ", "Desmopressin gives large dilute urine; furosemide gives small concentrated urine"], correctIndex: 1, explanation: "Desmopressin mimics ADH, inserting aquaporin-2 in the collecting duct so water is reabsorbed: small volume, concentrated urine. Furosemide blocks NKCC2 in the thick ascending limb, collapsing the medullary gradient and producing a large volume of dilute urine with substantial salt loss. The other patterns invert one or both mechanisms." }
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
            { id: "c1", dok: 1, q: "What is the normal arterial pH range?", a: "7.35-7.45.", options: ["6.95-7.05", "7.15-7.25", "7.35-7.45", "7.55-7.65"], correctIndex: 2, explanation: "Normal arterial pH is 7.35-7.45. Below 7.35 is acidemia; above 7.45 is alkalemia. The other ranges are well outside survivable physiology without immediate intervention." },
            { id: "c2", dok: 1, q: "Which compartment holds the most water?", a: "Intracellular fluid (about two-thirds of total body water).", options: ["Intracellular fluid", "Interstitial fluid", "Plasma", "Transcellular fluid"], correctIndex: 0, explanation: "Intracellular fluid holds about two-thirds of total body water. Interstitial fluid and plasma together make up the extracellular fluid, the remaining one-third. Transcellular fluid (CSF, joint fluid, etc.) is a small specialized fraction." },
            { id: "c3", dok: 1, q: "Which cation dominates the ECF?", a: "Sodium.", options: ["Potassium", "Sodium", "Calcium", "Magnesium"], correctIndex: 1, explanation: "Sodium (Na+) is the dominant cation in the extracellular fluid and is the main determinant of ECF osmolarity. Potassium is the dominant ICF cation. Ca2+ and Mg2+ are present but at much lower concentrations than Na+ in ECF." },
            { id: "c4", dok: 1, q: "Which cation dominates the ICF?", a: "Potassium.", options: ["Sodium", "Potassium", "Calcium", "Chloride"], correctIndex: 1, explanation: "Potassium (K+) is the dominant cation in the ICF, maintained by the Na+/K+ ATPase. Sodium dominates the ECF. Ca2+ is mostly stored in the ER/SR or bone; cytosolic Ca2+ is very low. Chloride is an anion, not a cation." },
            { id: "c5", dok: 2, q: "Why does severe vomiting cause metabolic alkalosis?", a: "Vomiting loses gastric H⁺ (HCl). The body has lost acid, so the remaining HCO₃⁻ pushes pH up. Plasma bicarbonate rises, pH rises (alkalosis). Volume loss compounds the picture by triggering aldosterone, which further drives renal acid loss.", options: ["Vomiting loses HCO3-, so the remaining acid drops pH", "Vomiting loses gastric H+, leaving HCO3- to drive pH up", "Vomiting causes CO2 retention and raises pH", "Vomiting has no acid-base effect; it just causes dehydration"], correctIndex: 1, explanation: "Vomiting loses stomach H+ (HCl), so the remaining bicarbonate pushes pH up (metabolic alkalosis). HCO3- is not lost in vomit; gastric secretions are acidic. CO2 changes are not the direct mechanism. Volume loss does compound things via aldosterone, but the primary acid-base effect is real." },
            { id: "c6", dok: 3, q: "A diabetic patient in DKA has pH 7.20, HCO₃⁻ 12 mEq/L, pCO₂ 25 mmHg. Interpret and explain each value.", a: "Acidic pH with low HCO₃⁻ = metabolic acidosis. The HCO₃⁻ has been consumed buffering ketoacids. The low pCO₂ is the respiratory compensation: the patient is hyperventilating (Kussmaul breathing) to blow off CO₂ and bring pH back toward normal. The compensation is partial since pH remains below 7.35.", options: ["Respiratory acidosis with renal compensation", "Metabolic acidosis with respiratory compensation", "Metabolic alkalosis with respiratory compensation", "Respiratory alkalosis without compensation"], correctIndex: 1, explanation: "Acidic pH with low HCO3- indicates metabolic acidosis; HCO3- has been consumed buffering ketoacids. The low pCO2 reflects Kussmaul hyperventilation, the respiratory compensation. Because pH remains below 7.35, the compensation is partial. The other interpretations conflict with the actual numbers." }
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
            { id: "c1", dok: 1, q: "Which cells produce testosterone?", a: "Leydig (interstitial) cells of the testis.", options: ["Sertoli cells", "Leydig (interstitial) cells", "Spermatogonia", "Cells of the prostate"], correctIndex: 1, explanation: "Leydig cells, between the seminiferous tubules, produce testosterone in response to LH. Sertoli cells support sperm development under FSH but do not make testosterone. Spermatogonia are the germ cells that become sperm. Prostate cells contribute to seminal fluid, not androgen synthesis." },
            { id: "c2", dok: 1, q: "Which cells support developing sperm?", a: "Sertoli cells (in the seminiferous tubule).", options: ["Leydig cells", "Spermatogonia", "Sertoli cells", "Cells of the epididymis"], correctIndex: 2, explanation: "Sertoli cells line the seminiferous tubules and nurse developing sperm, also forming the blood-testis barrier. Leydig cells make testosterone but do not directly support sperm. Spermatogonia are the germ cells, not support cells. The epididymis is where sperm mature after leaving the testis, not the site of support during spermatogenesis." },
            { id: "c3", dok: 1, q: "Where do sperm mature?", a: "The epididymis.", options: ["The epididymis", "The seminiferous tubules", "The vas deferens", "The prostate"], correctIndex: 0, explanation: "Sperm leave the seminiferous tubules immature and finish maturing (gaining motility) in the epididymis. The seminiferous tubules are where spermatogenesis happens, not maturation. The vas deferens transports mature sperm. The prostate adds fluid to semen but is not the maturation site." },
            { id: "c4", dok: 1, q: "Which pituitary hormone drives testosterone production?", a: "Luteinizing hormone (LH).", options: ["Follicle-stimulating hormone (FSH)", "Prolactin", "Growth hormone", "Luteinizing hormone (LH)"], correctIndex: 3, explanation: "LH stimulates Leydig cells to produce testosterone. FSH acts on Sertoli cells to support spermatogenesis. Prolactin's main male role is unclear physiologically and is not a primary driver of testosterone. Growth hormone supports general growth, not gonadal steroidogenesis as a primary driver." },
            { id: "c5", dok: 2, q: "Why do anabolic steroid abusers often develop infertility and testicular atrophy?", a: "Exogenous androgens feed back negatively on the hypothalamus and pituitary, suppressing GnRH, LH, and FSH. Without LH and FSH, the testes lose their drive to make testosterone and to spermatogenesis. The testes shrink and sperm counts plummet, often persisting after the drugs stop.", options: ["Steroids directly damage the testes by toxic effect", "Steroids accelerate sperm production until the supply runs out", "Steroids suppress GnRH, LH, and FSH, so the testes lose their drive", "Steroids increase only estrogen and have no LH/FSH effect"], correctIndex: 2, explanation: "Exogenous androgens feed back negatively on the hypothalamus and pituitary, suppressing GnRH, LH, and FSH; without LH the Leydig cells idle and without FSH spermatogenesis fails, so testes shrink and sperm counts plummet. The damage is from feedback suppression, not direct toxicity. Sperm production is suppressed, not accelerated. LH and FSH are clearly affected." },
            { id: "c6", dok: 3, q: "A patient cannot make GnRH. Predict the cascade of hormonal and reproductive findings.", a: "No GnRH → no LH or FSH → no testosterone (Leydig idle) and no spermatogenesis (Sertoli unsupported). The patient presents with low testosterone (delayed puberty if congenital, hypogonadism if acquired), small testes, and infertility. Treatment requires replacing the missing hypothalamic signal or its downstream products.", options: ["High testosterone, large testes, infertility", "Normal testosterone, normal testes, infertility", "High estrogen, normal testes, normal fertility", "Low testosterone, small testes, infertility"], correctIndex: 3, explanation: "No GnRH means no LH or FSH, so Leydig cells idle (low testosterone) and Sertoli cells lose support (failed spermatogenesis). The result is low testosterone, small testes, and infertility, classic hypogonadotropic hypogonadism. High testosterone with large testes would be the opposite. Normal testes with normal hormone levels would not match the deficit." }
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
            { id: "c1", dok: 1, q: "What triggers ovulation?", a: "The LH surge mid-cycle.", options: ["The FSH surge mid-cycle", "The LH surge mid-cycle", "The progesterone surge at day 14", "The estrogen drop just before day 14"], correctIndex: 1, explanation: "Mid-cycle, sustained high estrogen triggers a sharp LH surge from the pituitary, and that LH surge ruptures the dominant follicle (ovulation). FSH rises modestly mid-cycle but does not trigger ovulation. Progesterone rises after ovulation, not before. Estrogen rises into ovulation, then drops briefly." },
            { id: "c2", dok: 1, q: "What does the corpus luteum produce?", a: "Mostly progesterone (and some estrogen).", options: ["Mostly estrogen", "Mostly progesterone (and some estrogen)", "Mostly LH and FSH", "Mostly hCG"], correctIndex: 1, explanation: "The corpus luteum is the post-ovulatory follicle remnant; it produces mainly progesterone (with some estrogen) to maintain the endometrium. The pre-ovulatory follicle makes mostly estrogen. LH and FSH come from the pituitary, not the ovary. hCG is made by trophoblast tissue if pregnancy occurs, not by the corpus luteum itself." },
            { id: "c3", dok: 1, q: "Which phase of the uterine cycle features endometrial shedding?", a: "Menstrual phase.", options: ["Proliferative phase", "Secretory phase", "Menstrual phase", "Ovulatory phase"], correctIndex: 2, explanation: "The menstrual phase is when the functional endometrial layer sloughs off following the corpus luteum's regression and progesterone withdrawal. The proliferative phase rebuilds the endometrium under estrogen. The secretory phase prepares it for implantation under progesterone. Ovulation is a single event, not a shedding phase." },
            { id: "c4", dok: 1, q: "Which hormone primarily rebuilds the endometrium during the proliferative phase?", a: "Estrogen.", options: ["Progesterone", "Estrogen", "FSH", "LH"], correctIndex: 1, explanation: "Estrogen from the developing follicles rebuilds the endometrial lining during the proliferative phase. Progesterone supports the secretory phase. FSH and LH act on the ovary, not directly on the endometrium for rebuilding." },
            { id: "c5", dok: 2, q: "Explain why estrogen switches from negative to positive feedback mid-cycle.", a: "When estrogen rises above a threshold and stays elevated, pituitary sensitivity to GnRH changes. The pituitary responds with the LH surge instead of suppression, driving ovulation. After ovulation, the corpus luteum's progesterone restores negative feedback.", options: ["Estrogen always inhibits the pituitary; the surge comes from FSH instead", "Sustained high estrogen flips the pituitary response from suppression to a surge of LH", "Estrogen never feeds back; the LH surge is purely random timing", "Progesterone causes the LH surge, not estrogen"], correctIndex: 1, explanation: "When estrogen rises above a threshold and stays elevated, the pituitary response flips from negative to positive feedback, producing the LH surge that triggers ovulation. After ovulation, progesterone restores negative feedback. The other options deny or misattribute the surge." },
            { id: "c6", dok: 3, q: "Combined oral contraceptives suppress the LH surge. Explain mechanistically.", a: "Exogenous estrogen and progesterone maintain steady (artificially elevated) plasma hormone levels. Continuous negative feedback suppresses GnRH and gonadotropin release. Without the natural mid-cycle rise in estrogen, the positive-feedback switch does not occur, the LH surge is blunted, and ovulation is prevented.", options: ["They mimic pregnancy so the LH surge never occurs", "They poison the ovary so follicles cannot develop", "They constantly raise FSH so all follicles release at once", "They block all GnRH receptors permanently"], correctIndex: 0, explanation: "Combined oral contraceptives keep estrogen and progesterone steadily elevated, maintaining continuous negative feedback on the hypothalamus and pituitary; the natural mid-cycle estrogen rise that flips feedback to positive does not occur, the LH surge is blunted, and ovulation is prevented. They do not damage the ovary. They suppress, not amplify, FSH. The block on GnRH is reversible and pharmacological, not permanent receptor destruction." }
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
            { id: "c1", dok: 1, q: "Where does fertilization typically occur?", a: "In the ampulla of the uterine (fallopian) tube.", options: ["In the uterus, just before implantation", "In the ampulla of the uterine (fallopian) tube", "In the cervix as sperm enter", "In the ovary, immediately at ovulation"], correctIndex: 1, explanation: "Fertilization typically happens in the ampulla, the widest part of the uterine tube, where sperm meet the ovulated egg. The uterus is where the embryo implants days later, not where sperm meet egg. The cervix is the entry point but not the site of fertilization. The egg leaves the ovary at ovulation but fertilization occurs in the tube." },
            { id: "c2", dok: 1, q: "What does hCG do in early pregnancy?", a: "Maintains the corpus luteum so it continues producing progesterone until the placenta takes over.", options: ["Triggers ovulation in the early cycle", "Maintains the corpus luteum so it continues producing progesterone", "Suppresses the endometrium to allow implantation", "Blocks LH release from the pituitary"], correctIndex: 1, explanation: "hCG from the trophoblast keeps the corpus luteum alive past its normal lifespan, so it continues making progesterone until the placenta takes over by the end of the first trimester. hCG does not trigger ovulation in pregnancy. It supports, rather than suppresses, the endometrium indirectly via progesterone. It does not act primarily by blocking LH." },
            { id: "c3", dok: 1, q: "When does implantation occur after fertilization?", a: "Around day 6-7.", options: ["Day 1-2", "Day 6-7", "Day 12-14", "Day 20-25"], correctIndex: 1, explanation: "Implantation usually occurs around day 6-7 after fertilization, when the blastocyst reaches the uterus and burrows into the endometrium. Day 1-2 is too soon; the zygote is still in the tube. Day 12-14 would be too late for normal implantation. Day 20-25 is well past the implantation window." },
            { id: "c4", dok: 1, q: "When does the placenta take over hormone production from the corpus luteum?", a: "By the end of the first trimester.", options: ["By the end of the first trimester", "By the start of the second month", "By the end of the second trimester", "By the time of delivery"], correctIndex: 0, explanation: "The placenta becomes the dominant source of progesterone and estrogen by the end of the first trimester; before that, the corpus luteum maintains the pregnancy. The handover is not as early as the second month. Waiting until the second trimester or term would risk pregnancy loss if the corpus luteum fades first." },
            { id: "c5", dok: 2, q: "Why does maternal blood volume rise during pregnancy?", a: "To supply the growing placenta and fetus, support increased renal filtration, and provide a reserve for blood loss at delivery. Plasma volume rises more than red cell mass, producing the physiologic anemia of pregnancy.", options: ["To supply the placenta and fetus and buffer blood loss at delivery", "To dilute toxins that the fetus produces", "To replace red blood cells the fetus uses up daily", "To raise blood pressure so the fetus stays warm"], correctIndex: 0, explanation: "Maternal blood volume rises to perfuse the placenta and fetus, support higher renal filtration, and provide reserve for the blood loss expected at delivery. Plasma volume rises more than red cell mass, producing physiologic anemia. The fetus does not produce toxins requiring dilution. The fetus does not consume maternal red cells. The volume rise is not for warming." },
            { id: "c6", dok: 2, q: "Explain why home pregnancy tests target hCG rather than other hormones.", a: "Only trophoblast tissue makes hCG, and levels rise quickly after implantation. It is specific to pregnancy and detectable in urine within days of a missed period.", options: ["hCG is the only hormone that crosses into urine", "Only trophoblast tissue makes hCG, so its presence is specific to pregnancy", "hCG is detectable even before fertilization, giving early warning", "hCG is identical to LH, so any urine LH test would also work"], correctIndex: 1, explanation: "hCG is made by trophoblast tissue, so its presence in maternal urine is specific to pregnancy; levels rise rapidly after implantation and are detectable within days of a missed period. Other hormones can also reach urine, so specificity matters more than presence alone. hCG appears only after implantation, not before fertilization. hCG and LH share a subunit but differ enough that tests target the unique beta subunit." },
            { id: "c7", dok: 3, q: "A third-trimester patient becomes dizzy when lying flat on her back. Predict the cause and the management.", a: "The enlarged uterus compresses the inferior vena cava when supine, dropping venous return, stroke volume, and blood pressure. Roll the patient to her left side to relieve the compression.", options: ["The fetus is in distress; deliver immediately", "The uterus is compressing the inferior vena cava; roll to the left side", "The patient is dehydrated; give oral fluids and continue lying flat", "Blood pressure is too high; recheck supine in 10 minutes"], correctIndex: 1, explanation: "In late pregnancy, supine positioning lets the enlarged uterus compress the inferior vena cava, dropping venous return, stroke volume, and blood pressure (supine hypotensive syndrome). Rolling the patient onto her left side relieves the compression. Immediate delivery is not indicated. Lying flat would worsen the problem. The issue is low BP from venous return, not hypertension." }
          ]
        }

      ]
    }

  ]
};
