# Lecture 11 — Three.js XR helpers

**Week 11 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** VRButton/ARButton as oracles; students explain session + input  
**Success check:** they can strip a Three.js XR example to a short file they can explain and cite

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: helpers you can read | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
VRButton.createButton(renderer)
examples folder  =  oracle
cite the example URL

XREstimatedLight  +  fallback dir light
hand tracking     name only
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Helpers are not a license to paste 400 lines. Full example dump they cannot explain fails. Citation required. No CDN — local three build.

**Ask:** If I delete VRButton, what must you still know? Wait. Want: requestSession + loop.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VRButton, controllers*.

**Do not:** Full example dump, cannot explain.

### Minutes 10–12 — Frame

**Say:** AR light estimate named; fallback directional. Hands optional extra. Remove unused passes.

**Ask:** What is an oracle in this course?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Button helper. Then the session it hides.

**Board:** createButton. Cite URL.

**Say:** Strip to ~80 lines they can narrate.

**Ask:** Why cite the example?

**They do:** On paper: session, loop, select — three lines the helper wraps.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Strip a Three.js XR example. Plant dump. Plant no citation. Fallback dir light.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** VRButton + one cube they can explain. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: cite URL; remove unused passes. Homework: 80-line explain. Quiz: VRButton, oracle, citation.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | VRButton | Plant CDN. |
| 15–40 | Strip the example | Plant dump. |
| 40–55 | Cite + fallback light | No citation plant. |
| 55–60 | They narrate 80 lines | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. cite the example URL.
2. remove unused passes.

---

## Homework

1. Written: what the helper hid.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
document.body.appendChild(VRButton.createButton(renderer));
```

---

## Extra exercises

See [[XR/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. full example dump, cannot explain.
2. no citation.

## If we run long, cut

Hand tracking impl. Keep button + explain.

## If we run short, add

Remove unused passes.
