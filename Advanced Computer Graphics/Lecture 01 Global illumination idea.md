# Lecture 1 — Global illumination idea

**Week 1 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** direct vs indirect  
**Success check:** Define direct vs indirect light.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Advanced Computer Graphics/code/01-radiosity2.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: direct vs indirect | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
bounce paths; energy
One bounce vs many.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** The gap. RTR PBR is mostly **local**: lights + IBL as a stand-in for the rest of the world.

**Ask:** direct vs indirect light? Wait seven seconds. Take two answers.

**Board:** parked strip. Then bounce paths; energy.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *direct vs indirect*.

**Do not:** 'PBR already is GI'.

### Minutes 8–12 — Frame

**Say:** Today’s question: direct vs indirect. Kernel: direct vs indirect. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 'PBR already is GI'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The gap. RTR PBR is mostly **local**: lights + IBL as a stand-in for the rest of the world.

**Say:** Taxonomy. Radiosity, path tracing, photon mapping, irradiance volumes, screen-space GI, probes.

**Say:** Energy. Each bounce loses energy (unless metal).

**Ask:** direct vs indirect light? Wait seven seconds. Take two answers.

**They do:** On paper: list 5 GI methods in a table: realtime?

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: A diagram: lamp, wall, dark side of a cube — what RTR misses. Screenshot a Three.js scene vs a GI reference still (can be from a paper, cited).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** list 5 GI methods in a table: realtime?

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: list 5 GI methods in a table: realtime?; albedo < 1 note.. Homework: Written: why IBL is not full GI.; figure.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: direct vs indirect | Plant the first common mistake. |
| 10–30 | A diagram: lamp, wall, dark side of a cube — what RTR misses. Screenshot a Three.js scene vs a GI reference still (can be from a paper, cited). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. indirect (3)
2. bleeding (3)
3. IBL vs GI (4)


## Snippet

```
L_out = emit + ∫ BRDF * L_in * n·ω dω
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. The gap.** RTR PBR is mostly **local**: lights + IBL as a stand-in for the rest of the world. GI is light after **leaving** other surfaces.

**2. Taxonomy.** Radiosity, path tracing, photon mapping, irradiance volumes, screen-space GI, probes. This course **names** them and implements teaching-scale versions of two: radiosity idea + a tiny path tracer.

**3. Energy.** Each bounce loses energy (unless metal). White rooms still go grey if you forget albedo < 1.

---

## Common mistakes

1. 'PBR already is GI'.
2. unbounded albedo 2.0.

## If we run long, cut

Energy

## If we run short, add

albedo < 1 note.
