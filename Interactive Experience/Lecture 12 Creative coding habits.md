# Lecture 12 — Creative coding habits

**Week 12 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one seed, one palette, one motion; cite assets  
**Success check:** they can type a seed and regenerate a small composition without fifty sliders

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: choice under constraint | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
seed  →  rand(i)  →  pose / color

palette of 5
one motion

cite:  models, HDRI, shaders, AI textures
leva is optional; it does not replace a story
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Creative coding is not 50 sliders. One seed, one palette, one motion. Unlicensed assets fail. AI textures: still cite — AI course later, same table.

**Ask:** If I change the seed, do I get the same piece? Wait. Want: a different piece, deterministically.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *constraints, seeds*.

**Do not:** 50 sliders, no taste.

### Minutes 10–12 — Frame

**Say:** Deterministic rand. PNG export extra. Integrity: shaders and models cited.

**Ask:** What belongs in the asset table this week?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Constraint is the craft.

**Board:** seed → rand → composition. Palette of 5.

**Say:** leva is a tool. A story beat still wins.

**Ask:** Why is an unseeded Math.random a problem for a report?

**They do:** On paper: seed field + three parameters it drives.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Seed field regenerates a composition. Plant 50 sliders. Plant an unlicensed HDRI. Cite or cut.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Seed + palette of 5. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: palette; png extra. Homework: citations. Quiz: seed, palette, cite. Next: critique.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Seeded rand | Plant Math.random soup. |
| 15–40 | Palette of 5 | Plant 50 sliders. |
| 40–55 | Cite the HDRI | Unlicensed plant. |
| 55–60 | They regenerate | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. palette of 5.
2. png export extra.

---

## Homework

1. Written: constraints you chose.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
function rand(i){ return fract(sin(i*78.23)*43758.5); }
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 50 sliders, no taste.
2. unlicensed assets.

## If we run long, cut

Full generative-art syllabus. Keep seed + cite.

## If we run short, add

PNG export extra.
