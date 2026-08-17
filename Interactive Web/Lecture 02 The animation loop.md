# Lecture 2 — The animation loop

**Week 2 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rAF, dt, time  
**Success check:** rAF loop.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Interactive Web/code/02-raf.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: rAF, dt, time | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
requestAnimationFrame ring
Loop.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** vs setInterval. rAF syncs to refresh.

**Ask:** rAF loop? Wait seven seconds. Take two answers.

**Board:** parked strip. Then requestAnimationFrame ring.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rAF, dt, time*.

**Do not:** SetInterval(16).

### Minutes 10–12 — Frame

**Say:** Today’s question: rAF, dt, time. Kernel: rAF, dt, time. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: setInterval(16).

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** vs setInterval. rAF syncs to refresh.

**Say:** Time. t in seconds.

**Say:** Clear. clearRect each frame or trails.

**Ask:** rAF loop? Wait seven seconds. Take two answers.

**They do:** On paper: dt-cap.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A ball on a sine; pause key.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** dt-cap.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: dt-cap.; trail vs clear toggle.. Homework: Written: why rAF.; Code: loop module.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: rAF, dt, time | Plant the first common mistake. |
| 10–30 | A ball on a sine; pause key. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/02-raf.html` as the after-class check, not as the lecture.

---

## Lab

1. dt-cap.
2. trail vs clear toggle.

---

## Homework

1. Written: why rAF.
2. Code: loop module.

---

## Quiz next meeting (they hear this now)

1. rAF vs interval (4)
2. dt (3)
3. hidden tab (3)


## Snippet

```js
requestAnimationFrame(frame);
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. vs setInterval.** rAF syncs to refresh. Tab hidden slows it — good.

**2. Time.** t in seconds. sin(t) for motion.

**3. Clear.** clearRect each frame or trails.

---

## Common mistakes

1. setInterval(16).
2. uncapped dt.

## If we run long, cut

Clear

## If we run short, add

trail vs clear toggle.
