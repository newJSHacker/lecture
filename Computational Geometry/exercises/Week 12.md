# Extra exercises — Week 12 (closest pair + survey)

Lecture: [[Computational Geometry/Week 12 Closest Pair and Survey]]  
Demo: [17-closest-pair.html](../code/17-closest-pair.html)

---

## Written

1. Naive closest pair time.
2. Recurrence T(n) = 2 T(n/2) + O(n). Solution?
3. Why only a constant number of strip points in a δ × 2δ box? Packing picture.
4. Why presort, not sort inside every recursive call?
5. How do you build the strip from Py in linear time?
6. Duplicates: distance 0. Course vs project policy.
7. Arrangement: one picture, one graphics/CAD use.
8. Minkowski sum: character vs wall in configuration space. One picture.
9. Visibility graph: vertices of obstacles + edges that do not stab interiors. Pathfinding prototype vs navmesh in production.
10. Match each survey topic to one sentence you would say in a defense.

## Coding

11. `closestPair` vs `bruteClosestPair` on n = 200 random. Distances must match.
12. Draw the median line and the 2δ strip after the recursion (even if you only highlight the winner).
13. Worst-case-looking input: many points on a vertical line just inside the strip.

## Snippet

```js
function closestPairRec(Px, Py) {
  const n = Px.length;
  if (n <= 3) return bruteClosestPair(Px);
  const mid = Math.floor(n / 2);
  const midX = Px[mid].x;
  const Lset = new Set(Px.slice(0, mid));
  const left = closestPairRec(Px.slice(0, mid), Py.filter((p) => Lset.has(p)));
  const right = closestPairRec(Px.slice(mid), Py.filter((p) => !Lset.has(p)));
  let best = left.dist < right.dist ? left : right;
  const strip = Py.filter((p) => Math.abs(p.x - midX) < best.dist);
  for (let i = 0; i < strip.length; i++) {
    for (let j = i + 1; j < strip.length && j <= i + 7; j++) {
      if (strip[j].y - strip[i].y >= best.dist) break;
      const d = dist(strip[i], strip[j]);
      if (d < best.dist) best = { dist: d, a: strip[i], b: strip[j] };
    }
  }
  return best;
}
```
