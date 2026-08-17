# Lecture 3 — Controllers and input

**Week 3 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** select, squeeze, rays  
**Success check:** XRInputSource.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: select, squeeze, rays | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
target ray + squeeze
Controller + ray.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Input. Hands, controllers, gaze (last resort).

**Ask:** XRInputSource? Wait seven seconds. Take two answers.

**Board:** parked strip. Then target ray + squeeze.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *select, squeeze, rays*.

**Do not:** Mouse-only and calling it VR.

### Minutes 10–12 — Frame

**Say:** Today’s question: select, squeeze, rays. Kernel: select, squeeze, rays. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: mouse-only and calling it VR.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Input. Hands, controllers, gaze (last resort).

**Say:** Three.js. XRControllerModelFactory / Raycaster from controller.

**Say:** Haptics. pulse name.

**Ask:** XRInputSource? Wait seven seconds. Take two answers.

**They do:** On paper: show ray.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Point and `select` to change a cube color.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** show ray.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: show ray.; squeeze extra.. Homework: Written: input source fields.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: select, squeeze, rays | Plant the first common mistake. |
| 10–30 | Point and `select` to change a cube color. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. show ray.
2. squeeze extra.

---

## Homework

1. Written: input source fields.
2. demo.

---

## Quiz next meeting (they hear this now)

1. select (3)
2. target ray (4)
3. one controller (3)


## Snippet

```js
controller.addEventListener('select', onSelect);
```

---

## Extra exercises

See [[XR/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Input.** Hands, controllers, gaze (last resort). `select` is the click.

**2. Three.js.** XRControllerModelFactory / Raycaster from controller.

**3. Haptics.** pulse name. Optional.

---

## Common mistakes

1. mouse-only and calling it VR.
2. no ray debug.

## If we run long, cut

Haptics

## If we run short, add

squeeze extra.
