# Lecture 4 — Convex hull I (intuition and slow algorithms)

**Week 4 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Jarvis: start lowest-then-leftmost; next = all-left supporting; collinear take farthest; Θ(n h)  
**Success check:** they can wrap 8 points by hand; circle n is slower than a cloud with h=3; no atan2

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/04-point-in-polygon.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: the hull as extreme points before a famous O(n log n) algorithm | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
CH(S) = smallest convex set containing S
extreme = hull vertex = supporting line through p, S on one side

policy: unique points; drop strictly intermediate collinear

start = lowest then leftmost
o < 0: r is right of p→q → q = r
o = 0 and farther: q = r

time Θ(n h)     circle: h=n → Θ(n²)
Ω(n log n): points (xi, xi²); hull visits sorted x
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Rubber band around nails. Jarvis is output-sensitive: great when h is tiny, quadratic when points already sit on a circle. Polar angles wrap — we use orient.

**Ask:** Jarvis time in n and h? Wait. Want: Θ(n h).

**Board:** parked strip. Then rubber band around nails.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Convex hull I (intuition and slow algorithms)*.

**Do not:** Starting at a random point (may be interior; the first “wrap” is undefined).

### Minutes 10–12 — Frame

**Say:** Incremental hull: idea only (tangents, O(n²) naive). 3D incremental is the later mental model. Lower bound is algebraic decision-tree teaching level: if hull were o(n log n), sorting would be too. Measure cloud vs circle; do not invent milliseconds.

**Ask:** Why start at lowest-then-leftmost?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Interior points are not extreme. Collinear middles are not hull vertices under our policy.

**Board:** rubber band. One full wrap on 8 points with the candidate ray. Parabola (xi,xi²) and the lower hull.

**Say:** Invariant: polyline so far is a hull prefix; supporting ray has S on its left if we wrap CCW.

**Ask:** Is Jarvis optimal for points in convex position? Why not?

**They do:** Written: h=3 input and h=n input with Θ. Parabola reduction 6–8 sentences + 5 points.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Step mode: N one comparison, E one edge, Space finish. Current p/q/r colored. Time n=2000 cloud vs n=400 circle. Demo 07-jarvis.html. Plant starting at a random interior point. Plant nearest collinear (cuts the edge short). Plant duplicates infinite loop.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One wrap step: given p and candidates, pick next q. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: Jarvis; buttons cloud/circle/triangle+cloud; print n,h,elapsed; table 100/1k/10k. Homework: collinear policy + duplicate removal. Quiz: extreme point, Θ(nh), start, convex-position, sorting reduction.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Definitions + policy | Drop middle collinear. |
| 15–40 | Step-mode wrap | q jumps when a righter point appears. |
| 40–50 | Circle vs cloud timing | Measure; do not invent ms. |
| 50–60 | They implement the inner for-r | Circulate. No atan2. |

Point them at `Computational Geometry/code/04-point-in-polygon.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement Jarvis march.
2. Buttons: random cloud, random circle, triangle-plus-cloud.
3. Print n, h, elapsed milliseconds.
4. Measure n = 100, 1_000, 10_000 on cloud and on circle. Table in the README.

---

## Homework

1. Implement Jarvis with the course collinear policy and duplicate removal.
2. Written: an input with h = 3 and an input with h = n. State the resulting Θ.
3. Written: 6–8 sentences on the parabola reduction. Draw 5 points on y = x² and their hull.

---

## Quiz next meeting (they hear this now)

1. Define extreme point. (2 pts)
2. Jarvis time in terms of n and h. (2 pts)
3. Why start at lowest-then-leftmost? (2 pts)
4. Is Jarvis optimal for points in convex position? Why? (2 pts)
5. One sentence: how sorting reduces to hull. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Definitions (15 min).** Let S be a finite set of n points in the plane.
The **convex hull** `CH(S)` is the smallest convex set containing S.  
Equivalently: the intersection of all convex sets that contain S.  
Equivalently: the set of all convex combinations of points of S.
For a finite set, `CH(S)` is a convex polygon whose vertices are points of S.
A point p ∈ S is **extreme** if p is a vertex of `CH(S)`. Equivalently: there exists a supporting line through p such that all of S lies on one side.
**Interior / boundary / hole points:** a point strictly inside the hull is not extreme. Collinear points in the middle of a hull edge are extreme only if we keep them (policy).
**Course policy (state now, keep through Week 5):**
- Remove duplicate points first.
- On a hull edge, **drop** strictly intermediate collinear

**2. Jarvis march (25 min).** Also called **gift wrapping**.
### Idea
Start at a guaranteed hull point: the lowest point (smallest y; if tie, smallest x).  
Then repeatedly wrap a supporting line around the set until we return to the start.
### Algorithm
```
jarvis(S):
    remove duplicates
    if n ≤ 1: return S
    start = lowest-then-leftmost point
    hull = []
    p = start
    do:
        hull.append(p)
        q = first point in S that is not p
        for r in S:
            if r == p: continue
            o = orient(p, q, r)
            if o < 0:                 // r is right of p→q, so q is not the next hull vertex
                q = r
            else if o == 0 and farther(p, r, q):
                q = r                 // same direction, take the farthest
        p = q
    while p != start
    return hull


**3. Incremental construction (15 min).** Idea only. No required implementation.
Add points one by one.
- Maintain `CH` of the points so far.
- If the new point p is inside, do nothing.
- If p is outside, find the two tangents from p to the current hull and replace the visible chain by p.
Finding tangents on a convex polygon is O(log n) with binary search, or O(n) naively. A naive incremental algorithm is O(n²).
This is the right mental model for 3D incremental hulls. Mention it; do not code it this week.
---

**4. Lower bound (10 min).** **Claim.** Computing the convex hull in 2D takes Ω(n log n) time in the algebraic decision-tree model.
**Reduction (teaching).**  
To sort x1…xn, map each xi to the point `(xi, xi²)` on the parabola y = x². The hull (lower or full) visits the points in sorted x-order. If hull were o(n log n), sorting would be too.
So Graham / Andrew (next week) are optimal in the worst case. Jarvis is not, unless h is small.
---

---

## Common mistakes

1. Starting at a random point (may be interior; the first “wrap” is undefined).
2. Taking the nearest collinear point and cutting a hull edge short.
3. Infinite loop because duplicates were not removed (`p` never returns to `start` cleanly, or `q` stays equal to `p`).
4. Using angles and hitting the ±π wrap.

## If we run long, cut

Incremental code. Keep Jarvis + parabola.

## If we run short, add

Expected Gaussian h = O(log n) as a name.
