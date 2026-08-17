# Lecture 4 — Convex hull I (intuition and slow algorithms)

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** Jarvis march (gift wrapping)  
**Board first:** rubber band around nails

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 3 |
| 10–25 | Definitions: hull, extreme points, supporting line |
| 25–50 | Jarvis march, invariant, complexity |
| 50–65 | Incremental construction (idea) |
| 65–75 | Lower bound: hull is at least sorting |

---

## Learning goals

1. Define the convex hull of a finite point set.
2. Identify extreme points and supporting lines.
3. Run Jarvis march by hand and in code.
4. State the complexity Θ(n h) and when that is good or bad.
5. Explain why Ω(n log n) is a lower bound in the algebraic decision-tree sense (teaching level).

---

## 1. Definitions (15 min)

Let S be a finite set of n points in the plane.

The **convex hull** `CH(S)` is the smallest convex set containing S.  
Equivalently: the intersection of all convex sets that contain S.  
Equivalently: the set of all convex combinations of points of S.

For a finite set, `CH(S)` is a convex polygon whose vertices are points of S.

A point p ∈ S is **extreme** if p is a vertex of `CH(S)`. Equivalently: there exists a supporting line through p such that all of S lies on one side.

**Interior / boundary / hole points:** a point strictly inside the hull is not extreme. Collinear points in the middle of a hull edge are extreme only if we keep them (policy).

**Course policy (state now, keep through Week 5):**

- Remove duplicate points first.
- On a hull edge, **drop** strictly intermediate collinear points. The hull vertices are the two endpoints of that edge.

---

## 2. Jarvis march (25 min)

Also called **gift wrapping**.

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
```

`farther(p, r, q)` is `dist(p,r) > dist(p,q)`.

If we **drop** intermediate collinear points, the `o == 0` branch should still pick the farthest, so we jump to the end of the collinear run.

### Invariant

After k steps, the polyline `hull[0]…hull[k-1]` is a prefix of the hull boundary, and the current supporting ray has S on its left (if we wrap CCW).

We wrap CCW if “r is more left” updates q. The code above wraps by rejecting right turns, i.e. the next edge is the one with all points to the left or on it.

### Complexity

Each of the h hull edges scans up to n points.  
**Time: Θ(n h).**  
Space: O(h) besides the input.

| Input | h | Time |
| --- | --- | --- |
| Points in convex position (circle) | n | Θ(n²) |
| Points with 3 extreme (triangle + cloud inside) | 3 | Θ(n) |
| Random Gaussian | O(log n) expected | about O(n log n) |

Jarvis is **output-sensitive**. Good when h is tiny. Bad when the points are already on a circle.

### Trace on the board

Use 8 points, 5 on the hull. Walk one candidate at a time. Students should see q jump whenever a righter (or lefter) point appears.

---

## 3. Incremental construction (15 min)

Idea only. No required implementation.

Add points one by one.

- Maintain `CH` of the points so far.
- If the new point p is inside, do nothing.
- If p is outside, find the two tangents from p to the current hull and replace the visible chain by p.

Finding tangents on a convex polygon is O(log n) with binary search, or O(n) naively. A naive incremental algorithm is O(n²).

This is the right mental model for 3D incremental hulls. Mention it; do not code it this week.

---

## 4. Lower bound (10 min)

**Claim.** Computing the convex hull in 2D takes Ω(n log n) time in the algebraic decision-tree model.

**Reduction (teaching).**  
To sort x1…xn, map each xi to the point `(xi, xi²)` on the parabola y = x². The hull (lower or full) visits the points in sorted x-order. If hull were o(n log n), sorting would be too.

So Graham / Andrew (next week) are optimal in the worst case. Jarvis is not, unless h is small.

---

## Live coding (60 min)

Implement Jarvis with **step mode**.

Keys:

- `N` — one candidate comparison
- `E` — finish the current hull edge
- `Space` — run to completion

Draw:

- current p (blue)
- current candidate q (orange)
- point r being tested (black)
- accepted hull edges (thick)
- the full set (dots)

Talk:

- “I always start at lowest-then-leftmost, so I never start inside.”
- “When three are collinear I take the farthest, so I obey the drop-middle policy.”

Time a random n = 2000 run vs a circle of n = 400 so students see Θ(n h).

---

## Lab

1. Implement Jarvis march.
2. Buttons: random cloud, random circle, triangle-plus-cloud.
3. Print n, h, elapsed milliseconds.
4. Measure n = 100, 1_000, 10_000 on cloud and on circle. Table in the README.

Done when the circle case is visibly slower than the cloud for the same n.

---

## Homework

1. Implement Jarvis with the course collinear policy and duplicate removal.
2. Written: an input with h = 3 and an input with h = n. State the resulting Θ.
3. Written: 6–8 sentences on the parabola reduction. Draw 5 points on y = x² and their hull.

---

## Quiz (10 min)

1. Define extreme point. (2 pts)
2. Jarvis time in terms of n and h. (2 pts)
3. Why start at lowest-then-leftmost? (2 pts)
4. Is Jarvis optimal for points in convex position? Why? (2 pts)
5. One sentence: how sorting reduces to hull. (2 pts)

---

## Common mistakes

- Starting at a random point (may be interior; the first “wrap” is undefined).
- Taking the nearest collinear point and cutting a hull edge short.
- Infinite loop because duplicates were not removed (`p` never returns to `start` cleanly, or `q` stays equal to `p`).
- Using angles and hitting the ±π wrap.

---

## Board drawings

1. Rubber band / extreme points.
2. One full Jarvis wrap on 8 points with the candidate ray.
3. Parabola reduction: points `(xi, xi²)` and the lower hull.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 04]] · Demo: [07-jarvis.html](code/07-jarvis.html)

1. Fill Θ(n h) for: circle; triangle+cloud; expected Gaussian.
2. Start at a random interior point. What breaks?
3. 50 duplicate copies of 5 hull points. What infinite loop looks like.
4. Measure cloud vs circle in the demo. Do not invent milliseconds.

```js
// Jarvis: start lowest-then-leftmost; on collinear take the farthest (drop middles).
let q = firstPointNotP;
for (const r of P) {
  const o = orient(p, q, r);
  if (o < 0) q = r;
  else if (o === 0 && dist2(p, r) > dist2(p, q)) q = r;
}
```
