# Extra exercises — Week 13 (GPU map)

Lecture: [[Computer Graphics/Week 13 GPU Mapping]] · Demo: [16-webgl-cube](../code/16-webgl-cube.html)

## Written

1. `gl_Position` is which space?
2. Depth test replaces which CPU structure?
3. One black-screen cause from the conventions list.
4. `matrixWorldInverse` is which matrix?
5. May Three.js `Raycaster` be the student picking algorithm?

## Coding

6. Fill `u_p`, `u_v`, `u_m` from the **same** `mat4` kernel as the CPU cube.
7. One-page table: CPU function → GPU stage, in the repo.

```glsl
gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);
```
