# Canvas Module 0 — Paste-Ready Snippets (lean version)

Base URL for all iframes: **`https://drsrennie-stack.github.io/nonmajors/`**

## The lean approach

Module 0 has **4 native Canvas items**. The syllabus, welcome discussion, and AI Honor Contract are all iframed from branded HTML pages in the GitHub Pages repo, so they render in your course palette instead of plain Canvas styling.

1. **Course Syllabus & Welcome** — Canvas Page that iframes `biol304_syllabus.html`
2. **Welcome Discussion** — Canvas Discussion topic that iframes `welcome_discussion.html` in the prompt body
3. **Start-Here Syllabus Quiz** — Canvas Quiz with 8 high-yield questions
4. **AI Honor Contract** — Canvas Assignment where students upload a signed PDF, generated from the branded `ai_honor_contract.html` form

## How to use this file

For each item below: open the matching Canvas object, switch to the HTML editor (`</>` icon), paste the code block, and save.

---

## 1. Course Syllabus & Welcome (Canvas Page)

Suggested iframe height: **4200px**.

```html
<p>Welcome to BIO 304. The syllabus below is your single point of reference for the course. Use the table of contents inside it to jump to any section: welcome, course at a glance, learning outcomes, materials, the weekly rhythm, grading, deadlines, the 8-week schedule, how to reach me, integrity and AI policy, accessibility, regular substantive interaction, tech setup, and the resource index.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" target="_blank" rel="noopener"><strong>Open the full syllabus in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" width="100%" height="4200" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="BIO 304 Syllabus"></iframe></p>
```

---

## 2. Welcome Discussion (Canvas Discussion topic)

**Settings:**
- Title: `Welcome Discussion · BIO 304`
- Type: Threaded
- Available: Mon Jun 8, 12:00 AM
- Initial post due: Fri Jun 12, 11:59 PM
- Replies due: Sun Jun 14, 11:59 PM
- Points: 5 (low-stakes welcome)
- Require initial post before viewing replies: Yes

**Paste this into the prompt body** (Canvas Discussion HTML editor). The iframe loads the branded welcome page; the short text above it keeps Canvas's notification preview readable.

```html
<p>Welcome to BIO 304. Read the prompt below and post your introduction by Friday. Reply to at least two classmates by Sunday.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/welcome_discussion.html" target="_blank" rel="noopener"><strong>Open the welcome prompt in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/welcome_discussion.html" width="100%" height="1450" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="Welcome Discussion prompt"></iframe></p>
```

---

## 3. Start-Here Acknowledgment Quiz (Canvas Quiz)

8 questions covering the load-bearing facts in the syllabus. Use Canvas's Classic Quizzes or New Quizzes.

**Settings:**
- Title: `Start-Here Syllabus Quiz`
- Type: 8-point graded quiz (or practice, your call)
- Show one question at a time: No
- Time limit: None
- Allow multiple attempts: Yes, unlimited
- Module Requirement: Must score 100% before Module 1 unlocks

### Q1 (multiple choice, 1 point) — Course pace
> This is a 4-credit course delivered in 8 weeks. Approximately how many total hours per week should you plan for, per federal Carnegie Unit standards?

- [ ] 5 to 8 hours per week
- [ ] 10 to 12 hours per week
- [x] 22 to 24 hours per week
- [ ] 30 to 35 hours per week

Feedback (correct): "Right. About 8 to 10 of those hours are pre-work videos and the Wednesday lab block; the other 12 to 15 are outside-of-class study. Block both buckets on your calendar before Week 1."

### Q2 (multiple choice, 1 point) — Pre-work release schedule
> Which days does new lecture pre-work release each week?

- [ ] Monday only
- [x] Monday, Tuesday, Thursday, and Friday
- [ ] Every day Monday through Sunday
- [ ] Wednesday only

Feedback (correct): "Wednesday is for catching up on labs and joining the discussion. The weekend is for the quiz."

### Q3 (multiple choice, 1 point) — Quiz window
> When does the weekly quiz open and close?

- [ ] Opens Monday, closes Friday
- [ ] Opens Wednesday, closes Friday
- [x] Opens Friday at 12:00 AM, closes Sunday at 11:59 PM
- [ ] Opens Friday, closes Monday

Feedback (correct): "You have the full Fri to Sun window. Don't wait until Sunday night. Honorlock issues happen at the worst times."

### Q4 (multiple choice, 1 point) — Hand-labeling integrity rule
> What is the academic integrity rule about lab workbooks?

- [ ] You can type your labels and submit a typed version.
- [x] You must print the unlabeled diagram and label every structure by hand.
- [ ] You can copy a labeled diagram from any textbook.
- [ ] You can have AI generate the labels for you.

Feedback (correct): "Hand labeling is the integrity mechanism for this course. Typed or AI-generated labels will not be accepted."

