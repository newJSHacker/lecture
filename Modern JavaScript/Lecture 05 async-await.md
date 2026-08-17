# Lecture 5 — async/await

**Week 5 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** try/catch, sequential vs parallel  
**Success check:** Rewrite then as await.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/04-async.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: try/catch, sequential vs parallel | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
await inside async
Timeline.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Sugar. await is then with nicer stack traces.

**Ask:** Rewrite then as await? Wait seven seconds. Take two answers.

**Board:** parked strip. Then await inside async.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *try/catch, sequential vs parallel*.

**Do not:** Await in map without all.

### Minutes 10–12 — Frame

**Say:** Today’s question: try/catch, sequential vs parallel. Kernel: try/catch, sequential vs parallel. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: await in map without all.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Sugar. await is then with nicer stack traces.

**Say:** Parallel. Two independent fetches: all, not await a then await b unless order required.

**Say:** for-await. Name only.

**Ask:** Rewrite then as await? Wait seven seconds. Take two answers.

**They do:** On paper: Sequential vs parallel timing (measure).

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Load two JSON files in parallel; render.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Sequential vs parallel timing (measure).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Sequential vs parallel timing (measure).; try/catch around fetch.. Homework: Written: when not to parallelize.; Code: all.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: try/catch, sequential vs parallel | Plant the first common mistake. |
| 10–30 | Load two JSON files in parallel; render. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/04-async.html` as the after-class check, not as the lecture.

---

## Lab

1. Sequential vs parallel timing (measure).
2. try/catch around fetch.

---

## Homework

1. Written: when not to parallelize.
2. Code: all.

---

## Quiz next meeting (they hear this now)

1. async function return (3)
2. await in loop smell (4)
3. try/catch (3)


## Snippet

```js
const [a,b] = await Promise.all([fetch(u1), fetch(u2)]);
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Sugar.** await is then with nicer stack traces.

**2. Parallel.** Two independent fetches: all, not await a then await b unless order required.

**3. for-await.** Name only.

---

## Common mistakes

1. await in map without all.
2. empty catch.

## If we run long, cut

for-await

## If we run short, add

try/catch around fetch.
