# Extra exercises — Week 1 (images / pipeline)

Lecture: [[Computer Graphics/Week 01 What Computer Graphics Is]] · Demo: [01-putpixel](../code/01-putpixel.html)

## Written

1. Six spaces in order. One sentence each.
2. Rasterization vs ray tracing: who loops over triangles first?
3. `P * V * M` or `M * V * P` in this course? Why?
4. Canvas `(0,0)` vs world origin.
5. Why `canvas.width` must match the backing store, not only CSS size.
6. Index of pixel (3, 2) in a width-10 RGBA buffer.
7. What we will not implement this term (name three).

## Coding

8. `putPixel` with bounds checks. Tests: corner, off-canvas, 1×1.
9. `clear` then a clipped rectangle. Do not wrap with `%`.

```js
export function putPixel(img, x, y, r, g, b, a = 255) {
  x = x | 0; y = y | 0;
  if (x < 0 || y < 0 || x >= img.width || y >= img.height) return;
  const i = (y * img.width + x) * 4;
  img.data[i] = r; img.data[i+1] = g; img.data[i+2] = b; img.data[i+3] = a;
}
```
