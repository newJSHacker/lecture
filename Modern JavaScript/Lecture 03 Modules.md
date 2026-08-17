# Lecture 3 — Modules

**Week 3 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** export import  
**Success check:** export function.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: export import | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
files as API
Arrows between files.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Named exports. Course policy: named exports for kernels.

**Ask:** export function? Wait seven seconds. Take two answers.

**Board:** parked strip. Then files as API.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *export import*.

**Do not:** Mixing remote script URLs with local modules until it 'works'.

### Minutes 10–12 — Frame

**Say:** Today’s question: export import. Kernel: export import. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Mixing remote script URLs with local modules until it 'works'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Named exports. Course policy: named exports for kernels.

**Say:** Browsers. file:// often fails.

**Say:** Bundlers preview. Vite next week.

**Ask:** export function? Wait seven seconds. Take two answers.

**They do:** On paper: Three modules.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Split lerp into math.js; import in main.js.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three modules.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Three modules.; README serve.. Homework: Written: ESM vs classic script.; Code: import.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: export import | Plant the first common mistake. |
| 10–30 | Split lerp into math.js; import in main.js. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/08-modules.html` as the after-class check, not as the lecture.

---

## Lab

1. Three modules.
2. README serve.

---

## Homework

1. Written: ESM vs classic script.
2. Code: import.

---

## Quiz next meeting (they hear this now)

1. export syntax (4)
2. why serve (3)
3. named vs default (3)


## Snippet

```js
import { lerp } from './math.js';
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Named exports.** Course policy: named exports for kernels. Default optional.

**2. Browsers.** file:// often fails. npx serve.

**3. Bundlers preview.** Vite next week.

---

## Common mistakes

1. Mixing remote script URLs with local modules until it 'works'.

## If we run long, cut

Bundlers preview

## If we run short, add

README serve.
