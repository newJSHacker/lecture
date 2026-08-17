# Lecture 5 — Forces and integration

**Week 5 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** semi-implicit Euler in the update kernel: v+=a dt; p+=v dt; clamp dt and speed  
**Success check:** they can explode with huge dt, then cap, in the same packing as week 3

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: stable steps you can pause | Invariant: integration runs where the state lives; CPU physics + GPU draw is not GPGPU`

## Board at the end (they photograph this)

```
in the update kernel (FS or TF):
  v += a * dt
  p += v * dt          // semi-implicit: v first
  v = clamp(v, ±vmax)
  dt = min(dt, dtMax)

state layout still: RG pos, BA vel
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Same as Interactive Web physics-lite, all particles in parallel. Variable uncapped dt explodes. CPU physics then upload is not this course. Pause; inspect one texel.

**Ask:** Why v before p? Wait. Want: semi-implicit Euler.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Euler, clamp*.

**Do not:** Variable dt uncapped.

### Minutes 10–12 — Frame

**Say:** Stability: dt too big → explode. Clamp speed. Forces: gravity, attractor; curl noise extra. Box collide extra writes p and v in the same layout.

**Ask:** What causes the explode?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** One particle on the board: numbers, then the same in a texel.

**Board:** Euler + clamp. Circle dtMax.

**Say:** Attractor as a uniform. Plant uncapped rAF dt.

**Ask:** Write the two Euler lines.

**They do:** On paper: where dt is clamped.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Attractor + gravity; explode then cap dt. Plant variable dt uncapped. Plant CPU physics + GPU draw labeled GPGPU.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Box collide extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: box collide + curl extra. Homework: why cap dt; demo. Quiz: Euler, explode cause, clamp.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Euler in the kernel | Plant CPU physics as GPGPU. |
| 10–30 | Explode then dtMax | Plant uncapped dt. |
| 30–45 | Clamp speed | Same RG/BA layout. |
| 45–60 | They add a box | Circulate. Pause. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. box collide extra.
2. curl extra.

---

## Homework

1. Written: why cap dt.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vel += acc * dt; pos += vel * dt;
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. variable dt uncapped.
2. CPU physics + GPU draw as if it were GPGPU.

## If we run long, cut

RK4. Keep Euler + clamp + layout.

## If we run short, add

Curl noise as extra force.
