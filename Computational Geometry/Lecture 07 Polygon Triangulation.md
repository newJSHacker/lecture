# Lecture 7 — Polygon triangulation

**Week 7 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** ear: convex tip + no other vertex in triangle(v−1,v,v+1); clip → n−2 triangles, O(n²); fail on bowtie  
**Success check:** a C-shape yields n−2 triangles that fill; a bowtie throws; they have the midterm list

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/07-jarvis.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: triangulate a simple polygon because GPUs want triangles | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
simple n-gon: n−2 triangles, n−3 diagonals
ear tip: convex AND no other vertex in the ear triangle
Meisters: n≥4 ⇒ at least two ears

isEar: orient convex (not reflex); point-in-TRIANGLE not PIP
holes: not handled     Chazelle O(n): name only

ear clip ≠ Delaunay     CDT: name; Week 11

split vs merge vertex: label on a drawing (midterm)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Induction: a diagonal splits; triangles add to n−2. A reflex vertex is never an ear tip — the diagonal would lie outside. Hand out the midterm list today: no Voronoi, no kd-tree, no DCEL on the paper.

**Ask:** How many triangles in a simple 10-gon? Wait. Want: 8. Diagonals: 7.

**Board:** parked strip. Then a concave polygon, one ear shaded, then the remaining polygon.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Polygon triangulation*.

**Do not:** Testing `isEar` without the convex-turn test (a reflex “ear” diagonal is outside).

### Minutes 10–12 — Frame

**Say:** y-monotone: two chains, O(n) after sort. Full pipeline: monotone split O(n log n) then linear — picture of start/end/split/merge/regular; do not require the sweep. Same point set can be a skinny ear-clip or a Delaunay preview.

**Ask:** Does ear clipping as taught handle holes?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Existence of a diagonal from an ear — draw it; write-up is homework.

**Board:** induction split. Ear with an interior point that invalidates it. Split/merge sketches. Skinny vs Delaunay.

**Say:** Midterm topics 1–11 on a handout. Degeneracy will appear.

**Ask:** Define ear tip.

**They do:** Induction n−2. A concave quad has two ears (not a convex n-gon).

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Step-mode ears: candidate highlighted; green legal / red point inside; faint clipped ears. C-shape: reflex refused, then accepted after a neighbor clips. Bowtie: clear error, not an infinite loop. Demo 11-ear-clip.html. Plant isEar without the convex-turn test. Plant PIP on whole P instead of the ear triangle.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** isEar for one index. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: earClip; number triangles; convex, C, 12-vertex room; bowtie throws. Homework: study the list. Quiz: counts, ear, O(n²), holes, vs Delaunay. Next week exam.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | n−2 on the board | They count a hexagon. |
| 15–40 | Clip a C | Reflex refused. |
| 40–50 | Fail a bowtie | No infinite loop. |
| 50–60 | Issue midterm list | Photograph. No DCEL on it. |

Point them at `Computational Geometry/code/07-jarvis.html` as the after-class check, not as the lecture.

---

## Lab

1. Implement `earClip`.
2. Draw diagonals and number triangles in clip order.
3. Inputs: convex, C-shape, a 12-vertex simple room.
4. Bowtie must throw.

---

## Homework

1. Implement ear clipping.
2. Written: induction that a simple n-gon has n − 2 triangles.
3. Written: define an ear. Give a polygon with exactly two ears (a convex quadrilateral is too easy; use a convex n-gon — it has n ears — so instead use a concave quad, which has two).
4. **Study** the midterm list below.

---

## Quiz next meeting (they hear this now)

1. How many triangles in a simple 10-gon? How many diagonals? (2 pts)
2. Define ear tip. (3 pts)
3. Ear clipping time? (2 pts)
4. Does ear clipping as taught handle holes? (1 pt)
5. Name one difference vs Delaunay. (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Why triangulate (15 min).** GPUs draw triangles. A filled polygon in a canvas, a font outline, a UI blob, a roof footprint — all become triangles.
**Theorem.** Every simple polygon with n ≥ 3 vertices has a triangulation: n − 2 triangles, n − 3 diagonals, using only existing vertices.
**Proof sketch (induction).**
n = 3: already a triangle.
n > 3: a simple polygon has a diagonal (exists; we will get one from an ear). A diagonal splits P into P1, P2 with n1 + n2 = n + 2 vertices (the two endpoints are shared). By induction, triangles = (n1 − 2) + (n2 − 2) = n − 2.
**Existence of a diagonal.** Every simple n > 3 polygon has at least three convex vertices. At least one of those is an **ear**: the diagonal between its neighbors lies inside P. Clipping that ear is a diagonal.
Do not spend the whole lecture on the existenc

**2. Ears (25 min).** Vertex vi is an **ear tip** if:
1. vi is convex (not reflex, not a skip of a flat-only policy),
2. the diagonal `v_{i-1} v_{i+1}` lies **inside** P,
3. equivalently: triangle `v_{i-1} v_i v_{i+1}` contains **no other vertex** of P.
Condition 3 is what we implement. Because P is simple, “no vertex inside the ear triangle” plus “vi convex” implies the diagonal is inside.
### Meisters’ theorem (state)
Every simple polygon with n ≥ 4 has at least two ears.
### Ear clipping
```
earClip(P):
    if not simple: fail
    V = cyclic list of vertices
    T = []
    while |V| > 3:
        found = false
        for each vi in V:
            if isEar(vi, V):
                T.append(triangle(v_{i-1}, vi, v_{i+1}))
                remove vi from V
                found = true
                break
      

**3. Monotone polygons (15 min).** A polygon is **y-monotone** if its boundary splits into two chains from the top vertex to the bottom vertex, and each chain is never-upward (or never-downward).
A y-monotone polygon can be triangulated in **O(n)** with a stack, similar in spirit to Andrew’s hull scan.
**Full O(n log n) pipeline:**
1. Add diagonals to split a simple polygon into y-monotone pieces (sweep, O(n log n)).
2. Triangulate each piece in linear time.
Teach step 1 as a picture: merge/split/start/end/regular vertices. Do **not** require the sweep implementation. Students should be able to **label** a vertex as split vs merge on a drawing.
| Vertex type | Local picture | Action (idea) |
| --- | --- | --- |
| Start | both neighbors below, interior below | new helper |
| End | both neighbors above, interior above | close

**4. Two different triangulations (10 min).** | | Polygon triangulation | Delaunay (Week 11) |
| --- | --- | --- |
| Input | a simple polygon (edges are constraints) | a point set |
| Edges | all boundary edges must appear | no boundary unless we add a hull |
| Quality | any triangulation is allowed | empty circumcircle |
| Use | fill a shape | well-shaped mesh, terrain |
**Constrained Delaunay** sits between them: respect given edges, maximize the Delaunay property elsewhere. Name it. Project option.
---

---

## Common mistakes

1. Testing `isEar` without the convex-turn test (a reflex “ear” diagonal is outside).
2. Forgetting the polygon is cyclic.
3. Using point-in-polygon on the whole P instead of point-in-triangle.
4. Infinite loop on a self-intersecting input.
5. Claiming any triangulation is Delaunay.

## If we run long, cut

Monotone sweep implementation. Keep ears + n−2 + the list.

## If we run short, add

Label one split vertex on a drawing.
