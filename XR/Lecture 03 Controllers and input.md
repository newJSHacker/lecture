# Lecture 3 — Controllers and input

**Week 3 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** XRInputSource; select is the click; debug the ray  
**Success check:** they can select a cube along a controller or mouse-ray fallback and change its color

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: a ray you can see | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
hands · controllers · gaze (last resort)
select  =  click
squeeze =  named extra

controller.addEventListener('select', …)
show the ray     or it is mouse-only theatre
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Mouse-only and calling it VR fails. Gaze is last resort. The ray must be visible in the lab fallback too.

**Ask:** If I cannot see the ray, how do I debug a miss? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *select, squeeze, rays*.

**Do not:** Mouse-only and calling it VR.

### Minutes 10–12 — Frame

**Say:** Three.js XRControllerModelFactory / Raycaster from controller. Haptics pulse named, not required. Inline: mouse ray analog.

**Ask:** What event is the click?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Input sources. select vs squeeze.

**Board:** select listener. Draw the ray.

**Say:** Fallback: click-to-select on the inline cube. Same verb.

**Ask:** Why is gaze last resort?

**They do:** On paper: select → recolor. Fallback arrow.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Point and select to recolor. Plant mouse-only with no ray. Show the ray. Squeeze extra.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** select listener + visible ray or mouse analog. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: show ray; squeeze extra. Homework: select vs squeeze. Quiz: XRInputSource, select, why debug ray.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | select listener | Plant mouse-only VR. |
| 15–40 | Draw the ray | Plant no debug. |
| 40–55 | Inline click analog | Headset lottery plant. |
| 55–60 | They recolor a cube | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. show ray.
2. squeeze extra.

---

## Homework

1. Written: input source fields.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
controller.addEventListener('select', onSelect);
```

---

## Extra exercises

See [[XR/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. mouse-only and calling it VR.
2. no ray debug.

## If we run long, cut

Haptics API. Keep select + ray.

## If we run short, add

squeeze extra.
