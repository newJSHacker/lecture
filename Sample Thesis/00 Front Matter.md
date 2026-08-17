# Interactive Computational Geometry in the Browser

**Design and Evaluation of Convex Hull, Delaunay Triangulation, and Bounding-Volume Picking Algorithms for Web-Based Graphics**

A sample undergraduate graduation thesis for the program  
**Interactive Graphics and Web Technologies (IGWT)**

---

**Reference document — not for academic submission**

This thesis is an educational example for instructors and students. It shows the length, structure, and tone expected of a **20–30 page** project-based undergraduate thesis. Algorithmic claims follow standard literature. Any timing tables are **illustrative templates** and must be replaced with measurements from the author’s own implementation. Do not submit this text for credit.

Related notes: [[Graduation Requirements]] · [[04 Computational Geometry]] · [[03 Reference Thesis]]

---

## Abstract

Browser-based graphics applications routinely solve geometric problems that are usually taught as separate topics in computational geometry: constructing outlines of point sets, meshing scattered samples, and deciding which object a user has selected. In a web environment these problems must be solved with a small, robust kernel, visualized immediately, and connected to a real-time rendering pipeline.

This thesis presents the design and implementation of an interactive system that exposes three fundamental algorithms in a single JavaScript application: Andrew’s monotone-chain convex hull, incremental Delaunay triangulation with edge legalization, and a bounding-volume hierarchy (BVH) for ray–triangle picking. The system is intended both as a teaching tool for an undergraduate computational-geometry course and as a component library for interactive graphics on the web.

The work makes four contributions. First, it specifies a shared geometric kernel based on orientation and incircle predicates, and it documents a consistent policy for degeneracy. Second, it describes a modular architecture that separates predicates, constructions, spatial indexes, and visualization. Third, it implements the three algorithms so that their invariants can be observed step by step. Fourth, it defines a reproducible evaluation protocol that compares each algorithm with a naive baseline in terms of asymptotic cost, measured running time, and qualitative robustness.

The thesis argues that modern web technologies are a practical platform for undergraduate computational geometry, provided that students treat floating-point predicates as a first-class design problem rather than as an implementation detail. The resulting system is suitable as a capstone artifact: it can be demonstrated, tested, documented, and later reused in Three.js scenes for terrain meshing and object picking.

**Keywords:** computational geometry, convex hull, Delaunay triangulation, bounding volume hierarchy, ray picking, WebGL, JavaScript, interactive graphics, degeneracy, undergraduate thesis

---

## Contents

1. [[Sample Thesis/01 Introduction]]
2. [[Sample Thesis/02 Related Work]]
3. [[Sample Thesis/03 Geometric Foundations]]
4. [[Sample Thesis/04 System Design and Algorithms]]
5. [[Sample Thesis/05 Implementation]]
6. [[Sample Thesis/06 Evaluation]]
7. [[Sample Thesis/07 Discussion and Conclusion]]
8. [[Sample Thesis/08 References]]

**Suggested print length:** 24–28 pages (about 7,500–8,500 words, plus figures).

---

## Acknowledgements (sample wording)

I thank the instructors of the Interactive Graphics and Web Technologies program for feedback on the course visualizer and on an earlier draft of Chapter 6. Any remaining errors are my own. This sample acknowledgement is a placeholder for a real thesis.
