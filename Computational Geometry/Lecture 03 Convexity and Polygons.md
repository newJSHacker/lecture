# Lecture 3 — Convexity and polygons

**Week 3 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** classify: SELF_INTERSECTING | SIMPLE_CONCAVE | CONVEX via same-turn + non-adjacent proper intersects; shoelace signed area  
**Success check:** a bowtie is not convex; a C-shape is simple concave; reflex vertices light up; signed area gives CW/CCW

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/03-segments.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: say whether a polygon is convex, simple, or neither, and why algorithms care | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
convex set: segment pq stays inside
convex polygon: simple AND interior convex
reflex: interior >180°  ⇔  turn disagrees with sign(A)

simple + all turns same sign  ⇔  convex
bowtie: consistent turns on each lobe, not a convex polygon
        (simplicity required)

2A = Σ (xi yi+1 − xi+1 yi)     sign(A) = orientation
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** A UI blob or a font outline that self-intersects triangulates into garbage. We reject self-intersection rather than guess. Interior angles in degrees are the wrong primitive — use orient.

**Ask:** Is a star polygon simple? Convex? Wait. Want: usually neither (not simple).

**Board:** parked strip. Then convex set vs convex polygon vs simple polygon.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *polygon classifier + shoelace area*.

**Do not:** Calling any non-convex polygon “complex.”.

### Minutes 10–12 — Frame

**Say:** Hull of vertices always exists. Ear clipping and even–odd assume simple. SAT needs convex pieces. Adjacent edges share a vertex — do not mark them proper. FLAT vertices: document; allowed in convex by policy. Table stays up all semester: which algorithms need simple / convex.

**Ask:** Why does the same-turn test need simplicity?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Convex combination; hull is all convex combinations — Week 4 will reuse that sentence.

**Board:** segment stays inside. Four-polygon taxonomy. Reflex vertex. Shoelace as signed triangles from the origin.

**Say:** (⇒) interior ≤180°. (⇐) local convexity; without simplicity the bowtie is the counterexample. Do not pretend a full proof.

**Ask:** Shoelace of (0,0),(2,0),(0,2). Signed area?

**They do:** 1-page proof sketch: simple ⇔ same-turn for convexity; draw the bowtie.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Click polygon, Enter to close. Signed area, CW/CCW. Vertices green/orange/gray. Label CONVEX / SIMPLE_CONCAVE / SELF_INTERSECTING. Drag a hexagon until reflex; then cross non-adjacent edges. Demo 06-shoelace.html. Plant testing adjacent edges as proper. Plant |A| only, losing CW/CCW.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** shoelace. Eight minutes. Hand: (0,0),(4,0),(4,3),(0,3).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: classify + reflex highlight; fixtures convex, C, bowtie, flat. Homework: six fixtures including n=3 and duplicate-vertex square. Quiz: convex set, star, mixed turns, shoelace, why simplicity.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Convex set pictures | Union of convex is not always convex. |
| 15–40 | Classifier live | Bowtie must not be CONVEX. |
| 40–50 | Shoelace sign | Reverse vertices → flip sign. |
| 50–60 | They close a C-shape | Circulate. |

Point them at `Computational Geometry/code/03-segments.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement `classify(polygon)` with the algorithm above.
2. Implement shoelace and display area.
3. Highlight reflex vertices.
4. Required drawings: convex, C-shape, bowtie, one with a flat vertex.

---

## Homework

1. Written proof, 1 page: “A simple polygon is convex iff every turn has the same orientation.” Use the (⇒) direction fully. For (⇐) give the idea and state that simplicity is required. Draw the bowtie as a counterexample without simplicity.
2. Code: classifier + 6 fixtures (the four drawings plus n=3 and a duplicate-vertex square).
3. Compute by hand the shoelace area of (0,0), (4,0), (4,3), (0,3).

---

## Quiz next meeting (they hear this now)

1. Define convex set in one sentence. (2 pts)
2. Is a star polygon simple? Convex? (2 pts)
3. A 5-gon has turns +, +, −, +, +. Simple. Classification? (2 pts)
4. Shoelace of (0,0), (2,0), (0,2). Signed area? (2 pts)
5. Why does the same-turn test need simplicity? (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Convex sets (15 min).** A set S ⊆ ℝ² is **convex** if for every pair of points p, q in S, the whole segment pq lies in S.
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

**2. Polygon taxonomy (20 min).** A polygon is a closed chain of n ≥ 3 vertices.
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
2. Co

**3. The same-turn test (15 min).** **Theorem (teaching statement).**  
A simple polygon is convex if and only if every consecutive triple `v_{i-1}, v_i, v_{i+1}` has the same orientation, and that orientation is nonzero (no 180° flat vertex, or we treat flat as allowed by policy).
**Proof sketch (board).**
(⇒) If the polygon is convex, each interior angle is ≤ 180°, so each turn is a left turn if the polygon is CCW (or each is a right turn if CW).
(⇐) If every turn has the same sign, the polygon is locally convex. For a **simple** polygon this implies the interior is a convex set: any chord between two vertices that left the interior would force a reflex chain. (Do not pretend this is a full proof without simplicity. The bowtie has consistent turns on each triangle and is not a convex polygon.)
**Course policy on collinear 

**4. Shoelace formula (15 min).** For a polygon with vertices v0…v_{n-1}:
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

**5. Why “simple” is a precondition (rest of lecture).** Write a table and leave it up for the rest of the semester.
| Algorithm | Needs simple? | Needs convex? |
| --- | --- | --- |
| Point in polygon (even–odd) | yes, or define a fill rule | no |
| Ear clipping | yes | no |
| Convex hull of vertices | no | output is convex |
| SAT collision | yes | yes (convex pieces) |
| DCEL overlay | no crossings, or split them | no |
Graphics connection: a UI shape or a font outline that self-intersects will triangulate into garbage. Blender / SVG / glTF all silently assume almost-simple input. This course will **reject** self-intersection in the classifier rather than guess.
---

---

## Common mistakes

1. Calling any non-convex polygon “complex.”
2. Using interior angles in degrees instead of `orient`.
3. Testing adjacent edges for proper intersection and marking a valid polygon as self-intersecting.
4. Absolute area only, then losing CW/CCW.
5. Treating a bowtie as two convex polygons without splitting at the crossing.

## If we run long, cut

Weakly-simple. Keep taxonomy + same-turn + shoelace.

## If we run short, add

Intersection of two convex sets is convex — one picture.
