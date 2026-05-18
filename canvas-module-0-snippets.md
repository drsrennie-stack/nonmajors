# Canvas Module 0 — Paste-Ready Snippets (lean version)

Base URL for all iframes: **`https://drsrennie-stack.github.io/nonmajors/`**

## The lean approach

Module 0 used to have 14 separate Canvas items. It now has **3**. Everything else lives inside the single document-style syllabus at `biol304_syllabus.html`, navigable through its built-in table of contents. Fewer Canvas links, less to maintain, one canonical source of truth.

The three Module 0 items below are the only ones that must exist as native Canvas objects:

1. **Course Syllabus & Welcome** — a Canvas Page that iframes the syllabus hub.
2. **Welcome Discussion** — a Canvas Discussion topic (required for introductions and reply scaffolding).
3. **Start-Here Acknowledgment Quiz** — a Canvas Quiz (required to gate Module 1 unlock).

## How to use this file

For the Page below:

1. Open the Page in Canvas.
2. Click **Edit**.
3. Click the **HTML editor** icon (`</>`) at the top right of the editor.
4. Replace the contents with the code block under the page heading.
5. Switch back to the **Rich Content Editor** view and click **Save**.

For the Discussion and Quiz, follow the configuration notes in their sections (no iframe).

---

## 1. Course Syllabus & Welcome (Canvas Page)

Suggested iframe height: **4200px**. This is the full document-style syllabus.

```html
<p>Welcome to BIO 304. The syllabus below is your single point of reference for the course. Use the table of contents inside it to jump to welcome, course at a glance, learning outcomes, materials, the weekly rhythm, grading, deadlines, the 8-week schedule, how to reach me, integrity and AI policy, accessibility, RSI, tech setup, and the resource index.</p>
<p><a href="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" target="_blank" rel="noopener"><strong>Open the full syllabus in a new window &#8599;</strong></a></p>
<p><iframe src="https://drsrennie-stack.github.io/nonmajors/biol304_syllabus.html" width="100%" height="4200" style="border:1px solid #cfd6da;border-radius:8px;" loading="lazy" title="BIO 304 Syllabus"></iframe></p>
```

---

## 2. Welcome Discussion · BIO 304 (Canvas Discussion topic, no iframe)

**Title:** Welcome Discussion · BIO 304

**Settings:**
- Discussion type: **Threaded**
- Available from: course start date (Monday, June 8, 2026)
- Due: Sunday of Week 1
- Points: 5 to 10 (low-stakes welcome)
- Require initial post before viewing replies: **Yes**
- Reply required: **No**

**Prompt (paste into the message body):**

```html
<h2>Welcome to BIO 304</h2>
<p>Take a few minutes to introduce yourself. Share whatever feels right, but please touch on each of the following so your classmates and I know who you are:</p>
<ol>
  <li><strong>Your name</strong> and what you would like to be called.</li>
  <li><strong>Where you are in your education</strong>, and where you are headed. Pre-nursing, pre-med, pre-dental hygiene, allied health, or something else?</li>
  <li><strong>One specific body system or topic you are curious about</strong>. "How does my heart actually beat?" is a perfect answer.</li>
  <li><strong>One thing about your life outside of school</strong>: work, hobby, family, anything.</li>
  <li><strong>What time of day you do your best thinking</strong>. The pre-work is daily, and knowing your own rhythm will help you place it.</li>
</ol>
<p>Reply to at least two classmates by Sunday night. Look for someone who shares your interest or your time-of-day preference.</p>
<p>I will introduce myself here too, and respond to each of you in the first week.</p>
```

---

## 3. Start-Here Acknowledgment Quiz (Canvas Quiz)

The last item in Module 0. Use Classic Quizzes or New Quizzes depending on what ARC has enabled.

**Quiz settings:**
- Type: Practice or 5-point graded quiz
- Show one question at a time: **No**
- Time limit: **None**
- Allow multiple attempts: **Yes (unlimited)**
- Module Requirement: "Students must score at least 100% on this item" before Module 1 unlocks

