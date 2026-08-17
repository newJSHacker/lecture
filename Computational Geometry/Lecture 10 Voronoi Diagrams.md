# Lecture 10 — Voronoi diagrams

**Week 10 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** V(si)={p: dist(p,si)≤dist(p,sj) ∀j}; vertex = empty-circumcircle center; discrete Voronoi; no Fortune code  
**Success check:** dragging a site recolors the canvas; query point shows nearest site; they can state empty-circle and unbounded ⇔ hull

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/10-sweep.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: proximity: who is closest to this site? | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
cell V(si)     edge ⊂ perpendicular bisector
vertex = circumcenter of 3 sites
empty circle: no site in the interior

unbounded cell  ⇔  site on CH(S)
complexity O(n) vertices/edges in 2D

Fortune (intuition only):
  beach = parabolic arcs
  site event: new arc     circle event: vertex born
DO NOT IMPLEMENT

discrete: argmin dist per pixel     tie: smaller index
dual teaser: Delaunay next week
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Nearest neighbor is a cell membership test. We will not spend the week debugging Fortune — that is why we forbid it. Drawing Delaunay and calling it Voronoi is the other fail: they are dual; edges are not the same.

**Ask:** A cell is unbounded iff the site is …? Wait. Want: on the convex hull.

**Board:** parked strip. Then three sites, three perpendicular bisectors, one Voronoi vertex.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Voronoi diagrams*.

**Do not:** Drawing the Delaunay triangulation and calling it Voronoi (they are dual; edges are not the same).

### Minutes 10–12 — Frame

**Say:** General position: no four cocircular, no three collinear — then say what fails. Every pair of sites does not produce a Voronoi edge, only neighbors. Jump-flood / cone shaders: name for IGWT, not required. Do not invent fps.

**Ask:** Site event vs circle event?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Empty-circle is the homework proof and the bridge to Delaunay.

**Board:** three sites, three bisectors, one vertex, empty circle. Hull sites with unbounded rays. Beach line: two parabolas, a site punching an arc. Dual teaser.

**Say:** Applications: territory, coverage, stipple, Thiessen, city blocks.

**Ask:** A Voronoi vertex is the _____ of three sites.

**They do:** Proof: circumcircle of abc at a Voronoi vertex contains no other site. Fortune two events, three sentences each. No Fortune code.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Click sites, color pixels (or coarse grid), overlay dots, draggable q to nearest site. Optional messy all-bisectors to motivate a better algorithm. Do not start Fortune. Demo 14-voronoi-discrete.html. Plant == on distances.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** nearestSite(p, sites) with a tie-break. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: discrete Voronoi, add/remove/drag, query highlight, screenshot of a 3-color meeting, README why a vertex is a circumcenter. Quiz: V(si), circumcenter, empty circle, events, unbounded.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three sites by hand | Empty circle. |
| 15–35 | Beach-line cartoons only | Stop. No heap of arcs. |
| 35–50 | Discrete color + query | Dragging updates live. |
| 50–60 | Dual sentence | Connect sites whose cells share an edge. |

Point them at `Computational Geometry/code/10-sweep.html` as the after-class check, not as the lecture.

---

## Lab

1. Discrete Voronoi on a canvas.
2. n sites, add/remove/drag.
3. Query point with nearest-site highlight.
4. Screenshot: 8 sites, query in a cell, and a place where three colors meet (approximate vertex).
5. Written in README: why a vertex is a circumcenter, in your own words.

---

## Homework

1. **Proof (required).** Let v be a Voronoi vertex defined by sites a, b, c. Show that the circumcircle of abc contains no other site in its interior. (Use the definition of V(·) and dist(v,a) = dist(v,b) = dist(v,c).)
2. Written: which cells are unbounded, and why.
3. Written: Fortune’s two event types, three sentences each.
4. No Fortune code.

---

## Quiz next meeting (they hear this now)

1. Define V(si). (2 pts)
2. A Voronoi vertex is the _____ of three sites. (2 pts)
3. Empty-circle property, one sentence. (2 pts)
4. Site event vs circle event. (2 pts)
5. A cell is unbounded iff the site is _____. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Definition (20 min).** Let S = {s1, …, sn} be sites in the plane (assume general position: no four cocircular, no three collinear — then mention what fails).
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
The circle through those three site

**2. Fortune’s algorithm — intuition only (20 min).** A sweep line from top to bottom (standard picture).
Behind the sweep line the diagram is not yet safe: a site just below the line could still steal territory.
The **beach line** is the boundary between the “decided” region and the undecided region. It is a sequence of parabolic arcs. Each arc is the set of points equidistant from a site and the sweep line.
### Events
| Event | Meaning | Effect |
| --- | --- | --- |
| Site event | sweep line hits a new site | a new arc appears on the beach line |
| Circle event | sweep line hits the bottom of a circle through three sites that make consecutive arcs | an arc disappears; a Voronoi vertex is born |
Data structures (name only): a balanced tree for the beach line, a priority queue for events. Time O(n log n).
**Do not implement this in the lab.**

**3. Applications (15 min).** | Application | How |
| --- | --- |
| Nearest neighbor | the cell that contains q; or walk / point-locate in VD |
| Territory / service areas | cell = region assigned to a facility |
| Robot coverage / paths | Voronoi edges are locally farthest from sites (obstacles) |
| Stippling / mosaics | sites = dots; cells = tiles (project) |
| Meteorology / GIS | Thiessen polygons (same object) |
| Procedural cities | cells → blocks, dual Delaunay → roads (project) |
Live demo idea: move q, color the nearest site. That *is* the Voronoi membership test, even if we compute it by brute force this week.
---

**4. Discrete Voronoi (10 min).** For each pixel p, color p by argmin_i dist(p, si).
This is O(pixels × n). Fine for a 600×400 canvas and n ≤ 40. Jump-flooding and cone-shader methods exist on the GPU; mention for IGWT students, do not require.
The discrete picture is a raster approximation. Vertices will look like pixels where three colors meet.
Next week we get the exact combinatorial diagram via Delaunay.
---

---

## Common mistakes

1. Drawing the Delaunay triangulation and calling it Voronoi (they are dual; edges are not the same).
2. Thinking every pair of sites produces a Voronoi edge (only neighbors do).
3. Implementing Fortune badly and spending the week in debugging. That is why we forbid it.
4. Using `==` on distances; use `≤` and a consistent tie-break (smaller site index).

## If we run long, cut

Any Fortune attempt. Keep definition + discrete + empty circle.

## If we run short, add

Overlay a library Voronoi as a teaser if you already have one.
