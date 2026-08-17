# Extra exercises — Week 11 (Delaunay)

Lecture: [[Computational Geometry/Lecture 11 Delaunay Triangulation]]  
Demos: [15-incircle](../code/15-incircle.html) · [16-delaunay](../code/16-delaunay.html)

---

## Written

1. Define Delaunay via empty circumcircle.
2. Duality: Delaunay edge ↔ ? Delaunay triangle ↔ ? Hull sites ↔ ?
3. Illegal edge: incircle of one triangle contains the opposite vertex.
4. Angle test: ad is illegal iff the two opposite angles sum to more than 180°. Draw it.
5. A triangulation is Delaunay iff every interior edge is legal. What does a flip do to the min angle?
6. Incremental insertion: which triangles are deleted? What is the cavity?
7. Constrained Delaunay: what extra edges are forced? Why fonts / floor plans need it.
8. Delaunay maximizes the min angle. It is **not** always the minimum-weight triangulation. Do not claim that.
9. Super-triangle in Bowyer–Watson: why delete triangles that still touch it at the end?
10. Cocircular four points: what does the course policy say (either triangulation of the quad is Delaunay)?

## Coding

11. `incircle(a,b,c,d)` with ABC CCW. Tests: D inside, outside, cocircular square.
12. Bowyer–Watson on n ≥ 3. Hull edges must appear. Oracle: every triangle’s circumcircle empty of other sites (epsilon).
13. Visualizer: click to insert; do not rebuild from scratch if you claim incremental — or rebuild and say so.

## Snippet — incircle and Bowyer–Watson call

```js
function incircle(a, b, c, d) {
  const adx = a.x - d.x, ady = a.y - d.y;
  const bdx = b.x - d.x, bdy = b.y - d.y;
  const cdx = c.x - d.x, cdy = c.y - d.y;
  const det =
    (adx * adx + ady * ady) * (bdx * cdy - cdx * bdy) -
    (bdx * bdx + bdy * bdy) * (adx * cdy - cdx * ady) +
    (cdx * cdx + cdy * cdy) * (adx * bdy - bdx * ady);
  return orient(a, b, c) < 0 ? -det : det;
}

// Full incremental insert: CG.bowyerWatson(points) in kernel.js
```
