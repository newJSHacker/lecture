# Lecture 5 — Flexbox

**Week 5 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** axis, wrap, alignment  
**Success check:** Set flex direction.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Web Technologies/code/04-flex.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: axis, wrap, alignment | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
row of three cards
Axes.
Navbar.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** One-dimensional layout. Flex is a row or a column.

**Ask:** Set flex direction? Wait seven seconds. Take two answers.

**Board:** parked strip. Then row of three cards.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *axis, wrap, alignment*.

**Do not:** Nested flex until the page is soup.

### Minutes 10–12 — Frame

**Say:** Today’s question: axis, wrap, alignment. Kernel: axis, wrap, alignment. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Nested flex until the page is soup.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** One-dimensional layout. Flex is a row or a column.

**Say:** Alignment. justify-content vs align-items.

**Say:** gap. Prefer gap over margin hacks.

**Ask:** Set flex direction? Wait seven seconds. Take two answers.

**They do:** On paper: Holy-grail header/main/footer with flex column on body.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Navbar + three equal cards.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Holy-grail header/main/footer with flex column on body.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Holy-grail header/main/footer with flex column on body.; A toolbar of buttons.. Homework: Written: main vs cross axis.; Code: responsive wrap of chips.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: axis, wrap, alignment | Plant the first common mistake. |
| 10–30 | Navbar + three equal cards. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. flex-direction column (2)
2. justify-content (4)
3. gap vs margin (4)


## Snippet

```css
.row { display: flex; gap: 1rem; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. One-dimensional layout.** Flex is a row or a column. Navbars, toolbars, HUD over a canvas.

**2. Alignment.** justify-content vs align-items. Students mix these every year — live-code both.

**3. gap.** Prefer gap over margin hacks.

---

## Common mistakes

1. Nested flex until the page is soup.
2. Absolute positioning instead of flex.

## If we run long, cut

gap

## If we run short, add

A toolbar of buttons.
