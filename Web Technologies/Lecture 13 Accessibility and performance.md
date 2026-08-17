# Lecture 13 — Accessibility and performance

**Week 13 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** label, alt, keyboard path, contrast; LCP as a named metric not a number we invent  
**Success check:** they can tab through the page and every image has alt; they name LCP without a fake score

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Web Technologies/code/10-transform.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: usable, then maybe pretty | Invariant: if it cannot be used with a keyboard, it is not done; do not invent Lighthouse scores`

## Board at the end (they photograph this)

```
alt on img     label on input     one :focus visible

keyboard: Tab through the lab page

LCP  =  largest contentful paint   (name; measure later, do not invent)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** R3F and XR inherit this. A canvas with no keyboard story fails the experience course. Contrast is not a theme preference.

**Ask:** Can you use this page with the keyboard only? Wait. Then try.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *a11y, LCP name*.

**Do not:** Outline: none without a replacement.

### Minutes 10–12 — Frame

**Say:** alt empty only if decorative. Focus visible. Reduced motion named. LCP/CLS names — no invented scores.

**Ask:** When is alt="" correct?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Perceivable, operable. Skip the four-letter sermon; show the page.

**Board:** alt, label, focus. LCP name.

**Say:** Images without dimensions cause layout shift — CLS name.

**Ask:** What is LCP in one sentence?

**They do:** Tab the lab page; list what fails.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** A pretty button that is not a button (div). Plant. Fix with <button>. No Lighthouse number unless you run it live.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fix alt + labels + focus on last week’s page. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: keyboard path. Homework: alt audit. Quiz: alt, focus, LCP name. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | div-as-button | Plant. Fix button. |
| 15–40 | alt + label | Empty alt on content image. |
| 40–55 | Tab order | They walk it. |
| 55–60 | They fix focus | Circulate. |

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

None this meeting.


## Snippet

```css
:focus-visible { outline: 2px solid #1a4f8b; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. outline: none without a replacement.
2. Autoplaying loud video.

## If we run long, cut

ARIA soup. Keep alt, label, keyboard.

## If we run short, add

prefers-reduced-motion one rule.
