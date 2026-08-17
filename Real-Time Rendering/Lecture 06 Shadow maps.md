# Lecture 6 — Shadow maps

**Week 6 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** depth from light  
**Success check:** Render depth from the light.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: depth from light | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
light P V → depth tex → compare
Two cameras.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Algorithm. A camera at the light.

**Ask:** Render depth from the light? Wait seven seconds. Take two answers.

**Board:** parked strip. Then light P V → depth tex → compare.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *depth from light*.

**Do not:** CSM speech without a single map.

### Minutes 10–12 — Frame

**Say:** Today’s question: depth from light. Kernel: depth from light. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: CSM speech without a single map.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Algorithm. A camera at the light.

**Say:** Projection. Ortho for directional.

**Say:** WebGL. DEPTH_COMPONENT texture.

**Ask:** Render depth from the light? Wait seven seconds. Take two answers.

**They do:** On paper: show shadow map as grayscale extra.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Plane + cube; directional shadow; bias slider.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** show shadow map as grayscale extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: show shadow map as grayscale extra.; mapSize 512 vs 2048 measured.. Homework: Written: compare function.; Code or three.js with explanation of bias.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: depth from light | Plant the first common mistake. |
| 10–30 | Plane + cube; directional shadow; bias slider. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. show shadow map as grayscale extra.
2. mapSize 512 vs 2048 measured.

---

## Homework

1. Written: compare function.
2. Code or three.js with explanation of bias.

---

## Quiz next meeting (they hear this now)

1. who renders the map (4)
2. bias (3)
3. ortho why (3)


## Snippet

```glsl
float shadow = (zLight > mapZ + bias) ? 0.3 : 1.0;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Algorithm.** A camera at the light. Store depth. If the main pixel is farther than the map, it's in shadow.

**2. Projection.** Ortho for directional. Perspective for spot. Frustum must cover the scene — too tight acne, too loose jaggy.

**3. WebGL.** DEPTH_COMPONENT texture. Three.js does this; students should still draw the light frustum.

---

## Common mistakes

1. CSM speech without a single map.
2. bias 0.1.

## If we run long, cut

WebGL

## If we run short, add

mapSize 512 vs 2048 measured.
