# Week 7 — Polygon triangulation

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** ear clipping  
**Board first:** a concave polygon, one ear shaded, then the remaining polygon

Also today: hand out the **midterm topic list** (end of this note).

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 6 |
| 10–25 | Why triangulate; n − 2 triangles |
| 25–50 | Ears and ear clipping |
| 50–65 | Monotone polygons (idea) |
| 65–75 | Constrained vs mesh triangulation; midterm list |

---

## Learning goals

1. Prove a simple polygon with n vertices has n − 2 triangles and n − 3 diagonals.
2. Define an ear and Meisters’ theorem (teaching statement).
3. Implement ear clipping and know it is O(n²).
4. Explain why a y-monotone polygon is easier (O(n) after sort).
5. Distinguish polygon triangulation from Delaunay (Week 11).

---

## 1. Why triangulate (15 min)

GPUs draw triangles. A filled polygon in a canvas, a font outline, a UI blob, a roof footprint — all become triangles.

**Theorem.** Every simple polygon with n ≥ 3 vertices has a triangulation: n − 2 triangles, n − 3 diagonals, using only existing vertices.

**Proof sketch (induction).**

n = 3: already a triangle.

n > 3: a simple polygon has a diagonal (exists; we will get one from an ear). A diagonal splits P into P1, P2 with n1 + n2 = n + 2 vertices (the two endpoints are shared). By induction, triangles = (n1 − 2) + (n2 − 2) = n − 2.

**Existence of a diagonal.** Every simple n > 3 polygon has at least three convex vertices. At least one of those is an **ear**: the diagonal between its neighbors lies inside P. Clipping that ear is a diagonal.

Do not spend the whole lecture on the existence proof. Draw it. Assign the write-up as homework.

---

## 2. Ears (25 min)

Vertex vi is an **ear tip** if:

1. vi is convex (not reflex, not a skip of a flat-only policy),
2. the diagonal `v_{i-1} v_{i+1}` lies **inside** P,
3. equivalently: triangle `v_{i-1} v_i v_{i+1}` contains **no other vertex** of P.

Condition 3 is what we implement. Because P is simple, “no vertex inside the ear triangle” plus “vi convex” implies the diagonal is inside.

### Meisters’ theorem (state)

Every simple polygon with n ≥ 4 has at least two ears.

### Ear clipping

```
earClip(P):
    if not simple: fail
    V = cyclic list of vertices
    T = []
    while |V| > 3:
        found = false
        for each vi in V:
            if isEar(vi, V):
                T.append(triangle(v_{i-1}, vi, v_{i+1}))
                remove vi from V
                found = true
                break
        if not found: fail   // not simple, or numeric garbage
    T.append(remaining triangle)
    return T

isEar(vi, V):
    if orient(v_{i-1}, vi, v_{i+1}) is not a convex turn: return false
    for each vertex q in V except the three:
        if q is inside triangle(v_{i-1}, vi, v_{i+1})
           or on its boundary (except the three vertices):
            return false
    return true
```

Use Week 2 point-in-triangle: three orientation tests of the same sign (plus boundary policy).

### Complexity

Each of n − 3 clips may scan O(n) vertices to test ears.  
**O(n²).** Fine for n up to a few thousand (UI shapes, font glyphs). Not fine for a 200k-vertex GIS lake.

Faster: O(n log n) via monotone subdivision (below). O(n) exists (Chazelle) — mention, do not teach.

### Degeneracy

- Holes: ear clipping as written does **not** handle holes. Either ban holes or cut a channel to the outer boundary first.
- Flat vertices: treat as not ears; they can be skipped or removed in a preprocess.
- Almost-collinear “no vertex inside” with a vertex sitting on the diagonal: reject as ear (boundary case).

---

## 3. Monotone polygons (15 min)

A polygon is **y-monotone** if its boundary splits into two chains from the top vertex to the bottom vertex, and each chain is never-upward (or never-downward).

