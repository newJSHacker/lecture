# Computational Geometry

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Students learn to turn geometric problems into algorithms they can implement, visualize, and use in graphics, interaction, and visualization.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes (teach from these):** [[Computational Geometry/00 Lectures]]

---

## Where this course sits

Teach it in **Semester 2**, after:

- [[01 subjects#3. Mathematics for Computer Graphics]]
- [[01 subjects#1. Introduction to Programming]]

It should run **alongside or just before Computer Graphics I**. Students then reuse these algorithms in WebGL, Three.js, collision, meshes, terrain, and XR.

| Prerequisite | Why it is required |
| --- | --- |
| Programming (Python or JavaScript) | Every lab is an implementation |
| Vectors, matrices, trigonometry | Orientation tests, projections, transforms |
| Basic algorithms (sorting, recursion, trees) | Hulls, sweep lines, spatial indexes |

Do **not** start this course before students can write functions, arrays, and simple recursive code.

---

## Course goal

By the end of the semester, a student can:

1. Decide whether a geometric problem is convex-hull, intersection, triangulation, proximity, or search.
2. Prove correctness of the core 2D algorithms at the level of invariants, not full research proofs.
3. Implement robust 2D primitives (orientation, intersection, inside-polygon).
4. Visualize algorithms live (points, segments, polygons, meshes).
5. Apply the algorithms to a graphics-related project (collision, terrain, mesh, pathfinding, or configurator picking).

---

## Teaching structure (every week)

Use the same five-part week as the rest of the program.

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Definitions, invariants, one proof sketch, complexity |
| Live coding | 60 min | Professor implements the algorithm on a 2D canvas |
| Lab | 2–3 hours | Students finish a starter and see the result move |
| Homework | 4–6 hours | One algorithm + 3–5 written questions |
| Quiz | 10 min | Orientation, degeneracy, complexity, one picture question |

**Implementation language:** JavaScript + HTML Canvas (fits IGWT). Python + matplotlib is acceptable if the department prefers it. Keep the geometric kernel language-agnostic.

**Never lecture from slides only.** Every algorithm must appear as moving geometry on screen.

---

## Professor preparation (before Week 1)

Prepare these once; reuse them every year.

- Lecture slides with **diagrams, not paragraphs**
- A course repository:

```
comp-geom/
  lecture/
  starter/
  solutions/
  assignments/
  visualizer/     # shared 2D canvas viewer
  tests/          # orientation, intersection, hull fixtures
```

- A shared **geometry kernel** students import:

  - `orient(a, b, c)`
  - `onSegment(p, a, b)`
  - `segmentsIntersect(a, b, c, d)`
  - `pointInPolygon(p, polygon)`
- Auto-grader tests for primitives (hidden degenerate cases)
- Coding standard: no magic numbers, name points `p`, `q`, `r`, document expected complexity
- One recorded demo per week

---

## Assessment

| Component | Weight | Notes |
| --- | --- | --- |
| Labs (12) | 25% | Must run in the visualizer |
| Homework (8) | 20% | Mix of code and short proofs |
| Quizzes (10) | 10% | Weekly, 10 minutes |
| Midterm (Week 8) | 15% | Written: invariants, complexity, degeneracy |
| Final project | 30% | Working demo + 6–8 page report |

No exam-only course. The project is the proof of mastery.

---

# 15-week lecture plan

## Week 1 — What computational geometry is

### Goal

Students see that graphics already *is* computational geometry, and they learn the course rules: predicates, degeneracy, and visualization.

### Lecture

- Problems: closest pair, convex hull, segment intersection, point in polygon
- Discrete vs continuous geometry
- Predicates vs constructions
- Degenerate cases: collinear points, overlapping segments, duplicate vertices
- Why floating point breaks geometry
- Course map for 15 weeks

### Live coding

Build the shared visualizer: click to add points, drag, reset, show coordinates.

Implement `orient(a, b, c)` and color the triangle left / right / collinear.

### Lab

Students add:

- distance
- midpoint
- display of signed area

### Homework

1. Implement orientation and write 8 unit tests, including collinear cases.
2. Explain why `cross(b-a, c-a)` is better than computing angles.

### Quiz

Given 3 points, is `c` left of `ab`?

---

## Week 2 — Geometric primitives

### Goal

A correct kernel. Everything later depends on this week.

### Lecture

- Points, vectors, segments, rays, lines, polygons
- Cross product in 2D as signed area
- Segment–segment intersection (proper and improper)
- Point-in-polygon: ray casting and winding number
- Bounding boxes as a cheap reject test

### Live coding

Implement segment intersection with pictures of:

- crossing
- T-junction
- overlapping collinear
- disjoint but bounding boxes overlap

### Lab

`pointInPolygon` on a concave polygon. Students must handle a ray that hits a vertex.

### Homework

Write a robust `segmentsIntersect` that reports `proper`, `touch`, `overlap`, or `none`.

### Common mistakes to show

- Using `== 0` on floats
- Forgetting the bounding-box reject
- Ray casting along an edge

---

## Week 3 — Convexity and polygons

### Goal

Students can say whether a polygon is convex, simple, or neither, and why that matters for graphics.

### Lecture

- Convex sets and convex combinations
- Convex vs concave vs simple vs complex polygons
- Interior angle test
- Supporting lines
- Why many algorithms assume simple polygons
- Polygon area by the shoelace formula

### Live coding

Highlight reflex vertices. Compute area. Draw the convex hull of the vertex set as a preview of Week 4.

### Lab

Classify a user-drawn polygon: convex / simple concave / self-intersecting.

### Homework

Prove that a polygon is convex iff every turn has the same orientation.

---

## Week 4 — Convex hull I (intuition and slow algorithms)

### Goal

Students understand the hull as an extreme-point problem before they memorize a famous algorithm.

### Lecture

- Definitions: hull, extreme points, supporting line
- Gift wrapping (Jarvis march)
- Incremental construction
- Lower bound: hull is at least as hard as sorting
- Output-sensitive complexity

### Live coding

Jarvis march, one step per keypress. Show the “rotating calipers” mental image.

### Lab

Implement Jarvis march. Measure time on 100 / 1,000 / 10,000 random points.

### Homework

1. Implement Jarvis.
2. Give an input where it is Θ(nh) and one where h = n.

---

## Week 5 — Convex hull II (Graham and Andrew)

### Goal

Students implement the algorithm they will actually use.

### Lecture

- Graham scan
- Andrew’s monotone chain (preferred for implementation)
- Handling collinear points on the hull
- 3D convex hull (gift wrapping / incremental) as a preview only

### Live coding

Andrew’s algorithm: lower hull, then upper hull, with the stack drawn on screen.

### Lab

Implement Andrew’s monotone chain. Compare time with Jarvis from Week 4.

### Homework

Implement Graham or Andrew. Reject duplicate points. Document how collinear points are treated.

### Graphics connection

Axis-aligned and oriented bounding boxes, camera-frustum culling, 2D collision broad phase.

---

## Week 6 — Line segment intersection (sweep line)

### Goal

Students learn the sweep-line pattern, not only the intersection formula.

### Lecture

- Naive O(n²) test
- Plane sweep idea
- Event queue and status structure
- Bentley–Ottmann at a teaching level
- Degeneracy: many segments meet at one point

### Live coding

Sweep a vertical line across segments. Pause at every event. Highlight the active set.

Do **not** require a full red-black tree in the first lab. A sorted list is enough for n ≤ 200.

### Lab

Report all intersections of a set of segments. Visualize intersection points.

### Homework

Explain why the status must be ordered along the sweep line, not by y-coordinate of endpoints.

### Graphics connection

Map overlays, UI hit-testing, CAD edge intersections, clipping.

---

## Week 7 — Polygon triangulation

### Goal

Students can triangulate a simple polygon and see why GPUs want triangles.

### Lecture

- Every simple polygon with n vertices has n − 2 triangles
- Ear clipping
- Why monotone polygons are easier
- Split into monotone pieces (high-level)
- Constrained triangulation vs mesh triangulation

### Live coding

Ear clipping: highlight the current ear, clip it, repeat.

### Lab

Triangulate a simple concave polygon and draw the diagonals.

### Homework

Implement ear clipping. Fail cleanly on a self-intersecting polygon.

### Midterm next week — give a 1-page topic list today.

---

## Week 8 — Midterm + DCEL

### Midterm (first 60–75 min)

Written, no laptop.

Topics:

- Orientation and degeneracy
- Convex vs simple polygons
- Jarvis vs Andrew: complexity and when to use each
- Sweep-line events
- Ear clipping
- One short proof (same-orientation ⇒ convex)

### Lecture (remaining time)

- Doubly-connected edge list (DCEL)
- Vertices, half-edges, faces
- Why meshes in graphics are the same idea (half-edge / winged-edge)

### Lab

Walk a DCEL: given a half-edge, list the face boundary.

### Homework

None this week except midterm review notes.

---

## Week 9 — Point location and range search

### Goal

Students can answer “which face contains this point?” and “which points are in this rectangle?”

### Lecture

- Slab method
- Kirkpatrick’s hierarchy (idea only)
- kd-trees
- Range trees (idea only)
- Quadtrees
- Bounding volume hierarchies (BVH) as the graphics version

### Live coding

Build a kd-tree on a point set. Query a rectangle. Show visited vs pruned nodes.

### Lab

Implement a 2D kd-tree range query. Compare with brute force on 5,000 points.

### Homework

Draw one kd-tree by hand for 8 points. Show a query that prunes a subtree.

### Graphics connection

Picking, frustum culling, collision broad phase, nearest light, tile maps.

---

## Week 10 — Voronoi diagrams

### Goal

Students understand proximity: “who is closest to this site?”

### Lecture

- Definition and empty-circle property
- Sites, vertices, unbounded rays
- Fortune’s algorithm at intuition level (beach line, site/circle events)
- Applications: nearest neighbor, territory, robot coverage

### Live coding

Do **not** implement Fortune in one lecture. Generate a Voronoi diagram from a Delaunay library or from a slow discrete approximation, then explain the exact structure.

Show a live “move the query point, color the nearest site.”

### Lab

Discrete Voronoi: for each pixel, color by nearest site. Then compare with a computed diagram.

### Homework

Prove that a Voronoi vertex is the center of an empty circle through three sites.

---

## Week 11 — Delaunay triangulation

### Goal

The mesh students will actually use in graphics and terrain.

### Lecture

- Dual of Voronoi
- Empty circumcircle
- Legal / illegal edges and edge flips
- Incremental insertion (Bowyer–Watson at teaching level)
- Constrained Delaunay (idea)
- Relation to minimum-weight triangulations (do not overclaim)

### Live coding

Insert points one by one. Flip illegal edges. Show circumcircles.

### Lab

Incremental Delaunay for a small point set (n ≤ 80) with visible flips.

### Homework

Implement edge flip. Given a triangulation, legalize it.

### Graphics connection

Terrain, remeshing, interpolation, cloth / simulation, lightmap packing.

---

## Week 12 — Closest pair, intersections, and arrangements (selected)

### Goal

One more classic algorithm, then a map of topics you will *not* fully teach.

### Lecture

- Closest pair of points (divide and conquer)
- Line arrangements: zones, complexity (survey)
- Minkowski sums (survey, for collision)
- Visibility graphs (survey, for path planning)

Pick **closest pair** as the implemented topic. Treat the others as “know the name and the use.”

### Live coding

Closest pair divide-and-conquer, with the strip drawn.

### Lab

Implement closest pair. Compare with brute force.

### Homework

Trace closest pair on a 12-point example. State the recurrence and the O(n log n) bound.

---

## Week 13 — From 2D algorithms to graphics systems

### Goal

Students connect the course to the rest of IGWT.

### Lecture

| Algorithm | Graphics / web use |
| --- | --- |
| Convex hull | Bounding volumes, silhouette, 2D collision |
| Segment intersection | Clipping, CAD, map overlay, UI |
| Triangulation | GPU meshes, ear-clip UI shapes, font outlines |
| kd-tree / BVH | Picking, culling, ray–scene tests |
| Voronoi | Terrain, stippling, procedural regions |
| Delaunay | Meshes, interpolation, remeshing |
| Point in polygon | Hit-testing, selection, GIS |
| Minkowski sum | Character vs obstacle collision |

Also cover:

- Robustness: epsilon, adaptive predicates, exact arithmetic (Shewchuk)
- 3D: convex hull, Delaunay tetrahedralization, mesh repair — what changes
- Why game engines hide this behind PhysX / cannon.js / three-mesh-bvh

### Live coding

A mini scene: click to pick a mesh triangle using a BVH; show the ray and the visited boxes.

### Lab

Project checkpoint: each team demos a vertical slice.

### Homework

Project only.

---

## Week 14 — Project studio

No new theory.

### Lecture (30 min)

- How to write the report: problem, algorithm, complexity, degeneracy, screenshots, limitations
- Defense-style questions you will ask

### Studio

Teams work. Professor does code review at the desk.

Required this week:

- Algorithm runs on a non-trivial input
- At least one degenerate case handled or documented
- README with build instructions

---

## Week 15 — Project presentations

Each team (2–3 students) has **12 minutes + 5 minutes questions**.

Deliverables:

- Live demo
- Source repository
- 6–8 page report
- 30-second screen recording for the portfolio

---

# Final project (choose one)

Every project must implement **at least one core algorithm from this course**, not only call a library. A library is allowed for support (rendering, UI), not for the main algorithm.

| Project | Core algorithms | Why it fits IGWT |
| --- | --- | --- |
| 2D map editor | Segment intersection, DCEL, point location | GIS / web maps |
| Polygon modeler | Ear clipping or Delaunay, point-in-polygon | Vector UI, fonts, CAD |
| City / terrain generator | Voronoi + Delaunay | Procedural graphics |
| 2D physics playground | Hulls, SAT collision, sweep | Games, interaction |
| Picking / configurator | BVH or kd-tree, ray–triangle | Product configurator |
| Robot / crowd path demo | Visibility graph or Voronoi roadmap | XR, simulation |
| Stipple / mosaic image | Voronoi | Creative coding |
| Mesh repair toy | Intersection + triangulation | 3D asset pipeline |

### Project rubric

| Criterion | Weight |
| --- | --- |
| Correct algorithm (tests + degenerate cases) | 30% |
| Visual explanation of the algorithm | 20% |
| Code quality and repository | 15% |
| Report (complexity, limitations, citations) | 20% |
| Presentation and live demo | 15% |

---

# Week-by-week summary

| Week | Topic | Students implement | Graphics payoff |
| ---: | --- | --- | --- |
| 1 | Predicates, visualizer | `orient` | All later labs |
| 2 | Primitives | Intersection, point-in-polygon | Picking, hit-test |
| 3 | Convexity | Polygon classifier | Mesh / UI validity |
| 4 | Hull I | Jarvis | Bounding shapes |
| 5 | Hull II | Andrew | Collision, culling |
| 6 | Sweep line | Segment intersections | Clipping, CAD |
| 7 | Triangulation | Ear clipping | GPU triangles |
| 8 | Midterm + DCEL | Face walk | Half-edge meshes |
| 9 | Search | kd-tree range query | BVH, picking |
| 10 | Voronoi | Discrete Voronoi | Terrain, regions |
| 11 | Delaunay | Incremental + flips | Meshes, terrain |
| 12 | Closest pair | Divide and conquer | Proximity queries |
| 13 | Applications | BVH picking slice | Three.js / WebGL |
| 14 | Studio | Project | Portfolio |
| 15 | Presentations | Demo + report | Graduation evidence |

---

# Recommended textbooks

Assign **one** primary book. Use the others as references.

| Book | Use |
| --- | --- |
| de Berg, Cheong, van Kreveld, Overmars — *Computational Geometry: Algorithms and Applications* | Primary theory |
| O’Rourke — *Computational Geometry in C* | Implementation intuition |
| Mount — lecture notes (UMD) | Free weekly companion |
| Ericson — *Real-Time Collision Detection* | Graphics applications |
| Shewchuk — adaptive predicates papers / notes | Robustness week |

Do not ask undergraduates to read Fortune’s paper unaided. Teach the beach-line picture, then point to the paper.

---

# What to skip in a first undergraduate course

Say this explicitly in Week 1 so the course does not balloon.

- Full Fortune implementation
- Full Kirkpatrick point location
- 3D Delaunay / tetrahedralization as a required lab
- Linear programming in fixed dimension
- Motion planning completeness proofs
- Exact CGAL-style kernels as required code

Mention them. Do not grade them.

---

# Faculty checklist for the first offering

1. Write the visualizer and `orient` / `intersect` kernel in Week −2.
2. Record one 8-minute demo for Weeks 1–7 before the semester starts.
3. Prepare 10 quiz PDFs and the midterm.
4. Publish 4 project starter repos (map, hull collision, Delaunay terrain, BVH picker).
5. Schedule Week 13 as a joint session with Computer Graphics I if both run the same semester.
6. Collect every student project into the annual IGWT exhibition.

---

# One-sentence teaching principle

Students should leave this course able to **look at a graphics bug, name the geometric predicate that failed, and write a test for it.**
