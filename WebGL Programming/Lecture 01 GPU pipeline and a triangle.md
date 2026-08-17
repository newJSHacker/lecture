# Lecture 1 — GPU pipeline and a triangle

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** WebGL2 context, first triangle  
**Board first:** CPU buffers → VS → raster → FS → framebuffer

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

1. Create a WebGL2 context.
2. Compile a shader.
3. Draw a triangle.
4. Use the black-screen checklist.
5. Not Three.js this week.

---

## 1. Struggle a little

[[02 Curriculum Design Advice]] Course 7. Frameworks hide the pipeline.

## 2. Pipeline

Every lecture redraws GPU → VBO → VS → raster → FS → FBO.

## 3. Conventions

[[WebGL/01 Conventions]]. Demo: [[WebGL/demos/index.html]] 01.

## Live coding (60 min)

Typed triangle from demo 01; print compile/link logs.

---

## Lab

1. Clear color you can see.
2. Resize canvas backing store.

---

## Homework

1. Written: pipeline boxes.
2. Code: triangle.

---

## Quiz (10 min)

1. WebGL2 getContext (2)
2. where logs (4)
3. why not Three.js yet (4)

## Snippet

```js
const gl = canvas.getContext('webgl2');
```

## Extra exercises

Walk [[WebGL/demos/01-triangle.html]]. Copy, then type from memory.

---

## Common mistakes

- Starting in Three.js.
- 0×0 canvas.

---

## Board drawings

1. Pipeline.
2. Triangle.

