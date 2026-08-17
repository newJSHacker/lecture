# Lecture 3 — UV patterns

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** grid, polar, repeat  
**Board first:** st = fract(uv * n)

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

1. Make a checker.
2. Polar coordinates.
3. Repeat with fract.
4. Step/smoothstep.
5. Don't use a texture when a function suffices this week.

---

## 1. Procedural

Patterns are functions of uv and time. This is the Shadertoy muscle.

## 2. polar

`r = length(p); a = atan(p.y,p.x);`

## 3. AA

fwidth/smoothstep for edges. Aliased step() is a teaching moment.

## Live coding (60 min)

Fullscreen checker + spinning polar stripes.

---

## Lab

1. brick pattern extra.
2. smoothstep anti-alias a circle.

---

## Homework

1. Written: fract vs mod.
2. GLSL snippet in the repo.

---

## Quiz (10 min)

1. fract purpose (3)
2. atan (3)
3. why smoothstep (4)

## Snippet

```glsl
float checker = step(0.5, fract(uv.x*8.0)) == step(0.5, fract(uv.y*8.0)) ? 0.2 : 0.8;
```

---

## Common mistakes

- texture2D of a 4px checker instead of learning fract.
- atan(x,y) swapped.

---

## Board drawings

1. UV plane.
2. Polar.

