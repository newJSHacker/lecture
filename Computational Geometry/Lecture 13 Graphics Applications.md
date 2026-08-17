# Lecture 13 — From 2D algorithms to graphics systems

**Week 13 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** click → ray → BVH AABB prune → triangle (orient / barycentric); EPS is a policy; Shewchuk named; Three.js Raycaster is an oracle  
**Success check:** a vertical slice runs; they name the predicate that would break it; visited boxes vs hit triangle are visible

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/13-kd-range.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: connect the course to IGWT; picking is geometry, not ‘the engine knows’ | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
configurator: click → ray → BVH → triangle → barycentric → part
orient → back-face, clip side, ears
EPS = thick line, not exact     inconsistent signs possible
Shewchuk: adaptive; call a library for thesis meshes
3D orient = signed tetra volume

libraries hide: three-mesh-bvh, earcut, Delaunator, Recast
course rule: main algorithm is student code
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Joint with Computer Graphics I: the GPU picture does not replace the predicate. Growing EPS until Delaunay looks fine is forbidden. Starting the project from zero this week is what the checkpoint exists to prevent.

**Ask:** Why is EPS not exact? Wait. Want: it makes a band of COLLINEAR; predicates can still disagree around a cycle.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *From 2D algorithms to graphics systems*.

**Do not:** Using Three.js `Raycaster` for the live-coding “implementation” without a student BVH. Allowed as oracle, not as the demo of the algorithm.

### Minutes 10–12 — Frame

**Say:** Payoff table slowly, one course sentence + one IGWT sentence. Practical rules: snap UI, unique within EPS, one kernel file, do not grow EPS to pass tests. Ray–triangle: t,u,v barycentric, t≥0, u,v≥0, u+v≤1. Mesh repair is DCEL + Week 6 intersections — academic ‘Repair in Blender.’

**Ask:** 3D analog of orient(a,b,c)?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Leave one payoff column empty; fill with the class.

**Board:** payoff table. Three points, three disagreeing epsilon signs. Ray vs AABB vs triangle. Miss the parent box, never see the children.

**Say:** Terrain: Delaunay → normals → BufferGeometry. Collision: hull/AABB then SAT/segments.

**Ask:** Which course algorithm does click-to-pick use?

**They do:** README: build, degeneracy list, 6-bullet report outline. Project only.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** 20–80 triangles. Top-down BVH, longest-axis median. On click: orange visited boxes, gray pruned, green hit, print id and u,v. ‘Week 9 prune plus Week 2 inside-triangle, in 3D clothing.’ Demo 18-bvh-pick.html. Plant using Raycaster as the implementation. Plant five copies of orient with five epsilons.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Miss-parent-box early out. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: 10-minute vertical slice — algorithm theirs, something moves, one degeneracy discussed, repo runs, they know the weeks. Checkpoint complete/incomplete + advice. Quiz: pick pipeline, EPS, Shewchuk, 3D orient, one BVH library.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Fill the payoff table | Configurator row last. |
| 15–35 | Inconsistent epsilon picture | One kernel file. |
| 35–50 | BVH pick live | Count box tests vs triangle tests on a far miss. |
| 50–60 | Checkpoint roster | Advice, not grade shock. |

Point them at `Computational Geometry/code/13-kd-range.html` as the after-class check, not as the lecture.

---

## Lab

_(none this meeting)_

---

## Homework

1. README with build instructions
2. List of degenerate cases you handle or document
3. A 6-bullet report outline

---

## Quiz next meeting (they hear this now)

1. Which course algorithm does click-to-pick in a configurator use? (2 pts)
2. Why is EPS not exact? (2 pts)
3. What does Shewchuk’s method do that EPS does not? (2 pts)
4. 3D analog of `orient(a,b,c)`? (2 pts)
5. Name one library that hides BVH raycast. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. The payoff table (20 min).** Walk this slowly. For each row: one sentence from the course, one sentence from IGWT.
| Algorithm | Graphics / web use | Course week |
| --- | --- | --- |
| `orient` / predicates | back-face sign, clipping side, ear test | 1–2 |
| Segment intersection | CAD, map overlay, stroke vs stroke, clipping | 2, 6 |
| Point in polygon | click a country, select a mesh island in 2D UI | 2 |
| Convex hull | OBB / tight 2D collider, silhouette extremes | 4–5 |
| Sweep intersections | boolean outlines, font self-overlap | 6 |
| Ear clipping | Canvas/SVG fill, UI blobs, simple roofs | 7 |
| DCEL / half-edge | mesh edit, subdivision, walk rings | 8 |
| kd-tree | 2D range, “who is in this tile?” | 9 |
| BVH | ray picking, frustum culling, collision broad phase | 9, today |
| Voronoi | stipple, territories, 

**2. Robustness (20 min).** ### The problem, again
Orientation of nearly collinear points is a sign of a tiny determinant. IEEE-754 rounds. A predicate that is wrong **once** can:
- flip the wrong Delaunay edge
- invert a hull turn and lose a vertex
- mis-classify a click as outside
`EPS` does not make the predicate exact. It creates a **thick line** where you return COLLINEAR. That is a policy. It can still be inconsistent: A left of BC, B left of CA, C left of AB.
### Three levels (teach the names)
| Level | What | When |
| --- | --- | --- |
| Epsilon | `abs(cross) < EPS` | UI, games, this course’s default |
| Adaptive exact | Shewchuk: start float, recompute with more precision only if the error bound is bad | meshing, CAD |
| Exact rational / CGAL | integers or rationals, slow | kernels, research |
Shewchuk’s pap

**3. What changes in 3D (15 min).** | 2D | 3D |
| --- | --- |
| `orient` 3 points | `orient` 4 points (signed tetra volume) |
| Segment–segment | segment–triangle, triangle–triangle |
| Convex polygon | convex polyhedron |
| Delaunay triangles | Delaunay tetrahedra (sliver tets are a research problem) |
| Voronoi cells (polygons) | Voronoi cells (polyhedra) |
| Ear clipping | no simple analog; use CDT or voxel / tet tools |
| Point in polygon | point in polyhedron (ray cast + solid winding) |
**Ray–triangle (Möller–Trumbore, teaching).**  
Ray `o + t d`, triangle abc. Solve for t, u, v barycentric. Hit if t ≥ 0, u ≥ 0, v ≥ 0, u+v ≤ 1.
This is the narrow phase under the BVH.
**Mesh repair.**  
Imported glTF often has: non-manifold edges, opposite windings, duplicate vertices, self-intersections. A DCEL rebuild + Week 6 inters

**4. Who hides this in production (10 min).** | Library | What it hides |
| --- | --- |
| Three.js | scene graph, not spatial index (unless you add one) |
| `three-mesh-bvh` | BVH + raycast |
| cannon.js / rapier / PhysX | collision, often GJK / SAT / hulls |
| earcut | 2D ear clipping (hole support) |
| Delaunator | 2D Delaunay |
| CGAL | exact predicates, 3D hulls, tets |
| Recast / Detour | navmesh |
**Course rule still stands:** the project’s **main** algorithm is student code. These libraries may render, load models, or provide a reference oracle.
---

---

## Common mistakes

1. Using Three.js `Raycaster` for the live-coding “implementation” without a student BVH. Allowed as oracle, not as the demo of the algorithm.
2. Growing EPS until Delaunay “looks fine.”
3. Starting the project this week from zero. The checkpoint exists to prevent that.

## If we run long, cut

Exact CGAL kernel. Keep mapping + BVH pick + EPS policy.

## If we run short, add

Black-screen / miss: the ray never hit the parent box.
