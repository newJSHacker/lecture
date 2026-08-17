# Lecture 10 — Events

**Week 10 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** addEventListener('click'); preventDefault on a submit; bubbling named  
**Success check:** they can stop a form from navigating and handle the click on a parent with bubbling

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Web Technologies/code/07-toggle.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: clicks without inline onclick | Invariant: the browser fires events; you listen; preventDefault stops the default verb`

## Board at the end (they photograph this)

```
el.addEventListener('click', handler)

form submit  →  preventDefault()   or the page reloads

bubble:  target → … → body
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** WebGL picking is an event. A HUD button is an event. onclick= in HTML is forbidden in this course.

**Ask:** Why did the page flash and clear when I clicked Submit? Wait. Want: default form GET.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *bubble, preventDefault*.

**Do not:** Onclick attributes.

### Minutes 10–12 — Frame

**Say:** addEventListener. preventDefault. stopPropagation named, not required. Touch = pointer later in Interactive Web.

**Ask:** Where do you put the listener — inline attribute or script?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Target vs currentTarget teaching-level.

**Board:** bubble arrows. preventDefault on submit.

**Say:** One listener on ul for many li — delegation idea.

**Ask:** What does preventDefault do on a link?

**They do:** On paper: handler that logs the clicked li text.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Form that does not navigate. Then ul delegation. Demo 07-toggle.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Button increments a counter in the DOM. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: preventDefault form + counter. Homework: bubbling paragraph. Quiz: addEventListener, preventDefault, no onclick=.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | click listener | Plant onclick=. |
| 15–40 | submit + preventDefault | Page reload plant. |
| 40–55 | Delegation on ul | They see one listener. |
| 55–60 | They build counter | Circulate. |

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

None this meeting.


## Snippet

```js
form.addEventListener('submit', (e) => { e.preventDefault(); });
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. onclick attributes.
2. Forgetting preventDefault and wondering why the page reloads.

## If we run long, cut

Custom events. Keep click + preventDefault.

## If we run short, add

keydown Enter on a button.
