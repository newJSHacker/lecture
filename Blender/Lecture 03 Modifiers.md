# Lecture 3 — Modifiers

**Week 3 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Mirror with clipping; Array; Bevel; stack order; apply vs live  
**Success check:** they can mirror a crate with clipping and say glTF export applies mesh modifiers

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: non-destructive until export needs it | Invariant: modifiers are functions; order matters; applying every five minutes is not safety`

## Board at the end (they photograph this)

```
Mirror  +  clipping     (do not duplicate by hand)
Array   after the piece is right
Bevel   usually after Mirror

live while iterating
glTF export applies mesh modifiers

Boolean: blocking only; cleanup before animation
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Modifiers are the functions of modeling. Reverse the stack and you get double bevels. Demo checklist 03-budget.html is not this week's kernel — still glance at tris.

**Ask:** If Mirror sits after Bevel, what goes wrong? Wait. Want: you bevel a half then mirror a seam, or double bevel — show it.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *mirror, array, bevel*.

**Do not:** Applying every modifier 'to be safe' every five minutes.

### Minutes 10–12 — Frame

**Say:** Keep live. Apply before some exports if the engine cannot see them — glTF applies mesh modifiers. Boolean named, not soup.

**Ask:** Apply vs live — when must it apply?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Mirror clipping so the center welds.

**Board:** stack order. Array. Bevel.

**Say:** Plant applying every modifier to be safe every five minutes.

**Ask:** Does the engine see an unapplied Mirror if you forget export-apply?

**They do:** On paper: a three-modifier stack for a crate.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Mirror crate; reverse stack once. Plant apply-all. Plant boolean soup.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Toggle modifier visibility. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: toggle visibility; one boolean hole extra. Homework: apply vs live; stack screenshot. Quiz: clipping, why order, export applies?.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Mirror + clipping | Plant duplicate-by-hand. |
| 10–30 | Bevel after mirror | Plant reverse stack. |
| 30–45 | Array a bolt | They instance in Blender. |
| 45–60 | They toggle visibility | Circulate. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Toggle modifier visibility.
2. One boolean hole, then cleanup extra.

---

## Homework

1. Written: apply vs live.
2. Screenshot of modifier stack.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
Mirror → Bevel → Triangulate (export)
```

---

## Extra exercises

See [[Blender/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Applying every modifier 'to be safe' every five minutes.
2. Boolean soup.

## If we run long, cut

Geometry Nodes as the course. Keep mirror/array/bevel.

## If we run short, add

One boolean hole, then cleanup extra.
