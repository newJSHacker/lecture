# Lecture 6 — Audio visualization

**Week 6 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** user-gesture AudioContext; analyser bins → instance scale; mute  
**Success check:** they can start audio from a Play button and scale bars from an analyser without autoplay

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: bars that work silent | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
Play (gesture)  →  AudioContext
analyser.fftSize = 64
bins → instance scale     cap N

mute + still image     (not audio-only)
licensed loop only
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Browsers block autoplay. A surprise soundtrack is a fail. Audio is data for graphics — and a11y still needs a silent path.

**Ask:** Why did play() throw? Wait. Want: no user gesture.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *analyser → scale*.

**Do not:** Autoplay surprise.

### Minutes 10–12 — Frame

**Say:** fftSize named. Map bins to instances, not 1024 meshes. Do not ship a copyrighted album as the asset. Captions/mute in the HUD.

**Ask:** If the speaker is off, is the viz still readable?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Gesture first. Then analyser.

**Board:** Play → context → bins → scale. Cap N.

**Say:** Mute. Fallback still. Instances, not 32 Mesh objects if they already know Instances — else 32 is enough.

**Ask:** What does fftSize change?

**They do:** On paper: button, analyser, one bin → one bar.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Licensed short loop; 32 bars. Plant autoplay. Plant a full song file. Fix: button + tiny loop.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Play button starts context; one bar follows a bin. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: mute + still fallback. Homework: gesture paragraph. Quiz: autoplay, fftSize, why mute.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Play gesture | Plant autoplay. |
| 15–40 | Analyser → scale | Plant 1024 meshes. |
| 40–55 | Mute / silent still | Audio-only plant. |
| 55–60 | They cap N | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. mute.
2. fallback still image.

---

## Homework

1. Written: autoplay policy.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const ctx = new AudioContext(); analyser.fftSize = 64;
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. autoplay surprise.
2. copyrighted full songs as the asset without license.

## If we run long, cut

Beat-matching DSP. Keep gesture + bins.

## If we run short, add

Fallback still image in the HUD.
