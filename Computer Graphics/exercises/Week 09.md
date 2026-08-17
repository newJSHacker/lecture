# Extra exercises — Week 9 (NDC / depth)

Lecture: [[Computer Graphics/Week 09 Clip NDC Depth]] · Demo: [12-zbuffer](../code/12-zbuffer.html)

## Written

1. NDC from clip?
2. Why flip y for Canvas?
3. Depth init value in this kernel (1 = far).
4. Two overlapping triangles: who wins?
5. Why `near = 0.0001` causes z-fighting.

## Coding

6. Viewport tests: NDC (−1, 1) → top-left pixel.
7. Toggle depth; without it, painter order is wrong.

```js
ndc = clip.xyz / clip.w
sx = (ndc.x * 0.5 + 0.5) * width
sy = (1 - (ndc.y * 0.5 + 0.5)) * height
```
