# Lecture 9 — Clip, NDC, viewport, depth buffer

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** perspective divide, viewport, z-buffer rasterizer  
**Board first:** clip cube → square NDC → canvas, plus a y-flip

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz: camera + projection leftovers |
| 10–25 | Clip space and near-plane |
| 25–40 | NDC and viewport (y-flip) |
| 40–60 | Depth buffer |
| 60–75 | Z-fighting; debug views |

---

## Learning goals

1. Perspective-divide clip → NDC.
2. Map NDC to pixels with a y-flip for Canvas.
3. Reject or skip triangles with `w ≤ 0` / behind the near plane (policy).
4. Implement a z-buffer with a documented compare (`<` or `≤`).
5. Explain z-fighting as precision vs a stretched near/far.

---

## 1. Clip and near (15 min)

After `p_clip = P V M p`, the clip volume is (typical GL) −w ≤ x,y,z ≤ w.

If a triangle straddles the near plane, a naive divide produces garbage. **Course policy:** drop the triangle if any vertex has `w ≤ eps` or ndc out of range. Optional extra: lerp-clip against z=near. Full clipper is not required.

---

## 2. NDC and viewport (15 min)

```
ndc = clip.xyz / clip.w
```

NDC x,y,z in [−1,1] if inside the volume.

Canvas:

```
sx = (ndc.x * 0.5 + 0.5) * width
sy = (1 - (ndc.y * 0.5 + 0.5)) * height   // y-flip
```

Depth for the buffer: `z01 = ndc.z * 0.5 + 0.5` (0 near or 1 near — **pick one**, match compare).

---

## 3. Z-buffer (20 min)

Array `depth[width*height]`, init to +∞ (or 1.0 if using [0,1] far).

For each pixel in the triangle:

```
z = interpolate (barycentric of clip-space z or ndc z)
if z < depth[i]:   // closer
    depth[i] = z
    putPixel(...)
```

**Perspective-correct z** is a later extra. Affine z in NDC is acceptable for the lab if documented.

Two overlapping triangles: the nearer color wins. Disable depth → painter’s order bug.

---

## 4. Z-fighting (10 min)

Coplanar surfaces, or near too small and far too large: bits of z collapse. Fix: push near out, pull far in, add a polygon offset **name only**, or don’t stack two identical planes.

---

## Live coding (60 min)

Full cube: 12 triangles, PVM, divide, viewport, barycentric in **screen space**, z-buffer. Debug mode: color = gray(z).

Show: without depth, back faces scribble; with depth, a solid cube. Culling (Week 10) is optional if depth is correct.

---

## Lab

1. `viewport(ndc, width, height)` with y-flip tests.
2. Z-buffer cube.
3. Keys: toggle depth, toggle z-visualize.
4. A second triangle piercing the cube; occlusion must be correct.

Done when a TA rotates the cube (slider) and holes do not pop from missing depth.

---

## Homework

1. Written: why `near = 0.0001` is a bad idea.
2. Code: init depth; compare documented.
3. Written: y-flip formula, one picture.

---

## Quiz (10 min)

1. NDC from clip? (2 pts)
2. Why flip y for Canvas? (2 pts)
3. Depth init value? (2 pts)
4. Two triangles overlap. Who wins? (4 pts)

---

## Common mistakes

- Dividing before P (nonsense).
- Using clip.z as a pixel depth without mapping.
- `sy` without flip: cube is upside-down, then they negate Ry forever.
- Clearing color but not depth.

---

## Board drawings

1. Clip cube, divide, square.
2. NDC y-up vs canvas y-down.
3. Z-buffer as a second image.
