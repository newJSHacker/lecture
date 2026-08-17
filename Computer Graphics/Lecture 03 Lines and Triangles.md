# Lecture 3 — Rasterizing lines and triangles in 2D

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `barycentric`, filled triangle  
**Board first:** three points, a pixel inside, weights α, β, γ

---


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computer Graphics/code/03-alpha-over.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — three points, a pixel inside, weights α, β, γ.
- Parked strip: `Lecture 3 | Rasterizing lines and triangles in 2D | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
three points, a pixel inside, weights α, β, γ
Triangle with α, β, γ labeled at a point.
Two triangles of a quad; shared edge.
Pixel-center grid overlay.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 2 |
| 10–25 | Lines: DDA, Bresenham idea |
| 25–55 | Triangles: half-planes vs barycentric |
| 55–65 | Fill rule and cracks |
| 65–75 | Bounding box as reject (link to CG AABB) |

---

## Learning goals

1. Rasterize a line without gaps (DDA is enough; Bresenham named).
2. Compute barycentric coordinates of a pixel wrt a triangle.
3. Fill a triangle using α, β, γ ≥ 0 and α+β+γ = 1 (with epsilon).
4. Explain a top-left fill rule in one sentence.
5. Interpolate a color (or any attribute) with barycentric weights.

---

## 1. Lines (15 min)

**DDA:** walk the longer axis, step the other by `dy/dx`. Round to pixels.

**Bresenham:** integer error term; mention; do not require the derivation.

Clip lines to the canvas (Cohen–Sutherland name only, or just reject endpoints outside and accept ugly clipped segments this week).

A line is **not** a thin triangle. Do not rasterize lines as triangles until they ask.

---

## 2. Barycentric coordinates (30 min)

Point p in triangle abc:

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

## 3. Fill rule (10 min)

Shared edges would be drawn twice (or leave holes) if both triangles claim the boundary.

**Top-left rule (teaching):** a pixel on an edge belongs to the triangle that owns the top edge or the left edge. Implement a simple version: `α ≥ 0, β ≥ 0, γ > 0` (strict on one weight) **or** document “we double-draw shared edges; z-buffer will hide it in 3D.”

Cracks = inconsistent edge tests or integer vs float pixel centers. Test at **pixel centers** `(x+0.5, y+0.5)`.

---

## 4. Bounding box (10 min)

Loop `x` from `floor(min(ax,bx,cx))` to `ceil(max(...))`, same for y. Clip to canvas. Same idea as AABB reject in computational geometry: the box is not the triangle.

---

## Live coding (60 min)

1. One triangle, vertices draggable (mouse in pixel space).
2. Fill with barycentric; RGB = (α, β, γ) * 255.
3. Draw the bounding box dashed.
4. Degenerate button: collinear vertices → no fill, no crash.

Script: drag a vertex across another; the triangle flips; signed area changes sign; if they used unsigned area, the fill dies. Prefer signed + `abs` in the denominator, or skip if area ≈ 0.

---

## Lab

1. `barycentric(p, a, b, c)` → `{a, b, g}` or `null`.
2. `fillTriangle(img, a, b, c, colorA, colorB, colorC)`.
3. A quad = two triangles. Shared edge must not crash.
4. Optional: DDA line for wireframe overlay.

Done when the centroid is the mix of the three vertex colors.

---

## Homework

1. Eight tests for barycentric: three vertices, centroid, clearly outside, on edge, degenerate.
2. Written: why pixel **centers**, not integer corners.
3. Written: relate `orient` / signed area to α.

---

## Quiz (10 min)

1. Barycentric of a vertex (say a)? (2 pts)
2. Barycentric of the centroid? (2 pts)
3. Degenerate triangle: what does the code do? (2 pts)
4. Why a bounding box loop is not enough without the inside test? (4 pts)

---

## Common mistakes

- Testing `α+β+γ === 1` in floats without epsilon, and rejecting everyone.
- Using vertex pixels as integers then testing integer corners (holes).
- `area` unsigned, then a CW triangle never fills.
- Nested loops over the **whole canvas** for every triangle (fine for one triangle; death for a mesh — box it).

---

## Board drawings

1. Triangle with α, β, γ labeled at a point.
2. Two triangles of a quad; shared edge.
3. Pixel-center grid overlay.


## Extra exercises

See [[Computer Graphics/exercises/Week 03]].
