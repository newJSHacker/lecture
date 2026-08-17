# Lecture 5 — AR hit-test

**Week 5 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** plane detection idea  
**Success check:** immersive-ar.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: plane detection idea | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
hit-test source → pose
Phone + plane.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** AR. Phone or headset.

**Ask:** immersive-ar? Wait seven seconds. Take two answers.

**Board:** parked strip. Then hit-test source → pose.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *plane detection idea*.

**Do not:** ARKit-only native app as the homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: plane detection idea. Kernel: plane detection idea. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: ARKit-only native app as the homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** AR. Phone or headset.

**Say:** Web. Chrome Android / Quest.

**Say:** Privacy. Camera.

**Ask:** immersive-ar? Wait seven seconds. Take two answers.

**They do:** On paper: document device.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Place an object on a plane (real hit-test **or** inline fake plane).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** document device.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: document device.; remove last extra.. Homework: Written: fallback if no AR.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: plane detection idea | Plant the first common mistake. |
| 10–30 | Place an object on a plane (real hit-test **or** inline fake plane). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. document device.
2. remove last extra.

---

## Homework

1. Written: fallback if no AR.
2. demo.

---

## Quiz next meeting (they hear this now)

1. hit-test (4)
2. privacy (3)
3. inline fallback (3)


## Snippet

```js
const src = await session.requestHitTestSource({ space: viewerSpace });
```

---

## Extra exercises

See [[XR/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. AR.** Phone or headset. Hit-test gives a pose on a detected plane. Anchors persist it (next week).

**2. Web.** Chrome Android / Quest. Desktop often **no AR** — fallback: mouse-place on a fake plane in inline.

**3. Privacy.** Camera. Policy in the syllabus.

---

## Common mistakes

1. ARKit-only native app as the homework.
2. no fallback.

## If we run long, cut

Privacy

## If we run short, add

remove last extra.
