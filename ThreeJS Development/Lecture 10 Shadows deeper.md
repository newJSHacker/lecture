# Lecture 10 — Shadows deeper

**Week 10 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** shadow types named (PCF); bias / normalBias; CameraHelper on shadow.camera  
**Success check:** they tune bias on a character-scale cube and can name PCF without claiming a fps win

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: acne you can fix | Invariant: bias too large deletes shadows; one directional should not cover the earth`

## Board at the end (they photograph this)

```
PCF / PCFSoft   (names)
light.shadow.bias = −0.0001
light.shadow.normalBias   (named)

CameraHelper(light.shadow.camera)
frustum too big → acne + peter-panning

CSM   (name only)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Week 4 enabled shadows. Today knobs. Demo 03-lights-shadows.html and 20-shadow-contact.html knobs. Full maps in RTR. Do not set bias 0.1.

**Ask:** If the shadow pulls away from the feet, is that acne or peter-panning? Wait. Want: panning — bias too negative / frustum.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *types, bias*.

**Do not:** Bias 0.1 destroying shadows.

### Minutes 10–12 — Frame

**Say:** Helpers on the shadow camera. mapSize experiment measured. CSM name, skip implementation.

**Ask:** What is PCF in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Acne vs panning on the board.

**Board:** bias line + helper.

**Say:** One directional, tight frustum.

**Ask:** Why not bias = 0.1?

**They do:** On paper: two symptoms and which knob.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Tune bias on a character-scale cube. Plant bias 0.1. Plant one huge directional covering the earth.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** CameraHelper on shadow.camera. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: helper on; mapSize experiment measured. Homework: acne vs panning; bias. Quiz: bias, PCF, helper.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Acne plant | bias 0. |
| 10–30 | tune −0.0001 | Plant 0.1. |
| 30–45 | helper frustum | Too big. |
| 45–60 | They measure mapSize | No invented fps. |

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

None this meeting.


## Snippet

```js
light.shadow.bias = -0.0001;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. bias 0.1 destroying shadows.
2. one huge directional covering the earth.

## If we run long, cut

CSM implementation. Keep bias + helper.

## If we run short, add

mapSize experiment measured.
