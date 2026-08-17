# Lecture 1 — ES6 bindings and arrows

**Week 1 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** let const arrow  
**Success check:** let/const.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Modern JavaScript/code/01-arrows.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: let const arrow | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
function vs =>
Binding table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Why ES6+. The language of Three.js examples.

**Ask:** let/const? Wait seven seconds. Take two answers.

**Board:** parked strip. Then function vs =>.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *let const arrow*.

**Do not:** Var.

### Minutes 8–12 — Frame

**Say:** Today’s question: let const arrow. Kernel: let const arrow. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: var.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why ES6+. The language of Three.js examples.

**Say:** Arrows. Shorter, lexical this.

**Say:** Defaults. function f(x=0).

**Ask:** let/const? Wait seven seconds. Take two answers.

**They do:** On paper: 5 arrows with tests.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Rewrite a var/function script into const/arrows.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** 5 arrows with tests.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: 5 arrows with tests.; A default-param helper.. Homework: Written: this and arrows, 1 page.; Code: rewrite.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: let const arrow | Plant the first common mistake. |
| 10–30 | Rewrite a var/function script into const/arrows. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/01-arrows.html` as the after-class check, not as the lecture.

---

## Lab

1. 5 arrows with tests.
2. A default-param helper.

---

## Homework

1. Written: this and arrows, 1 page.
2. Code: rewrite.

---

## Quiz next meeting (they hear this now)

1. const rebound (3)
2. arrow vs function construct (4)
3. default param (3)


## Snippet

```js
const add = (a, b = 0) => a + b;
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Why ES6+.** The language of Three.js examples. Teaching old var is harm.

**2. Arrows.** Shorter, lexical this. Not identical to function in all ways — constructors.

**3. Defaults.** function f(x=0).

---

## Common mistakes

1. var.
2. arrows as constructors.

## If we run long, cut

Defaults

## If we run short, add

A default-param helper.
