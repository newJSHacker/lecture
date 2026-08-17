# Lecture 2 — FBO ping-pong

**Week 2 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** A→B→A textures  
**Success check:** Two textures.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: A→B→A textures | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
read A write B; swap
Two FBOs.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Why two. A shader cannot safely read the texel it is writing.

**Ask:** Two textures? Wait seven seconds. Take two answers.

**Board:** parked strip. Then read A write B; swap.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *A→B→A textures*.

**Do not:** One texture in/out.

### Minutes 10–12 — Frame

**Say:** Today’s question: A→B→A textures. Kernel: A→B→A textures. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: one texture in/out.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why two. A shader cannot safely read the texel it is writing.

**Say:** Size. Sim resolution ≠ canvas resolution.

**Say:** Precision. HALF_FLOAT / FLOAT textures for positions.

**Ask:** Two textures? Wait seven seconds. Take two answers.

**They do:** On paper: show A and B debug.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Game of life or a blur ping-pong; pause.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** show A and B debug.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: show A and B debug.; wrong same-texture bug then fix.. Homework: Written: why two textures.; Code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: A→B→A textures | Plant the first common mistake. |
| 10–30 | Game of life or a blur ping-pong; pause. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. feedback loop (4)
2. float tex (3)
3. sim vs canvas size (3)


## Snippet

```js
;[texA, texB] = [texB, texA];
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Why two.** A shader cannot safely read the texel it is writing. Ping-pong is the game-of-life / blur / particle-position pattern.

**2. Size.** Sim resolution ≠ canvas resolution.

**3. Precision.** HALF_FLOAT / FLOAT textures for positions. Unsigned byte is a trap.

---

## Common mistakes

1. one texture in/out.
2. RGBA8 positions.

## If we run long, cut

Precision

## If we run short, add

wrong same-texture bug then fix.
