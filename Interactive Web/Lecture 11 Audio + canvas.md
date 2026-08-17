# Lecture 11 — Audio + canvas

**Week 11 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Web Audio, analyser  
**Success check:** AudioContext.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: Web Audio, analyser | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
analyser fft bars
Bars.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Gesture. Browsers block autoplay.

**Ask:** AudioContext? Wait seven seconds. Take two answers.

**Board:** parked strip. Then analyser fft bars.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Web Audio, analyser*.

**Do not:** Autoplay noise.

### Minutes 10–12 — Frame

**Say:** Today’s question: Web Audio, analyser. Kernel: Web Audio, analyser. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: autoplay noise.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Gesture. Browsers block autoplay.

**Say:** Analyser. frequencyBinCount.

**Say:** Sync. t from audio.currentTime optional.

**Ask:** AudioContext? Wait seven seconds. Take two answers.

**They do:** On paper: Mute button.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Click-to-start oscillator or file; draw bars.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Mute button.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Mute button.; file input extra.. Homework: Written: autoplay policy.; Code: bars.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Web Audio, analyser | Plant the first common mistake. |
| 10–30 | Click-to-start oscillator or file; draw bars. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. Mute button.
2. file input extra.

---

## Homework

1. Written: autoplay policy.
2. Code: bars.

---

## Quiz next meeting (they hear this now)

1. why click first (4)
2. AnalyserNode (3)
3. autoplay (3)


## Snippet

```js
const ctxA = new AudioContext();
const an = ctxA.createAnalyser();
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Gesture.** Browsers block autoplay. Click to start.

**2. Analyser.** frequencyBinCount. Visualizer. Semester 5 audio viz is this grown up.

**3. Sync.** t from audio.currentTime optional.

---

## Common mistakes

1. autoplay noise.
2. creating AudioContext every frame.

## If we run long, cut

Sync

## If we run short, add

file input extra.
