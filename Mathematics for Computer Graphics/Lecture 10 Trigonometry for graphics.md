# Lecture 10 — Trigonometry for graphics

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** sin, polar, triangles  
**Board first:** unit circle

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

1. sin/cos of π/2, π.
2. Polar to cartesian.
3. Law of cosines name for a lighting picture.
4. Small-angle not required.
5. Oscillation as animation.

---

## 1. Unit circle

Coordinates (cosθ, sinθ). Animation of a planet is this.

## 2. Polar

r, θ → x, y. Useful for flowers, spur gears, SDF later.

## 3. Identities

Only sin²+cos²=1 required. Others optional.

## Live coding (60 min)

A point on a circle; θ slider. Then a pendulum y = cos(t).

---

## Lab

1. polar(r,θ).
2. Lissajous extra.

---

## Homework

1. Written: from polar to a vertex on a cylinder extra.
2. Code: N-gon vertices.

---

## Quiz (10 min)

1. cos(0) (2)
2. polar to xy (4)
3. why sin²+cos² (4)

## Snippet

```js
x = r * Math.cos(t); y = r * Math.sin(t);
```

---

## Common mistakes

- sin(degrees).
- r=0 polar crash.

---

## Board drawings

1. Unit circle.
2. N-gon.

