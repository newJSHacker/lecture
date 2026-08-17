# Lecture 2 — Destructuring and spread

**Week 2 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** pattern match lite  
**Success check:** Destructure objects/arrays.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/02-spread.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: pattern match lite | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
{x,y} = p
Patterns.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Destructure. const {x,y}=p.

**Ask:** Destructure objects/arrays? Wait seven seconds. Take two answers.

**Board:** parked strip. Then {x,y} = p.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pattern match lite*.

**Do not:** Thinking spread deep-copies nested meshes.

### Minutes 10–12 — Frame

**Say:** Today’s question: pattern match lite. Kernel: pattern match lite. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Thinking spread deep-copies nested meshes.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Destructure. const {x,y}=p.

**Say:** Spread. [...a, x].

**Say:** Rest. (...args).

**Ask:** Destructure objects/arrays? Wait seven seconds. Take two answers.

**They do:** On paper: Merge two option objects.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Swap via destucture; clone an array; clone a point.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Merge two option objects.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Merge two option objects.; Deep copy discussion.. Homework: Written: shallow vs deep.; Code: 8 tests.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: pattern match lite | Plant the first common mistake. |
| 10–30 | Swap via destucture; clone an array; clone a point. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/02-spread.html` as the after-class check, not as the lecture.

---

## Lab

1. Merge two option objects.
2. Deep copy discussion.

---

## Homework

1. Written: shallow vs deep.
2. Code: 8 tests.

---

## Quiz next meeting (they hear this now)

1. clone array (3)
2. rename destucture (3)
3. shallow pitfall (4)


## Snippet

```js
const { x, y } = p;
const q = { ...p, y: 0 };
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Destructure.** const {x,y}=p. Parameters too.

**2. Spread.** [...a, x]. Object spread shallow.

**3. Rest.** (...args).

---

## Common mistakes

1. Thinking spread deep-copies nested meshes.

## If we run long, cut

Rest

## If we run short, add

Deep copy discussion.
