# Extra exercises — Week 2 (color)

Lecture: [[Computer Graphics/Week 02 Color and Framebuffer]] · Demos: [02](../code/02-checker.html) [03](../code/03-alpha-over.html)

## Written

1. `over` for rgb, alpha in [0,1]. Ignore output alpha.
2. Is byte 128 half as much light as 255?
3. CSS-stretched canvas: why a circle becomes an ellipse.
4. Straight vs premultiplied: one sentence.
5. Letterbox vs stretch a 16:9 buffer in a 4:3 window.

## Coding

6. `overPixel` tests: opaque, alpha 0, 50% red on black.
7. Eight boxes with alpha 1/8 … 8/8.

```js
out_rgb = src_rgb * src_a + dst_rgb * (1 - src_a)
out_a   = src_a + dst_a * (1 - src_a)
```
