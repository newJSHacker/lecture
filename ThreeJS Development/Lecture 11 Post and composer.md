# Lecture 11 — Post and composer

**Week 11 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** EffectComposer = FBO plumbing; RenderPass then a cheap pass  
**Success check:** they can toggle composer vs renderer.render and say this is week-11 WebGL FBO

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: post as a pipeline, not a bloom preset dump | Invariant: composer without understanding framebuffer is a filter pack; extra passes cost fill rate`

## Board at the end (they photograph this)

```
renderer.render     →  canvas
composer:  scene FBO → pass → pass → screen

RenderPass(scene, camera)
OutputPass / gamma     color space

WebGL FBO week 11   =   this plumbing
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Bloom/HDR labs live in Real-Time Rendering. Demo 18-bloom.html is a name. Today: RenderPass + toggle vs raw render. Local jsm, no CDN.

**Ask:** If you never unbind an FBO in raw WebGL, what is the Three analog of forgetting composer.setSize? Wait. Want: resize / ping-pong size.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *EffectComposer name*.

**Do not:** Composer without understanding framebuffer.

### Minutes 10–12 — Frame

**Say:** sRGB output pass. Why not 8 passes. Cost sentence — measure or omit, no invented fps.

**Ask:** What is RenderPass?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two paths: raw render vs composer.

**Board:** render → pass → screen.

**Say:** Cheap pass or identity. Bloom is optional show.

**Ask:** Why not eight UnrealBloomPasses?

**They do:** On paper: composer vs renderer.render.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Composer with a cheap pass or gamma output. Demo 18-bloom.html as optional. Plant composer without FBO talk. Plant CDN examples/js.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Toggle composer vs raw render. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: toggle; cost sentence. Homework: extra fill rate; composer. Quiz: RenderPass, why not 8 passes, output color.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Map to FBO | Draw last semester. |
| 10–30 | RenderPass + output | Plant forgot setSize. |
| 30–45 | toggle raw | They see the difference. |
| 45–60 | They write cost sentence | No invented fps. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. toggle composer vs raw render.
2. cost sentence.

---

## Homework

1. Written: extra fill rate.
2. Code: composer.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
composer.addPass(new RenderPass(scene, camera));
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. composer without understanding framebuffer.

## If we run long, cut

Full bloom tuning. Keep plumbing + toggle.

## If we run short, add

Cost sentence: extra full-screen passes.
