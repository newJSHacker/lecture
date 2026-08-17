# Lecture 5 — Animation

**Week 5 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** clock, mixer name  
**Success check:** Clock dt.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: clock, mixer name | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
Clock.getDelta
Clock.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** dt. Same as Interactive Web.

**Ask:** Clock dt? Wait seven seconds. Take two answers.

**Board:** parked strip. Then Clock.getDelta.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *clock, mixer name*.

**Do not:** Rotation = t without dt on variable fps.

### Minutes 10–12 — Frame

**Say:** Today’s question: clock, mixer name. Kernel: clock, mixer name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: rotation = t without dt on variable fps.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** dt. Same as Interactive Web.

**Say:** Clips. Week 6 glTF may include clips.

**Say:** GSAP. Can tween Object3D; still one rAF.

**Ask:** Clock dt? Wait seven seconds. Take two answers.

**They do:** On paper: pause.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Spin + bounce with dt.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** pause.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: pause.; mixer extra if a clip exists.. Homework: Written: mixer vs rAF rotate.; Code: dt.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: clock, mixer name | Plant the first common mistake. |
| 10–30 | Spin + bounce with dt. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. pause.
2. mixer extra if a clip exists.

---

## Homework

1. Written: mixer vs rAF rotate.
2. Code: dt.

---

## Quiz next meeting (they hear this now)

1. getDelta (3)
2. mixer (4)
3. pause (3)


## Snippet

```js
const dt = clock.getDelta();
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. dt.** Same as Interactive Web.

**2. Clips.** Week 6 glTF may include clips.

**3. GSAP.** Can tween Object3D; still one rAF.

---

## Common mistakes

1. rotation = t without dt on variable fps.

## If we run long, cut

GSAP

## If we run short, add

mixer extra if a clip exists.
