# Lecture 3 — Particle state in textures

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** pos in RG, vel in BA  
**Board first:** texel = particle

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

1. Encode pos/vel in texels.
2. Spawn as a blit or CPU upload.
3. FS updates state.
4. Render as points/instances reading the tex.
5. Don't one draw call per particle.

---

## 1. SoA on the GPU

Each texel is a particle. Neighbor particles are not spatial neighbors unless you design a grid.

## 2. Render

Vertex shader fetches texel by gl_VertexID / instance ID.

## 3. WebGL2

Integer textures / fetch. Instancing from WebGL week 12.

## Live coding (60 min)

N=64² particles falling with wrap; points.

---

## Lab

1. mouse force extra.
2. reset button.

---

## Homework

1. Written: packing.
2. demo.

---

## Quiz (10 min)

1. why not one mesh per particle (4)
2. RG pos (3)
3. ID mapping (3)

## Snippet

```glsl
vec4 st = texelFetch(u_state, ivec2(gl_VertexID % W, gl_VertexID / W), 0);
```

---

## Common mistakes

- CPU loop 50k Mesh objects.
- points without depth policy.

---

## Board drawings

1. Texel grid.

