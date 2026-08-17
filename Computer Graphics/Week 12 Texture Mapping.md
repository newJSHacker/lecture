# Week 12 — Texture mapping

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** UV, `sampleNearest`, textured Lambert  
**Board first:** a quad with (0,0),(1,0),(1,1),(0,1) labeled

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 11 |
| 10–25 | UV, wrap, clamp |
| 25–45 | Sampling: nearest, bilinear (idea) |
| 45–60 | Perspective-correct interpolation (picture) |
| 60–75 | Texture as albedo; minification / mipmaps named |

---

## Learning goals

1. Attach UV to vertices and interpolate with barycentric.
2. Sample a texture with nearest neighbor and a wrap/clamp policy.
3. Multiply albedo by Lambert (texture is not lighting).
4. Explain why affine UV looks wrong in perspective.
5. Name bilinear and mipmaps without implementing mipmaps.

---

## 1. UV (15 min)

UV in [0,1] typically. `(0,0)` is which corner of the **image**? Canvas/PNG: often top-left. glTF: often bottom-left. **Pick one, write it on the board, stick to it.** If the texture is upside-down, flip v: `v = 1 - v`, do not randomly swap UVs on four vertices.

Wrap: `u = u - floor(u)` (repeat). Clamp: `u = min(1, max(0, u))`.

---

## 2. Sampling (20 min)

Nearest:

```
x = floor(u * width)
y = floor(v * height)
```

with wrap/clamp before that.

Bilinear: four taps, lerp. Name; optional lab extra.

Minification: many texels per pixel → aliasing. Mipmaps: prefiltered levels. Required knowledge: the **word** and why games use them. Not required code.

---

## 3. Perspective-correct (15 min)

Affine barycentric in **screen space** interpolates UV as if the triangle were flat on the screen. A perspective quad (road, floor) shows the classic bow-tie UV.

Teaching fix: interpolate `u/z`, `v/z`, `1/z`, then `u = (u/z) / (1/z)`. z from clip or view. Extra credit if they implement it; midterm-level: **describe** it.

---

## 4. Shading (10 min)

```
albedo = sample(tex, uv)   // linear if following Week 11
color = lambert * albedo + specular * light   // spec often not multiplied by albedo (policy)
```

A texture is not a reason to skip normals.

---

## Live coding (60 min)

Load a PNG into `ImageData` (or a procedural checker if `file://` blocks). Textured quad facing the camera. Then UVs on the cube (each face 0–1). Mag filter toggle nearest / bilinear if time.

UV debug: `putPixel` RGB = (u, v, 0).

---

## Lab

1. `sampleNearest(image, u, v, mode)`.
2. Textured cube **or** a floor quad in perspective (to see affine bug).
3. UV debug view.
4. Procedural checker fallback.

Done when rotating the cube does not smear a single texel across a face unless UVs are actually constant (a bug).

---

## Homework

1. Written: affine vs perspective-correct UV, one picture of a trapezoid.
2. Code: clamp vs repeat demo.
3. Written: mipmaps in three sentences.

---

## Quiz (10 min)

1. UV of a vertex — is it a position? (2 pts)
2. Nearest sample formula. (2 pts)
3. Why affine UV fails in perspective. (4 pts)
4. Texture replaces lighting? Yes/no. (2 pts)

---

## Common mistakes

- Integer UV 0–width mixed with 0–1.
- Sampling with v from the wrong origin; “fixing” by rotating the PNG.
- Perspective cube with one UV per cube (all faces the same smear).

---

## Board drawings

1. UV square on a mesh.
2. Nearest vs bilinear 2×2.
3. Trapezoid road, affine vs correct.
