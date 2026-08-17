# Lecture 9 — Accessibility in 3D

**Week 9 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** keyboard, labels, motion  
**Success check:** Keyboard select next part.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: keyboard, labels, motion | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
tab to parts; aria on HUD
Tab order.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** 3D is hostile by default. Orbit is a mouse skill.

**Ask:** Keyboard select next part? Wait seven seconds. Take two answers.

**Board:** parked strip. Then tab to parts; aria on HUD.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *keyboard, labels, motion*.

**Do not:** Canvas-only with no DOM.

### Minutes 10–12 — Frame

**Say:** Today’s question: keyboard, labels, motion. Kernel: keyboard, labels, motion. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: canvas-only with no DOM.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** 3D is hostile by default. Orbit is a mouse skill.

**Say:** Color. Not the only channel.

**Say:** Seizure. No 3Hz strobe.

**Ask:** Keyboard select next part? Wait seven seconds. Take two answers.

**They do:** On paper: focus styles.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Keyboard cycles three parts; HUD names them.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** focus styles.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: focus styles.; reduced motion stops auto orbit.. Homework: Written: a11y checklist 10 items.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: keyboard, labels, motion | Plant the first common mistake. |
| 10–30 | Keyboard cycles three parts; HUD names them. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. why HUD text (3)
2. keyboard (4)
3. strobe (3)


## Snippet

```jsx
<button onClick={selectNext}>Next part</button>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. 3D is hostile by default.** Orbit is a mouse skill. Provide: reset camera, keyboard cycle, HUD text for the selected part.

**2. Color.** Not the only channel. Selection outline + label.

**3. Seizure.** No 3Hz strobe. Bloom caps.

---

## Common mistakes

1. canvas-only with no DOM.
2. outline:none everywhere.

## If we run long, cut

Seizure

## If we run short, add

reduced motion stops auto orbit.
