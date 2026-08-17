# Lecture 7 — Keyframe animation

**Week 7 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** I-key, graph editor  
**Success check:** Insert loc/rot keyframes.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: I-key, graph editor | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
loc/rot/scale tracks
Dope sheet.
Lid arc.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** What engines see. glTF can store animation clips.

**Ask:** Insert loc/rot keyframes? Wait seven seconds. Take two answers.

**Board:** parked strip. Then loc/rot/scale tracks.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *I-key, graph editor*.

**Do not:** Auto-key on by accident, 400 garbage keys.

### Minutes 10–12 — Frame

**Say:** Today’s question: I-key, graph editor. Kernel: I-key, graph editor. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Auto-key on by accident, 400 garbage keys.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** What engines see. glTF can store animation clips.

**Say:** Graph editor. Ease-in.

**Say:** Object vs bone. Bones next week.

**Ask:** Insert loc/rot keyframes? Wait seven seconds. Take two answers.

**They do:** On paper: Looping rotation.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: A lid opening 0–24 frames; play in viewport.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Looping rotation.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Looping rotation.; Export thought: will this be a clip?. Homework: Written: what a F-curve is.; 24-frame gif or mp4 of viewport.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: I-key, graph editor | Plant the first common mistake. |
| 10–30 | A lid opening 0–24 frames; play in viewport. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Looping rotation.
2. Export thought: will this be a clip?

---

## Homework

1. Written: what a F-curve is.
2. 24-frame gif or mp4 of viewport.

---

## Quiz next meeting (they hear this now)

1. insert key (2)
2. linear vs bezier (4)
3. mixer later (4)


## Snippet

```
I → Location Rotation  |  Graph Editor → Vector handles
```

---

## Extra exercises

See [[Blender/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. What engines see.** glTF can store animation clips. Three.js `AnimationMixer` plays them. A spinning logo is enough this week.

**2. Graph editor.** Ease-in. Constant for stepped. Students leave default bezier and get 'bounce' they did not want.

**3. Object vs bone.** Bones next week. This week: object transforms.

---

## Common mistakes

1. Auto-key on by accident, 400 garbage keys.
2. Animating in edit mode verts for a rigid lid.

## If we run long, cut

Object vs bone

## If we run short, add

Export thought: will this be a clip?
