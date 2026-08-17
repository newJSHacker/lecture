# Lecture 6 — Audio visualization

**Week 6 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** analyser → scale  
**Success check:** User-gesture AudioContext.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: analyser → scale | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
byte frequency → instance scale
Bars in 3D.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Gesture. Browsers block autoplay.

**Ask:** User-gesture AudioContext? Wait seven seconds. Take two answers.

**Board:** parked strip. Then byte frequency → instance scale.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *analyser → scale*.

**Do not:** Autoplay surprise.

### Minutes 10–12 — Frame

**Say:** Today’s question: analyser → scale. Kernel: analyser → scale. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: autoplay surprise.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Gesture. Browsers block autoplay.

**Say:** Data. fftSize.

**Say:** a11y. Don't rely on audio only; show a mute and a visual that works silent.

**Ask:** User-gesture AudioContext? Wait seven seconds. Take two answers.

**They do:** On paper: mute.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Play a short licensed loop; 32 bars as boxes.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** mute.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: mute.; fallback still image.. Homework: Written: autoplay policy.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: analyser → scale | Plant the first common mistake. |
| 10–30 | Play a short licensed loop; 32 bars as boxes. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. why click first (4)
2. fftSize (3)
3. silent path (3)


## Snippet

```js
const ctx = new AudioContext(); analyser.fftSize = 64;
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Gesture.** Browsers block autoplay. A Play button is the lab.

**2. Data.** fftSize. Map bins to instances. Cap N.

**3. a11y.** Don't rely on audio only; show a mute and a visual that works silent.

---

## Common mistakes

1. autoplay surprise.
2. copyrighted full songs as the asset without license.

## If we run long, cut

a11y

## If we run short, add

fallback still image.
