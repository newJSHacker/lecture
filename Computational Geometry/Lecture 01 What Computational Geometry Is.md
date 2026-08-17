# Lecture 1 — What computational geometry is

**Week 1 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** orient(a,b,c) = sign of cross(b−a, c−a); LEFT / RIGHT / COLLINEAR; atan2 is the wrong primitive  
**Success check:** they can color a triangle left/right/collinear, print the raw cross, and say why not atan2

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Computational Geometry/code/01-orient.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: see that graphics already is computational geometry; freeze predicates, degeneracy, visualization | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
cross(b−a, c−a) = (bx−ax)(cy−ay) − (by−ay)(cx−ax)
>0 LEFT of directed ab (CCW)    =0 COLLINEAR    <0 RIGHT
area = cross / 2

predicate: discrete answer     construction: new geometry
atan2: slow, wraps ±π, branch cut     cross: four sub, two mul

degenerate: collinear hull · T-junction · overlap · duplicate verts
1e20 can swallow a 1 in IEEE — detect; do not hope
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Does this click hit the polygon? Do these walls cross? That is this course. 2D first; 3D is the same idea with one extra coordinate. A construction inherits the predicate’s errors — implement predicates first.

**Ask:** Is the intersection point of two lines a predicate or a construction? Wait. Want: construction.

**Board:** parked strip. Then one picture of three points and a signed area.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`orient(a, b, c)`*.

**Do not:** Using angles.

### Minutes 8–12 — Frame

**Say:** Four flagships: closest pair, hull, segment intersection, point in polygon. Fifth family named: proximity and search. Course policy: detect degeneracy, write a policy, write a test, never ==0 on a float without saying EPS. EPS does not solve everything — Week 13 robustness. We will not implement full Fortune, Kirkpatrick, 3D Delaunay, CGAL kernels; we name them. JS + Canvas. Labs 25, hw 20, quizzes 10, midterm 15, project 30.

**Ask:** Why is sorting polar angles a bad replacement for orient?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** AB is directed. orient(a,b,c) is not orient(b,a,c).

**Board:** triangle ABC, arrow on AB, +/− on C. Four flagship thumbnails. 15-week map: primitives, hulls, sweep/tri, proximity/search, project.

**Say:** I subtract A first so the test is translation-invariant. I print the raw value so near-zero is visible. I do not call Math.atan2.

**Ask:** cross for A=(0,0), B=(2,0), C=(1,3) — left/right?

**They do:** On paper: why cross beats polar angles for left-of-line, half page. One fragile float input (explain the risk).

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Visualizer from zero: click add, drag, reset, coordinates. Three points: segment AB, fill green/red/gray by orient, print LEFT/RIGHT/COLLINEAR and raw cross. Demo Computational Geometry/code/01-orient.html. Plant atan2. Plant cross===0 as ‘exact.’

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** orient with eps. Eight minutes. Four console tests: left, right, collinear-between, collinear-beyond.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: distance, midpoint, signed area, ‘make C collinear’ button. Homework: 8 tests including C=A, tiny triangle, translated copy. Quiz: cross, predicate vs construction, two degeneracies, why not atan2.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Click / drag visualizer | A visualizer that cannot move points cannot show degeneracy. |
| 10–35 | orient + raw cross | Plant atan2. Print v. |
| 35–50 | Drag to collinear | Gray + near-zero. |
| 50–60 | They add signed area | Circulate. |

Point them at `Computational Geometry/code/01-orient.html` as the after-class check, not as the lecture.

---

## Lab

_(none this meeting)_

---

## Homework

1. Implement `orient` with 8 unit tests. Required cases:
2. left, right
3. collinear, C between A and B
4. collinear, C beyond B
5. C = A
6. very small triangle
7. a translated copy of a previous case (invariance)
8. Written (half page): why the cross product is better than comparing polar angles for the left-of-line test.
9. Written: give one floating-point input you expect to be fragile. You do not need to break IEEE; you need to explain the risk.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Computational Geometry/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Opening (10 min).** Computer graphics is full of questions that look continuous but must be answered with discrete algorithms:
- Does this click hit the polygon?
- Do these two walls cross?
- What is the outline of this point cloud?
- Which triangle contains the ray?
- Who is the nearest site to this pixel?
Computational geometry is the study of **algorithms for geometric objects**: points, segments, polygons, and later meshes.
This course is 2D-first. Almost every 3D graphics test (ray–triangle, frustum, collision) is the same idea with one extra coordinate.
Write on the board:
```
input: finite set of points / segments / polygons
output: a combinatorial structure + a few constructed points
```
We care about:
- **correctness** on ugly inputs
- **complexity** in n
- **visualization** so students can see the i

