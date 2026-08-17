# Lecture 5 — Animation

**Week 5 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Clock.getDelta(); mixer is a name for glTF clips later  
**Success check:** they rotate with dt, can pause, and do not write rotation = t on a variable refresh display

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: motion that does not depend on fps | Invariant: time is dt; AnimationMixer is clips, not the rAF loop`

## Board at the end (they photograph this)

```
const dt = clock.getDelta();
mesh.rotation.y += speed * dt;

pause: skip the integrate, still render

AnimationMixer   (name)  —  glTF clips week 6
GSAP can tween Object3D; still one rAF
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Same as Interactive Web: rAF is the clock. rotation = elapsed without dt lies on 30 Hz vs 144 Hz. We do not invent fps — we integrate dt.

**Ask:** If the tab throttles, does rotation += 0.01 still mean the same angle per second? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *clock, mixer name*.

**Do not:** Rotation = t without dt on variable fps.

### Minutes 10–12 — Frame

**Say:** Clock. Mixer named so week 6 has a word. GSAP optional name; still one rAF. Pause is a boolean around the integrate.

**Ask:** Mixer vs rAF rotate — which plays a glTF clip?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** dt from getDelta. Speed in rad/s.

**Board:** pause still renders.

**Say:** Bounce with sin(time) is ok if time is accumulated dt.

**Ask:** What does getDelta return the first frame?

**They do:** On paper: the integrate line with dt.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Spin + bounce with dt. Plant rotation = t. Demo 01 or 06. No fps brag.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pause flag. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pause; mixer extra if a clip exists. Homework: mixer vs rAF; dt. Quiz: getDelta, mixer, pause.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Clock.getDelta | Plant Date.now()/16. |
| 10–30 | spin with dt | Plant += 0.01. |
| 30–45 | pause | Still render. |
| 45–60 | They pause | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. pause.
2. mixer extra if a clip exists.

---

## Homework

1. Written: mixer vs rAF rotate.
2. Code: dt.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const dt = clock.getDelta();
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. rotation = t without dt on variable fps.

## If we run long, cut

GSAP timeline. Keep dt + pause.

## If we run short, add

mixer extra only if a clip is already in the scene.
