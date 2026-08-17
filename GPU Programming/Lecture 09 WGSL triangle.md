# Lecture 9 — WGSL triangle

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** vertex_index, clip  
**Board first:** @vertex @fragment

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

1. A WGSL vs/fs pair.
2. swap chain / canvas context.
3. clip-space same as WebGL.
4. Don't hide in a 3k-line engine.
5. Map gl_Position.

---

## 1. WGSL

Typed. `@location`. No GLSL preprocessor soup.

## 2. Canvas

`navigator.gpu.requestAdapter` then `configure` the context.

## 3. Errors

Validation is loud. Good.

## Live coding (60 min)

Colored triangle WGSL; resize.

---

## Lab

1. uniform time extra.
2. compare GLSL side by side.

---

## Homework

1. Written: GLSL vs WGSL table (6 rows).
2. code.

---

## Quiz (10 min)

1. @builtin(position) (3)
2. bind group (4)
3. clip z (3)

## Snippet

```wgsl
@vertex fn vs(@builtin(vertex_index) i: u32) -> @builtin(position) vec4f { /* ... */ }
```

---

## Common mistakes

- three.js WebGPURenderer as the only lab with no WGSL read.
- copying a full sample unread.

---

## Board drawings

1. Triangle.

