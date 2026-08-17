# Computer Graphics I snippets

Runnable software-rasterizer demos and a shared math kernel for IGWT Computer Graphics I.

**Open:** [Computer Graphics/code/index.html](Computer%20Graphics/code/index.html)

**Copy from:** [Computer Graphics/code/kernel.js](Computer%20Graphics/code/kernel.js)

**Extra problem sets:** [Computer Graphics/exercises/00 Index.md](Computer%20Graphics/exercises/00%20Index.md)

Language is **JavaScript + Canvas `ImageData`**. Do not require Three.js for weeks 1–12. WebGL2 cube is demo 16 (Week 13). Three.js may be a 5-minute camera oracle in Week 7, not the student `lookAt`.

If `file://` is blocked, from `Computer Graphics/code/`:

```
npx serve
python -m http.server
```

## Demos

| # | File | Week | What it shows |
| ---: | --- | ---: | --- |
| 1 | [01-putpixel.html](Computer%20Graphics/code/01-putpixel.html) | 1 | `putPixel`, gradient |
| 2 | [02-checker.html](Computer%20Graphics/code/02-checker.html) | 2 | framebuffer |
| 3 | [03-alpha-over.html](Computer%20Graphics/code/03-alpha-over.html) | 2 | compositing |
| 4 | [04-barycentric.html](Computer%20Graphics/code/04-barycentric.html) | 3 | αβγ as RGB |
| 5 | [05-quad.html](Computer%20Graphics/code/05-quad.html) | 3 | two triangles |
| 6 | [06-vec3.html](Computer%20Graphics/code/06-vec3.html) | 4 | frames |
| 7 | [07-mat4-order.html](Computer%20Graphics/code/07-mat4-order.html) | 5 | T R vs R T |
| 8 | [08-rotate-center.html](Computer%20Graphics/code/08-rotate-center.html) | 5 | T(c) R T(−c) |
| 9 | [09-scene-graph.html](Computer%20Graphics/code/09-scene-graph.html) | 6 | parent × local |
| 10 | [10-lookat.html](Computer%20Graphics/code/10-lookat.html) | 7 | `V * eye ≈ 0` |
| 11 | [11-perspective.html](Computer%20Graphics/code/11-perspective.html) | 8 | fov / ortho |
| 12 | [12-zbuffer.html](Computer%20Graphics/code/12-zbuffer.html) | 9 | depth |
| 13 | [13-lambert.html](Computer%20Graphics/code/13-lambert.html) | 10 | `n·l` |
| 14 | [14-blinn-phong.html](Computer%20Graphics/code/14-blinn-phong.html) | 11 | spec + gamma |
| 15 | [15-texture.html](Computer%20Graphics/code/15-texture.html) | 12 | UV nearest |
| 16 | [16-webgl-cube.html](Computer%20Graphics/code/16-webgl-cube.html) | 13 | same PVM on GPU |
| 17 | [17-kernel-tests.html](Computer%20Graphics/code/17-kernel-tests.html) | all | fixtures |
| 18 | [18-project-sandbox.html](Computer%20Graphics/code/18-project-sandbox.html) | 14 | debug views |

## Kernel (copy; do not grow fov until the cube “shows up”)

```js
p_clip = P * V * M * vec4(p, 1)
ndc = clip.xyz / clip.w
sx = (ndc.x * 0.5 + 0.5) * width
sy = (1 - (ndc.y * 0.5 + 0.5)) * height   // canvas y grows down
```

Full `vec3`, `mat4`, `lookAt`, `perspective`, barycentric fill, z-buffer, Lambert, Blinn-Phong, and `sampleNearest` are in `kernel.js`.
