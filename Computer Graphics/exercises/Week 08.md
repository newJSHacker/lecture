# Extra exercises — Week 8 (projection)

Lecture: [[Computer Graphics/Lecture 08 Midterm and Projection]] · Demo: [11-perspective](../code/11-perspective.html)

Makeup drills (no laptop) plus projection.

## Written

1. Six spaces; barycentric of centroid; T R vs R T (midterm leftovers).
2. fov in radians. What happens if you pass degrees to `tan`?
3. aspect = width/height or the reverse?
4. Why `near = 0` is forbidden.
5. Smaller fov → larger or smaller cube on screen?

## Coding

6. Toggle ortho / perspective.
7. Slider fov; cube grows when fov shrinks.

```js
sy = 1 / tan(fovY / 2)
sx = sy / aspect
// last row of P copies -z into w (OpenGL-style)
```
