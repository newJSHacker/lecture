# Lecture 6 — Anchors and persistence

**Week 6 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** anchor = world-locked pose this session; honesty about 'forever'  
**Success check:** they can place two anchored cubes that stay while walking, or say the inline analog

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: locked pose, not a floating bug | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
createAnchor(pose, space)
this session  ≠  cloud forever

meters     a 10 m cube is a bug
unanchored HUD floats — call it out
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Anchors are a stable pose in the XR world. Cloud anchors as required work is a lottery and a product claim we do not make. Scale is meters — Blender habit.

**Ask:** If I walk around, why did the cube follow my head? Wait. Want: never anchored.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *world-locked pose*.

**Do not:** Cloud anchors as required.

### Minutes 10–12 — Frame

**Say:** UA-dependent. Student honesty: this session vs forever. Clear-all. 0.2 m object as a sanity check.

**Ask:** What do you write if persistence is not available?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** World-locked vs head-locked.

**Board:** createAnchor. Session vs forever.

**Say:** Scale. Furniture is not 10 m.

**Ask:** Why is a cloud-anchor vendor the wrong required lab?

**They do:** On paper: two poses, walk, they stay.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Two anchored cubes; walk. Plant unanchored floating UI. Plant cloud required. Inline: parent to world, not camera.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Two world-locked boxes (inline parent OK). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: clear all; 0.2 m scale. Homework: session vs forever. Quiz: anchor, meters, no cloud required.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Anchor vs float | Plant head-locked cube. |
| 15–40 | Two cubes stay | Plant cloud required. |
| 40–55 | Scale 0.2 m | 10 m plant. |
| 55–60 | They clear all | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. clear all.
2. scale 0.2 m object.

---

## Homework

1. Written: session vs persistent.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const anchor = await frame.createAnchor(pose, space);
```

---

## Extra exercises

See [[XR/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. cloud anchors as required.
2. unanchored floating UI.

## If we run long, cut

Cloud maps. Keep session anchor + scale.

## If we run short, add

0.2 m object as a ruler.
