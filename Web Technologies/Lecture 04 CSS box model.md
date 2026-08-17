# Lecture 4 — CSS box model

**Week 4 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** content + padding + border + margin; box-sizing: border-box as course policy  
**Success check:** they can draw the box of a 200px element with padding 20 and say the used width under border-box

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Web Technologies/code/03-box.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: stop guessing spacing | Invariant: every visible thing is a box; margin is outside`

## Board at the end (they photograph this)

```
  margin
    border
      padding
        content

box-sizing: border-box     (course policy)
width includes padding+border
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: a box-model overlay screenshot from DevTools | the overlay is a photo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** CSS is not a paint program. It is boxes. If width surprises you, you forgot padding.

**Ask:** Is margin inside the border? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *margin border padding content*.

**Do not:** !important everywhere.

### Minutes 10–12 — Frame

**Say:** Content, padding, border, margin. Course policy: border-box so width means the box you see. display block vs inline named.

**Ask:** What does width include under border-box?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw four nested rectangles. Label them.

**Board:** border-box vs content-box with numbers: 200 + padding.

**Say:** DevTools computed box. We inspect, we do not guess.

**Ask:** Margin collapse name — do we need it today? Want: name only.

**They do:** On paper: a 200px border-box with 20px padding — content width?

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** A card with padding. Plant content-box. Switch to border-box. Demo 03-box.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A card: image placeholder, title, two paragraphs. Border-box. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: card + inspect. Homework: draw three boxes from a screenshot. Quiz: four layers, border-box, margin vs padding.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Four layers | Plant margin inside. |
| 15–40 | border-box | Plant content-box width surprise. |
| 40–55 | Inspect | Computed pane. |
| 55–60 | They build the card | Circulate. |

Point them at `Web Technologies/code/03-box.html` as the after-class check, not as the lecture.

---

## Lab

1. A card with padding and a border.
2. Two boxes side by side with inline-block or flex preview.

---

## Homework

1. Written: content-box vs border-box.
2. Code: a priced product card.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```css
* { box-sizing: border-box; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. !important everywhere.
2. Mixing units randomly.

## If we run long, cut

Position absolute. Keep the four layers.

## If we run short, add

box-shadow as a fifth decoration, not a layer of the model.
