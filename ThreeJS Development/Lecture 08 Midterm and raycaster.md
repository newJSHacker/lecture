# Lecture 8 — Midterm and raycaster

**Week 8 of 15** · Three.js Development  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then Raycaster as an oracle — NDC mouse, not a BVH you write  
**Success check:** after the exam they can convert a pointer to NDC, intersectObjects, and say the engine is not the algorithm

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `ThreeJS Development/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: picking is a ray vs bounds the engine owns; y is flipped in NDC`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Scene/camera/renderer and Mesh→draw; matrixWorld as M; Basic vs Standard; lights/shadow flags; dt vs fps; GLTFLoader/traverse; albedo sRGB vs linear data maps.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
pointer NDC: x = (cx/w)*2-1     y = −(cy/h)*2+1
raycaster.setFromCamera(pointer, camera)
hits = raycaster.intersectObjects(pickables, recursive)

oracle  ≠  you implemented a BVH
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then picking. No laptop for the exam. After: Raycaster is an oracle. Computational Geometry owns the algorithm. Demo 07-raycaster.html.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Click to highlight a mesh. Plant forgot minus on y. Plant intersect the whole scene including helpers.

**They do:** Highlight on hit. Layer extra if time.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | NDC mapping | Plant +y. Picks the floor. |
| 15–40 | intersectObjects | Plant recursive false on a Group. |
| 40–60 | They highlight | Circulate. |

---

## Lab

1. layer extra.
2. reflection.

---

## Homework

1. Written: oracle vs algorithm.
2. Code: pick.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[ThreeJS Development/exercises/Week 08]].

## If we run long, cut

Octree. Keep NDC + oracle sentence.

## If we run short, add

layers extra: camera.layers vs raycaster.layers.
