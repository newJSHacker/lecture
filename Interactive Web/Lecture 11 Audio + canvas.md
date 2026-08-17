# Lecture 11 — Audio + canvas

**Week 11 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** AudioContext after a user gesture; AnalyserNode; draw bars in Canvas 2D  
**Success check:** they start audio on click, draw analyser bars, and can mute without creating a new context every frame

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: click-to-start, then a picture of the sound | Invariant: autoplay is blocked; one AudioContext; bars are data, not a 3D engine`

## Board at the end (they photograph this)

```
click  →  audioCtx.resume()   // or create on gesture
AnalyserNode  fftSize  getByteFrequencyData(buf)
rAF:  analyser → bars on canvas 2d

autoplay noise              =  fail
new AudioContext every frame =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Browsers block autoplay. A visualizer is analyser bins into week 1’s fillRect. Semester 5 audio viz is this grown up. No Three.js. No CDN synth library.

**Ask:** Why did new AudioContext() in the first script line stay silent? Wait. Want: policy — need a gesture, then resume.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Web Audio, analyser*.

**Do not:** Autoplay noise.

### Minutes 10–12 — Frame

**Say:** Gesture first. Oscillator or a local file input extra. Analyser frequencyBinCount. Optional sync from audio.currentTime — name, may cut. Mute is gain or suspend, not a new context.

**Ask:** Where does the analyser sit in the graph? Want: source → analyser → destination.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Click-to-start. Read the autoplay error if you plant autoplay.

**Board:** analyser fft bars. One context.

**Say:** Draw in the rAF you already have. Do not invent fps for the bars.

**Ask:** Mute: dest.disconnect vs gain.value = 0 vs suspend — pick one and freeze.

**They do:** On paper: mute button — which node it touches.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Click-to-start oscillator or file; draw bars. There is no audio demo in code/; do not open 09-gsap.html for this. Plant autoplay. Plant new AudioContext inside rAF.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Mute button. File input extra if the oscillator works. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: mute + file input extra. Homework: autoplay policy; bars. Quiz: why click first, AnalyserNode, autoplay.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | autoplay plant | Silent. Then click resume. |
| 10–30 | oscillator + analyser bars | Canvas 2D, not WebGL. |
| 30–45 | one context forever | Plant construct-in-loop. |
| 45–60 | They add mute | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. autoplay noise.
2. creating AudioContext every frame.

## If we run long, cut

currentTime sync. Keep gesture + analyser + bars.

## If we run short, add

file input extra.
