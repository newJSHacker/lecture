# Lecture 13 — Objects as programs

**Week 13 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `class Point { dist(q){…} }` or record + `dist(p,q)` — student choice, with tests  
**Success check:** they can say what `this` is in one sentence and they did not build an inheritance tree

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Programming/code/11-point.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: a method that uses the object | Invariant: `this` is the receiver; losing it in a callback is a later course; inheritance is skipped`

## Board at the end (they photograph this)

```
p.dist(q)     this is p

class Point {
  constructor(x,y){ this.x=x; this.y=y; }
  dist(q){ return Math.hypot(this.x-q.x, this.y-q.y); }
}

has-a  (sprite has a point)    not  is-a  trees
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: `this` undefined in a detached callback | the TypeError is a photo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** A method is a function stored on an object. `this` is the receiver. Inheritance is skipped — composition: a sprite **has** a point.

**Ask:** In `p.dist(q)`, what is `this`? Wait. Want: `p`.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`class Point { dist(q){…} }` or record + `dist(p,q)` — student choice, with tests*.

**Do not:** Deep inheritance for a homework.

### Minutes 10–12 — Frame

**Say:** `class` is optional sugar. Records plus functions are enough for IGWT math kernels. Demo `this` lost in a callback once; do not spend the hour on it.

**Ask:** Why skip inheritance this term?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** `counter.inc()` mutates. Prefer `add` that returns a **new** vector for the lab.

**Board:** has-a vs is-a. Point method box.

**Say:** BankAccount deposit/withdraw as the live-coding story; then Point.dist.

**Ask:** Write dist of two points in one line with hypot.

**They do:** On paper: a Vector add that returns new, does not mutate.

**Do not:** Mix Python syntax into a JS term. Skip the attempt.

### Minutes 35–50 — Show

**Say:** BankAccount, then Point. Plant an unbound `this`. Name it. Fix or avoid.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Vector object with add (returns new). No inheritance. Tests.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: `this` in one paragraph; Point class **or** record+functions, tests. Quiz: what is this, why no inheritance, dist. Next week is studio — freeze scope.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | BankAccount | Negative withdraw policy. |
| 15–40 | Point.dist | Plant this unbound. |
| 40–50 | Has-a sprite | No extends. |
| 50–60 | They write Vector.add | Circulate. |

Point them at `Programming/code/11-point.html` as the after-class check, not as the lecture.

---

## Lab

1. Vector object with add (returns new).
2. Do not use inheritance.

---

## Homework

1. Written: this in one paragraph.
2. Code: Point class or record+functions, your choice, tests.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
class Point {
  constructor(x,y){ this.x=x; this.y=y; }
  dist(q){ return Math.hypot(this.x-q.x, this.y-q.y); }
}
```

---

## Extra exercises

See [[Programming/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Deep inheritance for a homework.
2. this unbound.

## If we run long, cut

Getters. Keep this + no inheritance.

## If we run short, add

`#private` name only.
