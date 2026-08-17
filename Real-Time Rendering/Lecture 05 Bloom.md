# Lecture 5 — Bloom

**Week 5 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** bright pass + blur + add  
**Success check:** Extract highlights.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: bright pass + blur + add | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
threshold → blur → combine
Three FBOs.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Pipeline. Same as WebGL post.

**Ask:** Extract highlights? Wait seven seconds. Take two answers.

**Board:** parked strip. Then threshold → blur → combine.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *bright pass + blur + add*.

**Do not:** Bloom as a substitute for lighting.

### Minutes 10–12 — Frame

**Say:** Today’s question: bright pass + blur + add. Kernel: bright pass + blur + add. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: bloom as a substitute for lighting.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Pipeline. Same as WebGL post.

**Say:** Artifacts. Fireflies, threshold too low, huge kernel.

**Say:** Three.js. UnrealBloomPass as oracle **after** they draw the boxes.

**Ask:** Extract highlights? Wait seven seconds. Take two answers.

**They do:** On paper: threshold slider.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Bloom a bright sphere; toggle.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** threshold slider.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: threshold slider.; half-res extra.. Homework: Written: three passes.; screenshots on/off.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: bright pass + blur + add | Plant the first common mistake. |
| 10–30 | Bloom a bright sphere; toggle. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. bright pass (3)
2. separable (4)
3. why HDR first (3)


## Snippet

```glsl
vec3 hi = max(c - vec3(1.0), vec3(0.0));
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Pipeline.** Same as WebGL post. Threshold on HDR. Blur. Combine after tonemap or before — pick a policy and stick to it.

**2. Artifacts.** Fireflies, threshold too low, huge kernel.

**3. Three.js.** UnrealBloomPass as oracle **after** they draw the boxes.

---

## Common mistakes

1. bloom as a substitute for lighting.
2. full-res 12-tap in all directions naive 2D.

## If we run long, cut

Three.js

## If we run short, add

half-res extra.
