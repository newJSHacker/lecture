# Lecture 5 — Forces and integration

**Week 5 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Euler, clamp  
**Success check:** Semi-implicit Euler.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: Euler, clamp | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
v += a dt; p += v dt
Euler step.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Integration. Same as Interactive Web physics-lite.

**Ask:** Semi-implicit Euler? Wait seven seconds. Take two answers.

**Board:** parked strip. Then v += a dt; p += v dt.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Euler, clamp*.

**Do not:** Variable dt uncapped.

### Minutes 10–12 — Frame

**Say:** Today’s question: Euler, clamp. Kernel: Euler, clamp. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: variable dt uncapped.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Integration. Same as Interactive Web physics-lite.

**Say:** Stability. dt too big → explode.

**Say:** Forces. Gravity, attractor, curl noise extra.

**Ask:** Semi-implicit Euler? Wait seven seconds. Take two answers.

**They do:** On paper: box collide extra.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Attractor + gravity; explode then cap dt.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** box collide extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: box collide extra.; curl extra.. Homework: Written: why cap dt.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Euler, clamp | Plant the first common mistake. |
| 10–30 | Attractor + gravity; explode then cap dt. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. Euler (3)
2. explode cause (4)
3. clamp (3)


## Snippet

```glsl
vel += acc * dt; pos += vel * dt;
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Integration.** Same as Interactive Web physics-lite. GPU: all particles in parallel.

**2. Stability.** dt too big → explode. Clamp speed.

**3. Forces.** Gravity, attractor, curl noise extra.

---

## Common mistakes

1. variable dt uncapped.
2. CPU physics + GPU draw as if it were GPGPU.

## If we run long, cut

Forces

## If we run short, add

curl extra.
