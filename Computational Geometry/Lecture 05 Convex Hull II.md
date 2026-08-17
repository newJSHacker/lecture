# Lecture 5 — Convex hull II (Graham and Andrew)

**Week 5 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Andrew: sort (x,y); lower/upper stacks; while orient(h[-2],h[-1],p)≤0 pop; O(n log n); no atan2  
**Success check:** all-collinear returns two endpoints; Andrew on a circle is not Θ(n²); join does not duplicate endpoints

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/05-aabb.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: the hull algorithm they will actually use | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
Graham: p0 lowest-left; sort by orient(p0,a,b) not atan2; stack, pop non-left
Andrew (required):
  unique sort (x,y)
  lower L→R; upper reverse
  ≤0 pops collinear middles
  pop duplicated endpoints; concatenate

scan O(n): each point pushed/popped ≤ once per chain
Jarvis when h tiny; Andrew default

AABB is cheap and loose; hull is tight (diagonal stick)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Graham’s danger is polar sort. Andrew never asks for an angle. 3D hull is a mesh of triangles, not a polygon — gift wrap / incremental named, not coded.

**Ask:** What is the sort key in Andrew? Wait. Want: (x,y).

**Board:** parked strip. Then sort by x, build lower hull, build upper hull.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Convex hull II (Graham and Andrew)*.

**Do not:** Forgetting to unique-sort; then `<= 0` pops everything because consecutive duplicates are collinear with anything.

### Minutes 10–12 — Frame

**Say:** To keep collinear hull points, use <0 only. Forgetting unique-sort: consecutive duplicates are collinear with anything and ≤0 pops the world. Graphics: AABB, OBB, broad phase, silhouette = supporting line = one Jarvis step.

**Ask:** What does orient≤0 do to collinear hull points?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why the while-loop is O(n) after sorting: each index pushed/popped ≤ once.

**Board:** Graham polar around p0. Andrew sorted list, two stacks, join. AABB vs hull on a diagonal stick.

**Say:** Table Jarvis / Graham / Andrew. Default = Andrew.

**Ask:** Give one case where Jarvis beats Andrew.

**They do:** Prove the scan is O(n). One paragraph AABB vs hull as collision proxy.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Andrew with stacks drawn: sorted indices, lower blue, upper red, pops flash. Same 10k cloud and 2k circle as Week 4 — Andrew does not care that h=n. Demo 08-andrew.html. Plant concatenating without popping endpoints. Plant both chains L→R with the same orient test.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** lower-hull while-condition on paper then in code. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: Andrew; compare Jarvis; toggle drop vs keep collinear; tests n=0,1,2, triangle, all-collinear, square+interior. Homework: document collinear policy. Quiz: sort key, O(n) while, ≤0, when Jarvis, one 3D strategy.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Graham without atan2 | orient(p0,a,b); nearer-first pops middles. |
| 15–40 | Andrew step mode | Join off-by-one is the plant. |
| 40–50 | Circle n vs Jarvis | Andrew stays O(n log n). |
| 50–60 | They unique-sort first | Circulate. |

Point them at `Computational Geometry/code/05-aabb.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement Andrew.
2. Compare with last week’s Jarvis on:
3. random cloud n = 10_000
4. circle n = 2_000
5. Toggle policy: drop vs keep collinear. Show a 4-point collinear top edge.
6. Unit tests: n = 0,1,2; triangle; all-collinear; square with a point in the middle.

---

## Homework

1. Implement Andrew (or Graham if you justify polar compare without `atan2`).
2. Document the collinear policy in the README.
3. Written: prove the scan is O(n) after sorting (each index pushed/popped ≤ once per chain).
4. Written: one paragraph on AABB vs convex hull as a collision proxy. When is the AABB good enough?

---

## Quiz next meeting (they hear this now)

1. What is the sort key in Andrew? (2 pts)
2. Why is the while-loop total O(n)? (2 pts)
3. What does `orient <= 0` do to collinear hull points? (2 pts)
4. Give one case where Jarvis beats Andrew. (2 pts)
5. Name one 3D hull strategy. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Graham scan (20 min).** ### Steps
1. Find the lowest-then-leftmost point p0.
2. Sort the remaining points by polar angle around p0. Break ties by distance.
3. Scan the sorted list with a stack. While the last three points make a non-left turn, pop.
```
graham(S):
    remove duplicates
    p0 = lowest-then-leftmost
    L = others sorted by (orient(p0, a, b), then dist to p0)
        // a before b if orient(p0,a,b) > 0
        // if collinear, nearer first (they will be popped) or farther first (policy)
    stack = [p0, L[0], L[1]]
    for p in L[2…]:
        while orient(next_to_top, top, p) <= 0: pop
        push p
    return stack
```
`<= 0` pops collinear middles if we drop them.
### Why the sort is the dangerous part
Polar sort with `atan2` is fragile. Compare with `orient(p0, a, b)` instead.
If two points are

**2. Andrew’s monotone chain (25 min).** This is the algorithm students must implement. It avoids polar angles entirely.
### Steps
1. Remove duplicates.
2. Sort points by (x, y).
3. Build the **lower hull** left → right.
4. Build the **upper hull** left → right (or right → left).
5. Concatenate, removing the duplicated endpoints.
```
andrew(S):
    P = unique points sorted by (x, y)
    if |P| <= 2: return P
    lower = []
    for p in P:
        while |lower| >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            pop lower
        push p onto lower
    upper = []
    for p in reverse(P):
        while |upper| >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            pop upper
        push p onto upper
    pop last of lower   // same as first of upper
    pop last of upper   // same as first of lower
    return lower + upper

**3. 3D preview (10 min).** In 3D the hull is a convex polyhedron.
- **Gift wrapping** still works; a “step” is a face, and the search is over a 1D set of candidate edges. Time grows fast.
- **Incremental:** add a point, remove visible faces, sew the horizon. This is the usual textbook 3D algorithm.
- **Conflict graphs** make expected incremental construction O(n log n).
We will not implement 3D hulls. Graphics engines use them for collision hulls and for silhouette ideas. Students should know the output is a mesh of triangles, not a polygon.
---

**4. Graphics connections (10 min).** | Structure | How it uses a hull |
| --- | --- |
| AABB | hull of the 4 (or 8 in 3D) extreme coordinates; cheaper, looser |
| OBB | oriented box; a cheap approximation of the 2D hull |
| Broad-phase collision | if hulls (or AABBs) miss, objects miss |
| Camera / frustum | a 2D analog is “is this sprite’s hull on screen?” |
| Shadow / silhouette | extreme points in a light direction (supporting line) |
Live sentence: Jarvis is one supporting line after another. A directional extreme query is one step of Jarvis.
---

---

## Common mistakes

1. Forgetting to unique-sort; then `<= 0` pops everything because consecutive duplicates are collinear with anything.
2. Concatenating lower and upper without removing the duplicated endpoints → a zero-length edge and a later crash.
3. Building both chains left-to-right with the same orientation test, so one chain turns the wrong way.
4. Using `atan2` in Graham and failing the left-half vs right-half.

## If we run long, cut

Conflict-graph 3D. Keep Andrew + collinear policy.

## If we run short, add

Oracle: Andrew vertex set equals Jarvis vertex set.
