# Lecture 9 — Armatures and export pose

**Week 9 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rest pose, apply  
**Success check:** Apply rotation and scale on meshes.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: rest pose, apply | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
Ctrl+A apply rotation/scale
Axes.
Apply menu.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Apply transforms. Unapplied scale is the classic 'tiny model / huge model' in Three.js.

**Ask:** Apply rotation and scale on meshes? Wait seven seconds. Take two answers.

**Board:** parked strip. Then Ctrl+A apply rotation/scale.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rest pose, apply*.

**Do not:** Applying location and losing the scene.

### Minutes 10–12 — Frame

**Say:** Today’s question: rest pose, apply. Kernel: rest pose, apply. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Applying location and losing the scene.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Apply transforms. Unapplied scale is the classic 'tiny model / huge model' in Three.js.

**Say:** Orientation. Blender Z-up vs glTF / Three.js Y-up.

**Say:** IK. Name it.

**Ask:** Apply rotation and scale on meshes? Wait seven seconds. Take two answers.

**They do:** On paper: Bone axes overlay.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Apply scale on last week's arm; re-parent if needed; pose two frames.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Bone axes overlay.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Bone axes overlay.; Document rest pose in README.. Homework: Written: Z-up vs Y-up.; Checklist screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: rest pose, apply | Plant the first common mistake. |
| 10–30 | Apply scale on last week's arm; re-parent if needed; pose two frames. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. apply scale why (4)
2. Z vs Y (3)
3. rest pose (3)


## Snippet

```
Ctrl+A → Rotation & Scale  (object mode, backup first)
```

---

## Extra exercises

See [[Blender/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Apply transforms.** Unapplied scale is the classic 'tiny model / huge model' in Three.js. Ctrl+A → All Transforms on the mesh before parenting, with a backup.

**2. Orientation.** Blender Z-up vs glTF / Three.js Y-up. Exporter converts. Students must still check in the engine.

**3. IK.** Name it. Optional extra. FK is enough for a spinning sign or a simple arm.

---

## Common mistakes

1. Applying location and losing the scene.
2. Negative scale to 'mirror'.

## If we run long, cut

IK

## If we run short, add

Document rest pose in README.
