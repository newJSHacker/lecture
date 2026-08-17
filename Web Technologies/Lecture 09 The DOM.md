# Lecture 9 — The DOM

**Week 9 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** createElement, append, textContent; a list built from an array  
**Success check:** they can build three <li> from an array without writing HTML strings

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Web Technologies/code/07-toggle.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: nodes, not HTML soup | Invariant: the DOM is a tree you mutate; strings of tags are a last resort`

## Board at the end (they photograph this)

```
document.createElement('li')
li.textContent = item
ul.append(li)

querySelector  →  one
querySelectorAll → list
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** A scene graph later is the same idea: create a node, append it. Today the node is an element.

**Ask:** Why not ul.innerHTML += '<li>'+item? Wait. Want: escaping, slowness, XSS.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *nodes, createElement*.

**Do not:** InnerHTML += in a loop (slow and XSS).

### Minutes 10–12 — Frame

**Say:** createElement, append, remove. textContent. querySelectorAll forEach.

**Ask:** append vs innerHTML for a list from data?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Document is the root. Body is a child.

**Board:** create / append. Array of strings → ul.

**Say:** innerHTML of trusted static chrome is a maybe; never for user data.

**Ask:** What does querySelectorAll return?

**They do:** On paper: steps to add one li.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Build a todo list from ['a','b','c']. Demo 07-toggle.html or 08-todo.html. Plant innerHTML.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Render three people names as li. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: list from array. Homework: remove a node. Quiz: createElement, why not innerHTML, querySelectorAll.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | createElement | Plant innerHTML +=. |
| 15–40 | Array → ul | Forgot textContent. |
| 40–55 | Remove one | They try. |
| 55–60 | They render names | Circulate. |

Point them at `Web Technologies/code/07-toggle.html` as the after-class check, not as the lecture.

---

## Lab

1. Filter done items.
2. Do not use innerHTML to build the list from a string of tags if the text is user-provided — textContent on a created li.

---

## Homework

1. Written: source vs DOM.
2. Code: list of 20 items created in a loop.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const li = document.createElement('li');
li.textContent = text;
ul.append(li);
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. innerHTML += in a loop (slow and XSS).

## If we run long, cut

DocumentFragment. Keep create+append.

## If we run short, add

cloneNode name.
