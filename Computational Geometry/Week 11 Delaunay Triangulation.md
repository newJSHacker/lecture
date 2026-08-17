# Week 11 — Delaunay triangulation

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** incremental insertion + legalize / edge flip  
**Board first:** two adjacent triangles, one illegal edge, the flip

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 10 |
| 10–25 | Dual of Voronoi; empty circumcircle |
| 25–50 | Legal / illegal edges and flips |
| 50–65 | Incremental insertion (Bowyer–Watson teaching level) |
| 65–75 | Constrained Delaunay; graphics uses |

---

## Learning goals

1. Define the Delaunay triangulation via the empty circumcircle.
2. State the duality with the Voronoi diagram.
3. Test an edge for legality and flip it.
4. Insert a point and restore the Delaunay property.
5. Know what a constrained Delaunay triangulation is for.

---

## 1. Definition and dual (15 min)

A triangulation T of a point set S (plus the hull edges) is **Delaunay** if every triangle’s circumcircle contains **no site of S in its interior**.

**Duality.**  
Connect two sites by a Delaunay edge iff their Voronoi cells share an edge.  
A Delaunay triangle corresponds to a Voronoi vertex (the circumcenter).  
Unbounded Voronoi cells correspond to hull sites; hull edges are Delaunay.

So: Week 10’s empty circle at a Voronoi vertex **is** the empty circumcircle of a Delaunay triangle.

**Why we care.** Among all triangulations of S, the Delaunay triangulation maximizes the minimum angle (no skinnier triangle can be improved by a flip). That is the right default mesh for terrain and interpolation. It is **not** always the minimum-weight (shortest total edge length) triangulation. Do not claim that.

---

## 2. Legal edges and flips (25 min)

Consider two triangles abd and acd that share edge ad.  
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

The angle test is the one to draw: if the two angles opposite ad sum to more than 180°, flip.

**Flip.**  
Replace diagonal ad by the other diagonal bc. The two triangles become abc and bdc (relabel to match your figure).

**Theorem (teaching).**  
A triangulation is Delaunay iff every interior edge is legal.  
Repeatedly flipping illegal edges terminates at the Delaunay triangulation (each flip increases the min angle; there are finitely many triangulations).

```
legalize(edge ad):
    if ad is a hull edge: return
    let abc, adc be the two triangles
    if incircle(a, b, c, d) > 0:   // d inside abc, or the symmetric test
        flip ad → bc
        legalize(ab); legalize(ac)  // new edges may be illegal
        // (the exact pair is the edges of the new triangles that are not the flip)
```

---

## 3. Incremental insertion (15 min)

**Bowyer–Watson, teaching version.**

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
Delete every triangle whose circumcircle contains p. The hole is a star-shaped polygon. Connect p to every boundary vertex. That is equivalent to split-and-legalize.

Complexity: expected O(n log n) with a good location structure; a naive lab is O(n²), which is fine for n ≤ 80.

---

## 4. Constrained Delaunay and graphics (10 min)

A **constrained Delaunay triangulation (CDT)** must include a given set of edges (a polygon boundary, a river, a road). Edges that are not constraints still satisfy a constrained empty-circle property.

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

## Live coding (60 min)

n ≤ 40 points, click to insert.

Draw:

- triangles
- circumcircle of the triangle under the mouse
- illegal edges in red
- a flip as an animation (old diagonal fades, new one appears)

Script:

1. Four points, one illegal diagonal, one keypress flip.
2. Insert a fifth point inside a triangle, three legalize calls.
3. Show a circumcircle that contains a point — students should shout “illegal.”

---

## Lab

1. Implement `incircle` (or the angle-sum test) and `flip`.
2. Given a triangulation (JSON), legalize until none remain. Draw before/after.
3. Incremental insert for n ≤ 80 with visible flips.
4. Super-triangle: clip it from the final display.

Done when a known 6-point example matches a reference screenshot (provide one).

---

## Homework

1. Implement edge flip + legalize.
2. Written: prove that a Voronoi vertex’s empty circle is the empty circumcircle of the dual triangle (connect Week 10 homework to today).
3. Written: why Delaunay is not necessarily minimum-weight. One counterexample sketch is enough (a very flat quad where the short diagonal is illegal — actually be careful: in a quad the Delaunay diagonal is the one that satisfies incircle, which is the one that maximizes min angle, not always the shorter). State this honestly: **shorter ≠ Delaunay**.
4. One paragraph: CDT vs ear clipping for a game navmesh.

---

## Quiz (10 min)

1. Empty circumcircle property. (2 pts)
2. Dual: a Delaunay edge corresponds to what in VD? (2 pts)
3. When is a shared edge illegal? (2 pts)
4. What does a flip replace? (2 pts)
5. Does Delaunay always minimize total edge length? Yes/no. (2 pts)

---

## Common mistakes

- Flipping a hull edge.
- Incircle with the wrong orientation (sign flips; force CCW before the test).
- Forgetting to legalize recursively after a flip.
- Leaving the super-triangle in the mesh used for area/terrain.
- Calling ear clipping “Delaunay.”

---

## Board drawings

1. Dual: VD in dashed lines, DT in solid, one circle.
2. Illegal edge and the flip, with both circumcircles.
3. Insert p, cavity, retriangulate to p.
4. Skinny ear-clip triangle vs a flipped Delaunay pair.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 11]] · Demos: [15-incircle](code/15-incircle.html), [16-delaunay](code/16-delaunay.html)

1. Duality: Delaunay edge ↔ Voronoi edge. Delaunay triangle ↔ Voronoi vertex.
2. Illegal iff incircle contains the opposite vertex. Draw both circumcircles.
3. Delaunay maximizes min angle. It is not always minimum-weight. Do not claim that.
4. After Bowyer–Watson, no site lies in any remaining circumcircle (epsilon).

```js
function incircle(a, b, c, d) {
  const adx = a.x - d.x, ady = a.y - d.y;
  const bdx = b.x - d.x, bdy = b.y - d.y;
  const cdx = c.x - d.x, cdy = c.y - d.y;
  const det =
    (adx*adx + ady*ady) * (bdx*cdy - cdx*bdy) -
    (bdx*bdx + bdy*bdy) * (adx*cdy - cdx*ady) +
    (cdx*cdx + cdy*cdy) * (adx*bdy - bdx*ady);
  return orient(a, b, c) < 0 ? -det : det;
}
```
