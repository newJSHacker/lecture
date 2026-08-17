# Lecture 6 — Shadow maps

**Week 6 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** shadow-map pass: depth from light; shade pass: compare z  
**Success check:** they can render a depth map from the light, compare, and show the map as grayscale

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: two cameras: eye and light | Invariant: a camera at the light is a named pass; CSM without one map is a speech`

## Board at the end (they photograph this)

```
PASS 1  light camera  →  depth tex     (ortho if directional)
PASS 2  eye shade     →  compare zLight vs mapZ + bias

bias 0.1 is huge
mapSize: measure 512 vs 2048 on this device, or omit
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Algorithm: store depth from the light. If the main pixel is farther than the map, it is in shadow. WebGL DEPTH_COMPONENT. Three.js does this — they still draw the light frustum.

**Ask:** Who renders the shadow map — the eye or the light? Wait. Want: the light.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *depth from light*.

**Do not:** CSM speech without a single map.

### Minutes 10–12 — Frame

**Say:** Ortho for directional, perspective for spot. Frustum too tight → acne, too loose → jaggy. Bias is a uniform they will plant wrong.

**Ask:** Why ortho for a directional light?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two cameras. Two frustums.

**Board:** light P V → depth → compare. Circle bias.

**Say:** Show the map as grayscale extra. mapSize change is a measurement row, not a claimed fps.

**Ask:** Write the compare in one line (teaching).

**They do:** On paper: pass 1 vs pass 2.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Plane + cube; directional shadow; bias slider. Plant CSM speech. Plant bias 0.1. Grayscale map.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Show shadow map as grayscale. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: grayscale + mapSize 512 vs 2048 measured. Homework: compare function; bias paragraph. Quiz: who renders the map, bias, ortho why.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Light-depth pass | Plant CSM without a map. |
| 10–30 | Compare + bias | Plant bias 0.1. |
| 30–45 | Grayscale debug | Named extra view. |
| 45–60 | 512 vs 2048 table | Device + resolution; no invented fps. |

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

None this meeting.


## Snippet

```glsl
float shadow = (zLight > mapZ + bias) ? 0.3 : 1.0;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. CSM speech without a single map.
2. bias 0.1.

## If we run long, cut

Cascades. Keep one directional map + named passes.

## If we run short, add

Spot perspective as a name.
