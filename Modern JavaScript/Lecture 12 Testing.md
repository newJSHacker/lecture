# Lecture 12 — Testing

**Week 12 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** assert, tiny runner  
**Success check:** console.assert.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: assert, tiny runner | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
PASS / FAIL list
PASS list.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Culture. CG kernel tests and geometry fixtures.

**Ask:** console.assert? Wait seven seconds. Take two answers.

**Board:** parked strip. Then PASS / FAIL list.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *assert, tiny runner*.

**Do not:** Tests that only log 'ok'.

### Minutes 10–12 — Frame

**Say:** Today’s question: assert, tiny runner. Kernel: assert, tiny runner. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Tests that only log 'ok'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Culture. CG kernel tests and geometry fixtures.

**Say:** Runner. A page that prints PASS/FAIL.

**Say:** CI. GitHub Actions named; not required this term.

**Ask:** console.assert? Wait seven seconds. Take two answers.

**They do:** On paper: 5 more fixtures.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Port lerp/clamp tests to a test.html.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** 5 more fixtures.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: 5 more fixtures.; A deliberately failing test then fix.. Homework: Written: why hidden fixtures.; Code: test page.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: assert, tiny runner | Plant the first common mistake. |
| 10–30 | Port lerp/clamp tests to a test.html. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/08-modules.html` as the after-class check, not as the lecture.

---

## Lab

1. 5 more fixtures.
2. A deliberately failing test then fix.

---

## Homework

1. Written: why hidden fixtures.
2. Code: test page.

---

## Quiz next meeting (they hear this now)

1. AAA (3)
2. assert (3)
3. deleting tests (4)


## Snippet

```js
function assert(n,c){ if(!c) throw new Error(n); }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Culture.** CG kernel tests and geometry fixtures. Same habit.

**2. Runner.** A page that prints PASS/FAIL. No Jest required.

**3. CI.** GitHub Actions named; not required this term.

---

## Common mistakes

1. Tests that only log 'ok'.
2. Deleting FAIL cases.

## If we run long, cut

CI

## If we run short, add

A deliberately failing test then fix.