A y-monotone polygon can be triangulated in **O(n)** with a stack, similar in spirit to Andrew’s hull scan.

**Full O(n log n) pipeline:**

1. Add diagonals to split a simple polygon into y-monotone pieces (sweep, O(n log n)).
2. Triangulate each piece in linear time.

Teach step 1 as a picture: merge/split/start/end/regular vertices. Do **not** require the sweep implementation. Students should be able to **label** a vertex as split vs merge on a drawing.

| Vertex type | Local picture | Action (idea) |
| --- | --- | --- |
| Start | both neighbors below, interior below | new helper |
| End | both neighbors above, interior above | close a piece |
| Split | both neighbors below, interior above | add diagonal to helper |
| Merge | both neighbors above, interior below | add diagonal later |
| Regular | one neighbor up, one down | update helper |

This table is enough for the midterm at the level “what is a split vertex?”

---

## 4. Two different triangulations (10 min)

| | Polygon triangulation | Delaunay (Week 11) |
| --- | --- | --- |
| Input | a simple polygon (edges are constraints) | a point set |
| Edges | all boundary edges must appear | no boundary unless we add a hull |
| Quality | any triangulation is allowed | empty circumcircle |
| Use | fill a shape | well-shaped mesh, terrain |

**Constrained Delaunay** sits between them: respect given edges, maximize the Delaunay property elsewhere. Name it. Project option.

---

## Live coding (60 min)

Ear clipping in step mode.

- Current candidate vertex highlighted
- Ear triangle filled green if legal, red if a point is inside
- Clipped ears stay as faint triangles
- Remaining polygon outlined

Clip a C-shaped polygon. Students should see a reflex vertex refused, then accepted after its neighbor is removed.

Fail on a bowtie with a clear error, not an infinite loop.

---

## Lab

1. Implement `earClip`.
2. Draw diagonals and number triangles in clip order.
3. Inputs: convex, C-shape, a 12-vertex simple room.
4. Bowtie must throw.

Done when the C-shape produces n − 2 triangles and the union visually fills the polygon.

---

## Homework

1. Implement ear clipping.
2. Written: induction that a simple n-gon has n − 2 triangles.
3. Written: define an ear. Give a polygon with exactly two ears (a convex quadrilateral is too easy; use a convex n-gon — it has n ears — so instead use a concave quad, which has two).
4. **Study** the midterm list below.

---

## Quiz (10 min)

1. How many triangles in a simple 10-gon? How many diagonals? (2 pts)
2. Define ear tip. (3 pts)
3. Ear clipping time? (2 pts)
4. Does ear clipping as taught handle holes? (1 pt)
5. Name one difference vs Delaunay. (2 pts)

---

## Midterm topic list (print / post today)

Week 8, written, 60–75 minutes, no laptop.

1. `orient`, signed area, predicates vs constructions
2. Segment intersection types: proper / touch / overlap / none
3. Point in polygon: even–odd and the vertex-hit rule
4. Convex set; convex vs simple vs self-intersecting
5. Same-turn ⇔ convex for **simple** polygons (short proof)
6. Jarvis: idea, Θ(n h), when it is slow
7. Andrew: sort key, stack, O(n log n), collinear policy
8. Hull lower bound via the parabola (idea)
9. Sweep: events, status, why neighbors only
10. Ear: definition, n − 2 triangles, O(n²)
11. One degeneracy question (collinear / T-junction / ray through vertex)

No Voronoi, no kd-tree, no DCEL on the midterm.

---

## Common mistakes

- Testing `isEar` without the convex-turn test (a reflex “ear” diagonal is outside).
- Forgetting the polygon is cyclic.
- Using point-in-polygon on the whole P instead of point-in-triangle.
- Infinite loop on a self-intersecting input.
- Claiming any triangulation is Delaunay.

---

## Board drawings

1. Induction split along a diagonal.
2. One ear, one interior point that invalidates a candidate.
3. Split / merge vertex sketches.
4. Same point set: a bad skinny triangulation vs a Delaunay preview.
