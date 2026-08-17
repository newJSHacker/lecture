# Lecture 5 — async/await

**Week 5 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** async function; await; try/catch; sequential await vs Promise.all  
**Success check:** they rewrite a then-chain as await and can say when two fetches should run in parallel

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/04-async.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: readable async without a then pyramid | Invariant: await pauses that async function, not the whole page; independent work uses all`

## Board at the end (they photograph this)

```
async function go() {
  const res = await fetch('data.json');
  if (!res.ok) throw new Error(res.status);
  return res.json();
}

sequential:  await a; await b;
parallel:    const [a,b] = await Promise.all([fa, fb]);
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** await is then with a stack you can read. The bug is await in a map without all — you thought you parallelized and you did not. We measure order, we do not invent milliseconds.

**Ask:** What does an async function return if you never await it? Wait. Want: a Promise, already started.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *try/catch, sequential vs parallel*.

**Do not:** Await in map without all.

### Minutes 10–12 — Frame

**Say:** try/catch around await. Empty catch is a bug. for-await named only. Two independent JSON files: all, not await a then await b unless order is required.

**Ask:** await inside a non-async function — legal? Want: no (unless the function is async).

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Sugar. The Promise is still there. Errors become throw.

**Board:** two timelines — sequential vs all. Same two fetches.

**Say:** Serve the folder. fetch from file:// throws or CORS-fails — catch must say serve.

**Ask:** Why is await Promise.all(urls.map(fetch)) different from urls.map(async u => await fetch(u))?

**They do:** On paper: sequential vs parallel timing sketch. No fake fps — just order of start/finish.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Load two JSON files in parallel; render. Plant await a then await b first. Switch to all. Demo Modern JavaScript/code/04-async.html. Plant file:// and read ‘serve folder’.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Rewrite last week’s then-chain as await. Then time sequential vs all with performance.now() — report which started together, not a made-up speedup.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: sequential vs parallel (measure); try/catch around fetch. Homework: when not to parallelize; Promise.all code. Quiz: async return, await-in-loop smell, try/catch.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | then → await rewrite | Plant forgotten async keyword. |
| 10–30 | two fetches sequential | They see the wait. |
| 30–45 | Promise.all | Plant map(async) without all. |
| 45–60 | They add try/catch + serve note | Circulate. |

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

None this meeting.


## Snippet

```js
const [a,b] = await Promise.all([fetch(u1), fetch(u2)]);
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. await in map without all.
2. empty catch.

## If we run long, cut

for-await. Keep await + all vs sequential.

## If we run short, add

try/catch around fetch that prints res.status when !ok.
