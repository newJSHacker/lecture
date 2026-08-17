# Lecture 2 — VR session and loop

**Week 2 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** requestSession; local-floor; Three.js setAnimationLoop with XR  
**Success check:** they can enable renderer.xr, request a session from a gesture, and end the session

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a session that starts and ends | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
viewer · local · local-floor · bounded-floor · unbounded

teaching: local-floor
renderer.xr.enabled = true
setAnimationLoop     pose from XRFrame

End session     (test exit)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Spaces are not decoration. Unbounded as a week-2 requirement is a lottery. Standing origin this week; comfort is week 8 leftover + week 9.

**Ask:** Where is the floor — viewer space or local-floor? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *reference space*.

**Do not:** Never testing exit.

### Minutes 10–12 — Frame

**Say:** Three.js owns the XR loop; students still say the pose comes from the frame. Never testing exit is a plant. Inline still required.

**Ask:** What happens if we never call end?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Names of spaces. Freeze local-floor.

**Board:** enabled = true. Gesture → session. End button.

**Say:** Headset or TA recording; students still write the code. Fallback: inline floor plane.

**Ask:** Why not unbounded this week?

**They do:** On paper: start/end arrows + local-floor origin.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Enter VR if hardware; else TA video + student code. Plant missing end. Floor plane in inline.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** xr.enabled + end-session button (inline stub OK). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: end button; floor plane. Homework: space names. Quiz: local-floor, loop, why end.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Spaces on board | Plant unbounded required. |
| 15–40 | requestSession + loop | Plant no gesture. |
| 40–55 | End session | Never-exit plant. |
| 55–60 | They add a floor plane | Circulate. |

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

None this meeting.


## Snippet

```js
renderer.xr.enabled = true;
```

---

## Extra exercises

See [[XR/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. never testing exit.
2. unbounded tracking as week 2 required.

## If we run long, cut

Comfort vignette. Keep session + local-floor.

## If we run short, add

Floor plane in inline.
