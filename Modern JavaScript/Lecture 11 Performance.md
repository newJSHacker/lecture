# Lecture 11 — Performance

**Week 11 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** measure, GC, hot loops  
**Success check:** Measure with performance.now().

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/07-loop.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: measure, GC, hot loops | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
performance.now()
Timer.
Alloc vs reuse.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Measure. Invented timings forbidden.

**Ask:** Measure with performance.now()? Wait seven seconds. Take two answers.

**Board:** parked strip. Then performance.now().

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *measure, GC, hot loops*.

**Do not:** Optimizing unreadably without numbers.

### Minutes 10–12 — Frame

**Say:** Today’s question: measure, GC, hot loops. Kernel: measure, GC, hot loops. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Optimizing unreadably without numbers.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Measure. Invented timings forbidden.

**Say:** Allocations. new objects per pixel is death.

**Say:** Big-O. From Programming week 10.

**Ask:** Measure with performance.now()? Wait seven seconds. Take two answers.

**They do:** On paper: Don't ship a micro-opt without a number.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Sum 1e7 numbers; compare push in loop vs prealloc.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Don't ship a micro-opt without a number.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Don't ship a micro-opt without a number.; One GC-friendly rewrite.. Homework: Written: when not to optimize.; Code: measured table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: measure, GC, hot loops | Plant the first common mistake. |
| 10–30 | Sum 1e7 numbers; compare push in loop vs prealloc. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/07-loop.html` as the after-class check, not as the lecture.

---

## Lab

1. Don't ship a micro-opt without a number.
2. One GC-friendly rewrite.

---

## Homework

1. Written: when not to optimize.
2. Code: measured table.

---

## Quiz next meeting (they hear this now)

1. performance.now (3)
2. alloc in pixel loop (4)
3. prealloc (3)


## Snippet

```js
const t0 = performance.now();
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Measure.** Invented timings forbidden. Same rule as CG reports.

**2. Allocations.** new objects per pixel is death. Reuse vecs in a renderer.

**3. Big-O.** From Programming week 10. Profiling tab name.

---

## Common mistakes

1. Optimizing unreadably without numbers.

## If we run long, cut

Big-O

## If we run short, add

One GC-friendly rewrite.
