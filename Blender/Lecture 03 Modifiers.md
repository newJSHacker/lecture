# Lecture 3 — Modifiers

**Week 3 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** mirror, array, bevel  
**Success check:** Use Mirror with clipping.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: mirror, array, bevel | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
stack: mirror then bevel
Stack arrows.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Non-destructive. Modifiers are the 'functions' of modeling.

**Ask:** Mirror with clipping? Wait seven seconds. Take two answers.

**Board:** parked strip. Then stack: mirror then bevel.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *mirror, array, bevel*.

**Do not:** Applying every modifier 'to be safe' every five minutes.

### Minutes 10–12 — Frame

**Say:** Today’s question: mirror, array, bevel. Kernel: mirror, array, bevel. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Applying every modifier 'to be safe' every five minutes.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Non-destructive. Modifiers are the 'functions' of modeling.

**Say:** Order. Mirror before bevel usually.

**Say:** Boolean. Name it.

**Ask:** Mirror with clipping? Wait seven seconds. Take two answers.

**They do:** On paper: Toggle modifier visibility.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Mirrored headset or binoculars; bevel; array of buttons.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Toggle modifier visibility.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Toggle modifier visibility.; One boolean hole, then cleanup extra.. Homework: Written: apply vs live.; Screenshot of modifier stack.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: mirror, array, bevel | Plant the first common mistake. |
| 10–30 | Mirrored headset or binoculars; bevel; array of buttons. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. mirror clipping (3)
2. why order (4)
3. export applies? (3)


## Snippet

```
Mirror → Bevel → Triangulate (export)
```

---

## Extra exercises

See [[Blender/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Non-destructive.** Modifiers are the 'functions' of modeling. Keep them live while iterating. Apply before some exports if the engine cannot see them — glTF export applies mesh modifiers.

**2. Order.** Mirror before bevel usually. Array after the piece is right. Students reverse the stack and get double bevels.

**3. Boolean.** Name it. Use for blocking. Retopo or cleanup before animation.

---

## Common mistakes

1. Applying every modifier 'to be safe' every five minutes.
2. Boolean soup.

## If we run long, cut

Boolean

## If we run short, add

One boolean hole, then cleanup extra.
