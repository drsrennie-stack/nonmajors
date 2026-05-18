"""
Build 42 per-topic Lab ID Workbook HTML pages.
Each is a printable structure-identification (or process-labeling) workbook.
"""

import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

WORKBOOK_DATA = {
    "t-levels-of-organization": {"img_hint": "Hierarchy pyramid showing atom → molecule → organelle → cell → tissue → organ → organ system → organism (unlabeled).", "structures": ["Chemical level", "Cellular level (organelles and cells)", "Tissue level", "Organ level", "Organ system level", "Organism level"], "brief": "Label the six levels of structural organization on the unlabeled pyramid. Add one example body structure at each level."},
    "t-anatomical-terminology": {"img_hint": "Figure of a body in anatomical position with arrows pointing to body regions, cavities, and planes.", "structures": ["Anatomical position", "Sagittal plane", "Frontal (coronal) plane", "Transverse plane", "Cranial cavity", "Thoracic cavity", "Abdominopelvic cavity", "Right upper quadrant", "Left upper quadrant", "Right lower quadrant", "Left lower quadrant"], "brief": "Label the planes, cavities, and four abdominopelvic quadrants."},
    "t-homeostasis": {"img_hint": "Negative feedback loop diagram with empty boxes connected by arrows in a circle.", "structures": ["Stimulus", "Receptor", "Afferent pathway", "Control center", "Efferent pathway", "Effector", "Response (returns variable toward set point)"], "brief": "Label each component of the negative feedback loop using thermoregulation as the example."},
    "t-cell-structure": {"img_hint": "Generic eukaryotic cell cross-section showing all major organelles (unlabeled).", "structures": ["Plasma membrane", "Nucleus", "Nucleolus", "Nuclear envelope", "Rough endoplasmic reticulum", "Smooth endoplasmic reticulum", "Free ribosomes", "Golgi apparatus", "Mitochondria", "Lysosomes", "Peroxisomes", "Cytoskeleton"], "brief": "Label each organelle and write one function next to each label."},
    "t-membrane-transport": {"img_hint": "Cell membrane cross-section showing seven transport mechanisms (unlabeled).", "structures": ["Simple diffusion (e.g., O2)", "Facilitated diffusion (channel)", "Facilitated diffusion (carrier)", "Osmosis (through aquaporin)", "Primary active transport (Na+/K+ ATPase)", "Secondary active transport (Na+-glucose symporter)", "Endocytosis", "Exocytosis"], "brief": "Label each mechanism. Mark whether it is passive or active and whether ATP is required."},
    "t-epithelial-tissue": {"img_hint": "Six unlabeled micrographs of common epithelia.", "structures": ["Simple squamous", "Simple cuboidal", "Simple columnar", "Pseudostratified ciliated columnar", "Stratified squamous", "Transitional"], "brief": "Identify each epithelial type. Next to each label, write one location and one job."},
    "t-connective-tissue": {"img_hint": "Six unlabeled micrographs of connective tissues.", "structures": ["Loose areolar connective", "Adipose tissue", "Dense regular connective", "Dense irregular connective", "Hyaline cartilage", "Elastic cartilage", "Fibrocartilage", "Compact bone", "Blood"], "brief": "Identify each connective tissue. Name the dominant cell type and the function for each."},
    "t-muscle-nervous-tissue": {"img_hint": "Three unlabeled muscle micrographs plus a neuron diagram.", "structures": ["Skeletal muscle", "Cardiac muscle (intercalated discs)", "Smooth muscle", "Neuron: dendrites", "Neuron: cell body (soma)", "Neuron: axon", "Neuron: axon terminal", "Glial cell"], "brief": "Identify each muscle type and the labeled neuron parts."},
    "t-skin-layers": {"img_hint": "Cross-section of thick skin showing all epidermal layers, dermis, and hypodermis (unlabeled).", "structures": ["Stratum corneum", "Stratum lucidum", "Stratum granulosum", "Stratum spinosum", "Stratum basale", "Papillary layer of dermis", "Reticular layer of dermis", "Hypodermis", "Hair follicle", "Sebaceous gland", "Sweat gland", "Sensory receptor"], "brief": "Label the layers and embedded structures."},
    "t-skin-functions": {"img_hint": "Skin diagram with function and accessory-structure callouts.", "structures": ["Barrier / protection", "Thermoregulation (sweat, vasomotor)", "Sensation", "Vitamin D synthesis", "Limited excretion", "Hair follicle", "Sebaceous gland", "Eccrine sweat gland", "Apocrine sweat gland", "Nail"], "brief": "Label each function callout and each accessory structure."},
    "t-bone-tissue": {"img_hint": "Long bone cross-section + osteon (Haversian system) diagram, unlabeled.", "structures": ["Periosteum", "Compact bone", "Spongy bone", "Medullary cavity", "Endosteum", "Diaphysis", "Epiphysis", "Epiphyseal plate", "Osteon", "Central canal", "Lamellae", "Lacuna", "Canaliculi", "Osteocyte", "Osteoblast", "Osteoclast"], "brief": "Label the long bone regions and the osteon parts."},
    "t-axial-skeleton": {"img_hint": "Articulated axial skeleton from anterior and lateral views, unlabeled.", "structures": ["Frontal bone", "Parietal bone", "Temporal bone", "Occipital bone", "Mandible", "Maxilla", "Cervical vertebrae (C1-C7)", "Thoracic vertebrae (T1-T12)", "Lumbar vertebrae (L1-L5)", "Sacrum", "Coccyx", "Sternum", "True ribs (1-7)", "False ribs (8-10)", "Floating ribs (11-12)"], "brief": "Label every named bone or region. Identify atlas (C1) and axis (C2)."},
    "t-appendicular-skeleton": {"img_hint": "Articulated upper and lower limbs with girdles, unlabeled.", "structures": ["Clavicle", "Scapula", "Humerus", "Radius", "Ulna", "Carpals", "Metacarpals", "Phalanges (hand)", "Ilium", "Ischium", "Pubis", "Femur", "Patella", "Tibia", "Fibula", "Tarsals", "Metatarsals", "Phalanges (foot)"], "brief": "Label every bone in the upper and lower limbs."},
    "t-joints-movements": {"img_hint": "Six synovial joint examples plus arrows for body movements.", "structures": ["Plane joint", "Hinge joint", "Pivot joint", "Condyloid joint", "Saddle joint", "Ball-and-socket joint", "Flexion", "Extension", "Abduction", "Adduction", "Rotation", "Circumduction"], "brief": "Label each synovial joint type and movement."},
    "t-skeletal-muscle-microanatomy": {"img_hint": "Muscle tissue hierarchy plus a sarcomere diagram.", "structures": ["Epimysium", "Perimysium", "Endomysium", "Muscle fiber (cell)", "Myofibril", "Sarcomere", "Z-line", "M-line", "A band", "I band", "H zone", "Thick filament (myosin)", "Thin filament (actin)", "T-tubule", "Sarcoplasmic reticulum"], "brief": "Label every level of the hierarchy and every part of the sarcomere."},
    "t-sliding-filament": {"img_hint": "Four-step cross-bridge cycle diagram plus thin-filament regulation (unlabeled).", "structures": ["1. Cocking (ATP hydrolyzed)", "2. Cross-bridge formation", "3. Power stroke (ADP+Pi released)", "4. Detachment (new ATP binds)", "Ca2+ binds troponin", "Tropomyosin shifts", "SR Ca2+ ATPase (relaxation)"], "brief": "Label the four steps of the cross-bridge cycle in order. Mark where ATP is needed."},
    "t-motor-units": {"img_hint": "Motor unit diagram + twitch/tetanus tension curve, unlabeled.", "structures": ["Motor neuron (cell body in spinal cord)", "Axon branches", "Neuromuscular junction", "Single twitch", "Wave (frequency) summation", "Unfused tetanus", "Fused tetanus", "Type I (slow oxidative)", "Type IIx (fast glycolytic)"], "brief": "Label each part of the motor unit and each phase of the tension trace."},
    "t-neurons-rmp": {"img_hint": "Neuron anatomy + ion gradient diagram across the membrane, unlabeled.", "structures": ["Dendrites", "Cell body (soma)", "Axon hillock", "Axon", "Myelin sheath", "Node of Ranvier", "Axon terminal", "Na+ outside (high)", "K+ inside (high)", "Na+/K+ ATPase", "K+ leak channel", "Resting membrane potential ≈ -70 mV"], "brief": "Label the neuron parts. On the membrane diagram, show ion gradients."},
    "t-action-potentials": {"img_hint": "Action potential voltage trace + chemical synapse diagram, unlabeled.", "structures": ["Resting potential (-70 mV)", "Threshold (-55 mV)", "Depolarization (Na+ in)", "Peak (+30 mV)", "Repolarization (K+ out)", "Hyperpolarization", "Voltage-gated Ca2+ channel opens", "Vesicle releases neurotransmitter", "Postsynaptic receptor binding", "EPSP or IPSP"], "brief": "Label each phase of the AP and the synaptic transmission steps."},
    "t-cns-organization": {"img_hint": "Lateral view + sagittal section of the brain, unlabeled.", "structures": ["Frontal lobe", "Parietal lobe", "Temporal lobe", "Occipital lobe", "Precentral gyrus (motor cortex)", "Postcentral gyrus (somatosensory)", "Broca area", "Wernicke area", "Cerebellum", "Diencephalon (thalamus, hypothalamus)", "Midbrain", "Pons", "Medulla oblongata", "Dura mater", "Arachnoid mater", "Pia mater"], "brief": "Label every lobe, key cortex region, brainstem component, and meningeal layer."},
    "t-pns-autonomic": {"img_hint": "Cranial nerve diagram + sympathetic vs parasympathetic outflow comparison, unlabeled.", "structures": ["CN II Optic", "CN III Oculomotor", "CN V Trigeminal", "CN VII Facial", "CN VIII Vestibulocochlear", "CN X Vagus", "Sympathetic outflow (T1-L2)", "Parasympathetic outflow (CN III, VII, IX, X; S2-S4)", "Sympathetic ganglion (near cord)", "Parasympathetic ganglion (near target)", "Reflex arc: receptor, sensory, integration, motor, effector"], "brief": "Identify cranial nerves and outflow regions. Contrast pre- and post-ganglionic fiber lengths."},
    "t-vision": {"img_hint": "Sagittal section of the eye + retinal-layer detail, unlabeled.", "structures": ["Cornea", "Iris", "Pupil", "Lens", "Ciliary body/muscle", "Sclera", "Choroid", "Retina", "Fovea centralis", "Optic disc (blind spot)", "Optic nerve", "Vitreous humor", "Aqueous humor", "Rod", "Cone"], "brief": "Label each eye structure. Note which bend light and which detect light."},
    "t-hearing-equilibrium": {"img_hint": "Cross-section of the ear + cochlea/semicircular canal detail, unlabeled.", "structures": ["Pinna", "External auditory canal", "Tympanic membrane", "Malleus", "Incus", "Stapes", "Oval window", "Cochlea", "Round window", "Vestibule (utricle, saccule)", "Semicircular canals (3)", "Vestibulocochlear nerve (CN VIII)", "Organ of Corti"], "brief": "Label the path of sound and the structures that handle equilibrium."},
    "t-hormone-mechanisms": {"img_hint": "Two side-by-side hormone mechanism diagrams: lipid-soluble (intracellular) vs water-soluble (surface receptor + second messenger).", "structures": ["Lipid-soluble hormone (e.g., cortisol)", "Crosses plasma membrane", "Intracellular receptor", "Hormone-receptor complex binds DNA", "Altered gene expression (slow)", "Water-soluble hormone (e.g., insulin)", "Cell-surface receptor", "Second messenger cascade", "Rapid change in cell function"], "brief": "Label each mechanism. Mark speed and duration; write one example hormone for each."},
    "t-major-glands": {"img_hint": "Body silhouette with locations of all major endocrine glands, unlabeled.", "structures": ["Hypothalamus", "Pituitary (anterior and posterior)", "Pineal", "Thyroid", "Parathyroids (4)", "Thymus", "Adrenals (cortex and medulla)", "Pancreas (islets)", "Gonads"], "brief": "Label each gland. Add one major hormone and its job for each."},
    "t-blood-composition": {"img_hint": "Centrifuged blood tube + WBC differential smear, unlabeled.", "structures": ["Plasma (~55%)", "Buffy coat (WBCs + platelets)", "Erythrocytes (~45%)", "Neutrophil", "Eosinophil", "Basophil", "Lymphocyte", "Monocyte", "Platelet"], "brief": "Label each blood component and WBC type with its main role."},
    "t-hemostasis-blood-typing": {"img_hint": "Three-phase hemostasis diagram + ABO/Rh chart, unlabeled.", "structures": ["Phase 1: Vascular spasm", "Phase 2: Platelet plug", "Phase 3: Coagulation (fibrin)", "Type A: A antigen, anti-B antibody", "Type B: B antigen, anti-A antibody", "Type AB: both antigens, no antibodies (universal recipient)", "Type O: no antigens, both antibodies (universal donor)", "Rh+ (D antigen present)", "Rh- (no D antigen)"], "brief": "Label each phase of hemostasis. Complete the ABO/Rh chart."},
    "t-heart-cardiac-cycle": {"img_hint": "Anterior cross-section of the heart + cardiac cycle phase diagram, unlabeled.", "structures": ["Right atrium", "Left atrium", "Right ventricle", "Left ventricle", "Tricuspid valve", "Pulmonary valve", "Mitral (bicuspid) valve", "Aortic valve", "Superior vena cava", "Inferior vena cava", "Pulmonary trunk", "Pulmonary veins", "Aorta", "Cardiac cycle: filling, isovolumetric contraction, ejection, isovolumetric relaxation"], "brief": "Label every chamber, valve, and great vessel. Mark valve states at each cycle phase."},
    "t-conduction-ecg": {"img_hint": "Heart with conduction pathway overlay, unlabeled.", "structures": ["SA node (pacemaker)", "Atrial myocardium", "AV node (delay)", "Bundle of His", "Right bundle branch", "Left bundle branch", "Purkinje fibers", "Ventricular myocardium"], "brief": "Trace the conduction pathway from SA node to ventricular myocardium."},
    "t-vessels-hemodynamics": {"img_hint": "Cross-sections of artery, capillary, and vein with wall layers, unlabeled.", "structures": ["Artery (3 wall layers)", "Arteriole", "Capillary (single endothelial layer)", "Venule", "Vein with valve", "Tunica intima", "Tunica media", "Tunica externa", "Venous valve"], "brief": "Label each vessel type and its wall layers."},
    "t-lymphatic-innate": {"img_hint": "Lymphatic system silhouette + innate-cell types, unlabeled.", "structures": ["Cervical nodes", "Axillary nodes", "Inguinal nodes", "Lymphatic vessels", "Spleen", "Thymus", "Tonsils", "MALT", "Neutrophil", "Macrophage", "Natural killer cell", "Mast cell / basophil"], "brief": "Label lymphatic organs and innate cells with their roles."},
    "t-adaptive-immunity": {"img_hint": "Side-by-side humoral (B-cell) and cell-mediated (T-cell) response diagrams, unlabeled.", "structures": ["B cell", "Plasma cell", "Antibody", "Memory B cell", "Antigen-presenting cell (MHC II)", "Helper T cell (CD4)", "Cytotoxic T cell (CD8)", "MHC I (on all nucleated cells)", "MHC II (on APCs)", "Memory T cell"], "brief": "Label each cell and the path from antigen to memory."},
    "t-resp-anatomy-mechanics": {"img_hint": "Sagittal respiratory tract from nose to alveoli + breathing mechanics diagram, unlabeled.", "structures": ["Nasal cavity", "Pharynx", "Larynx", "Trachea", "Right primary bronchus", "Left primary bronchus", "Bronchioles", "Alveoli", "Diaphragm", "External intercostals", "Parietal pleura", "Visceral pleura", "Pleural cavity (negative pressure)"], "brief": "Label the airway and the muscles of breathing."},
    "t-gas-exchange-transport": {"img_hint": "Alveolus-capillary + tissue-capillary interfaces with O2/CO2 arrows, unlabeled.", "structures": ["External respiration: O2 in", "External respiration: CO2 out", "Internal respiration: O2 to tissue", "Internal respiration: CO2 to blood", "O2 bound to hemoglobin (98%)", "CO2 as bicarbonate (~70%)", "CO2 bound to Hb (~20%)", "CO2 dissolved (~10%)"], "brief": "Label gas movements and CO2 transport forms."},
    "t-gi-anatomy-motility": {"img_hint": "Whole GI tract silhouette + cross-section of GI wall (4 layers), unlabeled.", "structures": ["Mouth", "Esophagus", "Stomach", "Duodenum", "Jejunum", "Ileum", "Cecum", "Colon", "Rectum", "Anus", "Salivary glands", "Liver", "Gallbladder", "Pancreas", "Mucosa", "Submucosa", "Muscularis externa", "Serosa", "Lower esophageal sphincter", "Pyloric sphincter", "Ileocecal sphincter", "Anal sphincters"], "brief": "Label every GI segment, accessory organ, wall layer, and sphincter."},
    "t-digestion-absorption": {"img_hint": "Small intestine with villi + macromolecule digestion/absorption chart, unlabeled.", "structures": ["Plicae circulares", "Villi", "Microvilli", "Lacteal", "Carb digestion: amylases → brush-border", "Protein digestion: pepsin → pancreatic proteases → brush-border peptidases", "Fat digestion: bile + pancreatic lipase", "SGLT1 (Na+-glucose symporter)", "Chylomicrons exit via lacteals"], "brief": "Label absorptive surface and digestion sites for each macromolecule."},
    "t-kidney-filtration": {"img_hint": "Frontal section of kidney + single nephron with vasculature, unlabeled.", "structures": ["Cortex", "Medulla (renal pyramids)", "Renal pelvis", "Ureter", "Renal artery", "Renal vein", "Afferent arteriole", "Glomerulus", "Bowman capsule", "Efferent arteriole", "Proximal convoluted tubule", "Loop of Henle (descending and ascending)", "Distal convoluted tubule", "Collecting duct", "Filtration barrier (3 layers)"], "brief": "Label the kidney regions and the entire nephron."},
    "t-tubular-function": {"img_hint": "Nephron with each segment's specific transport job, unlabeled.", "structures": ["PCT: bulk Na+/water/glucose reabsorption", "Descending limb: water out (permeable)", "Thick ascending limb: NKCC2 cotransporter", "Early DCT: NCC cotransporter", "Late DCT/collecting duct: aldosterone-driven Na+ reabsorption, K+ secretion", "Collecting duct: ADH-driven water reabsorption via aquaporin-2", "Medullary interstitium (hypertonic)"], "brief": "Label each tubule segment with its action. Mark where ADH and aldosterone act."},
    "t-fluid-acid-base": {"img_hint": "Body fluid compartments + acid-base table comparing four disturbances, unlabeled.", "structures": ["Total body water (~60%)", "ICF (~2/3)", "ECF (~1/3)", "Plasma (~1/4 of ECF)", "Interstitial fluid (~3/4 of ECF)", "ECF cation: Na+", "ICF cation: K+", "Respiratory acidosis", "Respiratory alkalosis", "Metabolic acidosis", "Metabolic alkalosis"], "brief": "Label fluid compartments and each acid-base disturbance with its compensation."},
    "t-male-reproductive": {"img_hint": "Sagittal view of male pelvis + cross-section of seminiferous tubule, unlabeled.", "structures": ["Testis", "Seminiferous tubule (Sertoli cells, developing sperm)", "Leydig cells (testosterone)", "Epididymis", "Vas deferens", "Seminal vesicle", "Prostate", "Bulbourethral gland", "Ejaculatory duct", "Urethra", "Penis"], "brief": "Label structures and trace the path of sperm from production to ejaculation."},
    "t-female-reproductive": {"img_hint": "Sagittal female pelvis + ovary cross-section with follicle stages, unlabeled.", "structures": ["Ovary", "Primordial follicle", "Primary follicle", "Secondary follicle", "Mature (Graafian) follicle", "Corpus luteum", "Uterine (fallopian) tube", "Ampulla (site of fertilization)", "Uterus (fundus, body, cervix)", "Endometrium", "Myometrium", "Vagina"], "brief": "Label female reproductive structures and follicle stages."},
    "t-pregnancy-development": {"img_hint": "Cross-section of placenta showing maternal-fetal interface, unlabeled.", "structures": ["Maternal endometrium (decidua)", "Intervillous space (maternal blood)", "Chorionic villus", "Fetal capillary inside villus", "Placental membrane (no blood mixing)", "Umbilical arteries (deoxygenated fetal blood TO placenta)", "Umbilical vein (oxygenated TO fetus)", "Trophoblast (source of hCG)"], "brief": "Label placental structures. Mark where exchange occurs and note that maternal and fetal blood never mix."},
}


