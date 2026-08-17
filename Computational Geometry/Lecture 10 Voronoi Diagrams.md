# Lecture 10 — Voronoi diagrams

**Time:** 75 min lecture + 60 min live coding  
**What we implement:** discrete (pixel) Voronoi + nearest-site query  
**What we do not implement:** Fortune’s algorithm  
**Board first:** three sites, three perpendicular bisectors, one Voronoi vertex

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 9 |
| 10–30 | Definition, cells, vertices, empty circle |
| 30–50 | Fortune at intuition level |
| 50–65 | Applications |
| 65–75 | Discrete Voronoi and the dual teaser |

---

## Learning goals

1. Define the Voronoi cell of a site.
2. State the empty-circle property of a Voronoi vertex.
3. Describe Fortune’s beach line and the two event types.
4. Explain a discrete Voronoi (for each pixel, nearest site).
5. Name three applications: nearest neighbor, territory, coverage.

---

## 1. Definition (20 min)

Let S = {s1, …, sn} be sites in the plane (assume general position: no four cocircular, no three collinear — then mention what fails).

The **Voronoi cell** of si is

```
V(si) = { p | dist(p, si) ≤ dist(p, sj) for all j }
```

The **Voronoi diagram** VD(S) is the set of points that have at least two nearest sites (the boundaries) together with the cells.

### Geometry of an edge

The set of points equidistant from si and sj is the **perpendicular bisector** of si sj.  
A Voronoi edge is a (possibly unbounded) piece of that bisector: the points that are closer to {si, sj} than to any other site.

### Geometry of a vertex

A Voronoi vertex is equidistant from **three** sites (usually). It is the **circumcenter** of those three sites.

**Empty-circle property.**  
The circle through those three sites contains **no site in its interior**. If it did, that site would be closer to the center, and the vertex would not be Voronoi.

This sentence is the homework proof and the bridge to Delaunay next week.

### Unbounded cells

A cell is unbounded iff its site lies on the convex hull of S.  
Draw a hull and show rays going to infinity.

### Complexity

For n sites in 2D: O(n) vertices and edges. The diagram is a linear-size planar graph. That is why it is usable.

---

## 2. Fortune’s algorithm — intuition only (20 min)

A sweep line from top to bottom (standard picture).

Behind the sweep line the diagram is not yet safe: a site just below the line could still steal territory.

The **beach line** is the boundary between the “decided” region and the undecided region. It is a sequence of parabolic arcs. Each arc is the set of points equidistant from a site and the sweep line.

### Events

| Event | Meaning | Effect |
| --- | --- | --- |
| Site event | sweep line hits a new site | a new arc appears on the beach line |
| Circle event | sweep line hits the bottom of a circle through three sites that make consecutive arcs | an arc disappears; a Voronoi vertex is born |

Data structures (name only): a balanced tree for the beach line, a priority queue for events. Time O(n log n).

**Do not implement this in the lab.** Draw the beach line three times: before a site event, after a site event, at a circle event.

If students ask for code, point to a reference implementation and to Week 11: we will build the dual instead.

---

## 3. Applications (15 min)

| Application | How |
| --- | --- |
| Nearest neighbor | the cell that contains q; or walk / point-locate in VD |
| Territory / service areas | cell = region assigned to a facility |
| Robot coverage / paths | Voronoi edges are locally farthest from sites (obstacles) |
| Stippling / mosaics | sites = dots; cells = tiles (project) |
| Meteorology / GIS | Thiessen polygons (same object) |
| Procedural cities | cells → blocks, dual Delaunay → roads (project) |

Live demo idea: move q, color the nearest site. That *is* the Voronoi membership test, even if we compute it by brute force this week.

---

## 4. Discrete Voronoi (10 min)

For each pixel p, color p by argmin_i dist(p, si).

This is O(pixels × n). Fine for a 600×400 canvas and n ≤ 40. Jump-flooding and cone-shader methods exist on the GPU; mention for IGWT students, do not require.

The discrete picture is a raster approximation. Vertices will look like pixels where three colors meet.

Next week we get the exact combinatorial diagram via Delaunay.

---

## Live coding (60 min)

1. Click to add sites.
2. For each pixel (or a coarse grid), color by nearest site (semi-transparent).
3. Overlay sites as dots.
4. A draggable query point q; draw the segment to its nearest site; print the site id.
5. Optional: draw perpendicular bisectors of all pairs (messy) to motivate “we need a better algorithm.”

Do **not** start Fortune.

If you have a small Delaunay library already, you may overlay the exact Voronoi as a teaser and say “dual, next week.”

---

## Lab

1. Discrete Voronoi on a canvas.
2. n sites, add/remove/drag.
3. Query point with nearest-site highlight.
4. Screenshot: 8 sites, query in a cell, and a place where three colors meet (approximate vertex).
5. Written in README: why a vertex is a circumcenter, in your own words.

Done when dragging a site updates the coloring live.

---

## Homework

1. **Proof (required).** Let v be a Voronoi vertex defined by sites a, b, c. Show that the circumcircle of abc contains no other site in its interior. (Use the definition of V(·) and dist(v,a) = dist(v,b) = dist(v,c).)
2. Written: which cells are unbounded, and why.
3. Written: Fortune’s two event types, three sentences each.
4. No Fortune code.

---

## Quiz (10 min)

1. Define V(si). (2 pts)
2. A Voronoi vertex is the _____ of three sites. (2 pts)
3. Empty-circle property, one sentence. (2 pts)
4. Site event vs circle event. (2 pts)
5. A cell is unbounded iff the site is _____. (2 pts)

---

## Common mistakes

- Drawing the Delaunay triangulation and calling it Voronoi (they are dual; edges are not the same).
- Thinking every pair of sites produces a Voronoi edge (only neighbors do).
- Implementing Fortune badly and spending the week in debugging. That is why we forbid it.
- Using `==` on distances; use `≤` and a consistent tie-break (smaller site index).

---

## Board drawings

1. Three sites, three bisectors, one vertex, empty circle.
2. Hull sites with unbounded rays.
3. Beach line: sweep line, two parabolas, a new site punching an arc.
4. Dual teaser: connect sites whose cells share an edge — that is next week.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 10]] · Demo: [14-voronoi-discrete.html](code/14-voronoi-discrete.html)

1. Empty-circle property in one sentence.
2. Unbounded cell iff the site is on the hull. Check by eye in the demo.
3. Fortune event types (name only). We still do not implement Fortune.
4. Nearest-site query vs brute `argmin dist`.

```js
function nearestSite(p, sites) {
  let best = sites[0], bestD = dist2(p, sites[0]);
  for (let i = 1; i < sites.length; i++) {
    const d = dist2(p, sites[i]);
    if (d < bestD) { bestD = d; best = sites[i]; }
  }
  return best;
}
```
