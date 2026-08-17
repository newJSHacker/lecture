# Lecture 11 — Three.js XR helpers

**Week 11 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** VRButton, controllers  
**Success check:** Wire VRButton/ARButton.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: VRButton, controllers | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
XRButton.createButton(renderer)
Button + scene.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Helpers. The examples folder is an oracle.

**Ask:** Wire VRButton/ARButton? Wait seven seconds. Take two answers.

**Board:** parked strip. Then XRButton.createButton(renderer).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VRButton, controllers*.

**Do not:** Full example dump, cannot explain.

### Minutes 10–12 — Frame

**Say:** Today’s question: VRButton, controllers. Kernel: VRButton, controllers. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: full example dump, cannot explain.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Helpers. The examples folder is an oracle.

**Say:** AR light. XREstimatedLight.

**Say:** Hands. Hand tracking name.

**Ask:** Wire VRButton/ARButton? Wait seven seconds. Take two answers.

**They do:** On paper: cite the example URL.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: A three.js example stripped to 80 lines they can explain.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cite the example URL.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: cite the example URL.; remove unused passes.. Homework: Written: what the helper hid.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: VRButton, controllers | Plant the first common mistake. |
| 10–30 | A three.js example stripped to 80 lines they can explain. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. VRButton (3)
2. estimated light (4)
3. what you deleted (3)


## Snippet

```js
document.body.appendChild(VRButton.createButton(renderer));
```

---

## Extra exercises

See [[XR/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Helpers.** The examples folder is an oracle. Students must still explain session + input.

**2. AR light.** XREstimatedLight. Fallback dir light.

**3. Hands.** Hand tracking name. Optional extra.

---

## Common mistakes

1. full example dump, cannot explain.
2. no citation.

## If we run long, cut

Hands

## If we run short, add

remove unused passes.
