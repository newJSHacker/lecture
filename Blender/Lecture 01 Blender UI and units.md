# Lecture 1 — Blender UI and units

**Week 1 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** viewport navigation; scene unit = meter; save .blend; apply scale as a name  
**Success check:** they can orbit the viewport, set metric 1.0, and say a 100 m mug will fail in Three.js

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Blender/code/01-units.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: meters before modeling | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
Scene unit = 1 meter
character ~1.7 m     mug in centimeters (0.08 m)

Object vs Edit     Outliner     N-panel     numpad views

Ctrl+A Rotation & Scale   (name this week; do it before export)
Face orientation overlay     Statistics: triangles
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** This course supplies assets that survive in a real-time engine — not a Cycles feature film. Wrong scale is the #1 Three.js import bug. Checklist: Blender/code/01-units.html.

**Ask:** If a mug is 100 units tall in Blender, what happens in a Y-up meter world? Wait. Want: it is a building.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *viewport, meters, save*.

**Do not:** Modeling in whatever scale 'looks good'.

### Minutes 8–12 — Frame

**Say:** Metric, unit scale 1.0. Outliner names. Delete the default cube only after duplicating a backup. Never model at 'looks good' scale.

**Ask:** Object mode vs Edit mode — which moves the origin?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why Blender in IGWT: topology, UVs, Principled, glTF.

**Board:** meters. 1.7 m human. Outliner.

**Say:** Face orientation and statistics overlays on day one so they exist.

**Ask:** Why apply scale later?

**They do:** On paper: three objects with intended sizes in meters.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Set units; scale a cube to 1.7 m; screenshot outliner. Demo 01-units.html as the checklist. Plant modeling at unknown scale.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Rename objects in the outliner. Duplicate cube before delete. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: rename; backup cube. Homework: why meters; numbered outliner screenshot. Quiz: default unit, Object vs Edit, 100 m mug.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Orbit / numpad / outliner | Plant only watching YouTube. |
| 10–30 | Metric 1.0 + 1.7 m cube | Plant 'looks good' scale. |
| 30–45 | Face orientation overlay | Red faces named. |
| 45–60 | They rename + save | Circulate. 01-units.html. |

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

None this meeting.


## Snippet

```
Scene Properties → Units → Metric, Unit Scale 1.0
```

## Extra exercises

See [[Blender/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Modeling in whatever scale 'looks good'.
2. Never applying scale.

## If we run long, cut

Every keymap. Keep units + outliner.

## If we run short, add

Delete default cube only after duplicating a backup.
