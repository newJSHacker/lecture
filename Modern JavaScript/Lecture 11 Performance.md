# Lecture 11 — Performance

**Week 11 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** performance.now() before/after; allocations in a hot loop; reuse vs new  
**Success check:** they measure two versions of a loop and refuse to ship a micro-opt without a number they just took

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/07-loop.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: a number from the machine, not a vibe | Invariant: invented timings are forbidden; measure or omit; do not invent fps`

## Board at the end (they photograph this)

```
const t0 = performance.now();
… work …
const t1 = performance.now();   // ms, this run, this machine

hot loop:  no new Vec2 per pixel
prealloc  vs  push in a growing array

Big-O name from Programming — not a substitute for a measure
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: Performance panel screenshot of two measures | photo; no fps caption you did not record |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** A janky game loop is often allocations, not ‘JavaScript is slow.’ Same rule as CG reports: invented timings are a fail. Today we measure.

**Ask:** If you did not call performance.now(), may you write ‘twice as fast’ in the report? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *measure, GC, hot loops*.

**Do not:** Optimizing unreadably without numbers.

### Minutes 10–12 — Frame

**Say:** Measure. GC: new objects per pixel die. Reuse vectors in a renderer. Big-O from Programming week 10 is the sketch; the lab is a table of measured runs. Profiling tab named — optional.

**Ask:** Why is new {x,y} inside a 1e7 loop a GC story?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two runs, same machine, same input size. Write both numbers. Do not invent fps.

**Board:** performance.now wrap. Alloc vs reuse. Prealloc length vs push.

**Say:** Unreadable micro-opt without a number is a fail. Cap the story at one rewrite.

**Ask:** What belongs in the homework table? Want: n, version A ms, version B ms — not a slogan.

**They do:** On paper: the measure snippet and a two-row table header.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Sum 1e7 numbers; compare push in loop vs prealloc. Demo Modern JavaScript/code/07-loop.html for a dt-capped rAF — we do not quote fps from it. Read the two now() deltas out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Don't ship a micro-opt without a number. One GC-friendly rewrite. Eight minutes to fill the table even if the rewrite is incomplete.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: measured pair + one GC-friendly rewrite. Homework: when not to optimize; measured table. Quiz: performance.now, alloc in pixel loop, prealloc.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | now() wrap | Plant a claimed speedup with no numbers. |
| 10–30 | push vs prealloc 1e7 | Read both times. No fps. |
| 30–45 | alloc in a fake pixel loop | Reuse one object. |
| 45–60 | They fill a two-row table | Circulate. |

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

None this meeting.


## Snippet

```js
const t0 = performance.now();
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Optimizing unreadably without numbers.

## If we run long, cut

Big-O recap. Keep measure + one alloc rewrite.

## If we run short, add

One GC-friendly rewrite they can screenshot.
