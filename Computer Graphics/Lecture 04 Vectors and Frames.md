# Lecture 4 — Vectors, points, and frames

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `vec3` (`dot`, `cross`, `normalize`, `add`, `sub`, `scale`)  
**Board first:** a point is not an arrow

---


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computer Graphics/code/04-barycentric.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — a point is not an arrow.
- Parked strip: `Lecture 4 | Vectors, points, and frames | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
a point is not an arrow
Point vs vector.
Cross product right-hand rule.
Object axes drawn in the world.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 3 |
| 10–30 | Points, vectors, normals |
| 30–50 | Dot, cross, bases |
| 50–65 | Frames and change of basis |
| 65–75 | 2D rotation two ways: trig vs matrix |

---

## Learning goals

1. Refuse to add two points; subtract points to get a vector.
2. Compute dot and 3D cross; interpret 2D cross as signed area.
3. Build a right-handed orthonormal basis from a look direction and an up hint.
4. Say what a coordinate frame is.
5. Rotate a 2D point with a matrix.

---

## 1. Types (20 min)

| Object | Homogeneous w | Transforms with |
| --- | --- | --- |
| Point | 1 | Affine matrix M |
| Vector / direction | 0 | Linear part of M (no translation) |
| Normal | — | `transpose(inverse(M))` on the 3×3 (Week 6/10) |

Normals are not directions. Scaling an ellipse does not scale its normals the same way. Draw this; implement the normal matrix when lighting starts.

Computational geometry’s `orient(a,b,c)` is `sign(cross(b-a, c-a))`. Same algebra.

---

## 2. Products (20 min)

**Dot:** `a·b = |a||b|cosθ`. Projection; Lambert will be `n·l`.

**Cross (3D):** perpendicular to both; direction by right-hand rule. `|a×b| = |a||b|sinθ`.

**2D cross** (scalar): `ax by − ay bx`.

Unit vector: `normalize(v) = v / |v|`. Zero vector: do not divide; return a policy (skip the vertex, or `(0,1,0)`).

---

## 3. Frames (15 min)

A frame is an origin plus three axes. Object space is a frame. World space is a frame. The model matrix **is** the object frame written in world coordinates (columns = axes and translation, for column vectors).

Change of basis: coordinates in frame B from coordinates in frame A via the matrix whose columns are A’s axes in B.

Do not drown them in abstract linear algebra. One picture: a cube’s local x-axis drawn in the world.

---

## Live coding (60 min)

1. Draw a 2D origin and a point p.
2. Rotate p with `cos/sin`.
3. Rotate p with a 2×2 matrix. Identical.
4. Draw `i` and `j` after rotation (the frame).
5. Unit tests in the console: `dot` orthogonal = 0, `cross` of i,j = k.

---

## Lab

Implement `vec3.js` with tests:

- `dot((1,0,0),(0,1,0)) === 0`
- `cross((1,0,0),(0,1,0)) === (0,0,1)`
- `normalize((0,0,0))` does not return NaN
- `sub` of two points is a vector; adding a point and a vector is a point (document in comments)

Visualizer: draggable 2D vector, show length and a unit arrow.

---

## Homework

1. `vec3` tests as above plus `lerp(a, b, t)` for **points**.
2. Written: why `p + q` for two points is meaningless (unless you secretly meant midpoint with 1/2).
3. Written: right-hand rule for `cross(i, j)`.

---

## Quiz (10 min)

1. Point minus point is a …? (2 pts)
2. `dot` of two unit vectors is …? (2 pts)
3. 2D cross of (2,0) and (0,3)? (2 pts)
4. Do normals transform with M? Yes/no and the correct name. (4 pts)

---

## Common mistakes

- Normalizing in place and reusing the zero vector.
- Left-handed cross by swapping arguments “until the cube looks right.”
- Treating RGB as a vector space for lighting this week (wait for Week 10).

---

## Board drawings

1. Point vs vector.
2. Cross product right-hand rule.
3. Object axes drawn in the world.


## Extra exercises

See [[Computer Graphics/exercises/Week 04]].
