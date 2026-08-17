# Lecture 6 — Anchors and persistence

**Week 6 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** world-locked pose  
**Success check:** Create an anchor at a hit.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: world-locked pose | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
anchor → getPose each frame
Pinned cubes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Anchors. A stable pose in the XR world.

**Ask:** Create an anchor at a hit? Wait seven seconds. Take two answers.

**Board:** parked strip. Then anchor → getPose each frame.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *world-locked pose*.

**Do not:** Cloud anchors as required.

### Minutes 10–12 — Frame

**Say:** Today’s question: world-locked pose. Kernel: world-locked pose. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: cloud anchors as required.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Anchors. A stable pose in the XR world.

**Say:** Persistence. True world maps are platform features.

**Say:** Scale. Meters again.

**Ask:** Create an anchor at a hit? Wait seven seconds. Take two answers.

**They do:** On paper: clear all.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Place two anchored cubes; walk; they stay.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** clear all.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: clear all.; scale 0.2 m object.. Homework: Written: session vs persistent.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: world-locked pose | Plant the first common mistake. |
| 10–30 | Place two anchored cubes; walk; they stay. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. clear all.
2. scale 0.2 m object.

---

## Homework

1. Written: session vs persistent.
2. demo.

---

## Quiz next meeting (they hear this now)

1. anchor (3)
2. getPose (3)
3. honesty (4)


## Snippet

```js
const anchor = await frame.createAnchor(pose, space);
```

---

## Extra exercises

See [[XR/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Anchors.** A stable pose in the XR world. Device and UA dependent.

**2. Persistence.** True world maps are platform features. Student honesty: 'this session' vs 'forever'.

**3. Scale.** Meters again. A 10 m cube is a bug.

---

## Common mistakes

1. cloud anchors as required.
2. unanchored floating UI.

## If we run long, cut

Scale

## If we run short, add

scale 0.2 m object.
