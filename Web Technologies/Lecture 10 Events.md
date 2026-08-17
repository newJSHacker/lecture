# Lecture 10 — Events

**Week 10 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** bubble, preventDefault  
**Success check:** addEventListener.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Web Technologies/code/07-toggle.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: bubble, preventDefault | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
click on button inside form
Bubble arrows.
Canvas clicks.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** The event object. type, target, currentTarget.

**Ask:** addEventListener? Wait seven seconds. Take two answers.

**Board:** parked strip. Then click on button inside form.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *bubble, preventDefault*.

**Do not:** Onclick attributes.

### Minutes 10–12 — Frame

**Say:** Today’s question: bubble, preventDefault. Kernel: bubble, preventDefault. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: onclick attributes.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The event object. type, target, currentTarget.

**Say:** Delegation. One listener on ul for many li.

**Say:** Default actions. Forms navigate; links navigate.

**Ask:** addEventListener? Wait seven seconds. Take two answers.

**They do:** On paper: Keyboard move a box.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Canvas or div: click to place a dot (DOM or Canvas 2D).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Keyboard move a box.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Keyboard move a box.; Delegation on a list.. Homework: Written: bubble in 6 sentences.; Code: draw dots on click.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: bubble, preventDefault | Plant the first common mistake. |
| 10–30 | Canvas or div: click to place a dot (DOM or Canvas 2D). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/07-toggle.html` as the after-class check, not as the lecture.

---

## Lab

1. Keyboard move a box.
2. Delegation on a list.

---

## Homework

1. Written: bubble in 6 sentences.
2. Code: draw dots on click.

---

## Quiz next meeting (they hear this now)

1. preventDefault why (3)
2. target vs currentTarget (4)
3. key vs code (3)


## Snippet

```js
form.addEventListener('submit', (e) => { e.preventDefault(); });
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. The event object.** type, target, currentTarget. Keyboard `event.key`.

**2. Delegation.** One listener on ul for many li. Graphics: one pointer listener on canvas.

**3. Default actions.** Forms navigate; links navigate. preventDefault when the page should stay.

---

## Common mistakes

1. onclick attributes.
2. Forgetting preventDefault and wondering why the page reloads.

## If we run long, cut

Default actions

## If we run short, add

Delegation on a list.
