# Lecture 1 — What a program is

**Week 1 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `console.log` of a value; `'3' + 1` vs `Number('3') + 1`  
**Success check:** every student has DevTools open and has logged one line you can see from the aisle.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Browser + editor. No CDN. No slides required; 3 slides max if you use them.
- Demo: `Programming/code/01-types.html` (or a blank page + console).
- Backup: write the same three logs on the board if the projector dies.
- Parked strip: `Lecture 1 | Goal: see a value | Invariant: a computer only follows instructions`

## Board at the end (they photograph this)

```
input  →  process  →  output

value ≠ variable
  3     vs   let n = 3

'3' + 1  →  '31'     Number('3') + 1  →  4
```

Plus the 15-week map as five boxes: values, control, data, search, project.

## Slides today (cap: 3)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of DevTools with Console circled | Photograph; do not draw Chrome’s UI |
| 2 | Optional: the 15-week map typed cleanly | Only if your board handwriting is a problem |
| 3 | — | — |

No slide of “What is programming?” That is mouth + board.

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** “A computer has no idea what you meant. It only follows instructions. Today we will make it show us a value. If you cannot see a value, you cannot later see a pixel.”

**Ask:** “If the page is white and you think your program ran, where do you look first?” Wait seven seconds. Take two answers. Then: “The console. Not the desktop. Not me.”

**Board:** empty except the parked strip. Then write `input → process → output`.

**Slide:** 1 (DevTools), 20 seconds, then back to the board.

**They do:** open a browser. Do not code yet.

**Do not:** start with a history of Ada Lovelace. Do not open VS Code settings for ten minutes.

### Minutes 8–12 — Frame

**Say:** “This program (IGWT) uses **JavaScript** so Canvas, WebGL, and Three.js are the same language later. If this department already standardized on Python, we teach the same lectures in Python — we do not mix required labs.”

**Ask:** “What is the output of a graphics program, in one word?” Want: pixels (or image). Write it under `output`.

**Board:** under process, write `instructions`. Under output, write `console (this term) → pixels (later)`.

**Slide:** none.

**They do:** write today’s question in their notes: *How do I see a value?*

**Do not:** install Node unless the lab machines already have it. Browser console is enough.

### Minutes 12–35 — Build

**Say:** “A **value** is the thing. A **variable** is a name stuck to a thing. `3` is a value. `n` is a name.”

**Board:** two boxes. Left: `3` labeled value. Right: `n` with an arrow to `3` labeled variable.

**Say:** “Types today: number, string, boolean. `typeof` is a flashlight, not a design tool. Strings have quotes. `+` on numbers adds. `+` on strings glues. That collision will follow you to WebGL uniforms if you are sloppy.”

**Board:** table

| Expression | Result |
| --- | --- |
| `3 + 1` | `4` |
| `'3' + 1` | `'31'` |
| `Number('3') + 1` | `4` |
| `typeof 3` | `'number'` |
| `typeof '3'` | `'string'` |

Work the middle row slowly. Point at the quotes.

**Ask:** “Predict `'5' + 2`.” Hands. Then reveal. Then: “How do we force a number?” `Number(...)`.

**They do:** on paper, predict `'2' + 2` and `'2' - 2`. Collect two papers from the front row. `-` forces a number; `+` does not. That surprise is the lecture.

**Do not:** teach `==` vs `===` today except “we will use `===` from Lecture 3.” Do not teach `var`.

### Minutes 35–50 — Show

**Say:** “I am going to talk to the console. Watch my hands. A black page with a correct log is a passing step.”

**Slide:** none. Live browser. Zoom 140%.

Type, narrating:

```js
console.log('IGWT');
console.log(typeof 3, typeof '3');
console.log('3' + 1, Number('3') + 1);
```

**Ask:** “What would we see if I forgot the quotes on IGWT?” Wait. Then do it. Read the error **out loud**.

**They do:** the same three lines in their console. You walk the aisle. Success check: you see logs.

**Do not:** type a 40-line starter. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** “Celsius to Fahrenheit is three lines. Formula: `f = c * 9/5 + 32`. Use a name for `c`. Log `f`.”

**They do:** alone or pairs, 8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct version:

```js
const c = 20;
const f = c * 9 / 5 + 32;
console.log(f);
```

**Ask:** “Why `const` here?” Want: we are not rebinding `c`. “We will do `let` vs `const` properly in Lecture 2. Today: prefer `const` until you must rebind.”

**Do not:** live-code the formula for them before they try.

### Minutes 65–75 — Land

**Say:** “Photograph the board. The invariant is: you cannot debug what you cannot see. Lab: name, year, °C→°F, and one broken `+` with a comment. Homework: three predictions. Quiz next time on `'3' + 1`.”

**Board:** add `See the value. Then change it.`

**Slide:** 2 only if you did not draw the 15-week map. Five boxes: values · control · data · search · project.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Blank HTML, one script, `console.log('IGWT')` | Plant: script in `head` before you mention order. Fix: script at end of `body` or they open the console after reload. |
| 10–25 | Temperature, `const` | Plant: `'20' * 9/5` actually works (coercion). Say: “Do not rely on this. `Number`.” |
| 25–40 | `'5' + 2` | Plant on purpose. Fix with `Number`. Write the two-row table again. |
| 40–50 | `typeof`, `NaN === NaN` is false | Show once. “Flashlight.” |
| 50–60 | They type the lab’s broken `+` with a comment | You circulate. Do not sit. |

Point them at `Programming/code/01-types.html` as the after-class check, not as the lecture.

---

## Lab

1. A script that logs name and year.
2. Convert °C to °F.
3. One broken `+` example explained in a comment.

Done when a TA sees three log lines without opening the student’s editor.

---

## Homework

1. Three logged expressions: predicted vs actual.
2. Half page: why this program starts in JavaScript.

---

## Quiz next meeting (they hear this now)

1. What does `'3' + 1` yield? (2)
2. Value vs variable (3)
3. Where do you look when nothing appears on the page? (5)

## Snippet

```js
console.log(typeof 3, typeof '3', '3' + 1, Number('3') + 1);
```

## Extra exercises

See [[Programming/exercises/Week 01]].

---

## Common mistakes (yours, not only theirs)

- Teaching from slides with no log.
- Python syntax (`print`, `True`) in a JS term.
- Calling the course plan “the lecture.”

## If we run long, cut

The 15-week map (send the course plan PDF). Keep `'3' + 1`.

## If we run short, add

`true`, `false`, and `typeof`. Still no `==`.
