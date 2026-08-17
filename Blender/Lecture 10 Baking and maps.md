# Lecture 10 — Baking and maps

**Week 10 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** normal map stores offset to N; AO named; BaseColor sRGB, data maps non-color  
**Success check:** they know what a normal map stores and do not bake 8k or sRGB normals

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: maps an engine can sample | Invariant: 512–1k for student crates; 4k is a budget lecture not a flex; same colorSpace as Three.js week 7`

## Board at the end (they photograph this)

```
BaseColor     sRGB
Normal / Roughness / Metal     non-color (linear)

normal map = tangent-space offset to N
AO = cheap cavity / contact (name)

bake: high bevelled cube → low cube
512–1024     not 8k
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Same as Three.js colorSpace week. Baking every map at 8k is a fail. Substance is optional, not required. A subdivided bevelled cube onto a low cube is enough.

**Ask:** Is a 4k normal map on a mug a quality win? Wait. Want: usually a budget fail; texel density and distance matter.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *normal, AO names*.

**Do not:** Baking every map at 8k.

### Minutes 10–12 — Frame

**Say:** Cage, ray distance named. Color space check. Map list in README.

**Ask:** What do the channels of a normal map mean at teaching level?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** What a normal map stores. AO name.

**Board:** sRGB vs non-color.

**Say:** Plant sRGB normals. Plant 8k.

**Ask:** Why non-color on roughness?

**They do:** On paper: four slots and colorSpace.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Bake a bevelled high onto a low cube; assign. Plant 8k. Plant sRGB normals.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Color space check on the maps. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: normal on a flat plane extra; color space check. Homework: which maps are sRGB; map list in README. Quiz: normal channels, AO, 4k on a mug?.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | High bevel / low cube | Enough. |
| 10–30 | Bake normal | Plant 8k. |
| 30–45 | non-color vs sRGB | Plant sRGB normal. |
| 45–60 | They list maps in README | Circulate. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Normal map on a flat plane from a high bevel extra.
2. Color space check.

---

## Homework

1. Written: which maps are sRGB.
2. Map list in README.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
Image Texture → Color Space: sRGB (albedo) / Non-Color (normal, rough)
```

---

## Extra exercises

See [[Blender/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Baking every map at 8k.
2. sRGB normals.

## If we run long, cut

Substance Painter. Keep bake + colorSpace.

## If we run short, add

Normal on a flat plane from a high bevel extra.
