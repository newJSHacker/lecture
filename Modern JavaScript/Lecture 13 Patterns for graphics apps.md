# Lecture 13 — Patterns for graphics apps

**Week 13 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** game loop, modules, state  
**Success check:** Separate update(dt) and render().

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: game loop, modules, state | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
update vs render
Loop box.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Loop. Interactive Web and CG I already; now as architecture.

**Ask:** Separate update(dt) and render()? Wait seven seconds. Take two answers.

**Board:** parked strip. Then update vs render.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *game loop, modules, state*.

**Do not:** SetInterval(16) as the loop.

### Minutes 10–12 — Frame

**Say:** Today’s question: game loop, modules, state. Kernel: game loop, modules, state. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: setInterval(16) as the loop.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Loop. Interactive Web and CG I already; now as architecture.

**Say:** State. One object.

**Say:** Dirty flags. Name for editors.

**Ask:** Separate update(dt) and render()? Wait seven seconds. Take two answers.

**They do:** On paper: State to JSON extra.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: A bouncing ball with dt, pause, reset.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** State to JSON extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: State to JSON extra.; Cap dt.. Homework: Written: update vs render.; Code: loop.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: game loop, modules, state | Plant the first common mistake. |
| 10–30 | A bouncing ball with dt, pause, reset. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/08-modules.html` as the after-class check, not as the lecture.

---

## Lab

1. State to JSON extra.
2. Cap dt.

---

## Homework

1. Written: update vs render.
2. Code: loop.

---

## Quiz next meeting (they hear this now)

1. rAF (3)
2. dt (4)
3. pause (3)


## Snippet

```js
function frame(t){ const dt=t-last; last=t; update(dt); render(); requestAnimationFrame(frame); }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Loop.** Interactive Web and CG I already; now as architecture.

**2. State.** One object. Serialize later.

**3. Dirty flags.** Name for editors.

---

## Common mistakes

1. setInterval(16) as the loop.
2. Uncapped dt spikes.

## If we run long, cut

Dirty flags

## If we run short, add

Cap dt.
