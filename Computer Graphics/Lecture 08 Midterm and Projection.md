# Lecture 8 — Midterm and perspective projection

**Time:** 60–75 min midterm, then 30–45 min lecture + remaining live coding  
**New kernel:** `perspective`, `ortho`  
**Lab:** cube that foreshortens

Hand out the **midterm topic list at the end of Week 7**. No new project work this week except keeping notes.

---


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. This meeting includes a **midterm**. Say that at the door.

## Before you enter

- Demo: `Computer Graphics/code/08-rotate-center.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — today's picture.
- Parked strip: `Lecture 8 | Midterm and perspective projection | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
Frustum vs ortho box.
Similar triangles: smaller when farther.
Clip `w` as “the z that perspective needs.”
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Midterm (60–75 min)

Written. No laptop. 100 points.

### Suggested paper

**Q1. Pipeline (16 pts)**  
Six spaces in order. Which multiply is `P * V * M`? Canvas origin vs world origin.

**Q2. Color / raster (16 pts)**  
`over` formula. Barycentric of the centroid. Pixel centers.

**Q3. Vectors and matrices (24 pts)**  
Point vs vector (`w`). `T R` vs `R T`. Rotate about c. One 2×2 rotation by hand.

**Q4. Scene graph (20 pts)**  
Three-node chain; world matrix of the leaf. What M means.

**Q5. Camera (24 pts)**  
`lookAt` inputs. `V * eye`. Degenerate up. Why normals need a different matrix (name only).

### Grading note

Partial credit for a correct picture with a wrong name. No credit for “the GPU does it” on a space question.

---

## Lecture — Projection (remainder)

### Orthographic

Box to clip cube. No foreshortening. UI, CAD, debug.

### Perspective

Frustum: `fov` (vertical, radians), `aspect`, `near`, `far`.

Teaching matrix (OpenGL-style clip, column vectors) — write it once, test with a point on the center line:

```
sy = 1 / tan(fov/2)
sx = sy / aspect

P = [[sx, 0,  0,  0],
     [0,  sy, 0,  0],
     [0,  0,  a,  b],
     [0,  0, -1,  0]]
```

with `a`, `b` from near/far (derive or quote Shirley / Scratchapixel). The last row `(0,0,−1,0)` copies −z into `w` so divide later does perspective.

**Do not divide by w today in a vertex shader story.** Divide is Week 9. Today: build P, multiply, **look at clip.w**.

Near > 0. Far > near. `near = 0` is forbidden.

---

## Live coding

1. `ortho(l,r,b,t,n,f)` and `perspective(fov, aspect, n, f)`.
2. Course cube, M = identity, V = lookAt, P = perspective.
3. Toggle ortho.
4. Print `p_clip` for one vertex.

If the cube is behind the camera, V is wrong — do not “fix” P.

---

## Lab

1. Implement `perspective` with a unit test: a point on the camera’s look axis has ndc.x ≈ 0 after divide (Week 9 can finish divide; this week you may divide in JS for the test).
2. Slider fov. Cube must grow when fov shrinks.
3. Aspect from canvas width/height.

Done when ortho looks like a flat engineering drawing and perspective recedes.

---

## Homework

1. Written: why far/near too huge hurts depth (tease Week 9).
2. Code: `ortho` + toggle.
3. Midterm reflection optional: one mistake you will not repeat.

---

## Quiz

None (midterm week). Next quiz is Week 9 on projection + last week’s camera.

---

## Common mistakes

- fov in degrees passed to `tan`.
- aspect = height/width.
- P with +1 in the w-row while looking down −Z, inconsistent with V.

---

## Board drawings

1. Frustum vs ortho box.
2. Similar triangles: smaller when farther.
3. Clip `w` as “the z that perspective needs.”


## Extra exercises

See [[Computer Graphics/exercises/Week 08]].
