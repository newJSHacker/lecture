# Lecture 12 — Performance

**Week 12 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** draw calls; InstancedMesh; LOD name; renderer.info.render  
**Success check:** they log info.render on 200 meshes vs InstancedMesh and cap pixelRatio; they do not invent fps

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: count, then cut | Invariant: a Mesh is a draw; measure on this machine; 8k on a cube is a budget fail`

## Board at the end (they photograph this)

```
console.log(renderer.info.render)   // calls, triangles

200 Mesh     =  200 draws
1 InstancedMesh(n=200)  =  1 draw

LOD.addLevel(high, 0) / (mid, 8) / (low, 18)
pixelRatio 1 vs min(dpr, 2)

measure or omit     no invented fps
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Blender course polycounts meet the engine. Demos 08-instancing.html and 15-lod.html. WebGL week 12 in engine form.

**Ask:** If info.render.calls is 200, what did you probably create? Wait. Want: 200 Mesh, not InstancedMesh.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *draw calls, instancing, LOD name*.

**Do not:** Invented fps.

### Minutes 10–12 — Frame

**Say:** Frustum culling named. pixelRatio 1 vs 2 is a fill-rate lab. Stats.js optional. 8k textures on a cube forbidden.

**Ask:** What is a draw call in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Count first. Then instance or LOD.

**Board:** info.render. InstancedMesh.

**Say:** LOD name. Distances are teaching numbers, not a promise.

**Ask:** Why cap pixelRatio at 2?

**They do:** On paper: budget table headers: draws, tris, maps — fill later by measuring.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** 200 meshes vs InstancedMesh; log info.render. Demos 08-instancing.html, 15-lod.html. Plant invented 60 fps. Plant 8k on a cube.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** pixelRatio 1 vs 2. Log calls. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pixelRatio; stats. Homework: budget table measured; instanced. Quiz: draw call, InstancedMesh, info.render. R3F teaser next.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | info.render on a cube | 1 call. |
| 10–30 | 200 Mesh vs InstancedMesh | Log calls. No fps speech. |
| 30–45 | LOD name + demo 15 | Distances as names. |
| 45–60 | They cap pixelRatio | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. pixelRatio 1 vs 2.
2. stats.

---

## Homework

1. Written: a budget table (invented numbers forbidden — measure).
2. Code: instanced.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
console.log(renderer.info.render);
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. invented fps.
2. 8k textures on a cube.

## If we run long, cut

GPU profiler internals. Keep calls + instance + measure.

## If we run short, add

stats overlay or info.render dump.
