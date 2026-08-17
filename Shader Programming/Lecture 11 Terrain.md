# Lecture 11 — Terrain

**Week 11 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** heightmap fBm, lod name  
**Success check:** Height = fBm(xz).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: heightmap fBm, lod name | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
y = fbm(xz)
Slice of hills.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Terrain. The classic IQ scene.

**Ask:** Height = fBm(xz)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then y = fbm(xz).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *heightmap fBm, lod name*.

**Do not:** DEM downloads as the week.

### Minutes 10–12 — Frame

**Say:** Today’s question: heightmap fBm, lod name. Kernel: heightmap fBm, lod name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: DEM downloads as the week.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Terrain. The classic IQ scene.

**Say:** LOD. Step size can grow with t.

**Say:** Textures. Optional triplanar name.

**Ask:** Height = fBm(xz)? Wait seven seconds. Take two answers.

**They do:** On paper: snow line extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Fullscreen terrain march; fog.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** snow line extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: snow line extra.; shadow extra if time.. Homework: Written: height vs mesh terrain.; GLSL.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: heightmap fBm, lod name | Plant the first common mistake. |
| 10–30 | Fullscreen terrain march; fog. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. snow line extra.
2. shadow extra if time.

---

## Homework

1. Written: height vs mesh terrain.
2. GLSL.

---

## Quiz next meeting (they hear this now)

1. height fbm (3)
2. normal from height (4)
3. fog (3)


## Snippet

```glsl
float h = fbm(p.xz * 0.25);
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Terrain.** The classic IQ scene. One sun, fog, height color.

**2. LOD.** Step size can grow with t. Name only unless they implement.

**3. Textures.** Optional triplanar name. Not required.

---

## Common mistakes

1. DEM downloads as the week.
2. unlimited steps.

## If we run long, cut

Textures

## If we run short, add

shadow extra if time.
