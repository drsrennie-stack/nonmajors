# BIOL 304 Pre-Launch Accessibility Checklist

A practical accessibility sweep you can run through in about 30 minutes before the term opens. Not a full WCAG audit. Catches the most common real problems for real students.

---

## Part 1: Custom HTML Documents (10 minutes)

Test the four files we built: `biol304_syllabus.html`, `biol304_course_home.html`, `biol304_reading_map.html`, `nonmajors_ap_rhythm_card.html`.

### Keyboard navigation test
Open each file. Press Tab repeatedly. Check:
- [ ] You can reach every link with the keyboard alone
- [ ] The focused link is visually obvious (a highlight, outline, or color change)
- [ ] Tab order follows the visual reading order (top to bottom, left to right)
- [ ] You can escape out of any interactive element

### Zoom test
On each file, press Ctrl+ (or Cmd+) until the browser is at 200% zoom. Check:
- [ ] All text is still readable without horizontal scrolling
- [ ] No content is cut off on the right edge
- [ ] Tables remain usable (may scroll horizontally, that's OK)

### Color contrast spot check
Use a free tool like [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). Pick three text-background pairs on each document:
- [ ] Body text on white: should pass AA (4.5:1 minimum)
- [ ] Headings on white: should pass AA
- [ ] Terra links on white: should pass AA

The palette was built to meet AA contrast, but checking three samples per document takes 2 minutes and catches anything I missed.

### Screen reader quick test (if you have VoiceOver on Mac or NVDA on Windows)
Open each file. Start the screen reader. Navigate with the reader's heading shortcut (H key in most readers). Check:
- [ ] Headings read in a sensible order
- [ ] Each document has exactly one H1 (the page title)
- [ ] Lists announce as lists, not as disconnected items

---

## Part 2: Canvas Course Setup (10 minutes)

Use Canvas's built-in accessibility checker on every page and assignment you create.

### On every Canvas page you create:
- [ ] Run the Accessibility Checker (the icon in the rich content editor toolbar, looks like a person)
- [ ] Fix any flagged issues before publishing

### Global Canvas settings:
- [ ] Course navigation is simplified (hide items students don't need)
- [ ] Course home is set to the Course Home page you built (Settings → Course Details → Course Home Page → Pages Front Page)
- [ ] Student view works — use "Student View" button in course settings to see what they see

### Iframes specifically:
- [ ] Every iframe has a `title` attribute (the Canvas cheat sheet snippets include this)
- [ ] Iframes show content, not just scrollbars (adjust height if needed)
- [ ] Test on mobile — open Canvas on your phone and check the iframes reflow

---

## Part 3: Videos and Media (5 minutes to set up, ongoing to maintain)

### Every video you record:
- [ ] Captions are turned on (Loom auto-captions, then review and correct before publishing)
- [ ] If the video references something visual, describe it out loud ("As you can see on the left side of the diagram...")
- [ ] Provide a transcript on request, or auto-generate from captions

### Third-party videos you link to:
- [ ] Only link to videos with captions
- [ ] If captions are auto-generated and inaccurate, note this or find a better source

---

## Part 4: Document and Image Uploads (5 minutes)

### Every PDF you upload:
- [ ] Is text-based (not a scanned image of text)
- [ ] Has been run through Canvas's Accessibility Checker if uploaded to a Canvas page

### Every image or diagram you upload:
- [ ] Has alt-text that describes the image (not just "diagram" — actually describe what it shows)
- [ ] Decorative images have empty alt-text (alt="") so screen readers skip them
- [ ] Images of text are avoided when possible (use actual text instead)

### The anatomy labs specifically:
- [ ] OpenStax figures used in labs have their original alt-text preserved
- [ ] If a figure's alt-text is minimal, add an extended description in the lab instructions

---

## Part 5: Going Live (Ongoing habits)

These are habits to maintain, not one-time checks.

- [ ] When a student asks about an accessibility issue, respond within 48 hours
- [ ] When you discover a barrier mid-term, fix it and announce the fix to the class
- [ ] When DSPS sends an accommodation letter, acknowledge it within 48 hours and confirm the plan
- [ ] When creating new content (announcements, handouts, quiz items), run the Canvas Accessibility Checker every time

---

## What This Checklist Does Not Do

Be honest with yourself about this document's limits:

- It does not certify WCAG 2.2 AA compliance
- It does not replace a professional accessibility audit
- It does not catch every possible barrier
- It does not test with every assistive technology combination

If you want full certification, request an accessibility review from ARC's Distance Education office or the Los Rios accessibility services team.

---

## Known ARC/Los Rios Resources

- **ARC DSPS:** dsps@arc.losrios.edu · (916) 484-8382 · [arc.losrios.edu/dsps](https://arc.losrios.edu/dsps)
- **Canvas accessibility support:** 24/7 via the help menu inside Canvas
- **Los Rios Distance Education:** Contact your department chair for referral to the district DE accessibility team if you find a systemic issue

---

## After the Sweep

Once you have run this checklist, the Accessibility statement document (`biol304_accessibility.html`) is honest when it says the course "has been designed with accessibility principles in mind." Without the sweep, that statement is aspirational. Running it once before launch makes it true.
