# Lecture 11 — Delaunay triangulation

**Week 11 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Delaunay: empty circumcircle; illegal edge ⇔ incircle; flip; insert+legalize (n≤80); not minimum-weight  
**Success check:** a known 6-point example matches the reference; they can flip an illegal diagonal and not flip a hull edge

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/11-ear-clip.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: the mesh they will actually use in terrain and interpolation | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
DT ⇔ every triangle circumcircle empty of sites
dual: DT edge ↔ VD edge     DT triangle ↔ VD vertex

illegal: opposite vertex in circumcircle
         (angle sum >180° opposite the shared edge)
flip ad → bc     then legalize recursively
hull edges: never flip

incircle: force CCW or the sign flips
Delaunay maximizes min angle     shorter ≠ Delaunay
CDT: keep given edges; ear-clip can sliver
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Week 10’s empty circle at a Voronoi vertex is this week’s empty circumcircle. Ear clipping can produce slivers; show the same polygon, ear vs CDT. Do not claim minimum-weight.

**Ask:** Does Delaunay always minimize total edge length? Wait. Want: no.

**Board:** parked strip. Then two adjacent triangles, one illegal edge, the flip.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Delaunay triangulation*.

**Do not:** Flipping a hull edge.

### Minutes 10–12 — Frame

**Say:** Locate triangle: n≤80 brute point-in-triangle; walk toward p is nicer. Super-triangle: clip from the display. Bowyer–Watson cavity: delete triangles whose circle contains p, star-shaped hole, connect p — equivalent to split+legalize. Naive lab O(n²) is fine.

**Ask:** When is a shared edge illegal?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A triangulation is Delaunay iff every interior edge is legal. Flips terminate (min angle increases).

**Board:** VD dashed, DT solid, one circle. Illegal edge + both circumcircles. Insert p, cavity. Skinny ear vs flipped pair.

**Say:** Graphics: terrain, remesh, cloth, lightmaps, cities.

**Ask:** A Delaunay edge corresponds to what in VD?

**They do:** Connect Week 10 proof to today. Honest paragraph: shorter ≠ Delaunay. CDT vs ear clip for a navmesh.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** n≤40 click-insert. Circumcircle under mouse. Illegal edges red. Animate a flip. Script: four points one keypress flip; fifth point three legalize calls; class shouts ‘illegal’ when a point sits in a circle. Demos 15-incircle.html, 16-delaunay.html. Plant flipping a hull edge. Plant leaving the super-triangle in the terrain mesh. Plant calling ear clipping Delaunay.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** incircle (or angle-sum) on one quad. Eight minutes. Force CCW.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: flip+legalize a JSON triangulation; incremental n≤80; clip super-triangle; match a reference screenshot. Homework: edge flip. Quiz: empty circle, dual, illegal, what flip replaces, not min-weight.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Dual on last week’s three sites | Same circle. |
| 15–40 | One illegal, one flip | Both circumcircles drawn. |
| 40–50 | Insert inside a triangle | Three new edges, legalize. |
| 50–60 | They legalize a fixture | Circulate. |

