# Extra exercises — Week 5 (matrices)

Lecture: [[Computer Graphics/Week 05 Homogeneous Transforms]] · Demos: [07](../code/07-mat4-order.html) [08](../code/08-rotate-center.html)

## Written

1. Write T(1,2,3) (last column).
2. Does `T R` equal `R T`?
3. Rotate about c: three-matrix product.
4. w for a point vs a direction.
5. Inverse of T, of R, of uniform S.

## Coding

6. `T * T⁻¹ ≈ I`. `Ry(90°) * (1,0,0) ≈ (0,0,−1)` under this course’s Ry.
7. Button: T*R vs R*T. The pictures must differ.

```js
// column vectors: matrix nearest the point acts first
p2 = T * R * p     // rotate about origin, then translate
p2 = T(c) * R * T(-c) * p
```
