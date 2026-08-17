# Lecture 7 — Physics name

**Week 7 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rapier / cannon-es  
**Success check:** A physics engine is an **oracle** for collision, like Raycaster.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: rapier / cannon-es | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
collider ≠ mesh
Collider vs render.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Honesty. [[04 Computational Geometry]] is the algorithms course.

**Ask:** A physics engine is an **oracle** for collision, like Raycaster? Wait seven seconds. Take two answers.

**Board:** parked strip. Then collider ≠ mesh.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rapier / cannon-es*.

**Do not:** Claiming they implemented physics.

### Minutes 10–12 — Frame

**Say:** Today’s question: rapier / cannon-es. Kernel: rapier / cannon-es. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: claiming they implemented physics.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Honesty. [[04 Computational Geometry]] is the algorithms course.

**Say:** @react-three/rapier. Optional.

**Say:** Networking. Skip.

**Ask:** A physics engine is an **oracle** for collision, like Raycaster? Wait seven seconds. Take two answers.

**They do:** On paper: collider wireframe extra.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: A floor + dropping cubes; reset.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** collider wireframe extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: collider wireframe extra.; one sentence oracle vs kernel.. Homework: Written: collider vs mesh.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: rapier / cannon-es | Plant the first common mistake. |
| 10–30 | A floor + dropping cubes; reset. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. oracle (4)
2. fixed dt (3)
3. convex hull name (3)


## Snippet

```jsx
<RigidBody><mesh><boxGeometry/></mesh></RigidBody>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Honesty.** [[04 Computational Geometry]] is the algorithms course. Here students **use** a engine and must say so.

**2. @react-three/rapier.** Optional. A falling box is enough.

**3. Networking.** Skip. Single player.

---

## Common mistakes

1. claiming they implemented physics.
2. 1000 convex hulls.

## If we run long, cut

Networking

## If we run short, add

one sentence oracle vs kernel.
