# Lecture 13 — From 2D algorithms to graphics systems

**Time:** 75 min lecture + 60 min live coding  
**Live coding:** ray–triangle picking through a BVH  
**Lab:** project checkpoint (vertical slice)  
**Homework:** project only

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 12 |
| 10–30 | Algorithm → engine table |
| 30–50 | Robustness (epsilon, adaptive, exact) |
| 50–65 | What changes in 3D |
| 65–75 | Where libraries hide this |

---

## Learning goals

1. Map every core algorithm of the course to a graphics / web use.
2. Explain why `EPS` is a policy, not a proof.
3. Name Shewchuk adaptive predicates and when to use a library.
4. List what becomes harder in 3D (hull, Delaunay, predicates).
5. Pick a triangle in a small mesh with a BVH and a ray.

---

## 1. The payoff table (20 min)

Walk this slowly. For each row: one sentence from the course, one sentence from IGWT.

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
| Voronoi | stipple, territories, procedural blocks | 10 |
| Delaunay / CDT | terrain, navmesh, remesh | 11 |
| Closest pair | snap, weld, “too close to merge” | 12 |
| Minkowski | character vs wall in configuration space | 12 |
| Visibility graph | 2D path prototype; navmesh in production | 12 |

**Product configurator** (the program’s flagship example):  
click → ray → BVH → triangle → barycentric coordinates → which part / material. That is Weeks 2 + 9 + today.

**Terrain:** sites or height samples → Delaunay → vertex normals → a Three.js `BufferGeometry`. Weeks 11 + Computer Graphics I.

**Collision:** hull or AABB broad phase, SAT or segment tests narrow phase. Weeks 3–6.

---

## 2. Robustness (20 min)

### The problem, again

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

Shewchuk’s paper / notes are the reading. We do not reimplement them. For a thesis-quality mesh tool, **call a library**.

### Practical course rules

1. Snap inputs (grid) when the UI allows it.
2. Remove duplicates within EPS before hull / Delaunay.
3. One kernel file; do not copy `orient` into five files with five epsilons.
4. If a test fails only on a 1e-12 case, record it; do not “fix” by growing EPS until all tests pass.

---

## 3. What changes in 3D (15 min)

| 2D | 3D |
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
Imported glTF often has: non-manifold edges, opposite windings, duplicate vertices, self-intersections. A DCEL rebuild + Week 6 intersections is the academic version of “click Repair in Blender.”

---

## 4. Who hides this in production (10 min)

| Library | What it hides |
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

## Live coding (60 min)

A mini scene: 20–80 triangles (a box, a ground, a few props). No Three.js required; a 2D projection of 3D is enough, or a simple canvas raycaster.

1. Build a BVH of triangle AABBs (top-down median split on the longest axis).
2. On click, cast a ray.
3. Draw visited boxes in orange, pruned in gray, the hit triangle in green.
4. Print triangle id and barycentric u, v.

Talk: “this is Week 9’s prune test plus Week 2’s inside-triangle test, in 3D clothing.”

---

## Lab — project checkpoint

Each team (2–3) demos a **vertical slice** (10 minutes including setup):

- The core algorithm runs on a non-trivial input.
- Something moves on screen (not a screenshot-only).
- They can name the predicate that would break their demo.

TA / professor checklist:

| Check | Yes / no |
| --- | --- |
| Algorithm is theirs, not a library | |
| Visualizer or scene exists | |
| One degenerate case discussed | |
| Repo clones and runs | |
| They know which Weeks they are using | |

No grade shock this week: checkpoint is completion + advice. The rubric lives in Week 15.

---

## Homework

Project only. Before Week 14:

- README with build instructions
- List of degenerate cases you handle or document
- A 6-bullet report outline

---

## Quiz (10 min)

1. Which course algorithm does click-to-pick in a configurator use? (2 pts)
2. Why is EPS not exact? (2 pts)
3. What does Shewchuk’s method do that EPS does not? (2 pts)
4. 3D analog of `orient(a,b,c)`? (2 pts)
5. Name one library that hides BVH raycast. (2 pts)

---

## Common mistakes

- Using Three.js `Raycaster` for the live-coding “implementation” without a student BVH. Allowed as oracle, not as the demo of the algorithm.
- Growing EPS until Delaunay “looks fine.”
- Starting the project this week from zero. The checkpoint exists to prevent that.

---

## Board drawings

1. The payoff table (keep one column empty and fill with the class).
2. Inconsistent epsilon orientations (three points, three disagreeing signs).
3. Ray vs AABB vs triangle.
4. BVH: miss the parent box, never see the children.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 13]] · Demo: [18-bvh-pick.html](code/18-bvh-pick.html)

1. Configurator: click → ray/point → BVH → triangle → barycentric → part.
2. EPS is a thick line, not exact arithmetic. Inconsistent orientations exist.
3. Three.js `Raycaster` is an oracle, not the student BVH.
4. Count box tests vs triangle tests on a far miss.

```js
function pickBVH(node, q, hits) {
  if (!aabbContains(node.box, q)) return;
  if (node.leaf) {
    const t = node.item.t;
    if (pointInTriangle(q, t.a, t.b, t.c) !== "OUTSIDE") hits.push(node.item);
    return;
  }
  pickBVH(node.left, q, hits);
  pickBVH(node.right, q, hits);
}
```
