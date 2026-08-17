# Lecture 8 — Midterm and DCEL

**Time:** 60–75 min midterm, then 30–45 min lecture  
**New structure:** doubly-connected edge list  
**Lab:** walk a face

No homework this week except keeping midterm notes.

---

## Midterm (60–75 min)

Written. No laptop. 100 points. Topic list was issued in Week 7.

### Suggested paper (edit names/numbers as you like)

**Q1. Predicates (16 pts)**  
A=(0,0), B=(4,1), C=(2,3), D=(2,0).

1. Sign of `orient(A,B,C)`? (4)
2. Type of intersection of AB and CD? (4)
3. Is “circumcenter of ABC” a predicate or a construction? (4)
4. Give one reason not to use `atan2` for left-of-line. (4)

**Q2. Polygons (16 pts)**  
1. Define convex set. (4)
2. Classify: convex hexagon, C-shape, bowtie. (6)
3. Short proof: simple + all turns the same sign ⇒ locally convex, and why the bowtie shows simplicity is required. (6)

**Q3. Hulls (24 pts)**  
1. Jarvis time in n, h. Worst-case input. (6)
2. Andrew: write the lower-hull while-condition and say what `<= 0` does. (8)
3. Parabola reduction in 4–6 sentences. (10)

**Q4. Sweep (20 pts)**  
1. Three event types. (6)
2. Why test only status neighbors? (8)
3. After INTER, what happens to the two segments in T? (6)

**Q5. Triangulation and degeneracy (24 pts)**  
1. Number of triangles and diagonals in a simple 12-gon. (6)
2. Define an ear. (6)
3. Ray from q hits a polygon vertex. What goes wrong, and what is the half-open fix? (6)
4. T-junction: `proper`, `touch`, `overlap`, or `none`? (6)

### Grading note

Award partial credit for a correct picture with a wrong name. Do not award credit for “O(n log n)” on Jarvis without h.

---

## Lecture — DCEL (30–45 min)

### Why a new data structure

Arrays of vertices are enough for a single polygon. They fail as soon as we have:

- many faces (a triangulation, a map, a mesh)
- the need to walk around a face
- the need to walk around a vertex
- the need to split an edge at an intersection

A **doubly-connected edge list** stores a planar subdivision.

Graphics people already know this as a **half-edge mesh**.

---

### Records

**Vertex**

- `x, y`
- `incidentEdge` — one outgoing half-edge

**Half-edge**

- `origin` — vertex
- `twin` — the opposite half-edge
- `next` — next half-edge around the face
- `prev` — previous around the face (optional if you always have `next` and `twin`)
- `face` — the face on the left (for CCW faces)

**Face**

- `outer` — one half-edge on the outer boundary, or null if unbounded
- `inners` — half-edges on hole cycles, if any

Convention for this course: **walk `next` so the face is on the left** (CCW outer boundary, CW holes).

```
e.twin.origin == e.next.origin
e.twin.twin == e
e.next.prev == e
```

---

### Pictures (draw both)

1. One triangle: 3 vertices, 3 interior half-edges, 3 outer (unbounded-face) half-edges, 2 faces.
2. Two triangles sharing an edge: 4 vertices, 10 half-edges (5 edges × 2), 3 faces (two bounded + unbounded).

Count with the students. If the counts mismatch, the DCEL is wrong.

---

### Operations we need

```
walkFace(e):
    start = e
    do:
        visit e
        e = e.next
    while e != start

walkVertex(e):          // outgoing edges around origin
    start = e
    do:
        visit e
        e = e.twin.next
    while e != start
```

Splitting an edge at a point p (needed after Week 6 intersections, map overlay, mesh repair):

1. Insert vertex p.
2. Replace one edge by two.
3. Update `next` / `twin` on both faces.

Do this as a diagram. Coding the split is optional extra, not the lab.

---

### Graphics connection

| DCEL idea | Engine name |
| --- | --- |
| half-edge | half-edge / winged-edge |
| `next` around face | face loop |
| `twin.next` around vertex | vertex ring |
| faces | mesh faces / materials |
| split edge | edge split, subdivision |

Three.js `BufferGeometry` is **not** a DCEL. It is a triangle soup (or indexed soup). That is why adjacency queries are painful and why mesh-repair tools rebuild a half-edge structure first.

---

## Live coding (if any time remains)

Draw a hardcoded DCEL for two triangles. Log `walkFace` for each bounded face and `walkVertex` for the shared vertices.

Otherwise do this as the first 20 minutes of lab.

---

## Lab

Give students a JSON DCEL for:

- one triangle
- two triangles sharing an edge
- a convex pentagon with one diagonal (three faces)

They write:

1. `walkFace(edgeId) -> [vertexIds]`
2. `walkVertex(edgeId) -> [neighborVertexIds]`
3. A check: every half-edge’s twin’s twin is itself; every face walk returns to start.

Done when the pentagon-with-diagonal reports two bounded faces with the correct vertex cycles.

---

## Homework

None. Optional: read de Berg, chapter on DCEL (short).

---

## Quiz

None this week.

---

## Common mistakes

- Storing only one directed edge per segment, then being unable to walk both faces.
- Mixing CW and CCW in the same file.
- Forgetting the unbounded face. Euler numbers will not add up.
- Treating Three.js triangle indices as a DCEL in the lab report.

---

## Board drawings

1. Half-edge with arrows: `origin`, `twin`, `next`, `face`.
2. Two triangles, every half-edge labeled.
3. `walkVertex` = `twin.next` loop.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 08]] · Demo: [12-dcel-walk.html](code/12-dcel-walk.html)

Makeup drills (new numbers): A=(0,0), B=(6,0), C=(2,4), D=(2,−1).

1. `orient(A,B,C)` and type of AB ∩ CD.
2. 15-gon: triangles and diagonals.
3. Walk face 0 in the demo after ear-clip. Write the vertex cycle.
4. Split-edge thought experiment: which DCEL fields change?

```js
function walkFace(dcel, faceIndex) {
  const start = dcel.half.findIndex((h) => h.face === faceIndex);
  let e = start, ids = [];
  do { ids.push(dcel.half[e].origin); e = dcel.half[e].next; }
  while (e !== start);
  return ids;
}
```
