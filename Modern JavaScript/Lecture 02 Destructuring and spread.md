# Lecture 2 — Destructuring and spread

**Week 2 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** {x,y}=p and [...a, x]; object spread is shallow  
**Success check:** they merge two option objects with spread and can name one nested field that is still shared

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/02-spread.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: pattern-match a point without p.x soup | Invariant: spread copies one level; nested objects are aliases`

## Board at the end (they photograph this)

```
const { x, y } = p;
const q = { ...p, y: 0 };

[...a, x]          rest: (...args)

shallow:  nested mesh.geometry  still shared
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last time: one binding. Today: take a point apart. Graphics code is full of {x,y,z}. If they think spread deep-copies a mesh, they will mutate someone else’s geometry.

**Ask:** After const q = { ...p }; q.nested.k = 1 — does p.nested.k change? Wait. Want: yes, same object.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pattern match lite*.

**Do not:** Thinking spread deep-copies nested meshes.

### Minutes 10–12 — Frame

**Say:** Destructure in assignment and in parameters. Spread arrays and objects. Rest collects the leftover. Deep copy is structuredClone or a serializer — name only today.

**Ask:** Rename while destructuring: const { x: px } = p — what is px?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A pattern on the left matches a shape on the right. Missing fields are undefined unless you default.

**Board:** swap [a,b] = [b,a]. Clone array [...a]. Clone point { ...p }.

**Say:** Merge options: { ...defaults, ...user }. Last wins. Nested user.mesh is not cloned.

**Ask:** Rest vs spread — which is the left side of a signature?

**They do:** On paper: merge {color:'#111', size:2} with {size:4}. Write the result. Star the nested alias pitfall.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Swap via destructure; clone an array; clone a point; then mutate a nested field. Demo Modern JavaScript/code/02-spread.html. Read the shared nested key out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Merge two option objects. Eight minutes. Then write one sentence: what is still shared.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: merge + deep-copy discussion. Homework: shallow vs deep paragraph; eight tests. Quiz: clone array, rename destructure, shallow pitfall.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | {x,y}=p | Plant p.x still after rename — they forgot the new name. |
| 10–30 | Spread clone + nested mutate | Plant ‘it copied everything’. |
| 30–45 | Merge options | Last-wins demo. |
| 45–60 | They merge on paper then in the file | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. Thinking spread deep-copies nested meshes.

## If we run long, cut

Rest parameters. Keep destructure + shallow spread.

## If we run short, add

Deep copy discussion: structuredClone name, JSON round-trip cost.