**Questions:**

### Q1 (multiple choice, 1 point)
> When does new lecture pre-work release each week?

- [ ] Monday only
- [x] Monday, Tuesday, Thursday, and Friday
- [ ] Every day Monday through Sunday
- [ ] Wednesday only

Feedback (correct): "Right. Wednesday is for catching up and joining the discussion. Sunday closes the week."

### Q2 (multiple choice, 1 point)
> What is the academic integrity rule about lab workbooks?

- [ ] You can type your labels and submit a typed version.
- [x] You must print the unlabeled diagram and label every structure by hand.
- [ ] You can copy a labeled diagram from any textbook.
- [ ] You can have AI generate the labels for you.

Feedback (correct): "Hand labeling is the integrity mechanism for this course. Typed or AI-generated labels will not be accepted."

### Q3 (multiple choice, 1 point)
> When does the weekly quiz open and close?

- [ ] Opens Monday, closes Friday
- [ ] Opens Wednesday, closes Friday
- [x] Opens Friday, closes Sunday at 11:59 PM
- [ ] Opens Friday, closes Monday

Feedback (correct): "You have the full weekend to take the quiz. Don't wait until Sunday night."

### Q4 (multiple choice, 1 point)
> Which channel should you use to ask about your grade or a personal accommodation?

- [ ] The Virtual Office Hours discussion forum
- [x] Email or Canvas Inbox
- [ ] A public class discussion
- [ ] By posting in the welcome thread

Feedback (correct): "Anything confidential goes by email. Everything else belongs in the forum so your classmates can benefit from the answer."

### Q5 (true/false, 1 point)
> The pre-work hub uses spaced recall to surface cards I have rated as struggling more often than cards I have rated as easy.

- [x] True
- [ ] False

Feedback (correct): "Correct. The system schedules harder cards to come back sooner so you spend your time where you need it."

### Q6 (multiple choice, 1 point)
> What is the textbook for this course?

- [ ] A required hardcover textbook I need to purchase
- [x] OpenStax Anatomy and Physiology 2e, free online
- [ ] No textbook; everything is in the videos
- [ ] An e-book bundled with the course fee

Feedback (correct): "OpenStax is free. The Reading Map link inside the syllabus tells you which section supports each topic."

### Q7 (true/false, 1 point) — final agreement
> I have read the syllabus and I agree to the expectations described above.

- [x] True
- [ ] False

Feedback (correct): "Welcome. You are ready to start Week 1."

---

## What got dropped (and where it lives now)

Everything that was a separate Module 0 page is now an anchor inside `biol304_syllabus.html`:

| Was a Canvas Page | Now lives at |
|---|---|
| Welcome | `#welcome` |
| Syllabus Details | the full document |
| Technical Setup & Requirements | `#tech` |
| Submission Instructions | `#tech` |
| Academic Integrity & AI Policy | `#integrity` |
| How to Reach Me | `#reach` |
| Course Structure | `#rhythm`, `#grading`, `#schedule` |
| Course Dashboard | resource index `#resources` |
| Textbook & Materials | `#materials` |
| Accessibility & DSPS | `#access` |
| Reading Map | resource index `#resources` |
| Weekly Pacer | `#rhythm`, `#deadlines`, `#habits` |

Students hit one Canvas Page and have access to the whole syllabus via the sidebar table of contents.

---

## Module 0 setup checklist

1. Create the **Course Syllabus & Welcome** Page and paste the snippet from section 1.
2. Create the **Welcome Discussion** topic with the prompt from section 2.
3. Create the **Start-Here Acknowledgment Quiz** with the questions from section 3.
4. In Module 0 settings, require students to mark items 1 and 2 as **viewed/contributed** and to score 100% on the acknowledgment quiz before Module 1 unlocks.
5. Publish Module 0.
