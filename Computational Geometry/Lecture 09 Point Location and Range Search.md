# Lecture 9 — Point location and range search

**Week 9 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** kd-tree: alternate x/y median; range query prune if cell disjoint, take if cell ⊂ R; closed range  
**Success check:** oracle matches; at least one query prunes ≥40% of 5000 points; they draw 8 points and a pruned subtree

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/09-naive-intersect.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: which face contains q, and which points are in this rectangle — not ‘test every face’ | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
point location: slabs O(log n) query, O(n²) space — too fat
Kirkpatrick: name, O(n) space; we do not code it
ship: BVH / kd on boxes + point-in-triangle

kd build: axis = depth%2; median; cells
query: disjoint → prune; contained → report all; else both
worst O(√n + k)     thin query stabs many cells

quadtree splits space; range tree: name O(log² n + k)
BVH: tree of object AABBs (Week 13 pick)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Midterms back briefly; no quiz. Point location is not test every face. Practical substitute: a BVH plus last month’s inside test. Today we implement the kd-tree because the prune is visible.

**Ask:** When do we prune a node? Wait. Want: cell disjoint from R.

**Board:** parked strip. Then a point set, a query rectangle, brute force vs pruned boxes.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Point location and range search*.

**Do not:** Splitting always on x.

### Minutes 10–12 — Frame

**Say:** Include boundary (R closed). Split always on x is a fail. Forgetting the point at an internal node is a fail. Quadtree ≠ kd-tree in the report. Do not invent milliseconds; visited vs brute is the story.

**Ask:** Which axis at depth 3? Want: y (if depth 0 is x).

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Slab method as the obvious structure; space explodes.

**Board:** slabs. kd splits on 8 points. Query vs cell: disjoint / contained / overlap. BVH of three triangles.

**Say:** kd vs BVH table: points vs objects; orthogonal range vs ray/frustum; GIS vs three-mesh-bvh.

**Ask:** BVH stores what at each node?

**They do:** Hand-draw kd for (2,3),(5,4),(9,6),(4,7),(8,1),(7,2),(6,3),(3,6); query [3,7]×[2,5]. O(√n+k) paragraph. One Three.js BVH use.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Clickable points, drag rectangle, x-splits blue y red, visited orange, pruned gray, reported green. Counters vs brute on 5000. Demo 13-kd-range.html. Plant always splitting on x. Plant pruning with the child’s cell.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** rangeQuery prune test. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: build+query, oracle, 20 random rects, README figure of 8 points. Homework: that figure is required. Quiz: slabs, axis, prune, range-tree vs kd, BVH box.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Slabs then ‘we will not ship that’ | Kirkpatrick name. |
| 15–40 | Build 8 points on the board then in code | Median x first. |
| 40–50 | A query that greys a whole subtree | The story. |
| 50–60 | BVH sentence | Week 13 will pick with it. |

Point them at `Computational Geometry/code/09-naive-intersect.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement `buildKdTree` and `rangeQuery`.
2. Brute-force oracle: same reported set.
3. n = 5_000 random points, 20 random rectangles. Print average visited vs n.
4. One handwritten figure in the README: 8 points, the tree, one query, the pruned subtree circled.

---

## Homework

1. Hand-draw a kd-tree for these points:
2. Written: O(√n + k) in one paragraph — a thin vertical query that hits many vertical splits.
3. Written: one use of a BVH in a Three.js app.

---

## Quiz next meeting (they hear this now)

1. Slab method: query time and the space problem. (2 pts)
2. kd-tree: which axis at depth 3? (2 pts)
3. When do we prune a node? (2 pts)
4. Range tree vs kd-tree: one advantage each. (2 pts)
5. BVH stores what at each node? (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Point location (15 min).** **Problem.** Preprocess a planar subdivision (a DCEL). Then, for a query point q, report the face that contains q.
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
###

**2. kd-trees (25 min).** **Problem.** Preprocess n points. Query: report (or count) points inside a rectangle R = [x1, x2] × [y1, y2].
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
 

**3. Quadtrees and range trees (15 min).** ### Quadtree
Split the **space** into four squares, not the point set by median. Good for uniformly spread points and for images / tiles. Degenerates if all points sit in one corner (need a stop rule: capacity, or minimum cell size).
Graphics: mip-like spatial bins, terrain tiles, “what is in this screen tile?”
### Range tree
A tree on x; each node stores a tree of its subtree on y.  
Query: O(log² n + k). Space: O(n log n).
Name it as the theoretically nicer range-search structure. Do not implement.
---

**4. BVH — the graphics kd-tree (15 min).** A **bounding volume hierarchy** is a binary tree of objects (triangles, meshes), not of points.
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

---

## Common mistakes

1. Splitting always on x.
2. Forgetting to test the point stored at an internal node.
3. Pruning with the wrong cell (using the child’s cell for the parent).
4. Reporting points that lie on the boundary twice, or dropping boundary points. **Policy:** R is closed; include the boundary.
5. Building a quadtree and calling it a kd-tree in the report.

## If we run long, cut

Range-tree code. Keep kd prune + BVH name.

## If we run short, add

Closed-range boundary policy in the README.
