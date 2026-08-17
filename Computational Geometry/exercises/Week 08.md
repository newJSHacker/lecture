# Extra exercises — Week 8 (midterm + DCEL)

Lecture: [[Computational Geometry/Week 08 Midterm and DCEL]]  
Demo: [12-dcel-walk.html](../code/12-dcel-walk.html)

No extra homework for credit. These are recitation / makeup / oral-exam drills.

---

## Midterm drills (no laptop)

Work the lecture’s Q1–Q5 again with **new numbers**:

1. A=(0,0), B=(6,0), C=(2,4), D=(2,−1). `orient(A,B,C)`? Type of AB ∩ CD?
2. Circumcenter of ABC: predicate or construction?
3. Jarvis time, worst-case input.
4. Andrew lower-hull condition; what `<= 0` drops.
5. Parabola reduction in 5 sentences.
6. Three sweep events; why neighbors only; swap at INTER.
7. 15-gon: triangles and diagonals.
8. Define ear. Ray through vertex: what breaks, what is the fix.
9. T-junction: `proper` / `touch` / `overlap` / `none`.
10. Simple + all turns same ⇒ convex. Why the bowtie is the counterexample if you drop simplicity.

## DCEL written

11. Draw one triangle as three half-edges. Label `origin`, `next`, `twin` (twins missing if unbounded).
12. Walk around a face: start at `incidentEdge`, follow `next` until you return.
13. Walk around a vertex: `e = e.twin.next` (or `e.prev.twin`, depending on convention). State yours.
14. Why an array of vertices is not enough once two triangles share an edge.
15. Split an edge at an intersection: which records change?

## Snippet — walk a face

```js
function walkFace(dcel, faceIndex) {
  const start = dcel.half.findIndex((h) => h.face === faceIndex);
  const ids = [];
  let e = start;
  do {
    ids.push(dcel.half[e].origin);
    e = dcel.half[e].next;
  } while (e !== start);
  return ids.map((i) => dcel.verts[i]);
}
```

Build a DCEL from triangles with `CG.trianglesToDCEL` in [kernel.js](../code/kernel.js).
