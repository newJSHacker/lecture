# Lecture 2 — The animation loop

**Week 2 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** requestAnimationFrame; dt in seconds; clearRect; cap dt  
**Success check:** they have a rAF loop that moves with dt and can toggle clear vs trails

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Interactive Web/code/02-raf.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: motion that does not depend on a magic 16 | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
function frame(now) {
  const dt = Math.min(0.05, (now - last) / 1000);  // seconds, capped
  last = now;
  clearRect(0,0,w,h);     // or trails on purpose
  // update + draw
  requestAnimationFrame(frame);
}

setInterval(16)  =  not the loop
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** A path that does not move is week 1. Today the clock is rAF. setInterval(16) is a lie: it is not vsync, and a hidden tab keeps waking. We do not invent fps.

**Ask:** Why is dt in seconds, not ‘frames’? Wait. Want: motion = velocity × time; refresh rate is not a unit we assume.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rAF, dt, time*.

**Do not:** SetInterval(16).

### Minutes 10–12 — Frame

**Say:** rAF syncs to refresh and slows when the tab is hidden — good. t in seconds; sin(t) for a path. Clear each frame or you paint trails. Cap dt so a hitch does not teleport.

**Ask:** What if you forget to request the next frame?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** vs setInterval. One ring: schedule the next frame at the end.

**Board:** rAF ring. dt cap. clearRect vs trails.

**Say:** Pause key sets a flag; the loop still runs or you stop requesting — pick one and freeze.

**Ask:** Uncapped dt after a debugger pause — what happens to a ball with vx*dt?

**They do:** On paper: dt-cap one-liner and a pause flag.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** A ball on a sine; pause key. Demo Interactive Web/code/02-raf.html. Plant setInterval(16). Plant forgotten clearRect (trails). Plant uncapped dt.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** dt-cap. Trail vs clear toggle. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: dt-cap + trail toggle. Homework: why rAF; loop as a module. Quiz: rAF vs interval, dt, hidden tab.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | rAF ring | Plant setInterval(16). |
| 10–30 | sine ball + dt | Plant pixels-per-frame with no dt. |
| 30–45 | clear vs trails + pause | They see both. |
| 45–60 | They cap dt | Circulate. No fps claims. |

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

None this meeting.


## Snippet

```js
requestAnimationFrame(frame);
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. setInterval(16).
2. uncapped dt.

## If we run long, cut

Pause key if dt is still wrong. Keep rAF + dt + clear.

## If we run short, add

Trail vs clear toggle.
