# Lecture 1 — GPU pipeline and a triangle

**Week 1 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** WebGL2 context; clip-space triangle; gl_Position is clip, not pixels  
**Success check:** they get a red triangle from getContext('webgl2') with compile/link logs printed; they can say what gl_Position is

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `WebGL/demos/index.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: a first triangle without Three.js | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
CPU buffers → VS → raster → FS → framebuffer

gl_Position = clip (xyzw). GPU does the divide.
NDC after divide: xyz in [−1,1]

RH, Y-up, camera looks −Z
CCW front     column-major     P * V * M * vec4(p,1)

getContext('webgl2')   —  not Three.js
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** If they cannot explain gl_Position, they are not allowed to hide in Three.js yet. Today is raw WebGL2. A black screen is a checklist, not a personality.

**Ask:** Is gl_Position in pixels? Wait seven seconds. Want: no — clip space; the GPU divides by w.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *WebGL2 context, first triangle*.

**Do not:** Starting in Three.js.

### Minutes 8–12 — Frame

**Say:** Canvas, WebGL2 context, two shaders, one buffer, drawArrays TRIANGLES. Conventions freeze now: right-handed, Y-up, look −Z, CCW, column-major P*V*M. Week 1 triangle lives in clip with w=1 so it is already NDC. Matrices wait until week 7 — we still write the product on the board so the name exists.

**Ask:** Who fills the buffer — CPU or GPU?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Pipeline every lecture: VBO → VS → raster → FS → FBO. Draw it. Three.js is next course.

**Board:** gl_Position clip vs NDC vs pixels. Circle w. Do not divide in the VS.

**Say:** Compile log and link log are different. Print both. Clear color you can see: 0.10, 0.10, 0.12.

**Ask:** Why CCW? Want: OpenGL default front face.

**They do:** On paper: pipeline boxes plus one line: gl_Position = vec4(a_position, 0, 1).

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Typed triangle from WebGL/demos/01-triangle.html. Local _gl.js, no CDN. Plant getContext('webgl') then 'webgl2'. Plant a 0×0 canvas. Read the compile log out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Clear color you can see, then the three clip verts. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: visible clear + resize backing store. Homework: pipeline boxes; a triangle. Quiz: getContext webgl2, where logs, why not Three.js yet.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | getContext('webgl2') + clear | Plant webgl1 or Three.js. Fix: raw WebGL2. |
| 10–30 | 01-triangle.html typed | Plant missing #version 300 es. Read the log. |
| 30–45 | gl_Position on the board | Plant pixels. Write clip → NDC. |
| 45–60 | They type three verts | Circulate. No CDN. Serve if file:// dies. |

Point them at `WebGL/demos/index.html` as the after-class check, not as the lecture.

---

## Lab

1. Clear color you can see.
2. Resize canvas backing store.

---

## Homework

1. Written: pipeline boxes.
2. Code: triangle.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const gl = canvas.getContext('webgl2');
```

## Extra exercises

See [[WebGL Programming/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Starting in Three.js.
2. 0×0 canvas.

## If we run long, cut

P*V*M multiplication today. Keep clip triangle + logs.

## If we run short, add

Resize canvas backing store with devicePixelRatio named.
