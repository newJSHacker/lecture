# Lecture 3 — Conditions

**Week 3 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `if (x === 0)` and the live bug `if (x = 0)`  
**Success check:** every student has used `===` in the attempt and can say why `=` inside `if` is a bug

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Programming/code/03-grade.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: branch on a fact | Invariant: a condition is a yes/no; assignment is not a question`

## Board at the end (they photograph this)

```
if (cond) { … } else if { … } else { … }

===  compare value and type
=    assign (forbidden as the condition)

&&  both     ||  either     !  not
NaN === NaN  →  false
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of `if (x = 0)` assigning 0 and taking the true branch | the console lie is a photo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Last time we named values. Today the program chooses. A graphics program that cannot refuse a bad input is a black screen later — `if (!gl)` is this lecture in WebGL.

**Ask:** What is the difference between `=` and `===`? Wait seven seconds. Take two answers. Then write both on the board.

**Board:** parked strip. Then true/false diamond.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *if / else / comparisons*.

**Do not:** Assignment in if.

### Minutes 10–12 — Frame

**Say:** We use `===` and `!==` in this course. I will show `==` once as a bug. Nested `if` more than two deep is a smell — extract a function (Lecture 5).

**Ask:** What should a program do when the WebGL context is null?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A boolean is `true` or `false`. Comparisons produce booleans. `===` asks: same value **and** same type.

**Board:** a diamond: condition → true path / false path. Then the three-way `if / else if / else`.

**Say:** `&&` both, `||` either, `!` not. `NaN === NaN` is false — show it. That is why we never test NaN with `===`.

**Ask:** Predict `0 == ''`. Hands. Then show `true`. Then `0 === ''` → `false`. That is why `==` is banned.

**They do:** On paper: write the `if` for age ≥ 18. Collect two papers.

**Do not:** mix Python syntax into a JS term. Do not skip the attempt.

### Minutes 35–50 — Show

**Say:** I will write a grade classifier: A/B/C/F. Then I will plant `if (score = 0)`. Watch the console. I will read the result out loud. Then I will fix it to `===`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fizz for multiples of 3 (not Buzz yet). Use `%` and `=== 0`. Eight minutes. I do not help for three.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: guessing game 1–10 and fizz. Homework: rock-paper-scissors and a paragraph on `==` vs `===`. Quiz next time: `0 == ''`, age `if`, why `===`.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Grade classifier with `===` | Plant a missing `else`. Fix: F is the else. |
| 10–30 | `if (score = 0)` | Plant on purpose. Fix `===`. Write `=` vs `===` again. |
| 30–45 | `NaN === NaN` | Show false. “Flashlight, not a design tool.” |
| 45–60 | They type the guessing-game kernel | Circulate. Do not sit. |

Point them at `Programming/code/03-grade.html` as the after-class check, not as the lecture.

---

## Lab

1. Guessing game (1–10).
2. Fizz for multiples of 3 (no buzz yet).

---

## Homework

1. Rock-paper-scissors vs computer random.
2. Written: == vs ===.

---

## Quiz next meeting (they hear this now)

1. Result of `0 == ''` (2)
2. Write if for age ≥ 18 (4)
3. Why === (4)


## Snippet

```js
if (x === 0) console.log('zero');
```

---

## Extra exercises

See [[Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Boolean expressions.** `===` and `!==`. `==` is forbidden in this course except to show a bug once. `NaN === NaN` is false — show it.

**2. Control flow.** if / else if / else. Early return as a style. Nested if more than two deep is a smell; use a function.

**3. Guarding graphics later.** `if (!gl)` is the WebGL black-screen cousin. Conditions are how programs refuse to crash.

---

## Common mistakes

1. Assignment in if.
2. else attached to the wrong if.

## If we run long, cut

Nested if examples. Keep `===` and the assignment bug.

## If we run short, add

`&&` short-circuit: `gl && gl.drawArrays`. Still no `==` in student code.
