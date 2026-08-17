# Lecture 12 — Creative coding habits

**Week 12 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** constraints, seeds  
**Success check:** A seedable random.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: constraints, seeds | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
seed → scene
Seed box.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Craft. Creative coding is **choice under constraint**.

**Ask:** A seedable random? Wait seven seconds. Take two answers.

**Board:** parked strip. Then seed → scene.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *constraints, seeds*.

**Do not:** 50 sliders, no taste.

### Minutes 10–12 — Frame

**Say:** Today’s question: constraints, seeds. Kernel: constraints, seeds. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 50 sliders, no taste.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Craft. Creative coding is **choice under constraint**.

**Say:** Tools. leva sliders OK if they don't replace a story.

**Say:** Integrity. Shaders and models cited.

**Ask:** A seedable random? Wait seven seconds. Take two answers.

**They do:** On paper: palette of 5.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Seed field regenerates a small composition.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** palette of 5.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: palette of 5.; png export extra.. Homework: Written: constraints you chose.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: constraints, seeds | Plant the first common mistake. |
| 10–30 | Seed field regenerates a small composition. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. palette of 5.
2. png export extra.

---

## Homework

1. Written: constraints you chose.
2. demo.

---

## Quiz next meeting (they hear this now)

1. seed (3)
2. leva risk (3)
3. cite (4)


## Snippet

```js
function rand(i){ return fract(sin(i*78.23)*43758.5); }
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Craft.** Creative coding is **choice under constraint**. One seed, one palette, one motion.

**2. Tools.** leva sliders OK if they don't replace a story.

**3. Integrity.** Shaders and models cited. AI textures: AI course later, still cite.

---

## Common mistakes

1. 50 sliders, no taste.
2. unlicensed assets.

## If we run long, cut

Integrity

## If we run short, add

png export extra.
