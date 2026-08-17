# Lecture 14 — Project studio

**Week 14 of 15** · Computer Graphics I  
**Meeting:** studio (not a content lecture)  
**Kernel:** running pipeline + one debug view (n / UV / depth) + README that serves; freeze: cube+Lambert+texture beats broken glTF  
**Success check:** a TA can serve the folder, see more than an untransformed triangle, and hear where M,V,P are

This meeting is **studio**. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Rubric / report headings on the parked strip.
- Clock visible.
- Demo only if a volunteer asks for a blocked kernel: `Computer Graphics/code/14-blinn-phong.html`.
- Parked strip: `Lecture 14 | Goal: freeze and review | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
Report: problem · weeks used · pipeline · hard case · kernel vs lib · results · limits · refs
Defense: M V P order?  divide by w?  debug view?  disable depth?  library vs you?
         affine UV?  where encode?  left-handed API?

Must: serve · debug view · who wrote which file
Cuts: glTF/PBR/shadows → cube+Lambert+texture
      dual CPU/GPU → one path + mapping table
      city graph → two nodes
Do not invent fps. If you did not measure, say so.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture / studio (75 min)

### Minutes 0–10 — Frame

**Say:** This meeting is **studio**. No PBR lecture. If they are stuck on a matrix, debug the matrix. A correct z-buffer on canvas beats a broken gltf dump. Three people, one git author is a failure mode.

**Ask:** If behind, what do you cut first?

**They do:** write their cut list in one column.

**Do not:** introduce a new library today.

### Minutes 10–65 — Desk review

**Say:** Desk order: mat4/shaders, camera, rasterizer or depth test, report outline. Comment on the pipeline, not the CSS. Rehearse 12+5 once with a TA timer: 0–2 problem, 2–6 pipeline+limitation, 6–10 live debug view, 10–12 who did what.

**They do:** Studio. Serve first. One debug view. Recording draft.

**Do not:** sit at the podium. Do not add features for them.

### Minutes 65–75 — Land

**Say:** Report draft + 30s recording due before Week 15. Next week 12+5. No quiz.

**Do not:** “Any questions?” End on the clock.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Eight headings + eight questions + clock | Photograph. |
| 10–50 | Desk review | Kernel, then camera, then depth, then outline. |
| 50–60 | 60s rehearsal | Hard stop. |

This slot is **more studio**, not a hidden lecture.

---

## Lab

_(none this meeting)_

---

## Homework

_(none this meeting)_

---

## Quiz next meeting

None this week.

## Extra exercises

See [[Computer Graphics/exercises/Week 14]].

## Notes from the outline

**1. Report structure (15 min).** 6–8 pages, including figures. Not a Three.js tutorial.

| Section | What we want | Typical length |
| --- | --- | --- |
| Problem | What picture are you making? | ½ page |
| Related course ideas | Which weeks; what you did **not** use | ½ page |
| Pipeline | Spaces, matrices, raster or shaders | 2 pages |
| A hard case | Near plane, winding, gamma, affine UV | ½–1 page |
| Implementation | Math kernel vs library | 1 page |
| Results | Screenshots, debug views | 1 page |
| Limitations | Honest | ½ page |
| References | Shirley, Scratchapixel, WebGL spec, docs | ½ page |

**Figures must have captions.** “Figure 2. NDC y-flip.”

**Do not** paste 200 lines of shader. A 15-line vertex shader is enough.

**Do not** invent timings. If you did not measure FPS, say so.

---
**2. Questions I will ask next week (15 min).** 1. Point to M, V, P in your code. What is the product order?
2. Where do you divide by w?
3. Show a debug view (normals / UV / depth). What would a black normal view mean?
4. If I disable depth, what happens?
5. What did a library do, and what did you write?
6. Affine vs perspective-correct UV: did you implement it? If not, where would it show?
7. Linear vs sRGB: where do you encode?
8. What would break in a left-handed API?

### Presentation clock (Week 15)

- 12 minutes demo + story
- 5 minutes questions
- Hard stop. Rehearse once this week with a TA timer.

| Min | Content |
| ---: | --- |
| 0–2 | Problem and one picture |
| 2–6 | Pipeline, one matrix identity, one limitation |
| 6–10 | Live demo, including a debug view |
| 10–12 | Who did what; what you would do next |

---
**3. Studio rules.** ### Must be true before they leave today

- README runs on a lab machine (`npx serve` / `python -m http.server`).
- The scene is more than a single untransformed triangle **or** they have a written waiver from you for a documented recovery plan.
- One debug view works.
- README: who implemented which file.

### Desk review order

1. `mat4` / shaders
2. Camera
3. Rasterizer or depth test
4. Report outline

Comment on the **pipeline**, not the CSS.

### Scope cuts

| If they are behind | Cut |
| --- | --- |
| glTF / PBR / shadows | Cube + Lambert + texture |
| Dual CPU/GPU | One path, mapping table still required |
| Scene graph city | Two nodes |
| Beautiful post | Unlit textured cube with correct PVM |

---

## If we run long, cut

New libraries. Keep freeze.

## If we run short, add

Waiver only for a documented recovery plan on a single triangle.
