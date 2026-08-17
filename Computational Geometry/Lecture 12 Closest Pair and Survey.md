# Lecture 12 — Closest pair, arrangements, Minkowski sums, visibility

**Time:** 75 min lecture + 60 min live coding  
**Required algorithm:** closest pair of points, divide and conquer  
**Survey only:** arrangements, Minkowski sums, visibility graphs  
**Board first:** split by x-median, two recursive pairs, the strip

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 11 |
| 10–40 | Closest pair |
| 40–55 | Survey: arrangements, Minkowski, visibility |
| 55–70 | What we are not teaching, and why you still need the names |
| 70–75 | Project menu (point to Week 14–15 notes) |

---

## Learning goals

1. State the closest-pair problem and the naive Θ(n²) algorithm.
2. Run the O(n log n) divide-and-conquer algorithm, including the strip.
3. Explain why only a constant number of strip points can lie in a δ × δ box.
4. Define an arrangement, a Minkowski sum, and a visibility graph at the level of one picture each.
5. Match each survey topic to one graphics / robotics use.

---

## 1. Closest pair (30 min)

**Input:** n points.  
**Output:** a pair p, q minimizing dist(p, q). Assume distinct points.

Naive: all pairs, Θ(n²).

### Algorithm

Presort by x into Px and by y into Py (or sort y inside the recursion).

```
closest(Px, Py):
    if n <= 3: return brute force
    split Px into L and R at the median x = mid
    split Py into Ly, Ry (points of L / R, still sorted by y)
    (dL, pairL) = closest(L, Ly)
    (dR, pairR) = closest(R, Ry)
    δ = min(dL, dR)
    pair = the winner
    strip = points of Py with |x - mid| < δ
    scan strip in y-order:
        for each point, compare to the next few points
            (while Δy < δ; at most ~7 in theory)
        if a closer pair is found: update δ and pair
    return (δ, pair)
```

### The strip argument (this is the lecture)

Any pair closer than δ cannot have both points in L or both in R (those were already checked). So both sides of the median line, and both in the 2δ-wide strip.

In the strip, sort by y. For a point p, only points q with `q.y − p.y < δ` can beat δ. Those points lie in a δ × 2δ rectangle. Packing: disks of radius δ/2 around strip points are disjoint and sit in a box that holds only a constant number (classically 6–8, depending on the write-up). So the inner loop is O(1) per point, the merge is O(n), and

```
T(n) = 2 T(n/2) + O(n) = O(n log n)
```

Draw the packing. Do not handwave “we only check 7” without the box.

### Implementation notes

- Presort; do not sort the whole set in every recursive call.
- Build the strip from the already-sorted Py in linear time.
- Ties: any closest pair is fine; report one.
- Duplicates: distance 0; reject or treat as a special case in the project, not here.

---

## 2. Survey (15 min)

Each topic: definition, one picture, one complexity sentence, one use. No code.

### Line arrangements

n lines divide the plane into faces, edges, vertices.

- Complexity: Θ(n²) faces, edges, vertices.
- **Zone theorem (name):** the zone of one line (faces it touches) has complexity O(n).
- Incremental construction of an arrangement is O(n²).
- Use: visibility in a line-like world, duality (points ↔ lines), some graphics papers on line-space.

We will not build one.

### Minkowski sums

```
A ⊕ B = { a + b | a ∈ A, b ∈ B }
```

If A is an obstacle and B is a robot (as a set of vectors from a reference point), then A ⊕ (−B) is the **configuration-space obstacle**: the robot (as a point) cannot enter it.

For two convex polygons, the Minkowski sum is a convex polygon whose edges are the merged edge-direction lists. Time O(n + m).

Use: 2D collision (“does the character’s shape hit the wall?”), offset curves, packing.

SAT (separating axis theorem) in games is a cousin: convex vs convex.

### Visibility graphs

Vertices: corners of polygonal obstacles (plus start and goal).  
Edge: if the segment between two vertices does not stab an obstacle.