def load_topics():
    proc = subprocess.run(
        ['node', '-e',
         "const w={};new Function('window',require('fs').readFileSync('course-content.js','utf8'))(w);"
         "console.log(JSON.stringify(w.BIO304_COURSE_CONTENT.modules.flatMap(m=>m.topics.map(t=>({id:t.id,title:t.title,summary:t.summary,day:t.dayInCourse,module:m.title})))))"],
        cwd=HERE, capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIO 304 . {short_title} . Lab Workbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--navy:#1E3D4C;--navy-deep:#142A36;--navy-tint:#EDF1F3;--gold:#B8924A;--gold-deep:#9A7838;--terra:#C2734D;--terra-dark:#A0522D;--sage-dark:#4F6B57;--sage-deeper:#3F5B47;--white:#FFFFFF;--off-white:#FAFAF9;--gray-line:#CFD6DA;--gray-soft:#5C6970}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Lora',Georgia,serif;color:var(--navy);background:var(--off-white);line-height:1.55}}
.skip-link{{position:absolute;left:-9999px;top:0;background:var(--navy);color:var(--white);padding:10px 16px;z-index:100;text-decoration:none;font-weight:600;border-radius:0 0 6px 0}}
.skip-link:focus{{left:0}}
:focus-visible{{outline:3px solid var(--gold);outline-offset:2px}}
@media (prefers-reduced-motion: reduce){{*,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}}}
header{{background:var(--white);border-bottom:1px solid var(--gray-line);padding:24px 32px}}
.eyebrow{{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--terra-dark);margin:0 0 4px}}
h1{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;font-size:clamp(22px,3vw,32px);color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}}
.subhead{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);margin:0 0 8px}}
.usage{{font-style:italic;color:var(--gray-soft);font-size:14px;margin:6px 0 0}}
main{{max-width:880px;margin:0 auto;padding:24px}}
.card{{background:var(--white);border:1px solid var(--gray-line);border-radius:10px;padding:22px 24px;box-shadow:0 1px 3px rgba(0,0,0,.08);margin-bottom:18px}}
.section-band{{margin:24px 0 8px;padding:14px 18px;border-radius:8px}}
.section-band.anatomy{{background:#FAF1EC;border-left:6px solid var(--terra-dark)}}
.section-band.physiology{{background:#EEF1EE;border-left:6px solid var(--sage-dark)}}
.section-band p.tag{{font-family:'DM Sans',system-ui,sans-serif;font-weight:700;font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 4px;color:var(--terra-dark)}}
.section-band.physiology p.tag{{color:var(--sage-deeper)}}
.section-band h2{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:800;color:var(--navy);font-size:22px;margin:0;letter-spacing:-.01em}}
h2{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;color:var(--terra-dark);font-size:18px;margin:0 0 10px}}
.image-placeholder{{background:var(--navy-tint);border:2px dashed var(--navy);border-radius:8px;padding:60px 24px;text-align:center;color:var(--navy);font-family:'Plus Jakarta Sans',sans-serif;font-weight:600;min-height:240px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:8px}}
.placeholder-block{{background:#F1F4F1;border:2px dashed var(--sage-deeper);border-radius:8px;padding:24px;color:var(--navy);font-family:'Plus Jakarta Sans',sans-serif}}
.placeholder-block strong{{font-weight:700;color:var(--sage-deeper);display:block;margin-bottom:6px;letter-spacing:.04em;text-transform:uppercase;font-size:12px}}
.placeholder-block p{{margin:6px 0;font-family:'Lora',Georgia,serif;color:var(--navy);font-size:15px}}
.placeholder-block ol{{margin:8px 0;padding-left:22px}}
.placeholder-block li{{font-family:'Lora',Georgia,serif;color:var(--navy);margin:8px 0}}
.image-placeholder small{{display:block;font-weight:400;color:var(--gray-soft);font-style:italic;max-width:60ch}}
ol.structure-list{{font-family:'Lora',Georgia,serif;font-size:15px;line-height:1.9;padding-left:24px}}
ol.structure-list li{{padding:4px 0;border-bottom:1px dotted var(--gray-line)}}
ol.structure-list li:last-child{{border-bottom:none}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}}
.btn{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-weight:600;font-size:14px;padding:10px 18px;border-radius:6px;border:1px solid transparent;cursor:pointer;text-decoration:none;display:inline-block}}
.btn-primary{{background:var(--navy);color:var(--white);border-color:var(--navy)}}
.btn-primary:hover{{background:var(--navy-deep)}}
.btn-ghost{{background:transparent;color:var(--navy);border-color:var(--gray-line)}}
.btn-ghost:hover{{background:var(--navy-tint);border-color:var(--navy)}}
footer{{text-align:center;color:var(--gray-soft);padding:20px;font-style:italic;font-size:13px}}
@media print{{
  body{{background:white;color:black}}
  .no-print{{display:none!important}}
  .card{{box-shadow:none;border-color:#888;page-break-inside:avoid}}
  header{{border-bottom:2px solid #333}}
  .image-placeholder{{border-color:#555;background:#fafafa;color:#000}}
  h1,h2,h3{{color:black}}
}}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header>
  <p class="eyebrow">BIO 304 . WEEK {week} . {day_name_long} . LAB WORKBOOK</p>
  <h1>{title}</h1>
  <p class="subhead">{summary}</p>
  <p class="usage">Print this page. Use the structure list below to label the diagram by hand. Hand-labeled work is the integrity mechanism for this course.</p>
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
    <h2>1A. Unlabeled diagram</h2>
    <div class="image-placeholder" role="img" aria-label="Unlabeled diagram placeholder">
      <span>Insert unlabeled image here</span>
      <small>{img_hint}</small>
    </div>
    <p class="usage">After printing, label each structure using the list below. Write directly on the printout.</p>
  </article>

  <article class="card">
    <h2>1B. Structures to label ({structure_count})</h2>
    <ol class="structure-list">
      {structure_items}
    </ol>
    <p class="usage">{brief}</p>
  </article>

  <div class="section-band physiology">
    <p class="tag">Part 2 of 2</p>
    <h2>Physiology Lab</h2>
  </div>

  <article class="card">
    <h2>2A. Activity (to be customized)</h2>
    <div class="placeholder-block" role="region" aria-label="Physiology activity placeholder">
      <strong>Activity placeholder</strong>
      <p>This space is reserved for the topic-specific physiology activity (data interpretation, calculation, mechanism walkthrough, simulator, or clinical scenario). Dr. Rennie will fill in the specific activity for this topic.</p>
      <p style="margin-top:10px;color:var(--gray-soft);font-style:italic">Possible formats for {short_title}: graph reading, value calculation, scenario reasoning, predicting an outcome from a perturbation, or comparing two conditions.</p>
    </div>
  </article>

  <article class="card">
    <h2>2B. Synthesis questions (to be customized)</h2>
    <div class="placeholder-block" role="region" aria-label="Synthesis questions placeholder">
      <strong>Question placeholder</strong>
      <ol>
        <li>Synthesis question 1 (links anatomy to the physiology activity above).</li>
        <li>Synthesis question 2 (applies the concept to a clinical or everyday scenario).</li>
        <li>Synthesis question 3 (predicts what changes if one variable is altered).</li>
      </ol>
      <p style="margin-top:10px;color:var(--gray-soft);font-style:italic">Dr. Rennie will replace these with topic-specific questions tied to the activity above.</p>
    </div>
  </article>

  <article class="card">
    <h2>3. What to submit</h2>
    <p>Print this workbook. Complete <strong>both</strong> the Anatomy Lab (hand-labeled diagram + structure list) and the Physiology Lab (activity + synthesis questions). Photograph or scan every page and upload to Canvas before Sunday at 11:59 PM. Hand-labeled work is the integrity mechanism for this course.</p>
  </article>
</main>
<footer><p>Dr. Sharilyn Rennie . BIO 304 Lab Workbook . Day {day_num} of 32</p></footer>
<script>
(function(){{
  if(window.self===window.top)return;
  function sendHeight(){{
    const h=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight);
    try{{window.parent.postMessage({{type:'iframe-height',id:'bio304-workbook',height:h}},'*');}}catch(e){{}}
  }}
  window.addEventListener('load',sendHeight);
  window.addEventListener('resize',sendHeight);
  if(window.ResizeObserver){{new ResizeObserver(sendHeight).observe(document.body);}}else{{setInterval(sendHeight,800);}}
}})();
</script>
</body>
</html>
"""


def build_workbook(topic):
    tid = topic["id"]
    data = WORKBOOK_DATA.get(tid)
    if not data:
        return None
    day_num = topic["day"]
    week = (day_num - 1) // 4 + 1
    day_name_long = ["Monday", "Tuesday", "Thursday", "Friday"][(day_num - 1) % 4]
    structure_items = "\n      ".join(f"<li>{s}</li>" for s in data["structures"])
    return PAGE_TEMPLATE.format(
        short_title=topic["title"],
        week=week,
        day_name_long=day_name_long,
        day_num=day_num,
        title=topic["title"],
        summary=topic.get("summary", ""),
        img_hint=data["img_hint"],
        structure_count=len(data["structures"]),
        structure_items=structure_items,
        brief=data["brief"],
    )


def slugify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()


def main():
    topics = load_topics()
    built = 0
    for t in topics:
        html = build_workbook(t)
        if not html:
            print(f"  no workbook data for {t['id']}")
            continue
        day = t["day"]
        slug = slugify(t["title"])
        filename = f"workbook_day{day:02d}_{slug}.html"
        out_path = os.path.join(HERE, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        built += 1
    print(f"\nBuilt {built} workbook HTML files.")


if __name__ == "__main__":
    main()
