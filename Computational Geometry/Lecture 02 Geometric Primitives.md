# Lecture 2 — Geometric primitives

**Week 2 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** onSegment = collinear + AABB; segmentsIntersect → proper|touch|overlap|none; then construct the point  
**Success check:** they classify four pictures live and get BOUNDARY on a vertex, not a flicker

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/02-on-segment.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a correct kernel — everything later depends on this week | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
onSegment(c,a,b): orient=0 AND c in AABB(ab)

proper: opposite-sign orients, zeros not opposite
touch:  endpoint on the other (T) or shared vertex
overlap: collinear 1D intervals overlap
none:   including AABB-overlap but miss

PIP even–odd: half-open edges
  (a.y>q.y) != (b.y>q.y)
onSegment first → BOUNDARY

AABB is a reject, not the answer
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last week’s sign is this week’s intersection classifier. Classify with predicates; divide for the point only if proper or touch. The denominator is cross(B−A,D−C); near zero means parallel — do not divide.

**Ask:** Two AABBs overlap. Must the segments intersect? Wait. Want: no.

**Board:** parked strip. Then the five objects (point, segment, ray, line, polygon).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`onSegment`, `segmentsIntersect`, `pointInPolygon`*.

**Do not:** `== 0` on the cross product.

### Minutes 10–12 — Frame

**Say:** Point, vector, segment t∈[0,1], ray t≥0, line ℝ, closed polygon. Winding number named; even–odd is enough for simple polygons. Treating touch as none breaks later DCEL and map overlay. Zero-length segment is a test, not a surprise.

**Ask:** Why is collinear not enough for onSegment?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Four pictures: X, T, collinear overlap, disjoint boxes that overlap.

**Board:** four types. Ray through a vertex, then the half-open rule. AABB counterexample.

**Say:** Return type includes point for proper and touch.

**Ask:** A=(0,0),B=(4,0),C=(2,2),D=(2,−2). Type?

**They do:** On paper: why classify before dividing. Half-open edge rule, one paragraph.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Two segments, four draggable ends. Color green/orange/purple/gray. Draw the point. Overlay AABBs. Script all four cases. Pause on boxes-overlap/no-hit: ‘the box is not the algorithm.’ Demo 03-segments.html. Plant ==0. Plant counting both edges on a vertex hit.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** onSegment then proper-only intersect. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pointInPolygon even–odd on a concave polygon; vertex, edge, ray-hits-vertex. Homework: four-way segmentsIntersect + identical and zero-length. Quiz: type, onSegment, vertex-hit drawing, AABB converse.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Five objects | Polygon is closed: last→first. |
| 10–35 | Four intersection types live | Plant dividing while parallel. |
| 35–50 | AABB overlap, miss | Dashed boxes. |
| 50–60 | Ray through vertex plant | Then half-open. |

Point them at `Computational Geometry/code/02-on-segment.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement `pointInPolygon` (even–odd) on a concave polygon the user can draw.
2. Required test shapes:
3. convex
4. concave C-shape
5. query on a vertex
6. query on an edge
7. query whose ray hits a vertex
8. Display `INSIDE` / `OUTSIDE` / `BOUNDARY`.

---

## Homework

1. Implement `segmentsIntersect` returning the four-way type. Tests for all four pictures plus:
2. shared endpoint
3. identical segments
4. zero-length segment (A = B)
5. Written: why we classify with orientations before dividing for the intersection point.
6. Written: give the half-open edge rule in one paragraph.

---

## Quiz next meeting (they hear this now)

1. A=(0,0), B=(4,0), C=(2,2), D=(2,−2). Type of intersection? (2 pts)
2. Why is collinear not enough for `onSegment`? (2 pts)
3. Draw a concave polygon and a point whose naive ray hits a vertex. (3 pts)
4. Two AABBs overlap. Must the segments intersect? Yes/no and one sentence. (3 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Objects (10 min).** | Object | Definition we will use |
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

**2. `onSegment` (15 min).** C lies on segment AB iff:
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

**3. Segment intersection (20 min).** Let S1 = AB, S2 = CD.
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
A + t (B - A) = C 

**4. Point in polygon (20 min).** ### Ray casting (even–odd)
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
The condition `(a.y > q.y) != (b.y > q.y)` is

**5. Bounding boxes (10 min).** The **AABB** of a segment or polygon is
```
(min x, min y, max x, max y)
```
If two AABBs are disjoint, the objects cannot intersect. The converse is false. Picture 4 from Section 3 is the counterexample.
In graphics this is the broad phase. Computational geometry still needs the narrow-phase predicate.
---

---

## Common mistakes

1. `== 0` on the cross product.
2. Dividing before checking parallel.
3. Counting both edges when the ray hits a vertex.
4. Treating `touch` as `none` (breaks later DCEL and map overlay).
5. Using the AABB as the answer.

## If we run long, cut

Full winding-number holes. Keep four types + PIP vertex bug.

## If we run short, add

Shared endpoint as touch.
