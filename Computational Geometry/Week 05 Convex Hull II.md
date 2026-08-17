# Week 5 — Convex hull II (Graham and Andrew)

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** Andrew’s monotone chain (required), Graham scan (explained)  
**Board first:** sort by x, build lower hull, build upper hull

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 4 |
| 10–30 | Graham scan |
| 30–55 | Andrew’s monotone chain, invariant, collinear policy |
| 55–65 | 3D hull preview (no code) |
| 65–75 | Graphics: AABB, OBB, culling |

---

## Learning goals

1. Explain Graham scan: sort by polar angle, then scan with a stack.
2. Implement Andrew’s algorithm correctly.
3. Handle duplicates and collinear points on the hull.
4. State O(n log n) time and why the scan is O(n) after sorting.
5. Name one 3D hull method and why it is harder.

---

## 1. Graham scan (20 min)

### Steps

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

If two points are collinear with p0, the nearer one is **not** a hull vertex (under our policy). Sorting nearer-first and using `<= 0` pops it.

### Complexity

Sort: O(n log n).  
Scan: each point is pushed once and popped at most once, O(n).  
**Total: O(n log n).**

---

## 2. Andrew’s monotone chain (25 min)

This is the algorithm students must implement. It avoids polar angles entirely.

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
```

### Invariant (lower hull)

The stack is a strictly left-turning chain from the leftmost to the current point. All processed points lie above or on it.

`<= 0` means: pop on right turns **and** on collinear, so we drop middle collinear points.

To **keep** collinear hull points, use `< 0` only.

### Why the scan is O(n)

Same stack argument as Graham: each point is pushed once per chain and popped at most once.

### Trace on the board

Seven points. Sort. Build lower (3–4 pops). Build upper. Concatenate. Count h.

### Andrew vs Graham vs Jarvis

| | Jarvis | Graham | Andrew |
| --- | --- | --- | --- |
| Time | Θ(n h) | O(n log n) | O(n log n) |
| Sort key | none | polar around p0 | (x, y) |
| Implementation risk | infinite loop | polar ties | off-by-one at join |
| Use when | h is tiny | teaching polar sort | **default in this course** |

---

## 3. 3D preview (10 min)

In 3D the hull is a convex polyhedron.

- **Gift wrapping** still works; a “step” is a face, and the search is over a 1D set of candidate edges. Time grows fast.
- **Incremental:** add a point, remove visible faces, sew the horizon. This is the usual textbook 3D algorithm.
- **Conflict graphs** make expected incremental construction O(n log n).

We will not implement 3D hulls. Graphics engines use them for collision hulls and for silhouette ideas. Students should know the output is a mesh of triangles, not a polygon.

---

## 4. Graphics connections (10 min)

| Structure | How it uses a hull |
| --- | --- |
| AABB | hull of the 4 (or 8 in 3D) extreme coordinates; cheaper, looser |
| OBB | oriented box; a cheap approximation of the 2D hull |
| Broad-phase collision | if hulls (or AABBs) miss, objects miss |
| Camera / frustum | a 2D analog is “is this sprite’s hull on screen?” |
| Shadow / silhouette | extreme points in a light direction (supporting line) |

Live sentence: Jarvis is one supporting line after another. A directional extreme query is one step of Jarvis.

---

## Live coding (60 min)

Implement Andrew with the stack drawn.

Draw:

- sorted index next to each point
- lower hull in blue, growing
- upper hull in red, growing
- popped points flashing
- final polygon filled

Step keys as in Week 4.

Then run the same n = 10_000 cloud and circle as Week 4. Andrew should not care that h = n.

---

## Lab

1. Implement Andrew.
2. Compare with last week’s Jarvis on:
   - random cloud n = 10_000
   - circle n = 2_000
3. Toggle policy: drop vs keep collinear. Show a 4-point collinear top edge.
4. Unit tests: n = 0,1,2; triangle; all-collinear; square with a point in the middle.

Done when all-collinear returns the two endpoints only (drop policy).

---

## Homework

1. Implement Andrew (or Graham if you justify polar compare without `atan2`).
2. Document the collinear policy in the README.
3. Written: prove the scan is O(n) after sorting (each index pushed/popped ≤ once per chain).
4. Written: one paragraph on AABB vs convex hull as a collision proxy. When is the AABB good enough?

---

## Quiz (10 min)

1. What is the sort key in Andrew? (2 pts)
2. Why is the while-loop total O(n)? (2 pts)
3. What does `orient <= 0` do to collinear hull points? (2 pts)
4. Give one case where Jarvis beats Andrew. (2 pts)
5. Name one 3D hull strategy. (2 pts)

---

## Common mistakes

- Forgetting to unique-sort; then `<= 0` pops everything because consecutive duplicates are collinear with anything.
- Concatenating lower and upper without removing the duplicated endpoints → a zero-length edge and a later crash.
- Building both chains left-to-right with the same orientation test, so one chain turns the wrong way.
- Using `atan2` in Graham and failing the left-half vs right-half.

---

## Board drawings

1. Graham polar sort around p0.
2. Andrew: sorted list, lower stack, upper stack, join.
3. AABB vs true hull around a diagonal stick (AABB is huge; hull is tight).

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 05]] · Demo: [08-andrew.html](code/08-andrew.html)

1. Why is the scan O(n) after sorting?
2. Lower-hull condition: write `while |h| ≥ 2 and orient(h[-2], h[-1], p) <= 0`. What does `<= 0` drop?
3. Oracle: Andrew vertex set equals Jarvis vertex set (rotation allowed).
4. Collinear bottom edge of 5 points + one apex. Hull size 3.

```js
function build(seq) {
  const h = [];
  for (const p of seq) {
    while (h.length >= 2 && orient(h.at(-2), h.at(-1), p) <= 0) h.pop();
    h.push(p);
  }
  return h;
}
```
