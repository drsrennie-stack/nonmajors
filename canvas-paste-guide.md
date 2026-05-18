# BIO 304 Canvas Paste Guide

Base URL for every iframe: `https://drsrennie-stack.github.io/nonmajors/`
Course start: Monday, June 8, 2026 (Week 1)
Course end: Sunday, August 2, 2026 (Week 8)

## The restructured Canvas plan

**Total Canvas items: 27** (down from 102).

| Module | Items | Type |
|---|---|---|
| Module 0 | 3 | Page (syllabus), Discussion (welcome), Quiz (ack) |
| Modules 1 to 8 | 3 each, 24 total | Discussion, Quiz, Assignment (lab workbooks) |

Everything else lives inside the document-style syllabus at `biol304_syllabus.html`, which has a sticky table of contents and the full 8-week schedule with day-by-day pill links. Students never need a "Week N Hub" Canvas page because the syllabus already has it.

## How to use this guide

For each item below:

1. Open the matching Canvas module.
2. Create a new item of the listed type (Page, Discussion, Assignment, or Quiz).
3. For Pages and prompt bodies, click the **HTML editor** icon (`</>`) and paste the code block.
4. For Quizzes, build the questions manually using the prompts provided in `canvas-modules-1-8.md`.
5. Set the open/close dates as listed.
6. Publish.

---

# Module 0 (open the first day of class)

## 0.1 Course Syllabus & Welcome (Canvas Page)

This is the only page in Module 0 that uses an iframe. It embeds the full document-style syllabus, which contains the welcome letter, course at a glance, learning outcomes, materials, weekly rhythm, grading, deadlines, habits, 8-week schedule, how to reach me, integrity and AI policy, accessibility, RSI, tech setup, and the resource index. Students navigate through the sticky table of contents inside the iframe.

**Suggested iframe height: 4200px** (the syllabus is intentionally long so it can serve as a true printable syllabus).

```html
<p>Welcome to BIO 304. The syllabus below is your single point of reference for the course. Use the table of contents inside it to jump to any section: welcome, course at a glance, learning outcomes, materials, the weekly rhythm, grading, deadlines, the 8-week schedule, how to reach me, integrity and AI policy, accessibility, regular substantive interaction, tech setup, and the resource index.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" target="_blank" rel="noopener"><strong>Open the full syllabus in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" width="100%" height="4200" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="BIO 304 Syllabus"></iframe></p>
```

## 0.2 Welcome Discussion (Canvas Discussion topic, iframed branded page)

**Settings:**
- Title: `Welcome Discussion · BIO 304`
- Type: Threaded
- Available: Mon Jun 8, 12:00 AM
- Initial post due: Fri Jun 12, 11:59 PM
- Replies due: Sun Jun 14, 11:59 PM
- Points: 5
- Require initial post before viewing replies: Yes

Paste this into the discussion prompt body. The iframe renders the branded welcome page; the short text above it keeps Canvas notifications readable.

```html
<p>Welcome to BIO 304. Read the prompt below and post your introduction by Friday. Reply to at least two classmates by Sunday.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/welcome_discussion.html" target="_blank" rel="noopener"><strong>Open the welcome prompt in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/welcome_discussion.html" width="100%" height="1450" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Welcome Discussion prompt"></iframe></p>
```

## 0.3 Start-Here Syllabus Quiz (Canvas Quiz)

Native Canvas Quiz with 8 high-yield questions. Build them manually from `canvas-module-0-snippets.md` section 3.

**Settings:**
- Title: `Start-Here Syllabus Quiz`
- Type: 8-point graded (or practice, your call)
- Time limit: None
- Multiple attempts: Yes (unlimited)
- Module Requirement: 100% correct before Module 1 unlocks

---

# Module 1 (Week 1: Jun 8 to Jun 14)

Topics this week: Levels of Organization, Anatomical Terminology and Body Regions, Homeostasis and Feedback Loops, Cell Structure and Organelles, Membrane Transport.

## 1.1 Week 1 Lab Workbooks (Canvas Assignment)

Single assignment, 4 daily workbooks submitted as one upload by Sunday.

**Settings:**
- Title: `Week 1 Lab Workbooks`
- Submission type: File upload (PDF, JPG, or PNG, multiple files allowed)
- Due: Sun Jun 14, 11:59 PM
- Points: 20 (rubric with 4 rows, 5 pts each)

