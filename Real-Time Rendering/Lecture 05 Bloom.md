# Lecture 5 — Bloom

**Week 5 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** bloom: bright-pass → blur pass(es) → add; on HDR, named  
**Success check:** they can extract highlights, blur, combine, and toggle the three passes

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: three named bloom passes | Invariant: bloom is leftover HDR energy, not a substitute for lighting`

## Board at the end (they photograph this)

```
PASS  bright    max(c - t, 0)   on HDR
PASS  blur      separable H then V   (not naive 12×12)
PASS  add       combine  (policy: before or after tonemap — freeze one)

half-res  is a budget  (measure if you claim)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Same FBO idea as WebGL post. Draw the boxes before UnrealBloomPass. Fireflies and a huge kernel are artifacts. We do not invent fps; half-res is a named cut.

**Ask:** Which pass extracts the sun? Wait. Want: bright / threshold.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *bright pass + blur + add*.

**Do not:** Bloom as a substitute for lighting.

### Minutes 10–12 — Frame

**Say:** Threshold on HDR. Separable blur. Combine policy frozen in README. Three.js UnrealBloomPass is the oracle after the boxes.

**Ask:** Why HDR before bloom?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three FBO boxes. Label each pass.

**Board:** threshold → blur → add. Circle separable.

**Say:** Threshold slider is a uniform. Toggle the add pass.

**Ask:** Why not a naive 2D 12-tap?

**They do:** On paper: the three pass names in order.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Bloom a bright sphere; toggle. Plant bloom as lighting. Half-res extra — if they claim speed, they measure on this machine.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Threshold slider. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: threshold + half-res extra. Homework: three passes written; on/off screenshots. Quiz: bright pass, separable, why HDR first.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name bright pass | Plant bloom as lighting. |
| 10–30 | Separable blur | Plant naive 12×12. |
| 30–45 | Add + toggle | Freeze combine policy. |
| 45–60 | Half-res if time | Measure or omit fps. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. threshold slider.
2. half-res extra.

---

## Homework

1. Written: three passes.
2. screenshots on/off.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec3 hi = max(c - vec3(1.0), vec3(0.0));
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. bloom as a substitute for lighting.
2. full-res 12-tap in all directions naive 2D.

## If we run long, cut

UnrealBloomPass internals. Keep three named passes.

## If we run short, add

Half-res as a documented budget.
