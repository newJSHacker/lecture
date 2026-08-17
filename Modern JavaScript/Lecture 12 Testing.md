# Lecture 12 — Testing

**Week 12 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** assert that throws; a page or node script that prints PASS/FAIL; fixtures  
**Success check:** they have a failing test they then fix; tests that only log 'ok' are rejected

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: the kernel has a red/green list | Invariant: a test that cannot fail is not a test; hidden fixtures do not count`

## Board at the end (they photograph this)

```
function assert(name, cond) {
  if (!cond) throw new Error(name);
}

PASS  lerp 0
FAIL  clamp high     ← keep this case; do not delete

AAA: arrange, act, assert   (name)
No Jest required
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** CG kernels and geometry predicates live or die on fixtures. If it is not a module with a test, it is not a kernel. Today: a tiny runner, not a framework.

**Ask:** If every test logs 'ok' and never throws, how do you know lerp is wrong? Wait. Want: you don’t.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *assert, tiny runner*.

**Do not:** Tests that only log 'ok'.

### Minutes 10–12 — Frame

**Say:** console.assert is allowed; a throw-on-fail runner is clearer on a page. CI / GitHub Actions named, not required this term. Do not delete FAIL cases to go green.

**Ask:** What is a fixture here? Want: a known input/output pair.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Culture: same habit as Computational Geometry. Name the case.

**Board:** PASS/FAIL list. assert helper. Deliberate fail then fix.

**Say:** Port lerp/clamp tests to test.html or node test.js from week 7. Serve if it is a module page.

**Ask:** Why keep a test that failed this morning?

**They do:** On paper: five fixtures for clamp (low, high, inside, equal bounds, NaN policy — pick one and freeze).

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Port lerp/clamp tests to a test.html. Plant a test that only console.log('ok'). Then throw. 08-modules.html is the serve reminder — the test page is new today.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Five more fixtures. A deliberately failing test then fix. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: five fixtures + fail-then-fix. Homework: why hidden fixtures; test page. Quiz: AAA name, assert, deleting tests.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | assert helper | Plant log-'ok' tests. |
| 10–30 | test.html lerp/clamp | Serve if type=module. |
| 30–45 | Deliberate FAIL then fix | Do not delete the case. |
| 45–60 | They add five fixtures | Circulate. |

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

None this meeting.


## Snippet

```js
function assert(n,c){ if(!c) throw new Error(n); }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Tests that only log 'ok'.
2. Deleting FAIL cases.

## If we run long, cut

CI. Keep runner + one red test.

## If we run short, add

A deliberately failing test then fix, photographed.
