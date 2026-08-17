# Lecture 10 — Baking and maps

**Week 10 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** normal, AO names  
**Success check:** Know what a normal map stores.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: normal, AO names | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
high → low bake idea
High-low arrows.
Map slots.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Maps. BaseColor sRGB.

**Ask:** Know what a normal map stores? Wait seven seconds. Take two answers.

**Board:** parked strip. Then high → low bake idea.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *normal, AO names*.

**Do not:** Baking every map at 8k.

### Minutes 10–12 — Frame

**Say:** Today’s question: normal, AO names. Kernel: normal, AO names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Baking every map at 8k.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Maps. BaseColor sRGB.

**Say:** Bake. Cage, ray distance.

**Say:** Size. 512–1k for student crates.

**Ask:** Know what a normal map stores? Wait seven seconds. Take two answers.

**They do:** On paper: Normal map on a flat plane from a high bevel extra.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Bake or paint roughness dirt on the crate; show in Principled.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Normal map on a flat plane from a high bevel extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Normal map on a flat plane from a high bevel extra.; Color space check.. Homework: Written: which maps are sRGB.; Map list in README.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: normal, AO names | Plant the first common mistake. |
| 10–30 | Bake or paint roughness dirt on the crate; show in Principled. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. normal map channels (4)
2. AO (3)
3. 4k on a mug? (3)


## Snippet

```
Image Texture → Color Space: sRGB (albedo) / Non-Color (normal, rough)
```

---

## Extra exercises

See [[Blender/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Maps.** BaseColor sRGB. Normal / Roughness / Metal non-color. Same as Three.js `colorSpace` week.

**2. Bake.** Cage, ray distance. A subdivided bevelled cube onto a low cube is enough. Substance is optional, not required.

**3. Size.** 512–1k for student crates. 4k is a budget lecture, not a flex.

---

## Common mistakes

1. Baking every map at 8k.
2. sRGB normals.

## If we run long, cut

Size

## If we run short, add

Color space check.