**Paste this into the assignment body:**

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day. Print each workbook the night it is assigned, label every structure by hand using the structure list, then photograph or scan all four pages and upload them as a single submission by Sunday at 11:59 PM.</p>
<h3>Workbooks for Week 1</h3>
<ul>
  <li><strong>Monday (Jun 8)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day01_levels-of-organization.html" target="_blank" rel="noopener">Levels of Organization &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day01_anatomical-terminology-and-body-regions.html" target="_blank" rel="noopener">Anatomical Terminology and Body Regions &#8599;</a></li>
  <li><strong>Tuesday (Jun 9)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day02_homeostasis-and-feedback-loops.html" target="_blank" rel="noopener">Homeostasis and Feedback Loops &#8599;</a></li>
  <li><strong>Thursday (Jun 11)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day03_cell-structure-and-organelles.html" target="_blank" rel="noopener">Cell Structure and Organelles &#8599;</a></li>
  <li><strong>Friday (Jun 12)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day04_membrane-transport.html" target="_blank" rel="noopener">Membrane Transport &#8599;</a></li>
</ul>
<p><strong>Submission tips:</strong> upload as a single PDF if you can (combine pages), or upload separate JPG/PNG files for each day.</p>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 1.2 Week 1 Discussion (Canvas Discussion topic)

**Settings:**
- Title: `Week 1 Discussion: Finding homeostasis in your own life`
- Available: Wed Jun 10, 12:00 AM
- Initial post due: Fri Jun 12, 11:59 PM
- Replies due: Sun Jun 14, 11:59 PM
- Points: 10
- Require initial post before viewing replies: Yes

**Option A: paste the branded discussion page as an iframe** (one-line iframe in the prompt body, gives students the branded reading experience):

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week01_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 1 Discussion prompt"></iframe>
```

**Option B: paste the prompt HTML directly into the discussion body** (use this if you'd rather have the prompt visible in Canvas's native discussion style):

```html
<p>This week we built the four-part negative feedback loop (stimulus &rarr; receptor &rarr; control center &rarr; effector) and saw how the body keeps variables like body temperature, blood glucose, and pH near a set point.</p>
<p>Pick <strong>one variable in your own life</strong> that you actively regulate, but that is NOT a body variable. Examples: the temperature of your bedroom, your bank account balance, the amount of caffeine you drink in a day, the brightness of your phone screen.</p>
<p>In your initial post (200 to 300 words):</p>
<ol>
  <li><strong>Name the variable</strong> and its set point (your target).</li>
  <li><strong>Identify each of the four feedback components</strong> in YOUR system (what is the receptor? control center? effector? response?).</li>
  <li><strong>Describe a time the system worked</strong> and a time it failed.</li>
  <li><strong>Then tie it to the body</strong>: what physiological feedback loop is the closest analog?</li>
</ol>
<p>Reply to at least two classmates by Sunday. Look for someone whose system mirrors yours and someone whose differs.</p>
```

## 1.3 Week 1 Quiz (Canvas Quiz)

Native Canvas Quiz. Build manually using `canvas-modules-1-8.md` Module 1 section 3.

**Settings:**
- Title: `Week 1 Quiz`
- Available: Fri Jun 12, 12:00 AM
- Due: Sun Jun 14, 11:59 PM
- Time limit: 20 minutes
- One attempt
- Honorlock proctored: Yes
- Points: 20

---

# Module 2 (Week 2: Jun 15 to Jun 21)

Topics: Epithelial Tissue Classification, Connective Tissues, Muscle and Nervous Tissue Overview, Skin Structure and Layers, Skin Functions and Accessory Structures.

## 2.1 Week 2 Lab Workbooks (Assignment, due Sun Jun 21)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day. Print each workbook the night it is assigned, label every structure by hand using the structure list, then photograph or scan all four pages and upload them as a single submission by Sunday at 11:59 PM.</p>
<h3>Workbooks for Week 2</h3>
<ul>
  <li><strong>Monday (Jun 15)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day05_epithelial-tissue-classification.html" target="_blank" rel="noopener">Epithelial Tissue Classification &#8599;</a></li>
  <li><strong>Tuesday (Jun 16)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day06_connective-tissues.html" target="_blank" rel="noopener">Connective Tissues &#8599;</a></li>
  <li><strong>Thursday (Jun 18)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day07_muscle-and-nervous-tissue-overview.html" target="_blank" rel="noopener">Muscle and Nervous Tissue Overview &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day07_skin-structure-and-layers.html" target="_blank" rel="noopener">Skin Structure and Layers &#8599;</a></li>
  <li><strong>Friday (Jun 19)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day08_skin-functions-and-accessory-structures.html" target="_blank" rel="noopener">Skin Functions and Accessory Structures &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 2.2 Week 2 Discussion (Discussion, posts Wed Jun 17, replies due Sun Jun 21)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week02_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 2 Discussion prompt"></iframe>
```

