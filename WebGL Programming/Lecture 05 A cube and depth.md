# Lecture 5 — A cube and depth

**Week 5 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** indices, DEPTH_TEST, cull  
**Success check:** Indexed cube.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: indices, DEPTH_TEST, cull | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
enable DEPTH_TEST
Cube.
cull.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Hidden surfaces. Same as CG I z-buffer.

**Ask:** Indexed cube? Wait seven seconds. Take two answers.

**Board:** parked strip. Then enable DEPTH_TEST.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *indices, DEPTH_TEST, cull*.

**Do not:** No depth clear.

### Minutes 10–12 — Frame

**Say:** Today’s question: indices, DEPTH_TEST, cull. Kernel: indices, DEPTH_TEST, cull. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: no depth clear.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Hidden surfaces. Same as CG I z-buffer.

**Say:** Winding. CCW front.

**Say:** Demo. 04 cube, conventions.

**Ask:** Indexed cube? Wait seven seconds. Take two answers.

**They do:** On paper: cull toggle.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Cube with depth; toggle depth to show painter bugs.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cull toggle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: cull toggle.; wireframe extra.. Homework: Written: GPU depth vs CPU z-buffer.; Code: cube.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: indices, DEPTH_TEST, cull | Plant the first common mistake. |
| 10–30 | Cube with depth; toggle depth to show painter bugs. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. cull toggle.
2. wireframe extra.

---

## Homework

1. Written: GPU depth vs CPU z-buffer.
2. Code: cube.

---

## Quiz next meeting (they hear this now)

1. DEPTH_TEST (3)
2. CCW (3)
3. clear depth (4)


## Snippet

```js
gl.enable(gl.DEPTH_TEST);
gl.enable(gl.CULL_FACE);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Hidden surfaces.** Same as CG I z-buffer. Now the GPU.

**2. Winding.** CCW front. Inside-out = winding or mirrored scale.

**3. Demo.** 04 cube, conventions.

---

## Common mistakes

1. no depth clear.
2. near=0.

## If we run long, cut

Demo

## If we run short, add

wireframe extra.
