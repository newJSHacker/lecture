# Lecture 12 — Fullscreen post

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** scene tex → FS  
**Board first:** FBO color → quad

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

1. Render a 3D or Shadertoy scene to a texture (or use a still).
2. Second pass: vignette, grain, or color grade.
3. Don't stack 8 passes.
4. [[WebGL/15 Postprocess]].

---

## 1. Post

Same FBO idea as WebGL week 11. Shaders here are 2D image filters.

## 2. FXAA name

RTR will name AA. This week: kernel filters (blur/sharpen) as teaching.

## 3. Ping-pong

Named for GPU course.

## Live coding (60 min)

Vignette + grain on a marching scene or a textured cube.

---

## Lab

1. blur extra (separable name).
2. toggle post.

---

## Homework

1. Written: why extra fill rate.
2. Two-pass code.

---

## Quiz (10 min)

1. FBO (3)
2. grain should be (4)
3. 8 passes (3)

## Snippet

```glsl
color *= smoothstep(1.2, 0.4, length(uv-0.5));
```

---

## Common mistakes

- post as a substitute for lighting.
- 4K FBO on integrated GPU.

---

## Board drawings

1. Two passes.

