# Lecture 2 — FBO ping-pong

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** A→B→A textures  
**Board first:** read A write B; swap

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

1. Two textures.
2. Never read and write the same.
3. Swap references.
4. Clear policy.
5. [[WebGL/17 Particles and GPGPU]].

---

## 1. Why two

A shader cannot safely read the texel it is writing. Ping-pong is the game-of-life / blur / particle-position pattern.

## 2. Size

Sim resolution ≠ canvas resolution.

## 3. Precision

HALF_FLOAT / FLOAT textures for positions. Unsigned byte is a trap.

## Live coding (60 min)

Game of life or a blur ping-pong; pause.

---

## Lab

1. show A and B debug.
2. wrong same-texture bug then fix.

---

## Homework

1. Written: why two textures.
2. Code.

---

## Quiz (10 min)

1. feedback loop (4)
2. float tex (3)
3. sim vs canvas size (3)

## Snippet

```js
;[texA, texB] = [texB, texA];
```

---

## Common mistakes

- one texture in/out.
- RGBA8 positions.

---

## Board drawings

1. Two FBOs.

