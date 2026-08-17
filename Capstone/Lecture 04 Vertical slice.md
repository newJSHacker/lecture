# Lecture 4 — Vertical slice

**Week 4 of 15** · Capstone Project  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one path that works  
**Success check:** One happy path on the target device.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Capstone/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: one path that works | Invariant: the problem is users, not a tech list`

## Board at the end (they photograph this)

```
load → see → interact → reset
Path arrows.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Slice. If the slice is not there, the project is a wish.

**Ask:** One happy path on the target device? Wait seven seconds. Take two answers.

**Board:** parked strip. Then load → see → interact → reset.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one path that works*.

**Do not:** Slideware instead of a path.

### Minutes 10–12 — Frame

**Say:** Today’s question: one path that works. Kernel: one path that works. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: slideware instead of a path.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Slice. If the slice is not there, the project is a wish.

**Say:** Placeholders. Boxes with labels beat waiting for Blender.

**Say:** Demo. A TA can complete the path without the team in the room.

**Ask:** One happy path on the target device? Wait seven seconds. Take two answers.

**They do:** On paper: bug list.

**Do not:** start in an engine before the problem statement.

### Minutes 35–50 — Show

**Say:** Live demo: Happy path demo to the class (5 min) or TA.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** bug list.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: bug list.; 30s recording.. Homework: Slice tagged in git.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: one path that works | Plant the first common mistake. |
| 10–30 | Happy path demo to the class (5 min) or TA. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Capstone/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. bug list.
2. 30s recording.

---

## Homework

1. Slice tagged in git.

---

## Quiz next meeting (they hear this now)

1. happy path (4)
2. placeholder OK? (3)
3. TA alone (3)


## Extra exercises

See [[Capstone/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Slice.** If the slice is not there, the project is a wish. Graphics capstones die on loaders and cameras.

**2. Placeholders.** Boxes with labels beat waiting for Blender.

**3. Demo.** A TA can complete the path without the team in the room.

---

## Common mistakes

1. slideware instead of a path.
2. uncommitted assets.

## If we run long, cut

Demo

## If we run short, add

30s recording.
