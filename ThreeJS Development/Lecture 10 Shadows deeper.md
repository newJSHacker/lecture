# Lecture 10 — Shadows deeper

**Week 10 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** types, bias  
**Success check:** PCF name.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: types, bias | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
bias / normalBias
Acne.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** RTR later. Full shadow maps.

**Ask:** PCF name? Wait seven seconds. Take two answers.

**Board:** parked strip. Then bias / normalBias.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *types, bias*.

**Do not:** Bias 0.1 destroying shadows.

### Minutes 10–12 — Frame

**Say:** Today’s question: types, bias. Kernel: types, bias. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: bias 0.1 destroying shadows.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** RTR later. Full shadow maps.

**Say:** Helpers. CameraHelper on shadow.camera.

**Say:** CSM name. Skip implementation.

**Ask:** PCF name? Wait seven seconds. Take two answers.

**They do:** On paper: helper on.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Tune bias on a character-scale cube.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** helper on.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: helper on.; mapSize experiment measured.. Homework: Written: acne vs panning.; Code: bias.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: types, bias | Plant the first common mistake. |
| 10–30 | Tune bias on a character-scale cube. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. helper on.
2. mapSize experiment measured.

---

## Homework

1. Written: acne vs panning.
2. Code: bias.

---

## Quiz next meeting (they hear this now)

1. bias (4)
2. PCF (3)
3. helper (3)


## Snippet

```js
light.shadow.bias = -0.0001;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. RTR later.** Full shadow maps. Here: practical knobs.

**2. Helpers.** CameraHelper on shadow.camera.

**3. CSM name.** Skip implementation.

---

## Common mistakes

1. bias 0.1 destroying shadows.
2. one huge directional covering the earth.

## If we run long, cut

CSM name

## If we run short, add

mapSize experiment measured.
