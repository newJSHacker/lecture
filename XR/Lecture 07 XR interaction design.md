# Lecture 7 — XR interaction design

**Week 7 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** diegetic / world panel, large hits, waist height; not a 2D site at 1 m  
**Success check:** they can laser-select three large world buttons and say why tiny text fails

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: XR UI you can hit while seated | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
diegetic / world panel     vs     browser DOM only
arm's length     large hits     ~3–5° teaching target
waist / rest     not arms-up forever

sitting layout still works
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** VR UI is not a website pasted at one meter. Prefer world panels, large targets, rest poses. Browser-DOM-only never in-world fails the week. Tiny text fails.

**Ask:** After two minutes arms-up, what happened to accuracy? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *affordances, diegetic UI*.

**Do not:** Browser DOM only, never in-world.

### Minutes 10–12 — Frame

**Say:** Hover scale. Sitting layout extra. Feedback: highlight; sound/haptic optional. Inline: the same three buttons in a panel.

**Ask:** Diegetic vs HUD in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Affordances. Hits you can see.

**Board:** three buttons, arm's length. Sitting mark.

**Say:** Fatigue. Waist-level menus.

**Ask:** Why not only DOM overlay this week?

**They do:** Sketch a seated panel with three hits.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** World panel, three large buttons, laser select. Plant tiny text. Plant DOM-only. Sitting layout extra.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three world buttons (or inline panel analog). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: hover scale; sitting extra. Homework: diegetic vs HUD. Quiz: hit size, fatigue, sitting. Next: midterm then comfort.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | World panel | Plant DOM-only. |
| 15–40 | Large hits + laser | Plant tiny text. |
| 40–55 | Sitting layout | Arms-up plant. |
| 55–60 | They add hover scale | Circulate. |

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

None this meeting.


## Snippet

```
min hit ~ 3–5° visual angle teaching target
```

---

## Extra exercises

See [[XR/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. browser DOM only, never in-world.
2. tiny text.

## If we run long, cut

Full UX paper. Keep panel + hits.

## If we run short, add

Sitting layout extra.
