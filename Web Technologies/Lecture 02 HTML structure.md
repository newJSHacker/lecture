# Lecture 2 — HTML structure

**Week 2 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** <!DOCTYPE html> skeleton; html > head + body tree  
**Success check:** they indent a nested list and the validator in their head matches the indent

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Web Technologies/code/01-skeleton.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a first page that is a tree | Invariant: HTML is a tree, not Photoshop`

## Board at the end (they photograph this)

```
html
  head   title, meta charset
  body   heading, p, ul, a

<!DOCTYPE html>
<html lang="en"> … </html>
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last time: a request. Today: the document the server sent. Tags nest. If you do not indent, you will not see a broken tree.

**Ask:** Where does <title> show — in the page body or the tab? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tree, tags, a first page*.

**Do not:** Div soup already.

### Minutes 10–12 — Frame

**Say:** Skeleton: doctype, html lang, head charset, title, body. Purpose of charset: the browser must not guess. lang matters for a11y later.

**Ask:** Why indent?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Tree on the board: html splits into head and body. Head is not visible text.

**Board:** skeleton. Closing tags as matching brackets.

**Say:** Heading, paragraph, list, link. A personal page is enough. We do not paint in a visual editor.

**Ask:** Purpose of charset?

**They do:** On paper: nest ul inside a section, indent.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Build a one-screen personal page live: heading, paragraph, list, link. Plant an unclosed <p>. Read the tree in Elements.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** About-me page. Validate nesting by indenting. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: about-me + indent. Homework: Wikipedia intro layout, structure only. Quiz: charset, where title shows, why indent.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Skeleton | Plant missing charset. |
| 10–30 | Personal page | Plant unclosed tag. |
| 30–45 | Elements tree | They match indent to DOM. |
| 45–60 | They finish about-me | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. div soup already.
2. GBK charset guesses.

## If we run long, cut

Every HTML5 sectioning element. Keep skeleton + tree.

## If we run short, add

One <img> with alt, local file, no CDN.
