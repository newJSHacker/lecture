# Lecture 10 — Post stack

**Week 10 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** order of operations  
**Success check:** Write a stack order.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: order of operations | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
hdr → shadowed shade → bloom → tonemap → lut
Graph.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Order matters. Bloom on HDR.

**Ask:** a stack order? Wait seven seconds. Take two answers.

**Board:** parked strip. Then hdr → shadowed shade → bloom → tonemap → lut.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *order of operations*.

**Do not:** Eight Instagram filters as 'RTR'.

### Minutes 10–12 — Frame

**Say:** Today’s question: order of operations. Kernel: order of operations. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: eight Instagram filters as 'RTR'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Order matters. Bloom on HDR.

**Say:** Look dev. A product shot is a stack, not one shader.

**Say:** Kill switches. Each pass toggles for grading and for perf.

**Ask:** a stack order? Wait seven seconds. Take two answers.

**They do:** On paper: one LUT extra (tiny 16³ or 2D strip).

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Three toggles: bloom, grain, vignette; freeze order in README.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** one LUT extra (tiny 16³ or 2D strip).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: one LUT extra (tiny 16³ or 2D strip).; screenshot matrix.. Homework: Written: your order and why.; graph figure.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: order of operations | Plant the first common mistake. |
| 10–30 | Three toggles: bloom, grain, vignette; freeze order in README. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. one LUT extra (tiny 16³ or 2D strip).
2. screenshot matrix.

---

## Homework

1. Written: your order and why.
2. graph figure.

---

## Quiz next meeting (they hear this now)

1. tonemap vs bloom order (4)
2. LUT (3)
3. kill switch (3)


## Snippet

```
shade(HDR) → bloom → tonemap → sRGB → grain
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Order matters.** Bloom on HDR. Tonemap before 8-bit. Grain after. LUT last or before grain — pick.

**2. Look dev.** A product shot is a stack, not one shader.

**3. Kill switches.** Each pass toggles for grading and for perf.

---

## Common mistakes

1. eight Instagram filters as 'RTR'.
2. undocumented order.

## If we run long, cut

Kill switches

## If we run short, add

screenshot matrix.
