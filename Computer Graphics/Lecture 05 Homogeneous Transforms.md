# Lecture 5 — Homogeneous coordinates and affine transforms

**Week 5 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** mat4 multiply; T, Rx/Ry/Rz, S; T(c) R T(−c) about a center; w=1 vs w=0  
**Success check:** they can rotate a triangle about its centroid and say T R ≠ R T

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/05-quad.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: 4×4 so translation and (later) projection share one multiply | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
[ L  t ] [ x ]   [ Lx + t ]
[ 0  1 ] [ 1 ] = [   1    ]

column vectors: nearest matrix acts first
T * R * p     rotate about origin, then translate
R * T * p     translate, then orbit the origin

about c:  T(c) * R * T(−c) * p

T(t)⁻¹ = T(−t)    R⁻¹ = Rᵀ    S(s)⁻¹ = S(1/s)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** A 3×3 cannot translate. Homogeneous w=1 is a point; w=0 is a direction so t does not apply. Composition order is the whole of scene graphs next week.

**Ask:** Does T R equal R T? Wait. Want: no.

**Board:** parked strip. Then rotate-then-translate vs translate-then-rotate.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`mat4` multiply, `translate`, `rotateX/Y/Z`, `scale`*.

**Do not:** Row-major storage but column-vector formulas (document `m[col*4+row]` vs `m[row*4+col]` and **pick one**).

### Minutes 10–12 — Frame

**Say:** Draw Ry on the board. Confirm with (1,0,0) at small +θ. If Three.js disagrees later, the matrix drifted — fix the matrix, do not flip θ in five places. Row-vector APIs reverse the product; we do not use them. Document m[col*4+row] vs row-major and pick one.

**Ask:** w for a direction?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Affine = Lx + t. Homogeneous packs it.

**Board:** T R vs R T on a stick figure. Homogeneous columns. Three arrows for rotate-about-c.

**Say:** Inverse of a matrix with translation is not a transpose.

**Ask:** How do you rotate about c?

**They do:** By hand: 2×2 rotate (1,0) by 90°. Then T(1,0,0)*p for p=(0,0,0,1).

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** mul, mulVec. Triangle at origin, Ry slider. Offset it — swings around origin. Then T(c) R T(−c) about centroid. Print the matrix. Demo 07-mat4-order.html and 08-rotate-center.html. Plant translating after a fake P.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** rotateY of a point. Eight minutes. Write the expected vector from the board into the test.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: mat4 identity/mul/translate/rotateY/scale; rotate-about-center; A-vs-B button. Homework: rotateX/Z; why w=0. Quiz: write T, TR vs RT, about c, w.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | T as last column | Plant transposing a T to invert. |
| 15–40 | T*R vs R*T animation | They must see they differ. |
| 40–55 | About centroid | Clap when it works. |
| 55–60 | They toggle order | Circulate. |

Point them at `Computer Graphics/code/05-quad.html` as the after-class check, not as the lecture.

---

## Lab

1. `mat4.js`: `identity`, `mul`, `translate`, `rotateY`, `scale`.
2. Rotate-about-center on the Week 3 triangle.
3. Tests: `T * T⁻¹ = I` within epsilon; `R(90°) * (1,0,0)` ≈ `(0,0,−1)` or whatever **your** Ry does — write the expected vector in the test from the board.

---

## Homework

1. By hand: 2×2 rotation of (1,0) by 90°. Then one 4×4 `T(1,0,0) * p` for p=(0,0,0,1).
2. Code: `rotateX`, `rotateZ`.
3. Written: why directions use w=0.

---

## Quiz next meeting (they hear this now)

1. Write T(1,2,3) (you may write “identity plus last column”). (3 pts)
2. Does `T R` equal `R T`? (2 pts)
3. How do you rotate about c? (3 pts)
4. w for a direction? (2 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Affine and homogeneous (15 min).** An affine transform is linear part plus translation:
```
x' = L x + t
```
Homogeneous:
```
[ L  t ] [ x ]   [ Lx + t ]
[ 0  1 ] [ 1 ] = [   1    ]
```
Directions use `w = 0` so t does not apply. Lights-as-directions and view rays need this.
---

**2. Building blocks (25 min).** **Translate** `T(t)`: identity, last column `t` (column-vector convention).
**Scale** `S(sx,sy,sz)`: diagonal.
**Rotate** about a coordinate axis: 2D rotation block in the other two axes. Right-handed: positive `rotateY` turns from +Z toward +X? **Draw it.** Standard:
```
Ry(θ) = [[ cosθ, 0, sinθ, 0],
         [ 0,    1, 0,    0],
         [-sinθ, 0, cosθ, 0],
         [ 0,    0, 0,    1]]
```
Confirm with a point `(1,0,0)` at small positive θ. If the picture disagrees with Three.js later, the convention drifted — fix the matrix, do not flip θ in five places.
---

**3. Order (15 min).** Column vectors: **the matrix nearest the point acts first.**
```
T * R * p   // rotate around origin, then translate
R * T * p   // translate, then rotate around origin (orbits)
```
About an arbitrary point c:
```
T(c) * R * T(-c) * p
```
This is the lab.
Row-vector APIs (old D3D) reverse the product. We do not use them.
---

**4. Inverses (10 min).** - `T(t)⁻¹ = T(-t)`
- `R⁻¹ = Rᵀ` (rotation)
- `S(s)⁻¹ = S(1/s)` if s ≠ 0
- Non-uniform scale + rotation: inverse is not “invert each and reverse” unless you remember `(AB)⁻¹ = B⁻¹ A⁻¹`
Generic `inverse(M)` in the kernel is allowed; tests must include a known T*R.
---

---

## Common mistakes

1. Row-major storage but column-vector formulas (document `m[col*4+row]` vs `m[row*4+col]` and **pick one**).
2. Translating after projection (Week 8) by accident.
3. Inverting by transposing a matrix that has translation.

## If we run long, cut

Generic inverse derivation. Keep order + about-c.

## If we run short, add

A known T*R inverse test.
