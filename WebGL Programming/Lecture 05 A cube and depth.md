# Lecture 5 — A cube and depth

**Week 5 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** indexed cube, DEPTH_TEST, CULL_FACE, CCW front  
**Success check:** they enable depth, clear depth, and can toggle cull to see winding

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: a cube that is not painter-sorted by luck | Invariant: hidden surfaces are a GPU test; winding is CCW; near is not 0`

## Board at the end (they photograph this)

```
gl.enable(DEPTH_TEST)
gl.enable(CULL_FACE)     CCW front     cull BACK

clear COLOR | DEPTH      (forgot depth → flicker)

near 0.1   far 100       near=0 is illegal / fighting
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** CG I z-buffer is now a GPU bit. Without depth a cube is a scribble. Winding: if it is inside-out, you mirrored scale or reversed CCW — not 'WebGL is broken.'

**Ask:** Do you need to clear depth every frame? Wait. Want: yes, COLOR | DEPTH.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *indices, DEPTH_TEST, cull*.

**Do not:** No depth clear.

### Minutes 10–12 — Frame

**Say:** Indexed cube: 24 unique verts with normals later, or 8 verts if you accept shared normals. Today indices + depth. Demo 04-rotating-cube.html. Conventions: CCW.

**Ask:** What does CULL_FACE remove?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Same as CG I hidden surfaces. Now enable the test.

**Board:** DEPTH_TEST, clear mask, CCW.

**Say:** Toggle depth off — painter bugs. Toggle cull — missing faces.

**Ask:** Why is near=0 a problem?

**They do:** On paper: the two enable lines plus the clear mask.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Cube with depth; toggle depth to show painter bugs. Plant no depth clear. Plant near=0.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cull toggle. See which faces vanish. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: cull toggle; wireframe extra. Homework: GPU depth vs CPU z-buffer; cube. Quiz: DEPTH_TEST, CCW, clear depth.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Indexed cube no depth | It looks 'ok' from one angle. Plant. |
| 10–30 | enable DEPTH_TEST + clear | Plant forgot DEPTH bit. |
| 30–45 | CULL_FACE CCW | Plant CW verts. Inside-out. |
| 45–60 | They toggle cull | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. no depth clear.
2. near=0.

## If we run long, cut

Normal matrix. Keep cube + depth + cull.

## If we run short, add

Wireframe extra (LINES or barycentric name).
