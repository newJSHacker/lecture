# Lecture 2 — Object3D and transforms

**Week 2 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** position rotation scale  
**Success check:** position/quaternion/scale.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: position rotation scale | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
matrixWorld
Tree.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Graph. CG I scene graph with nicer API.

**Ask:** position/quaternion/scale? Wait seven seconds. Take two answers.

**Board:** parked strip. Then matrixWorld.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *position rotation scale*.

**Do not:** Scale -1 'to flip' without winding talk.

### Minutes 10–12 — Frame

**Say:** Today’s question: position rotation scale. Kernel: position rotation scale. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: scale -1 'to flip' without winding talk.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graph. CG I scene graph with nicer API.

**Say:** Euler. order property.

**Say:** Demo. hierarchy demo if present.

**Ask:** position/quaternion/scale? Wait seven seconds. Take two answers.

**They do:** On paper: axesHelper.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Parent a cube to another; spin parent.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** axesHelper.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: axesHelper.; lookAt extra.. Homework: Written: matrixWorld is M.; Code: parent.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: position rotation scale | Plant the first common mistake. |
| 10–30 | Parent a cube to another; spin parent. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. axesHelper.
2. lookAt extra.

---

## Homework

1. Written: matrixWorld is M.
2. Code: parent.

---

## Quiz next meeting (they hear this now)

1. position units (3)
2. matrixWorld (4)
3. euler order (3)


## Snippet

```js
parent.add(child);
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Graph.** CG I scene graph with nicer API.

**2. Euler.** order property. Gimbal from math course.

**3. Demo.** hierarchy demo if present.

---

## Common mistakes

1. scale -1 'to flip' without winding talk.

## If we run long, cut

Demo

## If we run short, add

lookAt extra.
