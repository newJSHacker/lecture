# Extra exercises — Week 5 (Graham / Andrew)

Lecture: [[Computational Geometry/Week 05 Convex Hull II]]  
Demo: [08-andrew.html](../code/08-andrew.html)

---

## Written

1. Graham: what is the sort key if you are forbidden to call `atan2`?
2. Why is the scan O(n) after sorting? (each point pushed/popped at most once)
3. Andrew: write the lower-hull while-condition. What does `<= 0` do under the drop-middle policy?
4. Why sort by (x, y) and not by polar angle in Andrew?
5. Duplicates: what happens if you skip unique-ification?
6. Upper hull is built on `reverse(P)`. Why pop the last of lower and last of upper before concat?
7. 3D hull: name one method and one reason it is harder (volume predicate / conflicts).
8. Graphics: AABB vs OBB vs convex hull as a collider. One sentence each.
9. Compare Jarvis and Andrew on a circle of n points (Θ).
10. Give an input where Graham’s polar sort is fragile and Andrew is not.

## Coding

11. Implement Andrew. Oracle: Jarvis on the same set; hull vertex sets must match (order may rotate).
12. Collinear-bottom input: five points on y = 0 plus one above. Hull size 3.
13. Time n = 2000 random vs n = 2000 circle. Report measured ms.

## Snippet — Andrew

```js
function andrew(S) {
  const P = uniquePoints(S).sort((u, v) => u.x - v.x || u.y - v.y);
  if (P.length <= 2) return P.slice();

  function build(seq) {
    const h = [];
    for (const p of seq) {
      while (h.length >= 2 && orient(h[h.length - 2], h[h.length - 1], p) <= 0) h.pop();
      h.push(p);
    }
    return h;
  }

  const lower = build(P);
  const upper = build(P.slice().reverse());
  lower.pop();
  upper.pop();
  return lower.concat(upper);
}
```
