# WebGL snippet index

Parent: [[07 WebGL and Shader Snippets]]

Open files under `WebGL/demos/`. They load `demos/_gl.js` with a classic `<script>` tag (works from `file://` on most browsers). If a texture or module fails, run `npx serve WebGL/demos`.

## Demos (open these)

| File | Idea | Course |
| --- | --- | --- |
| `demos/01-triangle.html` | Smallest WebGL2 program | 7 |
| `demos/02-colored-triangle.html` | Per-vertex colors as attributes | 7 |
| `demos/03-indexed-quad.html` | `ELEMENT_ARRAY_BUFFER` | 7 |
| `demos/04-rotating-cube.html` | Depth test, cull, MVP | 7 |
| `demos/05-canvas-texture.html` | Texture from a canvas (no CORS) | 7 |
| `demos/06-phong-cube.html` | Normals + Blinn-Phong | 7 / 10 |
| `demos/07-orbit-camera.html` | lookAt + mouse orbit | 7 |
| `demos/08-uv-debug.html` | UV as color, checker | 7 |
| `demos/09-fullscreen-gradient.html` | Fullscreen triangle, `gl_FragCoord` | 10 |
| `demos/10-noise-fbm.html` | Hash, fbm, domain warp | 10 |
| `demos/11-sdf-raymarch.html` | Sphere + box, soft shadow | 10 |
| `demos/12-toon-fresnel.html` | Quantized diffuse + rim | 10 |
| `demos/13-framebuffer-post.html` | Render to texture, vignette | 11 / 12 |
| `demos/14-instancing.html` | `drawArraysInstanced` | 12 |
| `demos/15-particles.html` | `gl.POINTS`, size, fade | 12 |
| `demos/16-pbr-direct.html` | Cook–Torrance, one light | 11 |
| `demos/17-normal-colors.html` | Debug: world normal as RGB | 7 |
| `demos/18-barycentric-wire.html` | Wireframe without a second mesh | 10 |
| `demos/19-dissolve.html` | Noise cutoff + edge color | 10 |
| `demos/20-water.html` | Sum of sines, fake spec | 10 |
| `demos/21-sky.html` | Gradient sky + sun disc | 10 |
| `demos/22-shadow-map.html` | Depth FBO, compare in light space | 11 |
| `demos/23-gpgpu-pingpong.html` | Two textures, particle integrate | 12 |
| `demos/24-matcap.html` | View-space normal → matcap UV | 10 |
| `demos/25-webgl1-triangle.html` | Same triangle in WebGL1 / GLSL 100 | 7 |
| `shadertoy/index.html` | Fire, water, waterfall, ocean, … (Shadertoy `mainImage`) | 10 |

## GLSL / JS catalogs (copy-paste)

| Note | Contents |
| --- | --- |
| [[WebGL/01 Conventions]] | Spaces, winding, gamma, checklist |
| [[WebGL/02 JS Helpers]] | Compile, matrices, geometry, FBO |
| [[WebGL/10 Pipeline]] | Context through framebuffer |
| [[WebGL/11 Vertex and Fragment]] | Shader skeletons |
| [[WebGL/12 Lighting]] | Lambert → PBR |
| [[WebGL/13 Noise]] | Hash through voronoi |
| [[WebGL/14 SDF and Ray Marching]] | SDF ops + tracer |
| [[WebGL/15 Postprocess]] | Fullscreen FX |
| [[WebGL/16 Effects]] | Fog, fire, triplanar, … |
| [[WebGL/17 Particles and GPGPU]] | Points, instancing, ping-pong |
| [[WebGL/18 Shadertoy Effects]] | How to paste fire/water into Shadertoy |

## How to use in a lab

1. Open one demo.
2. Change one number. Predict the picture. Then change it.
3. Break it (comment out `enable(DEPTH_TEST)`). Use the checklist.
4. Copy one GLSL function from a catalog into the demo.

Do not paste five catalogs into week 1. Triangle first.
