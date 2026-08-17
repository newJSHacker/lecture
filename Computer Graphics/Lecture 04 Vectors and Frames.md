# Lecture 4 — Vectors, points, and frames

**Week 4 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** vec3: dot, cross, normalize, add, sub, scale; point ≠ vector; 2D cross = signed area  
**Success check:** they refuse p+q, get a vector from p−q, and rotate a 2D point with a 2×2 matrix

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/04-barycentric.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: the math they thought they knew, now tied to a renderer | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
point  w=1   affine M
vector w=0   linear part (no t)
normal       (M⁻¹)ᵀ   (Week 6/10)

dot: |a||b|cosθ     Lambert will be n·l
cross 3D: RH perpendicular
2D cross: ax by − ay bx   =  orient’s kernel

normalize(0) → policy, not NaN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Last week signed area filled a triangle. That was a 2D cross. Today points are not arrows. Adding two points is a type error until you meant a midpoint.

**Ask:** Point minus point is a …? Wait. Want: vector.

**Board:** parked strip. Then a point is not an arrow.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`vec3` (`dot`, `cross`, `normalize`, `add`, `sub`, `scale`)*.

**Do not:** Normalizing in place and reusing the zero vector.

### Minutes 10–12 — Frame

**Say:** A frame is origin plus axes. M’s columns (column vectors) are object axes and origin in world. Do not drown in abstract LA. One picture: a cube’s local x drawn in the world. slerp is not this week; lerp of points along a segment is homework.

**Ask:** Do normals transform with M? Want: no — normal matrix.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** orient(a,b,c) is sign(cross(b−a,c−a)). Same algebra as Comp Geo.

**Board:** point vs vector. RH cross. Object axes in the world.

**Say:** Zero vector: do not divide. Skip or return (0,1,0) and document it.

**Ask:** 2D cross of (2,0) and (0,3)? Want: 6.

**They do:** On paper: why p+q is meaningless. RH rule for cross(i,j).

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Orbit a point with cos/sin, then 2×2 matrix — same picture. Draw i,j after rotation. Console: dot orthogonal = 0, cross(i,j)=k. Demo 06-vec3.html. Plant left-handed cross ‘until it looks right.’

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** normalize and a test that (0,0,0) is not NaN. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: vec3.js tests + draggable vector. Homework: lerp of points; written p+q. Quiz: p−p, unit dot, 2D cross, normals vs M.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Point vs vector on the board | Plant p+q as midpoint without ½. |
| 15–40 | cos/sin then matrix | Same picture or the matrix is wrong. |
| 40–50 | cross(i,j)=k | Plant swapped args. |
| 50–60 | They write normalize | Zero policy. Circulate. |

Point them at `Computer Graphics/code/04-barycentric.html` as the after-class check, not as the lecture.

---

## Lab

1. `dot((1,0,0),(0,1,0)) === 0`
2. `cross((1,0,0),(0,1,0)) === (0,0,1)`
3. `normalize((0,0,0))` does not return NaN
4. `sub` of two points is a vector; adding a point and a vector is a point (document in comments)

---

## Homework

1. `vec3` tests as above plus `lerp(a, b, t)` for **points**.
2. Written: why `p + q` for two points is meaningless (unless you secretly meant midpoint with 1/2).
3. Written: right-hand rule for `cross(i, j)`.

---

## Quiz next meeting (they hear this now)

1. Point minus point is a …? (2 pts)
2. `dot` of two unit vectors is …? (2 pts)
3. 2D cross of (2,0) and (0,3)? (2 pts)
4. Do normals transform with M? Yes/no and the correct name. (4 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Types (20 min).** | Object | Homogeneous w | Transforms with |
| --- | --- | --- |
| Point | 1 | Affine matrix M |
| Vector / direction | 0 | Linear part of M (no translation) |
| Normal | — | `transpose(inverse(M))` on the 3×3 (Week 6/10) |
Normals are not directions. Scaling an ellipse does not scale its normals the same way. Draw this; implement the normal matrix when lighting starts.
Computational geometry’s `orient(a,b,c)` is `sign(cross(b-a, c-a))`. Same algebra.
---

**2. Products (20 min).** **Dot:** `a·b = |a||b|cosθ`. Projection; Lambert will be `n·l`.
**Cross (3D):** perpendicular to both; direction by right-hand rule. `|a×b| = |a||b|sinθ`.
**2D cross** (scalar): `ax by − ay bx`.
Unit vector: `normalize(v) = v / |v|`. Zero vector: do not divide; return a policy (skip the vertex, or `(0,1,0)`).
---

**3. Frames (15 min).** A frame is an origin plus three axes. Object space is a frame. World space is a frame. The model matrix **is** the object frame written in world coordinates (columns = axes and translation, for column vectors).
Change of basis: coordinates in frame B from coordinates in frame A via the matrix whose columns are A’s axes in B.
Do not drown them in abstract linear algebra. One picture: a cube’s local x-axis drawn in the world.
---

---

## Common mistakes

1. Normalizing in place and reusing the zero vector.
2. Left-handed cross by swapping arguments “until the cube looks right.”
3. Treating RGB as a vector space for lighting this week (wait for Week 10).

## If we run long, cut

Normal-matrix derivation. Keep types + 2×2 rotate.

## If we run short, add

Orthonormal basis from look+up as a name — Week 7 lookAt.
