# Week 2 — Geometric primitives

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `onSegment`, `segmentsIntersect`, `pointInPolygon`  
**Board first:** the five objects (point, segment, ray, line, polygon)

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz from Week 1, then objects |
| 10–25 | Cross product recap and `onSegment` |
| 25–45 | Segment–segment intersection, all four answers |
| 45–65 | Point in polygon: ray casting and winding |
| 65–75 | Bounding boxes; list the failure cases |

---

## Learning goals

1. Define point, vector, segment, ray, line, and simple polygon.
2. Implement `onSegment` using orientation + bounding box.
3. Classify two segments as `proper`, `touch`, `overlap`, or `none`.
4. Explain ray casting and the vertex-hit bug.
5. Use an AABB as a reject test, not as the intersection test.

---

## 1. Objects (10 min)

| Object | Definition we will use |
| --- | --- |
| Point | `(x, y)` |
| Vector | difference of two points |
| Segment `ab` | points `(1-t)a + t b` for `t ∈ [0, 1]` |
| Ray `ab` | same, `t ≥ 0` |
| Line `ab` | same, `t ∈ ℝ` |
| Polygon | cyclic sequence of vertices `v0…v_{n-1}` with edges `vi → v_{i+1}` |

A polygon is **closed**. Edge `v_{n-1} → v0` always exists.

We do **not** yet require convexity. We do require that students can walk edges in order.

---

## 2. `onSegment` (15 min)

C lies on segment AB iff:

1. `orient(A, B, C) = 0` (collinear)
2. C is inside the axis-aligned bounding box of AB

```
onSegment(c, a, b):
    if orient(a, b, c) != 0: return false
    return min(a.x, b.x) - EPS <= c.x <= max(a.x, b.x) + EPS
       and min(a.y, b.y) - EPS <= c.y <= max(a.y, b.y) + EPS
```

**Why the box?** Collinear is not enough. C can sit on the line but outside the segment.

Draw:

```
A ---- B          C          (collinear, not on segment)
A -- C -- B                  (on segment)
A = C ---- B                 (on segment: endpoint)
```

---

## 3. Segment intersection (20 min)

Let S1 = AB, S2 = CD.

### Proper intersection

The segments cross at a point that is **interior** to both.

Predicate (no division):

```
orient(A,B,C) and orient(A,B,D) have opposite signs
AND
orient(C,D,A) and orient(C,D,B) have opposite signs
```

Opposite signs means one LEFT and one RIGHT. Zero is not opposite.

### Improper / touch

They share an endpoint, or one endpoint lies in the interior of the other (T-junction).

Use `onSegment`.

### Overlap

Collinear and the 1D intervals overlap.

### None

Everything else, including “bounding boxes overlap but segments do not.”

### Return type for the course

```
{ type: "proper" | "touch" | "overlap" | "none",
  point?: {x, y} }   // required for proper and touch
```

### Construction of the proper intersection point

Parametric:

```
A + t (B - A) = C + u (D - C)
```

Solve the 2×2 system. The denominator is `cross(B-A, D-C)`. If it is near zero, they are parallel; do not divide.

**Teach this order:** classify with predicates, construct the point only if `proper` or `touch`.

### Four pictures (draw all four)

1. Crossing X — `proper`
2. T-junction — `touch`
3. Two collinear overlapping intervals — `overlap`
4. Two disjoint segments whose AABBs overlap — `none`

---

## 4. Point in polygon (20 min)

### Ray casting (even–odd)

Cast a ray from q to +∞ in x (or a slightly tilted ray). Count crossings with polygon edges. Odd ⇒ inside.

**The vertex bug:** if the ray hits a vertex, two edges can both count, or neither, and the parity is wrong.

**Standard fix (half-open edges):** an edge `vi → vj` is counted only if one endpoint is strictly above the ray and the other is on or below (or the symmetric rule). Pick one rule and keep it.

```
pointInPolygonEvenOdd(q, P):
    inside = false
    for each edge (a, b) of P:
        if onSegment(q, a, b): return BOUNDARY
        if (a.y > q.y) != (b.y > q.y):
            xHit = a.x + (q.y - a.y) * (b.x - a.x) / (b.y - a.y)
            if q.x < xHit: inside = !inside
    return inside ? INSIDE : OUTSIDE
```

The condition `(a.y > q.y) != (b.y > q.y)` is the half-open trick.

### Winding number

Walk the boundary. Add +1 for CCW windings around q, −1 for CW. Nonzero ⇒ inside.

Winding handles holes and overlapping windings more cleanly. Even–odd is enough for simple polygons in this course.

### Boundary

Always test `onSegment` first. “Inside” vs “on” matters for picking and for clipping.

---

## 5. Bounding boxes (10 min)

The **AABB** of a segment or polygon is

```
(min x, min y, max x, max y)
```

If two AABBs are disjoint, the objects cannot intersect. The converse is false. Picture 4 from Section 3 is the counterexample.

In graphics this is the broad phase. Computational geometry still needs the narrow-phase predicate.

---

## Live coding (60 min)

Implement `segmentsIntersect` in the visualizer.

Interaction:

- Two segments, four draggable endpoints
- Color: green proper, orange touch, purple overlap, gray none
- Draw the intersection point when it exists
- Overlay both AABBs as dashed rectangles

Script the four cases by dragging live. Pause on the AABB-overlap / no-intersection case and say: “this is why the box is not the algorithm.”

Leave `pointInPolygon` as the lab. Show one failing ray-through-vertex if time remains.

---

## Lab

1. Implement `pointInPolygon` (even–odd) on a concave polygon the user can draw.
2. Required test shapes:
   - convex
   - concave C-shape
   - query on a vertex
   - query on an edge
   - query whose ray hits a vertex
3. Display `INSIDE` / `OUTSIDE` / `BOUNDARY`.

Done when the TA can put a point on a vertex and get `BOUNDARY`, not a flicker between in and out.

---

## Homework

1. Implement `segmentsIntersect` returning the four-way type. Tests for all four pictures plus:
   - shared endpoint
   - identical segments
   - zero-length segment (A = B)
2. Written: why we classify with orientations before dividing for the intersection point.
3. Written: give the half-open edge rule in one paragraph.

---

## Quiz (10 min)

1. A=(0,0), B=(4,0), C=(2,2), D=(2,−2). Type of intersection? (2 pts)
2. Why is collinear not enough for `onSegment`? (2 pts)
3. Draw a concave polygon and a point whose naive ray hits a vertex. (3 pts)
4. Two AABBs overlap. Must the segments intersect? Yes/no and one sentence. (3 pts)

---

## Common mistakes

- `== 0` on the cross product.
- Dividing before checking parallel.
- Counting both edges when the ray hits a vertex.
- Treating `touch` as `none` (breaks later DCEL and map overlay).
- Using the AABB as the answer.

---

## Board drawings

1. The four intersection types.
2. Ray casting with a vertex hit, then the same figure with the half-open rule marked.
3. AABB of two disjoint crossing-looking segments that do not meet.