## 2.3 Week 2 Quiz (Canvas Quiz, Fri Jun 19 to Sun Jun 21)

Honorlock, 20 min, one attempt.

---

# Module 3 (Week 3: Jun 22 to Jun 28)

Topics: Bone Tissue and Bone Growth, Axial Skeleton, Appendicular Skeleton, Joints and Body Movements.

## 3.1 Week 3 Lab Workbooks (due Sun Jun 28)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day.</p>
<h3>Workbooks for Week 3</h3>
<ul>
  <li><strong>Monday (Jun 22)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day09_bone-tissue-and-bone-growth.html" target="_blank" rel="noopener">Bone Tissue and Bone Growth &#8599;</a></li>
  <li><strong>Tuesday (Jun 23)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day10_axial-skeleton.html" target="_blank" rel="noopener">Axial Skeleton &#8599;</a></li>
  <li><strong>Thursday (Jun 25)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day11_appendicular-skeleton.html" target="_blank" rel="noopener">Appendicular Skeleton &#8599;</a></li>
  <li><strong>Friday (Jun 26)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day12_joints-and-body-movements.html" target="_blank" rel="noopener">Joints and Body Movements &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 3.2 Week 3 Discussion (posts Wed Jun 24, replies due Sun Jun 28)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week03_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 3 Discussion prompt"></iframe>
```

## 3.3 Week 3 Quiz (Fri Jun 26 to Sun Jun 28)

Honorlock, 20 min, one attempt.

---

# Module 4 (Week 4: Jun 29 to Jul 5)

Topics: Skeletal Muscle Microanatomy, Motor Units and Muscle Mechanics, Sliding Filament and the Cross-Bridge Cycle, Neurons and Resting Membrane Potential, Action Potentials and Synaptic Transmission.

## 4.1 Week 4 Lab Workbooks (due Sun Jul 5)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day.</p>
<h3>Workbooks for Week 4</h3>
<ul>
  <li><strong>Monday (Jun 29)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day13_skeletal-muscle-microanatomy.html" target="_blank" rel="noopener">Skeletal Muscle Microanatomy &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day13_motor-units-and-muscle-mechanics.html" target="_blank" rel="noopener">Motor Units and Muscle Mechanics &#8599;</a></li>
  <li><strong>Tuesday (Jun 30)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day14_sliding-filament-and-the-cross-bridge-cycle.html" target="_blank" rel="noopener">Sliding Filament and the Cross-Bridge Cycle &#8599;</a></li>
  <li><strong>Thursday (Jul 2)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day15_neurons-and-resting-membrane-potential.html" target="_blank" rel="noopener">Neurons and Resting Membrane Potential &#8599;</a></li>
  <li><strong>Friday (Jul 3)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day16_action-potentials-and-synaptic-transmission.html" target="_blank" rel="noopener">Action Potentials and Synaptic Transmission &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 4.2 Week 4 Discussion (posts Wed Jul 1, replies due Sun Jul 5)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week04_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 4 Discussion prompt"></iframe>
```

## 4.3 Week 4 Quiz (Fri Jul 3 to Sun Jul 5)

Honorlock, 20 min, one attempt.

---

# Module 5 (Week 5: Jul 6 to Jul 12)

Topics: CNS Organization (Brain and Spinal Cord), PNS and Autonomic Nervous System, Vision, Hearing and Equilibrium, Hormone Mechanisms, Major Endocrine Glands.

