# Week 11 — Blinn-Phong and gamma

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** Blinn-Phong; linear lighting; gamma encode  
**Board first:** reflection r vs half-vector h

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 10 |
| 10–30 | Phong vs Blinn-Phong |
| 30–45 | Multiple lights; clamp vs HDR teaser |
| 45–65 | Linear vs sRGB policy for this course |
| 65–75 | Debug views (normals, lighting only) |

---

## Learning goals

1. Write Blinn-Phong with a half-vector.
2. State that this model is not energy-conserving PBR.
3. Sum two lights.
4. Light in linear space; encode `pow(c, 1/2.2)` at the end.
5. Produce a normals-as-color debug view.

---

## 1. Specular (20 min)

Viewer `v = normalize(eye - p)` (world or view — same space as n).

Phong: `r = reflect(-l, n)`, spec = `(max(0, r·v))^shininess`.

Blinn: `h = normalize(l + v)`, spec = `(max(0, n·h))^shininess`.

Cheaper and the default in most real-time teaching. Shininess 16–64 for a cube; 256 is a pin spark.

```
color = ka * ambient
      + kd * max(0, n·l) * lightColor
      + ks * pow(max(0, n·h), shininess) * lightColor
```

If `n·l ≤ 0`, skip specular (light is behind the surface).

**PBR** (Semester 4): microfacets, energy conservation, IBL. Name it. Do not implement Cook-Torrance this week.

---

## 2. Many lights (15 min)

Sum contributions. uint8 will clip: `min(1, color)` or store float and encode once. HDR / bloom is Real-Time Rendering. Here: clip and mention the limitation in the report.

---

## 3. Gamma (20 min)

Policy from Week 2, now enforced:

1. Textures / vertex colors: treat 8-bit as sRGB → `pow(c/255, 2.2)` (approx).
2. Lights and Lambert in linear.
3. Output: `pow(linear, 1/2.2)` then * 255.

Toggle in the demo: wrong (light in sRGB) vs right. The wrong one often “looks contrasty” and students prefer it — tell them the projector lies, the policy stands.

Full sRGB curve (2.4 piecewise) is optional extra credit, not required.

---

## Live coding (60 min)

Blinn-Phong cube, shininess slider, two lights, gamma toggle. Debug: specular-only (kd=0).

Per-pixel Phong interpolation if Gouraud from last week is done: interpolate n, normalize, shade.

---

## Lab

1. `blinnPhong(...)` with tests: n=l=v → spec > 0; n opposite l → spec 0.
2. Two directional lights.
3. Gamma encode function.
4. Debug keys: N (normals), L (diffuse only), S (spec only).

Done when the highlight **moves with the camera** (depends on v). If it does not, they used a constant v.

---

## Homework

1. Written: h vs r, one picture.
2. Written: why lighting in sRGB is wrong (one paragraph).
3. Code: shininess slider documented in README.

---

## Quiz (10 min)

1. Half-vector formula. (2 pts)
2. Why skip spec when n·l < 0? (2 pts)
3. Where does gamma encode happen? (3 pts)
4. Is Blinn-Phong PBR? Yes/no. (3 pts)

---

## Common mistakes

- `v` as (0,0,1) forever.
- Adding spec in sRGB then gamma-encoding again.
- Shininess 0.5 because they thought it was a 0–1 roughness (it is an exponent).

---

## Board drawings

1. n, l, v, r, h.
2. Linear add vs sRGB add.
3. Two lights, two highlights.
