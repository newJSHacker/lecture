# Lecture 12 — A mini 2D engine

**Week 12 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** entities with update(dt) and render(ctx); input as a keys set; a cap on n  
**Success check:** they spawn on click into a list the loop updates, without an 800-line god object

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: a mini 2D engine, not Unity | Invariant: the loop is shared; each entity is a small object; physics is not inside render`

## Board at the end (they photograph this)

```
entities.forEach(e => e.update(dt));
entities.forEach(e => e.render(ctx));

keys = new Set()     keydown add / keyup delete
n ≈ 200 circles OK     n = 200000 not this course

god object 800 lines   =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Architecture enough to later map onto a Three.js scene: objects, a loop, input. Today it is Canvas 2D bouncers and a WASD player. Full engines are skipped on purpose.

**Ask:** If render draws and also writes vx, what breaks pause? Wait. Want: pause cannot skip sim independently.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *entities, loop, input*.

**Do not:** God object 800 lines.

### Minutes 10–12 — Frame

**Say:** Entity {update, render}. Input: a set of keys, not one global lastKey. Bounds: freeze a cap n. Collision can be naive. Pause is a flag in the loop from week 2.

**Ask:** Who calls requestAnimationFrame — each entity or the engine?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** List of entities. Engine owns time and clear. Mapping to later 3D: mesh ≈ entity, not this week’s kernel.

**Board:** update vs render. keys set. cap n.

**Say:** Spawn on click using week 3 mapping. Do not paste an engine from the internet.

**Ask:** Why a Set for keys instead of wasd booleans only?

**They do:** On paper: spawn on click — push entity with vx,vy,r.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Bouncers with WASD player. Demo Interactive Web/code/07-engine.html. Plant physics in render. Plant one 800-line script.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Spawn on click. Pause. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: spawn + pause. Homework: entity table; mini engine. Quiz: update vs render, input map, cap n.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | entity list + rAF | Plant god object. |
| 10–30 | bouncers dt | Plant sim in render. |
| 30–45 | WASD keys set | keyup missing plant. |
| 45–60 | They spawn on click | Circulate. Cap n. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. god object 800 lines.
2. physics in render.

## If we run long, cut

n=200 discussion. Keep entities + loop + input.

## If we run short, add

pause flag.
