# Lecture 1 — What computer graphics is

**Week 1 of 15** · Computer Graphics I  
**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `putPixel(x, y, rgb)` on `ImageData`  
**Board first:** object → world → view → clip → NDC → pixels  
**Success check:** they can point at six boxes and say which one `putPixel` lives in (pixels).

Session guide convention: [[Teaching/24 Session Guides]].


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computer Graphics/code/01-putpixel.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — object → world → view → clip → NDC → pixels.
- Parked strip: `Lecture 1 | What computer graphics is | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
object → world → view → clip → NDC → pixels
Six-space pipeline.
Framebuffer as a grid; one pixel’s RGBA.
The 15-week map as five boxes: pixels, transforms, camera, shade, GPU.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Classroom moves (75 min)

| Min | Phase | Say / board / slide / they do |
| ---: | --- | --- |
| 0–10 | Hook | **Say:** a computer has no cube, only numbers. **Board:** `geometry + camera + light + material → framebuffer`. **Slide:** one pretty still (optional). **They do:** write “what is an image?” in one line. |
| 10–25 | Build | Raster vs ray. **Board:** two loops (triangles vs pixels). **Slide:** none. **Ask:** which one is WebGL? Wait. |
| 25–45 | Build | Six spaces. **Board:** six boxes, fill slowly. **Slide:** none — this *is* the lecture. **Do not:** derive `P`. |
| 45–60 | Show | Conventions. **Board:** RH, +Y, look −Z, `P*V*M`, CCW. **Slide:** [[WebGL/01 Conventions]] screenshot only if the board is full. |
| 60–70 | Contract | Assessment table. **Slide:** 1, the table, 20pt. Then sit down the slide. |
| 70–75 | Land | **Say:** live coding is `putPixel`. Canvas y is down. Lab hook: checkerboard. **Do not:** “any questions?” |

**Slides today (cap: 4):** pretty still; assessment table; optional conventions page; nothing else.

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Why this course exists (a picture is an array) |
| 10–25 | Rasterization vs ray tracing |
| 25–45 | Pipeline of spaces; who does what |
| 45–60 | Conventions; what we will not implement |
| 60–70 | Course contract, assessment, 15-week map |
| 70–75 | Preview `putPixel`, then stand up for live coding |

---

## Learning goals

1. Define an image as a 2D array of colors plus a framebuffer.
2. Name rasterization and ray tracing and say which one this course implements.
3. Recite the space chain: object → world → view → clip → NDC → pixels.
4. State the course conventions (handedness, up, look, matrix order, winding).
5. Write a pixel without wrapping the buffer.

---

## 1. Opening (10 min)

A computer has no idea what a “cube” is. It has numbers: positions, indices, colors. Graphics is the craft of turning those numbers into an array of pixels fast enough to animate.

Write:

```
geometry + camera + light + material  →  framebuffer
```

This program (IGWT) will later put that framebuffer on a website, a configurator, and XR. This semester we **build the arrow**.

Computational geometry (if they are in it) answers “which triangle? does it hit?” This course answers “what color is this pixel?”

---

## 2. Two ways to make a picture (15 min)

### Rasterization (this course)

For each triangle:

1. Transform vertices to screen.
2. Find which pixels the triangle covers.
3. Shade those pixels (depth, light, texture).

The GPU does this. We will do it in JavaScript first so the GPU is not a shrine.

### Ray tracing (name only)

For each pixel, shoot a ray, find the nearest surface, shade. Offline films; also hardware RT later. We do **not** implement a path tracer here.

Draw both. Students should be able to say: games and WebGL are rasterization-first.

---

## 3. The pipeline of spaces (20 min)

Draw six boxes. Fill them slowly.

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

## 4. Conventions and skip list (15 min)

Freeze [[WebGL/01 Conventions]] now.

- Right-handed, +Y up, camera looks **−Z**
- Column vectors: `P * V * M * p`
- CCW winding is front
- Radians in code

**We will not implement this term:** shadow maps, deferred, PBR, Vulkan, a glTF parser as the core claim, Three.js as the weekly lab.

Three.js may appear for **five minutes** in Week 7 as a camera oracle. Students still write `lookAt`.

---

## 5. Course contract (10 min)

### Assessment

Labs 25%, homework 20%, quizzes 10%, midterm 15%, project 30%.

### How a week works

Lecture → live coding on a canvas → lab → homework → 10-minute quiz.

### Language

JavaScript + Canvas `ImageData`. WebGL2 in Week 13.

---

## Live coding (60 min)

Must work by the end of class:

1. Canvas in the DOM, backing store set (not 0×0).
2. `getImageData` / `putImageData` each frame (or after a draw).
3. `putPixel(x, y, r, g, b)` with integer coordinates and **bounds checks**.
4. A vertical gradient (y maps to intensity).
5. Print: width, height, `data.length === width * height * 4`.

Talk while typing:

- “Canvas y grows **down**. World y will grow **up**. We will flip in the viewport, Week 9, not today.”
- “Index is `(y * width + x) * 4`. Off-by-one here is a black screen later.”
- “I do not call `fillRect` for the renderer. `fillRect` is a UI overlay.”

Starter they leave with:

```js
export function putPixel(img, x, y, r, g, b, a = 255) {
  x = x | 0; y = y | 0;
  if (x < 0 || y < 0 || x >= img.width || y >= img.height) return;
  const i = (y * img.width + x) * 4;
  img.data[i] = r;
  img.data[i + 1] = g;
  img.data[i + 2] = b;
  img.data[i + 3] = a;
}
```

---

## Lab

1. `clear(img, r, g, b)`.
2. Checkerboard with cell size 16.
3. Filled axis-aligned rectangle function that **clips** to the canvas.
4. Do not wrap coordinates (`x % width` is a bug unless you are writing a torus demo).

Done when a TA can resize the canvas and the checkerboard still tiles without throwing.

---

## Homework

Due start of Week 2.

1. Pipeline diagram, six boxes, one sentence each.
2. `putPixel` + `clear` + rectangle, 8 tests (corners, off-canvas, 1×1).
3. Written: why we store 4 bytes per pixel. What is alpha **this week**? (We will blend in Week 2.)

---

## Quiz (10 min)

1. Rasterization vs ray tracing: which loops over triangles first? (2 pts)
2. Name the six spaces in order. (3 pts)
3. Matrix product in this course: `P * V * M` or `M * V * P`? (2 pts)
4. Canvas `(0,0)` is which corner? (3 pts)

---

## Common mistakes

- Setting CSS size and forgetting `canvas.width` / `canvas.height`.
- Using `fillRect` and calling it a renderer.
- Assuming world +Y is canvas +Y.
- Starting in Three.js “because the professor opened it once.”

---

## Board drawings

1. Six-space pipeline.
2. Framebuffer as a grid; one pixel’s RGBA.
3. The 15-week map as five boxes: pixels, transforms, camera, shade, GPU.


## Extra exercises

See [[Computer Graphics/exercises/Week 01]].
