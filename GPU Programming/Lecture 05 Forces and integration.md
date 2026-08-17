# Lecture 5 — Forces and integration

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Euler, clamp  
**Board first:** v += a dt; p += v dt

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

1. Semi-implicit Euler.
2. dt cap.
3. Collision with a plane/box.
4. Don't energy-explode.
5. Reset bounds.

---

## 1. Integration

Same as Interactive Web physics-lite. GPU: all particles in parallel.

## 2. Stability

dt too big → explode. Clamp speed.

## 3. Forces

Gravity, attractor, curl noise extra.

## Live coding (60 min)

Attractor + gravity; explode then cap dt.

---

## Lab

1. box collide extra.
2. curl extra.

---

## Homework

1. Written: why cap dt.
2. demo.

---

## Quiz (10 min)

1. Euler (3)
2. explode cause (4)
3. clamp (3)

## Snippet

```glsl
vel += acc * dt; pos += vel * dt;
```

---

## Common mistakes

- variable dt uncapped.
- CPU physics + GPU draw as if it were GPGPU.

---

## Board drawings

1. Euler step.

