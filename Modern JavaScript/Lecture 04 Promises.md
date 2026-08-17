# Lecture 4 — Promises

**Week 4 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Promise states; then / catch / finally; Promise.all of two loads  
**Success check:** they construct a timeout Promise and attach catch; they can name the three states

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/03-promise.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: one async value with an error path | Invariant: a Promise is pending, fulfilled, or rejected — once; then without catch loses the failure`

## Board at the end (they photograph this)

```
pending  →  fulfilled(value)
         →  rejected(error)

p.then(onOk).catch(onErr).finally(cleanup)

Promise.all([a, b])     allSettled  (name)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Fetch returns a Promise. A texture load is a Promise. If they only then(), the rejection is an unhandled scream later. Today: the state machine.

**Ask:** Does then() run if the Promise already fulfilled? Wait. Want: yes — it still schedules.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *then catch finally*.

**Do not:** Then without catch.

### Minutes 10–12 — Frame

**Say:** new Promise((resolve, reject) => …). Do not wrap already-sync math in a Promise. all waits for every success; one reject fails the all. allSettled named for later.

**Ask:** What is the return type of fetch('data.json') before you call json()?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three states. You cannot un-fulfill. finally runs either way — good for a spinner name.

**Board:** then chain. Circle catch. Forgotten catch = unhandled rejection.

**Say:** Fake load: setTimeout inside new Promise. Then Promise.all of two fakes.

**Ask:** all vs allSettled in one sentence?

**They do:** On paper: Promise.all of two fake loads; what prints if the second rejects.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Fake load with setTimeout wrapped in a Promise; then fetch data.json under a local server. Demo Modern JavaScript/code/03-promise.html. Plant then without catch on a reject.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Promise.all of two timeout Promises. Eight minutes. Then add one catch that writes a visible error.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: Promise.all + error-path UI. Homework: why promises vs callbacks; timeout promise. Quiz: three states, fetch return type, unhandled rejection.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | pending → fulfill | Plant resolve twice — second is ignored. |
| 10–30 | timeout Promise + then/catch | Plant missing catch. |
| 30–45 | fetch data.json | Plant file://. Serve. 04-async.html is next week’s await. |
| 45–60 | They all() two fakes | Circulate. |

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

None this meeting.


## Snippet

```js
new Promise((res) => setTimeout(res, 500));
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. then without catch.
2. new Promise for already-sync code everywhere.

## If we run long, cut

allSettled details. Keep states + catch.

## If we run short, add

Error path UI: a <pre> that shows the rejection message.
