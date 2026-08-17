# Lecture 1 — ES6 bindings and arrows

**Week 1 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** let/const (no var); arrow as expression; default param  
**Success check:** they rewrite a var/function helper to const + arrow and can say why new Arrow() fails

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Modern JavaScript/code/01-arrows.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: stop teaching 1999 JavaScript | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
let     rebind OK, block scope
const   no rebind; object fields still mutable
var     hoists — forbidden in this course

const add = (a, b = 0) => a + b;
=>  lexical this;  not a constructor
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** IGWT ships ES modules. Three.js samples are arrows and const. If we spend a week on var, the rest of the program fights us. Today: bindings and arrows.

**Ask:** What happens if you write const n = 1; n = 2? Wait seven seconds. Want: TypeError, not silent.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *let const arrow*.

**Do not:** Var.

### Minutes 8–12 — Frame

**Say:** Block scope. const is the default; let when you rebind. Arrow is shorter and lexical this — it is not function. We freeze: no var, no new on an arrow.

**Ask:** Can you call an arrow with new? Want: no.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A binding is a name. var hoists and leaks out of blocks — that is why we ban it.

**Board:** function add(a,b) vs const add = (a,b=0) => a+b. Circle default param.

**Say:** Arrows do not get their own this and cannot be constructors. Methods that need this wait until week 10.

**Ask:** Does const freeze the object? Want: no — only the binding.

**They do:** On paper: five arrows (double, even?, clamp, lerp, identity) plus one default-param helper.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Rewrite a var/function script into const/arrows live. Plant var i in a for and log it after the loop. Demo Modern JavaScript/code/01-arrows.html. Serve the folder if you later add type=module.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Five arrows with a console.assert each. Default-param helper last. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: arrows + asserts; a default-param helper. Homework: one page on this vs arrows; rewrite a var script. Quiz: const rebound, arrow as constructor, default param.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | const vs let vs var | Plant var hoisting after a block. |
| 10–30 | Rewrite to arrows | Plant new on an arrow. Read the TypeError. |
| 30–45 | Default param + map | They copy 01-arrows.html kernel. |
| 45–60 | They write five arrows | Circulate. No CDN. |

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

None this meeting.


## Snippet

```js
const add = (a, b = 0) => a + b;
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. var.
2. arrows as constructors.

## If we run long, cut

Defaults if the rewrite is still messy. Keep const + arrow.

## If we run short, add

A default-param helper with a test.
