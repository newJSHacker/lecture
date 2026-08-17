# Chapter 6 — Evaluation

## 6.1 Purpose

The evaluation answers three questions.

1. **Functional:** does the implementation satisfy the invariants of Chapters 3 and 4?
2. **Asymptotic:** do the measured growth rates match the textbook bounds on the intended input families?
3. **Practical:** is the system interactive in the teaching range, and does the BVH reduce triangle tests relative to a linear scan?

A fourth question — “is this faster than CGAL / Delaunator / three-mesh-bvh?” — is out of scope. Those libraries are oracles or future replacements, not competitors in an undergraduate thesis.

## 6.2 Experimental protocol

All timing experiments must be described with the following card. A submitted thesis fills every row with the author’s machine.

| Item | Protocol |
| --- | --- |
| CPU / RAM | state model and size |
| Browser or Node | state version |
| Power | “plugged in, performance mode” on laptops |
| Input families | listed in Section 6.4 |
| Repeats | warm-up discarded; report median of 11 runs |
| Clock | `performance.now()` |
| What is timed | algorithm only, not Canvas draw |

**This sample thesis does not report real measurements.** The tables below are **templates**. Their numbers are italicized and marked *illustrative*. Replacing them is a requirement for any graded submission.

## 6.3 Functional results

The test suite of Section 5.8 is the functional evaluation. For a completed project the author should report:

| Suite | Cases | Result |
| --- | --- | --- |
| Kernel predicates | 40 | *all pass (illustrative)* |
| Hull invariants + oracle | 25 | *all pass (illustrative)* |
| Delaunay legalize + oracle n ≤ 30 | 20 | *18 pass, 2 fragile cocircular (illustrative)* |
| BVH vs linear raycast, 200 random rays | 200 | *same closest triangle (illustrative)* |

Fragile cases are not failures if they are documented. They *are* failures if they are deleted to make a green badge.

**Correctness claims that do not need a clock:**

- After Andrew, every input point is on or to the left of every directed hull edge (CCW hull).
- After Delaunay, every interior edge is legal under the same `incircle` used to build the mesh.
- Every BVH hit agrees with a linear Möller–Trumbore scan on the same ray, up to t-ties broken by triangle index.

## 6.4 Input families

| Name | Description | Purpose |
| --- | --- | --- |
| Cloud | i.i.d. uniform in the unit square | typical hull / Delaunay |
| Circle | points on a circle | Jarvis worst case, h = n |
| Hull3 | three extreme points + interior cloud | Jarvis best case, h = 3 |
| Collinear | points on a line | degeneracy |
| Grid | regular m × m grid | cocircular quads |
| Jitter grid | grid + 1% noise | terrain adapter |
| Mesh-S | 64 triangles (boxes) | BVH debug |
| Mesh-M | 5,000 triangles | BVH timing |

## 6.5 Convex hull

### 6.5.1 What to measure

Time Andrew and Jarvis on Cloud, Circle, and Hull3 for n ∈ {500, 2,000, 8,000}. Record n, h, and milliseconds.

### 6.5.2 Expected shape (not a substitute for data)

Andrew should be insensitive to h. Jarvis should be clearly slower on Circle than on Hull3 at the same n. If a student’s plot does not show that, the implementation or the input generator is wrong.

**Table 6.1.** Convex-hull running time (*illustrative template*).

| n | Family | h | Andrew (ms) | Jarvis (ms) |
| ---: | --- | ---: | ---: | ---: |
| 2,000 | Cloud | *O(log n)* | *2.1* | *3.4* |
| 2,000 | Circle | 2,000 | *2.0* | *48* |
| 2,000 | Hull3 | 3 | *2.0* | *1.1* |
| 8,000 | Circle | 8,000 | *9.5* | *720* |

**Figure 6.1 (placeholder).** Log-log plot of time vs n for Andrew on Cloud.

## 6.6 Delaunay triangulation

### 6.6.1 What to measure

- Build time on Cloud and Jitter grid for n ∈ {200, 800, 2,000}.
- Number of flips per insertion (histogram).
- Number of walk steps per insertion.
- Oracle disagreement rate vs Delaunator for n ≤ 30, 100 random sets.

### 6.6.2 Qualitative evaluation

**Figure 6.2 (placeholder).** Same 40 points: a non-Delaunay triangulation with a skinny pair, and the mesh after legalize.

**Figure 6.3 (placeholder).** Terrain adapter: shaded mesh from the jittered grid.

The author should discuss sliver triangles on Grid (cocircular) versus Jitter grid. If the legalize loop does not terminate, that is a kernel bug, not a “performance issue.”

**Table 6.2.** Incremental Delaunay (*illustrative template*).

| n | Family | Time (ms) | Mean flips / insert | Mean walk steps |
| ---: | --- | ---: | ---: | ---: |
| 800 | Cloud | *18* | *3.1* | *12* |
| 2,000 | Cloud | *95* | *3.4* | *22* |
| 2,000 | Grid | *140* | *unstable / fragile* | *—* |

## 6.7 BVH picking

### 6.7.1 What to measure

For Mesh-S and Mesh-M, 200 random rays through the scene AABB:

- median triangle tests (linear vs BVH);
- median node visits and prunes;
- median time;
- disagreement count vs linear scan.

### 6.7.2 Expected shape

On Mesh-M a coherent scene should show an order-of-magnitude drop in triangle tests. A pathological mesh that fills the same AABB (every triangle overlapping the center) will not. The thesis should include one such negative example so that the BVH is not advertised as magic.

**Table 6.3.** Ray picking (*illustrative template*).

| Mesh | Method | Median triangle tests | Median time (ms) | Disagreements |
| --- | --- | ---: | ---: | ---: |
| Mesh-M | Linear | 5,000 | *1.8* | 0 |
| Mesh-M | BVH | *40* | *0.12* | *0* |
| Overlapping | BVH | *2,400* | *1.1* | *0* |

**Figure 6.4 (placeholder).** One ray, visited boxes in orange, pruned in gray.

## 6.8 Robustness

The following cases are required screenshots or test logs in a real submission:

1. Hull of an all-collinear set → two endpoints.
2. Duplicate points in the hull input → ignored.
3. Delaunay insertion exactly on an edge → edge split, not a loop.
4. Ray through a triangle vertex → still a unique closest hit (index tie-break).
5. `EPS_ORIENT` increased by 100× → list which tests flip.

Item 5 is the honesty test. If enlarging epsilon “fixes” a random Cloud failure, the algorithm is wrong.

## 6.9 Usability (lightweight)

Five classmates perform three tasks: add points and compute a hull; insert until they see a flip; pick a part in the configurator adapter. The only recorded metric is task completion (yes/no) and one sentence of confusion. This is not a CHI study. It is enough to catch a visualizer that cannot reset.

## 6.10 Summary of evaluation claims

What this sample is allowed to claim:

- the *form* of a correct undergraduate evaluation;
- the *invariants* that must hold;
- the *input families* that make complexity visible.

What it is not allowed to claim:

- that the italicized milliseconds were measured;
- that the system is faster than published libraries;
- that epsilon predicates are exact.

A student who copies Table 6.1 into a submitted PDF without running the experiment has fabricated results.
