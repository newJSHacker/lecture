# Lecture 9 — Deferred idea

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** G-buffer then lights  
**Board first:** albedo n depth → light pass

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

1. Name G-buffer channels.
2. Lights as fullscreen or volumes.
3. Bandwidth cost.
4. Don't implement a AAA deferred engine.
5. Forward+ / clustered names.

---

## 1. Why

Many lights, few objects that write G-buffer. Light pass reads G and adds.

## 2. What goes in G

albedo, metallic-rough, normals, depth. Packed.

## 3. WebGL

MRT names. Students can draw a **debug view** of n and albedo from a fake G (multiple targets or just extra textures).

## Live coding (60 min)

Debug view: albedo | normals | depth as three panes (can be extra FBOs or Three.js).

---

## Lab

1. count lights that would hurt forward.
2. written G layout.

---

## Homework

1. Written: when deferred wins.
2. debug screenshot.

---

## Quiz (10 min)

1. G channels (4)
2. MRT (3)
3. when not to deferred (3)

## Snippet

```glsl
layout(location=0) out vec4 gAlbedo;
```

---

## Common mistakes

- deferred for a single cube.
- no debug views.

---

## Board drawings

1. G panes.

