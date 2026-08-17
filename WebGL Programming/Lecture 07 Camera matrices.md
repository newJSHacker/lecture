# Lecture 7 — Camera matrices

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** P V M in the shader  
**Board first:** gl_Position = P*V*M*pos

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

1. Reuse CG I lookAt/perspective if they have it.
2. u_p u_v u_m.
3. Orbit.
4. Don't hardcode P forever.
5. Handedness freeze.

---

## 1. Same math

[[10 Computer Graphics I]] Weeks 7–9.

## 2. Three.js later

These uniforms are camera.projectionMatrix etc.

## 3. Demo

07 orbit.

## Live coding (60 min)

lookAt + perspective from JS mat4; spin the cube.

---

## Lab

1. WASD extra.
2. ortho toggle.

---

## Homework

1. Written: mapping table CPU→uniform.
2. Code: orbit.

---

## Quiz (10 min)

1. product order (4)
2. lookAt (3)
3. fov radians (3)

## Snippet

```glsl
gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);
```

---

## Common mistakes

- Three.js camera as the lab.
- row-major P.

---

## Board drawings

1. PVM.

