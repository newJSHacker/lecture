# Lecture 7 — Textures and color space

**Week 7 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** TextureLoader; albedo SRGBColorSpace; data maps stay linear  
**Success check:** they put a local map on a sphere and can say which maps are sRGB

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: maps that match the shader | Invariant: wrong colorSpace is a lighting bug; sRGB normals are a bug`

## Board at the end (they photograph this)

```
albedo / color map     SRGBColorSpace
normal, roughness, metal     linear / NoColorSpace

tex.colorSpace = THREE.SRGBColorSpace   // albedo only
tex.wrapS = RepeatWrapping; tex.repeat.set(4,4)

renderer.outputColorSpace = SRGBColorSpace
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** CG I gamma, WebGL week 9 pow(1/2.2). three r152+ colorSpace. Demo 05-canvas-texture.html. Uncapped anisotropy is not the lab.

**Ask:** Should a normal map be SRGBColorSpace? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *map, colorSpace*.

**Do not:** SRGB normals.

### Minutes 10–12 — Frame

**Say:** Maps: albedo vs normal vs roughness. Repeat 4. Canvas texture is a CPU map — still local.

**Ask:** Which maps are sRGB?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Color management. outputColorSpace on renderer.

**Board:** sRGB vs linear table.

**Say:** Plant sRGB on normals. The lighting goes muddy.

**Ask:** Why repeat wrapping on a floor?

**They do:** On paper: three map types and their colorSpace.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Albedo on a sphere; wrong colorSpace toggle. Demo 05-canvas-texture.html. Plant sRGB normals.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** repeat 4. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: repeat 4; normal extra. Homework: which maps are sRGB; texture. Quiz: albedo space, normal sRGB?, repeat. Midterm next week on 1–7.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | TextureLoader local | Plant CDN image host. |
| 10–30 | albedo SRGB | Plant default wrong on a PNG. |
| 30–45 | normal linear | Plant SRGB on normal. |
| 45–60 | They repeat 4 | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. repeat 4.
2. normal extra.

---

## Homework

1. Written: which maps are sRGB.
2. Code: texture.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
tex.colorSpace = THREE.SRGBColorSpace;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. sRGB normals.
2. uncapped anisotropy always.

## If we run long, cut

Anisotropy race. Keep colorSpace table.

## If we run short, add

normalMap extra on Standard.
