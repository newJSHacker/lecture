# Lecture 4 — Locomotion

**Week 4 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** teleport vs smooth  
**Success check:** Teleport to a nav mesh or plane.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: teleport vs smooth | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
arc teleport; vignette optional
Arc + fade.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Comfort. Vection makes people sick.

**Ask:** Teleport to a nav mesh or plane? Wait seven seconds. Take two answers.

**Board:** parked strip. Then arc teleport; vignette optional.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *teleport vs smooth*.

**Do not:** Smooth locomotion only, no option.

### Minutes 10–12 — Frame

**Say:** Today’s question: teleport vs smooth. Kernel: teleport vs smooth. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: smooth locomotion only, no option.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Comfort. Vection makes people sick.

**Say:** Nav. A plane is enough.

**Say:** Blink. Fade on teleport extra.

**Ask:** Teleport to a nav mesh or plane? Wait seven seconds. Take two answers.

**They do:** On paper: disable smooth or hide behind a setting.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Teleport on select-hit a floor; snap turn 30°.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** disable smooth or hide behind a setting.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: disable smooth or hide behind a setting.; vignette extra.. Homework: Written: why teleport default.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: teleport vs smooth | Plant the first common mistake. |
| 10–30 | Teleport on select-hit a floor; snap turn 30°. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. disable smooth or hide behind a setting.
2. vignette extra.

---

## Homework

1. Written: why teleport default.
2. demo.

---

## Quiz next meeting (they hear this now)

1. vection (4)
2. snap turn (3)
3. navmesh (3)


## Snippet

```js
// raycast floor → on select, camera-parent to hit point
```

---

## Extra exercises

See [[XR/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Comfort.** Vection makes people sick. Teleport + snap turn is the default student policy unless they document otherwise.

**2. Nav.** A plane is enough. Navmesh name.

**3. Blink.** Fade on teleport extra.

---

## Common mistakes

1. smooth locomotion only, no option.
2. flying by default.

## If we run long, cut

Blink

## If we run short, add

vignette extra.