**2. Four flagship problems (15 min).** Draw each one. Do not implement yet.
### Closest pair
Input: n points.  
Output: the two that are nearest.
Naive: try all pairs, Θ(n²).  
This course: divide and conquer, O(n log n) (Week 12).
### Convex hull
Input: n points.  
Output: the smallest convex polygon containing them.
Mental image: stretch a rubber band around nails.
### Segment intersection
Input: n line segments.  
Output: all crossing points, or yes/no.
Naive: every pair, Θ(n²).  
This course: sweep line (Week 6).
### Point in polygon
Input: a polygon P and a query point q.  
Output: inside / outside / on boundary.
Used every time a user clicks a shape.
**Fifth family, named now, taught later:** proximity (Voronoi / Delaunay) and search (kd-tree / BVH).
---

**3. Predicates vs constructions (15 min).** A **predicate** returns a discrete answer.
Examples:
- Is c left of directed line ab?
- Do segments ab and cd intersect?
- Is triangle abc oriented counterclockwise?
A **construction** returns new geometry.
Examples:
- The intersection point of two lines
- The circumcenter of three points
- The convex hull polygon
**Teaching rule:** implement predicates first. Constructions inherit their errors.
The fundamental 2D predicate is orientation.
For points a, b, c define
```
cross(b - a, c - a) = (bx - ax)(cy - ay) - (by - ay)(cx - ax)
```
| Sign | Meaning |
| --- | --- |
| > 0 | c is to the **left** of directed line ab (CCW) |
| = 0 | a, b, c are **collinear** |
| < 0 | c is to the **right** of ab (CW) |
This value is also twice the signed area of triangle abc.
```
area(abc) = cross(b - a, c - 

**4. Degeneracy and floating point (15 min).** A case is **degenerate** when a predicate that is “usually” nonzero becomes zero, or when objects coincide.
Show these four pictures:
1. Three collinear points on a hull
2. Two segments that touch at an endpoint (T-junction)
3. Two overlapping collinear segments
4. Duplicate vertices in a polygon
Then show the floating-point surprise:
```
a = (0, 0)
b = (1, 0)
c = (1e20, 1)
```
The true orientation is LEFT, but `1e20` can swallow the `1` in IEEE-754 double. Naive code reports COLLINEAR.
**Course policy on degeneracy:**
- Detect it. Do not hope it will not happen.
- Define a policy (keep collinear hull points or drop them).
- Write a test for it.
- Never use `== 0` on a computed float without saying you are using an epsilon.
Exact arithmetic and Shewchuk predicates are named now, required l

**5. Course contract (15 min).** ### What we will implement
Weeks 1–7: kernel, polygons, hulls, sweep, triangulation.  
Week 8: midterm + DCEL.  
Weeks 9–12: search, Voronoi, Delaunay, closest pair.  
Weeks 13–15: graphics applications and the project.
### What we will not implement
Full Fortune, Kirkpatrick point location, 3D Delaunay, CGAL kernels. We will **name** them.
### How a week works
Lecture → live coding on a canvas → lab → homework → 10-minute quiz.
### Assessment reminder
Labs 25%, homework 20%, quizzes 10%, midterm 15%, project 30%.
### Language
JavaScript + Canvas, unless the department has already standardized on Python. The math does not change.
---

---

## Common mistakes

1. Using angles.
2. Testing `cross === 0` and then arguing the code is “exact.”
3. Forgetting that AB is **directed**. `orient(a,b,c)` is not `orient(b,a,c)`.
4. Building a visualizer that cannot move points. Degeneracy is easier to show by dragging.

## If we run long, cut

Shewchuk details. Keep orient + degeneracy pictures.

## If we run short, add

Reduce point-in-triangle to three orient tests — name the boundary policy.
