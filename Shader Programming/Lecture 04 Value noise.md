# Lecture 4 — Value noise

**Week 4 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** hash(lattice) then bilinear lerp — value noise, not Math.random  
**Success check:** they can hash a lattice point and lerp the four corners

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: deterministic noise you can pause | Invariant: same uv → same noise; fireflies are a random() per frame`

## Board at the end (they photograph this)

```
i = floor(p)     f = fract(p)

a--b     hash(i+corner)
|  |     mix mix  (bilinear)
c--d

sin/dot hash  =  teaching, not crypto
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Fire, water, terrain, grain — all start here. If they call Math.random in the FS, the picture sparkles and they cannot debug a still.

**Ask:** Why not random() every frame? Wait. Want: not a function of uv.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *hash, lerp*.

**Do not:** True random per frame (fireflies).

### Minutes 10–12 — Frame

**Say:** Value noise interpolates scalars. Perlin gradients are a name; fBm next week can use either. Hash artifacts exist — show them, do not hide.

**Ask:** What is bilinear here?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Lattice. Four corners. Hash is a float in 0..1.

**Board:** bilinear. Smoothstep on f as optional fade.

**Say:** A 200-line noise library unread is a clip. Ten lines they can pause.

**Ask:** Write hash(vec2) in one line (sin/dot is allowed).

**They do:** On paper: four hashes and two mix calls.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Fullscreen value noise; slider for scale (a uniform). Plant true random per frame. Overlay the lattice.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Animate z as time extra, or freeze time and change scale. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: time or lattice overlay. Homework: why hash; noise(vec2). Quiz: why no Math.random, bilinear, artifact.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | hash(vec2) | Plant Math.random. |
| 10–30 | Bilinear value noise | Plant copying 200 unread lines. |
| 30–45 | Scale uniform | Pause time; debug a still. |
| 45–60 | They add lattice overlay | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Animate z as time extra.
2. Show lattice overlay.

---

## Homework

1. Written: why hash.
2. Code: noise(vec2).

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. true random per frame (fireflies).
2. copying a 200-line library unread.

## If we run long, cut

Gradient noise proof. Keep hash + bilinear.

## If we run short, add

fade(t)=t*t*(3-2*t) name.