## 5.1 Week 5 Lab Workbooks (due Sun Jul 12)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day.</p>
<h3>Workbooks for Week 5</h3>
<ul>
  <li><strong>Monday (Jul 6)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day17_cns-organization-brain-and-spinal-cord.html" target="_blank" rel="noopener">CNS Organization: Brain and Spinal Cord &#8599;</a></li>
  <li><strong>Tuesday (Jul 7)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day18_pns-and-autonomic-nervous-system.html" target="_blank" rel="noopener">PNS and Autonomic Nervous System &#8599;</a></li>
  <li><strong>Thursday (Jul 9)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day19_vision.html" target="_blank" rel="noopener">Vision &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day19_hearing-and-equilibrium.html" target="_blank" rel="noopener">Hearing and Equilibrium &#8599;</a></li>
  <li><strong>Friday (Jul 10)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day20_hormone-mechanisms.html" target="_blank" rel="noopener">Hormone Mechanisms &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day20_major-endocrine-glands.html" target="_blank" rel="noopener">Major Endocrine Glands &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 5.2 Week 5 Discussion (posts Wed Jul 8, replies due Sun Jul 12)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week05_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 5 Discussion prompt"></iframe>
```

## 5.3 Week 5 Quiz (Fri Jul 10 to Sun Jul 12)

Honorlock, 20 min, one attempt.

---

# Module 6 (Week 6: Jul 13 to Jul 19)

Topics: Blood Composition and Hemopoiesis, Hemostasis and Blood Typing, Heart Anatomy and the Cardiac Cycle, Cardiac Conduction System, Blood Vessels and Hemodynamics.

## 6.1 Week 6 Lab Workbooks (due Sun Jul 19)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day.</p>
<h3>Workbooks for Week 6</h3>
<ul>
  <li><strong>Monday (Jul 13)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day21_blood-composition-and-hemopoiesis.html" target="_blank" rel="noopener">Blood Composition and Hemopoiesis &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day21_hemostasis-and-blood-typing.html" target="_blank" rel="noopener">Hemostasis and Blood Typing &#8599;</a></li>
  <li><strong>Tuesday (Jul 14)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day22_heart-anatomy-and-the-cardiac-cycle.html" target="_blank" rel="noopener">Heart Anatomy and the Cardiac Cycle &#8599;</a></li>
  <li><strong>Thursday (Jul 16)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day23_cardiac-conduction-system.html" target="_blank" rel="noopener">Cardiac Conduction System &#8599;</a></li>
  <li><strong>Friday (Jul 17)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day24_blood-vessels-and-hemodynamics.html" target="_blank" rel="noopener">Blood Vessels and Hemodynamics &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 6.2 Week 6 Discussion (posts Wed Jul 15, replies due Sun Jul 19)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week06_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 6 Discussion prompt"></iframe>
```

## 6.3 Week 6 Quiz (Fri Jul 17 to Sun Jul 19)

Honorlock, 20 min, one attempt.

---

# Module 7 (Week 7: Jul 20 to Jul 26)

Topics: Lymphatic System and Innate Immunity, Adaptive Immunity, Respiratory Anatomy and Mechanics, Gas Exchange and Transport, GI Tract Anatomy and Motility, Digestion and Absorption.

## 7.1 Week 7 Lab Workbooks (due Sun Jul 26)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day.</p>
<h3>Workbooks for Week 7</h3>
<ul>
  <li><strong>Monday (Jul 20)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day25_lymphatic-system-and-innate-immunity.html" target="_blank" rel="noopener">Lymphatic System and Innate Immunity &#8599;</a></li>
  <li><strong>Tuesday (Jul 21)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day26_adaptive-immunity.html" target="_blank" rel="noopener">Adaptive Immunity &#8599;</a></li>
  <li><strong>Thursday (Jul 23)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day27_respiratory-anatomy-and-mechanics.html" target="_blank" rel="noopener">Respiratory Anatomy and Mechanics &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day27_gas-exchange-and-transport.html" target="_blank" rel="noopener">Gas Exchange and Transport &#8599;</a></li>
  <li><strong>Friday (Jul 24)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day28_gi-tract-anatomy-and-motility.html" target="_blank" rel="noopener">GI Tract Anatomy and Motility &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day28_digestion-and-absorption.html" target="_blank" rel="noopener">Digestion and Absorption &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 7.2 Week 7 Discussion (posts Wed Jul 22, replies due Sun Jul 26)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week07_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 7 Discussion prompt"></iframe>
