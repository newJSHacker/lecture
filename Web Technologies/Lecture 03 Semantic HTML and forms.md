# Lecture 3 — Semantic HTML and forms

**Week 3 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** nav, main, form: label+input, submit does a GET until we say otherwise  
**Success check:** every input has a label they can click

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Web Technologies/code/02-form.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: a page with a meaning | Invariant: semantics is for machines and humans; a div soup is not a form`

## Board at the end (they photograph this)

```
header / nav / main / footer

<label for="email">Email</label>
<input id="email" name="email" />

form without label  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** A configurator later is a form on top of WebGL. If they cannot label an input, they cannot ship a UI.

**Ask:** Can you click the word Email and focus the box? Wait. Want: only if label for=id.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *nav, main, form controls*.

**Do not:** Placeholder as label.

### Minutes 10–12 — Frame

**Say:** nav, main, footer. Forms: name attributes are what would be submitted. We do not post to a backend this week.

**Ask:** Why not only placeholder instead of a label?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Landmark elements. One main.

**Board:** label+input. for/id pair.

**Say:** button type submit vs button. Required and type=email as names.

**Ask:** What does name= do?

**They do:** On paper: a two-field form with labels.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** A tiny search form. Plant an input with only placeholder. Then add a real label.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Contact form: name, email, message. Every control labeled. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: labeled form. Homework: landmarks on last week’s page. Quiz: for/id, one main, placeholder vs label.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Landmarks | Two mains as the plant. |
| 10–35 | Form | Plant unlabeled input. |
| 35–50 | Click the label | They feel the focus. |
| 50–60 | They add message field | Circulate. |

Point them at `Web Technologies/code/02-form.html` as the after-class check, not as the lecture.

---

## Lab

1. Fieldset of radio materials.
2. One error message associated with an input.

---

## Homework

1. Written: why label-for.
2. Code: form that prevents default and logs JSON.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" required/>
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Placeholder as label.
2. Unlabeled inputs.

## If we run long, cut

Every input type. Keep label+main.

## If we run short, add

fieldset/legend name only.
