# Lecture 5 — CSS transitions

**Week 5 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** hover, states  
**Success check:** transition property.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Interactive Web/code/05-css.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: hover, states | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
transition: transform .2s
Lift.
media.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** States. hover, focus, class on.

**Ask:** transition property? Wait seven seconds. Take two answers.

**Board:** parked strip. Then transition: transform .2s.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *hover, states*.

**Do not:** Transition: all 1s.

### Minutes 10–12 — Frame

**Say:** Today’s question: hover, states. Kernel: hover, states. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: transition: all 1s.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** States. hover, focus, class on.

**Say:** Properties. transform and opacity composite.

**Say:** Motion. Respect reduced motion.

**Ask:** transition property? Wait seven seconds. Take two answers.

**They do:** On paper: reduced-motion media query.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A button that lifts on hover; a class toggle.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** reduced-motion media query.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: reduced-motion media query.; Don't transition width.. Homework: Written: why transform.; Code: card.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: hover, states | Plant the first common mistake. |
| 10–30 | A button that lifts on hover; a class toggle. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/05-css.html` as the after-class check, not as the lecture.

---

## Lab

1. reduced-motion media query.
2. Don't transition width.

---

## Homework

1. Written: why transform.
2. Code: card.

---

## Quiz next meeting (they hear this now)

1. which props (4)
2. reduced motion (3)
3. transition all smell (3)


## Snippet

```css
@media (prefers-reduced-motion: reduce){ * { transition: none !important; } }
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. States.** hover, focus, class on.

**2. Properties.** transform and opacity composite. Layout-triggering props jank.

**3. Motion.** Respect reduced motion. Inclusive teaching.

---

## Common mistakes

1. transition: all 1s.
2. ignoring reduced motion.

## If we run long, cut

Motion

## If we run short, add

Don't transition width.
