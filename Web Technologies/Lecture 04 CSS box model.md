# Lecture 4 — CSS box model

**Week 4 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** margin border padding content  
**Success check:** Draw the box model.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Web Technologies/code/03-box.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: margin border padding content | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
box with four layers
Box model.
Computed panel.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Everything is a box. Layout is boxes.

**Ask:** Draw the box model? Wait seven seconds. Take two answers.

**Board:** parked strip. Then box with four layers.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *margin border padding content*.

**Do not:** !important everywhere.

### Minutes 10–12 — Frame

**Say:** Today’s question: margin border padding content. Kernel: margin border padding content. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: !important everywhere.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Everything is a box. Layout is boxes.

**Say:** border-box. Course policy: `* { box-sizing: border-box; }` in the reset.

**Say:** Cascade intro. Specificity later.

**Ask:** Draw the box model? Wait seven seconds. Take two answers.

**They do:** On paper: A card with padding and a border.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Color the content/padding/border/margin of one box using outlines.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A card with padding and a border.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: A card with padding and a border.; Two boxes side by side with inline-block or flex preview.. Homework: Written: content-box vs border-box.; Code: a priced product card.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: margin border padding content | Plant the first common mistake. |
| 10–30 | Color the content/padding/border/margin of one box using outlines. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. Four layers (4)
2. What border-box includes (3)
3. Inspect where (3)


## Snippet

```css
* { box-sizing: border-box; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Everything is a box.** Layout is boxes. Graphics people who skip this fight later UI overlays on WebGL canvases.

**2. border-box.** Course policy: `* { box-sizing: border-box; }` in the reset.

**3. Cascade intro.** Specificity later. This week: one stylesheet, class selectors.

---

## Common mistakes

1. !important everywhere.
2. Mixing units randomly.

## If we run long, cut

Cascade intro

## If we run short, add

Two boxes side by side with inline-block or flex preview.
