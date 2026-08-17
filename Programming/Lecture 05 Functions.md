# Lecture 5 — Functions

**Week 5 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `clamp(x,a,b)` and `lerp(a,b,t)` with `console.assert`  
**Success check:** they write a function that **returns** a value, not only `console.log`

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Programming/code/05-clamp.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: name a recipe | Invariant: parameters in, one return out; locals die at the brace`

## Board at the end (they photograph this)

```
        in →  [ clamp ]  → out
               x, a, b

function clamp(x, a, b) {
  return Math.max(a, Math.min(b, x));
}

missing return  →  undefined
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** A function is a named recipe. `putPixel`, `dot`, `orient` later are functions. If you cannot write `clamp`, you cannot write a renderer.

**Ask:** What does a function return if you forget `return`? Wait. Want: `undefined`.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`clamp(x,a,b)` and `lerp(a,b,t)` with `console.assert`*.

**Do not:** Functions that only log.

### Minutes 10–12 — Frame

**Say:** Parameters are local names. Arguments are the values you pass. `console.log` inside is a side effect — fine for debugging, not the result of a math helper.

**Ask:** Is `clamp` allowed to print instead of returning? Want: no.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw a box. Arrows in: `x,a,b`. Arrow out: the clamped number.

**Board:** two stack frames: `main` calls `clamp`. Locals of `clamp` are not visible in `main`.

**Say:** `let` is block-scoped. Loop `i` dies after the `for`. No globals for math helpers. Name functions with verbs: `clamp`, `lerp`, `countVowels`.

**Ask:** Why `const` for `t` in lerp? Want: we do not rebind t.

**They do:** On paper: write `lerp(a,b,t)` in one line.

**Do not:** Mix Python syntax into a JS term. Skip the attempt.

### Minutes 35–50 — Show

**Say:** I implement `clamp`, `lerp`, `min3`. I `console.assert(lerp(0,10,0.5)===5)`. When an assert fails, I read it out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Write `isEven` and `max3` that **return**. Eight minutes. I reject solutions that only log.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: isEven, max3, countVowels. Homework: 8 tests for lerp; side effect vs return. Quiz: missing return, `let` in for, write clamp.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | `clamp` with asserts | Plant a swapped min/max. |
| 10–30 | `lerp` | Plant `a + t*b` wrong formula. Fix `a + (b-a)*t`. |
| 30–45 | `min3` | Show nested calls. |
| 45–60 | They write countVowels kernel | Circulate. |

Point them at `Programming/code/05-clamp.html` as the after-class check, not as the lecture.

---

## Lab

1. isEven, max3, countVowels.
2. A function that returns, not only logs.

---

## Homework

1. 8 tests for lerp.
2. Written: side effect vs return.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
```

---

## Extra exercises

See [[Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Functions that only log.
2. Globals for everything.

## If we run long, cut

Closures. They wait until Modern JS.

## If we run short, add

A function that returns another function — name only.
