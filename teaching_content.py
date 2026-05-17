"""
BIO 304 Teaching Guide Content

Per topic, the three sections that go into the per-module PDFs:
  science      - The substantive content to teach. Not just notes; the teacher's
                 framing of what to say in the video and what depth to reach.
  teaching     - dict with four keys: before_video, misconceptions, order, self_test
  clinical     - Why this matters for the student and their future patients.

Edit the strings here; the builder script regenerates PDFs from this file.
"""

TEACHING = {

    # ============================================================
    # MODULE 1: FOUNDATIONS
    # ============================================================

    "t-levels-of-organization": {
        "science": (
            "The hierarchy is a scaffold, not a list. The point is that every level builds on the one below "
            "and that function emerges as complexity rises. A single sodium atom does nothing interesting. "
            "Pack billions of them into the right gradient across a membrane and you get an action potential. "
            "Pack action potentials into the right wiring and you get a thought. The lesson is that biology "
            "lives in the relationships between parts, not in the parts themselves."
            "\n\n"
            "Anchor the eleven organ systems by what they do. Integumentary protects. Skeletal supports. "
            "Muscular moves. Nervous and endocrine communicate (one fast, one slow). Cardiovascular and "
            "lymphatic transport. Respiratory and digestive bring in oxygen and nutrients; urinary and "
            "respiratory remove waste. Reproductive perpetuates. Students who can recite eleven systems "
            "but cannot say what each is FOR will not retain the rest of the course."
            "\n\n"
            "Drop in two specific examples to make emergence concrete: cardiac contraction depends on "
            "intercalated discs (cell-level structure) creating a functional syncytium (tissue-level "
            "behavior) producing coordinated ejection (organ-level function). And gas exchange depends "
            "on the alveolar wall being one cell thick (cellular) so that diffusion distance is minimal "
            "(tissue), so that gas exchange is fast enough (organ) to support whole-body metabolism."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw the six levels as nested boxes and write one example per level "
                "from a body part of their choosing (heart, skin, etc.). They have to commit before the "
                "video gives them the answer."
            ),
            "misconceptions": [
                "Students confuse 'organ system' with 'organ.' The kidney is an organ; the urinary "
                "system is the kidney plus ureters, bladder, urethra.",
                "Students think the levels are a one-time list to memorize. They are a recurring "
                "framework you will reach for throughout the entire course.",
                "Cells are often pictured as identical building blocks. Emphasize that there are "
                "hundreds of cell types, each shaped for its job."
            ],
            "order": (
                "Levels first (hierarchy), then organ systems (with one-sentence functions), then "
                "emergence (with two concrete examples). Do not start with the organ system list. "
                "The hierarchy is the load-bearing concept."
            ),
            "self_test": [
                "Without notes, list the six levels of organization in order.",
                "Pick three organ systems and write one sentence describing each one's job.",
                "Explain what 'emergent property' means using your own example."
            ]
        },
        "clinical": (
            "When your patient has a problem, you must locate it at the right level. A drug works at "
            "the chemical or cellular level but the patient experiences it at the organism level. "
            "Treatment-resistant hypertension might be a chemical problem (a receptor mutation), a "
            "cellular problem (renal cells malfunctioning), an organ problem (kidney damage), or a "
            "system problem (RAAS dysregulation). Each level demands a different intervention. Nurses "
            "who can move fluently between levels catch things others miss: the patient whose 'fatigue' "
            "turns out to be cellular (mitochondrial dysfunction from a statin) rather than psychological."
        )
    },

    "t-anatomical-terminology": {
        "science": (
            "Anatomical position is the reference frame. Every directional term, every plane, every "
            "regional name assumes the patient is standing in this position. If your patient is lying "
            "face down on the OR table, the surgeon does not say 'the kidney is above the bladder' "
            "from the patient's current orientation. They say 'superior to the bladder' from "
            "anatomical position. This consistency is the entire point."
            "\n\n"
            "Teach the directional terms as pairs, because they are always relative: superior versus "
            "inferior, medial versus lateral, proximal versus distal. Distal and proximal only make "
            "sense relative to an origin (usually the trunk for limbs). The wrist is distal to the "
            "elbow but proximal to the fingers. Students who chant directional terms in isolation "
            "miss this."
            "\n\n"
            "The three planes and the body cavities give you the vocabulary to describe any imaging "
            "study. A transverse CT slice through the abdomen will show kidneys, vertebra, and large "
            "vessels in cross-section. A sagittal MRI of the brain will show the corpus callosum "
            "lengthwise. The nine abdominal regions are more precise than the four quadrants and worth "
            "the small extra investment."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a stick figure in anatomical position and label as many "
                "directional pairs as they can. Then have them draw a transverse, sagittal, and "
                "frontal section through the figure."
            ),
            "misconceptions": [
                "Students forget that anatomical position is a fixed reference and try to update "
                "terms when the patient moves.",
                "Confusion between dorsal/ventral and posterior/anterior. They are synonyms in humans; "
                "in four-legged animals they differ.",
                "Students think 'midsagittal' and 'sagittal' are the same. Midsagittal is the unique "
                "plane through the middle; any parallel plane is sagittal."
            ],
            "order": (
                "Position first, then directional terms (in pairs), then planes (with imaging "
                "examples), then cavities and regions. The vocabulary loads incrementally."
            ),
            "self_test": [
                "Without notes, give five pairs of directional terms.",
                "Sketch a transverse, frontal, and sagittal plane through the body.",
                "Place your hand on the upper right region of your abdomen and name the region "
                "and likely organs."
            ]
        },
        "clinical": (
            "This is the vocabulary every clinical report uses. A radiology read will say 'mass in "
            "the right upper quadrant, anterior to the kidney.' You cannot follow the report without "
            "the language. A nursing assessment will document pain 'lateral to the umbilicus, "
            "radiating distally down the right leg.' This is not academic vocabulary; it is the "
            "minimum standard for clinical communication. Sloppy terminology causes real handoff "
            "errors. A patient with right lower quadrant pain has a very different workup than one "
            "with left lower quadrant pain."
        )
    },

    "t-homeostasis": {
        "science": (
            "Homeostasis is the deepest concept in physiology. Almost every system you will study "
            "exists to regulate something. Make this load-bearing. The four parts of a negative "
            "feedback loop, stimulus, receptor, control center, effector, are a template you can "
            "lay over thermoregulation, blood glucose, blood pressure, blood pH, osmolarity, and "
            "calcium balance. Once they have the template, the rest of the course is variations on "
            "a theme."
            "\n\n"
            "Negative feedback opposes change. Positive feedback amplifies it. Positive feedback is "
            "rare in physiology because it is dangerous. The body only uses it when it needs to "
            "drive to an end point quickly (childbirth, clotting) and then shut it off. Anytime "
            "students see a system go to extremes, suspect a broken negative feedback loop or an "
            "inappropriately running positive one."
            "\n\n"
            "The set point is the target. Diseases often reset the set point rather than destroy "
            "the feedback machinery. Fever is the classic example: the hypothalamus has been told by "
            "pyrogens to defend 39 degrees instead of 37, and the entire feedback system dutifully "
            "drives toward the new target. The patient shivers (effector response) and the skin "
            "vasoconstricts (effector response) until they hit the new set point. Then they feel "
            "hot, because their body is hot. Get this and you understand a huge fraction of clinical "
            "physiology."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw a negative feedback loop for body temperature: arrows, "
                "labels, where the receptor is, where the effector is. Pre-commitment makes the "
                "feedback diagram stick."
            ),
            "misconceptions": [
                "Students think 'negative feedback' is bad. Reframe: it is stabilizing.",
                "Students think positive feedback is rare because it is unimportant. It is rare "
                "because it is risky, but where it occurs it is essential.",
                "The set point is confused with the current value. They are different. The set "
                "point is the target; the current value is what the receptor is measuring."
            ],
            "order": (
                "Definition, then loop components (with one shared example, like temperature), then "
                "negative versus positive contrast, then set point disturbances (fever). The loop "
                "components are the conceptual core; everything else hangs on them."
            ),
            "self_test": [
                "From memory, list the four components of a negative feedback loop.",
                "Identify the receptor, control center, and effector in the baroreflex.",
                "Explain in your own words why fever feels cold at the start and hot at the end."
            ]
        },
        "clinical": (
            "Almost every disease you will see is a homeostatic failure. Diabetes is broken glucose "
            "homeostasis. Hypertension is broken blood pressure homeostasis. Acidosis and alkalosis "
            "are broken pH homeostasis. Heart failure breaks blood pressure, then volume, then "
            "respiratory homeostasis in a cascade. Nurses live in this world: every set of vitals "
            "is a homeostatic readout. When something is out of range you are not just noting "
            "numbers; you are asking which loop is failing and which compensation is firing. A "
            "tachycardic, hypotensive patient is showing you their baroreflex trying to save their "
            "blood pressure. Reading vitals as feedback loops, not just values, changes the level "
            "of care you give."
        )
    },

    # ============================================================
    # MODULE 3: THE CELL
    # ============================================================

    "t-cell-structure": {
        "science": (
            "The plasma membrane is the boundary between alive and not-alive at the smallest scale. "
            "Phospholipid bilayer with embedded proteins. Selectively permeable: the cell decides "
            "what comes in and what goes out. Surface proteins are receptors, channels, transporters, "
            "and identity markers. If you teach nothing else about cells, teach the membrane. "
            "Everything in physiology happens across membranes."
            "\n\n"
            "Organelles divide labor. The nucleus stores DNA. The nucleolus inside makes ribosomal "
            "RNA. Free ribosomes make cytoplasmic proteins; rough-ER ribosomes make secreted and "
            "membrane proteins. The Golgi modifies and sorts proteins from the ER. Mitochondria are "
            "the ATP factories, with their own DNA (legacy of bacterial ancestry) and double "
            "membrane. Lysosomes digest debris. Peroxisomes detoxify reactive oxygen species and "
            "metabolize fatty acids."
            "\n\n"
            "Specialization is the story. A pancreatic acinar cell that secretes massive amounts "
            "of digestive enzymes has enormous rough ER. A cardiac myocyte that contracts non-stop "
            "is packed with mitochondria. A red blood cell, which just needs to carry hemoglobin, "
            "ditches its nucleus and most organelles entirely. Organelle abundance maps onto "
            "function; this is a question students will see again and again."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw a cell with the membrane and label what each major organelle "
                "does. They commit, then the video corrects them."
            ),
            "misconceptions": [
                "Cells are pictured as identical generic blobs. Reality: hundreds of cell types, "
                "each shaped for function.",
                "Mitochondria are 'powerhouses' in cliche. Better: ATP factories, with their own "
                "DNA, and they sense and respond to the cell's energy state.",
                "Students confuse the ER with the Golgi. ER makes; Golgi modifies and ships."
            ],
            "order": (
                "Membrane first (load-bearing), then nucleus, then the protein-secretion pipeline "
                "(ribosome to rough ER to Golgi), then mitochondria, then the cleanup crew "
                "(lysosomes, peroxisomes)."
            ),
            "self_test": [
                "List the organelles a pancreatic acinar cell would have in abundance and why.",
                "Why are red blood cells unusual in lacking a nucleus?",
                "What is the difference between rough ER and smooth ER in function?"
            ]
        },
        "clinical": (
            "Mitochondrial diseases cause exercise intolerance, muscle weakness, and neurodegeneration "
            "because high-demand tissues fail first when ATP supply drops. Lysosomal storage diseases "
            "(Tay-Sachs, I-cell) accumulate undigested debris in cells, producing progressive organ "
            "failure. Drugs that target the plasma membrane, ion channels, receptors, transporters, "
            "are the backbone of pharmacology. A patient on a statin has had hepatic mitochondria "
            "tweaked. A patient on chemotherapy is having their cell division and protein synthesis "
            "machinery hit hard. Cellular biology is the level at which most modern medicine acts."
        )
    },

    "t-membrane-transport": {
        "science": (
            "Anything that moves into or out of a cell goes either down its gradient (passive, free) "
            "or against its gradient (active, costs ATP). That single distinction organizes the entire "
            "topic."
            "\n\n"
            "Passive: simple diffusion through the bilayer (small, nonpolar molecules; O2, CO2, "
            "steroid hormones). Facilitated diffusion through channels or carriers (polar molecules "
            "and ions). Osmosis is water moving down its concentration gradient through aquaporins. "
            "All of these are 'free' to the cell. They use the energy already in the gradient."
            "\n\n"
            "Active: primary active transport burns ATP directly (the Na/K ATPase is the prototype, "
            "pumping 3 Na out and 2 K in per ATP). Secondary active transport uses the gradient set "
            "up by primary pumps (the Na-glucose symporter in the small intestine drags glucose in "
            "against its gradient by piggybacking on the Na coming in down its gradient). Build "
            "the conceptual chain: Na/K ATPase establishes the Na gradient; everything else in the "
            "cell uses that gradient as currency. This is why ouabain (a Na/K pump inhibitor) "
            "ultimately disables glucose absorption from the gut, even though it never touches "
            "the glucose transporter."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a cell membrane and predict which of these molecules cross "
                "passively versus require help: O2, glucose, Na, water, cholesterol, K. Then check."
            ),
            "misconceptions": [
                "Students think active transport means 'fast.' It means 'against the gradient.'",
                "Students lump all transport into 'osmosis.' Osmosis is specifically water.",
                "Aquaporins are sometimes thought of as exotic. They are everywhere; without them, "
                "water movement would be much too slow for physiology."
            ],
            "order": (
                "Frame the question (down or up the gradient?), then passive types, then active "
                "types, then the Na/K ATPase as the master gradient-builder."
            ),
            "self_test": [
                "Without notes, list two molecules that cross by simple diffusion and two that "
                "need help.",
                "Explain why blocking the Na/K pump eventually stops glucose absorption.",
                "Predict what happens to a red blood cell in pure water."
            ]
        },
        "clinical": (
            "Diuretics work by manipulating tubular transporters. Furosemide blocks the NKCC2 "
            "cotransporter in the loop of Henle, causing massive Na and water loss. Spironolactone "
            "blocks aldosterone (which controls Na reabsorption). IV fluids are designed around "
            "osmotic principles: isotonic saline keeps cells stable, hypotonic fluid drives water "
            "into cells (treating dehydration), hypertonic fluid pulls water out (treating cerebral "
            "edema). Cholera kills by hijacking the intestinal Cl channel, driving massive secretion. "
            "Cystic fibrosis is a defective Cl channel. Once you see the body as a network of "
            "transport mechanisms, much of clinical pharmacology becomes legible."
        )
    },

    # ============================================================
    # MODULE 4: TISSUES
    # ============================================================

    "t-epithelial-tissue": {
        "science": (
            "Epithelia cover and line. They are everywhere there is a body surface, external (skin) "
            "or internal (gut lumen, blood vessel, alveolus). Their job is barrier, exchange, "
            "secretion, or absorption, depending on location. They are avascular; nutrients come "
            "from the underlying connective tissue."
            "\n\n"
            "Classification is by layer count (first name) and cell shape (second name). Simple = "
            "one layer, made for exchange or secretion. Stratified = multiple layers, made for "
            "protection. Squamous = flat (good for diffusion). Cuboidal = cubed (room for secretion "
            "machinery). Columnar = tall (room for both, with microvilli for absorption). Once they "
            "have the naming logic, they can predict structure from function and vice versa."
            "\n\n"
            "Special cases: pseudostratified columnar (looks layered but is not, lines the upper "
            "airway, has cilia) and transitional (urinary bladder, can stretch flat). Spend extra "
            "time on the upper airway: pseudostratified ciliated columnar with goblet cells is the "
            "mucociliary escalator. When that fails (smoking, cystic fibrosis), the lungs lose their "
            "main defense. Predicting structure from function is the highest-yield exam skill in "
            "this section."
        ),
        "teaching": {
            "before_video": (
                "Show students a list of locations (alveolus, esophagus, kidney tubule, bladder, "
                "upper airway, small intestine) and have them predict the epithelial type for each "
                "before watching."
            ),
            "misconceptions": [
                "Pseudostratified is not actually stratified. Every cell still touches the basement "
                "membrane.",
                "Transitional epithelium does not appear transitional under a microscope; the name "
                "means it transitions in appearance when the bladder fills.",
                "Students confuse 'simple' for 'simple to understand.' It means one cell layer."
            ],
            "order": (
                "Function categories (barrier, exchange, secretion), then the naming system, then "
                "examples by location, then the special cases."
            ),
            "self_test": [
                "Name the epithelium of an alveolus and explain why.",
                "Why is the upper airway pseudostratified with cilia rather than stratified squamous?",
                "What changes about transitional epithelium between an empty and full bladder?"
            ]
        },
        "clinical": (
            "Chronic smokers undergo squamous metaplasia of the upper airway: protective stratified "
            "squamous replaces the original ciliated columnar. The new tissue cannot clear mucus, "
            "and pathogens linger. This is the cellular start of COPD. Burns destroy epidermis "
            "(stratified squamous) and demand grafting because the protective barrier is the entire "
            "point of skin. Barrett's esophagus replaces esophageal stratified squamous with "
            "columnar (in response to acid reflux); the new tissue is metabolically more active and "
            "more likely to become cancerous. Almost every tissue-level diagnosis in pathology is "
            "an epithelial story."
        )
    },

    "t-connective-tissue": {
        "science": (
            "Connective tissue is defined by what is between the cells, not the cells themselves. "
            "Cells suspended in an extracellular matrix of ground substance plus protein fibers "
            "(collagen, elastic, reticular). Vary the matrix and you get loose connective tissue, "
            "dense connective tissue, cartilage, bone, or blood. One family, enormous range of "
            "function."
            "\n\n"
            "Loose connective (areolar, adipose, reticular) is the general-purpose packing. Dense "
            "regular (tendons, ligaments) has parallel collagen for tensile strength in one "
            "direction. Dense irregular (dermis) has interwoven collagen for strength in all "
            "directions. Cartilage has chondrocytes in lacunae within a flexible matrix; it is "
            "avascular and heals poorly. Bone has osteocytes in a rigid mineralized matrix. Blood "
            "is connective tissue with a liquid matrix (plasma)."
            "\n\n"
            "Repair maps onto vascularity. Loose connective heals fast (rich blood supply). Cartilage "
            "heals poorly (avascular; nutrients arrive by diffusion only). Bone heals well, contrary "
            "to intuition, because it is highly vascular and has active osteoblasts ready to lay "
            "down new matrix. This is why a torn meniscus often fails to heal but a broken femur "
            "usually does."
        ),
        "teaching": {
            "before_video": (
                "Ask students to list five connective tissues and rank them by how well they heal. "
                "They have to predict before the data."
            ),
            "misconceptions": [
                "Blood is connective tissue. This is counterintuitive but high-yield.",
                "Adipose is sometimes seen as inert padding. It is metabolically and endocrinologically "
                "active.",
                "Students assume cartilage and bone are similar because they are both 'hard.' "
                "Their vascular biology and repair capacity are opposite."
            ],
            "order": (
                "What defines connective tissue (matrix), then types organized by matrix composition, "
                "then repair, organized by vascularity."
            ),
            "self_test": [
                "Without notes, list five connective tissue types.",
                "Why does cartilage heal poorly while bone heals well?",
                "Why is blood classified as connective tissue?"
            ]
        },
        "clinical": (
            "Osteogenesis imperfecta (defective collagen) makes bones brittle but also affects "
            "tendons, ligaments, and the sclera. Ehlers-Danlos syndromes affect collagen and produce "
            "hypermobile joints and fragile skin. A meniscal tear often requires surgery because "
            "cartilage cannot self-repair; a torn ACL has limited repair capacity for the same "
            "reason. Tendinopathy is a slow disease because the blood supply to tendons is limited. "
            "Burn patients lose dermis and require grafting because the dense irregular collagen "
            "network underneath the epidermis is the structural foundation skin needs."
        )
    },

    "t-muscle-nervous-tissue": {
        "science": (
            "Three muscle types, two nervous tissue cells: a small set, but high-yield. Compare-and-"
            "contrast pedagogy works best here."
            "\n\n"
            "Skeletal muscle: striated, multinucleated, voluntary, attached to bone. Cardiac: "
            "striated, single nucleus, involuntary, has intercalated discs (gap junctions that allow "
            "the heart to act as a functional syncytium). Smooth: not striated, single nucleus, "
            "involuntary, walls of hollow organs (gut, vessels, bladder, uterus). The discriminating "
            "features are striation (yes for skeletal and cardiac, no for smooth) and nucleus count "
            "(many for skeletal, one for the others)."
            "\n\n"
            "Nervous tissue is neurons plus glia. Neurons are the excitable, signaling cells. Glia "
            "are the support cells: in the CNS, astrocytes (blood-brain barrier and metabolism), "
            "oligodendrocytes (myelin), microglia (immune), ependymal (CSF production). In the PNS, "
            "Schwann cells make myelin and satellite cells support cell bodies. Glia outnumber "
            "neurons and do most of the day-to-day maintenance. When myelin fails (multiple "
            "sclerosis in CNS, Guillain-Barre in PNS), conduction fails."
        ),
        "teaching": {
            "before_video": (
                "Have students predict, for each muscle type: striated yes or no, nuclei one or "
                "many, voluntary or not, where in the body."
            ),
            "misconceptions": [
                "Cardiac muscle is sometimes lumped with skeletal because both are striated. The "
                "regulation and conduction biology are very different.",
                "Smooth muscle is thought of as weak. It is enormously strong; the uterus in labor "
                "and the GI tract are smooth muscle.",
                "Glia are thought of as background. They do most of the work of the nervous system."
            ],
            "order": (
                "Three muscle types side-by-side (compare on a small set of features), then neurons "
                "as excitable cells, then glia as the support network."
            ),
            "self_test": [
                "Which muscle type has intercalated discs and why does that matter?",
                "What CNS cell makes myelin?",
                "What goes wrong physiologically when myelin is destroyed?"
            ]
        },
        "clinical": (
            "Multiple sclerosis destroys CNS myelin and produces conduction failure across whatever "
            "tract is affected: vision changes if the optic nerve is hit, weakness or numbness if "
            "spinal tracts are hit, coordination loss if cerebellar pathways are hit. Guillain-Barre "
            "syndrome attacks PNS myelin and produces ascending paralysis. Smooth muscle disorders "
            "include irritable bowel syndrome (dysregulated gut motility), urinary incontinence "
            "(detrusor dysfunction), and asthma (bronchial smooth muscle hyperreactivity). Cardiac "
            "myocyte loss is the substrate of heart failure. Three muscle types, three families of "
            "disease."
        )
    },

    # ============================================================
    # MODULE 5: INTEGUMENTARY
    # ============================================================

    "t-skin-layers": {
        "science": (
            "Skin is your largest organ by surface area. Two layers strictly (epidermis, dermis) "
            "plus a hypodermis underneath that is technically not skin but is functionally part of "
            "the system. Each layer has a job."
            "\n\n"
            "Epidermis: stratified squamous keratinized, avascular, several sub-layers (basale, "
            "spinosum, granulosum, lucidum in thick skin only, corneum). Keratinocytes are born at "
            "the basale, mature upward, die, and form the cornified layer that protects against "
            "everything from microbes to water loss. Melanocytes in the basale produce melanin and "
            "transfer it to keratinocytes for UV protection. Langerhans cells (immune surveillance) "
            "and Merkel cells (touch) live here too."
            "\n\n"
            "Dermis: vascular, where the action is. Papillary layer has capillary loops and fine "
            "sensory endings; reticular layer is dense irregular connective tissue, the source of "
            "skin's strength. Hair follicles, glands, and nerves are dermal. Hypodermis is adipose "
            "and loose connective tissue, providing insulation and energy storage."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a cross-section of skin and try to label five layers/structures "
                "before watching."
            ),
            "misconceptions": [
                "Students think the epidermis is vascular. It is avascular; it lives off diffusion "
                "from the dermis.",
                "Tanning is sometimes seen as healthy. Tanning is the keratinocyte response to UV "
                "damage; melanin is protective but the damage has already occurred.",
                "The hypodermis is often called part of the skin. Technically it is not, but "
                "functionally it is inseparable."
            ],
            "order": (
                "Three layers overview, then epidermis with sub-layers, then dermis with vascular "
                "and sensory content, then hypodermis. Build from outside in."
            ),
            "self_test": [
                "List the layers of the epidermis from deep to superficial in thick skin.",
                "Why is the epidermis avascular?",
                "Where in the skin would a needle for an intradermal injection actually deliver "
                "the medication?"
            ]
        },
        "clinical": (
            "Burn depth: first-degree burns are epidermal (sunburn-like, painful, no scar). Second-"
            "degree are partial-thickness (blister, painful, may scar). Third-degree are full-"
            "thickness (extending into or through the dermis; the tissue from which new skin would "
            "regrow is gone, requiring grafting). Pressure ulcers, IV infiltrations, melanoma "
            "screening, transdermal drug delivery, all of these depend on knowing exactly where in "
            "the skin you are. A nurse who can name skin layers reads burns, wounds, and skin "
            "lesions with confidence."
        )
    },

    "t-skin-functions": {
        "science": (
            "Skin functions are not a list to memorize, they are a checklist for clinical assessment. "
            "Protection (barrier, immunity), thermoregulation (sweat and vasomotor), sensation (touch, "
            "pressure, temperature, pain), vitamin D synthesis (UVB on 7-dehydrocholesterol), and "
            "minor excretion (small amounts of nitrogen waste in sweat). Lose any of these and the "
            "patient suffers."
            "\n\n"
            "Accessory structures: hair (insulation, sensation, identification), nails (protection "
            "of digit tips, fine manipulation), eccrine sweat glands (thermoregulation), apocrine "
            "sweat glands (axilla and groin, activated at puberty, produce odor when bacteria feed "
            "on the secretion), sebaceous glands (oily sebum, waterproofs, slightly antimicrobial). "
            "Each accessory structure is a specialization of skin tissue."
            "\n\n"
            "Thermoregulation deserves a beat: vasodilation brings warm blood to the skin surface "
            "for heat dissipation (radiation, conduction), sweating cools by evaporation (water's "
            "high heat of vaporization, see Chemistry of Life), vasoconstriction conserves core "
            "heat. The countercurrent arrangement between cutaneous arteries and veins is an "
            "additional layer of thermal control."
        ),
        "teaching": {
            "before_video": (
                "Ask students to list every function of skin they can think of in 60 seconds, then "
                "compare to your list. Most will get fewer than half."
            ),
            "misconceptions": [
                "Skin is seen as cosmetic. It is the body's largest immune and thermoregulatory organ.",
                "Sweat is thought to cool by 'feeling cool.' It cools by evaporating; if it just "
                "drips off without evaporating, no cooling occurs.",
                "Vitamin D from skin is often overlooked. Sun exposure is a major route; deficiency "
                "is common in dark-skinned people at high latitudes."
            ],
            "order": (
                "Functions first (with thermoregulation expanded), then accessory structures and "
                "how each contributes."
            ),
            "self_test": [
                "Name five functions of the integumentary system.",
                "Explain how sweating actually cools the body.",
                "Why are dark-skinned people at higher risk of vitamin D deficiency in northern "
                "climates?"
            ]
        },
        "clinical": (
            "Burn patients lose fluid through damaged skin at staggering rates and die of "
            "dehydration, hypothermia, and infection long before the burn itself would kill them. "
            "Diabetics with poor circulation develop pressure ulcers because skin cannot defend or "
            "repair itself without good blood flow. Patients with autonomic dysfunction lose "
            "thermoregulation; spinal cord injury patients above T6 cannot vasoconstrict below the "
            "level of injury and are at risk for hypothermia in mild cold. Vitamin D status affects "
            "bone health, immunity, and probably mood; supplementation matters. Skin assessment is "
            "the most accessible window into systemic disease the nurse has."
        )
    },

    # ============================================================
    # MODULE 6: SKELETAL
    # ============================================================

    "t-bone-tissue": {
        "science": (
            "Bone is connective tissue with a mineralized matrix. It is alive and constantly being "
            "remodeled. The cells are osteoblasts (build matrix), osteocytes (mature, trapped in "
            "lacunae, sense load), and osteoclasts (resorb matrix; derived from monocyte lineage, "
            "not osteoblasts). Osteoblast versus osteoclast balance determines whether bone is being "
            "added or removed."
            "\n\n"
            "Compact bone is dense, organized into osteons (Haversian systems). Each osteon has "
            "concentric lamellae of matrix around a central canal carrying vessels and nerves. "
            "Spongy bone is the trabecular meshwork in the interior of bones, often containing red "
            "marrow. Long bones have a diaphysis (shaft), epiphyses (ends), metaphysis (growth zone), "
            "periosteum (outer covering), and endosteum (lining the marrow cavity)."
            "\n\n"
            "Two kinds of ossification: intramembranous (skull flat bones, clavicle) directly from "
            "mesenchyme, and endochondral (most other bones) from a hyaline cartilage model. "
            "Lengthening occurs at the epiphyseal plate until it closes in late adolescence. "
            "Throughout life, remodeling continues. PTH raises blood calcium by activating osteoclasts; "
            "calcitonin opposes it (modest effect). Estrogen restrains osteoclasts; this is why "
            "postmenopausal women lose bone rapidly."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw a long bone in cross-section and label five structures. They "
                "have to commit before checking."
            ),
            "misconceptions": [
                "Bone is thought of as inert. Bone is intensely metabolically active and "
                "continuously remodeled.",
                "Osteoclast and osteoblast names sound similar; students mix them up. Cue: clast "
                "like clast-rophobic = breaking down; blast like blast off = building.",
                "Calcium balance and bone density are sometimes seen as the same thing. They are "
                "linked but distinct: short-term calcium balance can be at the expense of bone density."
            ],
            "order": (
                "Cells, then compact vs spongy structure, then ossification types, then lifelong "
                "remodeling and hormonal control."
            ),
            "self_test": [
                "Cue yourself: what does each bone cell do?",
                "How does estrogen affect bone density and why does postmenopausal osteoporosis "
                "happen?",
                "What is happening at the epiphyseal plate and why does it close in adulthood?"
            ]
        },
        "clinical": (
            "Osteoporosis is bone loss from accelerated osteoclast activity relative to osteoblasts. "
            "Postmenopausal women are at high risk because estrogen normally restrains osteoclasts. "
            "Bisphosphonates are first-line treatment; they inhibit osteoclasts. Hyperparathyroidism "
            "raises blood calcium by mobilizing bone calcium, producing kidney stones, fractures, "
            "and 'stones, bones, groans' on the boards. Pediatric fracture management depends on "
            "whether the epiphyseal plate is involved (Salter-Harris classification); plate injuries "
            "can disrupt growth. Bone metastases are common in advanced cancers and cause pain, "
            "fractures, and hypercalcemia. Nurses caring for elderly patients are constantly thinking "
            "about fall risk, fracture prevention, and bone density."
        )
    },

    "t-axial-skeleton": {
        "science": (
            "The axial skeleton is the central line: skull, vertebral column, and thoracic cage. "
            "Its job is protection of the most vulnerable organs (brain, spinal cord, heart, lungs) "
            "and anchorage for the appendicular skeleton."
            "\n\n"
            "Skull: eight cranial bones (frontal, parietal pair, temporal pair, occipital, sphenoid, "
            "ethmoid) and fourteen facial bones (maxillae, zygomatics, mandible, and the smaller "
            "facial bones). Sutures are immovable joints. The vertebral column has five regions: "
            "cervical (7, including the atlas and axis), thoracic (12, articulating with ribs), "
            "lumbar (5, the weight-bearers), sacrum (5 fused), coccyx (3-4 fused)."
            "\n\n"
            "Thoracic cage: sternum (manubrium, body, xiphoid) and 12 pairs of ribs (true 1-7, "
            "false 8-10, floating 11-12). Function: protect heart and lungs, anchor breathing "
            "muscles. The shape and mobility of the cage are critical for ventilation; chronic "
            "obstructive lung disease patients develop a barrel chest because their inflated lungs "
            "remodel the cage."
        ),
        "teaching": {
            "before_video": (
                "Ask students to list the five regions of the vertebral column and the count of "
                "vertebrae in each, from memory."
            ),
            "misconceptions": [
                "Students think all vertebrae look the same. Each region has distinctive shape "
                "because of different function: cervical for mobility, thoracic for rib articulation, "
                "lumbar for weight-bearing.",
                "Floating ribs are thought of as defects. They are normal anatomy.",
                "The sacrum is treated as a single bone; it is five fused vertebrae and the fusion "
                "is functionally important."
            ],
            "order": (
                "Skull, then vertebral column with regional contrasts, then thoracic cage and its "
                "ventilatory role."
            ),
            "self_test": [
                "Without notes, write the number of vertebrae in each region.",
                "What is unique about C1 (atlas) and C2 (axis) and why?",
                "How does a compression fracture of a thoracic vertebra change posture and breathing?"
            ]
        },
        "clinical": (
            "Compression fractures of thoracic and lumbar vertebrae are common in osteoporosis and "
            "produce loss of height, kyphosis ('dowager's hump'), and chronic pain. Rib fractures "
            "limit ventilation because breathing hurts; nurses watch for atelectasis and pneumonia. "
            "Skull fractures depend on where they are: a basilar skull fracture can damage cranial "
            "nerves; a temporal bone fracture can rupture the middle meningeal artery and cause an "
            "epidural hematoma. Spinal cord injuries are classified by level: a C5 transection "
            "preserves diaphragm function but paralyzes the arms and legs; C3 or above paralyzes the "
            "diaphragm and the patient needs ventilator support."
        )
    },

    "t-appendicular-skeleton": {
        "science": (
            "The appendicular skeleton is everything that hangs off the axial. Pectoral girdle "
            "(clavicle and scapula) attaches the upper limb. Pelvic girdle (two coxal bones plus "
            "the sacrum) attaches the lower limb. The trade-off across the two girdles is "
            "instructive: pectoral is loose (mobility), pelvic is fused (stability)."
            "\n\n"
            "Upper limb: humerus (arm), radius (lateral, thumb side) and ulna (medial) (forearm), "
            "8 carpals (wrist), 5 metacarpals (palm), 14 phalanges (fingers). Lower limb: femur "
            "(thigh, largest bone in the body), tibia (medial weight-bearer) and fibula (lateral) "
            "(leg), 7 tarsals (ankle and back of foot), 5 metatarsals (foot), 14 phalanges (toes)."
            "\n\n"
            "Pelvic girdle has key sex differences: female pelvis is wider, shallower, with a "
            "larger pelvic inlet, designed for childbirth. The pubic angle is wider in females "
            "(about 100 degrees) versus narrower in males (about 60 degrees). These are clinically "
            "relevant in obstetrics, pelvic surgery, and forensic anthropology."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw the bones of one arm and one leg from memory, labeling. They "
                "have to commit before correction."
            ),
            "misconceptions": [
                "Students confuse radius and ulna. Cue: radius is on the same side as the radial "
                "artery (thumb side).",
                "Tibia and fibula get mixed up. Tibia is the weight-bearer (much thicker); fibula "
                "is the lateral splint.",
                "Students assume male and female skeletons are identical. The pelvis differs "
                "significantly."
            ],
            "order": (
                "Pectoral girdle, upper limb proximal to distal, then pelvic girdle, then lower limb. "
                "Compare girdle mobility versus stability as a closing concept."
            ),
            "self_test": [
                "Which forearm bone is on the thumb side?",
                "How many bones in the wrist?",
                "How does the female pelvis differ from the male and why?"
            ]
        },
        "clinical": (
            "Clavicle fractures are common (the most common fracture in children) and usually heal "
            "without surgery, but the shoulder drops because the strut is broken. Hip fractures in "
            "the elderly are a major source of morbidity; mortality at one year is around 20-30%. "
            "Carpal tunnel syndrome (median nerve compression at the wrist) is a workplace injury "
            "epidemic. Pelvic fractures from high-energy trauma can hide enormous blood loss in "
            "the pelvic cavity. Obstetric nursing depends on knowing pelvic anatomy in detail."
        )
    },

    "t-joints-movements": {
        "science": (
            "Joints classify two ways. Structurally: fibrous, cartilaginous, synovial, based on what "
            "connects the bones. Functionally: synarthrosis (immovable), amphiarthrosis (slightly "
            "movable), diarthrosis (freely movable). Most synovial joints are diarthroses; most "
            "fibrous and many cartilaginous joints are synarthroses or amphiarthroses."
            "\n\n"
            "Synovial joints have the most clinical relevance. They have a joint cavity filled with "
            "synovial fluid, articular cartilage on bone ends, a fibrous capsule, and often "
            "ligaments, menisci, and bursae. Subtypes: plane (carpals), hinge (elbow, knee, "
            "interphalangeal), pivot (atlanto-axial), condyloid (wrist), saddle (thumb), ball-and-"
            "socket (shoulder, hip). Each subtype has characteristic movements."
            "\n\n"
            "Movements: flexion (decreases joint angle), extension (increases it), abduction (moves "
            "away from midline), adduction (moves toward midline), rotation (around long axis), "
            "circumduction (cone-shaped sweep), plus the specialty terms (pronation, supination, "
            "inversion, eversion, dorsiflexion, plantarflexion). Teach the major terms with both "
            "the verbal definition and a body demonstration."
        ),
        "teaching": {
            "before_video": (
                "Have students perform each movement (flexion, extension, abduction, etc.) on "
                "themselves and write the joint that allows it. Movement memory is stronger than "
                "verbal memory."
            ),
            "misconceptions": [
                "Students confuse pronation and supination. Cue: supination = palm up, like "
                "carrying SOUP.",
                "Flexion is sometimes thought to mean 'curling.' It means decreasing the joint "
                "angle, which is curling for some joints but not for others (the shoulder flexes "
                "by raising the arm forward).",
                "Hinge joints are thought to be limited to one axis. They are, but with some "
                "rotation in the knee (which is unusual)."
            ],
            "order": (
                "Classification (structural and functional), then synovial subtypes with examples, "
                "then movements with physical demonstration."
            ),
            "self_test": [
                "Name the six synovial joint subtypes and give an example of each.",
                "What is the difference between abduction and adduction?",
                "Demonstrate flexion and extension of the elbow, hip, and shoulder."
            ]
        },
        "clinical": (
            "Rheumatoid arthritis attacks synovial joints; the inflamed synovium forms a pannus "
            "that erodes cartilage, then bone, leaving deformed joints. Osteoarthritis is wear and "
            "tear: cartilage thins, joint space narrows, osteophytes form. Joint dislocations are "
            "more common at the shoulder than the hip because the shoulder trades stability for "
            "mobility. Ligament injuries (ACL, MCL of the knee) are common in athletes. Hip "
            "replacements and knee replacements are among the most common surgeries in the elderly "
            "population. Knowing joint anatomy is part of every assessment of a patient who fell, "
            "had a sports injury, or has chronic joint pain."
        )
    },

    # ============================================================
    # MODULE 7: MUSCULAR
    # ============================================================

    "t-skeletal-muscle-microanatomy": {
        "science": (
            "The structural hierarchy is the spine of the topic: muscle, fascicle, fiber (cell), "
            "myofibril, sarcomere. Each level is wrapped in connective tissue (epimysium, "
            "perimysium, endomysium) that converges into the tendon. Build this scaffold first; "
            "everything else hangs on it."
            "\n\n"
            "The sarcomere is the contractile unit. Z-line to Z-line. Thick filaments (myosin) in "
            "the center (A band). Thin filaments (actin, troponin, tropomyosin) extending from the "
            "Z-line (I band). The overlap region is where cross-bridges can form. During contraction "
            "the I band shrinks and the H zone (myosin only) narrows, but the A band (thick filament "
            "length) does not change. This is a common test point and a useful conceptual anchor."
            "\n\n"
            "Excitation machinery: sarcolemma (the muscle fiber's plasma membrane), T-tubules "
            "(deep invaginations that carry action potentials into the interior), sarcoplasmic "
            "reticulum (SR, the calcium store wrapping each myofibril). T-tubules and SR meet at "
            "triads, where electrical excitation triggers calcium release. This coupling is "
            "essential; disrupt the triads and contraction fails even though action potentials "
            "still propagate."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the structural hierarchy as nested levels, then a sarcomere "
                "with bands labeled. Pre-commitment makes the next topic (sliding filament) much "
                "easier."
            ),
            "misconceptions": [
                "Students think the A band changes length during contraction. It does not; the thick "
                "filament is rigid.",
                "T-tubules and SR are confused. T-tubules carry action potentials inward; SR "
                "stores and releases calcium. Both meet at the triad.",
                "Sarcomere is sometimes called sarcomeres (plural). Get the singular cue: it is "
                "one unit, repeated."
            ],
            "order": (
                "Hierarchy first, then sarcomere structure, then excitation machinery. Save the "
                "cross-bridge cycle for the next topic; it is its own beat."
            ),
            "self_test": [
                "Without notes, list the structural levels from whole muscle down to sarcomere.",
                "Sketch a sarcomere and label A band, I band, H zone, Z-line.",
                "What is the function of a triad?"
            ]
        },
        "clinical": (
            "Muscular dystrophies are diseases of structural proteins (dystrophin in Duchenne). "
            "The sarcolemma cannot withstand the mechanical stress of contraction, fibers break "
            "down, and progressive weakness results. Malignant hyperthermia (next topic) involves "
            "a defective SR calcium channel. Statins occasionally cause myopathy: muscle pain and "
            "weakness from sarcomere-level disturbance. Understanding skeletal muscle microanatomy "
            "is understanding why a patient with myopathy is weak and what tests confirm it (CK "
            "elevation, biopsy)."
        )
    },

    "t-sliding-filament": {
        "science": (
            "This is one of the most beautiful pieces of physiology and one of the highest-yield "
            "topics in A&P. Spend the time."
            "\n\n"
            "Step 0 (the trigger): action potential at the neuromuscular junction releases ACh, "
            "opens nicotinic receptors, depolarizes the sarcolemma. The depolarization sweeps down "
            "T-tubules and triggers calcium release from the SR. Calcium is the signal."
            "\n\n"
            "The four-step cross-bridge cycle: (1) Cocking, myosin head hydrolyzes ATP to ADP+Pi "
            "and reorients into the high-energy position. (2) Binding, calcium binds troponin, "
            "tropomyosin shifts off the actin sites, myosin binds actin. (3) Power stroke, myosin "
            "pivots, pulling actin toward the M-line, releasing ADP and Pi. (4) Detachment, a new "
            "ATP binds myosin, which releases actin; cycle repeats. The thin filaments slide along "
            "the thick filaments; the sarcomere shortens; the muscle contracts. Filament lengths "
            "do not change; their overlap does."
            "\n\n"
            "Relaxation: when neural input stops, ACh is broken down by acetylcholinesterase, the "
            "sarcolemma repolarizes, the SR calcium ATPase pumps calcium back into the SR, troponin "
            "returns to its resting position, tropomyosin re-covers the actin sites. No calcium, "
            "no cross-bridges, no contraction. Both excitation and relaxation require ATP. This is "
            "why rigor mortis happens: after death, no ATP means myosin cannot detach from actin."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a sarcomere at rest and predict what changes during contraction. "
                "Then they have to draw the four-step cycle in order before watching."
            ),
            "misconceptions": [
                "Students think calcium directly attaches myosin to actin. Calcium binds troponin; "
                "troponin moves tropomyosin; tropomyosin exposes the actin site.",
                "ATP is thought to be needed only for the power stroke. It is needed for cocking "
                "AND detachment, but the power stroke itself is the release of stored energy.",
                "Rigor mortis is sometimes thought to be from low calcium. It is from no ATP, so "
                "no detachment, so locked cross-bridges."
            ],
            "order": (
                "Trigger first (ACh to calcium), then the four steps drilled IN ORDER with hand "
                "gestures, then relaxation, then rigor as a check on understanding."
            ),
            "self_test": [
                "Without notes, list the four steps of the cross-bridge cycle in order.",
                "Where in the cycle is ATP hydrolyzed? Where is fresh ATP needed?",
                "Explain rigor mortis in terms of cross-bridge biology."
            ]
        },
        "clinical": (
            "Curare and similar drugs block nicotinic ACh receptors at the neuromuscular junction, "
            "preventing depolarization, causing flaccid paralysis. Used clinically for surgical "
            "muscle relaxation. Organophosphate poisoning inhibits acetylcholinesterase, so ACh "
            "lingers, producing fasciculations and eventually depolarization block and respiratory "
            "paralysis (the farm worker's emergency, the sarin gas attack). Malignant hyperthermia "
            "is a genetic defect in the SR calcium release channel: certain anesthetics trigger "
            "uncontrolled calcium release, sustained contraction, hyperthermia from continuous "
            "cross-bridge cycling, ATP depletion, and rhabdomyolysis. Treatment is dantrolene "
            "(blocks SR calcium release). Every one of these stories is one node of the cross-bridge "
            "cycle being attacked."
        )
    },

    "t-motor-units": {
        "science": (
            "A motor unit is one motor neuron plus all the muscle fibers it innervates. Small motor "
            "units (a few fibers) give fine control: extraocular muscles have motor units of 5-10 "
            "fibers. Large motor units (many fibers) give power: quadriceps motor units have "
            "thousands. The size of the motor unit is set by what the muscle needs to do."
            "\n\n"
            "Force grading happens two ways. Recruitment: activate more motor units (the Henneman "
            "size principle says small units fire first, large units recruited as force demand "
            "rises). Frequency summation: fire the same motor unit faster, so twitches overlap. "
            "If firing is fast enough, twitches fuse into a sustained, smooth contraction (tetanus). "
            "These two mechanisms are how the body smoothly grades force from picking up a feather "
            "to deadlifting a barbell."
            "\n\n"
            "Fiber types: Type I (slow oxidative, fatigue-resistant, postural muscles), Type IIa "
            "(fast oxidative, intermediate), Type IIx (fast glycolytic, powerful but fatigue quickly). "
            "Endurance training shifts the population toward Type I characteristics; power training "
            "toward Type IIx. Fatigue has multiple causes: substrate depletion (glycogen, ATP), "
            "metabolic byproduct accumulation (H+, Pi), and neural factors (central fatigue)."
        ),
        "teaching": {
            "before_video": (
                "Ask students to predict the motor unit size in an eye muscle versus a thigh muscle. "
                "They have to commit before the answer."
            ),
            "misconceptions": [
                "Tetanus the disease is named after tetanus the contraction, which causes the "
                "rigid muscles. Students often miss this connection.",
                "Students think 'recruitment' is about overall fitness. It is the moment-to-moment "
                "neural decision to activate more motor units.",
                "Fast and slow twitch fibers are sometimes thought to be fixed at birth. They are "
                "largely genetic but training shifts the population."
            ],
            "order": (
                "Motor unit definition, then force grading (recruitment and frequency summation), "
                "then fiber types and adaptation."
            ),
            "self_test": [
                "Why are extraocular muscles innervated by very small motor units?",
                "What is the difference between recruitment and frequency summation?",
                "Predict the fiber type adaptations in an endurance athlete versus a sprinter."
            ]
        },
        "clinical": (
            "Myasthenia gravis is an autoimmune attack on nicotinic ACh receptors at the NMJ, "
            "producing fluctuating weakness that worsens with repeated use. Lambert-Eaton syndrome "
            "is an attack on the presynaptic voltage-gated calcium channel; the resulting "
            "decrease in ACh release produces weakness that improves with repeated activation "
            "(opposite of myasthenia). Critical illness myopathy and disuse atrophy occur in ICU "
            "patients within days of immobilization. ALS destroys motor neurons themselves, "
            "denervating muscles and producing progressive paralysis. Nurses caring for any patient "
            "with weakness need to think about what part of the motor system is failing."
        )
    },

    # ============================================================
    # MODULE 8: NERVOUS
    # ============================================================

    "t-neurons-rmp": {
        "science": (
            "Neuron anatomy first: dendrites receive, soma integrates, axon transmits, axon terminal "
            "releases neurotransmitter. The neuron is shaped for its job: a polarized communication "
            "device that can be a few millimeters long (interneuron) or over a meter long (motor "
            "neuron from spinal cord to foot)."
            "\n\n"
            "Resting membrane potential is about -70 mV: the inside of the cell is negative relative "
            "to the outside. Two main forces keep it that way: the Na/K ATPase actively pumps 3 Na "
            "out and 2 K in (net export of positive charge, slightly negative contribution to the "
            "potential), and K leak channels let K flow out down its concentration gradient (leaving "
            "the inside more negative). The membrane at rest is mostly permeable to K; this is why "
            "the resting potential sits close to the K equilibrium potential of -90 mV but not "
            "exactly there (small contributions from Na and Cl)."
            "\n\n"
            "Glia matter: astrocytes maintain the blood-brain barrier and clean up extracellular K "
            "and neurotransmitter. Oligodendrocytes wrap axons in myelin (CNS); Schwann cells do "
            "the same job in the PNS. Microglia are the immune cells of the brain. Ependymal cells "
            "line the ventricles and produce CSF. Glia outnumber neurons by roughly 10:1; the "
            "nervous system is mostly glia, not neurons."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a neuron with the parts labeled and then a graph of membrane "
                "potential over time at rest. They have to commit to the resting value."
            ),
            "misconceptions": [
                "Students think the resting potential is set entirely by the Na/K pump. The pump "
                "is necessary to build the gradients, but the resting potential is set by ion "
                "permeability (mostly K leak).",
                "The minus sign of -70 mV is sometimes ignored. It is the entire point: the cell "
                "interior is negative.",
                "Glia are seen as bystanders. They are essential and outnumber neurons."
            ],
            "order": (
                "Anatomy first, then the gradients (Na out, K in), then permeability and the "
                "resting potential, then glia as context."
            ),
            "self_test": [
                "What is the typical resting membrane potential of a neuron?",
                "Why is the inside of the cell negative?",
                "Name the CNS glial cells and what each one does."
            ]
        },
        "clinical": (
            "Local anesthetics block voltage-gated Na channels and prevent action potentials in "
            "sensory neurons; the patient loses pain sensation. Cardiac glycosides (digoxin) inhibit "
            "the Na/K ATPase, which raises intracellular Na, which in turn raises intracellular Ca "
            "(through the Na/Ca exchanger), strengthening cardiac contraction. Multiple sclerosis "
            "(demyelination of CNS axons) is a glial disease. Hypokalemia and hyperkalemia both "
            "produce dangerous changes in membrane excitability, which is why potassium is one of "
            "the most carefully monitored electrolytes in the hospital. Every nurse needs to "
            "understand the relationship between potassium and the resting potential."
        )
    },

    "t-action-potentials": {
        "science": (
            "The action potential is one of physiology's signature stories. Spend time on it; this "
            "is high-yield."
            "\n\n"
            "Phases: at rest, -70 mV. A stimulus depolarizes the membrane; if it reaches threshold "
            "(about -55 mV), voltage-gated Na channels open en masse, Na rushes in down its "
            "gradient, and the membrane swings positive (to about +30 mV). Then Na channels "
            "inactivate (a separate gate closes them) and voltage-gated K channels open; K rushes "
            "out, repolarizing the cell. K channels close slowly, producing a brief "
            "afterhyperpolarization. The Na/K pump resets the gradients (slowly, in the background). "
            "All-or-none: a suprathreshold stimulus always produces the same-size AP."
            "\n\n"
            "Propagation: unmyelinated axons propagate continuously, regenerating the AP at every "
            "patch of membrane (slow). Myelinated axons regenerate the AP only at nodes of Ranvier; "
            "the signal effectively jumps from node to node (saltatory conduction, much faster). "
            "Refractory periods (absolute, then relative) prevent backward propagation and limit "
            "firing frequency."
            "\n\n"
            "Synaptic transmission: AP reaches the terminal, opens voltage-gated Ca channels, Ca "
            "rushes in, vesicles fuse with the membrane, neurotransmitter is released into the "
            "synaptic cleft, binds receptors on the postsynaptic membrane, produces an EPSP "
            "(excitatory) or IPSP (inhibitory). Signal termination: reuptake, enzymatic breakdown, "
            "or diffusion away. EPSPs and IPSPs summate at the postsynaptic axon hillock; if the "
            "net depolarization reaches threshold, the postsynaptic cell fires."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a labeled action potential trace from memory: time on x-axis, "
                "voltage on y-axis, with the phases marked. They have to commit before the video."
            ),
            "misconceptions": [
                "Bigger stimulus equals bigger action potential. False: all-or-none means the AP "
                "is the same size regardless of stimulus strength. Bigger stimulus equals more "
                "frequent APs.",
                "K and Na are confused as to direction. Cue: Na is in for depolarization, K is "
                "out for repolarization.",
                "Saltatory conduction is sometimes described as 'jumping' which makes students "
                "think the AP literally jumps over membrane. It is regenerated at each node, just "
                "not at intervening membrane."
            ],
            "order": (
                "Resting potential recap, then the AP phases (in order with ion movements), then "
                "all-or-none and refractory periods, then propagation, then synaptic transmission "
                "as the next-cell handoff."
            ),
            "self_test": [
                "From memory, label the phases of an action potential on a voltage trace.",
                "Explain saltatory conduction in one sentence.",
                "What ion triggers neurotransmitter release at the axon terminal?"
            ]
        },
        "clinical": (
            "Multiple sclerosis demyelinates CNS axons; saltatory conduction fails; symptoms "
            "depend on which tracts are affected. Local anesthetics block Na channels in sensory "
            "neurons selectively (because sensory axons are smaller and more easily blocked) and "
            "produce regional anesthesia. SSRIs raise synaptic serotonin by blocking reuptake; the "
            "antidepressant effect lags weeks behind the immediate pharmacology because downstream "
            "neuroplasticity changes are slow. Botulinum toxin blocks neurotransmitter release "
            "(presynaptic) and causes flaccid paralysis; tetanus toxin blocks inhibitory "
            "neurotransmitter release and causes rigid paralysis. Almost every neurology drug acts "
            "on some node of the AP-synapse cascade."
        )
    },

    "t-cns-organization": {
        "science": (
            "The brain has four major regions to get right. Cerebrum: the cortex (gray matter) over "
            "white matter, divided into four lobes (frontal, parietal, temporal, occipital). "
            "Diencephalon: thalamus (sensory relay), hypothalamus (homeostasis HQ), epithalamus "
            "(pineal gland). Brainstem: midbrain, pons, medulla (vital reflexes, cranial nerves "
            "III-XII). Cerebellum: motor coordination and balance."
            "\n\n"
            "Functional cortex landmarks: precentral gyrus (frontal lobe) is the primary motor "
            "cortex; postcentral gyrus (parietal lobe) is the primary somatosensory cortex. "
            "Occipital lobe has the primary visual cortex; temporal lobe has auditory cortex and "
            "Wernicke area (language comprehension); Broca area is in the frontal lobe (language "
            "production). These landmarks are how you read a stroke."
            "\n\n"
            "Coverings and fluid: three meningeal layers (dura outside, arachnoid, pia next to "
            "the brain). CSF is made by choroid plexus in the ventricles, circulates through the "
            "subarachnoid space, and drains via arachnoid villi into the venous system. The spinal "
            "cord runs from the medulla to L1-L2. Below L1-L2, the cauda equina (loose bundle of "
            "spinal nerve roots) is what you stick a needle around for a lumbar puncture."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the cerebrum, label the four lobes, and put a star on the "
                "precentral gyrus, postcentral gyrus, Broca area, and Wernicke area. They have "
                "to commit before the video."
            ),
            "misconceptions": [
                "Students think the cerebellum makes movements happen. It modulates and coordinates "
                "movements; the motor cortex initiates them.",
                "The brainstem is often dismissed as small. It contains the vital reflex centers "
                "for breathing, heart rate, and consciousness.",
                "Broca and Wernicke get confused. Cue: Broca (frontal) is for production "
                "('mouth in front'), Wernicke (temporal) is for comprehension ('ears on side')."
            ],
            "order": (
                "Four major regions, then cortex landmarks, then meninges and CSF, then spinal cord "
                "as the extension into the body."
            ),
            "self_test": [
                "Name the four lobes of the cerebrum.",
                "Where is the primary motor cortex?",
                "What is the difference between Broca aphasia and Wernicke aphasia?"
            ]
        },
        "clinical": (
            "Strokes are localized by neurological deficit. A patient with right-sided weakness, "
            "right-sided sensory loss, and Broca-type aphasia has had a left middle cerebral "
            "artery stroke. A patient with vertical gaze palsy, ipsilateral facial weakness, and "
            "contralateral body weakness has a brainstem lesion. Cerebellar strokes produce "
            "ataxia (uncoordinated movement) without paralysis. Increased intracranial pressure "
            "produces a stereotyped triad: hypertension, bradycardia, irregular breathing "
            "(Cushing triad). Nurses are often the first to spot neurological changes by serial "
            "assessment; knowing the anatomy means knowing where the problem is."
        )
    },

    "t-pns-autonomic": {
        "science": (
            "PNS = cranial nerves and spinal nerves. Twelve pairs of cranial nerves (mostly head "
            "and neck; vagus, CN X, is the long-haul exception, innervating the heart, lungs, and "
            "much of the GI tract). Thirty-one pairs of spinal nerves, each with sensory (dorsal "
            "root) and motor (ventral root) fibers."
            "\n\n"
            "Somatic motor vs autonomic motor. Somatic is voluntary, single neuron from CNS to "
            "skeletal muscle, releases ACh at the NMJ. Autonomic is involuntary, two-neuron chain "
            "(pre-ganglionic from CNS, synapses in a ganglion, post-ganglionic to target), "
            "innervates smooth muscle, cardiac muscle, and glands."
            "\n\n"
            "Sympathetic ('fight or flight'): thoracolumbar origin (T1-L2). Short pre-ganglionic, "
            "long post-ganglionic. Most post-ganglionic releases norepinephrine at the target. "
            "Effects: pupils dilate, heart rate and force up, bronchi dilate, gut motility down, "
            "skeletal muscle vasodilation, skin vasoconstriction, glycogen breakdown. Designed for "
            "action."
            "\n\n"
            "Parasympathetic ('rest and digest'): craniosacral origin (CN III, VII, IX, X plus "
            "S2-S4). Long pre-ganglionic, short post-ganglionic. Releases ACh at target. Effects: "
            "pupils constrict, heart rate down, bronchi constrict, gut motility up, digestion "
            "active. Designed for maintenance."
            "\n\n"
            "Most organs receive both; the balance shifts depending on state. The reflex arc is "
            "the basic functional unit: receptor, sensory neuron, integration center (often spinal "
            "cord), motor neuron, effector."
        ),
        "teaching": {
            "before_video": (
                "Ask students to predict the sympathetic effect on each of: pupil, heart rate, "
                "gut, bronchi, glycogen. Then test the same list under parasympathetic activation."
            ),
            "misconceptions": [
                "Sympathetic and parasympathetic are seen as opposing forces in a tug-of-war. "
                "More accurately, they have different baselines for different organs, and the "
                "balance shifts.",
                "Both divisions release ACh at some point. Cue: parasympathetic uses ACh at the "
                "target; sympathetic uses NE at the target (with ganglia using ACh in both cases).",
                "Students think autonomic effects are slow because they are involuntary. Sympathetic "
                "responses can be very fast (adrenaline surge in seconds)."
            ],
            "order": (
                "PNS overview (cranial and spinal nerves), then somatic vs autonomic distinction, "
                "then sympathetic and parasympathetic in detail, then the reflex arc."
            ),
            "self_test": [
                "List the five components of a reflex arc.",
                "What does the sympathetic system do to the eye? The heart? The gut?",
                "Which cranial nerve has the broadest parasympathetic distribution?"
            ]
        },
        "clinical": (
            "Beta-blockers blunt sympathetic effects on the heart (slower rate, less force, lower "
            "blood pressure). Atropine blocks parasympathetic effects at muscarinic receptors and "
            "is used to raise heart rate or dry secretions. Spinal cord injuries above T6 disrupt "
            "sympathetic outflow and produce autonomic dysreflexia: a noxious stimulus below the "
            "lesion (full bladder, pressure ulcer) triggers an unopposed sympathetic surge with "
            "severe hypertension and headache, while the parasympathetic system tries to "
            "compensate above the lesion. This is a true emergency. Diabetic autonomic neuropathy "
            "produces orthostatic hypotension, gastroparesis, and erectile dysfunction. Knowing "
            "the autonomic system is knowing why many medications produce predictable side effects."
        )
    },

    # ============================================================
    # MODULE 9: SPECIAL SENSES
    # ============================================================

    "t-vision": {
        "science": (
            "Light hits the cornea first; the cornea does most of the eye's fixed focusing. Then "
            "the lens, which is adjustable (accommodation). Then the vitreous humor; then the retina, "
            "which contains photoreceptors."
            "\n\n"
            "Accommodation: for near vision the ciliary muscle contracts, the zonular fibers slacken, "
            "and the lens elastically rounds up (stronger refraction). For far vision the ciliary "
            "muscle relaxes, zonules pull the lens flatter. With age the lens stiffens "
            "(presbyopia) and near vision worsens; reading glasses compensate."
            "\n\n"
            "Photoreceptors: rods are highly sensitive, give black-and-white vision, dominate at "
            "low light. Cones come in three types (red, green, blue), are less sensitive but give "
            "color and acuity, dominate in daylight. The fovea is the area of sharpest vision: "
            "all cones, no overlying neurons. The optic disc is where the optic nerve leaves the "
            "eye; no photoreceptors, hence the blind spot."
            "\n\n"
            "Phototransduction: light isomerizes the chromophore in rhodopsin (or cone opsins), "
            "which triggers a signaling cascade that hyperpolarizes the photoreceptor. Photoreceptors "
            "release less glutamate in light. Downstream bipolar and ganglion cells interpret the "
            "change. The signal exits via the optic nerve, partially crosses at the optic chiasm, "
            "and reaches the lateral geniculate nucleus and visual cortex."
        ),
        "teaching": {
            "before_video": (
                "Have students draw an eye in cross-section and label cornea, lens, retina, fovea, "
                "optic disc, optic nerve."
            ),
            "misconceptions": [
                "The lens does most of the focusing. False: the cornea does most of it; the lens "
                "fine-tunes via accommodation.",
                "Rods give color vision. False: rods are achromatic; cones give color.",
                "Students think the blind spot is at the center of vision. It is offset; you do "
                "not notice it because the brain fills in the missing region."
            ],
            "order": (
                "Light path through the eye, then accommodation, then photoreceptor types and "
                "distribution, then the basics of phototransduction."
            ),
            "self_test": [
                "What structure does most of the eye's fixed refraction?",
                "Why is night vision mostly black and white?",
                "Why is there a blind spot and where is it?"
            ]
        },
        "clinical": (
            "Cataracts cloud the lens (often from oxidative stress with age); surgery replaces the "
            "lens with a synthetic one. Glaucoma raises intraocular pressure (failure of aqueous "
            "humor drainage) and damages the optic nerve; nurses screen for this in older patients. "
            "Macular degeneration destroys the fovea, robbing central vision but sparing peripheral. "
            "Diabetic retinopathy damages retinal vessels and is a leading cause of blindness. "
            "Color blindness is usually an X-linked recessive disorder of cone opsins (mostly "
            "affecting males). Visual symptoms in any patient should prompt thinking about which "
            "anatomical level is failing."
        )
    },

    "t-hearing-equilibrium": {
        "science": (
            "Sound path: pinna and external auditory canal funnel sound to the tympanic membrane. "
            "Vibration of the tympanic membrane moves the malleus, then the incus, then the stapes. "
            "The stapes pushes on the oval window, sending pressure waves into the perilymph of "
            "the cochlea."
            "\n\n"
            "In the cochlea, the basilar membrane vibrates, with different frequencies producing "
            "maximum vibration at different positions (tonotopy: high frequencies at the base, "
            "low frequencies at the apex). Hair cells in the organ of Corti have stereocilia that "
            "bend with basilar membrane motion. Bending opens mechanically gated K channels; the "
            "hair cell depolarizes; it releases glutamate onto CN VIII (the vestibulocochlear "
            "nerve), which carries the signal to the auditory cortex."
            "\n\n"
            "Equilibrium: the vestibule (utricle and saccule) detects linear acceleration and head "
            "tilt via otolith organs. The three semicircular canals detect rotational acceleration. "
            "All use hair cells with stereocilia in gel; head motion shears the gel and bends the "
            "cilia. Vestibular signals travel with auditory signals on CN VIII to the brainstem and "
            "cerebellum."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the ear in cross-section: outer, middle, inner; tympanic "
                "membrane, ossicles, cochlea, semicircular canals. Then label them."
            ),
            "misconceptions": [
                "Students think hearing happens in the cochlea entirely. It begins at the tympanic "
                "membrane and ends in the auditory cortex.",
                "All hearing loss is the same. Conductive loss (middle ear) is different from "
                "sensorineural loss (cochlea or nerve).",
                "Vertigo from inner ear problems is sometimes confused with light-headedness "
                "from low blood pressure. Vertigo is true spinning; light-headedness is not."
            ],
            "order": (
                "Sound path mechanically, then cochlear transduction (tonotopy), then equilibrium "
                "as a parallel hair-cell system."
            ),
            "self_test": [
                "Name the three middle ear ossicles in order.",
                "Where in the cochlea are high frequencies detected?",
                "Which structures detect rotational versus linear acceleration?"
            ]
        },
        "clinical": (
            "Otitis media (middle ear infection) is the most common reason a child sees a doctor; "
            "fluid behind the tympanic membrane produces conductive hearing loss. Presbycusis "
            "(age-related sensorineural hearing loss) starts with high frequencies (hair cells at "
            "the cochlear base) and progresses. Benign paroxysmal positional vertigo (BPPV) is "
            "loose otoconia drifting into a semicircular canal; head movements trigger spinning "
            "vertigo. Meniere disease is endolymph dysregulation in the inner ear, producing "
            "episodic vertigo, fluctuating hearing loss, and tinnitus. Aminoglycoside antibiotics "
            "(gentamicin) are ototoxic; nurses monitor hearing carefully during long courses."
        )
    },

    # ============================================================
    # MODULE 10: ENDOCRINE
    # ============================================================

    "t-hormone-mechanisms": {
        "science": (
            "Hormones are signaling molecules released into the blood by endocrine glands. Three "
            "chemical classes, two mechanisms."
            "\n\n"
            "Lipid-soluble hormones (steroids from cholesterol: cortisol, aldosterone, sex steroids; "
            "thyroid hormone): cross the plasma membrane, bind intracellular receptors, act as "
            "transcription factors. Effects are slow (hours to days) and long-lasting because they "
            "change which proteins the cell is making. Water-soluble hormones (peptides like "
            "insulin, growth hormone, ADH; catecholamines like epinephrine): cannot cross the "
            "membrane, bind cell-surface receptors, trigger intracellular second messenger cascades "
            "(cAMP, IP3/DAG, Ca). Effects are fast (seconds to minutes) and transient."
            "\n\n"
            "Feedback: almost every endocrine axis uses long-loop negative feedback. The end-product "
            "hormone suppresses the hypothalamus and pituitary that produced the upstream releasing "
            "and stimulating hormones. Cortisol suppresses CRH and ACTH. Thyroid hormone suppresses "
            "TRH and TSH. Disease often manifests when feedback is broken: primary failure (gland "
            "itself broken; downstream hormone low, upstream high because no negative feedback), "
            "secondary failure (pituitary broken; both upstream and downstream low), tertiary "
            "failure (hypothalamus broken). Pattern recognition here is high-yield."
        ),
        "teaching": {
            "before_video": (
                "Have students sketch the hypothalamus-pituitary-target gland axis as a feedback "
                "loop. Where does the end-hormone send its negative feedback signal?"
            ),
            "misconceptions": [
                "Students think hormones act on every cell. They act only on cells that have the "
                "right receptor.",
                "Steroid versus peptide mechanism is sometimes blurred. Steroids = intracellular "
                "receptor + transcription. Peptides = surface receptor + second messenger.",
                "Negative feedback in endocrine systems is sometimes thought to be optional. It is "
                "the default; positive feedback is the rare exception (LH surge before ovulation)."
            ],
            "order": (
                "Three chemical classes, then two mechanisms, then feedback patterns and the "
                "primary/secondary/tertiary failure logic."
            ),
            "self_test": [
                "Where are steroid hormone receptors located?",
                "Why must insulin be injected and not swallowed?",
                "What does it mean when a patient has high ACTH and low cortisol?"
            ]
        },
        "clinical": (
            "Primary hypothyroidism (Hashimoto): low T4, high TSH. Secondary hypothyroidism "
            "(pituitary failure): low T4, low TSH. Same low T4, different cause. Cushing syndrome: "
            "high cortisol producing hyperglycemia, central obesity, immunosuppression, "
            "hypertension. Addison disease: primary adrenal failure with low cortisol, high ACTH, "
            "skin hyperpigmentation. Diabetes insipidus: low ADH, dilute high-volume urine. SIADH: "
            "high ADH, concentrated low-volume urine, dilutional hyponatremia. Every one of these "
            "stories is a hormone level plus a feedback consequence."
        )
    },

    "t-major-glands": {
        "science": (
            "The pituitary is the master, but the hypothalamus is its boss. The hypothalamus "
            "releases small peptides (CRH, TRH, GnRH, GHRH, etc.) that travel via a tiny portal "
            "system to the anterior pituitary, which then releases the trophic hormones: ACTH, TSH, "
            "FSH, LH, GH, prolactin. The posterior pituitary stores and releases ADH and oxytocin "
            "made in the hypothalamus."
            "\n\n"
            "Thyroid: T3 and T4 set metabolic rate; calcitonin lowers blood calcium (modest in "
            "adults). Parathyroids (four small glands posterior to the thyroid) release PTH, which "
            "raises blood calcium by osteoclast activation, renal calcium retention, and vitamin D "
            "activation. Adrenal cortex (three zones, top to bottom): zona glomerulosa makes "
            "aldosterone (Na retention), zona fasciculata makes cortisol (stress and metabolism), "
            "zona reticularis makes androgens. Adrenal medulla makes epinephrine and norepinephrine "
            "(sympathetic effector)."
            "\n\n"
            "Pancreas islets: alpha cells make glucagon (raises blood glucose), beta cells make "
            "insulin (lowers blood glucose), delta cells make somatostatin (regulator). Gonads: "
            "testes make testosterone; ovaries make estrogen and progesterone. Each gland is a "
            "story; pair each hormone with its main job in one sentence and students can build a "
            "matrix they will use for the rest of healthcare."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a body outline and place every major endocrine gland with one "
                "hormone and one job per gland. They have to commit before the video."
            ),
            "misconceptions": [
                "Students confuse hypothalamus and pituitary. Hypothalamus is the upstream "
                "controller; pituitary is the executive that fires hormones into the blood.",
                "ADH and oxytocin are sometimes confused. ADH = water retention; oxytocin = labor, "
                "milk letdown, social bonding.",
                "The adrenal cortex and medulla are different tissues with different embryonic "
                "origins, despite sharing one capsule."
            ],
            "order": (
                "Hypothalamus-pituitary axis, then thyroid/parathyroid, then adrenals, then "
                "pancreas, then gonads."
            ),
            "self_test": [
                "Name the gland that makes ADH and where it is released.",
                "What three things does PTH do to raise blood calcium?",
                "Which adrenal zone makes aldosterone and what does aldosterone do?"
            ]
        },
        "clinical": (
            "Type 1 diabetes: autoimmune destruction of pancreatic beta cells; no insulin; "
            "hyperglycemia, ketoacidosis without exogenous insulin. Type 2 diabetes: insulin "
            "resistance plus eventual beta cell failure. Hyperthyroidism (Graves): heat intolerance, "
            "weight loss, tremor, palpitations. Hypothyroidism: cold intolerance, weight gain, "
            "fatigue, bradycardia. Pheochromocytoma: a catecholamine-secreting adrenal tumor "
            "producing episodic hypertension, headache, sweating, palpitations. Hyperparathyroidism: "
            "high calcium producing kidney stones, bone loss, neuropsychiatric symptoms. Each gland "
            "has its overproduction and underproduction story; nurses need both for any patient "
            "with endocrine symptoms."
        )
    },

    # ============================================================
    # MODULE 11: BLOOD
    # ============================================================

    "t-blood-composition": {
        "science": (
            "Blood is connective tissue: cells in a liquid matrix (plasma). About 55% plasma, 45% "
            "formed elements by volume. Plasma is mostly water plus proteins (albumin maintains "
            "oncotic pressure; globulins include antibodies; fibrinogen makes fibrin for clots), "
            "electrolytes, glucose, hormones, and wastes."
            "\n\n"
            "Formed elements: erythrocytes (RBCs, 99% of cells; biconcave, no nucleus, packed with "
            "hemoglobin, 120-day lifespan, function = O2/CO2 transport). Leukocytes (WBCs, immune "
            "cells). Platelets (cell fragments from megakaryocytes; central to hemostasis)."
            "\n\n"
            "WBC types: granulocytes (neutrophils, eosinophils, basophils, granular cytoplasm) and "
            "agranulocytes (lymphocytes, monocytes). Neutrophils are the most abundant; first "
            "responders to bacterial infection. Eosinophils target parasites and allergic responses. "
            "Basophils release histamine in inflammation. Lymphocytes (B and T) drive adaptive "
            "immunity. Monocytes leave blood and mature into tissue macrophages."
            "\n\n"
            "Hematopoiesis: all blood cells come from hematopoietic stem cells in red marrow (axial "
            "skeleton and proximal limb bones in adults). Erythropoiesis (RBC production) is "
            "driven by erythropoietin, made by the kidneys in response to low oxygen. Low EPO "
            "(chronic kidney disease) = anemia."
        ),
        "teaching": {
            "before_video": (
                "Ask students to predict the percentages of plasma vs cells, and to list the five "
                "kinds of WBC in order of abundance. They have to commit first."
            ),
            "misconceptions": [
                "Students think blood is just RBCs. By cell count yes, but by function the WBCs "
                "and platelets are equally critical.",
                "Blood is sometimes described as 'red liquid.' It is a connective tissue with a "
                "specific cell-to-matrix structure.",
                "RBCs without a nucleus seems like a disability. It is a specialization: more "
                "room for hemoglobin, more flexible to squeeze through capillaries."
            ],
            "order": (
                "Plasma vs formed elements, then RBC specifics, then WBC types and roles, then "
                "platelets briefly, then hematopoiesis."
            ),
            "self_test": [
                "What percentage of blood is plasma?",
                "Name the WBC types from most to least abundant.",
                "Why are patients with chronic kidney disease anemic?"
            ]
        },
        "clinical": (
            "CBC (complete blood count) is the most common lab test. Low hemoglobin = anemia "
            "(many causes: iron deficiency, B12, chronic disease, blood loss). High WBC = "
            "infection or leukemia. Low platelets = bleeding risk. The differential (percentages "
            "of each WBC type) tells you what kind of infection: bacterial typically raises "
            "neutrophils; viral often raises lymphocytes; parasites raise eosinophils. Patients on "
            "chemotherapy have predictable cytopenias from bone marrow suppression; nurses time "
            "their assessments and protective measures accordingly. Recombinant EPO is given to "
            "dialysis patients to treat anemia of CKD."
        )
    },

    "t-hemostasis-blood-typing": {
        "science": (
            "Three phases of hemostasis: vascular spasm (damaged vessel constricts), platelet plug "
            "formation (platelets adhere to exposed collagen via von Willebrand factor, activate, "
            "and recruit more platelets), and coagulation (the clotting cascade ends in fibrin, "
            "which reinforces the plug). The cascade has intrinsic and extrinsic pathways that "
            "converge on a common pathway producing thrombin, which converts fibrinogen to fibrin."
            "\n\n"
            "ABO typing: RBCs may carry A antigen, B antigen, both, or neither (Type O). Plasma "
            "carries antibodies against absent antigens (Type A has anti-B; Type O has both; Type "
            "AB has neither). Type O is the universal RBC donor (no antigens to trigger recipient "
            "antibodies); Type AB is the universal RBC recipient (no antibodies to attack donor "
            "RBCs). For plasma, the rule reverses: AB is the universal plasma donor."
            "\n\n"
            "Rh factor: Rh+ means D antigen present. Anti-Rh antibodies form only after exposure. "
            "Critical in pregnancy: an Rh- mother carrying an Rh+ fetus may produce anti-Rh "
            "antibodies, which can cross the placenta in a future pregnancy and attack an Rh+ "
            "fetus, producing hemolytic disease of the newborn. RhoGAM (anti-Rh antibody given to "
            "the mother) prevents this by clearing fetal Rh+ cells before her immune system "
            "responds."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the three phases of hemostasis as a flowchart and predict "
                "what a missing platelet plug, or missing fibrin, would mean."
            ),
            "misconceptions": [
                "Students think clotting and clot dissolution are separate things. They are "
                "balanced: fibrinolysis is happening alongside coagulation; the net result is the "
                "lifespan of the clot.",
                "ABO and Rh are sometimes mixed. ABO antibodies are pre-formed (natural); Rh "
                "antibodies form only after exposure.",
                "Type O is universal donor for RBCs, NOT for plasma."
            ],
            "order": (
                "Three phases of hemostasis, then ABO logic, then Rh logic with the pregnancy "
                "implication."
            ),
            "self_test": [
                "Name the three phases of hemostasis.",
                "Which is the universal RBC donor and which is the universal plasma donor?",
                "Why are Rh- women given RhoGAM during pregnancy?"
            ]
        },
        "clinical": (
            "Hemophilia A and B (clotting factor deficiencies) produce delayed bleeding into joints "
            "and tissue. Von Willebrand disease (the most common inherited bleeding disorder) "
            "produces mucocutaneous bleeding. Warfarin inhibits vitamin-K-dependent clotting "
            "factors and is used to prevent stroke in atrial fibrillation; the trade-off is "
            "bleeding risk, which is monitored with INR. Heparin inhibits thrombin and is used "
            "for acute anticoagulation. Transfusion reactions occur when ABO mismatch happens "
            "(recipient antibodies attack donor RBCs); hemolysis can be rapidly fatal, hence the "
            "two-nurse identity check at the bedside. Liver disease produces coagulopathy because "
            "the liver makes most clotting factors."
        )
    },

    # ============================================================
    # MODULE 12: CARDIOVASCULAR
    # ============================================================

    "t-heart-cardiac-cycle": {
        "science": (
            "The heart has four chambers and four valves. Right side carries deoxygenated blood: "
            "vena cavae into right atrium (RA) through tricuspid valve into right ventricle (RV), "
            "through pulmonary valve into pulmonary trunk and lungs. Left side carries oxygenated "
            "blood: pulmonary veins into left atrium (LA), through mitral (bicuspid) valve into "
            "left ventricle (LV), through aortic valve into aorta. The two sides are functionally "
            "in series."
            "\n\n"
            "The cardiac cycle has four phases (one beat = one cycle): ventricular filling "
            "(AV valves open, blood drops in passively, then atrial systole tops it off), "
            "isovolumetric contraction (all valves closed, pressure rises in the ventricles), "
            "ventricular ejection (semilunar valves open, blood is ejected), isovolumetric "
            "relaxation (all valves closed, pressure falls). The cycle then restarts."
            "\n\n"
            "Heart sounds: S1 ('lub') is the closure of the AV valves at the start of systole. "
            "S2 ('dub') is the closure of the semilunar valves at the end of systole. S3 (early "
            "diastolic gallop) can be normal in young athletes or pathologic in heart failure. S4 "
            "(late diastolic) is often pathologic, reflecting a stiff ventricle. Murmurs are "
            "audible turbulence; the timing in the cycle and where they are loudest tell you which "
            "valve is malfunctioning."
            "\n\n"
            "Frank-Starling mechanism: within the working range, the more the ventricle is "
            "stretched by incoming blood (preload), the more forcefully it contracts on the next "
            "beat. The heart pumps out what it receives. This is the basis of moment-to-moment "
            "matching of cardiac output to venous return."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the heart in cross-section, label all four chambers and four "
                "valves, and trace the path of a red blood cell from vena cava to aorta."
            ),
            "misconceptions": [
                "Students think the heart is one pump. It is two pumps in series.",
                "S1 and S2 are sometimes mixed. Cue: S1 (lub) is louder and longer (AV valves "
                "shutting against ventricular pressure); S2 (dub) is sharper.",
                "Frank-Starling is sometimes thought of as a feedback loop. It is a structural "
                "property of muscle, not a regulatory loop."
            ],
            "order": (
                "Anatomy and blood flow, then valves and the cardiac cycle phases, then heart "
                "sounds, then Frank-Starling as the integrating concept."
            ),
            "self_test": [
                "Trace blood from the inferior vena cava to the aorta, naming every chamber and "
                "valve.",
                "Which valves close at S1? Which at S2?",
                "What is happening during isovolumetric contraction?"
            ]
        },
        "clinical": (
            "Mitral regurgitation: blood leaks back into the LA during systole; forward cardiac "
            "output drops; chronic volume overload dilates the LV. Aortic stenosis: narrowed valve "
            "raises the pressure the LV must generate; chronic pressure overload causes concentric "
            "LV hypertrophy. Heart failure with reduced ejection fraction (HFrEF): the LV ejects "
            "less than 40% per beat; backward congestion produces pulmonary edema; forward "
            "underperfusion produces fatigue and renal dysfunction. Cardiac tamponade: fluid in "
            "the pericardial sac compresses the heart, dropping preload and cardiac output; this "
            "is a true emergency. Nurses monitor for the early signs (rising JVP, dropping BP, "
            "muffled heart sounds: Beck's triad). Every patient with a murmur deserves a careful "
            "reading of timing and location."
        )
    },

    "t-conduction-ecg": {
        "science": (
            "The heart paces itself. The sinoatrial (SA) node sits in the right atrial wall and fires "
            "60-100 times per minute at rest. From there, the impulse spreads through atrial "
            "myocardium, hits the atrioventricular (AV) node, and is deliberately held there for "
            "about 100 milliseconds. That delay is the load-bearing concept: it lets the atria "
            "finish contracting and emptying before the ventricles fire. Without it, atria and "
            "ventricles would contract simultaneously, ventricular filling would collapse, and "
            "stroke volume would crash."
            "\n\n"
            "After the AV delay, the signal races through the Bundle of His, down the right and "
            "left bundle branches, and out into the Purkinje fibers, which distribute it almost "
            "simultaneously to the entire ventricular myocardium. That speed is essential: "
            "ventricles need to contract as a coordinated unit to eject effectively. Slow or "
            "uneven spread produces inefficient pumping."
            "\n\n"
            "For essentials scope, you do not have to teach ECG wave-by-wave interpretation. The "
            "core concept is the pathway and the timing. Mention arrhythmias as a category "
            "(AV block, atrial fibrillation, ventricular fibrillation) so students recognize the "
            "vocabulary, but you do not need them reading rhythm strips."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the heart and trace the conduction pathway with arrows from "
                "SA to ventricular myocardium. They commit before the video confirms the route."
            ),
            "misconceptions": [
                "Students think the AV node speeds the signal up. It deliberately slows it; the delay "
                "is the entire point.",
                "The conduction system is sometimes confused with the coronary arteries. Conduction "
                "is electrical (myocardial cells specialized for fast conduction); arteries are "
                "the blood supply.",
                "Ventricular fibrillation is sometimes thought to be a fast heart rate. It is "
                "chaotic activity with no coordinated contraction at all; the ventricles quiver."
            ],
            "order": (
                "Pacemaker (SA node) → AV delay (why it matters) → fast ventricular spread "
                "(Bundle of His, Purkinje) → coordinated ejection. Add arrhythmias as failure modes "
                "of each step."
            ),
            "self_test": [
                "Without notes, draw the conduction pathway in order.",
                "Why is the AV nodal delay necessary?",
                "Why is rapid Purkinje conduction important for effective ejection?"
            ]
        },
        "clinical": (
            "Atrial fibrillation is the most common sustained arrhythmia and a major stroke risk: "
            "stagnant blood in the fibrillating atrium can clot and embolize to the brain. "
            "Anticoagulation (warfarin or a DOAC) is standard. AV blocks (especially third-degree) "
            "drop cardiac output because atrial and ventricular contractions decouple; pacemakers "
            "restore coordination. Ventricular fibrillation is the cardiac-arrest rhythm that "
            "responds to defibrillation, which is why AEDs are everywhere. Every nurse on a "
            "telemetry floor is watching this pathway in real time."
        )
    },

    "t-vessels-hemodynamics": {
        "science": (
            "Blood vessels are a structural and functional gradient. Arteries are thick-walled and "
            "elastic, carrying blood under high pressure. Arterioles are smaller and heavily "
            "muscled; they are the primary site of vascular resistance. Capillaries are single-"
            "endothelial-layer tubes where exchange happens. Venules and veins are thin-walled "
            "with valves; they hold most of the blood volume (capacitance vessels)."
            "\n\n"
            "Blood pressure equation: BP = cardiac output (CO) x total peripheral resistance (TPR). "
            "Cardiac output equation: CO = stroke volume (SV) x heart rate (HR). Stroke volume is "
            "set by preload, contractility, and afterload. Total peripheral resistance is dominated "
            "by arteriolar diameter. Mean arterial pressure (MAP) is the perfusion pressure that "
            "matters to tissues; you want it roughly 65 or above."
            "\n\n"
            "Regulation: short-term, the baroreflex (carotid sinus and aortic arch baroreceptors "
            "to medullary cardiovascular centers) adjusts HR and vascular tone within seconds. "
            "Long-term, the kidneys via RAAS (renin-angiotensin-aldosterone) and ANP regulate "
            "blood volume. Both axes are clinical workhorses."
        ),
        "teaching": {
            "before_video": (
                "Have students predict what happens to BP if (a) arterioles vasoconstrict, "
                "(b) HR doubles, (c) plasma volume drops. Then they have to commit before checking."
            ),
            "misconceptions": [
                "Students think 'high BP' just means HR is fast. It can also mean high resistance, "
                "high volume, high contractility.",
                "Veins are sometimes called 'low-pressure arteries.' They have different "
                "structure: thin walls, valves, more compliant.",
                "Capillaries are thought of as small arteries. They are unique: single layer, no "
                "muscle, designed for exchange."
            ],
            "order": (
                "Vessel types, then the BP equation and components, then short-term and long-term "
                "regulation."
            ),
            "self_test": [
                "Where in the circulation is the primary site of resistance?",
                "Write the equations for cardiac output and blood pressure.",
                "Why do veins have valves?"
            ]
        },
        "clinical": (
            "Hypertension is the most common chronic disease in adults. Treatments target each "
            "node of the BP equation: diuretics drop volume (and therefore CO), beta blockers "
            "drop HR and contractility, calcium channel blockers drop contractility and "
            "vasodilate, ACE inhibitors drop RAAS-driven vasoconstriction and volume retention. "
            "Hypovolemic shock from blood loss produces tachycardia (baroreflex compensation) "
            "and vasoconstriction; nurses watch for these as the warning signs before BP itself "
            "collapses. Orthostatic hypotension (BP drops when standing) reflects autonomic or "
            "volume problems and is a fall risk in the elderly."
        )
    },

    # ============================================================
    # MODULE 13: LYMPHATIC AND IMMUNE
    # ============================================================

    "t-lymphatic-innate": {
        "science": (
            "The lymphatic system returns interstitial fluid to the blood (about 3 L per day) and "
            "filters that fluid through lymph nodes for immune surveillance. Lymph vessels parallel "
            "the venous system. Major lymphoid organs: lymph nodes (filter lymph), spleen (filters "
            "blood), thymus (T cell maturation), tonsils, and MALT (mucosa-associated lymphoid "
            "tissue scattered along the gut, airway, etc.)."
            "\n\n"
            "Innate immunity is the body's general (non-specific) defense and is the first line. "
            "Surface barriers: skin (stratified squamous keratinized), mucous membranes (with "
            "antimicrobial peptides and IgA), low stomach pH, ciliated airway. If something gets "
            "past, innate cells respond: neutrophils (first responders, eat bacteria), macrophages "
            "(eat and recruit), natural killer cells (kill virus-infected and tumor cells without "
            "prior exposure). The complement system is a cascade of plasma proteins that lyse "
            "pathogens and mark them for phagocytosis. Interferons are antiviral cytokines."
            "\n\n"
            "Inflammation: the response to tissue damage or infection. Vasodilation and increased "
            "vascular permeability deliver immune cells and plasma proteins to the site. Cardinal "
            "signs: redness (rubor), heat (calor), swelling (tumor), pain (dolor), loss of "
            "function. Chemotaxis recruits more cells. Inflammation is necessary but can cause "
            "tissue damage if uncontrolled."
        ),
        "teaching": {
            "before_video": (
                "Have students sketch the path of interstitial fluid into a lymphatic capillary, "
                "through a lymph node, and back to the blood. Then list the five cardinal signs "
                "of inflammation."
            ),
            "misconceptions": [
                "Students confuse the lymphatic and the cardiovascular systems. They are parallel "
                "but separate; lymph empties into the venous system at the subclavian veins.",
                "Innate immunity is sometimes dismissed as primitive. It handles 99% of insults "
                "without you noticing.",
                "Inflammation is seen as pathological. It is the body's defense; chronic or "
                "uncontrolled inflammation is the pathology."
            ],
            "order": (
                "Lymphatic anatomy and function, then innate immunity layers (barriers, cells, "
                "complement), then inflammation as the visible result."
            ),
            "self_test": [
                "Name the four cardinal signs of inflammation.",
                "Name two phagocytic cells.",
                "Why do asplenic patients need extra vaccines and antibiotic precautions?"
            ]
        },
        "clinical": (
            "Lymphedema (often after lymph node dissection for breast cancer surgery, or from "
            "filariasis) is the failure of lymph drainage; the affected limb swells permanently. "
            "Splenectomy patients are at high risk of overwhelming infection from encapsulated "
            "organisms (Strep pneumoniae, H. influenzae, N. meningitidis); they receive specific "
            "vaccines. Sepsis is uncontrolled systemic inflammation in response to infection; "
            "early recognition (SIRS criteria, qSOFA, lactate) is critical for survival. Allergies "
            "and anaphylaxis involve inappropriate or excessive innate (and adaptive) responses. "
            "Nurses caring for any patient with infection are watching for the transition from "
            "local to systemic inflammatory response."
        )
    },

    "t-adaptive-immunity": {
        "science": (
            "Adaptive immunity has two defining features: specificity (each lymphocyte recognizes "
            "one antigen) and memory (re-exposure produces a faster, larger response). It comes in "
            "two arms."
            "\n\n"
            "Humoral immunity: B cells, when activated, become plasma cells that produce "
            "antibodies. Antibodies (IgG, IgM, IgA, IgE, IgD) circulate and tag extracellular "
            "pathogens for destruction by neutralization, opsonization, complement activation, or "
            "antibody-dependent cell killing (ADCC). This is your primary defense against "
            "circulating bacteria, toxins, and viruses outside cells."
            "\n\n"
            "Cell-mediated immunity: T cells, in two main flavors. Helper T cells (CD4) coordinate "
            "the response by activating B cells, cytotoxic T cells, and macrophages. Cytotoxic T "
            "cells (CD8) directly kill infected or abnormal cells. T cells need antigen presented "
            "on MHC molecules: MHC class I (on all nucleated cells, presents intracellular "
            "peptides to CD8) or MHC class II (on antigen-presenting cells, presents extracellular "
            "peptides to CD4)."
            "\n\n"
            "Activation requires two signals: antigen plus co-stimulation. This two-key rule "
            "prevents autoimmunity (a lymphocyte that binds self-antigen without co-stimulation "
            "is suppressed or killed). Clonal expansion produces effector cells (do the job) and "
            "memory cells (live for years, respond fast on re-exposure). Vaccination relies "
            "entirely on memory."
        ),
        "teaching": {
            "before_video": (
                "Have students predict: which arm of adaptive immunity is best at killing virus-"
                "infected cells versus extracellular bacteria? Then they have to commit."
            ),
            "misconceptions": [
                "Students think innate and adaptive immunity work in series. They cooperate "
                "constantly; innate cells present antigen and drive adaptive responses.",
                "Antibodies are sometimes thought to kill pathogens directly. They tag, neutralize, "
                "or recruit; killing is usually by complement or phagocytes.",
                "Vaccines are sometimes thought to give you the disease. They give you the antigen "
                "without the pathogen; your memory cells will respond if you ever encounter the "
                "real one."
            ],
            "order": (
                "Definition and features (specificity, memory), then humoral arm with antibody "
                "functions, then cell-mediated arm with MHC presentation, then activation rules "
                "and memory."
            ),
            "self_test": [
                "Which T cell subset directly kills infected cells?",
                "Which MHC class presents to CD4 T cells?",
                "Why are vaccinated people protected even though they have never had the disease?"
            ]
        },
        "clinical": (
            "HIV destroys CD4 T cells; without coordination, both humoral and cell-mediated "
            "immunity collapse, and patients develop opportunistic infections. Transplant patients "
            "receive immunosuppression to prevent T cell rejection of the graft; the trade-off is "
            "infection and cancer risk. Autoimmune diseases (lupus, rheumatoid arthritis, type 1 "
            "diabetes, MS, Hashimoto, Graves) reflect loss of self-tolerance. Vaccination has "
            "transformed pediatric mortality. Monoclonal antibody therapies (mAbs ending in -mab) "
            "target specific receptors or pathogens. Every patient with infection, autoimmunity, "
            "or immunodeficiency is a story about the adaptive immune system functioning, failing, "
            "or overshooting."
        )
    },

    # ============================================================
    # MODULE 14: RESPIRATORY
    # ============================================================

    "t-resp-anatomy-mechanics": {
        "science": (
            "Two zones. Conducting zone: nose, pharynx, larynx, trachea, bronchi, bronchioles. "
            "Warms, humidifies, filters. No gas exchange happens here. Respiratory zone: respiratory "
            "bronchioles, alveolar ducts, alveoli. Gas exchange happens here. The alveoli are "
            "simple squamous (Type I pneumocytes) with surfactant from Type II pneumocytes."
            "\n\n"
            "Pleura: parietal pleura lines the thoracic cavity; visceral pleura covers the lung. "
            "Between them is a tiny pleural cavity with serous fluid and (critically) negative "
            "pressure. The negative pressure couples the lung to the chest wall: as the chest wall "
            "expands during inspiration, the lung is pulled outward with it. Lose the negative "
            "pressure (pneumothorax) and the lung collapses elastically."
            "\n\n"
            "Mechanics: Boyle's law. Pressure and volume vary inversely at constant temperature. "
            "Inspiration: diaphragm contracts (pulls down) and external intercostals lift the rib "
            "cage; thoracic volume rises; alveolar pressure drops below atmospheric; air flows in. "
            "Expiration at rest is passive: muscles relax, elastic recoil shrinks the thorax, "
            "alveolar pressure rises above atmospheric, air flows out. Forced expiration adds "
            "internal intercostals and abdominal muscles."
        ),
        "teaching": {
            "before_video": (
                "Have students sketch the airway from mouth to alveolus, label conducting vs "
                "respiratory zone, and identify Type I and Type II pneumocytes at the alveolus."
            ),
            "misconceptions": [
                "Students think the lungs actively pull air in. Air is sucked in passively by "
                "the pressure gradient produced by the diaphragm and chest wall.",
                "Surfactant is thought of as optional. It is essential: without it, alveolar "
                "surface tension collapses the alveoli.",
                "Pleural pressure is sometimes assumed to equal atmospheric. It is normally slightly "
                "negative; that is what holds the lung expanded."
            ],
            "order": (
                "Anatomy and the two zones, then the pleura and the negative pressure rule, then "
                "Boyle's law and the mechanics of breathing."
            ),
            "self_test": [
                "What is the main muscle of inspiration?",
                "What does surfactant do?",
                "Why does a pneumothorax cause the lung to collapse?"
            ]
        },
        "clinical": (
            "Pneumothorax is air in the pleural cavity (from trauma, spontaneous rupture, or "
            "iatrogenic); the affected lung collapses; treatment is chest tube drainage to restore "
            "negative pressure. Pleural effusion is fluid in the pleural cavity (transudate from "
            "heart failure or hypoalbuminemia, exudate from infection or malignancy). Asthma "
            "is bronchospasm and airway inflammation, narrowing the conducting zone. COPD "
            "(emphysema and chronic bronchitis) destroys alveoli and obstructs airways. Neonatal "
            "respiratory distress syndrome is surfactant deficiency in premature infants; "
            "exogenous surfactant therapy is life-saving. Every breath in your patient is a "
            "Boyle's-law transaction."
        )
    },

    "t-gas-exchange-transport": {
        "science": (
            "Gas exchange happens by diffusion down partial pressure gradients. External "
            "respiration: between alveolar air and pulmonary capillary blood. Alveolar O2 is "
            "about 100 mmHg; pulmonary venous blood arrives at 40 mmHg; O2 diffuses into blood "
            "until equilibrium. CO2 goes the other way. Internal respiration: between systemic "
            "capillary blood and tissue. The gradients are reversed there."
            "\n\n"
            "Oxygen transport: about 98% bound to hemoglobin, 2% dissolved in plasma. Each Hb "
            "molecule binds 4 O2 cooperatively (the binding of one O2 increases affinity for the "
            "next). The Hb-O2 dissociation curve is sigmoidal. Conditions that shift it right "
            "(acidosis, high CO2, high temperature, high 2,3-BPG: the Bohr effect) cause Hb to "
            "release MORE O2 to tissues. This is why exercising muscle, which is acidic, hot, and "
            "high in CO2, gets extra oxygen automatically."
            "\n\n"
            "CO2 transport: about 70% as bicarbonate (the carbonic anhydrase reaction in RBCs: "
            "CO2 + H2O -> H2CO3 -> H+ + HCO3-), 20% bound to hemoglobin, 10% dissolved. The "
            "bicarbonate system is also the body's main blood buffer; respiratory rate adjusts CO2 "
            "and therefore pH on a minute-to-minute basis."
            "\n\n"
            "Control of ventilation: central chemoreceptors in the medulla respond to CSF pH (a "
            "proxy for arterial CO2). Peripheral chemoreceptors (carotid and aortic bodies) "
            "respond to severely low arterial O2 (typically below 60 mmHg). CO2 is the primary "
            "moment-to-moment driver. In chronic CO2 retainers (severe COPD), the central drive "
            "desensitizes and the patient relies on the hypoxic drive; high inspired O2 can blunt "
            "this and cause hypoventilation."
        ),
        "teaching": {
            "before_video": (
                "Have students predict: at exercising muscle, does Hb release more or less O2? "
                "Why? They have to commit before the Bohr effect is explained."
            ),
            "misconceptions": [
                "Students think dissolved O2 is the main carrier. No, 98% is on Hb. Dissolved O2 "
                "(measured as pO2) is just the part that determines Hb saturation.",
                "CO2 is thought to be transported mainly bound to Hb. No, mostly as bicarbonate.",
                "Students think low O2 is the main driver of breathing. It is not. CO2 (via pH "
                "of the CSF) is the primary minute-to-minute driver."
            ],
            "order": (
                "Where exchange happens (external vs internal), then O2 transport with the Bohr "
                "effect, then CO2 transport with the bicarbonate buffer, then control of "
                "ventilation."
            ),
            "self_test": [
                "What is the main form of CO2 transport in blood?",
                "What conditions shift the Hb-O2 curve to the right and what is the consequence?",
                "Why does CO poisoning cause hypoxia even though arterial pO2 is normal?"
            ]
        },
        "clinical": (
            "Carbon monoxide poisoning: CO binds Hb with 250x O2 affinity; oxygen-carrying "
            "capacity collapses, even though pO2 looks normal on blood gas. Pulse oximetry can be "
            "falsely normal; co-oximetry is required. Treatment is 100% O2 and, in severe cases, "
            "hyperbaric oxygen. Acute respiratory acidosis (CO2 retention from respiratory failure) "
            "produces falling pH; renal compensation takes days. Chronic respiratory acidosis "
            "(COPD) has compensated pH because the kidneys have retained HCO3- over time. Pulse "
            "oximetry, arterial blood gas interpretation, and supplemental O2 titration are core "
            "nursing skills that depend on this physiology."
        )
    },

    # ============================================================
    # MODULE 15: DIGESTIVE
    # ============================================================

    "t-gi-anatomy-motility": {
        "science": (
            "The GI tract is a single tube from mouth to anus, about 9 meters long. Path: mouth, "
            "pharynx, esophagus, stomach, small intestine (duodenum, jejunum, ileum), large "
            "intestine (cecum, ascending, transverse, descending, sigmoid colon), rectum, anus. "
            "Accessory organs (salivary glands, liver, gallbladder, pancreas) deliver enzymes "
            "and bile into the tube."
            "\n\n"
            "Wall layers (deep to superficial): mucosa (epithelium, lamina propria, muscularis "
            "mucosae), submucosa (vessels, submucosal/Meissner plexus), muscularis externa (inner "
            "circular and outer longitudinal smooth muscle layers with myenteric/Auerbach plexus "
            "between), serosa or adventitia. The two enteric nerve plexuses make up the enteric "
            "nervous system, sometimes called the 'second brain' for its independent function."
            "\n\n"
            "Motility comes in two flavors. Peristalsis: a wave of smooth muscle contraction that "
            "propels content forward. Segmentation: localized contractions that mix without net "
            "forward motion (small intestine). Sphincters divide the tract into functional "
            "compartments: lower esophageal (cardia), pyloric (stomach to duodenum), ileocecal "
            "(ileum to cecum), internal and external anal."
        ),
        "teaching": {
            "before_video": (
                "Have students trace the GI tract from mouth to anus, naming every segment in "
                "order, then label the major sphincters."
            ),
            "misconceptions": [
                "Students think the small intestine is small. It is small in diameter but very "
                "long (about 6 meters); the large intestine is shorter (about 1.5 m) but wider.",
                "Peristalsis and segmentation are sometimes mixed. Peristalsis moves food forward; "
                "segmentation mixes it in place.",
                "Sphincters are thought of as decorative. Each is functionally critical; failure "
                "produces specific clinical syndromes (achalasia, gastroparesis, anal incontinence)."
            ],
            "order": (
                "Organ sequence, then the wall layer structure (same throughout, with regional "
                "modifications), then motility and sphincters."
            ),
            "self_test": [
                "Name the three parts of the small intestine in order.",
                "What is the function of the pyloric sphincter?",
                "How does peristalsis differ from segmentation?"
            ]
        },
        "clinical": (
            "Achalasia: the lower esophageal sphincter cannot relax; food and liquid accumulate "
            "in the lower esophagus, producing dysphagia and regurgitation. Gastroparesis: "
            "delayed stomach emptying, often in diabetics from autonomic neuropathy. Small bowel "
            "obstruction: peristalsis pushes against a blockage, causing cramping, distension, "
            "vomiting. C. difficile colitis: pseudomembranous colon inflammation after antibiotics; "
            "severe diarrhea, electrolyte disturbance. Hirschsprung disease: absence of enteric "
            "plexus in part of the colon; obstruction in newborns. Every GI symptom should make "
            "you ask which segment is failing and how."
        )
    },

    "t-digestion-absorption": {
        "science": (
            "Each macromolecule has a digestion story. Carbohydrates: salivary amylase begins "
            "starch breakdown in the mouth (stops in the stomach because of acid). Pancreatic "
            "amylase resumes in the small intestine, producing disaccharides. Brush-border enzymes "
            "(maltase, sucrase, lactase) finish the job to monosaccharides, which are absorbed by "
            "SGLT1 (Na-glucose symporter) and GLUT2."
            "\n\n"
            "Proteins: pepsin in the stomach (activated from pepsinogen by acid) begins. Pancreatic "
            "proteases (trypsin, chymotrypsin, carboxypeptidase, activated by enterokinase in the "
            "duodenum) continue. Brush-border peptidases finish to amino acids and small peptides, "
            "absorbed by amino-acid transporters."
            "\n\n"
            "Lipids: bile (made by liver, stored in gallbladder, released into duodenum in "
            "response to CCK) emulsifies fats. Pancreatic lipase hydrolyzes triglycerides to "
            "monoglycerides and fatty acids. Products form micelles, diffuse into enterocytes, "
            "reassemble into chylomicrons, and enter lymph via lacteals. Fat-soluble vitamins "
            "(A, D, E, K) ride along."
            "\n\n"
            "Absorptive surface: plicae circulares (folds), villi (finger-like projections), "
            "microvilli (brush border). Together they multiply surface area roughly 600-fold "
            "compared to a smooth tube of the same length. Small intestine = absorption central. "
            "Large intestine reclaims water and electrolytes, ferments residual carbohydrates, "
            "and forms feces."
        ),
        "teaching": {
            "before_video": (
                "Have students predict where each macromolecule (carbs, proteins, fats) is digested "
                "and where it is absorbed. They have to commit first."
            ),
            "misconceptions": [
                "Students think the stomach does most of the digestion. The stomach starts protein "
                "digestion and stores food; the small intestine does the lion's share.",
                "Fats are thought to enter the blood like carbs and protein. They enter lymph "
                "first (chylomicrons via lacteals).",
                "Bile is sometimes confused with a digestive enzyme. It is not an enzyme; it is "
                "an emulsifier that lets enzymes (lipase) access the substrate."
            ],
            "order": (
                "Each macromolecule's digestion and absorption in turn, then the absorptive "
                "surface design as the unifying answer to 'how does so much get absorbed so fast.'"
            ),
            "self_test": [
                "Where is most absorption accomplished?",
                "What does bile do, and where does it come from?",
                "Why do fats enter lymph rather than blood directly?"
            ]
        },
        "clinical": (
            "Lactose intolerance: lactase deficiency; lactose is not digested, ferments in the "
            "colon, draws water in osmotically, causing gas and diarrhea. Celiac disease: gluten "
            "triggers autoimmune destruction of small intestinal villi; absorption fails; the "
            "patient develops nutritional deficiencies. Cystic fibrosis affects the pancreas: "
            "thick secretions block enzyme delivery, causing maldigestion. Cholecystectomy "
            "(gallbladder removal): bile flow continues but is no longer concentrated and stored; "
            "patients often tolerate small fatty meals but not large ones. Bariatric surgery alters "
            "absorption and digestion deliberately for weight loss; lifelong vitamin and protein "
            "monitoring is essential. GI complaints should prompt thinking about which step of "
            "digestion or absorption is failing."
        )
    },

    # ============================================================
    # MODULE 16: URINARY
    # ============================================================

    "t-kidney-filtration": {
        "science": (
            "The kidney's gross anatomy is layered: outer cortex, inner medulla (with renal "
            "pyramids), drain to the renal pelvis to the ureter. Each kidney has about a million "
            "nephrons. Blood path: renal artery to interlobar arteries to arcuate to interlobular "
            "to afferent arteriole into the glomerulus, then efferent arteriole out, then "
            "peritubular capillaries (or vasa recta for juxtamedullary nephrons), and venous "
            "return."
            "\n\n"
            "The nephron is the functional unit. It has the renal corpuscle (glomerulus surrounded "
            "by Bowman's capsule) and the tubule (proximal convoluted tubule, loop of Henle, "
            "distal convoluted tubule, collecting duct). Cortical nephrons (85%) have short loops "
            "of Henle. Juxtamedullary nephrons (15%) have long loops that dip deep into the medulla "
            "and produce the concentration gradient that allows the kidney to make concentrated "
            "urine."
            "\n\n"
            "Filtration: the filtration barrier has three layers (fenestrated capillary endothelium, "
            "basement membrane, podocyte slit diaphragms). Cells and large proteins are excluded; "
            "water, ions, glucose, amino acids, and small molecules pass freely. GFR (glomerular "
            "filtration rate) is about 125 mL/min, or 180 L per day. Of that, less than 1% becomes "
            "urine; the rest is reabsorbed. GFR is autoregulated by myogenic response (afferent "
            "arteriole constricts in response to stretch) and tubuloglomerular feedback (macula "
            "densa senses tubular flow)."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a nephron with all its tubular segments and the vascular "
                "supply, then label the filtration barrier."
            ),
            "misconceptions": [
                "Students think the kidney just makes urine. It also regulates BP (RAAS), acid-"
                "base balance, calcium, EPO production, vitamin D activation.",
                "Glomerular filtrate is sometimes confused with urine. Filtrate is roughly the "
                "composition of plasma minus proteins; urine is what is left after reabsorption.",
                "Tubular handling is thought of as passive. Most is active and tightly regulated."
            ],
            "order": (
                "Gross anatomy, then the nephron structure, then the filtration barrier and GFR, "
                "then autoregulation."
            ),
            "self_test": [
                "What is the typical GFR?",
                "Name the three layers of the glomerular filtration barrier.",
                "How does the kidney maintain a stable GFR despite changes in BP?"
            ]
        },
        "clinical": (
            "Proteinuria suggests damage to the filtration barrier (often at the podocyte slit "
            "diaphragm in nephrotic syndrome). Hematuria can mean glomerular (RBC casts on "
            "urinalysis) or post-glomerular (stones, infection) bleeding. Acute kidney injury "
            "(AKI) can be prerenal (poor perfusion), intrinsic (the kidney tissue is damaged), or "
            "postrenal (obstruction). Chronic kidney disease (CKD) stages are based on GFR; "
            "treatment escalates from medical management to dialysis to transplant. Every patient "
            "with deranged labs (creatinine, BUN, electrolytes, acid-base) deserves a kidney-"
            "centric reading."
        )
    },

    "t-tubular-function": {
        "science": (
            "The tubule reshapes the filtrate. Each segment has characteristic transport biology, "
            "and each is a drug target."
            "\n\n"
            "Proximal convoluted tubule (PCT): bulk reabsorption. About 65% of filtered Na, water, "
            "glucose, amino acids, and bicarbonate are reabsorbed here. Glucose has a tubular "
            "maximum (Tm); above blood glucose of about 180 mg/dL the transporters saturate and "
            "glucose spills into urine (glucosuria of diabetes). Loop of Henle: descending limb is "
            "permeable to water but not ions (water leaves, filtrate concentrates); thick "
            "ascending limb is impermeable to water but actively reabsorbs Na, K, 2Cl via the "
            "NKCC2 cotransporter (target of loop diuretics like furosemide). Net effect: a "
            "hypertonic medullary interstitium (the countercurrent multiplier)."
            "\n\n"
            "Distal convoluted tubule (DCT): reabsorbs Na and Cl via the NCC cotransporter "
            "(target of thiazide diuretics). Late DCT and collecting duct: principal cells under "
            "aldosterone control reabsorb Na and secrete K (target of potassium-sparing diuretics "
            "like spironolactone). Intercalated cells handle acid-base by secreting H+ or "
            "bicarbonate."
            "\n\n"
            "Hormonal control: ADH (from posterior pituitary, rises when plasma osmolarity is "
            "high or volume is low) inserts aquaporin-2 channels in the collecting duct apical "
            "membrane; water flows out of the duct into the hypertonic medulla, producing "
            "concentrated urine. Aldosterone (from adrenal cortex) drives Na reabsorption (water "
            "follows) and K secretion in the collecting duct. ANP (from atria, in volume overload) "
            "opposes RAAS and promotes Na and water excretion."
        ),
        "teaching": {
            "before_video": (
                "Have students label a nephron with each segment's job: 'PCT does X, loop does Y, "
                "DCT does Z, collecting duct does W.' They have to commit before video."
            ),
            "misconceptions": [
                "Students think the collecting duct is what concentrates the urine. The collecting "
                "duct uses the gradient that the loop of Henle established; both are required.",
                "Aldosterone is sometimes confused with ADH. Cue: aldosterone moves SALT (and water "
                "follows); ADH moves WATER (alone).",
                "Diuretics are not all the same; loop, thiazide, and K-sparing have different "
                "sites and different electrolyte profiles."
            ],
            "order": (
                "Each tubular segment in order with its main job, then the countercurrent "
                "multiplier, then ADH and aldosterone as the fine-tuning controls."
            ),
            "self_test": [
                "Which segment reabsorbs the most filtered Na?",
                "What does ADH do mechanistically in the collecting duct?",
                "How does the countercurrent multiplier set up urine concentration?"
            ]
        },
        "clinical": (
            "Diabetes insipidus: ADH absent (central) or ineffective (nephrogenic). Result: large "
            "volumes of dilute urine, thirst, risk of hypernatremia. Treatment: desmopressin "
            "(synthetic ADH) or address the cause. SIADH: too much ADH. Result: small volumes of "
            "concentrated urine, water retention, dilutional hyponatremia. Furosemide blocks "
            "NKCC2 in the loop; potent diuresis with hypokalemia, hypocalcemia risk. Thiazides "
            "block NCC in the DCT; milder diuresis. Spironolactone blocks aldosterone receptor; "
            "K-sparing, used in heart failure and primary hyperaldosteronism. Nurses titrating "
            "fluids and electrolytes in CHF, cirrhosis, and renal failure are working this "
            "physiology constantly."
        )
    },

    "t-fluid-acid-base": {
        "science": (
            "Body fluid compartments: total body water is about 60% of body weight. Intracellular "
            "fluid (ICF) is about two-thirds; extracellular fluid (ECF) is about one-third. ECF "
            "subdivides into interstitial (75%) and plasma (25%). The compartments have very "
            "different electrolyte profiles: ICF is high K and low Na, while ECF is the reverse. "
            "These differences are maintained by the Na/K ATPase and matter because shifts can be "
            "catastrophic (hyperkalemia causes lethal arrhythmias because it disrupts the "
            "membrane potential)."
            "\n\n"
            "Electrolyte priorities for the boards and the bedside: Na sets ECF osmolarity and "
            "volume; hyponatremia and hypernatremia produce neurologic symptoms. K sets membrane "
            "excitability; hyperkalemia and hypokalemia produce cardiac and muscle symptoms. "
            "Calcium has neuromuscular effects and is regulated by PTH, calcitonin, and vitamin D. "
            "Magnesium and phosphate are quieter but important cofactors and bone components."
            "\n\n"
            "Acid-base: normal arterial pH is 7.35-7.45. Three lines of defense. Buffers "
            "(bicarbonate, phosphate, protein) blunt acid loads on the second-to-second scale. "
            "Respiratory compensation adjusts CO2 within minutes. Renal compensation adjusts HCO3- "
            "and H+ excretion over hours to days. Four classic disturbances: respiratory acidosis "
            "(high CO2), respiratory alkalosis (low CO2), metabolic acidosis (low HCO3- or high "
            "non-CO2 acid), metabolic alkalosis (high HCO3- or loss of acid). Pattern recognition "
            "is the entire game: pH, pCO2, HCO3- read together tell the story."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the body fluid compartments as nested boxes with percentages, "
                "then label which compartment is high in K versus high in Na."
            ),
            "misconceptions": [
                "Students think 'edema' is too much total water. Often it is redistribution between "
                "compartments (low albumin lets fluid leak from plasma to interstitium).",
                "Hyponatremia is sometimes treated as low total body Na. Often it is too much "
                "water, not too little salt.",
                "Acid-base is reduced to memorizing equations. The story is which system is "
                "broken and which is compensating."
            ],
            "order": (
                "Compartments and their composition, then key electrolytes and their disturbances, "
                "then acid-base with the four-disturbance pattern."
            ),
            "self_test": [
                "Which compartment holds the most water?",
                "What does the pattern pH 7.20, pCO2 25, HCO3- 12 represent?",
                "Why does severe vomiting cause metabolic alkalosis?"
            ]
        },
        "clinical": (
            "Diabetic ketoacidosis: ketoacids accumulate, HCO3- is consumed buffering them, pH "
            "drops, the patient hyperventilates (Kussmaul) to drop CO2 in compensation. Vomiting: "
            "loss of gastric H+ causes metabolic alkalosis; volume loss adds aldosterone-driven "
            "K loss. COPD: chronic CO2 retention with renal compensation (high HCO3-) and chronic "
            "compensated respiratory acidosis. Hyperkalemia (renal failure, K-sparing diuretics, "
            "Addison) is a true emergency because it causes peaked T waves and ventricular "
            "arrhythmias. Hyponatremia in elderly patients on thiazides is common and can cause "
            "seizures. Every set of labs has a fluid-and-electrolyte story; nurses who can read "
            "it catch problems early."
        )
    },

    # ============================================================
    # MODULE 17: REPRODUCTIVE
    # ============================================================

    "t-male-reproductive": {
        "science": (
            "Testes do two jobs: produce sperm and produce testosterone. Sperm production happens "
            "in the seminiferous tubules, which are lined with Sertoli cells that support "
            "developing spermatogonia through meiosis. Testosterone is produced by Leydig cells "
            "(interstitial cells) outside the tubules. The blood-testis barrier (formed by Sertoli "
            "cell tight junctions) protects developing sperm from immune attack."
            "\n\n"
            "Sperm pathway: seminiferous tubule, rete testis, epididymis (sperm matures here, "
            "becomes motile, is stored), vas deferens (ascending through the inguinal canal), "
            "ejaculatory duct (joining with seminal vesicle duct), prostatic urethra, urethra. "
            "Accessory glands add to the seminal fluid: seminal vesicles (fructose, prostaglandins, "
            "about 60% of volume), prostate (alkaline secretion, enzymes, about 30%), bulbourethral "
            "glands (mucus pre-ejaculate)."
            "\n\n"
            "Hormonal axis: hypothalamic GnRH drives pituitary LH and FSH. LH stimulates Leydig "
            "cells to make testosterone. FSH plus testosterone supports Sertoli cells and "
            "spermatogenesis. Testosterone feeds back negatively on the hypothalamus and pituitary "
            "to stabilize the system. Inhibin from Sertoli cells specifically suppresses FSH, "
            "fine-tuning spermatogenesis."
        ),
        "teaching": {
            "before_video": (
                "Have students draw a cross-section of a testis with seminiferous tubules and "
                "Leydig cells labeled, then trace the path of sperm from tubule to urethra."
            ),
            "misconceptions": [
                "Students think the testis is one structure with one function. It does sperm "
                "production AND testosterone production via different cells.",
                "The epididymis is sometimes overlooked. Sperm leaving the seminiferous tubules "
                "are not yet motile; they mature in the epididymis.",
                "Testosterone is thought of as 'the male hormone' but it is also made (in smaller "
                "amounts) by the adrenal cortex in both sexes."
            ],
            "order": (
                "Testis structure and its two jobs, then sperm pathway with accessory glands, then "
                "the hormonal axis."
            ),
            "self_test": [
                "Which cells produce testosterone?",
                "Which cells support developing sperm?",
                "Why do anabolic steroid users develop testicular atrophy?"
            ]
        },
        "clinical": (
            "Testicular torsion is a surgical emergency; twisting of the spermatic cord cuts off "
            "blood supply and the testis dies within hours. Varicocele (enlarged pampiniform "
            "plexus) is a common cause of infertility because the heat impairs spermatogenesis. "
            "Benign prostatic hyperplasia (BPH) is age-related prostate enlargement causing "
            "urinary symptoms. Prostate cancer is the most common solid tumor in men; PSA "
            "screening is controversial but widely used. Hypogonadism (from various causes) "
            "produces low testosterone, low energy, reduced libido, reduced muscle mass; "
            "replacement therapy is increasingly common but has risks."
        )
    },

    "t-female-reproductive": {
        "science": (
            "Ovaries produce eggs (oocytes) and hormones. Females are born with all their "
            "primordial follicles already arrested in prophase I of meiosis. Each cycle a cohort "
            "of follicles begins maturing; usually one becomes dominant. The dominant follicle's "
            "granulosa and theca cells produce estrogen under FSH and LH stimulation."
            "\n\n"
            "Ovarian cycle (about 28 days). Follicular phase (days 1-14): follicle matures; "
            "estrogen rises. Ovulation (day 14): LH surge triggers release of the secondary "
            "oocyte. Luteal phase (days 15-28): ruptured follicle becomes the corpus luteum, which "
            "produces progesterone (and some estrogen) to support potential implantation. If no "
            "pregnancy, the corpus luteum regresses, hormones drop, and the cycle restarts."
            "\n\n"
            "Uterine (menstrual) cycle parallels the ovarian: menstrual phase (days 1-5, shedding "
            "of endometrium), proliferative phase (days 6-14, estrogen rebuilds endometrium), "
            "secretory phase (days 15-28, progesterone makes endometrium glandular and receptive). "
            "If no implantation, progesterone falls and the cycle restarts."
            "\n\n"
            "Hormonal control: GnRH from hypothalamus drives LH and FSH. Estrogen and progesterone "
            "feed back, mostly negatively. The key twist: rising estrogen mid-cycle switches "
            "feedback from negative to positive, triggering the LH surge. After ovulation, the "
            "corpus luteum's progesterone restores negative feedback. If pregnancy occurs, the "
            "embryo's hCG keeps the corpus luteum alive until the placenta takes over hormone "
            "production."
        ),
        "teaching": {
            "before_video": (
                "Have students draw the ovarian cycle phases with FSH, LH, estrogen, and "
                "progesterone curves over 28 days. Then label the uterine phases underneath."
            ),
            "misconceptions": [
                "Students think eggs are made monthly. All eggs are present from birth; the monthly "
                "cycle is which one matures.",
                "Estrogen is thought to only feed back negatively. The mid-cycle switch to "
                "positive feedback is the key trigger for ovulation.",
                "The menstrual cycle is reduced to the bleeding phase. It is the integration of "
                "ovarian and uterine cycles over the entire month."
            ],
            "order": (
                "Ovarian anatomy and oogenesis, then the ovarian cycle, then the uterine cycle in "
                "parallel, then hormonal control with the feedback switch."
            ),
            "self_test": [
                "What triggers ovulation?",
                "What does the corpus luteum produce?",
                "How do combined oral contraceptives prevent pregnancy?"
            ]
        },
        "clinical": (
            "Polycystic ovary syndrome (PCOS): irregular cycles, anovulation, hyperandrogenism, "
            "insulin resistance; common cause of infertility. Endometriosis: endometrial tissue "
            "outside the uterus producing painful, cyclic bleeding and infertility. Menopause: "
            "ovarian estrogen production declines; hot flashes, bone loss, mood changes. Hormonal "
            "contraception, fertility treatment, and management of menstrual disorders all "
            "depend on understanding the axis. Pap smears, mammograms, and pelvic exams are "
            "screening tools nurses help administer. Pregnancy testing detects hCG."
        )
    },

    "t-pregnancy-development": {
        "science": (
            "Fertilization happens in the ampulla of the uterine tube within hours of ovulation. "
            "The zygote divides as it travels toward the uterus and arrives as a blastocyst. "
            "Implantation in the endometrium is around day 6-7. Trophoblast cells secrete hCG "
            "almost immediately; hCG keeps the corpus luteum alive so it continues producing the "
            "progesterone that holds the endometrium in place. By the end of the first trimester, "
            "the placenta takes over hormone production."
            "\n\n"
            "The placenta is the working interface between mother and fetus. It exchanges gases, "
            "nutrients, and waste, but maternal and fetal blood never directly mix. It is also an "
            "endocrine organ (progesterone, estrogen, hPL) and an imperfect filter (many drugs, "
            "alcohol, and infections cross to the fetus)."
            "\n\n"
            "Maternal physiology changes substantially. Blood volume rises about 40 percent by "
            "the second trimester. Cardiac output increases. Renal filtration goes up. The "
            "respiratory drive shifts because progesterone affects ventilation. Late in pregnancy, "
            "the enlarged uterus presses on the inferior vena cava when the mother lies supine, "
            "compressing venous return and dropping blood pressure: classic supine hypotensive "
            "syndrome of pregnancy. For essentials scope, skip the developmental biology details "
            "(germ layers, organogenesis week-by-week) and focus on the maternal-fetal interface."
        ),
        "teaching": {
            "before_video": (
                "Ask students to draw the maternal-fetal interface: maternal blood on one side, "
                "fetal vessels on the other, the placental membrane between. They have to commit "
                "to whether blood mixes (it does not) before the video confirms."
            ),
            "misconceptions": [
                "Maternal and fetal blood mix at the placenta. They do not; only molecules diffuse "
                "across the placental membrane.",
                "Students think pregnancy is mostly about the baby. Maternal physiology changes "
                "dramatically: blood volume, cardiac output, renal function, respiratory drive.",
                "hCG is sometimes thought to come from the mother. It comes from trophoblast "
                "(fetal-side) tissue, which is why it is such a specific pregnancy marker."
            ],
            "order": (
                "Fertilization and implantation → hormonal support (hCG, corpus luteum, placenta) "
                "→ placental functions → maternal physiology by trimester."
            ),
            "self_test": [
                "Where does fertilization typically occur?",
                "What is the role of hCG in early pregnancy?",
                "Why does maternal blood volume rise during pregnancy?"
            ]
        },
        "clinical": (
            "Ectopic pregnancy: implantation outside the uterus, usually in the tube. Rupture "
            "produces hemorrhagic shock; this is a surgical emergency. Preeclampsia: third-"
            "trimester hypertension and proteinuria, with risk of progression to eclampsia "
            "(seizures); blood pressure monitoring and timely delivery are the management. "
            "Gestational diabetes: places mother at risk of preeclampsia and fetus at risk of "
            "macrosomia and shoulder dystocia at delivery. Supine hypotensive syndrome: a "
            "third-trimester patient becomes dizzy lying flat. Roll her left to relieve IVC "
            "compression. These are the prenatal nursing scenarios this unit prepares students for."
        )
    }
}
