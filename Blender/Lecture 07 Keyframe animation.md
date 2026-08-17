# Lecture 7 — Keyframe animation

**Week 7 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** I-key loc/rot; Graph Editor bezier vs linear vs constant; clip idea  
**Success check:** they insert loc/rot keys on a spinning logo and can say a F-curve is what the mixer will play

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: a clip an engine can play | Invariant: engines see glTF clips; auto-key garbage is not animation; object transforms this week, bones next`

## Board at the end (they photograph this)

```
I  →  Location / Rotation
Graph Editor:  bezier (default bounce you did not want)
               linear
               constant (stepped)

glTF clip  →  Three.js AnimationMixer
24 fps is a project setting, not a runtime promise
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** A spinning logo is enough. Three.js mixer plays clips. Default bezier makes a bounce they did not want. Do not auto-key 400 garbage keys. Do not invent runtime fps from the timeline.

**Ask:** Does 24 fps in Blender mean 24 fps in the browser? Wait. Want: no — it is the clip's time base; the mixer uses dt.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *I-key, graph editor*.

**Do not:** Auto-key on by accident, 400 garbage keys.

### Minutes 10–12 — Frame

**Say:** Object vs bone: bones next week. Will this export as a clip? Constant for stepped. Midterm next week on 1–7.

**Ask:** What is a F-curve?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Insert loc/rot. Open the graph.

**Board:** three interpolation names.

**Say:** Plant auto-key. Plant animating verts in edit mode for a rigid lid.

**Ask:** Mixer vs rAF rotate — which needs a clip?

**They do:** On paper: three keys for a 360° Y spin.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Spin a logo; show bezier bounce; switch linear. Plant auto-key. Plant edit-mode vert anim for a lid.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Looping rotation. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: looping rotation; export thought. Homework: what a F-curve is; 24-frame viewport capture (not a fps claim). Quiz: insert key, linear vs bezier, mixer later.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | I-key loc/rot | Plant auto-key on. |
| 10–30 | Graph bezier → linear | Unwanted bounce. |
| 30–45 | clip name | Mixer later. |
| 45–60 | They loop the spin | Circulate. No fps brag. |

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

None this meeting.


## Snippet

```
I → Location Rotation  |  Graph Editor → Vector handles
```

---

## Extra exercises

See [[Blender/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Auto-key on by accident, 400 garbage keys.
2. Animating in edit mode verts for a rigid lid.

## If we run long, cut

NLA strips. Keep I-key + graph + clip name.

## If we run short, add

Will this be a clip on export — write yes/no.
