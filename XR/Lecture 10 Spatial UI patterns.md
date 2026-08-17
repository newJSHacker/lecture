# Lecture 10 — Spatial UI patterns

**Week 10 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** menus, keyboards, inventories  
**Success check:** Follow-head menu (with lag).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: menus, keyboards, inventories | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
follow-head vs world-locked
Wrist menu.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Patterns. Wrist menu, belt, look-to-pin.

**Ask:** Follow-head menu (with lag)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then follow-head vs world-locked.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *menus, keyboards, inventories*.

**Do not:** Custom keyboard as the whole project.

### Minutes 10–12 — Frame

**Say:** Today’s question: menus, keyboards, inventories. Kernel: menus, keyboards, inventories. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: custom keyboard as the whole project.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Patterns. Wrist menu, belt, look-to-pin.

**Say:** Text entry. Painful.

**Say:** System. Don't trap the user; they must exit to the OS menu.

**Ask:** Follow-head menu (with lag)? Wait seven seconds. Take two answers.

**They do:** On paper: world-locked mode extra.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Wrist or look-down menu with 3 actions.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** world-locked mode extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: world-locked mode extra.; exit XR button obvious.. Homework: Written: follow vs world.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: menus, keyboards, inventories | Plant the first common mistake. |
| 10–30 | Wrist or look-down menu with 3 actions. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. world-locked mode extra.
2. exit XR button obvious.

---

## Homework

1. Written: follow vs world.
2. demo.

---

## Quiz next meeting (they hear this now)

1. trap (4)
2. wrist (3)
3. text entry (3)


## Extra exercises

See [[XR/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Patterns.** Wrist menu, belt, look-to-pin. Pick one.

**2. Text entry.** Painful. Prefer fewer strings; large keys; or HUD on companion phone extra.

**3. System.** Don't trap the user; they must exit to the OS menu.

---

## Common mistakes

1. custom keyboard as the whole project.
2. no exit.

## If we run long, cut

System

## If we run short, add

exit XR button obvious.
