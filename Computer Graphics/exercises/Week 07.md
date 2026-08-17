# Extra exercises — Week 7 (camera)

Lecture: [[Computer Graphics/Week 07 Cameras]] · Demo: [10-lookat](../code/10-lookat.html)

## Written

1. Name eye, target, up.
2. After V, where is the eye?
3. Why this course looks down −Z.
4. `V * eye` should be …?
5. Degenerate: up ∥ look. What do you do?

## Coding

6. `lookAt` fixture: eye (0,0,5), target origin, `V*eye ≈ 0`.
7. Sliders for eye. Do not call Three.js `lookAt` in the lab.

```js
w = normalize(eye - target)
u = normalize(cross(up, w))   // fallback if parallel
v = cross(w, u)
```
