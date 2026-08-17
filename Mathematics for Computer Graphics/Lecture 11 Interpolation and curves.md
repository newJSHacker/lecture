# Lecture 11 — Interpolation and curves

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** lerp, Bezier intro  
**Board first:** lerp on a segment; cubic Bezier

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

1. lerp(a,b,t).
2. Clamp t or not (policy).
3. Quadratic Bezier as lerp of lerps.
4. Cubic Bezier name for fonts/UI.
5. Not to confuse with slerp (name).

---

## 1. lerp

a + t(b-a). Colors, camera paths, keyframes.

## 2. Bezier

De Casteljau. Two control points for cubic. SVG and fonts.

## 3. Parametric speed

t is not arc length. Mention; do not implement arc-length this term.

## Live coding (60 min)

Drag 4 Bezier handles; sample 32 points.

---

## Lab

1. lerp tests t=0,1,0.5.
2. Quadratic Bezier function.

---

## Homework

1. Written: t vs distance.
2. Code: cubic Bezier.

---

## Quiz (10 min)

1. lerp t=0 (2)
2. quadratic as lerps (5)
3. arc length warning (3)

## Snippet

```js
function lerp(a,b,t){ return a + (b-a)*t; }
```

---

## Common mistakes

- t outside [0,1] without saying if extrapolating.
- Calling Bezier slerp.

---

## Board drawings

1. Segment.
2. Handles.

