# Lecture 9 — Accessibility in 3D

**Week 9 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** keyboard cycle, HUD name, reduced-motion stops auto orbit  
**Success check:** they can tab or press Next to select three parts and read the name without the mouse

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: 3D that a keyboard can use | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
Next part   (button, focus visible)
HUD text    =  selected name
outline     +  label   (not color alone)

prefers-reduced-motion → stop auto orbit
no 3 Hz strobe
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Orbit is a mouse skill. A canvas with no keyboard story fails this course and XR later. Color-only selection fails.

**Ask:** Can you use this page with keyboard only? Wait. Then try.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *keyboard, labels, motion*.

**Do not:** Canvas-only with no DOM.

### Minutes 10–12 — Frame

**Say:** Reset camera. Cycle parts. HUD names them. Bloom caps. Empty alt only if decorative — the HUD is not decorative.

**Ask:** When is outline:none a fail?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Hostile by default. Provide a path.

**Board:** Next + HUD + outline. Reduced-motion stops spin.

**Say:** Seizure: no 3 Hz strobe. We do not invent Lighthouse scores.

**Ask:** Why is color-only selection a fail?

**They do:** Tab the HUD; list what fails.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Keyboard cycles three parts; HUD names them. Plant canvas-only. Plant outline:none. Fix button + focus.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Next-part button + label. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: focus styles; reduced-motion kills auto orbit. Homework: keyboard path paragraph. Quiz: Next, not color-only, reduced-motion.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | div-as-control | Plant. Fix button. |
| 15–40 | Cycle + HUD name | Color-only plant. |
| 40–55 | Reduced-motion | Auto orbit plant. |
| 55–60 | They add focus-visible | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. focus styles.
2. reduced motion stops auto orbit.

---

## Homework

1. Written: a11y checklist 10 items.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```jsx
<button onClick={selectNext}>Next part</button>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. canvas-only with no DOM.
2. outline:none everywhere.

## If we run long, cut

Full WCAG sermon. Keep keyboard + label.

## If we run short, add

Reset-camera button.
