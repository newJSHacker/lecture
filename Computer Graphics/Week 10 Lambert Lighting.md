# Week 10 — Lighting I (Lambert)

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** Lambert, face and vertex normals, normal matrix  
**Board first:** `n·l` on a cube face, light arrow, clamped at 0

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 9 |
| 10–25 | Normals vs positions |
| 25–50 | Lambert, ambient, spaces |
| 50–65 | Flat vs Gouraud |
| 65–75 | Culling vs lighting |

---

## Learning goals

1. Compute a face normal from three vertices (`cross`).
2. Shade with `max(0, n·l)` in a chosen space (world **or** view — freeze one).
3. Apply the normal matrix when M has scale.
4. Compare flat and Gouraud on the cube.
5. Distinguish back-face culling from “the face is black because n·l < 0.”

---

## 1. Normals (15 min)

Face normal: `normalize(cross(b-a, c-a))` with CCW vertices.

Vertex normals: average adjacent faces, or from the mesh file. A sphere needs vertex normals; a faceted cube can use face normals.

Transform: `n_world = normalize(normalMat * n_obj)` with `normalMat = transpose(inverse(M_3×3))`.

---

## 2. Lambert (25 min)

Directional light: `l` is a unit vector **toward** the light (or from the surface — pick and write it on the board).

```
diff = kd * max(0, dot(n, l))
color = ka * ambient + diff * lightColor
```

`ka` is a policy so unlit faces are not pitch black on a projector.

**Space:** transform n and l into the same space. Mixing world n with view l is the classic bug.

Point lights: `l = normalize(lightPos - p)`. Need a position p at the vertex or (later) in the fragment. This week: directional is enough; point light is the lab extra.

---

## 3. Interpolation (15 min)

**Flat:** one n per triangle, one color, fill.

**Gouraud:** Lambert at vertices, barycentric-interpolate **color**. Fast; highlights smear (Week 11).

**Phong interpolation:** interpolate **normals**, normalize, shade per pixel. Better; do this in Week 11 if Gouraud is already working.

---

## 4. Culling (10 min)

Back-face: `dot(n_view, viewDir)` or screen-space winding. Culled faces are not drawn. A front face with `n·l < 0` is still drawn, just dark. Students conflate these.

---

## Live coding (60 min)

Cube, face normals, one directional light, sliders for light angles. Ambient slider. Toggle culling (2D winding of the projected triangle).

Debug: color = `n * 0.5 + 0.5`.

---

## Lab

1. Face-Lambert cube.
2. Gouraud with vertex normals (cube can reuse face normals at vertices — it will look faceted; that is OK).
3. `normalMatrix(M)`.
4. Debug normals view.

Done when rotating the light moves the terminator, and the debug-normal view is colorful, not black.

---

## Homework

1. Written: derive why `(M⁻¹)ᵀ` for normals (short; Shirley). Or: one picture of non-uniform scale on a circle.
2. Code: `lambert(n, l, kd, ka)`.
3. Point light extra: falloff optional, not required.

---

## Quiz (10 min)

1. Face normal formula. (2 pts)
2. `max(0, n·l)` — why max? (2 pts)
3. Same space for n and l. Why? (3 pts)
4. Culling vs negative Lambert. (3 pts)

---

## Common mistakes

- Lighting in object space while the camera moved.
- Not normalizing n after interpolation (Week 11) or after the normal matrix.
- `l` pointing toward the surface, then wondering why the cube is black.

---

## Board drawings

1. Face with n and l, θ.
2. Non-uniform scale, wrong vs right normals.
3. Gouraud colors at vertices, blend inside.
