# Lecture 7 — Responsive and media

**Week 7 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** viewport meta; one breakpoint with min-width; fluid images  
**Success check:** they can show the same page readable at ~360px and desktop without a second site

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Web Technologies/code/06-responsive.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: one document, two widths | Invariant: responsive is layout change, not a separate mobile app`

## Board at the end (they photograph this)

```
<meta name="viewport" content="width=device-width, initial-scale=1"/>

@media (min-width: 720px) { … }

img { max-width: 100%; height: auto; }
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Phone screenshot of a desktop-only page overflowing | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Capstone must work on a phone. Viewport meta is not optional. We do not invent a second URL.

**Ask:** What happens without the viewport meta on a phone? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *viewport, breakpoints*.

**Do not:** Only testing at 1920px.

### Minutes 10–12 — Frame

**Say:** Mobile first: default is the small layout; min-width adds columns. Breakpoint: pick one number and freeze it for the lab.

**Ask:** min-width vs max-width — which matches mobile-first?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Viewport. Then fluid images.

**Board:** one breakpoint. Two sketches: stacked vs two-column.

**Say:** DevTools device mode is a lie-detector, not a real phone — still use it today.

**Ask:** Why height: auto on img?

**They do:** Sketch stacked vs 720px two-column.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Stack cards, then row at 720px. Demo 06-responsive.html. Plant missing viewport.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Last week’s grid stacks under 720px. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: viewport + one breakpoint. Homework: overflow screenshot. Quiz: viewport, min-width, img rule.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Viewport | Plant missing meta. |
| 15–40 | Breakpoint | Plant max-width spaghetti. |
| 40–55 | Fluid img | Broken height. |
| 55–60 | They stack the grid | Circulate. |

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

None this meeting.


## Snippet

```html
<meta name="viewport" content="width=device-width, initial-scale=1"/>
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Only testing at 1920px.
2. Tiny tap targets.

## If we run long, cut

Three breakpoints. Keep one.

## If we run short, add

prefers-reduced-motion name — Lecture 13.
