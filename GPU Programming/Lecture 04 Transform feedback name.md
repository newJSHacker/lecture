# Lecture 4 — Transform feedback name

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** VS output captured  
**Board first:** varyings → buffer

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

1. Name TF: vertex shader writes buffers.
2. When to prefer TF vs FS ping-pong.
3. Don't require a full TF lab if time is short — a diagram is allowed with a tiny demo.
4. WebGL2 API names.

---

## 1. TF

Particles as vertices. VS updates pos. Rasterizer can be rasterizer discard.

## 2. vs FS

FS ping-pong is often easier in WebGL teaching. TF is the 'graphics pipeline as compute' story.

## 3. WebGPU

Compute shaders make TF less necessary. Still teach the name.

## Live coding (60 min)

Diagram + optional tiny TF or a 'we use ping-pong instead' README with a working FS sim.

---

## Lab

1. rasterizer discard name.
2. compare one sentence.

---

## Homework

1. Written: TF vs FBO.
2. working particles from week 3 OK.

---

## Quiz (10 min)

1. TF captures (4)
2. discard (3)
3. WebGPU replacement (3)

## Snippet

```js
gl.transformFeedbackVaryings(prog, ['v_pos'], gl.SEPARATE_ATTRIBS);
```

---

## Common mistakes

- skipping particles entirely.
- claiming TF without a buffer.

---

## Board drawings

1. VS to buffer.

