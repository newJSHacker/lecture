# Lecture 10 — Closures and this

**Week 10 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** closure = function + environment; factory; this lost on a callback  
**Success check:** they write makeCounter and fix a button handler that lost this — arrow or bind

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/06-closure.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: private state without a global | Invariant: a closure remembers bindings, not a photocopy of values at call time unless you wrap them`

## Board at the end (they photograph this)

```
function makeCounter() {
  let n = 0;
  return () => ++n;     // closes over n
}

this  in a method = the receiver
lost on callback →  arrow  or  .bind(this)
not window
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Module state is a closure. A GL context held in a closure is common and easy to leak — we name that, we do not open WebGL. Today: factory and this.

**Ask:** After const inc = makeCounter(); inc(); inc(); what does the third inc() return? Wait. Want: 3.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *factory, bind*.

**Do not:** Closures as magic.

### Minutes 10–12 — Frame

**Say:** Function plus the environment it was created in. Closures are not magic. this is the receiver of a method; passing obj.method as a listener loses it. Arrow lexical this, or bind. No this = window hacks.

**Ask:** Does an arrow inside makeCounter close over n? Want: yes.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Environment box on the board: n lives after makeCounter returns.

**Board:** makeCounter. Then a class-or-object method handed to addEventListener.

**Say:** Graphics: closing over a heavy context — mention leak. Week 13 will put state in one object instead of a pile of closures.

**Ask:** bind vs arrow — name one difference (teaching-level).

**They do:** On paper: once(fn) — extra factory that runs fn at most once.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** makeCounter(); then a button this bug and fix. Demo Modern JavaScript/code/06-closure.html. Plant this as window. Fix with arrow or bind.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** once(fn) extra. Tests for counter: 1,2,3. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: once + counter tests. Homework: closure vs global; fix this. Quiz: what a closure keeps, this in arrow, bind.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | makeCounter | Plant a global n. Then hide n in the factory. |
| 10–30 | button this bug | Plant obj.method as listener. Read undefined. |
| 30–45 | arrow or bind | They pick one and freeze it. |
| 45–60 | They write once(fn) | Circulate. |

Point them at `Modern JavaScript/code/06-closure.html` as the after-class check, not as the lecture.

---

## Lab

1. Once function extra.
2. Tests for counter.

---

## Homework

1. Written: closure vs global.
2. Code: fix this.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
function makeCounter(){ let n=0; return () => ++n; }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Closures as magic.
2. this hacked with window.

## If we run long, cut

GL leak mention. Keep factory + this fix.

## If we run short, add

Tests for counter: three asserts.
