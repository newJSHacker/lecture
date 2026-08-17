# Lecture 9 — The DOM

**Week 9 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** nodes, createElement  
**Success check:** Walk parent/children.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Web Technologies/code/07-toggle.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: nodes, createElement | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
tree with a new li
DOM tree.
li append.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** The tree is live. Elements tab is the DOM after JS.

**Ask:** Walk parent/children? Wait seven seconds. Take two answers.

**Board:** parked strip. Then tree with a new li.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *nodes, createElement*.

**Do not:** InnerHTML += in a loop (slow and XSS).

### Minutes 10–12 — Frame

**Say:** Today’s question: nodes, createElement. Kernel: nodes, createElement. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: innerHTML += in a loop (slow and XSS).

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The tree is live. Elements tab is the DOM after JS.

**Say:** Create vs clone. createElement for one item.

**Say:** Lists. A todo list is the lab.

**Ask:** Walk parent/children? Wait seven seconds. Take two answers.

**They do:** On paper: Filter done items.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Todo: add item, remove item, no framework.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Filter done items.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Filter done items.; Do not use innerHTML to build the list from a string of tags if the text is user-provided — textContent on a created li.. Homework: Written: source vs DOM.; Code: list of 20 items created in a loop.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: nodes, createElement | Plant the first common mistake. |
| 10–30 | Todo: add item, remove item, no framework. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. createElement (3)
2. appendChild (3)
3. Why not innerHTML for user text (4)


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

**1. The tree is live.** Elements tab is the DOM after JS. View-source is not.

**2. Create vs clone.** createElement for one item. templates later.

**3. Lists.** A todo list is the lab. This is the scene graph of the document.

---

## Common mistakes

1. innerHTML += in a loop (slow and XSS).

## If we run long, cut

Lists

## If we run short, add

Do not use innerHTML to build the list from a string of tags if the text is user-provided — textContent on a created li.
