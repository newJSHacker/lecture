# Lecture 13 — Polish and performance

**Week 13 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** pooling, culling 2D  
**Success check:** Skip draw if off canvas.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: pooling, culling 2D | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
offscreen skip
Cull.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Culling. AABB vs canvas.

**Ask:** Skip draw if off canvas? Wait seven seconds. Take two answers.

**Board:** parked strip. Then offscreen skip.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pooling, culling 2D*.

**Do not:** Pooling without measuring.

### Minutes 10–12 — Frame

**Say:** Today’s question: pooling, culling 2D. Kernel: pooling, culling 2D. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: pooling without measuring.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Culling. AABB vs canvas.

**Say:** Pooling. Reuse particles.

**Say:** Measure. performance.now frames.

**Ask:** Skip draw if off canvas? Wait seven seconds. Take two answers.

**They do:** On paper: pool extra.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: 1000 particles: naive vs skip-offscreen.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** pool extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: pool extra.; fps readout.. Homework: Written: when to pool.; Code: cull.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: pooling, culling 2D | Plant the first common mistake. |
| 10–30 | 1000 particles: naive vs skip-offscreen. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. offscreen skip (4)
2. pool (3)
3. overdraw (3)


## Snippet

```js
if (x < -r || x > w + r) return;
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Culling.** AABB vs canvas. CG geometry AABB.

**2. Pooling.** Reuse particles.

**3. Measure.** performance.now frames.

---

## Common mistakes

1. pooling without measuring.
2. invented fps.

## If we run long, cut

Measure

## If we run short, add

fps readout.
