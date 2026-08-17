# Extra exercises — Week 3 (triangles)

Lecture: [[Computer Graphics/Week 03 Lines and Triangles]] · Demos: [04](../code/04-barycentric.html) [05](../code/05-quad.html)

## Written

1. Barycentric of a vertex; of the centroid.
2. Why pixel **centers** `(x+0.5, y+0.5)`?
3. Degenerate triangle: what does the code do?
4. Relate signed area / `orient` to α.
5. Why a bounding box loop is not enough.

## Coding

6. `barycentric` tests: three vertices, centroid, outside, on edge, collinear.
7. Quad as two triangles; shared edge must not crash.

```js
function barycentric(p, a, b, c) {
  const area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
  if (Math.abs(area) < 1e-8) return null;
  const alpha = ((b.x - p.x) * (c.y - p.y) - (b.y - p.y) * (c.x - p.x)) / area;
  const beta  = ((c.x - p.x) * (a.y - p.y) - (c.y - p.y) * (a.x - p.x)) / area;
  return { a: alpha, b: beta, g: 1 - alpha - beta };
}
```
