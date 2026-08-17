# Week 9 — Point location and range search

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** 2D kd-tree range query  
**Board first:** a point set, a query rectangle, brute force vs pruned boxes

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–5 | Return midterms briefly; no quiz |
| 5–20 | Point location: slabs, Kirkpatrick (idea) |
| 20–45 | kd-trees and range search |
| 45–60 | Quadtrees and range trees (survey) |
| 60–75 | BVH as the graphics version |

---

## Learning goals

1. State the point-location problem and the slab method’s cost.
2. Build a 2D kd-tree and run an axis-aligned range query.
3. Explain prune vs visit using the node’s bounding box.
4. Contrast kd-tree, quadtree, range tree, and BVH.
5. Connect range search to picking and frustum culling.

---

## 1. Point location (15 min)

**Problem.** Preprocess a planar subdivision (a DCEL). Then, for a query point q, report the face that contains q.

### Slab method

Draw a vertical line through every vertex. The plane splits into slabs. Inside a slab the upper/lower edge order is constant. Binary search the slab by x, then binary search the edges by y.

- Query: O(log n)
- Space: O(n²) in the worst case (every pair of lines contributes)

Too much space. Mention as the “obvious” structure.

### Kirkpatrick’s hierarchy (idea only)

Repeatedly remove an independent set of low-degree vertices from a triangulation and retriangulate. A query walks from the coarsest triangle down to the original face.

- Query: O(log n)
- Space: O(n)

We will not implement this. Students should remember: **point location is not “test every face.”**

### Practical substitute in this course

For a triangulation or a UI scene, a **BVH or kd-tree on bounding boxes** plus a point-in-polygon / point-in-triangle test is what they will actually ship.

---

## 2. kd-trees (25 min)

**Problem.** Preprocess n points. Query: report (or count) points inside a rectangle R = [x1, x2] × [y1, y2].

### Build

Alternate the splitting axis: depth 0 splits on x at the median, depth 1 on y, and so on.

```
build(points, depth):
    if points is empty: return null
    if |points| == 1: return leaf(points[0])
    axis = depth % 2          // 0 = x, 1 = y
    sort points by axis
    mid = median
    return node(
        axis, points[mid],
        build(left half, depth+1),
        build(right half, depth+1)
    )
```

Build time O(n log² n) with a sort at each node, or O(n log n) if we presort both axes. Space O(n).

Each node implicitly owns an axis-aligned region (the cell). Store the cell or recompute it from the path.

### Range query

```
query(node, R):
    if node is null: return
    if node.cell is disjoint from R: return          // prune
    if node.cell is inside R: report all points in subtree  // take
    else:
        if node.point is in R: report it
        query(node.left, R)
        query(node.right, R)
```

**Worst-case query** for reporting in 2D is O(√n + k), where k is the number reported. (The √n comes from a thin query that stabs many cells.) Average random queries are much faster.

### Trace

Eight points. Build the tree on the board. Query a rectangle that misses the right subtree entirely. Cross out that subtree.

---

## 3. Quadtrees and range trees (15 min)

### Quadtree

Split the **space** into four squares, not the point set by median. Good for uniformly spread points and for images / tiles. Degenerates if all points sit in one corner (need a stop rule: capacity, or minimum cell size).

Graphics: mip-like spatial bins, terrain tiles, “what is in this screen tile?”

### Range tree

A tree on x; each node stores a tree of its subtree on y.  
Query: O(log² n + k). Space: O(n log n).

Name it as the theoretically nicer range-search structure. Do not implement.

---

## 4. BVH — the graphics kd-tree (15 min)

A **bounding volume hierarchy** is a binary tree of objects (triangles, meshes), not of points.

- Each leaf: one object (or a small bucket)
- Each node: an AABB (or OBB / sphere) of its descendants
- Query (ray, frustum, click): skip a node if the query misses its box

This is Week 2’s AABB reject, recursively.

| | kd-tree | BVH |
| --- | --- | --- |
| Splits | space, median of points | objects into two groups |
| Bounds | implicit cells | stored AABB |
| Typical query | orthogonal range | ray / frustum |
| Used in | databases, GIS, this lab | Three.js, game engines, `three-mesh-bvh` |

Week 13 will pick a triangle with a BVH. Today, say the word and draw one tree of three AABBs.

---

## Live coding (60 min)

Build a kd-tree on a clickable point set.

Query tool: drag a rectangle.

Draw:

- splitting lines (x blue, y red)
- visited nodes in orange
- pruned cells in gray
- reported points in green
- counters: visited, pruned, reported, brute-force checks

Compare with brute force on 5_000 points. The prune count should be the story, not the milliseconds alone.

---

## Lab

1. Implement `buildKdTree` and `rangeQuery`.
2. Brute-force oracle: same reported set.
3. n = 5_000 random points, 20 random rectangles. Print average visited vs n.
4. One handwritten figure in the README: 8 points, the tree, one query, the pruned subtree circled.

Done when the oracle always matches and at least one query prunes ≥ 40% of points.

---

## Homework

1. Hand-draw a kd-tree for these points:  
   (2,3), (5,4), (9,6), (4,7), (8,1), (7,2), (6,3), (3,6).  
   Split x at the median first. Show a query [3,7] × [2,5] and mark prune / visit.
2. Written: O(√n + k) in one paragraph — a thin vertical query that hits many vertical splits.
3. Written: one use of a BVH in a Three.js app.

---

## Quiz (10 min)

1. Slab method: query time and the space problem. (2 pts)
2. kd-tree: which axis at depth 3? (2 pts)
3. When do we prune a node? (2 pts)
4. Range tree vs kd-tree: one advantage each. (2 pts)
5. BVH stores what at each node? (2 pts)

---

## Common mistakes

- Splitting always on x.
- Forgetting to test the point stored at an internal node.
- Pruning with the wrong cell (using the child’s cell for the parent).
- Reporting points that lie on the boundary twice, or dropping boundary points. **Policy:** R is closed; include the boundary.
- Building a quadtree and calling it a kd-tree in the report.

---

## Board drawings

1. Slabs through vertices.
2. kd-tree splits on 8 points.
3. A query rectangle vs a node cell: disjoint / contained / overlap.
4. BVH of three triangles.
