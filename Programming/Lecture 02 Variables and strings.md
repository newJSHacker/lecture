# Lecture 2 — Variables and strings

**Week 2 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `const full = \`${first} ${last}\`;` plus `const x = 1; x = 2` → TypeError  
**Success check:** they can say, in one sentence, when they would use `let` instead of `const`.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS): `'3' + 1`, value vs variable, where to look.
- Demo: `Programming/code/02-strings.html`.
- Parked strip: `Lecture 2 | Goal: name a value without lying | Invariant: the name is not the thing`

## Board at the end (they photograph this)

```
let n = 3;     n is a box (can replace contents)
const n = 3;   n is a label stuck on 3 (cannot rebind)

const full = `${first} ${last}`;

legal name:  fullName     not:  2nd    not:  full-name
```

## Slides today (cap: 2)

| # | What is on it | Why not the board |
| ---: | --- | --- |
| 1 | Screenshot of the TypeError when reassigning `const` | The red stack is a photo |
| 2 | — | — |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Collect. Do not mark in silence for 10 minutes — mark item 1 together: `'3' + 1`.

**Say:** “If you wrote `4`, you believed `+` always adds. That is Lecture 1. Today we name things so we can reuse them.”

**Do not:** skip the quiz to “cover more.”

### Minutes 10–12 — Frame

**Say:** “A variable is a **binding**: a name attached to a value. Today: `let` vs `const`, strings, and names humans can read.”

**Board:** `let n = 3;` and a box with `3` in it.

**They do:** write the question: *When do I rebind?*

### Minutes 12–35 — Build

**Say:** “`const` cannot be rebound. The box’s *label* is glued. If the value is an object, the fields can still change — we are not doing objects until Lecture 7. Do not say ‘const means immutable’ in this course.”

**Board:** `const n = 3;` then `n = 4;` with a red X.

**Ask:** “Will `const s = 'hi'; s = 'yo'` throw?” Wait. Yes.

**Say:** “`let` when the name must point at a new value: a counter, a loop index. Default to `const`. `var` is banned. An old blog is not a spec.”

**Board:** `var` with a strike-through.

**Strings.** Write `'Ada'` and `"Ada"` — both fine; pick one style and keep it. `` `Ada` `` for templates.

**Board:**

```
`${first} ${last}`
     ^ hole
```

**Say:** “`.length`, `.slice(0, 2)`, `.includes('a')`. `s[0]` is a character. UTF-16 is a footnote, not a lecture.”

**They do:** on paper, write a template that logs `Ada is 36`. Circulate.

**Do not:** teach regex. Do not teach `var` hoisting diagrams.

### Minutes 35–50 — Show

Live: `fullName(first, last)` that **returns** a string, then `console.log`. Then:

```js
const x = 1;
x = 2;
```

**Slide:** 1 when the TypeError appears. Read the first stack line out loud.

**Ask:** “What failed — the value `1`, or the rebinding?” Want: rebinding.

**They do:** type the TypeError once so they are not afraid of it.

### Minutes 50–65 — Attempt

**Say:** “Write `initials(first, last)` that returns `'A.L.'` from `'Ada'`, `'Lovelace'`. Use `const`. Template or `+` — your choice. Then I will show the template.”

8 minutes. Then board:

```js
function initials(first, last) {
  return `${first[0]}.${last[0]}.`;
}
```

**Do not:** introduce `function` as a big theory. “A named recipe. Return sends a value out. Lecture 5 is functions properly. Today we need a name for a recipe.”

If they have not had `function` in Lecture 1, use only expressions in the attempt and save `function` for live coding. Safer attempt: three `const` lines building a bio string, no function.

**Safer attempt (use this if Lecture 1 had no functions):**

```js
const first = 'Ada';
const last = 'Lovelace';
const year = 1815;
const bio = `${first} ${last} (${year})`;
console.log(bio);
```

### Minutes 65–75 — Land

**Say:** “Photograph the boxes. Lab: length, slice, includes, and a bio line. Homework: `let` vs `const` in six sentences — I will mark ‘const means never changes’ as incomplete. Next quiz: the TypeError, a template, why not `var`.”

**Do not:** start Lecture 3 conditions.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | `fullName` with template | Plant: `fullName = first + last` missing space. Fix: template. |
| 15–30 | Rebind `const` | Leave the TypeError on screen 20 seconds. |
| 30–45 | `let` counter `n = n + 1` | Contrast with `const`. |
| 45–60 | Style: camelCase, no `full-name` | Plant an illegal identifier, read the error. |

---

## Lab

1. String kit: length, slice, includes.
2. A bio line from three variables.

## Homework

1. Eight tests for a pad/trim helper (they may write a clumsy version).
2. Written: `let` vs `const`, six sentences.

## Quiz (10 min, start of Lecture 3)

1. What fails: `const x = 1; x = 2`? (3)
2. Template literal of name+age (4)
3. Why not `var`? (3)

## Snippet

```js
const full = `${first} ${last}`;
```

## Extra exercises

See [[Programming/exercises/Week 02]].

## If we run long, cut

`includes`. Keep `const` vs `let` and the template.

## If we run short, add

`trim` and a joke about leading spaces in names.
