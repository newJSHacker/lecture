# Week 5 — Homogeneous coordinates and affine transforms

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `mat4` multiply, `translate`, `rotateX/Y/Z`, `scale`  
**Board first:** rotate-then-translate vs translate-then-rotate

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 4 |
| 10–25 | Affine maps; why 4×4 |
| 25–50 | Homogeneous points and directions |
| 50–65 | Composition order |
| 65–75 | Inverse of T, R, S |

---

## Learning goals

1. Write a translation as a 4×4 matrix.
2. Explain `w = 1` vs `w = 0`.
3. Compose transforms and predict the picture.
4. Rotate a shape about its center.
5. Invert T, R, uniform S without calling a generic inverse (optional generic inverse in the kernel).

---

## 1. Affine and homogeneous (15 min)

An affine transform is linear part plus translation:

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

## 2. Building blocks (25 min)

**Translate** `T(t)`: identity, last column `t` (column-vector convention).

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

## 3. Order (15 min)

Column vectors: **the matrix nearest the point acts first.**

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

## 4. Inverses (10 min)

- `T(t)⁻¹ = T(-t)`
- `R⁻¹ = Rᵀ` (rotation)
- `S(s)⁻¹ = S(1/s)` if s ≠ 0
- Non-uniform scale + rotation: inverse is not “invert each and reverse” unless you remember `(AB)⁻¹ = B⁻¹ A⁻¹`

Generic `inverse(M)` in the kernel is allowed; tests must include a known T*R.

---

## Live coding (60 min)

1. `mul(A,B)`, `mulVec(M, p)` with `w`.
2. A triangle at the origin; slider θ; `Ry`.
3. Same triangle offset; show it swings around the origin.
4. `T(c) R T(-c)` about the centroid. Students clap when it works.

Print the matrix. Do not hide it in a library.

---

## Lab

1. `mat4.js`: `identity`, `mul`, `translate`, `rotateY`, `scale`.
2. Rotate-about-center on the Week 3 triangle.
3. Tests: `T * T⁻¹ = I` within epsilon; `R(90°) * (1,0,0)` ≈ `(0,0,−1)` or whatever **your** Ry does — write the expected vector in the test from the board.

Done when order A vs B is a button that changes the animation.

---

## Homework

1. By hand: 2×2 rotation of (1,0) by 90°. Then one 4×4 `T(1,0,0) * p` for p=(0,0,0,1).
2. Code: `rotateX`, `rotateZ`.
3. Written: why directions use w=0.

---

## Quiz (10 min)

1. Write T(1,2,3) (you may write “identity plus last column”). (3 pts)
2. Does `T R` equal `R T`? (2 pts)
3. How do you rotate about c? (3 pts)
4. w for a direction? (2 pts)

---

## Common mistakes

- Row-major storage but column-vector formulas (document `m[col*4+row]` vs `m[row*4+col]` and **pick one**).
- Translating after projection (Week 8) by accident.
- Inverting by transposing a matrix that has translation.

---

## Board drawings

1. T R vs R T on a stick figure.
2. Homogeneous column for a point and a vector.
3. Rotate about c as three arrows.
