# Lecture 7 — Physics name

**Week 7 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rapier/cannon-es is an oracle for collision, like Raycaster  
**Success check:** they can drop a cube on a floor, reset, and write one sentence: we did not implement contact

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: use physics; do not claim the algorithm | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
oracle     rapier / cannon-es / Raycaster
kernel     our scene, HUD, reset, labels

<RigidBody>  falling box
reset →  origin

single player     no netcode
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Computational Geometry owns predicates. Today we use an engine and we say so. Claiming you implemented physics because a cube fell is an integrity fail.

**Ask:** Is a falling box a physics paper? Wait. Want: no — it is an oracle.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rapier / cannon-es*.

**Do not:** Claiming they implemented physics.

### Minutes 10–12 — Frame

**Say:** Floor + dropping cubes + reset. Collider wireframe extra. Skip networking. 1000 convex hulls is not the lab.

**Ask:** What must the README say about rapier?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Oracle vs kernel. Write both words.

**Board:** RigidBody box; reset arrow.

**Say:** Same honesty as Raycaster: we call it, we do not derive GJK.

**Ask:** Why is 1000 hulls a cut?

**They do:** One sentence: oracle vs kernel for this lab.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Floor + drop + reset. Plant 'we implemented physics' in a comment. Cross it out. Wireframe extra.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One falling box and a reset button. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: wireframe extra; oracle sentence. Homework: that sentence in README. Quiz: oracle, reset, no netcode. Next: midterm then Suspense.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Floor + gravity | Plant algorithm claim. |
| 15–40 | Drop cubes + reset | Plant 1000 hulls. |
| 40–55 | Oracle sentence on board | They copy. |
| 55–60 | They add reset | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. collider wireframe extra.
2. one sentence oracle vs kernel.

---

## Homework

1. Written: collider vs mesh.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```jsx
<RigidBody><mesh><boxGeometry/></mesh></RigidBody>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. claiming they implemented physics.
2. 1000 convex hulls.

## If we run long, cut

Networking. Keep floor + honesty.

## If we run short, add

Collider wireframe.
