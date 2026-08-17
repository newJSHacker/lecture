# Chapter 7 — Discussion and Conclusion

## 7.1 Answers to the research questions

**RQ1. Kernel.**  
A single module of orientation, on-segment, intersection, point-in-triangle, incircle, and AABB tests is sufficient for hull, Delaunay, and picking. The important design rule is negative: algorithms must not grow private epsilons. Chapter 5’s test split (kernel in Node, visualizer in the browser) is what makes that rule enforceable.

**RQ2. Algorithms.**  
Andrew’s chain, incremental legalizing Delaunay, and a median-split AABB BVH are appropriate for n in the teaching range. Jarvis is worth keeping as a baseline because it makes output-sensitive complexity visible. Fortune, Chan, and Kirkpatrick would not change the educational outcome of a 20–30 page thesis.

**RQ3. Visualization.**  
Step iterators found bugs that unit tests missed, especially asymmetric twins after a flip. Visualization is therefore part of the method, not part of the GUI polish. Color conventions shared with the lecture notes reduce cognitive load.

**RQ4. Evaluation.**  
Functional invariants, oracle tests, and timing against naive baselines are enough. Fabricated FPS tables are not. Chapter 6 is intentionally a protocol. A graded thesis must fill it with data.

## 7.2 Implications for the IGWT program

The system is a bridge between the computational-geometry course and the graphics studio.

- Computer Graphics I can import the Delaunay index buffer instead of a hand-made grid.
- The configurator / interaction course can import the BVH instead of a linear `Raycaster`.
- The capstone can treat the kernel as a dependency, the way a product uses a physics engine, *provided* the student can still point to `orient`.

The larger curricular claim is modest: graduates should be able to look at a graphics bug, name the predicate that failed, and write a test for it. That sentence is also the teaching principle of the course [see [[04 Computational Geometry]]].

## 7.3 Limitations

1. **Robustness.** Epsilon predicates are inconsistent on some near-degenerate inputs. Shewchuk’s adaptive predicates or an exact library would be required for CAD-quality work [32], [33].
2. **Asymptotics.** Incremental Delaunay with walk location is not worst-case optimal. Large GIS point sets need a different locator or a library [23].
3. **3D geometry.** Hulls and Delaunay meshes remain 2D. Picking is 3D, but collision, tetrahedralization, and mesh repair are future work.
4. **Constrained edges.** Rivers, roads, and polygon boundaries are not respected. A CDT is the natural next algorithm [22].
5. **Evaluation in this sample.** Timing tables are templates. The document must not be cited as experimental evidence.

## 7.4 Future work

1. Replace `incircle` with an adaptive exact predicate and re-run the fragile Grid family.
2. Implement a constrained Delaunay triangulation and compare it with ear clipping on building footprints.
3. Add a SAH (surface-area heuristic) BVH split and compare visit counts with the median split [4].
4. Port the kernel to TypeScript and to a WebGPU compute path for discrete Voronoi (course Week 10).
5. Use the visualizer as required lab software in the computational-geometry course and collect which degenerate cases students still miss.

## 7.5 Ethical and academic notes

A project-based thesis in this program is a piece of engineering scholarship. It is legitimate to use textbooks, Stack Overflow, and large language models as *tools*. It is not legitimate to submit generated text or generated “measurements” as if they were the student’s experimental work. The present document is a reference for structure and tone. A submitted thesis must describe a system the author actually built.

## 7.6 Conclusion

This thesis specified a browser-based system for three geometric problems that appear throughout interactive graphics: constructing a convex hull, meshing a point set with a Delaunay triangulation, and picking a triangle with a bounding-volume hierarchy. The algorithms are standard. The contribution is their integration on a shared kernel, their visible invariants, and an evaluation protocol that an undergraduate can actually carry out.

The work supports a simple claim. The web is a sufficient platform for teaching and applying computational geometry at the level required by an Interactive Graphics and Web Technologies program, if — and only if — predicates, degeneracy, and tests are treated as the core of the system rather than as chores to be finished after the shaders look good.

---

# Appendix A — Suggested figure list for the printed PDF

| Figure | Caption |
| --- | --- |
| 1.1 | Three failure pictures: wrong pick, sliver terrain, self-intersecting outline |
| 4.1 | Four-layer architecture |
| 4.2 | Andrew lower/upper stacks on a 12-point set |
| 4.3 | One illegal edge and its flip, with circumcircles |
| 4.4 | BVH split of a 16-triangle mesh |
| 5.2–5.4 | Visualizer screenshots (hull, Delaunay, pick) |
| 6.1 | Hull timing plot |
| 6.2 | Before/after legalize |
| 6.3 | Terrain adapter |
| 6.4 | Ray and BVH boxes |

# Appendix B — Oral defense (sample questions)

These match the program’s oral-defense requirement [[Graduation Requirements]].

1. Why is `atan2` the wrong primitive for “left of a line”?
2. Show the input on which Jarvis is quadratic and Andrew is not.
3. Prove, in four sentences, that a Delaunay triangulation has empty circumcircles if and only if every edge is legal.
4. Your `incircle` failed on a regular grid. What did you do, and why is deleting the test unacceptable?
5. A ray hits two triangles at the same t. How do you pick a part?
6. What would you change first if this kernel were used in a medical-measurement tool rather than a teaching demo?
