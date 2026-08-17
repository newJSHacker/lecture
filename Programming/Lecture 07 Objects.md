# Lecture 7 — Objects

**Week 7 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `const p = { x, y }` and centroid of an array of points  
**Success check:** they read `p.y` and can stringify a point without functions inside

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Programming/code/07-centroid.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: name the parts of a thing | Invariant: an object is named fields; an array is ordered slots — do not use objects as lists`

## Board at the end (they photograph this)

```
p = { x: 1, y: 2 }      p.x      p['x']

centroid = average of {x,y} points

JSON:  '{"x":1,"y":2}'   no functions, no NaN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: JSON of a point in DevTools | the quotes are easier to photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** A mesh vertex is `{x,y,z}`. A student is `{name, scores: []}`. Today we make records. Midterm next week on values through objects.

**Ask:** How do you read y of `{x:1, y:2}`? Wait. Want: `p.y`.

**Board:** parked strip. Then dot vs bracket.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *records, nested data*.

**Do not:** `p[x]` without quotes.

### Minutes 10–12 — Frame

**Say:** Dot when you know the key. Brackets when the key is in a variable. `p[x]` without quotes looks up a variable named x — usually a bug.

**Ask:** When would you use `p[key]` instead of `p.x`?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Nesting: `{ name, scores: [] }`. This is the address book.

**Board:** point record. Arrow from `p` to a box with x and y.

**Say:** `JSON.stringify` / `parse`. JSON cannot store functions or NaN. Clipboard paste is enough; file I/O waits.

**Ask:** Is `[0,1,2]` or `{0:0,1:1,2:2}` the list? Want: the array.

**They do:** On paper: write a point and a student with three scores.

**Do not:** mix Python syntax into a JS term. Do not skip the attempt.

### Minutes 35–50 — Show

**Say:** Array of `{x,y}`; compute centroid. Assert it. Plant `p[x]` without quotes.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three-person address book as objects in an array. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: address book; comment on shallow vs deep copy. Homework: parse JSON of points, sum x. Quiz next meeting is the midterm topic list — objects included. Midterm is Lecture 8, on paper.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Literal `{x,y}` | Plant `p[x]`. |
| 10–30 | Centroid | Empty array: decide a policy, do not crash. |
| 30–45 | stringify / parse | Show functions disappear. |
| 45–60 | They build the address book | Circulate. |

Point them at `Programming/code/07-centroid.html` as the after-class check, not as the lecture.

---

## Lab

1. Address book of 3 people.
2. Deep vs shallow copy discussion in comments.

---

## Homework

1. Parse a JSON string of points, sum x.
2. Written: when to use array vs object.

---

## Quiz next meeting (they hear this now)

1. Access y of {x:1,y:2} (2)
2. JSON of a point (4)
3. Why not object as list (4)


## Snippet

```js
const p = { x: 1, y: 2 };
```

---

## Extra exercises

See [[Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Records.** A point is `{x, y}`. A student is `{name, scores: []}`. This is the mesh vertex of Semester 2.

**2. Dot and bracket.** `p.x` vs `p['x']`. Brackets when the key is in a variable.

**3. JSON.** Show stringify of a point. Mention that JSON cannot store functions or NaN. File I/O waits; clipboard paste is enough.

---

## Common mistakes

1. `p[x]` without quotes.
2. Circular JSON.

## If we run long, cut

Deep clone algorithms. Keep literal + centroid.

## If we run short, add

Optional chaining `p?.x` name only.
