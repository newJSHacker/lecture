# Lecture 13 — The same scene on the GPU

**Time:** 75 min lecture + 60 min live coding  
**Live coding:** WebGL2 cube = student PVM + Lambert + texture  
**Lab:** project checkpoint (vertical slice)  
**Homework:** project only

---


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computer Graphics/code/13-lambert.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — today's picture.
- Parked strip: `Lecture 13 | The same scene on the GPU | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
Payoff table (leave the GPU column empty; fill with the class).
Vertex vs fragment shader boxes.
Same cube, two windows: CPU / GPU.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 12 |
| 10–30 | CPU function → GPU stage table |
| 30–50 | WebGL2: attributes, uniforms, depth, cull |
| 50–65 | Where Three.js hides V and P |
| 65–75 | Picking is geometry, not “the engine” |

---

## Learning goals

1. Map every stage of the software renderer to a GPU name.
2. Write (or complete) a WebGL2 program for the course cube.
3. Point to `u_proj * u_view * u_model` in a shader.
4. Use Three.js only as a labeled oracle, not as the checkpoint.
5. Freeze project scope.

---

## 1. The payoff table (20 min)

Walk slowly. One sentence from this course, one from WebGL.

| Student CPU | GPU / API |
| --- | --- |
| `putPixel` | fragment writes to framebuffer |
| barycentric fill | rasterizer (fixed) |
| z-buffer | `DEPTH_TEST` |
| `P * V * M` | vertex shader `gl_Position` |
| Lambert / Blinn | fragment shader |
| `sampleNearest` | `texture()` + sampler |
| scene graph | CPU updates uniforms / instancing |
| y-flip viewport | viewport + NDC; canvas still y-down in UI |

Open [[WebGL/01 Conventions]] and [[WebGL/demos/index.html]]. Demos 01–04 and 06 are the path. Students may copy boilerplate; they must **fill** `u_model`, `u_view`, `u_proj` from their `mat4` code if they claim the math.

---

## 2. WebGL2 minimum (20 min)

- Compile / link; print shader logs
- One `vec3` position attribute, one `vec2` uv
- Uniforms: three mat4, light dir, sampler
- `enable(DEPTH_TEST)`, `enable(CULL_FACE)`, CCW
- Black-screen checklist from conventions (canvas size, camera, near plane, winding)

Vertex shader is Weeks 5–9. Fragment shader is Weeks 10–12.

---

## 3. Three.js (15 min)

`camera.projectionMatrix` is P. `camera.matrixWorldInverse` is V. `mesh.matrixWorld` is M. `MeshPhongMaterial` is Week 11. `Raycaster` is computational geometry, not a lighting topic.

If they submit a Three.js scene for the **checkpoint**, they still need a one-page table mapping Object3D to their software renderer. No table, incomplete.

---

## 4. Picking (10 min)

Click → ray → triangle (CG Weeks 2, 9, 13). The GPU picture does not replace the predicate.

---

## Live coding (60 min)

Port the course cube to WebGL2. Same texture as Week 12. Move the camera with the same `lookAt`. Side-by-side if possible: canvas software vs WebGL.

When it mismatches: NDC y, winding, linear/sRGB, light space.

---

## Lab (checkpoint)

Must be true:

- Mesh (at least the cube)
- Camera (`lookAt` or documented Three.js camera)
- One light
- One texture **or** a debug UV/normal view
- Depth correct
- README: how to run; which files are student math vs library

Software-only slice is **complete** if WebGL failed. WebGL-only slice is complete if they can explain each uniform. Both is the A path.

---

## Homework

Project. Written: CPU → GPU table, one page, in the repo.

---

## Quiz (10 min)

1. Where does `gl_Position` sit in the space chain? (2 pts)
2. Depth test replaces which CPU structure? (2 pts)
3. Name one black-screen cause. (2 pts)
4. `matrixWorldInverse` is which matrix? (2 pts)
5. May Three.js Raycaster be the student picking algorithm? (2 pts)

---

## Common mistakes

- Using Three.js for the checkpoint with no mapping table.
- sRGB texture sampled as linear in WebGL (gamma surprise vs CPU).
- Growing EPS / fov until the cube “shows up” instead of fixing V.

---

## Board drawings

1. Payoff table (leave the GPU column empty; fill with the class).
2. Vertex vs fragment shader boxes.
3. Same cube, two windows: CPU / GPU.


## Extra exercises

See [[Computer Graphics/exercises/Week 13]].
