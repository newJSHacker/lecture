# Extra exercises — Week 9 (kd-tree and location)

Lecture: [[Computational Geometry/Lecture 09 Point Location and Range Search]]  
Demo: [13-kd-range.html](../code/13-kd-range.html)

---

## Written

1. Point location: preprocess a subdivision, query a face. Why is “test every face” not the answer?
2. Slab method: query time? Space problem?
3. Kirkpatrick: one sentence. Do we implement it?
4. kd-tree: which axis at depth 0, 1, 2, 3?
5. When do we prune a node? When must we visit both children?
6. Range is closed: points on the boundary of R count. Why say this out loud?
7. Quadtree vs kd-tree: one advantage each.
8. Range tree vs kd-tree: one advantage each.
9. BVH stores what at each node? What is the leaf test?
10. Practical substitute in this course for planar point location?

## Coding

11. Build kd-tree; range query; brute-force oracle. They must match on 50 random queries.
12. Draw node boxes. A query disjoint from the parent box must not visit children (count visits).
13. Do not forget the point stored at an internal node.

## Snippet

```js
function buildKd(points, depth) {
  if (!points.length) return null;
  if (points.length === 1) return { leaf: true, p: points[0], box: aabb(points) };
  const axis = depth % 2;
  const sorted = points.slice().sort((u, v) => (axis === 0 ? u.x - v.x : u.y - v.y));
  const mid = Math.floor(sorted.length / 2);
  return {
    leaf: false,
    axis,
    p: sorted[mid],
    box: aabb(points),
    left: buildKd(sorted.slice(0, mid), depth + 1),
    right: buildKd(sorted.slice(mid + 1), depth + 1),
  };
}

function rangeQuery(node, R, out) {
  if (!node || !aabbOverlap(node.box, R)) return; // prune
  if (aabbContains(R, node.p)) out.push(node.p);
  if (node.leaf) return;
  rangeQuery(node.left, R, out);
  rangeQuery(node.right, R, out);
}
```
