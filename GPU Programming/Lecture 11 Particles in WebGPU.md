# Lecture 11 — Particles in WebGPU

**Week 11 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Particle struct in a storage buffer; compute update pass then render points  
**Success check:** they can keep pos/vel on the GPU and write a WebGL fallback note — no 100k JS uploads

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: two named passes, one struct layout | Invariant: the buffer is the source of truth; Safari-old or a textured cube may stay WebGL`

## Board at the end (they photograph this)

```
struct P { pos: vec2f, vel: vec2f }   // draw stride

PASS 1  compute  update P
PASS 2  render   draw points

do not upload 100k pos from JS each frame
fallback: week-2 ping-pong  (README)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Two passes: physics compute, then draw. Buffer sizes and workgroup limits named. Honesty: if the audience is old Safari, WebGL ping-pong is enough. Invented N is not a measurement.

**Ask:** Where is the source of truth — JS array, or the GPU buffer? Wait. Want: GPU buffer.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *buffer of structs*.

**Do not:** Uploading 100k positions from JS every frame.

### Minutes 10–12 — Frame

**Say:** dt uniform. WebGL fallback note is the attempt if compute is blocked. Feature detect from week 8.

**Ask:** When would you not use WebGPU?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Struct bytes on the board: pos.xy vel.xy, alignment.

**Board:** compute then draw. Circle no JS upload.

**Say:** N is a constant they can count in the buffer — not a fantasy million.

**Ask:** Write struct P.

**They do:** On paper: stride of one particle in bytes (teaching: 16).

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** N particles in WGSL compute; draw as points. Plant 100k JS uploads. Plant no fallback story. dt uniform.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** WebGL fallback note. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: fallback note + dt. Homework: when not WebGPU; demo. Quiz: source of truth, two passes, Safari.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Struct layout | Plant JS upload each frame. |
| 10–30 | Compute then draw | Name both passes. |
| 30–45 | dt uniform | Pause. |
| 45–60 | Fallback README | Circulate. Detect. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. WebGL fallback note.
2. dt uniform.

---

## Homework

1. Written: when you would not use WebGPU.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```wgsl
struct P { pos: vec2f, vel: vec2f }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. uploading 100k positions from JS every frame.
2. no fallback story for the course project if required to run in the lab.

## If we run long, cut

Indirect draw. Keep struct + two passes + fallback sentence.

## If we run short, add

Workgroup / buffer limits as names.
