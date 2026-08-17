# Lecture 1 — What computer graphics is

**Week 1 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** putPixel(x, y, rgb) on Canvas ImageData; six spaces; RH +Y look −Z; P*V*M; CCW  
**Success check:** they can point at six boxes and say putPixel lives in pixels, not in clip

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Computer Graphics/code/01-putpixel.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: see that graphics is geometry + sampling + shading, with no magic engine yet | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
object → world → view → clip → NDC → pixels

geometry + camera + light + material  →  framebuffer

RH  +Y up  look −Z
p_clip = P * V * M * vec4(p,1)    CCW front

putPixel: index = (y * width + x) * 4
canvas (0,0) = top-left; world +Y is not canvas +Y
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | One pretty still of a cube | do not lecture the pipeline from the still |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** A computer has no cube, only numbers. Today we freeze the pipeline and write a pixel. Computational geometry asks which triangle; we ask what color this pixel is. Three.js is not this week’s lab.

**Ask:** If the picture is an array, where does putPixel live — object space or pixels? Wait seven seconds.

**Board:** parked strip. Then object → world → view → clip → NDC → pixels.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`putPixel(x, y, rgb)` on `ImageData`*.

**Do not:** Setting CSS size and forgetting `canvas.width` / `canvas.height`.

### Minutes 8–12 — Frame

**Say:** Rasterization loops triangles then pixels. Ray tracing loops pixels then rays — name only; we implement raster. Do not derive P today. Promise Week 8. Conventions freeze now: right-handed, +Y, camera looks −Z, column vectors P*V*M, CCW. Radians in code.

**Ask:** Which loop does WebGL run first — triangles or rays?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw geometry + camera + light + material → framebuffer. That arrow is the semester.

**Board:** six boxes, fill slowly. Object, world, view, clip (w matters), NDC, pixels. Who runs which later: CPU builds M,V,P; vertex shader object→clip; rasterizer fragments; fragment shader color.

**Say:** Skip list on the board: shadows, deferred, PBR, Vulkan, glTF as the claim, Three.js as the weekly lab. Assessment: labs 25, hw 20, quizzes 10, midterm 15, project 30. Language: JS + ImageData. WebGL2 in Week 13 as a map, not the engine.

**Ask:** P*V*M or M*V*P in this course? Want: P*V*M.

**They do:** On paper: six boxes, one sentence each. Circle the box putPixel writes.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Canvas, backing store not 0×0, getImageData/putImageData. putPixel with integer coords and bounds checks. Vertical gradient. Print width, height, data.length === width*height*4. Demo Computer Graphics/code/01-putpixel.html. Plant fillRect as ‘the renderer.’ Plant CSS size without canvas.width.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Write putPixel with the index formula and a clip. Eight minutes. No fillRect.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the six boxes and the conventions. Lab: clear, checkerboard 16, clipped rectangle — do not wrap x%width. Homework: pipeline diagram; putPixel tests (corners, off-canvas, 1×1). Quiz: raster vs ray, six spaces, P*V*M, canvas (0,0).

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Canvas + ImageData | Plant CSS size, backing store 0×0. Black screen. |
| 10–30 | putPixel + bounds | Plant missing clip; wrap as a torus bug. |
| 30–45 | Gradient; y down | Say: world +Y flip is Week 9 viewport, not today. |
| 45–60 | They write checkerboard cells | Circulate. No Three.js. |

Point them at `Computer Graphics/code/01-putpixel.html` as the after-class check, not as the lecture.

---

## Lab

1. `clear(img, r, g, b)`.
2. Checkerboard with cell size 16.
3. Filled axis-aligned rectangle function that **clips** to the canvas.
4. Do not wrap coordinates (`x % width` is a bug unless you are writing a torus demo).

---

## Homework

1. Pipeline diagram, six boxes, one sentence each.
2. `putPixel` + `clear` + rectangle, 8 tests (corners, off-canvas, 1×1).
3. Written: why we store 4 bytes per pixel. What is alpha **this week**? (We will blend in Week 2.)

---

## Quiz next meeting (they hear this now)

1. Rasterization vs ray tracing: which loops over triangles first? (2 pts)
2. Name the six spaces in order. (3 pts)
3. Matrix product in this course: `P * V * M` or `M * V * P`? (2 pts)
4. Canvas `(0,0)` is which corner? (3 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Opening (10 min).** A computer has no idea what a “cube” is. It has numbers: positions, indices, colors. Graphics is the craft of turning those numbers into an array of pixels fast enough to animate.
Write:
```
geometry + camera + light + material  →  framebuffer
```
This program (IGWT) will later put that framebuffer on a website, a configurator, and XR. This semester we **build the arrow**.
Computational geometry (if they are in it) answers “which triangle? does it hit?” This course answers “what color is this pixel?”
---

**2. Two ways to make a picture (15 min).** ### Rasterization (this course)
For each triangle:
1. Transform vertices to screen.
2. Find which pixels the triangle covers.
3. Shade those pixels (depth, light, texture).
The GPU does this. We will do it in JavaScript first so the GPU is not a shrine.
### Ray tracing (name only)
For each pixel, shoot a ray, find the nearest surface, shade. Offline films; also hardware RT later. We do **not** implement a path tracer here.
Draw both. Students should be able to say: games and WebGL are rasterization-first.
---

**3. The pipeline of spaces (20 min).** Draw six boxes. Fill them slowly.
| Space | Question |
| --- | --- |
| Object | Where is this vertex on the mesh? |
| World | Where is it in the scene? |
| View | Where is it relative to the camera? |
| Clip | After projection, before divide; `w` matters |
| NDC | After divide; xyz typically in [−1, 1] |
| Pixels | Which framebuffer index? |
The product they will write by Week 9:
```
p_clip = P * V * M * vec4(p_obj, 1)
p_ndc  = p_clip.xyz / p_clip.w
p_pix  = viewport(p_ndc)
```
Do not derive P today. Promise Week 8.
**Who runs which box later**
- CPU / your JS: build M, V, P, submit vertices
- Vertex shader: object → clip
- Rasterizer (fixed): clip → fragments
- Fragment shader: color
Week 13 is this table with WebGL names.
---

**4. Conventions and skip list (15 min).** Freeze [[WebGL/01 Conventions]] now.
- Right-handed, +Y up, camera looks **−Z**
- Column vectors: `P * V * M * p`
- CCW winding is front
- Radians in code
**We will not implement this term:** shadow maps, deferred, PBR, Vulkan, a glTF parser as the core claim, Three.js as the weekly lab.
Three.js may appear for **five minutes** in Week 7 as a camera oracle. Students still write `lookAt`.
---

**5. Course contract (10 min).** ### Assessment
Labs 25%, homework 20%, quizzes 10%, midterm 15%, project 30%.
### How a week works
Lecture → live coding on a canvas → lab → homework → 10-minute quiz.
### Language
JavaScript + Canvas `ImageData`. WebGL2 in Week 13.
---

---

## Common mistakes

1. Setting CSS size and forgetting `canvas.width` / `canvas.height`.
2. Using `fillRect` and calling it a renderer.
3. Assuming world +Y is canvas +Y.
4. Starting in Three.js “because the professor opened it once.”

## If we run long, cut

Who-runs-which GPU table. Keep six boxes + putPixel.

## If we run short, add

Alpha as a fourth byte name; blend is Week 2.
