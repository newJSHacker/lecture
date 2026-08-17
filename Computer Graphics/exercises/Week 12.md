# Extra exercises — Week 12 (textures)

Lecture: [[Computer Graphics/Week 12 Texture Mapping]] · Demo: [15-texture](../code/15-texture.html)

## Written

1. Is UV a position in world space?
2. Nearest sample formula.
3. Why affine UV fails in perspective (trapezoid picture).
4. Texture replaces lighting? Yes/no.
5. Mipmaps in three sentences.

## Coding

6. `sampleNearest` clamp vs repeat.
7. UV debug coloring. Checker × Lambert.

```js
x = floor(u * width)
y = floor(v * height)
albedo = sample(tex, uv)
color = lambert * albedo
```
