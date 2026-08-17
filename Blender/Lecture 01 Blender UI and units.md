# Lecture 1 — Blender UI and units

**Week 1 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** viewport, meters, save  
**Success check:** Navigate the 3D viewport.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Blender/code/01-units.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: viewport, meters, save | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
grid = meters; origin at 0
Meter grid.
Outliner.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Why Blender in IGWT. Semester 3 already has WebGL and Three.js.

**Ask:** Navigate the 3D viewport? Wait seven seconds. Take two answers.

**Board:** parked strip. Then grid = meters; origin at 0.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *viewport, meters, save*.

**Do not:** Modeling in whatever scale 'looks good'.

### Minutes 8–12 — Frame

**Say:** Today’s question: viewport, meters, save. Kernel: viewport, meters, save. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Modeling in whatever scale 'looks good'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why Blender in IGWT. Semester 3 already has WebGL and Three.js.

**Say:** Units. Scene unit = 1 meter.

**Say:** UI. Outliner, Properties, Timeline.

**Ask:** Navigate the 3D viewport? Wait seven seconds. Take two answers.

**They do:** On paper: Rename objects in the outliner.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Create a 2 m cube, a 0.2 m cube, and a camera. Screenshot the dimensions panel. Save `week01.blend`.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Rename objects in the outliner.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Rename objects in the outliner.; Delete the default cube only after duplicating a backup.. Homework: Written: why meters.; A numbered screenshot of your outliner.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: viewport, meters, save | Plant the first common mistake. |
| 10–30 | Create a 2 m cube, a 0.2 m cube, and a camera. Screenshot the dimensions panel. Save `week01.blend`. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/01-units.html` as the after-class check, not as the lecture.

---

## Lab

1. Rename objects in the outliner.
2. Delete the default cube only after duplicating a backup.

---

## Homework

1. Written: why meters.
2. A numbered screenshot of your outliner.

---

## Quiz next meeting (they hear this now)

1. Default unit (2)
2. Object vs Edit (4)
3. Why a 100 m mug fails in Three.js (4)


## Snippet

```
Scene Properties → Units → Metric, Unit Scale 1.0
```

## Extra exercises

See [[Blender/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Why Blender in IGWT.** Semester 3 already has WebGL and Three.js. This course supplies **assets** that survive in a real-time engine: clean topology, UVs, PBR maps, and glTF. It is not a film-lighting course.

**2. Units.** Scene unit = 1 meter. A character is ~1.7 m. A product is centimeters. Wrong scale is the #1 Three.js import bug.

**3. UI.** Outliner, Properties, Timeline. N-panel. Numpad views. Edit vs Object. Students who only watch YouTube never learn the outliner.

---

## Common mistakes

1. Modeling in whatever scale 'looks good'.
2. Never applying scale.

## If we run long, cut

UI

## If we run short, add

Delete the default cube only after duplicating a backup.
