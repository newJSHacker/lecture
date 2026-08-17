# Chapter 5 — Implementation

## 5.1 Environment

| Item | Choice |
| --- | --- |
| Language | JavaScript (ES2020), `"type": "module"` |
| 2D view | HTML Canvas 2D |
| 3D view | Three.js r160, optional |
| Tests | Node test runner (or equivalent) |
| Host | static files; no server-side geometry |

The geometric kernel has no DOM dependency and is tested in Node. The visualizer imports the kernel and the algorithms. This split is what makes the test suite possible.

**Figure 5.1 (placeholder).** Repository tree: `kernel/`, `algo/`, `viz/`, `adapters/`, `tests/`.

## 5.2 Kernel

The kernel is about 250 lines. The important functions are those of Chapter 3. Two implementation notes matter for reproducibility.

**No `atan2` in predicates.** Polar sort is never used. Andrew sorts by coordinates. Delaunay uses `pointInTriangle` and `incircle`.

**One epsilon file.** Changing `EPS_ORIENT` from 1e-9 to 1e-12 is a one-line experiment. Chapter 6 forbids “tuning epsilon until the screenshot looks right” as a way to pass tests. Tests that fail only on pathological coordinates are marked `fragile` and recorded, not deleted.

Intersection points, circumcenters, and barycentric coordinates are isolated in `kernel/construct.js`. A construction is allowed to return `null` when the supporting predicate is zero.

## 5.3 Convex hull module

Andrew’s algorithm is a direct transcription of Section 4.4. The only non-obvious detail is the treatment of n ≤ 2 after unique-sort: the function returns the remaining points and does not attempt to build chains.

The step iterator yields `{stack, phase: "lower"|"upper", popped}` so the Canvas view can flash popped vertices. Tests cover:

- empty, one, two points;
- a triangle;
- a square with an interior point;
- an all-collinear set (expected: two endpoints);
- a translated copy of a previous fixture (invariance).

Jarvis is a second file with the same output contract, so the oracle test can compare the two polygons as cyclic sequences.

## 5.4 Delaunay module

The mesh is a list of triangles and a map from directed edges `(i,j)` to the opposite vertex. A flip of edge ij replaces two triangles and updates four map entries. An incorrect update here is the most common implementation bug; the step visualizer draws the twin in red if the map is asymmetric.

Point location starts at the last created triangle and walks across the edge whose orientation says the query is outside. If the walk exceeds a safety bound (4n), the implementation falls back to a linear scan and logs a warning. That guard exists because an inconsistent mesh can loop.

The super-triangle is placed using the AABB of the input, expanded by a large margin. After insertion, any triangle incident to a super-vertex is removed. Tests compare the set of edges, for n ≤ 30, with Delaunator used as an oracle [23]. Edges are compared as undirected pairs. Cocircular inputs are marked `fragile`.

## 5.5 BVH module

Build is recursive and uses a copy of the triangle-index array. The AABB of a node is the union of triangle AABBs, not the AABB of centroids; using centroids for the stored box is a bug that misses hits.

Möller–Trumbore is implemented from the original paper [9] with a parallel-guard on the determinant. Back-facing triangles are still accepted for picking; a configurator should select a part even if the click hits the underside of a thin board. Shadow rays, if added later, would cull the back face.

The debug query returns `{hit, visits, prunes, boxes[]}` for the visualizer.

## 5.6 Visualizer

The Canvas application has three tabs: Hull, Delaunay, and Pick.

Common interaction: click to add a point, drag to move, key `N` for a step, key `Space` to run. The Pick tab loads a built-in mesh of a few dozen triangles and a ground plane; a click casts a camera ray (in the 2D teaching view, an orthographic ray).

Color conventions are fixed across the course and the thesis:

| Color | Meaning |
| --- | --- |
| Blue | current hull stack / current walk triangle |
| Orange | candidate being tested / visited BVH box |
| Red | illegal edge / failed ear / back-facing debug |
| Green | accepted hull edge / legal triangle / hit |
| Gray | pruned cell or inactive geometry |

**Figure 5.2 (placeholder).** Hull step: lower stack in blue, popped point flashing.

**Figure 5.3 (placeholder).** Delaunay: circumcircle of the hover triangle, one red illegal edge.

**Figure 5.4 (placeholder).** BVH: orange visited boxes, gray pruned boxes, green hit triangle.

## 5.7 Adapters

The terrain adapter samples (x, y) in a unit square, evaluates a sum of two sine waves plus a small jitter, triangulates, and builds a `BufferGeometry`. The jitter avoids a perfectly regular grid, which produces many cocircular quads and stresses `incircle`.

The picking adapter attaches the BVH to a Three.js scene. Three.js `Raycaster` is used only as an oracle in a debug overlay, not as the shipped picker [5].

## 5.8 Testing discipline

Tests are divided into:

1. **Predicate fixtures** — hand-computed left/right/collinear and the four intersection types.
2. **Oracle tests** — Andrew vs Jarvis; Delaunay vs Delaunator on random n ≤ 30.
3. **Invariant tests** — after hull, all points have `orient ≤ 0` relative to every directed hull edge; after Delaunay, every interior edge is legal.
4. **Degeneracy tests** — duplicates, collinear hull, point on a Delaunay edge, ray through a triangle vertex.

A thesis that reports only screenshots is not considered evaluated. Chapter 6 uses these tests as the functional half of the evaluation.

## 5.9 What was not implemented

The repository deliberately omits Fortune’s algorithm, hole-aware ear clipping, a persistent DCEL editor, and exact predicates. Those omissions keep the implementation inside the page budget and match the course rule: name them, do not grade a broken Fortune.
