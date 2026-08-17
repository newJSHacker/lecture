# Lecture 12 — Browser rendering pipeline

**Week 12 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** DOM CSSOM layout paint composite  
**Success check:** Name DOM, CSSOM, layout, paint, composite.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Web Technologies/code/10-transform.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: DOM CSSOM layout paint composite | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
the six-stage stack from Course 2 advice
Pipeline stack.
Layer sandwich.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** How a pixel gets there. Parse HTML → DOM.

**Ask:** DOM, CSSOM, layout, paint, composite? Wait seven seconds. Take two answers.

**Board:** parked strip. Then the six-stage stack from Course 2 advice.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *DOM CSSOM layout paint composite*.

**Do not:** Animating left/top for everything.

### Minutes 10–12 — Frame

**Say:** Today’s question: DOM CSSOM layout paint composite. Kernel: DOM CSSOM layout paint composite. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Animating left/top for everything.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** How a pixel gets there. Parse HTML → DOM.

**Say:** Jank. Reading offsetWidth in a loop forces layout.

**Say:** Layers. A WebGL canvas is often its own layer.

**Ask:** DOM, CSSOM, layout, paint, composite? Wait seven seconds. Take two answers.

**They do:** On paper: Paint flashing experiment.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Animate a box with transform vs top/left; feel the difference (or show paint flashing).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Paint flashing experiment.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Paint flashing experiment.; One forced-layout bug in a starter to fix.. Homework: Written: pipeline boxes.; Code: CSS transform animation.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: DOM CSSOM layout paint composite | Plant the first common mistake. |
| 10–30 | Animate a box with transform vs top/left; feel the difference (or show paint flashing). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/10-transform.html` as the after-class check, not as the lecture.

---

## Lab

1. Paint flashing experiment.
2. One forced-layout bug in a starter to fix.

---

## Homework

1. Written: pipeline boxes.
2. Code: CSS transform animation.

---

## Quiz next meeting (they hear this now)

1. Order of layout and paint (4)
2. Why transform (3)
3. Name composite (3)


## Snippet

```css
.box { transform: translateX(20px); }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. How a pixel gets there.** Parse HTML → DOM. CSS → CSSOM. Layout boxes. Paint. Composite layers. Same spirit as CG I's space chain: named stages.

**2. Jank.** Reading offsetWidth in a loop forces layout. Animate transform/opacity when possible.

**3. Layers.** A WebGL canvas is often its own layer. UI HTML sits on top. That is Interactive Web + R3F later.

---

## Common mistakes

1. Animating left/top for everything.
2. No DevTools.

## If we run long, cut

Layers

## If we run short, add

One forced-layout bug in a starter to fix.
