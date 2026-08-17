# Lecture 7 — Textures and color space

**Week 7 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** map, colorSpace  
**Success check:** TextureLoader.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: map, colorSpace | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
SRGBColorSpace
Maps.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Color. CG I gamma.

**Ask:** TextureLoader? Wait seven seconds. Take two answers.

**Board:** parked strip. Then SRGBColorSpace.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *map, colorSpace*.

**Do not:** SRGB normals.

### Minutes 10–12 — Frame

**Say:** Today’s question: map, colorSpace. Kernel: map, colorSpace. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: sRGB normals.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Color. CG I gamma.

**Say:** Maps. albedo vs normal vs roughness.

**Say:** Demo. textures.

**Ask:** TextureLoader? Wait seven seconds. Take two answers.

**They do:** On paper: repeat 4.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Albedo on a sphere; wrong colorSpace toggle if you can.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** repeat 4.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: repeat 4.; normal extra.. Homework: Written: which maps are sRGB.; Code: texture.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: map, colorSpace | Plant the first common mistake. |
| 10–30 | Albedo on a sphere; wrong colorSpace toggle if you can. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. albedo space (4)
2. normal sRGB? (3)
3. repeat (3)


## Snippet

```js
tex.colorSpace = THREE.SRGBColorSpace;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Color.** CG I gamma. three r152+ colorSpace.

**2. Maps.** albedo vs normal vs roughness.

**3. Demo.** textures.

---

## Common mistakes

1. sRGB normals.
2. uncapped anisotropy always.

## If we run long, cut

Demo

## If we run short, add

normal extra.
