# Extra exercises — Week 7 (ear clipping)

Lecture: [[Computational Geometry/Lecture 07 Polygon Triangulation]]  
Demo: [11-ear-clip.html](../code/11-ear-clip.html)

---

## Written

1. Simple n-gon: how many triangles? How many diagonals?
2. Define an ear tip in three bullets (convex; diagonal inside; no other vertex in the triangle).
3. Meisters: at least how many ears for n ≥ 4?
4. Complexity of the naive clip? When is that fine (UI blob vs GIS lake)?
5. Why is a reflex vertex never an ear tip?
6. Induction sketch: a diagonal splits n into n1, n2 with n1 + n2 = n + 2. Finish the triangle count.
7. y-monotone polygon: why is triangulation easier after vertices are sorted?
8. Constrained triangulation vs Delaunay: one sentence each. Do not claim ear clipping is Delaunay.
9. What should `earClip` do on a bowtie?
10. Midterm prep: list the 11 topics from the lecture note. No Voronoi, no kd-tree, no DCEL.

## Coding

11. `isEar` + `earClip`. Assert `|T| = n − 2` on convex and C-shape.
12. Step mode: clip one ear per keypress. Color the candidate triangle.
13. Point-in-triangle, not point-in-polygon, for the interior-vertex test.

## Snippet

```js
function isEar(P, i, ccw) {
  const n = P.length;
  const a = P[(i + n - 1) % n], b = P[i], c = P[(i + 1) % n];
  const o = orient(a, b, c);
  if (o === 0) return false;
  if (ccw ? o < 0 : o > 0) return false; // reflex
  for (let j = 0; j < n; j++) {
    if (j === (i + n - 1) % n || j === i || j === (i + 1) % n) continue;
    if (pointInTriangle(P[j], a, b, c) !== "OUTSIDE") return false;
  }
  return true;
}

function earClip(P) {
  const V = P.map((p) => ({ x: p.x, y: p.y }));
  const ccw = shoelace(V) >= 0;
  const T = [];
  while (V.length > 3) {
    let found = false;
    for (let i = 0; i < V.length; i++) {
      if (isEar(V, i, ccw)) {
        const n = V.length;
        T.push([V[(i + n - 1) % n], V[i], V[(i + 1) % n]]);
        V.splice(i, 1);
        found = true;
        break;
      }
    }
    if (!found) break; // not simple
  }
  if (V.length === 3) T.push([V[0], V[1], V[2]]);
  return T;
}
```
