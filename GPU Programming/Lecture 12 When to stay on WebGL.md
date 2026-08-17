# Lecture 12 — When to stay on WebGL

**Week 12 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** decision table: feature → WebGL2 ping-pong or WebGPU compute; detect; pick one API for the final  
**Success check:** they can feature-detect, screenshot support, and write a one-page memo without rewriting the semester in three APIs

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: a decision you can freeze | Invariant: IGWT is web; WebGL2 still ships; WebGPU is taught without stranding labs; no CUDA`

## Board at the end (they photograph this)

```
need              stay WebGL2           move WebGPU
particles teach   FBO ping-pong         storage + compute
atomics / reduce  mip hack              compute atomics
lab browsers      always                detect + fallback

project: pick ONE api unless you demo both
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Decision, not a rewrite. Porting shaders is work. Pipelines are verbose. Gain: compute, less driver magic. canIuse is a screenshot they take, not a CDN widget in the product.

**Ask:** Must the final be both APIs? Wait. Want: no — pick one unless you explicitly demo both.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *compatibility, tools*.

**Do not:** Rewriting the semester in three APIs.

### Minutes 10–12 — Frame

**Say:** One-page decision for a capstone-shaped idea. Risk list. Still JS in the browser.

**Ask:** One reason to stay on WebGL?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Table feature → API. Fill three rows live.

**Board:** the decision tree. Circle detect.

**Say:** Risk list: Safari, validation, time to port.

**Ask:** One reason to move to WebGPU?

**They do:** On paper: their project row in the table.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** A one-page decision for their idea. Plant rewriting the semester in three APIs. Plant CUDA as a third column.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** canIuse screenshot + risk list. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: screenshot + risks. Homework: decision memo 1 page. Quiz: one reason WebGL, one WebGPU, detect. Next: choose a sim.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Fill the table | Plant three-API rewrite. |
| 10–30 | Detect in a stub page | Plant CUDA column. |
| 30–45 | Risk list | Safari / time. |
| 45–60 | They freeze one API | Circulate. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. canIuse screenshot.
2. risk list.

---

## Homework

1. Written: decision memo 1 page.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[GPU Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. rewriting the semester in three APIs.

## If we run long, cut

Vulkan. Keep the table + detect + one API.

## If we run short, add

Shader rewrite cost as a bullet.
