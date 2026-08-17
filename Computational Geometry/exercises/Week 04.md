# Extra exercises — Week 4 (Jarvis)

Lecture: [[Computational Geometry/Week 04 Convex Hull I]]  
Demo: [07-jarvis.html](../code/07-jarvis.html)

---

## Written

1. Define extreme point two ways (hull vertex; supporting line).
2. Jarvis time in n and h. Fill: circle of n points; triangle plus n−3 interior points; random Gaussian (expected h).
3. Why start at lowest-then-leftmost? What fails if you start at a random point?
4. Course policy: collinear points on a hull edge. Keep middles or drop? What does the `o == 0` branch do?
5. Parabola reduction: map xi → (xi, xi²). Why does the hull order give sorted x?
6. Is Jarvis optimal for points in convex position? Why?
7. Invariant after k wraps: state it in one sentence.
8. Space besides the input?
9. Duplicate points: what infinite-loop failure looks like.
10. Incremental hull idea (no code): inside vs outside, two tangents.

## Coding

11. Jarvis with step keys N / E / Space (lecture live-coding).
12. Buttons: cloud, circle, triangle+cloud. Table n ∈ {100, 1000} and milliseconds. Do not invent timings you did not measure.
13. Remove duplicates **before** wrapping. Test: 50 copies of 5 hull points.

## Snippet — Jarvis

```js
function jarvis(S) {
  const P = uniquePoints(S);
  if (P.length <= 2) return P.slice();
  const start = lowestThenLeftmost(P);
  const hull = [];
  let p = start;
  do {
    hull.push(p);
    let q = P[0] === p ? P[1] : P[0];
    for (const r of P) {
      if (r === p) continue;
      const o = orient(p, q, r);
      if (o < 0) q = r;                              // r is righter
      else if (o === 0 && dist2(p, r) > dist2(p, q)) q = r; // farthest
    }
    p = q;
  } while (p !== start);
  return hull;
}
```
