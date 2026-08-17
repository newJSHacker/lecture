# Extra exercises — Week 6 (sweep)

Lecture: [[Computational Geometry/Week 06 Sweep Line Intersection]]  
Demos: [09-naive](../code/09-naive-intersect.html) · [10-sweep](../code/10-sweep.html)

---

## Written

1. Naive time? When is it optimal?
2. Sweep time in n and I for the BST version. Lab version (array status)?
3. Name the three event types and one action each.
4. Why test only status neighbors? Draw two segments that do **not** become neighbors and do not intersect.
5. After INTER, what happens in T?
6. Why is status the y-order **along L**, not the y of endpoints?
7. If I = n²/4, is sweep asymptotically better than naive?
8. Vertical segments: how do you order events (x then y)?
9. `touch` vs `none`: which later weeks break if you drop T-junctions?
10. Why can a sorted list replace a BST for n ≤ 200?

## Coding

11. Naive reporter + teaching sweep. Same hits (as a set of unordered pairs) on 20 random segments.
12. Fixture: two crossings, one T-junction, one AABB-miss pair.
13. Do **not** test every pair and then draw a vertical line. That is not a sweep.

## Snippet — naive reporter

```js
function naiveSegmentIntersections(segments) {
  const hits = [];
  for (let i = 0; i < segments.length; i++) {
    for (let j = i + 1; j < segments.length; j++) {
      const r = segmentsIntersect(segments[i].a, segments[i].b, segments[j].a, segments[j].b);
      if (r.type !== "none") hits.push({ i, j, type: r.type, point: r.point });
    }
  }
  return hits;
}
```

Teaching sweep: copy `CG.teachingSweep` from [kernel.js](../code/kernel.js). Status is an array sorted by y-at-event-x.
