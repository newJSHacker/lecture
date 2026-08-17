# Lecture 9 — Performance in XR

**Week 9 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** stereo cost; framebuffer scale factor; cut bloom in VR; do not invent fps  
**Success check:** they can setFramebufferScaleFactor and write a table: device, scale, what they cut

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: a cheaper frame, honestly measured | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
two eyes     MSAA expensive     overdraw hurts
renderer.xr.setFramebufferScaleFactor(0.8)

cut bloom in VR     shadow map 512

device | scale | cut     — fps only if measured
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Two eyes. Desktop bloom stacks in VR are a common fail. Invented fps still forbidden. Scale 1.0 vs 0.7 is a look-vs-cost experiment — on a headset or a TA video, plus the same code path inline.

**Ask:** Does stereo mean two draws? Wait. Want: often yes, or multiview as a name.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *fill rate, foveation name*.

**Do not:** Desktop bloom stack unchanged in VR.

### Minutes 10–12 — Frame

**Say:** Multiview named. Quest targets documented, not invented. Student table required.

**Ask:** What do you cut first — bloom or the verb?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Fill rate. Overdraw. Two eyes.

**Board:** setFramebufferScaleFactor. Empty fps if unmeasured.

**Say:** Shadow 512. Bloom off in VR.

**Ask:** Why is desktop bloom a VR trap?

**They do:** Fill the three-column table on paper.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Scale 1.0 vs 0.7; note look vs cost. Do not quote fps unless measured here. Plant bloom-on. Plant 90.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** setFramebufferScaleFactor and log it. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: cut bloom; shadow 512. Homework: table. Quiz: two eyes, scale factor, no invented fps.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Stereo cost | Plant 90 fps. |
| 15–40 | Scale factor | Plant bloom stack. |
| 40–55 | Table on a named device | They write. |
| 55–60 | They cut bloom | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. cut bloom in VR.
2. shadow map 512.

---

## Homework

1. Written: stereo cost.
2. table.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
renderer.xr.setFramebufferScaleFactor(0.8);
```

---

## Extra exercises

See [[XR/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. desktop bloom stack unchanged in VR.
2. invented fps.

## If we run long, cut

Foveation implementation. Keep scale + table.

## If we run short, add

Shadow map 512.
