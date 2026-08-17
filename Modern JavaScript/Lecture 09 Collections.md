# Lecture 9 — Collections

**Week 9 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Map Set  
**Success check:** Map vs object.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/05-mapset.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: Map Set | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
Map vs object keys
Table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Map. Any key.

**Ask:** Map vs object? Wait seven seconds. Take two answers.

**Board:** parked strip. Then Map vs object keys.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Map Set*.

**Do not:** __proto__ as a key on {}.

### Minutes 10–12 — Frame

**Say:** Today’s question: Map Set. Kernel: Map Set. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: __proto__ as a key on {}.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Map. Any key.

**Say:** Set. Unique vertices before hull — CG geometry.

**Say:** WeakMap. Name for caches; GC.

**Ask:** Map vs object? Wait seven seconds. Take two answers.

**They do:** On paper: Anagram check via maps extra.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Histogram with Map; unique with Set.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Anagram check via maps extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Anagram check via maps extra.; Object-key bug demo.. Homework: Written: when Map.; Code: unique points.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Map Set | Plant the first common mistake. |
| 10–30 | Histogram with Map; unique with Set. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Modern JavaScript/code/05-mapset.html` as the after-class check, not as the lecture.

---

## Lab

1. Anagram check via maps extra.
2. Object-key bug demo.

---

## Homework

1. Written: when Map.
2. Code: unique points.

---

## Quiz next meeting (they hear this now)

1. Map vs object (4)
2. Set has (3)
3. weak name (3)


## Snippet

```js
const m = new Map(); m.set(p, 1);
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Map.** Any key. Insertion order.

**2. Set.** Unique vertices before hull — CG geometry.

**3. WeakMap.** Name for caches; GC.

---

## Common mistakes

1. __proto__ as a key on {}.

## If we run long, cut

WeakMap

## If we run short, add

Object-key bug demo.
