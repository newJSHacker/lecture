# Extra exercises — Week 11 (Blinn-Phong)

Lecture: [[Computer Graphics/Lecture 11 Blinn Phong and Gamma]] · Demo: [14-blinn-phong](../code/14-blinn-phong.html)

## Written

1. Half-vector formula.
2. Why skip spec when `n·l < 0`?
3. Where does gamma encode happen?
4. Is Blinn-Phong PBR?
5. Why the highlight must move when the camera moves.

## Coding

6. `blinnPhong` tests: facing vs back.
7. Gamma toggle. Lighting stays linear.

```js
h = normalize(l + v)
spec = ks * pow(max(0, dot(n, h)), shininess)
out = pow(clamp(linear, 0, 1), 1/2.2)
```
