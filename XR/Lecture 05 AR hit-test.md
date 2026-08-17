# Lecture 5 — AR hit-test

**Week 5 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** hit-test pose on a plane, or inline fake plane; ARKit-native is not the homework  
**Success check:** they can place an object on a real hit-test or a documented fake plane

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: place on a plane without a headset lottery | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
immersive-ar  +  hit-test source
desktop: often no AR  →  mouse-place on fake plane

requestHitTestSource({ space: viewerSpace })
document the device     camera permission
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** AR is a pose on a detected plane. Desktop often has no AR. The lab is real hit-test or a fake plane — written in the README. Native ARKit as the homework is out of scope.

**Ask:** If Chrome on the lab laptop has no AR, what do you submit? Wait. Want: inline fake plane + the same place verb.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *plane detection idea*.

**Do not:** ARKit-only native app as the homework.

### Minutes 10–12 — Frame

**Say:** Anchors persist next week. Privacy: camera. Policy in the syllabus. Remove-last extra.

**Ask:** What is a hit-test in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Plane detection idea. Pose, not a mesh of the room.

**Board:** hit-test vs fake plane. Same place verb.

**Say:** Document device. No lottery.

**Ask:** Why is an ARKit app the wrong homework?

**They do:** README two lines: device, fallback.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Place on plane or fake plane. Plant no fallback. Plant native-only. Remove-last extra.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Click-to-place on a plane (fake OK). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: document device; remove-last extra. Homework: fallback paragraph. Quiz: hit-test, fake plane, camera.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Hit-test name | Plant ARKit homework. |
| 15–40 | Place on plane / fake | Plant no fallback. |
| 40–55 | Document device | Lottery plant. |
| 55–60 | They place one object | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. document device.
2. remove last extra.

---

## Homework

1. Written: fallback if no AR.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const src = await session.requestHitTestSource({ space: viewerSpace });
```

---

## Extra exercises

See [[XR/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. ARKit-only native app as the homework.
2. no fallback.

## If we run long, cut

Privacy law. Keep place + fallback.

## If we run short, add

Remove last extra.
