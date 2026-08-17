# Lecture 2 — VR session and loop

**Week 2 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** reference space  
**Success check:** requestSession immersive-vr.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: reference space | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
local-floor vs viewer
Floor origin.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Spaces. viewer, local, local-floor, bounded-floor, unbounded.

**Ask:** requestSession immersive-vr? Wait seven seconds. Take two answers.

**Board:** parked strip. Then local-floor vs viewer.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *reference space*.

**Do not:** Never testing exit.

### Minutes 10–12 — Frame

**Say:** Today’s question: reference space. Kernel: reference space. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: never testing exit.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Spaces. viewer, local, local-floor, bounded-floor, unbounded.

**Say:** Loop. Three.js handles `setAnimationLoop` with XR.

**Say:** Comfort. Week 9.

**Ask:** requestSession immersive-vr? Wait seven seconds. Take two answers.

**They do:** On paper: end session button.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Enter VR on a headset **or** record a TA doing it; student still writes the session code.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** end session button.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: end session button.; floor plane.. Homework: Written: reference space.; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: reference space | Plant the first common mistake. |
| 10–30 | Enter VR on a headset **or** record a TA doing it; student still writes the session code. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. end session button.
2. floor plane.

---

## Homework

1. Written: reference space.
2. code.

---

## Quiz next meeting (they hear this now)

1. local-floor (4)
2. who owns rAF (3)
3. cleanup (3)


## Snippet

```js
renderer.xr.enabled = true;
```

---

## Extra exercises

See [[XR/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Spaces.** viewer, local, local-floor, bounded-floor, unbounded. Teaching: local-floor for room-scale-ish.

**2. Loop.** Three.js handles `setAnimationLoop` with XR. Students should still know the pose comes from the frame.

**3. Comfort.** Week 9. This week: standing origin.

---

## Common mistakes

1. never testing exit.
2. unbounded tracking as week 2 required.

## If we run long, cut

Comfort

## If we run short, add

floor plane.
