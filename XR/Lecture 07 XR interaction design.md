# Lecture 7 — XR interaction design

**Week 7 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** affordances, diegetic UI  
**Success check:** Diegetic vs HUD.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: affordances, diegetic UI | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
laser vs hands vs panel
Panel at arm length.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** UX. VR UI is not a 2D website pasted at 1 m without thought.

**Ask:** Diegetic vs HUD? Wait seven seconds. Take two answers.

**Board:** parked strip. Then laser vs hands vs panel.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *affordances, diegetic UI*.

**Do not:** Browser DOM only, never in-world.

### Minutes 10–12 — Frame

**Say:** Today’s question: affordances, diegetic UI. Kernel: affordances, diegetic UI. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: browser DOM only, never in-world.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** UX. VR UI is not a 2D website pasted at 1 m without thought.

**Say:** Fatigue. Arms-up is tiring.

**Say:** Feedback. Highlight, sound optional, haptic optional.

**Ask:** Diegetic vs HUD? Wait seven seconds. Take two answers.

**They do:** On paper: hover scale.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: A world-space panel with 3 large buttons; laser select.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** hover scale.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: hover scale.; sitting layout extra.. Homework: Written: 8 XR UX rules.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: affordances, diegetic UI | Plant the first common mistake. |
| 10–30 | A world-space panel with 3 large buttons; laser select. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. hover scale.
2. sitting layout extra.

---

## Homework

1. Written: 8 XR UX rules.
2. demo.

---

## Quiz next meeting (they hear this now)

1. angular size (4)
2. diegetic (3)
3. fatigue (3)


## Snippet

```
min hit ~ 3–5° visual angle teaching target
```

---

## Extra exercises

See [[XR/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. UX.** VR UI is not a 2D website pasted at 1 m without thought. Prefer world panels at arm's length, large hit targets.

**2. Fatigue.** Arms-up is tiring. Waist-level menus. Rest poses.

**3. Feedback.** Highlight, sound optional, haptic optional.

---

## Common mistakes

1. browser DOM only, never in-world.
2. tiny text.

## If we run long, cut

Feedback

## If we run short, add

sitting layout extra.
