# Lecture 10 — Closures and this

**Week 10 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** factory, bind  
**Success check:** Write a closure counter.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/06-closure.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: factory, bind | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
inner function remembering n
Environment box.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Closure. Function + environment.

**Ask:** a closure counter? Wait seven seconds. Take two answers.

**Board:** parked strip. Then inner function remembering n.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *factory, bind*.

**Do not:** Closures as magic.

### Minutes 10–12 — Frame

**Say:** Today’s question: factory, bind. Kernel: factory, bind. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Closures as magic.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Closure. Function + environment.

**Say:** this. Methods.

**Say:** Graphics. A closure over a GL context is common and easy to leak — mention.

**Ask:** a closure counter? Wait seven seconds. Take two answers.

**They do:** On paper: Once function extra.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: makeCounter(); then a button this bug and fix.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Once function extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Once function extra.; Tests for counter.. Homework: Written: closure vs global.; Code: fix this.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: factory, bind | Plant the first common mistake. |
| 10–30 | makeCounter(); then a button this bug and fix. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. what a closure keeps (4)
2. this in arrow (3)
3. bind (3)


## Snippet

```js
function makeCounter(){ let n=0; return () => ++n; }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Closure.** Function + environment. Private counters. Module state.

**2. this.** Methods. Losing this on callback — arrow or bind.

**3. Graphics.** A closure over a GL context is common and easy to leak — mention.

---

## Common mistakes

1. Closures as magic.
2. this hacked with window.

## If we run long, cut

Graphics

## If we run short, add

Tests for counter.
