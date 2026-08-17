# Lecture 9 — WGSL triangle

**Week 9 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** vertex_index, clip  
**Success check:** A WGSL vs/fs pair.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: vertex_index, clip | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
@vertex @fragment
Triangle.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** WGSL. Typed.

**Ask:** A WGSL vs/fs pair? Wait seven seconds. Take two answers.

**Board:** parked strip. Then @vertex @fragment.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *vertex_index, clip*.

**Do not:** Three.js WebGPURenderer as the only lab with no WGSL read.

### Minutes 10–12 — Frame

**Say:** Today’s question: vertex_index, clip. Kernel: vertex_index, clip. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: three.js WebGPURenderer as the only lab with no WGSL read.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** WGSL. Typed.

**Say:** Canvas. `navigator.gpu.requestAdapter` then `configure` the context.

**Say:** Errors. Validation is loud.

**Ask:** A WGSL vs/fs pair? Wait seven seconds. Take two answers.

**They do:** On paper: uniform time extra.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Colored triangle WGSL; resize.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** uniform time extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: uniform time extra.; compare GLSL side by side.. Homework: Written: GLSL vs WGSL table (6 rows).; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: vertex_index, clip | Plant the first common mistake. |
| 10–30 | Colored triangle WGSL; resize. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. uniform time extra.
2. compare GLSL side by side.

---

## Homework

1. Written: GLSL vs WGSL table (6 rows).
2. code.

---

## Quiz next meeting (they hear this now)

1. @builtin(position) (3)
2. bind group (4)
3. clip z (3)


## Snippet

```wgsl
@vertex fn vs(@builtin(vertex_index) i: u32) -> @builtin(position) vec4f { /* ... */ }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. WGSL.** Typed. `@location`. No GLSL preprocessor soup.

**2. Canvas.** `navigator.gpu.requestAdapter` then `configure` the context.

**3. Errors.** Validation is loud. Good.

---

## Common mistakes

1. three.js WebGPURenderer as the only lab with no WGSL read.
2. copying a full sample unread.

## If we run long, cut

Errors

## If we run short, add

compare GLSL side by side.
