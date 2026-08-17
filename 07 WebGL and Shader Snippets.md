# 07 WebGL and Shader Snippets

Runnable WebGL2 demos and copy-paste GLSL for **IGWT** Courses 7, 10, 11, and 12.

These are teaching snippets, not a production engine. Each demo is one idea. Open the HTML files in a browser (a local static server is safest). Do not start from Three.js here. Three.js comes after students can get a triangle on screen from this folder.

## Start

1. [[WebGL/00 Index]] — map of demos and catalogs
2. [[WebGL/01 Conventions]] — clip space, winding, color, black-screen checklist
3. Open `WebGL/demos/01-triangle.html`

## What is in the folder

| Path | What it is |
| --- | --- |
| [[WebGL/00 Index]] | Catalog of every demo and GLSL file |
| [[WebGL/01 Conventions]] | Spaces, winding, gamma, debug |
| [[WebGL/02 JS Helpers]] | Shared `demos/_gl.js` documented |
| [[WebGL/10 Pipeline]] | Context, shaders, buffers, VAO, uniforms, textures, FBO |
| [[WebGL/11 Vertex and Fragment]] | Attribute plumbing, varyings, clip-space patterns |
| [[WebGL/12 Lighting]] | Lambert, Phong, Blinn, PBR, toon, fresnel, IBL-lite |
| [[WebGL/13 Noise]] | Hash, value noise, fbm, voronoi, warp |
| [[WebGL/14 SDF and Ray Marching]] | Primitives, CSG, sphere tracer |
| [[WebGL/15 Postprocess]] | Fullscreen pass, bloom-lite, FX, color |
| [[WebGL/16 Effects]] | Fog, dissolve, water, fire, triplanar, matcap, barycentric |
| [[WebGL/17 Particles and GPGPU]] | Points, ping-pong, instancing |
| [[WebGL/demos/]] | Self-contained HTML you can open and edit |

## Teaching use

- Course 7: demos 01–08, then [[WebGL/10 Pipeline]]
- Course 10: demos 09–12, 16, 20–21 and [[WebGL/13 Noise]], [[WebGL/14 SDF and Ray Marching]]
- Course 11: demos 13, 16, 22 and [[WebGL/12 Lighting]], [[WebGL/15 Postprocess]]
- Course 12: demos 14–15, 23 and [[WebGL/17 Particles and GPGPU]]

Live-code from a demo, then delete a function and have students restore it. See [[Teaching/06 Live Coding Pedagogy]].

## License

Teaching notes. Reuse with attribution. Snippets are small and intended to be copied into student starters.
