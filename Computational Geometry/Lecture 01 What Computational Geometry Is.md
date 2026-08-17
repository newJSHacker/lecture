# Lecture 1 — What computational geometry is

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `orient(a, b, c)`  
**Board first:** one picture of three points and a signed area

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Why this course exists (graphics already is geometry) |
| 10–25 | Four flagship problems |
| 25–40 | Predicates vs constructions |
| 40–55 | Degeneracy and floating point |
| 55–70 | Course contract and 15-week map |
| 70–75 | Preview `orient`, then stand up for live coding |

---

## Learning goals

By the end of the lecture a student can:

1. Name the five problem families of this course.
2. Distinguish a **predicate** from a **construction**.
3. Give three degenerate cases that break naive code.
4. Compute the 2D cross product and interpret its sign.
5. Explain why `atan2` is the wrong primitive for “left of a line.”

---

## 1. Opening (10 min)

Computer graphics is full of questions that look continuous but must be answered with discrete algorithms:

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
- **visualization** so students can see the invariant

---

## 2. Four flagship problems (15 min)

Draw each one. Do not implement yet.

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

## 3. Predicates vs constructions (15 min)

A **predicate** returns a discrete answer.

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
area(abc) = cross(b - a, c - a) / 2
```

**Why not angles?**

`atan2` is slow, wraps at ±π, and is unstable near the branch cut. The cross product uses four subtractions and two multiplies. It is the primitive of the whole course.

### Pseudocode

```
orient(a, b, c):
    v = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if v > EPS: return LEFT
    if v < -EPS: return RIGHT
    return COLLINEAR
```

This week, mention `EPS` but do not pretend it solves everything. Week 13 returns to robustness.

---

## 4. Degeneracy and floating point (15 min)

A case is **degenerate** when a predicate that is “usually” nonzero becomes zero, or when objects coincide.

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

Exact arithmetic and Shewchuk predicates are named now, required later only as reading.

---

## 5. Course contract (15 min)

### What we will implement

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

## Live coding (60 min)

Build the shared visualizer from zero.

**Must work by the end of class:**

1. Click adds a point.
2. Drag moves the nearest point.
3. Reset clears.
4. Coordinates drawn next to each point.
5. If the student (or you) has selected three points A, B, C:
   - draw segment AB
   - fill triangle ABC with green / red / gray by `orient`
   - print `LEFT`, `RIGHT`, or `COLLINEAR` and the raw cross value

Talk while typing:

- “I subtract A first so the test is translation-invariant.”
- “I do not call `Math.atan2`.”
- “I print the raw value so we can see near-zero cases.”

Starter they leave with:

```js
export function cross(ax, ay, bx, by, cx, cy) {
  return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
}

export function orient(a, b, c, eps = 1e-9) {
  const v = cross(a.x, a.y, b.x, b.y, c.x, c.y);
  if (v > eps) return 1;
  if (v < -eps) return -1;
  return 0;
}
```

---

## Lab (2–3 hours)

Using the visualizer:

1. Implement `distance(a, b)` and `midpoint(a, b)`.
2. Display the signed area of ABC.
3. Add a button: “make C collinear with AB” (project C onto AB).
4. Write 4 console tests: left, right, collinear-between, collinear-beyond.

Done when a TA can click three points and see sign, area, and distance without opening the console.

---

## Homework

Due start of Week 2.

1. Implement `orient` with 8 unit tests. Required cases:
   - left, right
   - collinear, C between A and B
   - collinear, C beyond B
   - C = A
   - very small triangle
   - a translated copy of a previous case (invariance)
2. Written (half page): why the cross product is better than comparing polar angles for the left-of-line test.
3. Written: give one floating-point input you expect to be fragile. You do not need to break IEEE; you need to explain the risk.

---

## Quiz (10 min, start of Week 2 or end of Week 1)

1. Compute `cross` for A=(0,0), B=(2,0), C=(1,3). Inside/left/right? (2 pts)
2. Is “the intersection point of two lines” a predicate or a construction? (2 pts)
3. Name two degenerate cases for segment intersection. (3 pts)
4. Why is sorting polar angles a bad replacement for `orient`? One sentence. (3 pts)

---

## Common mistakes

- Using angles.
- Testing `cross === 0` and then arguing the code is “exact.”
- Forgetting that AB is **directed**. `orient(a,b,c)` is not `orient(b,a,c)`.
- Building a visualizer that cannot move points. Degeneracy is easier to show by dragging.

---

## Board drawings

1. Triangle ABC with an arrow on AB and a + / − on C.
2. Four flagship problem thumbnails.
3. The 15-week map as five boxes: primitives, hulls, sweep/tri, proximity/search, project.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 01]] · Demo: [01-orient.html](code/01-orient.html)

Recitation picks (do not replace the homework):

1. Translate ABC by (1000, −50). Does `orient` change? Why is that better than comparing `atan2`?
2. Predicate or construction: left-of-line, intersection point, circumcenter.
3. Reduce point-in-triangle to three `orient` tests. Boundary policy?
4. Student writes `if (cross === 0)`. What policy did they just invent?

```js
function orient(a, b, c, eps = 1e-9) {
  const v = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
  if (v > eps) return 1;
  if (v < -eps) return -1;
  return 0;
}
```
