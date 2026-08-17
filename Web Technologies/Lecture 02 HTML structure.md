# Lecture 2 — HTML structure

**Week 2 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** tree, tags, a first page  
**Success check:** Write a valid skeleton.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Web Technologies/code/01-skeleton.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: tree, tags, a first page | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
html > head + body
Tree.
Skeleton.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Tags and tree. HTML is a tree, not a canvas.

**Ask:** a valid skeleton? Wait seven seconds. Take two answers.

**Board:** parked strip. Then html > head + body.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tree, tags, a first page*.

**Do not:** Div soup already.

### Minutes 10–12 — Frame

**Say:** Today’s question: tree, tags, a first page. Kernel: tree, tags, a first page. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: div soup already.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Tags and tree. HTML is a tree, not a canvas.

**Say:** head vs body. title, charset, viewport meta.

**Say:** Semantics preview. h1–h6, p, a, img.

**Ask:** a valid skeleton? Wait seven seconds. Take two answers.

**They do:** On paper: About-me page.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Build a one-screen personal page: heading, paragraph, list, link.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** About-me page.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: About-me page.; Validate nesting by indenting.. Homework: Clone a simple Wikipedia intro layout (structure only).. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: tree, tags, a first page | Plant the first common mistake. |
| 10–30 | Build a one-screen personal page: heading, paragraph, list, link. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/01-skeleton.html` as the after-class check, not as the lecture.

---

## Lab

1. About-me page.
2. Validate nesting by indenting.

---

## Homework

1. Clone a simple Wikipedia intro layout (structure only).

---

## Quiz next meeting (they hear this now)

1. Purpose of charset (2)
2. Where does title show (3)
3. Why indent (5)


## Snippet

```html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"/><title>IGWT</title></head>
<body></body>
</html>
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Tags and tree.** HTML is a tree, not a canvas. Mismatched tags are the DOM cousin of a broken mesh.

**2. head vs body.** title, charset, viewport meta. Body is visible content.

**3. Semantics preview.** h1–h6, p, a, img. Semantic week is next; this week structure.

---

## Common mistakes

1. div soup already.
2. GBK charset guesses.

## If we run long, cut

Semantics preview

## If we run short, add

Validate nesting by indenting.
