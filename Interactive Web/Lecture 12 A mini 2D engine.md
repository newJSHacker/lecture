# Lecture 12 — A mini 2D engine

**Week 12 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** entities, loop, input  
**Success check:** Entity {update,render}.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: entities, loop, input | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
entity list update render
Boxes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Architecture. Enough to later map onto Three.js scenes.

**Ask:** Entity {update,render}? Wait seven seconds. Take two answers.

**Board:** parked strip. Then entity list update render.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *entities, loop, input*.

**Do not:** God object 800 lines.

### Minutes 10–12 — Frame

**Say:** Today’s question: entities, loop, input. Kernel: entities, loop, input. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: god object 800 lines.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Architecture. Enough to later map onto Three.js scenes.

**Say:** Input. keys set.

**Say:** Bounds. n=200 circles fine; n=200000 not.

**Ask:** Entity {update,render}? Wait seven seconds. Take two answers.

**They do:** On paper: spawn on click.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Bouncers with WASD player.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** spawn on click.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: spawn on click.; pause.. Homework: Written: entity table.; Code: mini engine.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: entities, loop, input | Plant the first common mistake. |
| 10–30 | Bouncers with WASD player. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. spawn on click.
2. pause.

---

## Homework

1. Written: entity table.
2. Code: mini engine.

---

## Quiz next meeting (they hear this now)

1. update vs render (4)
2. input map (3)
3. cap n (3)


## Snippet

```js
entities.forEach(e => e.update(dt));
entities.forEach(e => e.render(ctx));
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Architecture.** Enough to later map onto Three.js scenes.

**2. Input.** keys set.

**3. Bounds.** n=200 circles fine; n=200000 not.

---

## Common mistakes

1. god object 800 lines.
2. physics in render.

## If we run long, cut

Bounds

## If we run short, add

pause.
