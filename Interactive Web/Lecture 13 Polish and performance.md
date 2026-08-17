# Lecture 13 — Polish and performance

**Week 13 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** skip draw if AABB is off-canvas; pool instead of new per particle; measure with performance.now  
**Success check:** they toggle culling on 1000 particles and can say they must measure before pooling

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: the same engine, fewer wasted draws | Invariant: cull is a boolean skip; pooling is reuse; do not invent fps`

## Board at the end (they photograph this)

```
if (x < -r || x > w + r || y < -r || y > h + r) return;  // skip draw

pool:  dead[i] = true;  reuse slot instead of new
measure:  t0 = performance.now();  …  t1

invented fps           =  fail
pooling without a number =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: DevTools screenshot of two runs, cull on vs off | photo of numbers you just took |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Week 12 spawned freely. Today we skip offscreen draw and we reuse slots. Computational Geometry AABB is the test. Same rule as Modern JS week 11: measure or omit. 08-cull.html already has the toggle.

**Ask:** If a particle is off-canvas, do we still update(dt)? Wait. Want: usually yes — it may come back; we skip render.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pooling, culling 2D*.

**Do not:** Pooling without measuring.

### Minutes 10–12 — Frame

**Say:** Culling: AABB vs canvas. Pooling: reuse particles. Measure with performance.now on a batch — not an fps HUD you made up. Overdraw named.

**Ask:** Does culling replace a smaller spawn cap?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Update can still run. Render returns early. Write the four inequalities.

**Board:** offscreen skip. Pool slot. now() wrap.

**Say:** Toggle cull like the demo. Read two now() deltas. No fps slogan.

**Ask:** When is pooling wasted work?

**They do:** On paper: pool extra — acquire/release two functions.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** 1000 particles: naive vs skip-offscreen. Demo Interactive Web/code/08-cull.html (checkbox; hint says do not invent fps). Plant an fps number on the board. Erase it. Plant pooling without a measure.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pool extra. Optional readout of two now() numbers — not an fps widget. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pool extra; measured readout. Homework: when to pool; cull. Quiz: offscreen skip, pool, overdraw. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | AABB skip draw | Plant skipping update too, then discuss. |
| 10–30 | 1000 particles toggle | 08-cull.html. Measure, no fps. |
| 30–45 | pool acquire/release | Plant new every spawn. |
| 45–60 | They write two now() times | Circulate. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. pool extra.
2. fps readout.

---

## Homework

1. Written: when to pool.
2. Code: cull.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
if (x < -r || x > w + r) return;
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. pooling without measuring.
2. invented fps.

## If we run long, cut

Pooling if cull is not in. Keep skip-draw + measure.

## If we run short, add

A measured on/off table, two rows, no fps.
