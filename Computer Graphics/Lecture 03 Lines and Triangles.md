# Lecture 3 — Rasterizing lines and triangles in 2D

**Week 3 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** barycentric(p,a,b,c); fill if α,β,γ ≥ −eps and area ≠ 0; test pixel centers  
**Success check:** they fill a triangle colored by αβγ and skip a collinear triple without crashing

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/03-alpha-over.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: a filled triangle from three pixel coordinates — the heart of the course | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
p = α a + β b + γ c
α+β+γ = 1
α,β,γ ≥ 0  ⇔  inside (boundary = policy)

α = area(pbc)/area(abc)     area = ½ cross(b−a, c−a)
if area ≈ 0: skip (degenerate)

test at (x+0.5, y+0.5)
bbox is a reject, not the triangle
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** GPUs fill triangles. Today we do it with signed area — the same cross as Computational Geometry’s orient. A line is not a thin triangle.

**Ask:** Barycentric of a vertex a? Wait. Want: (1,0,0).

**Board:** parked strip. Then three points, a pixel inside, weights α, β, γ.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`barycentric`, filled triangle*.

**Do not:** Testing `α+β+γ === 1` in floats without epsilon, and rejecting everyone.

### Minutes 10–12 — Frame

**Say:** DDA walks the long axis; Bresenham is named, not derived. Half-planes vs barycentric: we implement barycentric. Top-left fill rule: cracks otherwise. Course policy: α,β,γ ≥ −eps, or document double-draw and let z-buffer hide it in 3D. Same formula later for UV, n, z.

**Ask:** Why not loop the whole canvas for every triangle?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Signed area. Unsigned area kills a CW triangle. Prefer signed + abs in the denominator, or skip if area ≈ 0.

**Board:** triangle, a pixel, αβγ. Two triangles of a quad; shared edge. Pixel-center overlay.

**Say:** Bounding box = AABB reject, like computational geometry. The box is not the triangle.

**Ask:** Barycentric of the centroid? Want: (1/3,1/3,1/3).

**They do:** On paper: relate orient / signed area to α. Why pixel centers, not integer corners.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Draggable 2D triangle; RGB = αβγ*255; dashed bbox; degenerate button. Demo 04-barycentric.html. Plant unsigned area. Plant α+β+γ === 1 without eps, rejecting everyone.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** barycentric returning null if degenerate. Eight minutes. Tests: vertex, centroid, outside.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: barycentric + fillTriangle + a quad. Homework: eight tests including on-edge and degenerate. Quiz: vertex, centroid, degenerate policy, why bbox is not enough.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | DDA line stub | Do not rasterize lines as triangles. |
| 10–35 | Barycentric fill RGB=αβγ | Plant integer-corner tests → holes. |
| 35–50 | Drag through collinear | Must not crash. Signed area sign flip. |
| 50–60 | They fill a quad | Shared edge. Circulate. |

Point them at `Computer Graphics/code/03-alpha-over.html` as the after-class check, not as the lecture.

---

## Lab

1. `barycentric(p, a, b, c)` → `{a, b, g}` or `null`.
2. `fillTriangle(img, a, b, c, colorA, colorB, colorC)`.
3. A quad = two triangles. Shared edge must not crash.
4. Optional: DDA line for wireframe overlay.

---

## Homework

1. Eight tests for barycentric: three vertices, centroid, clearly outside, on edge, degenerate.
2. Written: why pixel **centers**, not integer corners.
3. Written: relate `orient` / signed area to α.

---

## Quiz next meeting (they hear this now)

1. Barycentric of a vertex (say a)? (2 pts)
2. Barycentric of the centroid? (2 pts)
3. Degenerate triangle: what does the code do? (2 pts)
4. Why a bounding box loop is not enough without the inside test? (4 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Lines (15 min).** **DDA:** walk the longer axis, step the other by `dy/dx`. Round to pixels.
**Bresenham:** integer error term; mention; do not require the derivation.
Clip lines to the canvas (Cohen–Sutherland name only, or just reject endpoints outside and accept ugly clipped segments this week).
A line is **not** a thin triangle. Do not rasterize lines as triangles until they ask.
---

**2. Barycentric coordinates (30 min).** Point p in triangle abc:
```
p = α a + β b + γ c
α + β + γ = 1
α, β, γ ≥ 0   ⇔   p inside (including boundary, policy)
```
Areas (signed):
```
α = area(pbc) / area(abc)
β = area(pca) / area(abc)
γ = area(pab) / area(abc)
```
Signed area in 2D is the same cross product as [[Computational Geometry/Lecture 01 What Computational Geometry Is]]:
```
area(abc) = 0.5 * cross(b-a, c-a)
```
If `area(abc) = 0`, the triangle is degenerate: skip it.
**Inside test:** α, β, γ all ≥ −eps and |α+β+γ − 1| small (they should already sum to 1 algebraically).
**Interpolation:**
```
color(p) = α color(a) + β color(b) + γ color(c)
```
Same formula for UV, normals, z (later).
---

**3. Fill rule (10 min).** Shared edges would be drawn twice (or leave holes) if both triangles claim the boundary.
**Top-left rule (teaching):** a pixel on an edge belongs to the triangle that owns the top edge or the left edge. Implement a simple version: `α ≥ 0, β ≥ 0, γ > 0` (strict on one weight) **or** document “we double-draw shared edges; z-buffer will hide it in 3D.”
Cracks = inconsistent edge tests or integer vs float pixel centers. Test at **pixel centers** `(x+0.5, y+0.5)`.
---

**4. Bounding box (10 min).** Loop `x` from `floor(min(ax,bx,cx))` to `ceil(max(...))`, same for y. Clip to canvas. Same idea as AABB reject in computational geometry: the box is not the triangle.
---

---

## Common mistakes

1. Testing `α+β+γ === 1` in floats without epsilon, and rejecting everyone.
2. Using vertex pixels as integers then testing integer corners (holes).
3. `area` unsigned, then a CW triangle never fills.
4. Nested loops over the **whole canvas** for every triangle (fine for one triangle; death for a mesh — box it).

## If we run long, cut

Bresenham derivation. Keep barycentric + degenerate skip.

## If we run short, add

Strict γ > 0 as a toy top-left rule.
