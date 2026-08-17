# Extra exercises — Week 13 (graphics applications)

Lecture: [[Computational Geometry/Lecture 13 Graphics Applications]]  
Demo: [18-bvh-pick.html](../code/18-bvh-pick.html)

---

## Written

1. Fill five rows of the payoff table from memory (algorithm → graphics use → week).
2. Product configurator pipeline: click → ? → ? → barycentric → part id.
3. Why is EPS a policy, not a proof? Give an inconsistent-orientation sketch.
4. Shewchuk adaptive predicates: start float, recompute only if the error bound is bad. How is that different from growing EPS?
5. 3D analog of `orient(a,b,c)`?
6. What becomes harder in 3D: hull, Delaunay, predicates — one bullet each.
7. Name a library that hides BVH raycast. When may students use it as an **oracle**?
8. Why is Three.js `Raycaster` not the live-coding implementation?
9. Parent AABB miss: do we test children?
10. Barycentric coordinates of a hit: how do you know which texture / part?

## Coding

11. Ear-clip a polygon, `buildBVH`, pick with a query point. Highlight hit triangles.
12. Count box tests vs triangle tests. A miss far away should be cheap.
13. Optional oracle: if the department already uses Three.js, compare hit identity, not just “a mesh was hit.”

## Snippet — 2D BVH pick

```js
function buildBVH(triangles) {
  const items = triangles.map((t, i) => ({ t, i, box: aabb([t.a, t.b, t.c]) }));
  function rec(list, depth) {
    if (list.length === 1) return { leaf: true, item: list[0], box: list[0].box };
    const axis = depth % 2;
    list.sort((u, v) => center(u.box, axis) - center(v.box, axis));
    const mid = Math.floor(list.length / 2);
    const left = rec(list.slice(0, mid), depth + 1);
    const right = rec(list.slice(mid), depth + 1);
    return { leaf: false, left, right, box: union(left.box, right.box) };
  }
  return rec(items, 0);
}

function pickBVH(node, q, hits) {
  if (!aabbContains(node.box, q)) return; // miss parent → skip children
  if (node.leaf) {
    const t = node.item.t;
    if (pointInTriangle(q, t.a, t.b, t.c) !== "OUTSIDE") hits.push(node.item);
    return;
  }
  pickBVH(node.left, q, hits);
  pickBVH(node.right, q, hits);
}
```
