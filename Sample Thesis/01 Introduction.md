# Chapter 1 — Introduction

## 1.1 Background

Interactive graphics on the web have moved from decorative canvases to complete applications: product configurators, scientific plots, map editors, and educational simulations all run inside a browser. These applications look like rendering problems. Many of their failures, however, are geometric. A click selects the wrong triangle. A concave roof fails to triangulate. A point cloud produces a self-intersecting outline. A terrain mesh contains sliver triangles that shade badly.

Computational geometry studies exactly these questions. Classic textbooks treat convex hulls, triangulations, and spatial search as algorithms on an abstract real RAM [1], [2]. Graphics engines treat the same questions as engine features: collision hulls, navmeshes, and bounding-volume hierarchies [3], [4]. Undergraduate programs in Interactive Graphics and Web Technologies (IGWT) sit between the two traditions. Students must be able to name the predicate that failed, implement the algorithm, and then put the result on a GPU.

The browser is an attractive laboratory for that work. JavaScript and HTML Canvas make visualization cheap. WebGL and libraries such as Three.js make it possible to reuse a 2D kernel inside a 3D scene [5], [6]. The same environment also exposes the difficulty of the subject: IEEE-754 floating-point arithmetic, user-generated degenerate input, and the expectation of interactive frame rates.

## 1.2 Motivation

Three observations motivate this thesis.

First, students can complete a computer-graphics course without ever writing an orientation test. They call `Raycaster`, `ConvexGeometry`, or a Delaunay package and never see an illegal edge. When a mesh later misbehaves, they have no vocabulary for the failure.

Second, a first course in computational geometry can remain a museum of algorithms unless the implementations are visible. A gift-wrapping animation, a flip of an illegal diagonal, and a BVH that paints pruned boxes teach more than a recurrence on a slide.

Third, the three problems of **outline**, **mesh**, and **pick** appear together in almost every IGWT capstone. A configurator needs picking. A terrain demo needs a triangulation. A 2D editor needs a hull or a simple-polygon test. Implementing them in one system shows that they share a kernel.

## 1.3 Problem statement

The problem addressed by this thesis is the following.

> Design a small, browser-based system that implements convex hull construction, Delaunay triangulation, and BVH ray picking on a shared geometric kernel, so that each algorithm can be visualized, tested on degenerate input, and reused in a web-graphics application.

The problem is not to invent a new hull algorithm. It is to produce a coherent, documented, and evaluable implementation that is honest about floating-point error and suitable as an undergraduate research artifact.

## 1.4 Research questions

1. How should a JavaScript geometric kernel represent orientation, segment intersection, and the incircle test so that hull, Delaunay, and picking code do not diverge?
2. Which textbook algorithms are appropriate for an interactive undergraduate system with n on the order of 10²–10⁴ points or triangles?
3. How can visualization expose the invariant of each algorithm rather than only its final output?
4. What evaluation is sufficient to claim that the implementation is correct and useful, without fabricating experimental results?

## 1.5 Objectives

1. Specify a kernel of predicates and a degeneracy policy.
2. Implement Andrew’s monotone-chain convex hull [7].
3. Implement incremental Delaunay triangulation with legalizing flips [1], [8].
4. Implement a top-down BVH over triangle AABBs and a ray–triangle test [4], [9].
5. Provide a step-mode visualizer for hull and Delaunay, and a prune/visit visualizer for picking.
6. Define an evaluation protocol: functional tests, complexity checks, and timing against naive baselines.

## 1.6 Scope and limitations

The thesis is restricted to:

- 2D hulls and 2D Delaunay triangulations;
- 3D picking of triangles already in memory (no disk streaming);
- epsilon-based predicates, not exact rational arithmetic;
- n small enough for a teaching visualizer (hull and Delaunay up to a few thousand points; BVH up to a few tens of thousands of triangles).

The thesis does **not** implement Fortune’s Voronoi algorithm, Kirkpatrick point location, 3D Delaunay tetrahedralization, or a CGAL-style exact kernel [10], [11]. Those topics are discussed only as related work and future extensions.

## 1.7 Contributions

1. A compact architecture for teaching computational geometry in the browser.
2. A documented degeneracy policy that is shared by hull, triangulation, and intersection tests.
3. Reference implementations of three algorithms with visible invariants.
4. An evaluation chapter that separates **what must be measured** from **illustrative numbers**, so that a student submitting a real thesis knows what to replace.

## 1.8 Thesis organization

Chapter 2 reviews algorithms, robustness, and web-graphics practice.  
Chapter 3 states the geometric foundations used throughout.  
Chapter 4 presents the system design and the three algorithms.  
Chapter 5 describes the implementation.  
Chapter 6 defines evaluation and reports the form of the results.  
Chapter 7 discusses implications, limitations, and future work, then concludes.
