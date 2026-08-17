# Extra exercises — Week 4 (vectors)

Lecture: [[Computer Graphics/Week 04 Vectors and Frames]] · Demo: [06-vec3](../code/06-vec3.html)

## Written

1. Point minus point is a …? Point plus point?
2. `dot` of two unit vectors.
3. 2D cross of (2,0) and (0,3).
4. Do normals transform with M? Correct name.
5. Right-hand rule for `cross(i, j)`.

## Coding

6. `dot` / `cross` / `normalize(0)` must not return NaN.
7. Rotate (1,0) with a 2×2 matrix; match `cos/sin`.

```js
function vcross(a, b) {
  return {
    x: a.y * b.z - a.z * b.y,
    y: a.z * b.x - a.x * b.z,
    z: a.x * b.y - a.y * b.x,
  };
}
```
