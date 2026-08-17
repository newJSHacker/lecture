# Extra exercises — Week 10 (Voronoi)

Lecture: [[Computational Geometry/Week 10 Voronoi Diagrams]]  
Demo: [14-voronoi-discrete.html](../code/14-voronoi-discrete.html)

---

## Written

1. Define V(si).
2. A Voronoi edge is a piece of which line?
3. A Voronoi vertex is equidistant from how many sites (usual case)? Which construction is it?
4. Empty-circle property: state it. This is the homework proof and the bridge to Week 11.
5. A cell is unbounded iff … ?
6. Complexity of VD(S) in 2D (vertices/edges)?
7. Fortune: beach line is made of what arcs? Two event types?
8. Why we implement discrete Voronoi, not Fortune, in the lab.
9. Three applications: nearest neighbor, territory, coverage. One sentence each.
10. Dual teaser: connecting sites whose cells share an edge gives … ?

## Coding

11. Discrete Voronoi (pixel / cell nearest site). Click to add sites. Color by site index.
12. Overlay the convex hull. Check unbounded cells ↔ hull sites by eye.
13. Nearest-site query: click a point that is not a site; highlight the owner. Oracle: brute `argmin dist`.

## Snippet — discrete Voronoi / nearest site

```js
function nearestSite(p, sites) {
  let best = sites[0], bestD = dist2(p, sites[0]);
  for (let i = 1; i < sites.length; i++) {
    const d = dist2(p, sites[i]);
    if (d < bestD) { bestD = d; best = sites[i]; }
  }
  return best;
}

// per pixel (or every `step` pixels):
const site = nearestSite({ x, y }, sites);
const idx = sites.indexOf(site);
ctx.fillStyle = palette[idx % palette.length];
ctx.fillRect(x, y, step, step);
```
