# Lecture 2 — FBO ping-pong

**Week 2 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** ping-pong: read A, write B, swap — two FLOAT textures  
**Success check:** they can draw two FBOs, swap, and debug A vs B without sampling the texture they are writing

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: A→B→A you can pause | Invariant: a shader cannot safely read the texel it is writing; RGBA8 positions are a trap`

## Board at the end (they photograph this)

```
frame n:    sample A  →  write B
swap:       [A,B] = [B,A]

A  FLOAT RGBA     B  FLOAT RGBA
   (sim res)         (sim res)

sim resolution  ≠  canvas resolution
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Ping-pong is game-of-life, blur, and particle positions. One texture in/out is a race. Unsigned byte positions die. This is still WebGL — WebGPU compute comes after the midterm.

**Ask:** Why two textures? Wait. Want: cannot read what you write.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *A→B→A textures*.

**Do not:** One texture in/out.

### Minutes 10–12 — Frame

**Say:** HALF_FLOAT / FLOAT for state. Sim res ≠ canvas. Pause the swap to debug A and B as color.

**Ask:** What is wrong with RGBA8 for positions?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two rectangles on the board. Arrows read/write.

**Board:** the swap line. Circle FLOAT.

**Say:** Plant same-texture, then fix. Local 01-pong.html.

**Ask:** Write the swap in one JS line.

**They do:** On paper: memory layout of A and B.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Game of life or blur ping-pong; pause. Plant one texture in/out. Plant RGBA8 positions. Show A and B debug views.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Show A and B debug. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: debug views + same-texture bug then fix. Homework: why two textures; code. Quiz: feedback loop, float tex, sim vs canvas.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Draw A and B | Plant one texture in/out. |
| 10–30 | Swap each frame | Plant RGBA8 state. |
| 30–45 | Pause; show A vs B | They see the layout. |
| 45–60 | They fix same-texture | Circulate. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. show A and B debug.
2. wrong same-texture bug then fix.

---

## Homework

1. Written: why two textures.
2. Code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
;[texA, texB] = [texB, texA];
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. one texture in/out.
2. RGBA8 positions.

## If we run long, cut

Precision formats catalog. Keep two FLOAT textures + swap.

## If we run short, add

Sim res as a uniform they can shrink — measure if they claim speed.
