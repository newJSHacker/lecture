# Lecture 2 — Metal-rough PBR

**Week 2 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Cook-Torrance names  
**Success check:** Name D, F, G at teaching level.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: Cook-Torrance names | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
D F G; spec + diff
Microfacet cartoon.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Idea. Microfacets.

**Ask:** D, F, G at teaching level? Wait seven seconds. Take two answers.

**Board:** parked strip. Then D F G; spec + diff.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Cook-Torrance names*.

**Do not:** Metalness 0.5 'for look'.

### Minutes 10–12 — Frame

**Say:** Today’s question: Cook-Torrance names. Kernel: Cook-Torrance names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: metalness 0.5 'for look'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Idea. Microfacets.

**Say:** Split. Students write a **tiny** GGX or use a provided 30-line kernel.

**Say:** Maps. Blender pack from [[19 Blender for Real-Time Graphics]].

**Ask:** D, F, G at teaching level? Wait seven seconds. Take two answers.

**They do:** On paper: compare to MeshStandardMaterial extra.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Two spheres: gold-ish metal vs plastic; roughness slider.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** compare to MeshStandardMaterial extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: compare to MeshStandardMaterial extra.; F0 chart.. Homework: Written: metal vs dielectric in 8 sentences.; Code or shader.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Cook-Torrance names | Plant the first common mistake. |
| 10–30 | Two spheres: gold-ish metal vs plastic; roughness slider. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. compare to MeshStandardMaterial extra.
2. F0 chart.

---

## Homework

1. Written: metal vs dielectric in 8 sentences.
2. Code or shader.

---

## Quiz next meeting (they hear this now)

1. F0 of plastic ~ (3)
2. what roughness does (4)
3. D F G (3)


## Snippet

```glsl
vec3 F0 = mix(vec3(0.04), albedo, metallic);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Idea.** Microfacets. Rough = more spread. Metal = no dielectric diffuse, F0 = albedo.

**2. Split.** Students write a **tiny** GGX or use a provided 30-line kernel. Three.js Standard is the oracle to compare, not the lab substitute in the first hour.

**3. Maps.** Blender pack from [[19 Blender for Real-Time Graphics]].

---

## Common mistakes

1. metalness 0.5 'for look'.
2. roughness as a gray albedo.

## If we run long, cut

Maps

## If we run short, add

F0 chart.
