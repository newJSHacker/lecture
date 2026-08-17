# Lecture 13 — The same scene on the GPU

**Week 13 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** same cube: CPU putPixel/bary/z/PVM/Lambert/sample → GPU fragment/raster/DEPTH/gl_Position/texture(); Three.js is an oracle  
**Success check:** they fill u_model, u_view, u_proj from their mat4 (or a mapping table if Three.js); software-only slice is complete if WebGL failed

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/13-lambert.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: map their renderer onto WebGL2; do not abandon what they wrote | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
CPU putPixel          →  fragment write
barycentric fill      →  rasterizer (fixed)
z-buffer              →  DEPTH_TEST
P * V * M             →  vertex gl_Position
Lambert / Blinn       →  fragment shader
sampleNearest         →  texture() + sampler

Three.js: projectionMatrix = P
          matrixWorldInverse = V
          mesh.matrixWorld = M
Raycaster = Comp Geo, not lighting
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Week 13 is the same scene on the GPU, not a new engine. Joint note with Computational Geometry: picking is ray vs triangle. A library is windowing and decode, not the student claim ‘I wrote a renderer.’

**Ask:** matrixWorldInverse is which matrix? Wait. Want: V.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *The same scene on the GPU*.

**Do not:** Using Three.js for the checkpoint with no mapping table.

### Minutes 10–12 — Frame

**Say:** Students may copy WebGL boilerplate; they must fill uniforms from their math if they claim the math. Checkpoint: mesh, camera, one light, texture or debug UV/n, depth, README student-vs-library. Black-screen checklist: canvas size, camera, near, winding. Do not invent fps. Do not grow fov until the cube ‘shows up’ — fix V.

**Ask:** May Three.js Raycaster be the student picking algorithm? Want: no.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Leave the GPU column empty; fill with the class.

**Board:** payoff table. Vertex vs fragment boxes. Same cube, two windows.

**Say:** Vertex shader is Weeks 5–9. Fragment is Weeks 10–12. enable DEPTH_TEST, CULL_FACE, CCW.

**Ask:** Where does gl_Position sit in the space chain? Want: clip.

**They do:** On paper: CPU function → GPU stage, one page. That table is homework in the repo.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Port the course cube to WebGL2: Lambert, one texture, same lookAt. Side-by-side software vs WebGL if possible. Use WebGL/demos/index.html (01–04, 06) if stuck on boilerplate. Demo 16-webgl-cube.html. When it mismatches: NDC y, winding, linear/sRGB, light space. Plant Three.js checkpoint with no mapping table.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Point at u_proj * u_view * u_model in the shader. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab is the project checkpoint. Software-only is complete. WebGL-only is complete if they explain each uniform. Both is the A path. Homework: project + the table. Quiz: gl_Position, depth test, black-screen cause, matrixWorldInverse, Raycaster.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Fill the payoff table live | They name GPU stages. |
| 15–40 | WebGL2 cube uniforms from their mat4 | Plant sRGB texture vs CPU gamma. |
| 40–50 | Three.js oracle: P, V, M hiding places | Close it. Table still required. |
| 50–60 | Picking sentence | Ray vs triangle, not ‘the engine knows.’ |

Point them at `Computer Graphics/code/13-lambert.html` as the after-class check, not as the lecture.

---

## Lab

_(none this meeting)_

---

## Homework

_(none this meeting)_

---

## Quiz next meeting (they hear this now)

1. Where does `gl_Position` sit in the space chain? (2 pts)
2. Depth test replaces which CPU structure? (2 pts)
3. Name one black-screen cause. (2 pts)
4. `matrixWorldInverse` is which matrix? (2 pts)
5. May Three.js Raycaster be the student picking algorithm? (2 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. The payoff table (20 min).** Walk slowly. One sentence from this course, one from WebGL.
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

**2. WebGL2 minimum (20 min).** - Compile / link; print shader logs
- One `vec3` position attribute, one `vec2` uv
- Uniforms: three mat4, light dir, sampler
- `enable(DEPTH_TEST)`, `enable(CULL_FACE)`, CCW
- Black-screen checklist from conventions (canvas size, camera, near plane, winding)
Vertex shader is Weeks 5–9. Fragment shader is Weeks 10–12.
---

**3. Three.js (15 min).** `camera.projectionMatrix` is P. `camera.matrixWorldInverse` is V. `mesh.matrixWorld` is M. `MeshPhongMaterial` is Week 11. `Raycaster` is computational geometry, not a lighting topic.
If they submit a Three.js scene for the **checkpoint**, they still need a one-page table mapping Object3D to their software renderer. No table, incomplete.
---

**4. Picking (10 min).** Click → ray → triangle (CG Weeks 2, 9, 13). The GPU picture does not replace the predicate.
---

---

## Common mistakes

1. Using Three.js for the checkpoint with no mapping table.
2. sRGB texture sampled as linear in WebGL (gamma surprise vs CPU).
3. Growing EPS / fov until the cube “shows up” instead of fixing V.

## If we run long, cut

Second shader pass. Keep one program + the table.

## If we run short, add

Print shader compile logs.
