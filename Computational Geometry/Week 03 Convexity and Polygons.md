# Week 3 — Convexity and polygons

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** polygon classifier + shoelace area  
**Board first:** convex set vs convex polygon vs simple polygon

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 2 |
| 10–25 | Convex sets and convex combinations |
| 25–45 | Polygon taxonomy |
| 45–60 | Same-turn test and supporting lines |
| 60–75 | Shoelace formula; why algorithms assume simple |

---

## Learning goals

1. Define a convex set and a convex combination.
2. Classify a polygon as convex, simple concave, or self-intersecting.
3. Use the all-turns-same-orientation test.
4. Compute signed area with the shoelace formula.
5. Explain why most algorithms this semester assume a **simple** polygon.

---

## 1. Convex sets (15 min)

A set S ⊆ ℝ² is **convex** if for every pair of points p, q in S, the whole segment pq lies in S.

A **convex combination** of points p1…pk is

```
λ1 p1 + … + λk pk
  where λi ≥ 0 and λ1 + … + λk = 1
```

The **convex hull** of a set is the set of all convex combinations of its points. That sentence is the definition we will use again in Week 4.

Draw:

- a disk (convex)
- a banana (not convex: the chord leaves the set)
- a triangle (convex)
- a star polygon (not convex)

**Supporting line:** a line L through the boundary of S such that S lies entirely in one closed half-plane of L. Convex sets have a supporting line at every boundary point. This is the geometric engine of gift wrapping.

---

## 2. Polygon taxonomy (20 min)

A polygon is a closed chain of n ≥ 3 vertices.

| Name | Meaning |
| --- | --- |
| Simple | edges meet only at shared endpoints; no self-crossings |
| Convex | simple, and the interior is a convex set |
| Concave (non-convex) | simple, but at least one reflex vertex |
| Complex / self-intersecting | edges cross (bowtie, star) |
| Weakly simple | touches itself but does not cross (mention only) |

A **reflex vertex** has interior angle > 180°. Equivalently, the turn at that vertex has the **opposite** orientation from the polygon’s overall orientation.

### How to get the overall orientation

Signed area (Section 4). Positive ⇒ CCW in our convention. Then a vertex i is reflex iff

```
orient(v_{i-1}, v_i, v_{i+1})
```

disagrees with that sign.

### Pictures (draw all four)

1. Convex hexagon
2. Concave “C”
3. Bowtie (two triangles sharing a crossing)
4. Regular star {5/2}

Ask: which of our later algorithms may run on each?  
Answer: hull of the **vertices** always exists. Ear clipping and even–odd filling assume simple. Self-intersecting polygons must be rejected or repaired.

---

## 3. The same-turn test (15 min)

**Theorem (teaching statement).**  
A simple polygon is convex if and only if every consecutive triple `v_{i-1}, v_i, v_{i+1}` has the same orientation, and that orientation is nonzero (no 180° flat vertex, or we treat flat as allowed by policy).

**Proof sketch (board).**

(⇒) If the polygon is convex, each interior angle is ≤ 180°, so each turn is a left turn if the polygon is CCW (or each is a right turn if CW).

(⇐) If every turn has the same sign, the polygon is locally convex. For a **simple** polygon this implies the interior is a convex set: any chord between two vertices that left the interior would force a reflex chain. (Do not pretend this is a full proof without simplicity. The bowtie has consistent turns on each triangle and is not a convex polygon.)

**Course policy on collinear vertices:**

- `FLAT` is allowed in the convex class if you document it.
- For hulls next week we will drop or keep them explicitly.

### Algorithm

```
classify(P):
    if n < 3: return INVALID
    if any non-adjacent edges intersect properly: return SELF_INTERSECTING
    sign = 0
    for i in 0..n-1:
        o = orient(v[i-1], v[i], v[i+1])
        if o == 0: continue   // flat, by policy
        if sign == 0: sign = o
        else if o != sign: return SIMPLE_CONCAVE
    return CONVEX
```

Intersection of non-adjacent edges uses Week 2. Adjacent edges share a vertex and must not be reported as `proper`.

---

## 4. Shoelace formula (15 min)

For a polygon with vertices v0…v_{n-1}:

```
2A = Σ_{i=0}^{n-1} (v_i.x * v_{i+1}.y - v_{i+1}.x * v_i.y)
```

with `v_n = v_0`.

Then `A` is the **signed** area. `|A|` is the geometric area.

Derivation: sum of signed areas of triangles `(origin, v_i, v_{i+1})`. The origin cancels; any origin works.

**Uses:**

- orientation of the polygon (sign of A)
- reflex-vertex test
- later: ear clipping needs a consistent interior

If A = 0 the polygon is degenerate (collapsed).

---

## 5. Why “simple” is a precondition (rest of lecture)

Write a table and leave it up for the rest of the semester.

| Algorithm | Needs simple? | Needs convex? |
| --- | --- | --- |
| Point in polygon (even–odd) | yes, or define a fill rule | no |
| Ear clipping | yes | no |
| Convex hull of vertices | no | output is convex |
| SAT collision | yes | yes (convex pieces) |
| DCEL overlay | no crossings, or split them | no |

Graphics connection: a UI shape or a font outline that self-intersects will triangulate into garbage. Blender / SVG / glTF all silently assume almost-simple input. This course will **reject** self-intersection in the classifier rather than guess.

---

## Live coding (60 min)

User draws a polygon by clicking, Enter to close.

Show:

- signed area and CW/CCW
- each vertex colored: green convex, orange reflex, gray flat
- label: `CONVEX` / `SIMPLE_CONCAVE` / `SELF_INTERSECTING`
- faint convex hull of the vertices (call a stub; real hull is Week 4–5)

Drag a vertex of a convex hexagon until it becomes reflex. Students should see the label flip.

Then drag two non-adjacent edges across each other and show `SELF_INTERSECTING`.

---

## Lab

1. Implement `classify(polygon)` with the algorithm above.
2. Implement shoelace and display area.
3. Highlight reflex vertices.
4. Required drawings: convex, C-shape, bowtie, one with a flat vertex.

Done when the bowtie is not reported as convex.

---

## Homework

1. Written proof, 1 page: “A simple polygon is convex iff every turn has the same orientation.” Use the (⇒) direction fully. For (⇐) give the idea and state that simplicity is required. Draw the bowtie as a counterexample without simplicity.
2. Code: classifier + 6 fixtures (the four drawings plus n=3 and a duplicate-vertex square).
3. Compute by hand the shoelace area of (0,0), (4,0), (4,3), (0,3).

---

## Quiz (10 min)

1. Define convex set in one sentence. (2 pts)
2. Is a star polygon simple? Convex? (2 pts)
3. A 5-gon has turns +, +, −, +, +. Simple. Classification? (2 pts)
4. Shoelace of (0,0), (2,0), (0,2). Signed area? (2 pts)
5. Why does the same-turn test need simplicity? (2 pts)

---

## Common mistakes

- Calling any non-convex polygon “complex.”
- Using interior angles in degrees instead of `orient`.
- Testing adjacent edges for proper intersection and marking a valid polygon as self-intersecting.
- Absolute area only, then losing CW/CCW.
- Treating a bowtie as two convex polygons without splitting at the crossing.

---

## Board drawings

1. Convex set definition (segment stays inside).
2. Four-polygon taxonomy.
3. One reflex vertex with the two incident edges and a marked interior.
4. Shoelace as sum of signed triangles from the origin.
