# Lecture 4 — Lights and shadows intro

**Week 4 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Ambient + Directional + Point named; shadowMap.enabled; castShadow / receiveShadow  
**Success check:** they light a cube on a plane, toggle a shadow, and do not spawn ten point lights

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: one key light, then a shadow you can see | Invariant: a light is uniforms plus optional shadow FBO; acne is bias, not 'broken PBR'`

## Board at the end (they photograph this)

```
Ambient     =  cheap fill (no direction)
Directional =  sun     Point = omni     Spot named

renderer.shadowMap.enabled = true
mesh.castShadow / plane.receiveShadow
light.castShadow = true
mapSize 512 vs 2048   (measure; not 8192)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Energy: too many lights is a later clustered topic. Demo 03-lights-shadows.html. Shadow mapping internals live in Real-Time Rendering — here we enable and see acne.

**Ask:** Does AmbientLight cast a shadow? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *dir/point/ambient*.

**Do not:** 10 point lights as the aesthetic.

### Minutes 10–12 — Frame

**Say:** Helpers: DirectionalLightHelper. mapSize 8192 on integrated GPU is a freeze violation. Contact-shadow demo 20 is later.

**Ask:** What WebGL object is a shadow map?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three types. One key directional.

**Board:** enable shadowMap + flags.

**Say:** Acne name. Bias next week deeper.

**Ask:** Why a ground plane this week?

**They do:** On paper: flags needed for a cube to shadow a plane.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Lit cube + plane; toggle shadow. Demo 03-lights-shadows.html. Plant 10 point lights. Plant mapSize 8192.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Light helper on. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: helper; mapSize 512 vs 2048 extra measure. Homework: acne; shadows. Quiz: castShadow, ambient purpose, mapSize.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Hemisphere or ambient + dir | Plant only ambient. |
| 10–30 | shadowMap + flags | Plant forgot receiveShadow. |
| 30–45 | mapSize measure | No invented fps. |
| 45–60 | They add helper | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. light helper.
2. mapSize 512 vs 2048 extra measure.

---

## Homework

1. Written: acne.
2. Code: shadows.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
dir.castShadow = true; renderer.shadowMap.enabled = true;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 10 point lights as the aesthetic.
2. mapSize 8192 on integrated GPU.

## If we run long, cut

PCFSoft internals. Keep enable + one shadow.

## If we run short, add

mapSize 512 vs 2048 measured on this machine.