Point them at `Computational Geometry/code/11-ear-clip.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement `incircle` (or the angle-sum test) and `flip`.
2. Given a triangulation (JSON), legalize until none remain. Draw before/after.
3. Incremental insert for n ≤ 80 with visible flips.
4. Super-triangle: clip it from the final display.

---

## Homework

1. Implement edge flip + legalize.
2. Written: prove that a Voronoi vertex’s empty circle is the empty circumcircle of the dual triangle (connect Week 10 homework to today).
3. Written: why Delaunay is not necessarily minimum-weight. One counterexample sketch is enough (a very flat quad where the short diagonal is illegal — actually be careful: in a quad the Delaunay diagonal is the one that satisfies incircle, which is the one that maximizes min angle, not always the shorter). State this honestly: **shorter ≠ Delaunay**.
4. One paragraph: CDT vs ear clipping for a game navmesh.

---

## Quiz next meeting (they hear this now)

1. Empty circumcircle property. (2 pts)
2. Dual: a Delaunay edge corresponds to what in VD? (2 pts)
3. When is a shared edge illegal? (2 pts)
4. What does a flip replace? (2 pts)
5. Does Delaunay always minimize total edge length? Yes/no. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Definition and dual (15 min).** A triangulation T of a point set S (plus the hull edges) is **Delaunay** if every triangle’s circumcircle contains **no site of S in its interior**.
**Duality.**  
Connect two sites by a Delaunay edge iff their Voronoi cells share an edge.  
A Delaunay triangle corresponds to a Voronoi vertex (the circumcenter).  
Unbounded Voronoi cells correspond to hull sites; hull edges are Delaunay.
So: Week 10’s empty circle at a Voronoi vertex **is** the empty circumcircle of a Delaunay triangle.
**Why we care.** Among all triangulations of S, the Delaunay triangulation maximizes the minimum angle (no skinnier triangle can be improved by a flip). That is the right default mesh for terrain and interpolation. It is **not** always the minimum-weight (shortest total edge length) triangulation. Do not cl

**2. Legal edges and flips (25 min).** Consider two triangles abd and acd that share edge ad.  
(Or abc and adc — pick one labeling and stick to it.)
Edge ad is **illegal** if the circumcircle of one triangle contains the opposite vertex of the other.
**Incircle test (predicate).**  
For triangle abc (CCW) and point d:
```
incircle(a, b, c, d) > 0  ⇒  d is inside the circumcircle of abc
```
The exact 4×4 determinant is in de Berg / Shewchuk. For the lab, a geometric construction is acceptable if you invert a well-tested circumcenter and compare distances — but **state that it is unstable**. Prefer the determinant if you can.
```
// teaching form: compare angles
// ad is illegal iff angle at b + angle at c > 180°
// (the two angles opposite the shared edge)
```
The angle test is the one to draw: if the two angles opposite ad sum

**3. Incremental insertion (15 min).** **Bowyer–Watson, teaching version.**
Maintain a Delaunay triangulation of the points inserted so far. Start with a huge bounding triangle that contains S.
```
insert(p):
    find the triangle t that contains p          // walk or walk+barycentric
    if p is inside t:
        split t into three triangles
        legalize the three new interior edges
    if p is on an edge e:
        split the one or two triangles of e into two each
        legalize the new edges
```
**Locate t.** For n ≤ 80, test every triangle (point-in-triangle from Week 2 / 7). For a nicer demo, walk from a random triangle toward p (good in practice, worst-case linear).
**Bowyer–Watson cavity form (picture).**  
Delete every triangle whose circumcircle contains p. The hole is a star-shaped polygon. Connect p to every bo

**4. Constrained Delaunay and graphics (10 min).** A **constrained Delaunay triangulation (CDT)** must include a given set of edges (a polygon boundary, a river, a road). Edges that are not constraints still satisfy a constrained empty-circle property.
Use: triangulate a polygon *and* keep it well-shaped; game navmeshes; GIS.
| Use | Why Delaunay |
| --- | --- |
| Terrain | interpolate height; avoid slivers |
| Remeshing | better triangles before shading |
| Cloth / simulation | more stable elements |
| Lightmap packing | well-distributed vertices |
| Procedural cities | dual of Voronoi cells |
Week 7’s ear clipping can produce slivers. Show one picture: same polygon, ear-clip vs CDT.
---

---

## Common mistakes

1. Flipping a hull edge.
2. Incircle with the wrong orientation (sign flips; force CCW before the test).
3. Forgetting to legalize recursively after a flip.
4. Leaving the super-triangle in the mesh used for area/terrain.
5. Calling ear clipping “Delaunay.”

## If we run long, cut

Full Bowyer–Watson robustness. Keep incircle + flip + insert.

## If we run short, add

Show ear-clip slivers vs DT on one polygon.
