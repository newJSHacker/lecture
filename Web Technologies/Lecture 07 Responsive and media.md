# Lecture 7 — Responsive and media

**Week 7 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** viewport, breakpoints  
**Success check:** Set viewport meta.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Web Technologies/code/06-responsive.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: viewport, breakpoints | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
phone vs laptop frames
Frames.
Stack vs row.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Viewport. `width=device-width` or the page is 980px shrunk.

**Ask:** Set viewport meta? Wait seven seconds. Take two answers.

**Board:** parked strip. Then phone vs laptop frames.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *viewport, breakpoints*.

**Do not:** Only testing at 1920px.

### Minutes 10–12 — Frame

**Say:** Today’s question: viewport, breakpoints. Kernel: viewport, breakpoints. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Only testing at 1920px.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Viewport. `width=device-width` or the page is 980px shrunk.

**Say:** Breakpoints. Start from the actual layout breaking, not from Bootstrap's numbers.

**Say:** Images. max-width: 100%.

**Ask:** Set viewport meta? Wait seven seconds. Take two answers.

**They do:** On paper: Fix a horizontal overflow.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: A page that stacks cards under 640px.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fix a horizontal overflow.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Fix a horizontal overflow.; Fluid type with clamp extra.. Homework: Written: why viewport meta.; Code: two-breakpoint layout.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: viewport, breakpoints | Plant the first common mistake. |
| 10–30 | A page that stacks cards under 640px. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/06-responsive.html` as the after-class check, not as the lecture.

---

## Lab

1. Fix a horizontal overflow.
2. Fluid type with clamp extra.

---

## Homework

1. Written: why viewport meta.
2. Code: two-breakpoint layout.

---

## Quiz next meeting (they hear this now)

1. viewport meta (4)
2. min-width vs max-width (3)
3. max-width 100% on img (3)


## Snippet

```html
<meta name="viewport" content="width=device-width, initial-scale=1"/>
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Viewport.** `width=device-width` or the page is 980px shrunk. Required on every IGWT page.

**2. Breakpoints.** Start from the actual layout breaking, not from Bootstrap's numbers. One or two breakpoints is enough.

**3. Images.** max-width: 100%. Later: srcset name only.

---

## Common mistakes

1. Only testing at 1920px.
2. Tiny tap targets.

## If we run long, cut

Images

## If we run short, add

Fluid type with clamp extra.
