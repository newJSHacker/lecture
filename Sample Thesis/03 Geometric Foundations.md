# Chapter 3 — Geometric Foundations

This chapter records the definitions and predicates on which the rest of the thesis depends. Implementation details appear in Chapter 5. The notation follows de Berg et al. [1] with a few web-specific conventions.

## 3.1 Objects

A **point** is a pair (x, y) in ℝ², or (x, y, z) in ℝ³. A **vector** is the difference of two points. A **segment** ab is the set (1−t)a + t b for t ∈ [0, 1]. A **ray** uses t ≥ 0. A **simple polygon** is a closed chain of vertices whose edges meet only at shared endpoints. A **triangle** is a simple polygon with three vertices. All 2D polygons in this thesis are assumed to be given in counterclockwise (CCW) order unless stated otherwise.

## 3.2 The orientation predicate

For points a, b, c in the plane define

```
cross(a, b, c) = (b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x).
```

This quantity is twice the signed area of triangle abc. The **orientation** is

```
orient(a, b, c) = +1    if cross > ε
                =  0    if |cross| ≤ ε
                = −1    if cross < −ε.
```

The value +1 means that c lies to the left of the directed line ab (CCW). The value −1 means right (CW). Zero is reported as collinear *under the epsilon policy*, not as exact collinearity.

Orientation is translation invariant if it is computed from differences, as above. It is not rotation-invariant under naive scaling: very large coordinates can overflow the meaningful bits of a double [32]. Inputs in this system are expected to lie in a reasonable world box, for example [−1e6, 1e6]² after a scene transform.

Polar angles are not used as a substitute for orientation. The function `atan2` is slower, wraps at ±π, and is a construction, not a predicate.

## 3.3 On-segment and intersection

Point c lies on segment ab if `orient(a, b, c) = 0` and c lies in the axis-aligned bounding box of ab, expanded by ε. Collinearity alone is not sufficient.

Two segments ab and cd are classified as:

- **proper** — they cross at a point interior to both;
- **touch** — they share a point that is an endpoint of at least one segment;
- **overlap** — they are collinear and their intervals overlap in more than a point;
- **none**.

A proper intersection exists when `orient(a, b, c)` and `orient(a, b, d)` have opposite nonzero signs, and the same holds with the roles reversed. The intersection *point* is a construction and is computed only after the predicate says the intersection exists. Parallel segments are detected by a near-zero cross product of their directions; the code must not divide in that case.

## 3.4 Point in triangle and point in polygon

A point q is strictly inside a CCW triangle abc if `orient(a, b, q)`, `orient(b, c, q)`, and `orient(c, a, q)` are all positive. Boundary cases are reported separately when any orientation is zero and `onSegment` holds.

Point-in-polygon uses the even–odd rule with a half-open edge convention so that a ray through a vertex is not counted twice [2]. The implementation tests the boundary first. This predicate is used by the Delaunay locator and by 2D picking.

## 3.5 Convexity and hulls

A set S is convex if it contains the segment between any two of its points. The **convex hull** CH(S) is the smallest convex set containing S. For a finite set it is a convex polygon whose vertices are extreme points of S.

**Degeneracy policy (hull).** Duplicate points, identified within ε in both coordinates, are removed before construction. If three hull vertices would be collinear, the middle vertex is dropped. The output is therefore a strictly convex polygon, possibly with fewer vertices than a human drawing of the “visual” hull.

A simple polygon is convex if and only if every consecutive triple has the same nonzero orientation [2]. The bowtie (two segments crossing) shows that the same-turn test is not sufficient without simplicity.

## 3.6 Incircle and Delaunay legality

Let abc be a CCW triangle and d a fourth point. The **incircle** predicate reports whether d lies inside, on, or outside the unique circle through a, b, and c. In exact arithmetic it is the sign of a 4×4 determinant [32]. This thesis uses that determinant in double precision, with an epsilon on the result, and notes that the test is more fragile than orientation.

An interior edge ad shared by triangles abd and acd is **illegal** if the incircle of one triangle contains the opposite vertex of the other. A **flip** replaces ad by the other diagonal. A triangulation of a point set is Delaunay if and only if every interior edge is legal [1]. Flips terminate because each flip increases the minimum angle.

The empty-circle property of a Voronoi vertex is the same statement in dual form [19]: the circumcenter of a Delaunay triangle is a Voronoi vertex, and its circumcircle contains no site in its interior.

## 3.7 Bounding volumes and rays

The **axis-aligned bounding box** (AABB) of a set is the product of the intervals of its coordinates. If two AABBs are disjoint, the objects cannot intersect. The converse is false; the AABB is a reject test, not an intersection test.

A **bounding-volume hierarchy** is a binary tree whose leaves hold primitives (here, triangles) and whose internal nodes hold the AABB of their descendants [4], [28]. A query that misses a node box never visits the children.

A ray is o + t d with t ≥ 0. Intersection with an AABB uses the slab method (per-axis t intervals). Intersection with a triangle uses Möller–Trumbore barycentric coordinates (t, u, v) [9]. A hit requires t ≥ 0, u ≥ 0, v ≥ 0, and u + v ≤ 1.

## 3.8 Complexity model

Running-time claims use the standard real-RAM / algebraic decision-tree model of computational geometry [1], [2]. They describe the number of predicate evaluations, not JavaScript wall-clock time. Chapter 6 measures wall-clock time separately and treats it as an implementation property.

The relevant bounds for this thesis are:

| Problem | Naive | Implemented |
| --- | --- | --- |
| Convex hull | — | Andrew O(n log n); Jarvis Θ(n h) |
| Delaunay, incremental, walk locate | O(n²) worst case | expected better; lab target n ≤ 2,000 |
| All-pairs closest / all-pairs intersect | Θ(n²) | used only as oracles |
| Ray vs n triangles | Θ(n) | BVH: output-sensitive; worst case still linear |

A 2D hull has an Ω(n log n) lower bound by reduction from sorting (map x_i to (x_i, x_i²)) [1]. Andrew is therefore optimal in the worst-case sense used in undergraduate courses.

## 3.9 Implications for the kernel

All later chapters assume a single module that exports `orient`, `onSegment`, `segmentsIntersect`, `pointInTriangle`, `incircle`, and AABB tests. No algorithm is allowed to reimplement a predicate with a private epsilon. That rule is the main software-engineering contribution of the thesis, and it is the one most often violated in student code.
