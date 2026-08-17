# Lecture 13 — Accessibility and performance

**Week 13 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** a11y, LCP name  
**Success check:** Keyboard the lab page.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Web Technologies/code/10-transform.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: a11y, LCP name | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
focus ring on a button
Tab path.
Budget list.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Keyboard. Tab order.

**Ask:** Keyboard the lab page? Wait seven seconds. Take two answers.

**Board:** parked strip. Then focus ring on a button.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *a11y, LCP name*.

**Do not:** Outline: none without a replacement.

### Minutes 10–12 — Frame

**Say:** Today’s question: a11y, LCP name. Kernel: a11y, LCP name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: outline: none without a replacement.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Keyboard. Tab order.

**Say:** Performance. Images sized.

**Say:** Inclusive. [[Teaching/10 Inclusive Teaching and Accessibility]]

**Ask:** Keyboard the lab page? Wait seven seconds. Take two answers.

**They do:** On paper: Fix 3 a11y issues.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Audit the Week 7 page with keyboard + one axe DevTools pass (or checklist).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fix 3 a11y issues.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Fix 3 a11y issues.; Compress one image.. Homework: Written: three a11y checks.; Code: focus styles visible.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: a11y, LCP name | Plant the first common mistake. |
| 10–30 | Audit the Week 7 page with keyboard + one axe DevTools pass (or checklist). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/10-transform.html` as the after-class check, not as the lecture.

---

## Lab

1. Fix 3 a11y issues.
2. Compress one image.

---

## Homework

1. Written: three a11y checks.
2. Code: focus styles visible.

---

## Quiz next meeting (they hear this now)

1. alt purpose (3)
2. Why focus ring (4)
3. One perf budget (3)


## Snippet

```css
:focus-visible { outline: 2px solid #1a4f8b; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Keyboard.** Tab order. Skip links name. Canvas games need a non-pointer path or a documented limit.

**2. Performance.** Images sized. JS deferred. Later: glTF budgets in Blender week.

**3. Inclusive.** [[Teaching/10 Inclusive Teaching and Accessibility]]

---

## Common mistakes

1. outline: none without a replacement.
2. Autoplaying loud video.

## If we run long, cut

Inclusive

## If we run short, add

Compress one image.
