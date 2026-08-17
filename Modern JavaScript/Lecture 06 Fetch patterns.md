# Lecture 6 — Fetch patterns

**Week 6 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** JSON, abort, cache  
**Success check:** Headers.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/06-closure.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: JSON, abort, cache | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
AbortController name
Race.
Key skull.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** APIs. GET JSON.

**Ask:** Headers? Wait seven seconds. Take two answers.

**Board:** parked strip. Then AbortController name.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *JSON, abort, cache*.

**Do not:** Keys in source.

### Minutes 10–12 — Frame

**Say:** Today’s question: JSON, abort, cache. Kernel: JSON, abort, cache. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Keys in source.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** APIs. GET JSON.

**Say:** Abort. Cancel on new search.

**Say:** Secrets. No API keys in the repo.

**Ask:** Headers? Wait seven seconds. Take two answers.

**They do:** On paper: POST to a local mock extra.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Search-as-you-type fake: abort previous.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** POST to a local mock extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: POST to a local mock extra.; Handle 500.. Homework: Written: why keys not in git.; Code: abort.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: JSON, abort, cache | Plant the first common mistake. |
| 10–30 | Search-as-you-type fake: abort previous. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/06-closure.html` as the after-class check, not as the lecture.

---

## Lab

1. POST to a local mock extra.
2. Handle 500.

---

## Homework

1. Written: why keys not in git.
2. Code: abort.

---

## Quiz next meeting (they hear this now)

1. AbortController (4)
2. where keys live (3)
3. GET cache (3)


## Snippet

```js
const c = new AbortController();
fetch(url, { signal: c.signal });
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. APIs.** GET JSON. POST for later backends.

**2. Abort.** Cancel on new search.

**3. Secrets.** No API keys in the repo. AI course will repeat this.

---

## Common mistakes

1. Keys in source.
2. No abort, race of answers.

## If we run long, cut

Secrets

## If we run short, add

Handle 500.
