# Lecture 10 — Spatial UI patterns

**Week 10 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one spatial menu pattern; obvious exit; do not ship a custom keyboard as the project  
**Success check:** they can open a wrist or look-down menu with three actions and exit XR

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: three actions, a way out | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
pick one:  wrist · belt · look-to-pin
3 actions
exit XR  obvious     (OS menu still exists)

text entry is painful — fewer strings
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Patterns: wrist, belt, look-to-pin. Pick one. A custom keyboard as the whole project fails. Trapping the user fails.

**Ask:** Where is Exit? Wait. Then find it.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *menus, keyboards, inventories*.

**Do not:** Custom keyboard as the whole project.

### Minutes 10–12 — Frame

**Say:** World-locked mode extra. Companion-phone HUD named extra. Inline: the same three actions in a panel.

**Ask:** Why is text entry a last resort?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** One pattern. Three actions.

**Board:** wrist/belt/look. Exit circled.

**Say:** System: they must reach the OS menu. We do not trap.

**Ask:** What is look-to-pin for?

**They do:** Sketch one menu + exit.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Wrist or look-down menu, three actions. Plant no exit. Plant custom keyboard as the week.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three-action menu + exit. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: world-locked extra; exit obvious. Homework: pattern paragraph. Quiz: one pattern, exit, no keyboard-project.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Pick a pattern | Plant all three at once. |
| 15–40 | Three actions | Plant keyboard project. |
| 40–55 | Exit XR | Trap plant. |
| 55–60 | They place exit | Circulate. |

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

None this meeting.


## Extra exercises

See [[XR/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. custom keyboard as the whole project.
2. no exit.

## If we run long, cut

System keyboard research. Keep menu + exit.

## If we run short, add

Exit control obvious in inline too.
