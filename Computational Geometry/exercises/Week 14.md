# Extra exercises — Week 14 (project studio)

Lecture: [[Computational Geometry/Week 14 Project Studio]]  
Demo: [20-project-sandbox.html](../code/20-project-sandbox.html)

No new theory. These are desk-review prompts. Answer in the repo and the report outline, not in a new essay tonight.

---

## Studio checklist (must be true before leaving)

1. A stranger can run the demo from the README on a lab machine.
2. The core algorithm runs on more than 5 toy points.
3. One degenerate case is handled or shown and explained.
4. README: install, run, who implemented which file.
5. Kernel file exists (`orient` / intersection / incircle / …).
6. Tests exist. At least one would fail if `orient` flipped sign.
7. Report outline has the 8 headings from the lecture.
8. 30-second recording planned (even if filmed later today).

## Defense drills (write answers in a `DEFENSE.md` the TA can skim)

9. What is the predicate at the center?
10. Complexity, and for which n did you try it? (measured, not invented)
11. Show a degenerate input. What does the program do?
12. If I replace your algorithm with the naive one, what do I lose?
13. What would break in 3D?
14. Which result is a construction, and which predicate supports it?
15. What did a library do, and what did you write?

## Scope cuts (pick one if behind)

| Behind | Cut to |
| --- | --- |
| Fortune | Discrete Voronoi + Delaunay dual |
| Map editor | Intersection + DCEL walk |
| 3D physics | 2D hull + SAT |
| Pathfinding + rendering | Visibility graph on a 2D plan |
| Shaders | Unlit canvas + correct kernel |

## Snippet — freeze a degeneracy fixture

```js
// tests/degeneracy.js  — one file the TA opens first
const collinearHull = [
  { x: 0, y: 0 }, { x: 1, y: 0 }, { x: 2, y: 0 }, { x: 1, y: 1 }
];
assert(andrew(collinearHull).length === 3); // drop middle

const tJunction = segmentsIntersect(
  { x: 0, y: 0 }, { x: 4, y: 0 },
  { x: 2, y: 0 }, { x: 2, y: 3 }
);
assert(tJunction.type === "touch");

const vertexHit = pointInPolygon({ x: 1, y: 1 }, [
  { x: 0, y: 0 }, { x: 2, y: 0 }, { x: 2, y: 2 }, { x: 0, y: 2 }
]);
assert(vertexHit === "BOUNDARY" || vertexHit === "INSIDE"); // if (1,1) is interior; use a real vertex:
assert(pointInPolygon({ x: 0, y: 0 }, [
  { x: 0, y: 0 }, { x: 2, y: 0 }, { x: 2, y: 2 }, { x: 0, y: 2 }
]) === "BOUNDARY");
```

Paste your **actual** degenerate input into the sandbox and leave it as the reset state for the desk review.
