# Lecture 9 — Armatures and export pose

**Week 9 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** apply rotation & scale; rest pose; Z-up Blender vs Y-up glTF; no negative scale mirror  
**Success check:** they apply rotation/scale on the mesh before parenting, document rest pose, and check axes in a viewer later

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: a bind pose that survives export | Invariant: unapplied scale is tiny/huge in Three.js; exporter converts Z-up but they still check`

## Board at the end (they photograph this)

```
Ctrl+A Rotation & Scale   on the mesh   (backup first)
Do not apply location if it wrecks the scene

Blender Z-up     glTF / Three.js Y-up
exporter converts — still verify in a viewer

negative scale 'to mirror'  →  facing bug
IK named, optional; FK enough
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Unapplied scale is the classic tiny model in Three.js. Face orientation from week 2 still applies. If it is wrong in a glTF viewer, the engine is not the bug.

**Ask:** Why apply scale before parenting to a bone? Wait. Want: the bone inherits a 100× scale and the mesh becomes a building or a speck.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rest pose, apply*.

**Do not:** Applying location and losing the scene.

### Minutes 10–12 — Frame

**Say:** Bone axes overlay. Document rest pose in README. Negative scale to mirror is forbidden. IK name only.

**Ask:** Who is responsible for Y-up — Blender, exporter, or Three.js?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Apply rot/scale with a backup.

**Board:** Z vs Y. Rest pose.

**Say:** Plant applying location and losing the scene.

**Ask:** What is rest pose in one sentence?

**They do:** On paper: checklist before export parenting.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Apply scale; parent; pose. Plant negative scale mirror. Plant apply location.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Bone axes overlay. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: axes overlay; rest pose in README. Homework: Z-up vs Y-up; checklist screenshot. Quiz: apply scale why, Z vs Y, rest pose.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Unapplied scale plant | Cube is 100 m. |
| 10–30 | Ctrl+A rot/scale | Backup first. |
| 30–45 | Y-up talk | Viewer later. |
| 45–60 | They document rest pose | Circulate. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Bone axes overlay.
2. Document rest pose in README.

---

## Homework

1. Written: Z-up vs Y-up.
2. Checklist screenshot.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
Ctrl+A → Rotation & Scale  (object mode, backup first)
```

---

## Extra exercises

See [[Blender/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Applying location and losing the scene.
2. Negative scale to 'mirror'.

## If we run long, cut

Full IK. Keep apply + rest + axes.

## If we run short, add

Document rest pose in README.
