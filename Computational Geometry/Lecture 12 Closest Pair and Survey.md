# Lecture 12 — Closest pair, arrangements, Minkowski sums, visibility

**Week 12 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** closest pair: presort Px,Py; T(n)=2T(n/2)+O(n); strip |x−mid|<δ; O(1) y-neighbors (packing)  
**Success check:** oracle matches; strip scan is visibly not n²; they can draw the δ×2δ packing

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/12-dcel-walk.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: one more classic algorithm, then a map of names we will not fully teach | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
naive Θ(n²)
δ = min(δL, δR)
strip: |x−mid|<δ from already-sorted Py
for each p, only q with Δy<δ  (≤ ~7 by packing δ/2 disks)

T(n)=2T(n/2)+O(n)=O(n log n)
do not sort inside every recursive call

survey (picture + use, no lab code):
  arrangement Θ(n²)     zone O(n)
  A ⊕ B  C-obstacle     SAT cousin
  visibility graph      hug corners; Voronoi roadmap stays away
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Closest pair is the implemented topic. Arrangements, Minkowski, visibility: one picture each. A visibility graph is a project, not this lab. Project menu points at Weeks 14–15.

**Ask:** Why is the strip 2δ wide? Wait. Want: any closer pair must straddle the median, each within δ.

**Board:** parked strip. Then split by x-median, two recursive pairs, the strip.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Closest pair, arrangements, Minkowski sums, visibility*.

**Do not:** Sorting inside every recursive call (then it is O(n log² n) or worse if sloppy).

### Minutes 10–12 — Frame

**Say:** Presort; build strip in linear time from Py. Ties: any closest pair. Duplicates: dist 0, not this week. Checking all pairs in the strip is correct but not the algorithm. Do not invent timings; n=2000 vs brute should diverge because of the strip, not because you quote fps.

**Ask:** A ⊕ B is used for what in robotics?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw the packing. Do not handwave ‘we only check 7’ without the box.

**Board:** split, two recursive pairs, δ, strip. δ/2 disks in the neighborhood. Minkowski square⊕disk. Start, goal, a few visibility edges.

**Say:** Leave the field-map table up through the project (Fortune no, Kirkpatrick no, 3D Delaunay no, exact kernels Week 13).

**Ask:** Visibility-graph edge exists when?

**They do:** Trace 12 points; recurrence. Packing 1 page. Minkowski collision and visibility path, 4–6 sentences each, no code.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Median line, yellow strip, thin candidate pairs, thick best. Step the merge scan: 1–3 neighbors, not everyone. Demo 17-closest-pair.html. Plant sorting every call. Plant all-pairs in the strip. Plant implementing a visibility graph ‘for the lab.’

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Build the strip from Py in linear time. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: O(n log n) closest pair, oracle n≤800, times at 2k/5k, 12-point README trace. Homework: packing + two survey paragraphs. Quiz: time, strip width, O(1) inner, Minkowski, visibility edge. Next: graphics systems.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–20 | Recursion + strip on the board | Packing disks. |
| 20–40 | Step the strip scan | Most points compare to 1–3. |
| 40–50 | Survey three pictures | No code. |
| 50–60 | Project menu | Main algorithm must be theirs. |

Point them at `Computational Geometry/code/12-dcel-walk.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement closest pair, O(n log n).
2. Brute-force oracle for n ≤ 800.
3. Random n = 2_000, 5_000: print time vs brute (brute only at 2_000 if slow).
4. One trace on a 12-point set in the README: δ from left, δ from right, strip members, final pair.

---

## Homework

1. Trace closest pair on 12 given points (put a fixed set in the assignment PDF). State the recurrence and the O(n log n) bound.
2. Written: packing argument, 1 page, with a δ × 2δ picture.
3. Written, 4–6 sentences each: Minkowski sum for collision; visibility graph for a path. No code.

---

## Quiz next meeting (they hear this now)

1. Closest-pair time after the strip argument? (2 pts)
2. Why is the strip 2δ wide? (2 pts)
3. Why is the inner loop O(1) per point? (2 pts)
4. A ⊕ B is used for what in robotics? (2 pts)
5. Visibility-graph edge exists when? (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Closest pair (30 min).** **Input:** n points.  
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
Any pair closer than δ c

**2. Survey (15 min).** Each topic: definition, one picture, one complexity sentence, one use. No code.
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
For two convex polygons, the Minkowski sum is a convex polygon whose edges are the merged edge

**3. The map of the rest of the field (15 min).** Write this table and leave it up through the project.
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

---

## Common mistakes

1. Sorting inside every recursive call (then it is O(n log² n) or worse if sloppy).
2. Building the strip from an unsorted list and then sorting (correct but hide the linear merge).
3. Checking all pairs in the strip (correct but not the algorithm).
4. Using `< δ` vs `≤ δ` inconsistently; pick `<` and stick to it.
5. Implementing a visibility graph for the lab. That is a project, not this week.

## If we run long, cut

Arrangement construction. Keep closest pair + three names.

## If we run short, add

n=3 brute base case written carefully.
