# Lecture 5 — Flexbox

**Week 5 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** flex container: direction, wrap, justify-content, align-items  
**Success check:** they can make a row of three cards that wrap without float

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Web Technologies/code/04-flex.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: a row that wraps on purpose | Invariant: flex is one axis plus a cross axis; float is not how we layout in this course`

## Board at the end (they photograph this)

```
display: flex
main axis →     justify-content
cross axis ↓    align-items

flex-wrap: wrap
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** A HUD later is a flex row. Floats are history in this program.

**Ask:** Which axis does flex-direction: row run along? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *axis, wrap, alignment*.

**Do not:** Nested flex until the page is soup.

### Minutes 10–12 — Frame

**Say:** Container properties vs item flex: 1. Gap. We freeze: no float layouts.

**Ask:** What does wrap do when the row is too wide?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Container first. Then items.

**Board:** main vs cross. Three boxes.

**Say:** justify vs align. Mix them up once on purpose.

**Ask:** flex: 1 means?

**They do:** On paper: nav with logo left, links right — which justify?

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Three cards in a row, wrap. Demo 04-flex.html. Plant forgot wrap.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Header: logo + nav links with space-between. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: wrapping cards. Homework: header. Quiz: main axis, wrap, no floats.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Row of boxes | Plant float. |
| 15–40 | Wrap + gap | Plant margin hacks. |
| 40–55 | space-between header | They copy. |
| 55–60 | They wrap cards | Circulate. |

Point them at `Web Technologies/code/04-flex.html` as the after-class check, not as the lecture.

---

## Lab

1. Holy-grail header/main/footer with flex column on body.
2. A toolbar of buttons.

---

## Homework

1. Written: main vs cross axis.
2. Code: responsive wrap of chips.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```css
.row { display: flex; gap: 1rem; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Nested flex until the page is soup.
2. Absolute positioning instead of flex.

## If we run long, cut

flex-grow math. Keep wrap + axes.

## If we run short, add

align-self on one item.
