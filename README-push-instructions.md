# BIO 304 — strip misplaced anatomical position images

## What got found

Scanned both repos for the three anatomical position images (anterior-bodyUE, anterior-bodyLE, posterior-lateral):

- **BIO 004**: only on `anatomical-terminology.html` — correct, no action needed
- **BIO 304**: on 35 pages, only 1 legitimate (`body-regions.html`) → **34 pages have them misplaced**

## What this push fixes

Strips the entire "plate" block (3 images + "Click any image to enlarge" caption) from all 34 misplaced pages. Leaves `body-regions.html` alone since that's where they belong. Pages affected:

action-potentials-synapses, adaptive-immunity, appendicular-skeleton, axial-skeleton, blood-composition, blood-vessels-hemodynamics, bone-tissue, cardiac-conduction, cell-structure, cns-organization, connective-tissues, cross-bridge-cycle, digestion-absorption, epithelial-tissue, female-reproductive, fluid-electrolyte-acid-base, gas-exchange-transport, gi-anatomy-motility, hearing-equilibrium, heart-anatomy, hemostasis-blood-typing, hormone-mechanisms, joints-and-movements, kidney-anatomy-gfr, lymphatic-innate-immunity, major-endocrine-glands, male-reproductive, membrane-transport, motor-units, muscle-nervous-tissue, neurons-resting-potential, pns-autonomic, pregnancy-basics, respiratory-anatomy

## Push commands

```bash
cd ~/Documents/nonmajors
cp "/Users/sharilynrennie/Documents/Claude/Projects/Lecture Slides/_PUSH-TO-GITHUB/BIO-304-strip-misplaced-images/"*.html .
git add *.html
git status        # should show 34 modified
git commit -m "Strip misplaced anatomical position images from non-anatomy pages"
git push origin main
```

## Verify after push

Wait 2 min, open any affected page in incognito, e.g.:

https://drsrennie-stack.github.io/nonmajors/cell-structure.html
https://drsrennie-stack.github.io/nonmajors/membrane-transport.html

The three anatomical-position image cards should be GONE. Page should jump straight from "By the end" learning objectives into the content tables.

## What's next

After this push, every page will be clean of the wrong images. Then we go page by page and add the RIGHT images (with OpenStax fallback where you don't have your own). Suggest doing 5-10 pages per batch.

First batch I'd recommend (your top-priority lecture pages):
1. cell-structure.html → labeled cell + plasma membrane + protein secretion (3-image slider)
2. membrane-transport.html → passive vs active + diffusion types + tonicity (3-image slider)
3. epithelial-tissue.html → classification grid (single image)
4. connective-tissues.html → CT types collage
5. muscle-nervous-tissue.html → muscle + neuron close-ups

Tell me when you've pushed this strip-fix and I'll start on the first batch.
