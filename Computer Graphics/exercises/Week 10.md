# Extra exercises — Week 10 (Lambert)

Lecture: [[Computer Graphics/Lecture 10 Lambert Lighting]] · Demo: [13-lambert](../code/13-lambert.html)

## Written

1. Face normal from three CCW vertices.
2. Why `max(0, n·l)`?
3. Same space for n and l. Why?
4. Culling vs negative Lambert.
5. Why `(M⁻¹)ᵀ` for normals.

## Coding

6. Face-Lambert cube; light yaw slider.
7. Debug view `n * 0.5 + 0.5`. Must not be black.

```js
diff = kd * max(0, dot(n, l))
color = ka * ambient + diff * lightColor
```