```

## 7.3 Week 7 Quiz (Fri Jul 24 to Sun Jul 26)

Honorlock, 20 min, one attempt.

---

# Module 8 (Week 8: Jul 27 to Aug 2)

Topics: Kidney Anatomy and Glomerular Filtration, Tubular Function and Urine Concentration, Fluid Electrolyte and Acid-Base Balance, Male Reproductive System, Female Reproductive System, Pregnancy A&P (Basics).

## 8.1 Week 8 Lab Workbooks (due Sun Aug 2)

```html
<p>This week you will hand-label four lab workbooks, one per pre-work day. Final week of the course.</p>
<h3>Workbooks for Week 8</h3>
<ul>
  <li><strong>Monday (Jul 27)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day29_kidney-anatomy-and-glomerular-filtration.html" target="_blank" rel="noopener">Kidney Anatomy and Glomerular Filtration &#8599;</a></li>
  <li><strong>Tuesday (Jul 28)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day30_tubular-function-and-urine-concentration.html" target="_blank" rel="noopener">Tubular Function and Urine Concentration &#8599;</a></li>
  <li><strong>Thursday (Jul 30)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day31_fluid-electrolyte-and-acid-base-balance.html" target="_blank" rel="noopener">Fluid, Electrolyte, and Acid-Base Balance &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day31_male-reproductive-system.html" target="_blank" rel="noopener">Male Reproductive System &#8599;</a></li>
  <li><strong>Friday (Jul 31)</strong>: <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day32_female-reproductive-system.html" target="_blank" rel="noopener">Female Reproductive System &#8599;</a> + <a href="https://drsrennie-stack.github.io/nonmajors/workbook_day32_pregnancy-a-p-basics.html" target="_blank" rel="noopener">Pregnancy A&amp;P (Basics) &#8599;</a></li>
</ul>
<p><strong>Hand-labeling is the integrity mechanism for this course.</strong> Typed or AI-generated labels are not accepted.</p>
```

## 8.2 Week 8 Discussion (posts Wed Jul 29, replies due Sun Aug 2)

```html
<iframe src="https://drsrennie-stack.github.io/nonmajors/week08_discussion.html" width="100%" height="1100" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Week 8 Discussion prompt"></iframe>
```

## 8.3 Week 8 Quiz (Fri Jul 31 to Sun Aug 2)

Honorlock, 20 min, one attempt. Final quiz of the course.

---

# Iframe quick reference (every iframe URL in one place)

| What | URL | Suggested height |
|---|---|---|
| Syllabus (Module 0) | `https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html` | 4200px |
| Week 1 discussion | `https://drsrennie-stack.github.io/nonmajors/week01_discussion.html` | 1100px |
| Week 2 discussion | `https://drsrennie-stack.github.io/nonmajors/week02_discussion.html` | 1100px |
| Week 3 discussion | `https://drsrennie-stack.github.io/nonmajors/week03_discussion.html` | 1100px |
| Week 4 discussion | `https://drsrennie-stack.github.io/nonmajors/week04_discussion.html` | 1100px |
| Week 5 discussion | `https://drsrennie-stack.github.io/nonmajors/week05_discussion.html` | 1100px |
| Week 6 discussion | `https://drsrennie-stack.github.io/nonmajors/week06_discussion.html` | 1100px |
| Week 7 discussion | `https://drsrennie-stack.github.io/nonmajors/week07_discussion.html` | 1100px |
| Week 8 discussion | `https://drsrennie-stack.github.io/nonmajors/week08_discussion.html` | 1100px |

If any iframe height looks wrong once it renders in Canvas, change the `height="…"` value and save.

---

# What to do once Canvas is built

1. Test one iframe URL in your browser before mass-pasting. If GitHub Pages hasn't refreshed yet, the syllabus link returns 404; wait 60 seconds and retry.
2. After pasting Module 0, click into the syllabus page in Student View. Confirm the TOC sidebar shows on the left and clicking a link jumps to the right section.
3. Set Module Requirements so students must view the syllabus and pass the acknowledgment quiz before Module 1 unlocks.
4. Publish modules week-by-week, not all at once. Open Module N on Friday of Week N-1 so students see what's coming.
