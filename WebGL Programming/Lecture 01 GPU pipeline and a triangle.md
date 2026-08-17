# Lecture 1 — GPU pipeline and a triangle

**Week 1 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** WebGL2 context, first triangle  
**Success check:** Create a WebGL2 context.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `WebGL/demos/index.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: WebGL2 context, first triangle | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
CPU buffers → VS → raster → FS → framebuffer
Pipeline.
Triangle.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Struggle a little. [[02 Curriculum Design Advice]] Course 7.

**Ask:** Create a WebGL2 context? Wait seven seconds. Take two answers.

**Board:** parked strip. Then CPU buffers → VS → raster → FS → framebuffer.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *WebGL2 context, first triangle*.

**Do not:** Starting in Three.js.

### Minutes 8–12 — Frame

**Say:** Today’s question: WebGL2 context, first triangle. Kernel: WebGL2 context, first triangle. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Starting in Three.js.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Struggle a little. [[02 Curriculum Design Advice]] Course 7.

**Say:** Pipeline. Every lecture redraws GPU → VBO → VS → raster → FS → FBO.

**Say:** Conventions. [[WebGL/01 Conventions]].

**Ask:** Create a WebGL2 context? Wait seven seconds. Take two answers.

**They do:** On paper: Clear color you can see.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Typed triangle from demo 01; print compile/link logs.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Clear color you can see.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Clear color you can see.; Resize canvas backing store.. Homework: Written: pipeline boxes.; Code: triangle.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: WebGL2 context, first triangle | Plant the first common mistake. |
| 10–30 | Typed triangle from demo 01; print compile/link logs. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. WebGL2 getContext (2)
2. where logs (4)
3. why not Three.js yet (4)


## Snippet

```js
const gl = canvas.getContext('webgl2');
```

## Extra exercises

See [[WebGL Programming/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Struggle a little.** [[02 Curriculum Design Advice]] Course 7. Frameworks hide the pipeline.

**2. Pipeline.** Every lecture redraws GPU → VBO → VS → raster → FS → FBO.

**3. Conventions.** [[WebGL/01 Conventions]]. Demo: [[WebGL/demos/index.html]] 01.

---

## Common mistakes

1. Starting in Three.js.
2. 0×0 canvas.

## If we run long, cut

Conventions

## If we run short, add

Resize canvas backing store.
