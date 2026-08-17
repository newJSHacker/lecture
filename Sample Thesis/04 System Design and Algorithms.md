# Chapter 4 — System Design and Algorithms

## 4.1 Design goals

The system has three design goals, in order of priority.

1. **Correctness of predicates.** A wrong orientation cannot be repaired by a prettier scene graph.
2. **Visibility of invariants.** A student (or examiner) must be able to see the stack, the illegal edge, or the pruned box.
3. **Reuse in graphics.** The same hull, mesh, and BVH modules must be callable from a Canvas demo and from a Three.js scene.

Performance is a goal only after these three. The evaluation in Chapter 6 therefore compares against naive baselines, not against highly tuned C++ libraries.

## 4.2 Architecture

The application is organized in four layers.

```
UI / visualizer
    ↓
algorithms (hull, delaunay, bvh)
    ↓
kernel (predicates, AABB)
    ↓
math (vectors, matrices)
```

The visualizer may depend on algorithms. Algorithms may depend on the kernel. The kernel may not depend on the visualizer. This rule prevents the common student pattern in which `orient` is copied into a draw function and later edited in only one place.

**Figure 4.1 (placeholder).** Layer diagram with the four boxes and the allowed arrows.

A scene in the optional Three.js view is an adapter: it converts a Delaunay triangulation into a `BufferGeometry` and a BVH query into a highlight material. It does not own a second kernel.

## 4.3 Shared data types

Points are plain objects `{x, y}` or `{x, y, z}`. A 2D triangle is three vertex indices into a point array. A half-edge structure is used internally by the Delaunay module so that an edge can find its twin and its two faces [1]. The visualizer never mutates the kernel’s arrays; it receives snapshots.

The degeneracy policy of Chapter 3 is implemented once in `kernel/policy.js` as named constants `EPS_ORIENT`, `EPS_SNAP`, and `EPS_INCIRCLE`. Chapter 5 explains how they are chosen.

## 4.4 Convex hull: Andrew’s monotone chain

### 4.4.1 Algorithm

Given a set S of n points:

1. Remove duplicates within `EPS_SNAP`.
2. Sort the remaining points lexicographically by (x, y).
3. Build the lower hull left to right. While the last three points of the stack do not make a left turn (`orient ≤ 0`), pop.
4. Build the upper hull by scanning the sorted array from right to left with the same rule.
5. Concatenate the two chains, omitting the duplicated endpoints.

### 4.4.2 Invariant

After each insertion into the lower stack, the stack is a strictly left-turning chain from the leftmost point to the current point, and every processed point lies on or above that chain.

### 4.4.3 Complexity

Sorting dominates: O(n log n). Each point is pushed and popped at most once per chain, so the scans are O(n). The algorithm is therefore O(n log n) and O(n) extra memory.

### 4.4.4 Jarvis as baseline

Jarvis march is implemented for comparison and for step-mode teaching [12]. It starts at the lowest-then-leftmost point and, at each vertex, scans all points to find the next supporting direction. Its time is Θ(n h). Chapter 6 uses a circular point set (h = n) and a triangular cloud (h = 3) to make that bound visible.

## 4.5 Delaunay triangulation: incremental legalization

### 4.5.1 Algorithm

The implementation follows the incremental flip algorithm [1], [8].

1. Create a **super-triangle** that contains all input points.
2. For each point p in random order:
   - locate the triangle t that contains p by walking from the previous triangle, using `pointInTriangle`;
   - split t into three triangles (or split an edge if p lies on one);
   - legalize every new interior edge: if an edge is illegal under `incircle`, flip it and legalize the two edges that become exposed.
3. Delete every triangle that shares a vertex with the super-triangle.

### 4.5.2 Invariant

After each insertion and its legalize cascade, the mesh of inserted points (plus the super-triangle) is Delaunay.

### 4.5.3 Location and complexity

Walking is expected to be cheap on well-shaped meshes and linear in the worst case. Combined with O(n) work per insertion in the worst case, the implementation is O(n²) in the worst case. That is acceptable for the teaching range. A student who needs larger n should add a location structure or call Delaunator [23].

### 4.5.4 Why not ear clipping as the main mesh

Ear clipping triangulates a *polygon* [17]. It is implemented in the course labs and may be used to fill a UI shape. It is the wrong main algorithm for a terrain or a point cloud, because it does not optimize triangle shape. Chapter 6 includes one qualitative figure comparing an ear-clipped concave polygon with a constrained-style mesh of the same vertices; a full constrained Delaunay implementation is left as future work.

## 4.6 BVH picking

### 4.6.1 Build

Triangles are placed in an array. A node is built recursively:

- if the bucket has at most L triangles (L = 4 in the default), store them as a leaf;
- otherwise split the longest axis of the centroid AABB at the median centroid and build two children;
- store the AABB of all triangles in the node (not only of the centroids).

### 4.6.2 Query

```
pick(node, ray, best):
    if ray misses node.aabb: return
    if node is leaf:
        for each triangle:
            if Möller–Trumbore hits and t < best.t: update best
    else:
        pick(node.left, ray, best)
        pick(node.right, ray, best)
```

The visualizer records visit/prune counts. Closest-hit is required; any-hit would be enough for shadows but not for selection.

### 4.6.3 Complexity

Build is O(n log n) with median splits. A query is O(n) in the worst case (a ray that stabs every box) and much smaller on typical scenes with spatial locality [4]. Chapter 6 reports visit counts, which are more informative than a single millisecond number.

## 4.7 Visualization as part of the design

Each algorithm exposes a **step iterator**.

- Hull: one stack operation per step.
- Delaunay: one insert, or one flip, per step.
- BVH: one node visit per step, with the current box highlighted.

This is not cosmetic. Several bugs in early drafts (a missing twin after a flip; a hull that kept a middle collinear point) were found only when the iterator was drawn. The thesis therefore treats the visualizer as a debugging instrument, not as a user-interface extra.

## 4.8 Application adapters

Two adapters demonstrate reuse.

**Terrain adapter.** A height function z = f(x, y) is sampled on a jittered grid. The (x, y) samples are triangulated. The resulting index buffer is uploaded to Three.js. Normals are computed from adjacent faces.

**Configurator adapter.** A small assembly of boxes and imported glTF triangles is wrapped in the BVH. A click produces a ray in world space; the hit triangle id maps to a part name and a highlight.

Neither adapter is a complete commercial product. They exist to show that the kernel survives contact with a rendering engine.

## 4.9 Threats the design accepts

The architecture accepts three known weaknesses.

1. Epsilon predicates can be inconsistent on near-zero inputs.
2. Walking point location can be slow or fail if the mesh is temporarily non-Delaunay during a bug.
3. A median-split AABB BVH is not the fastest ray-tracing structure.

These are acceptable in an undergraduate system if they are measured and documented. They would not be acceptable in a CAD kernel.
