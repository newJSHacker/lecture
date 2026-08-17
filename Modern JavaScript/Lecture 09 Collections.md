# Lecture 9 — Collections

**Week 9 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Map for arbitrary keys; Set for uniqueness; object keys are strings  
**Success check:** they histogram with Map and unique an array with Set; they can say why {} as a dict is a trap

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/05-mapset.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: the right collection, not everything in {} | Invariant: object keys stringify; Map keeps the key you gave it`

## Board at the end (they photograph this)

```
{}     keys → strings (and symbols)
Map    any key, insertion order     m.set(p, 1); m.get(p)
Set    unique                       s.has(x)

__proto__ as a key on {}  =  fail
WeakMap  name: GC cache
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** A vertex dict keyed by point objects will break if you use {}. Computational Geometry unique-before-hull is a Set. Today: Map and Set as the default collections.

**Ask:** Is m.get(p) the same as m.get(otherPointWithSameXY) for two objects? Wait. Want: no — identity, unless you key on a string.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Map Set*.

**Do not:** __proto__ as a key on {}.

### Minutes 10–12 — Frame

**Say:** Map: any key, .set .get .has .delete. Set: unique values. WeakMap named for caches that should not keep objects alive. We do not implement a hashmap.

**Ask:** When is {} still OK? Want: a record with known string fields, not a dictionary of arbitrary keys.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Histogram: Map from word to count. Object-key bug: __proto__ or toString as a key.

**Board:** Map vs object keys table. Set of numbers [1,1,2] → size 2.

**Say:** Unique vertices: Set, or Map if you need a payload. WeakMap name only.

**Ask:** Set.has vs array.includes — why Set for a large unique list (teaching-level)?

**They do:** On paper: anagram check — two Maps of character counts, or one Map and decrement.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Histogram with Map; unique with Set. Demo Modern JavaScript/code/05-mapset.html. Plant {}['__proto__'] as a key. Then Map.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Anagram check via maps. Eight minutes. Then unique points with a string key `${x},${y}` if object identity is wrong.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: anagram + object-key bug demo. Homework: when Map; unique points. Quiz: Map vs object, Set.has, WeakMap name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Set unique | Plant [1,1,2] with {} flags. |
| 10–30 | Map histogram | Plant object key stringify of a point. |
| 30–45 | __proto__ on {} | They see the trap. Switch to Map. |
| 45–60 | They write anagram Maps | Circulate. |

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

None this meeting.


## Snippet

```js
const m = new Map(); m.set(p, 1);
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. __proto__ as a key on {}.

## If we run long, cut

WeakMap. Keep Map vs {} + Set.

## If we run short, add

Object-key bug demo as a two-minute live.
