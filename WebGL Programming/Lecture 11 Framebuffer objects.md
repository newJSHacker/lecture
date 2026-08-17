# Lecture 11 — Framebuffer objects

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** render to texture  
**Board first:** FBO → color tex → second pass

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

1. createFramebuffer.
2. texture as color attach.
3. check status COMPLETE.
4. Unbind to default FB.
5. Ping-pong named.

---

## 1. Offscreen

Post and GPGPU. [[WebGL/15 Postprocess]], [[WebGL/17 Particles and GPGPU]].

## 2. Size

FBO size vs canvas.

## 3. Depth

DEPTH_COMPONENT16 renderbuffer if 3D into FBO.

## Live coding (60 min)

Draw cube to FBO; display as a quad.

---

## Lab

1. incomplete FBO debug.
2. second pass invert extra.

---

## Homework

1. Written: why FBO.
2. Code: one offscreen pass.

---

## Quiz (10 min)

1. COMPLETE (3)
2. unbind (3)
3. post (4)

## Snippet

```js
gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
```

---

## Common mistakes

- forgetting to unbind.
- depth missing then 3D into FBO.

---

## Board drawings

1. Two passes.

