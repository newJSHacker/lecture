# Extra exercises — Week 2 (primitives)

Lecture: [[Computational Geometry/Lecture 02 Geometric Primitives]]  
Demos: [02](../code/02-on-segment.html) · [03](../code/03-segments.html) · [04](../code/04-point-in-polygon.html) · [05](../code/05-aabb.html)

---

## Written

1. A=(0,0), B=(4,0), C=(2,2), D=(2,−2). Intersection type of AB and CD? Construct the point.
2. A=(0,0), B=(4,0), C=(4,1), D=(4,−1). Type? Why is it not `proper`?
3. A=(0,0), B=(4,0), C=(2,0), D=(6,0). Type?
4. A=(0,0), B=(2,2), C=(2,0), D=(4,2). AABBs overlap. Type of intersection?
5. Why classify with orientations **before** dividing for the intersection point?
6. Write the half-open edge rule for ray casting in one paragraph.
7. Draw a concave C-shape and a query whose +x ray hits a vertex. Show the naive double-count.
8. Identical segments AB and AB. What should `segmentsIntersect` return under the course policy?
9. Zero-length segment A=A vs CD. When is the answer `touch` vs `none`?
10. Two AABBs overlap. Must the segments intersect? Yes/no and a counterexample.
11. Winding number vs even–odd: which do we require for simple polygons this semester?
12. Why is “inside” vs “boundary” a different answer for picking and for clipping?

## Coding

13. Four-way `segmentsIntersect` plus tests for the four pictures, shared endpoint, identical segments, zero-length.
14. `pointInPolygon` on: convex, C-shape, vertex query, edge query, ray-through-vertex.
15. Overlay both AABBs in the visualizer. Script the “boxes overlap, segments miss” drag live.

## Snippet — onSegment and intersection

```js
function onSegment(c, a, b, eps = 1e-9) {
  if (orient(a, b, c, eps) !== 0) return false;
  return c.x >= Math.min(a.x, b.x) - eps && c.x <= Math.max(a.x, b.x) + eps
      && c.y >= Math.min(a.y, b.y) - eps && c.y <= Math.max(a.y, b.y) + eps;
}

function segmentsIntersect(a, b, c, d, eps = 1e-9) {
  const o1 = orient(a, b, c, eps), o2 = orient(a, b, d, eps);
  const o3 = orient(c, d, a, eps), o4 = orient(c, d, b, eps);
  if (o1 && o2 && o3 && o4 && o1 !== o2 && o3 !== o4) {
    return { type: "proper", point: intersectionPoint(a, b, c, d) };
  }
  const hits = [];
  if (onSegment(c, a, b, eps)) hits.push(c);
  if (onSegment(d, a, b, eps)) hits.push(d);
  if (onSegment(a, c, d, eps)) hits.push(a);
  if (onSegment(b, c, d, eps)) hits.push(b);
  if (!hits.length) return { type: "none" };
  if (o1 === 0 && o2 === 0 && hits.length >= 2) return { type: "overlap", point: hits[0] };
  return { type: "touch", point: hits[0] };
}
```

## Snippet — even–odd PIP

```js
function pointInPolygon(q, P, eps = 1e-9) {
  const n = P.length;
  for (let i = 0; i < n; i++) {
    if (onSegment(q, P[i], P[(i + 1) % n], eps)) return "BOUNDARY";
  }
  let inside = false;
  for (let i = 0; i < n; i++) {
    const a = P[i], b = P[(i + 1) % n];
    if ((a.y > q.y) !== (b.y > q.y)) {
      const xHit = a.x + (q.y - a.y) * (b.x - a.x) / (b.y - a.y);
      if (q.x < xHit) inside = !inside;
    }
  }
  return inside ? "INSIDE" : "OUTSIDE";
}
```
