# Lecture 3 — Semantic HTML and forms

**Week 3 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** nav, main, form controls  
**Success check:** Use header/main/footer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Web Technologies/code/02-form.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: nav, main, form controls | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
label tied to input id
Page outline.
FormData.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Semantics. Screen readers and the outline.

**Ask:** header/main/footer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then label tied to input id.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *nav, main, form controls*.

**Do not:** Placeholder as label.

### Minutes 10–12 — Frame

**Say:** Today’s question: nav, main, form controls. Kernel: nav, main, form controls. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Placeholder as label.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Semantics. Screen readers and the outline.

**Say:** Forms. input, textarea, select.

**Say:** Accessibility. Focus order.

**Ask:** header/main/footer? Wait seven seconds. Take two answers.

**They do:** On paper: Fieldset of radio materials.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: A contact form that logs FormData in the console (no backend).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fieldset of radio materials.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Fieldset of radio materials.; One error message associated with an input.. Homework: Written: why label-for.; Code: form that prevents default and logs JSON.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: nav, main, form controls | Plant the first common mistake. |
| 10–30 | A contact form that logs FormData in the console (no backend). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. main vs div (3)
2. label for (4)
3. button type submit vs button (3)


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

**1. Semantics.** Screen readers and the outline. Inclusive teaching: [[Teaching/10 Inclusive Teaching and Accessibility]].

**2. Forms.** input, textarea, select. label[for]. required. This is how a configurator collects a material name later.

**3. Accessibility.** Focus order. Alt text. Color not the only channel.

---

## Common mistakes

1. Placeholder as label.
2. Unlabeled inputs.

## If we run long, cut

Accessibility

## If we run short, add

One error message associated with an input.
