# Lecture 9 — Rotations in 2D/3D

**Week 9 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** R2(θ) frozen on the board; Ry(90)*(1,0,0) test; same Ry as CG I  
**Success check:** they write one 2D rotation matrix and they do not put degrees in it

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/07-rotate.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: turn an angle into a matrix | Invariant: write one R and freeze; order of 3D Euler angles matters; quaternions named not required`

## Board at the end (they photograph this)

```
R2(θ) = [[c, -s], [s, c]]     // FREEZE THIS (or the documented variant — one only)

thumb on axis, fingers rotation sense

Euler: order matters; gimbal lock named
quaternions: name only
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: gimbal lock photo or a small animation | do not derive quaternion slerp |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Same Ry as [[Computer Graphics/Lecture 05 Homogeneous Transforms]]. Mixing conventions is the bug.

**Ask:** R(90°) of (1,0) with **our** matrix? Compute on the board.

**Board:** parked strip. Then right-hand thumb on axis.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Ry, composition*.

**Do not:** Mixing conventions.

### Minutes 10–12 — Frame

**Say:** Rx, Ry, Rz. Euler gimbal lock: name and a picture. Quaternions named, not required.

**Ask:** Why does order of Rx Ry Rz matter?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** 2D first. Cos/sin in **radians**.

**Board:** thumb. Euler vs one matrix.

**Say:** Compose two rotations. Degrees in matrices — do not.

**Ask:** Gimbal lock in one sentence.

**They do:** Rotate (1,0) by 90° with the frozen matrix.

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Rotate a square; or cube wireframe with Ry. Demo `07-rotate.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Ry(90)*(1,0,0) test; two Euler orders compared.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: gimbal lock in 6 sentences; rotateZ. Quiz: R(90) of (1,0), order, gimbal name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Freeze R2 | The other convention as a plant. |
| 15–40 | Compose 2D | Degrees plant. |
| 40–55 | Euler warning | Picture. |
| 55–60 | They test Ry 90 | Circulate. |

Point them at `Mathematics for Computer Graphics/code/07-rotate.html` as the after-class check, not as the lecture.

---

## Lab

1. Ry(90)*(1,0,0) test.
2. Two Euler orders compared.

---

## Homework

1. Written: gimbal lock in 6 sentences.
2. Code: rotateZ.

---

## Quiz next meeting (they hear this now)

1. R(90) of (1,0) (3)
2. why order matters (4)
3. gimbal lock name (3)


## Snippet

```js
// use the same Ry as Computer Graphics/code/kernel.js
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. 2D.** [[c,-s],[s,c]] or the course's documented variant — **write one and freeze**.

**2. 3D.** Rx, Ry, Rz. Order matters. Euler gimbal lock: name and a picture; quaternions named, not required.

**3. Convention.** Same Ry as [[Computer Graphics/Lecture 05 Homogeneous Transforms]].

---

## Common mistakes

1. Mixing conventions.
2. Degrees in matrices.

## If we run long, cut

Quaternion code. Keep R2 + freeze.

## If we run short, add

Axis-angle name.
