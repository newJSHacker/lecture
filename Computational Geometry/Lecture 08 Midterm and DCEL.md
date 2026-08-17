# Lecture 8 — Midterm and DCEL

**Week 8 of 15** · Computational Geometry  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** DCEL: half-edge origin/twin/next/face; walkFace = next loop; walkVertex = twin.next; face on the left  
**Success check:** after the exam they walk two bounded faces of a pentagon-with-diagonal and twin.twin==e

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Computational Geometry/code/08-andrew.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: predicates before constructions; degeneracy is the course`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** orient and degeneracy; proper/touch/overlap/none; PIP vertex-hit; convex vs simple vs bowtie; same-turn ⇔ convex for simple (short proof); Jarvis Θ(nh); Andrew sort+≤0+O(n log n); parabola lower bound; sweep events and neighbors; ear + n−2; one degeneracy. No Voronoi, kd-tree, or DCEL on the paper.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
Vertex: x,y, incidentEdge
Half: origin, twin, next, face (left, CCW outer)
Face: outer, inners

e.twin.origin == e.next.origin
e.twin.twin == e

walkFace: e = e.next
walkVertex: e = e.twin.next

two triangles share an edge:
  4 verts, 10 half-edges, 3 faces (2 bounded + unbounded)

Three.js BufferGeometry is triangle soup, not a DCEL
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then DCEL. No laptop. After: half-edges are how you walk a face and split an edge after Week 6 intersections. Grading: a correct picture with a wrong name gets partial; O(n log n) on Jarvis without h gets zero.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Hardcoded DCEL for two triangles. Log walkFace and walkVertex on the shared verts. Demo 12-dcel-walk.html. Plant storing one directed edge per segment. Plant forgetting the unbounded face.

**They do:** walkFace(edgeId) → vertex ids. Every twin.twin is itself.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Count a triangle DCEL with the class | 3+3 halves, 2 faces. |
| 15–40 | Two triangles, label every half | Counts mismatch ⇒ the DCEL is wrong. |
| 40–60 | walkFace / walkVertex | They type the loops. |

---

## Lab

1. one triangle
2. two triangles sharing an edge
3. a convex pentagon with one diagonal (three faces)
4. `walkFace(edgeId) -> [vertexIds]`
5. `walkVertex(edgeId) -> [neighborVertexIds]`
6. A check: every half-edge’s twin’s twin is itself; every face walk returns to start.

---

## Homework

_(none this meeting)_

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Computational Geometry/exercises/Week 08]].

## If we run long, cut

Edge-split coding. Keep records + two walks.

## If we run short, add

Euler check: include the unbounded face.