### Q5 (multiple choice, 1 point) — Grading weights
> Which component is the LARGEST single weight in your grade?

- [ ] Lab workbooks (30%)
- [x] Pre-work engagement (40%)
- [ ] Weekly discussions (10%)
- [ ] Weekly quizzes (20%)

Feedback (correct): "Daily video viewing and spaced recall are 40% of your grade. Show up every day and this component takes care of itself."

### Q6 (multiple choice, 1 point) — DSPS accommodations
> If you have DSPS accommodations, when must you present your accommodation letter to Dr. Rennie?

- [ ] Whenever you happen to need them
- [ ] Before the final exam
- [x] In Week 1, so adjustments are in place before your first deadline
- [ ] Only if you fail a quiz first

Feedback (correct): "You are required to present your DSPS letter in Week 1. Accommodations are always honored, but I need the letter early to set up Honorlock extensions and any other adjustments before any deadline arrives."

### Q7 (multiple choice, 1 point) — Late work
> What is the late work policy in this course?

- [ ] 10% deduction per day late
- [ ] Late work accepted up to one week after the deadline
- [x] Late work earns zero points, no exceptions
- [ ] Late work accepted with a doctor's note

Feedback (correct): "Late work is zero. If life is hitting hard, email me BEFORE a deadline. Solutions exist before the deadline. They do not exist after."

### Q8 (multiple choice, 1 point) — Communication channel
> You have a question about how a concept on Tuesday's pre-work video connects to Friday's content. Where should you post it?

- [x] The Virtual Office Hours forum
- [ ] My personal cell phone
- [ ] Your group chat with classmates
- [ ] Email to Dr. Rennie

Feedback (correct): "The forum is the preferred channel for anything non-confidential, because other students learn from your question. Email is for confidential matters only (grades, accommodations, personal circumstances)."

---

## 4. AI Honor Contract (Canvas Assignment)

Students open the branded contract page, type their name, date, statement, and signature, print to PDF, and upload the PDF here.

**Assignment settings:**
- Title: `AI Honor Contract`
- Submission type: Online → File upload (PDF)
- Allowed file extensions: pdf
- Allowed attempts: unlimited (until due)
- Due: Tue Jun 9, 11:59 PM (end of Week 1 day 2)
- Points: 5 (complete or incomplete, all-or-nothing)
- Module Requirement: must submit before Module 1 unlocks

**Paste this into the assignment body** (Canvas Assignment HTML editor):

```html
<p>Read the AI Use Policy below, fill in your name, date, statement, and typed signature directly in the embedded form, click <strong>Print / Save as PDF</strong>, save the file as <code>LastName_AI_Honor_Contract.pdf</code>, and upload it here.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/ai_honor_contract.html" target="_blank" rel="noopener"><strong>Open the AI Honor Contract in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/ai_honor_contract.html" width="100%" height="3400" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="AI Honor Contract"></iframe></p>
<h3>If you ever need to submit an AI Transparency Document later</h3>
<p>When an assignment in this course permits AI use AND you use AI, you must submit a completed AI Transparency Document alongside your assignment file. The form lives at <a href="https://drsrennie-stack.github.io/nonmajors/ai_transparency_document.html" target="_blank" rel="noopener"><strong>ai_transparency_document.html &#8599;</strong></a>. Bookmark it. You will not need it for lab workbooks, discussions, or quizzes (AI is not permitted on those).</p>
```

---

## What got dropped (and where it lives now)

Everything that used to be a separate Module 0 Canvas Page is now an anchor inside `biol304_syllabus.html`:

| Was a Canvas Page | Now lives at |
|---|---|
| Welcome letter | `#welcome` |
| Syllabus details | the full document |
| Tech setup & requirements | `#tech` |
| Submission instructions | `#tech` |
| Academic integrity & AI policy | `#integrity` |
| How to reach me | `#reach` |
| Course structure | `#rhythm`, `#grading`, `#schedule` |
| Course dashboard | resource index `#resources` |
| Textbook & materials | `#materials` |
| Accessibility & DSPS | `#access` |
| Reading map | resource index `#resources` |
| Weekly pacer | `#rhythm`, `#deadlines`, `#habits` |

Students hit one Canvas Page, then use the syllabus's sticky TOC to navigate.

---

## Module 0 setup checklist

1. Create the **Course Syllabus & Welcome** Page and paste the snippet from section 1.
2. Create the **Welcome Discussion** topic and paste the snippet from section 2.
3. Create the **Start-Here Syllabus Quiz** and build the 8 questions from section 3.
4. Create the **AI Honor Contract** Assignment and paste the snippet from section 4.
5. In Module 0 settings, set requirements: students must mark item 1 viewed, contribute to item 2, score 100% on item 3, and submit item 4 before Module 1 unlocks.
6. Publish Module 0.
