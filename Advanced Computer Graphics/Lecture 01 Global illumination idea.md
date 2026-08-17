# Lecture 1 — Global illumination idea

**Week 1 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** direct = bounce 0; GI is the rest; IBL is not GI  
**Success check:** they can point at the dark side of a cube and say what local PBR misses

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Advanced Computer Graphics/code/01-radiosity2.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: name the gap before a tracer | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
lamp → cube face     =  direct (bounce 0)
wall → cube back     =  indirect (GI)

IBL  =  stand-in for the rest of the world
IBL  ≠  GI

albedo < 1     white room goes grey
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Three.js local scene vs cited GI still | photograph |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** RTR PBR is mostly local: lights + IBL as a stand-in. GI is light after leaving other surfaces. 'PBR already is GI' is the plant. We do not start with a production path tracer.

**Ask:** Does an HDRI mean the cube's shadow side received bounce from the wall? Wait. Want: no — that is IBL, not GI.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *direct vs indirect*.

**Do not:** 'PBR already is GI'.

### Minutes 8–12 — Frame

**Say:** Taxonomy named: radiosity, path tracing, photon mapping, irradiance volumes, SSGI, probes. This course implements teaching-scale radiosity idea + a tiny tracer. Energy: unbounded albedo 2.0 is a bug.

**Ask:** What is color bleeding?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The gap. Draw lamp, wall, dark side.

**Board:** bounce 0 vs rest. IBL ≠ GI.

**Say:** Rendering equation as a name. L_out = emit + ∫ … We will not solve it in closed form today.

**Ask:** Why does a white room go grey?

**They do:** Table of 5 GI methods: realtime? teaching impl this term?

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Diagram + cited GI still vs Three.js local. Plant 'PBR is GI'. Plant albedo 2.0. Demo 01-radiosity2.html as a teaser, not the week's kernel.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Five-method table + IBL vs GI sentence. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: table; albedo note. Homework: why IBL is not full GI. Quiz: indirect, bleeding, IBL vs GI.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Lamp / wall / dark side | Plant PBR=GI. |
| 15–40 | Taxonomy names | Plant production tracer. |
| 40–55 | Albedo < 1 | Albedo 2 plant. |
| 55–60 | They write IBL ≠ GI | Circulate. |

Point them at `Advanced Computer Graphics/code/01-radiosity2.html` as the after-class check, not as the lecture.

---

## Lab

1. list 5 GI methods in a table: realtime?
2. albedo < 1 note.

---

## Homework

1. Written: why IBL is not full GI.
2. figure.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
L_out = emit + ∫ BRDF * L_in * n·ω dω
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 'PBR already is GI'.
2. unbounded albedo 2.0.

## If we run long, cut

Energy proofs. Keep gap + IBL ≠ GI.

## If we run short, add

Albedo < 1 note.
