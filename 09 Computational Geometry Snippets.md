# Computational Geometry snippets

Runnable Canvas demos and a shared 2D kernel for the IGWT course.

**Open:** [Computational Geometry/code/index.html](Computational%20Geometry/code/index.html)

**Copy from:** [Computational Geometry/code/kernel.js](Computational%20Geometry/code/kernel.js)

**Extra problem sets:** [Computational Geometry/exercises/00 Index.md](Computational%20Geometry/exercises/00%20Index.md)

Language is **JavaScript + HTML Canvas**. Do not require Three.js, WebGL, CGAL, or Qhull for weeks 1–12. Three.js `Raycaster` may be an oracle in Week 13, not the student algorithm.

If `file://` is blocked, from `Computational Geometry/code/`:

```
npx serve
python -m http.server
```

## Demos

| # | File | Week | What it shows |
| ---: | --- | ---: | --- |
| 1 | [01-orient.html](Computational%20Geometry/code/01-orient.html) | 1 | `cross` / `orient` / signed area |
| 2 | [02-on-segment.html](Computational%20Geometry/code/02-on-segment.html) | 2 | collinear ≠ on segment |
| 3 | [03-segments.html](Computational%20Geometry/code/03-segments.html) | 2 | proper / touch / overlap / none |
| 4 | [04-point-in-polygon.html](Computational%20Geometry/code/04-point-in-polygon.html) | 2 | even–odd + boundary |
| 5 | [05-aabb.html](Computational%20Geometry/code/05-aabb.html) | 2 | box overlap is not intersection |
| 6 | [06-shoelace.html](Computational%20Geometry/code/06-shoelace.html) | 3 | area + convex / concave / bowtie |
| 7 | [07-jarvis.html](Computational%20Geometry/code/07-jarvis.html) | 4 | gift wrap, Θ(n h) |
| 8 | [08-andrew.html](Computational%20Geometry/code/08-andrew.html) | 5 | monotone chain |
| 9 | [09-naive-intersect.html](Computational%20Geometry/code/09-naive-intersect.html) | 6 | all pairs |
| 10 | [10-sweep.html](Computational%20Geometry/code/10-sweep.html) | 6 | teaching sweep vs naive |
| 11 | [11-ear-clip.html](Computational%20Geometry/code/11-ear-clip.html) | 7 | n − 2 triangles |
| 12 | [12-dcel-walk.html](Computational%20Geometry/code/12-dcel-walk.html) | 8 | half-edge `next` |
| 13 | [13-kd-range.html](Computational%20Geometry/code/13-kd-range.html) | 9 | prune vs visit |
| 14 | [14-voronoi-discrete.html](Computational%20Geometry/code/14-voronoi-discrete.html) | 10 | nearest site per pixel |
| 15 | [15-incircle.html](Computational%20Geometry/code/15-incircle.html) | 11 | illegal edge |
| 16 | [16-delaunay.html](Computational%20Geometry/code/16-delaunay.html) | 11 | Bowyer–Watson |
| 17 | [17-closest-pair.html](Computational%20Geometry/code/17-closest-pair.html) | 12 | D&C vs brute oracle |
| 18 | [18-bvh-pick.html](Computational%20Geometry/code/18-bvh-pick.html) | 13 | parent box miss |
| 19 | [19-kernel-tests.html](Computational%20Geometry/code/19-kernel-tests.html) | all | hidden-fixture style |
| 20 | [20-project-sandbox.html](Computational%20Geometry/code/20-project-sandbox.html) | 14–15 | freeze a degeneracy |

## Kernel (copy these; do not grow EPS until it “looks fine”)

```js
function cross(a, b, c) {
  return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

function orient(a, b, c, eps = 1e-9) {
  const v = cross(a, b, c);
  if (v > eps) return 1;
  if (v < -eps) return -1;
  return 0;
}
```

Full implementations of `onSegment`, `segmentsIntersect`, `pointInPolygon`, `andrew`, `earClip`, `incircle`, `bowyerWatson`, `closestPair`, `buildBVH` are in `kernel.js`. Exercise sheets repeat the teaching-sized versions.

Policy reminders:

- Hull: drop strictly intermediate collinear vertices.
- Range queries: closed boxes; include the boundary.
- `touch` is not `none`.
- Discrete Voronoi is not Fortune.
- Ear clipping is not Delaunay.
