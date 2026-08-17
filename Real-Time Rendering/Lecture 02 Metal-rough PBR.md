# Lecture 2 — Metal-rough PBR

**Week 2 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Cook-Torrance names: D spread, F fresnel, G shadowing; metal-rough split  
**Success check:** they can name D, F, G and set F0 = mix(0.04, albedo, metallic)

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: name the shade BRDF | Invariant: metalness 0.5 'for look' is not a material; roughness is not a grey albedo`

## Board at the end (they photograph this)

```
PASS: forward PBR shade

D  microfacet distribution   (rough → spread)
F  fresnel                   F0 = mix(0.04, albedo, metal)
G  geometry / shadowing

dielectric: diffuse + spec
metal:      no dielectric diffuse; F0 = albedo
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Microfacets. Students write a tiny GGX or use a 30-line kernel. MeshStandardMaterial is the oracle after they can name D, F, G — not the lab substitute in the first hour.

**Ask:** What is F0 of plastic, roughly? Wait. Want: ~0.04.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Cook-Torrance names*.

**Do not:** Metalness 0.5 'for look'.

### Minutes 10–12 — Frame

**Say:** Rough = more spread. Maps from Blender later. We do not invent how many ms GGX costs.

**Ask:** What does roughness do to D?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Cartoon of microfacets: mirror vs sandpaper.

**Board:** D F G + F0 mix. Circle metal 0 or 1 for the lab.

**Say:** Compare to Standard after the picture is drawn.

**Ask:** Write the F0 mix line.

**They do:** On paper: metal vs dielectric in four bullets.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Two spheres: gold-ish metal vs plastic; roughness slider. Plant metalness 0.5 for look. Local glTF/maps only — no CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Compare to MeshStandardMaterial extra, or an F0 chart. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: oracle compare + F0 chart. Homework: metal vs dielectric in 8 sentences; shader. Quiz: F0 plastic, roughness, D F G.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | D F G names | Plant roughness as grey albedo. |
| 10–30 | Metal vs plastic | Plant metalness 0.5. |
| 30–45 | Roughness uniform | Still one shade pass. |
| 45–60 | They chart F0 | Circulate. |

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

None this meeting.


## Snippet

```glsl
vec3 F0 = mix(vec3(0.04), albedo, metallic);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. metalness 0.5 'for look'.
2. roughness as a gray albedo.

## If we run long, cut

Full Karis listing. Keep D F G + F0.

## If we run short, add

Blender pack as a name.
