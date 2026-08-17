# Lecture 6 — Textures

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** upload, UV, sampling  
**Board first:** uv as color debug

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. texImage2D.
2. uv attribute.
3. TEXTURE_2D bind.
4. flipY policy.
5. sRGB name.

---

## 1. Upload

async image onload. Premultiply options.

## 2. Debug

uv as color. [[WebGL/08 uv debug]] if present, else shader.

## 3. Filtering

NEAREST vs LINEAR. Mips named.

## Live coding (60 min)

Textured quad then cube.

---

## Lab

1. uv debug.
2. wrap repeat vs clamp.

---

## Homework

1. Written: flipY.
2. Code: sample.

---

## Quiz (10 min)

1. texImage2D (3)
2. uv debug (4)
3. NEAREST (3)

## Snippet

```glsl
outColor = texture(u_tex, v_uv);
```

---

## Common mistakes

- sampling before upload done.
- wrong flipY.

---

## Board drawings

1. UV.

