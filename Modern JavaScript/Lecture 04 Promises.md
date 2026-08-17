# Lecture 4 — Promises

**Week 4 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** then catch finally  
**Success check:** Create a Promise.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/03-promise.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: then catch finally | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
pending fulfilled rejected
State machine.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** States. Pending, fulfilled, rejected.

**Ask:** Create a Promise? Wait seven seconds. Take two answers.

**Board:** parked strip. Then pending fulfilled rejected.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *then catch finally*.

**Do not:** Then without catch.

### Minutes 10–12 — Frame

**Say:** Today’s question: then catch finally. Kernel: then catch finally. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: then without catch.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** States. Pending, fulfilled, rejected.

**Say:** Composition. then chains.

**Say:** Errors. Forgotten catch.

**Ask:** Create a Promise? Wait seven seconds. Take two answers.

**They do:** On paper: Promise.all of two fake loads.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Fake load with setTimeout wrapped in a Promise; then fetch data.json.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Promise.all of two fake loads.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Promise.all of two fake loads.; Error path UI.. Homework: Written: why promises vs callbacks.; Code: timeout promise.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: then catch finally | Plant the first common mistake. |
| 10–30 | Fake load with setTimeout wrapped in a Promise; then fetch data.json. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/03-promise.html` as the after-class check, not as the lecture.

---

## Lab

1. Promise.all of two fake loads.
2. Error path UI.

---

## Homework

1. Written: why promises vs callbacks.
2. Code: timeout promise.

---

## Quiz next meeting (they hear this now)

1. three states (3)
2. fetch return type (3)
3. unhandled rejection (4)


## Snippet

```js
new Promise((res) => setTimeout(res, 500));
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. States.** Pending, fulfilled, rejected.

**2. Composition.** then chains. all vs allSettled names.

**3. Errors.** Forgotten catch. async week next.

---

## Common mistakes

1. then without catch.
2. new Promise for already-sync code everywhere.

## If we run long, cut

Errors

## If we run short, add

Error path UI.
