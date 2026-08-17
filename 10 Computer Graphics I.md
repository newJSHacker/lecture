# Computer Graphics I

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Students learn how an image is made: pixels, transforms, cameras, rasterization, lighting, and textures. They implement a **tiny software renderer** in JavaScript, then map every stage onto WebGL / Three.js so later courses are names they already understand.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes (teach from these):** [[Computer Graphics/00 Lectures]]  
**Extra exercises:** [[Computer Graphics/exercises/00 Index]]  
**Code snippets / software rasterizer:** [[11 Computer Graphics Snippets]] · [Computer Graphics/code/index.html](Computer%20Graphics/code/index.html)

Related later courses (do not steal their labs):

- [[07 WebGL and Shader Snippets]] — GPU API, Semester 3
- [[08 Three.js Snippets]] — engine, Semester 3
- Real-Time Rendering / Shader Programming — PBR, shadows, post, Semester 4

---

## Where this course sits

Teach it in **Semester 2**, after:

- [[01 subjects#3. Mathematics for Computer Graphics]]
- [[01 subjects#1. Introduction to Programming]]

Run it **alongside or just after** [[04 Computational Geometry]]. Week 13 of computational geometry (BVH picking) and Week 13 of this course (GPU mapping) can share a joint session.

| Prerequisite | Why it is required |
| --- | --- |
| Programming (JavaScript) | Every lab writes a renderer or a shader-sized function |
| Vectors, matrices, trigonometry | Transforms, cameras, lighting |
| Canvas or DOM comfort | Framebuffer is an `ImageData` |

Do **not** start this course before students can write nested loops and small vector functions. Do **not** start with Three.js as the student algorithm. Three.js is a **named map of the pipeline** in Week 13, and an optional camera-move demo in Week 7, not the weekly lab.

---

## Course goal

By the end of the semester, a student can:

1. Trace a vertex from object space to a pixel (model → world → view → clip → NDC → screen).
2. Rasterize a triangle with barycentric coordinates and a depth buffer.
3. Light a surface with Lambert and Blinn-Phong using interpolated normals.
4. Sample a texture with UV coordinates and state the min/mag problem.
5. Point at a WebGL / Three.js program and name which stage of **their** software renderer it is.

---

## Teaching structure (every week)

Same five-part week as computational geometry.

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Definitions, one derivation, one picture of the pipeline |
| Live coding | 60 min | Professor implements that stage in the shared software renderer |
| Lab | 2–3 hours | Students finish a starter and see pixels change |
| Homework | 4–6 hours | One implementation + 3–5 written questions |
| Quiz | 10 min | Spaces, matrices, barycentric, one picture question |

**Implementation language:** JavaScript + Canvas `ImageData` for Weeks 1–12. **WebGL2** appears in Week 13 as the same scene on the GPU. Python is acceptable only if the department already standardized on it; then use NumPy arrays as the framebuffer.

**Never lecture from slides only.** Every week a picture on screen must change because of code written in class.

---

## Conventions (freeze in Week 1, keep all year)

Copy the WebGL course freeze so students do not relearn handedness in Semester 3. Full list: [[WebGL/01 Conventions]]

```
object → world → view → clip → NDC → pixels
p_clip = P * V * M * p_object
```

| Choice | This course |
| --- | --- |
| Handedness | Right-handed |
| Up | +Y |
| Camera looks | −Z |
| Matrices | Column-major; multiply `P * V * M * vec4(p,1)` |
| Front face | Counter-clockwise |
| Color | Lighting in linear space; gamma 2.2 at the **end** (Week 11–12) |
| Angles | Radians in code; degrees only on the board if you convert in front of them |

If a cube is inside-out, it is winding or a mirrored scale — not “the API is broken.”

---

## Professor preparation (before Week 1)

Prepare these once; reuse them every year.

- Pipeline posters: one wall of spaces, one wall of a triangle going to pixels
- A course repository:

```
cg1/
  lecture/
  starter/
  solutions/
  assignments/
  raster/         # shared software renderer (ImageData)
  math/           # vec3, mat4, barycentric
  tests/          # transform, barycentric, depth fixtures
```

- A shared **math kernel** students import (they may rewrite it; they may not treat it as magic):

  - `vec3`, `dot`, `cross`, `normalize`
  - `mat4` multiply, `translate`, `rotate`, `scale`, `lookAt`, `perspective`, `ortho`
  - `barycentric(p, a, b, c)`
- Auto-grader tests for `mat4` multiply and barycentric (including a point on an edge)
- One recorded 8-minute demo per week
- A 12-triangle cube OBJ (or hardcoded) used from Week 6 onward so scenes stay comparable

---

## Assessment

| Component | Weight | Notes |
| --- | --- | --- |
| Labs (12) | 25% | Must write pixels or a shader-sized function |
| Homework (8) | 20% | Mix of code and short derivations |
| Quizzes (10) | 10% | Weekly, 10 minutes |
| Midterm (Week 8) | 15% | Written: spaces, matrices, raster, no laptop |
| Final project | 30% | Working renderer or scene + 6–8 page report |

No exam-only course. The project is the proof of mastery.

---

# 15-week lecture plan

## Week 1 — What computer graphics is

### Goal

Students see that graphics is **geometry + sampling + shading**, and they learn the course rules: a pipeline of spaces, a framebuffer, and no magic engines yet.

### Lecture

- What an image is: a 2D array of colors
- The real-time pipeline vs offline ray tracing (name both; implement rasterization)
- Object, camera, light, material, framebuffer
- Course map for 15 weeks
- Conventions: right-handed, Y-up, −Z look, CCW

### Live coding

Create a canvas, get `ImageData`, write a nested loop that fills a gradient. Put the image. Show that `(0,0)` is **top-left in the canvas**, and that we will convert from a y-up world later.

### Lab

Checkerboard; then a function `putPixel(x, y, rgb)` with bounds checks.

### Homework

1. Written: pipeline boxes from object to pixel, one sentence each.
2. Code: `clear(color)` and a 100×100 red rectangle that does not wrap.

### Quiz

Is the canvas origin the same as the world origin? Yes/no and one sentence.

---

## Week 2 — Color, pixels, and the framebuffer

### Goal

Students can talk about resolution, aspect ratio, alpha, and why 8-bit sRGB is not linear light.

### Lecture

- Pixel as a sample, not a little square (teaching level)
- RGB, alpha, premultiplied vs straight
- Framebuffer, pitch, byte order
- Aspect ratio; letterboxing
- sRGB vs linear (name it; full gamma policy in Week 11)

### Live coding

Blend two overlapping translucent rectangles. Show the bug if you interpolate 8-bit sRGB as if it were linear (bright gray in the middle of black–white).

### Lab

`drawLine` stub using DDA (next week finishes Bresenham). Alpha blend `over`.

### Homework

Written: why averaging two sRGB pixels is not the same as averaging linear radiance. One picture.

---

## Week 3 — Rasterizing lines and triangles in 2D

### Goal

A filled triangle on the canvas from three pixel coordinates. This is the heart of the course.

### Lecture

- DDA vs Bresenham (idea)
- Triangle as three half-planes vs barycentric
- Edge equations and the top-left fill rule (why cracks appear otherwise)
- Bounding box of a triangle as a reject, like AABB in computational geometry

### Live coding

Barycentric fill of one 2D triangle. Color by barycentric weights (RGB = αβγ).

### Lab

Mesh of two triangles (quad). Handle a degenerate (collinear) triangle without crashing.

### Homework

Implement `barycentric`. Tests: centroid, vertex, outside, on edge.

---

## Week 4 — Vectors, points, and frames

### Goal

Points are not vectors. Bases change. This week is the math they thought they already knew, now tied to a renderer.

### Lecture

- Point vs vector vs normal (normals transform differently — preview)
- Dot, cross, length, orthonormal bases
- Coordinate frames; change of basis
- Link to [[04 Computational Geometry]]: `orient` is a 2D cross product. Same sign story in 3D as a scalar triple product later.

### Live coding

Orbit a 2D point around the origin with `cos`/`sin`. Then do it with a 2×2 matrix. Same picture.

### Lab

Unit tests for `dot`, `cross`, `normalize`. Visual: draw basis vectors after a rotation.

### Homework

Written: why you must not add two points. Code: `lerp` and `slerp` are **not** this week; only lerp of points along a segment.

---

## Week 5 — Homogeneous coordinates and affine transforms

### Goal

4×4 matrices so translation and projection live in the same multiply.

### Lecture

- Affine = linear + translation
- Homogeneous `(x,y,z,1)` vs directions `(x,y,z,0)`
- Translate, rotate about X/Y/Z, scale
- Composition: **right to left** if column vectors (`T * R * p` means rotate first)
- Inverse of T, R, S (and when scale is non-uniform)

### Live coding

`mat4` multiply in JS. Animate translate ∘ rotate vs rotate ∘ translate. Students must see they differ.

### Lab

Rotate a triangle about its **center**, not the origin. (Translate to origin, rotate, translate back.)

### Homework

Multiply two matrices by hand (2×2 warmup, then one 4×4 with mostly zeros). Code: `rotateY`.

---

## Week 6 — Hierarchical models and scene graphs

### Goal

A solar system / robot arm from a tree of transforms. This is how glTF and Three.js scenes are stored.

### Lecture

- Model matrix as object → world
- Parent × local
- Scene graph; traversal
- Instancing as the same mesh, different M
- Normal matrix teaser: `transpose(inverse(M))` if non-uniform scale

### Live coding

Sun, Earth, Moon: three cubes or three triangles, parented. Time slider.

### Lab

A two-bone arm or a turret on a tank. Draw local axes at each node (debug).

### Homework

Written: give M_world for a node three levels deep. Code: scene graph with `children` and `localMatrix`.

---

## Week 7 — Cameras and the view transform

### Goal

`lookAt` and why the view matrix is the inverse of the camera’s world transform.

### Lecture

- Eye, target, up
- Camera basis: `w` (look), `u`, `v`
- View matrix V
- Moving the world vs moving the camera
- Optional 5-minute Three.js orbit demo as an **oracle** of the same spaces ([[08 Three.js Snippets]]), then back to student matrices

### Live coding

Implement `lookAt`. Fly the camera around the Week 6 solar system.

### Lab

WASD or sliders: eye position. A “look at origin” button.

### Homework

Written: if the camera is at `(0,0,5)` looking at origin, what is V on the diagonal (teaching numbers). Code: `lookAt` tests.

---

## Week 8 — Midterm and perspective projection

### Midterm (60–75 min)

Written. Spaces, 2D barycentric, matrix order, point vs vector, scene-graph multiply. Topic list issued in Week 7.

### Lecture (remainder)

- Orthographic vs perspective
- Frustum: fov, aspect, near, far
- Clip space and `w`
- Why we do **not** divide by `w` in the vertex shader later (GPU does it)

### Live coding

`perspective(fov, aspect, near, far)`. Draw a cube that foreshortens.

### Lab

Toggle ortho / perspective on the same scene.

---

## Week 9 — Clip, NDC, viewport, depth buffer

### Goal

A correct 3D triangle rasterizer: transform, divide, viewport, z-buffer.

### Lecture

- Clip volume; why near-plane clipping exists (optional: lerp clip, not full Sutherland–Hodgman)
- NDC in [−1,1]
- Viewport to pixels; **y-flip** because canvas y grows down
- Depth buffer; `less` vs `lequal`
- Z-fighting; never set near = 0

### Live coding

Full path: cube vertices → PVM → NDC → pixels + z-buffer. Two overlapping triangles, correct occlusion.

### Lab

Render the course cube with depth. Disable depth: show the bug. Paint z as grayscale debug.

### Homework

Written: why near too small causes z-fighting. Code: viewport transform with y-flip.

---

## Week 10 — Lighting I (Lambert)

### Goal

A lit cube that is not “each face a random color.”

### Lecture

- Vertex normals vs face normals
- Lambert: `max(0, n·l)`
- Ambient as a policy against pure black
- Light in **world** or **view** space — pick one and keep it
- Back-face culling vs lighting (they are not the same)

### Live coding

Per-face Lambert on the cube. Move the light.

### Lab

Per-vertex Lambert with barycentric interpolation of intensity (Gouraud). Compare to flat.

### Homework

Written: why a scaled non-uniform mesh needs a normal matrix. Code: `transformNormal`.

---

## Week 11 — Lighting II (Blinn-Phong) and color

### Goal

Specular highlights and a gamma-aware output.

### Lecture

- Phong vs Blinn-Phong (`h = normalize(l+v)`)
- Shininess; energy is not conserved (say it; PBR is Semester 4)
- Multiple lights: sum, then clamp or HDR teaser
- Linear vs sRGB: do lighting in linear; `pow(c, 1/2.2)` at the end

### Live coding

Blinn-Phong on the cube. Toggle gamma.

### Lab

Two lights. Debug view: normals as color (`n*0.5+0.5`).

### Homework

Written: half-vector vs reflection vector. Code: `blinnPhong(n, l, v, kd, ks, shininess)`.

---

## Week 12 — Texture mapping

### Goal

A textured quad and a textured cube. UVs are just another interpolant.

### Lecture

- UV in [0,1]; wrapping, clamping
- Perspective-correct interpolation (`u/z`, `1/z`) — teaching picture; implement if time
- Mag filter: nearest vs bilinear
- Min filter / mipmaps: name them; implement nearest for the lab
- Texture as albedo; still multiply by Lambert

### Live coding

Load an image into an array. Sample nearest. Textured quad facing the camera, then on the cube.

### Lab

Checkerboard procedural texture if image load is blocked (`file://`). UV debug coloring.

### Homework

Written: why affine UV interpolation looks wrong on a perspective quad. Code: `sampleNearest(tex, u, v)`.

---

## Week 13 — The same scene on the GPU

### Goal

Students map **their** renderer onto WebGL2 (and optionally Three.js) without abandoning what they wrote.

### Lecture

- Vertex shader = transform to clip
- Fragment shader = lighting + texture
- Attributes, uniforms, buffers
- Depth test, cull face
- Where Three.js hides V and P (`camera.matrixWorldInverse`, `projectionMatrix`)
- Joint note with computational geometry: picking is ray vs triangle, not “the engine knows”

### Live coding

Port the course cube: one WebGL2 program, Lambert, one texture. Use [[WebGL/demos/index.html]] as the triangle-through-cube sequence if students are stuck on boilerplate — they still must explain each uniform.

### Lab

**Project checkpoint.** Software **or** WebGL vertical slice: mesh + camera + light + texture + depth.

### Homework

Project only. Written: a table “my CPU function → GPU stage.”

---

## Week 14 — Project studio

No new theory. Desk review: kernel (`mat4`, barycentric, z-buffer or shaders), visualizer, one ugly mesh, README.

### Scope cuts

| If they are behind | Cut |
| --- | --- |
| PBR / shadows | Lambert + one texture |
| Full glTF loader | Hardcoded cube + one OBJ |
| Deferred / post | Forward software or one WebGL pass |
| Beautiful UI | Canvas + keyboard |
| Three.js scene they cannot explain | Back to software rasterizer |

A correct z-buffer on a plain canvas beats a broken `gltf` dump.

---

## Week 15 — Project presentations

12 minutes + 5 minutes questions. Live demo, repo, 6–8 page report, 30-second recording.

---

# Final project (choose one)

Every project must implement **the pipeline or a stage of it**, not only call Three.js. A library is allowed for windowing and image decode, not for the student claim (“I wrote a renderer”).

| Project | Must include | Why it fits IGWT |
| --- | --- | --- |
| Software mesh viewer | PVM, raster, z-buffer, Lambert, texture | Core course |
| Solar system / robot | Scene graph + camera | Animation, configurators |
| First-person room | lookAt, collision AABB optional | Games, XR later |
| OBJ + MTL viewer | Normals, UVs, multiple materials | Asset pipeline |
| CPU → GPU port | Same scene in software and WebGL | Bridge to Semester 3 |
| 2D UI renderer | Transforms + textured quads, no 3D | Weaker; allow only if 3D math is already solid |

### Project rubric

| Criterion | Weight |
| --- | --- |
| Correct pipeline (tests + one debug view) | 30% |
| Visual explanation of a stage | 20% |
| Code quality and repository | 15% |
| Report (spaces, limitations, citations) | 20% |
| Presentation and live demo | 15% |

---

# Week-by-week summary

| Week | Topic | Students implement | Later-course payoff |
| ---: | --- | --- | --- |
| 1 | Images, pipeline | `putPixel`, gradient | All labs |
| 2 | Color, framebuffer | Alpha over | Compositing |
| 3 | 2D raster | Barycentric triangle | GPU fragments |
| 4 | Vectors and frames | `dot`/`cross` | Lighting |
| 5 | Homogeneous / affine | `mat4`, rotate-about-center | Every engine |
| 6 | Scene graph | Parent × local | glTF, Three.js |
| 7 | Camera | `lookAt` | Orbit / FPS |
| 8 | Midterm + projection | `perspective` | Clip space |
| 9 | NDC, viewport, depth | z-buffer cube | Hidden surface |
| 10 | Lambert | `n·l` | Materials |
| 11 | Blinn-Phong, gamma | Specular + sRGB out | PBR later |
| 12 | Textures | UV sample | glTF albedo |
| 13 | WebGL map | Same cube on GPU | Semester 3 |
| 14 | Studio | Project | Portfolio |
| 15 | Presentations | Demo + report | Graduation evidence |

---

# Recommended textbooks

Assign **one** primary book. Use the others as references.

| Book / site | Use |
| --- | --- |
| Marschner & Shirley — *Fundamentals of Computer Graphics* | Primary theory |
| Scratchapixel (rasterization, barycentric, cameras) | Free weekly companion |
| Angel & Shreiner — *Interactive Computer Graphics* | OpenGL-shaped pipeline |
| Hughes et al. — *Computer Graphics: Principles and Practice* | Reference depth |
| Akenine-Möller et al. — *Real-Time Rendering* | **Not** the undergraduate primary; steal pictures for Week 13+ |

Do not assign a Vulkan spec. Do not assign *Physically Based Rendering* as required reading in Semester 2.

---

# What to skip in a first undergraduate course

Say this explicitly in Week 1 so the course does not balloon.

- Full perspective-correct interpolation proof (picture + optional lab extra)
- Full frustum clipping of triangles (clip against near, or drop triangles that straddle near)
- Shadow maps, SSAO, deferred, IBL, HDR pipelines
- Write-your-own GPU / WebGPU (Semester 4–5)
- Global illumination
- Three.js as the weekly implementation

Mention them. Do not grade them.

---

# Faculty checklist for the first offering

1. Write `vec3`/`mat4`/`barycentric` and a one-triangle rasterizer in Week −2.
2. Record one 8-minute demo for Weeks 1–9 before the semester starts.
3. Prepare 10 quiz PDFs and the midterm.
4. Publish 3 project starter repos (software viewer, scene graph, WebGL cube).
5. Schedule Week 13 as a joint session with Computational Geometry Week 13 if both run.
6. Collect every student project into the annual IGWT exhibition.
7. Tell students where [[WebGL/]] and [[ThreeJS/]] live — **after** they can put a triangle in a framebuffer.

---

# One-sentence teaching principle

Students should leave this course able to **look at a wrong picture, name the pipeline stage that failed, and write a debug view for it** (normals, UVs, depth, NDC).