Shortest path among obstacles = shortest path in this graph (2D, polygonal).  
Size: O(n²) in the worst case.  
Use: crowd / robot project; navmesh is the modern games substitute.

Voronoi roadmaps (Week 10) stay away from obstacles; visibility graphs hug corners. Different aesthetics, both valid project bases.

---

## 3. The map of the rest of the field (15 min)

Write this table and leave it up through the project.

| Name | We did? | If you need it later |
| --- | --- | --- |
| Predicates, intersection, PIP | yes | kernel of everything |
| Hulls | yes | collision, culling |
| Sweep intersections | yes | CAD, maps |
| Ear clipping | yes | UI, fonts |
| DCEL | yes | meshes |
| kd-tree / BVH | yes | picking |
| Voronoi / Delaunay | yes | terrain, regions |
| Closest pair | today | proximity |
| Fortune fully | no | library |
| Kirkpatrick | no | library |
| Arrangements | name | reading |
| Minkowski | name | collision project |
| Visibility graph | name | path project |
| 3D Delaunay | no | meshing tools |
| Exact kernels | Week 13 | Shewchuk |

---

## Live coding (60 min)

Closest pair with the strip drawn.

- Points
- Median line
- Recursive bounding boxes (optional)
- Strip in yellow
- Candidate pairs in the strip as thin lines
- Current best pair thick

Keys: step the merge scan. Students should see that most strip points compare to 1–3 neighbors, not to everyone.

Then run n = 2_000 vs brute force. Times should diverge.

---

## Lab

1. Implement closest pair, O(n log n).
2. Brute-force oracle for n ≤ 800.
3. Random n = 2_000, 5_000: print time vs brute (brute only at 2_000 if slow).
4. One trace on a 12-point set in the README: δ from left, δ from right, strip members, final pair.

Done when oracle matches and the strip scan is visibly not n².

---

## Homework

1. Trace closest pair on 12 given points (put a fixed set in the assignment PDF). State the recurrence and the O(n log n) bound.
2. Written: packing argument, 1 page, with a δ × 2δ picture.
3. Written, 4–6 sentences each: Minkowski sum for collision; visibility graph for a path. No code.

---

## Quiz (10 min)

1. Closest-pair time after the strip argument? (2 pts)
2. Why is the strip 2δ wide? (2 pts)
3. Why is the inner loop O(1) per point? (2 pts)
4. A ⊕ B is used for what in robotics? (2 pts)
5. Visibility-graph edge exists when? (2 pts)

---

## Common mistakes

- Sorting inside every recursive call (then it is O(n log² n) or worse if sloppy).
- Building the strip from an unsorted list and then sorting (correct but hide the linear merge).
- Checking all pairs in the strip (correct but not the algorithm).
- Using `< δ` vs `≤ δ` inconsistently; pick `<` and stick to it.
- Implementing a visibility graph for the lab. That is a project, not this week.

---

## Board drawings

1. Split, two recursive pairs, δ, the strip.
2. δ/2 disks packed in the 2δ × δ neighborhood.
3. Minkowski: square ⊕ disk = rounded square; polygon ⊕ robot = C-obstacle.
4. Two obstacles, start, goal, a few visibility edges.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 12]] · Demo: [17-closest-pair.html](code/17-closest-pair.html)

1. Packing: why only O(1) strip comparisons per point.
2. Presort Px, Py. Do not sort inside every recursive call.
3. DC distance must match brute on n = 200.
4. Survey: Minkowski = robot ⊕ obstacle. Visibility graph is a project, not this lab.

```js
const strip = Py.filter((p) => Math.abs(p.x - midX) < best.dist);
for (let i = 0; i < strip.length; i++) {
  for (let j = i + 1; j <= i + 7 && j < strip.length; j++) {
    if (strip[j].y - strip[i].y >= best.dist) break;
    // maybe update best
  }
}
```
