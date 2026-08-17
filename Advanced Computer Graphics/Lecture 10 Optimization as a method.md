# Lecture 10 — Optimization as a method

**Week 10 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** profile, cut, measure  
**Success check:** Pick a slow scene (theirs or a starter).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: profile, cut, measure | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
before / after table
Before/after.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Method. Advanced CG is also **engineering**.

**Ask:** Pick a slow scene (theirs or a starter)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then before / after table.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *profile, cut, measure*.

**Do not:** Optimizing without a before row.

### Minutes 10–12 — Frame

**Say:** Today’s question: profile, cut, measure. Kernel: profile, cut, measure. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: optimizing without a before row.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Method. Advanced CG is also **engineering**.

**Say:** Cuts that are algorithms. BVH for the tracer (geometry course).

**Say:** Paper vs product. A cut that changes the image must be screenshotted.

**Ask:** Pick a slow scene (theirs or a starter)? Wait seven seconds. Take two answers.

**They do:** On paper: one algorithm cut.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Two-row table on a named device.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** one algorithm cut.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: one algorithm cut.; one asset cut.. Homework: Written: what you would not cut.; table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: profile, cut, measure | Plant the first common mistake. |
| 10–30 | Two-row table on a named device. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. one algorithm cut.
2. one asset cut.

---

## Homework

1. Written: what you would not cut.
2. table.

---

## Quiz next meeting (they hear this now)

1. CPU vs GPU (3)
2. image-changing cut (4)
3. device (3)


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Method.** Advanced CG is also **engineering**. Same rule as RTR week 12, now on a heavier scene (tracer spp, volume steps, lights).

**2. Cuts that are algorithms.** BVH for the tracer (geometry course). Russian roulette. Tile culling.

**3. Paper vs product.** A cut that changes the image must be screenshotted.

---

## Common mistakes

1. optimizing without a before row.
2. fantasy 200 fps.

## If we run long, cut

Paper vs product

## If we run short, add

one asset cut.
