# Lecture 13 — Patterns for graphics apps

**Week 13 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rAF loop; update(dt) then render(); one state object; cap dt  
**Success check:** they can pause/reset a bouncing ball without putting physics inside draw

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: architecture for a graphics app, not a new renderer | Invariant: time is a delta; draw does not simulate; setInterval(16) is not the loop`

## Board at the end (they photograph this)

```
function frame(t) {
  const dt = Math.min(0.05, (t - last) / 1000);
  last = t;
  update(dt);
  render();
  requestAnimationFrame(frame);
}

state = { … }     serialize later
dirty flags       name for editors
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Interactive Web already has rAF. Computer Graphics I already has a tick. Today it is modules and state: one object, update vs render, tests on the kernel. This is the last content week before studio.

**Ask:** Why cap dt? Wait. Want: a backgrounded tab or a hitch must not teleport the ball.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *game loop, modules, state*.

**Do not:** SetInterval(16) as the loop.

### Minutes 10–12 — Frame

**Say:** Loop as architecture. State is one object — JSON extra in lab. Dirty flags named for editors, not required. No Three.js. No invented fps on the HUD.

**Ask:** Where does bounce live — update or render?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Interactive Web and CG I already; now files: loop.js, state, render.

**Board:** update vs render boxes. Cap dt. pause flag.

**Say:** setInterval(16) desyncs and does not pause in a hidden tab the way rAF does.

**Ask:** What goes in JSON.stringify(state) — functions? Want: data only.

**They do:** On paper: state to JSON extra — which fields survive a round-trip.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** A bouncing ball with dt, pause, reset. Demo Modern JavaScript/code/07-loop.html (dt-capped rAF). Plant setInterval(16). Plant uncapped dt after a debugger pause.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** State to JSON extra. Cap dt if missing. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: JSON state + cap dt. Homework: update vs render paragraph; loop code. Quiz: rAF, dt, pause. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | rAF + cap dt | Plant setInterval(16). |
| 10–30 | update vs render ball | Plant physics in render. |
| 30–45 | pause / reset | State object, not a global pile. |
| 45–60 | They JSON.stringify state | Circulate. |

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

None this meeting.


## Snippet

```js
function frame(t){ const dt=t-last; last=t; update(dt); render(); requestAnimationFrame(frame); }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. setInterval(16) as the loop.
2. Uncapped dt spikes.

## If we run long, cut

Dirty flags. Keep loop + state + cap dt.

## If we run short, add

Cap dt on a hitch they trigger with a debugger pause.
