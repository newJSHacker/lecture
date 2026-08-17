# Chapter 2 — Related Work

This chapter reviews the algorithms implemented in the thesis, the literature on geometric robustness, and the practice of computational geometry on the web. The aim is not an exhaustive survey. It is to justify the particular choices made in Chapters 4 and 5.

## 2.1 Convex hulls

The convex hull of a finite point set is a classical primitive. Jarvis’s gift wrapping computes the hull in Θ(n h) time by walking supporting lines [12]. The algorithm is output-sensitive and excellent when h is tiny; it is quadratic when the points are in convex position. Graham’s scan sorts by polar angle around an extreme point and then walks a stack in linear time, for O(n log n) total [13]. Andrew’s monotone chain uses the same stack idea but sorts by (x, y), which avoids polar-angle ties [7]. Chan’s algorithm combines Jarvis and Graham to achieve O(n log h) [14]. Three-dimensional hulls are substantially harder; randomized incremental construction and the Qhull package are the usual practical references [15], [16].

This thesis uses Andrew’s algorithm as the default implementation and Jarvis as a teaching baseline. The choice follows the undergraduate course: Andrew is easier to implement correctly than Graham, and it is worst-case optimal. Chan’s algorithm is omitted because the extra machinery does not change the visual story for n in the teaching range.

## 2.2 Triangulations and Delaunay meshes

Every simple polygon with n vertices admits a triangulation with n − 2 triangles [2]. Ear clipping is the standard O(n²) undergraduate method [17]. Faster polygon triangulation proceeds by monotone subdivision [1]. These algorithms fill a *given* boundary. They do not, by themselves, produce well-shaped triangles.

The Delaunay triangulation of a point set is characterized by the empty-circumcircle property: no site lies in the interior of any triangle’s circumcircle [1], [18]. It is the dual of the Voronoi diagram [19]. Incremental insertion with edge flips (or the equivalent Bowyer–Watson cavity) is the usual teaching algorithm [8], [20], [21]. Fortune’s sweep computes the Voronoi diagram, and therefore the Delaunay triangulation, in O(n log n) time [10]. Constrained Delaunay triangulation respects prescribed edges and is the right tool for navmeshes and GIS polygons [22].

On the web, Delaunator is a widely used 2D implementation [23]. Earcut triangulates polygons, including holes, for map rendering [24]. This thesis reimplements incremental Delaunay rather than calling Delaunator for the main algorithm, because the educational goal is the legalize/flip invariant. A library may be used as an *oracle* in tests.

## 2.3 Geometric search and picking

Point location asks which face of a subdivision contains a query point. The slab method is simple and uses quadratic space; Kirkpatrick’s hierarchy achieves O(log n) queries with linear space [11]. Range searching on points is solved by kd-trees, range trees, and quadtrees [1], [25].

Interactive graphics almost never uses Kirkpatrick’s hierarchy. It uses bounding-volume hierarchies. Clark described hierarchical geometric models for hidden-surface work [26]. Rubin and Whitted and later Kay and Kajiya used nested volumes for ray tracing [27], [28]. Gottschalk, Lin, and Manocha popularized OBB trees for collision [29]. In modern web practice, Three.js performs naive raycasts unless a structure such as `three-mesh-bvh` is added [5], [30]. The Möller–Trumbore test is the usual narrow-phase ray–triangle intersection [9].

This thesis implements a top-down AABB BVH and Möller–Trumbore picking. A 2D kd-tree is discussed as the planar analogue taught in the course, but picking is evaluated in 3D because that is the IGWT use case.

## 2.4 Robustness

Fortune and Van Wyk, Shewchuk, and the CGAL project documented that naive floating-point predicates fail on near-degenerate input [31], [32], [33]. Shewchuk’s adaptive predicates evaluate a floating-point filter and fall back to exact arithmetic only when the error bound requires it [32]. Exact constructions (intersection points, circumcenters) remain difficult even when predicates are exact [34].

Game and web code typically uses an epsilon. That policy is acceptable for teaching and for many interactive applications if it is *consistent* and *tested*. It is not a substitute for an exact kernel in CAD. Chapter 3 states the epsilon policy used here; Chapter 7 discusses when a student project should switch to a library.

## 2.5 Computational geometry in the browser

JavaScript is an unusual vehicle for computational geometry: it offers only IEEE-754 doubles, no operator overloading, and a single-threaded UI unless workers are used. It also offers Canvas and WebGL, which make algorithm animation straightforward. Several teaching visualizers exist for hulls and Delaunay triangulations; few treat a shared kernel, degeneracy tests, and BVH picking as one thesis-sized system. That combination is the gap this work fills.

## 2.6 Summary of design decisions

| Topic | Adopted approach | Rejected for this thesis |
| --- | --- | --- |
| Hull | Andrew, Jarvis as baseline | Chan, 3D Qhull |
| Mesh | Incremental Delaunay + flips | Fortune, ear clipping as the main mesh |
| Search | AABB BVH + Möller–Trumbore | Kirkpatrick, full kd-tree picking |
| Predicates | Shared kernel, epsilon policy | CGAL exact kernel |
| Platform | JavaScript + Canvas + optional Three.js | Native C++ only |

These decisions keep the implementation inside a 20–30 page undergraduate scope while remaining faithful to the literature.
