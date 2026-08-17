# Week 14 — Project studio

**Time:** 30 min lecture, then studio until the period ends  
**No new theory**  
**Required this week:** running pipeline, one debug view, README

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–15 | How to write the report |
| 15–30 | Defense-style questions; presentation clock |
| 30–end | Desk review. Professor and TAs circulate. |

Do not give a lecture on PBR. If a team is stuck on a matrix, debug the matrix.

---

## Learning goals (for the studio)

1. Freeze scope: one pipeline story, one visual.
2. Write a report a second examiner can grade without watching the demo twice.
3. Answer “what is in clip space?” without guessing.

---

## 1. Report structure (15 min)

6–8 pages, including figures. Not a Three.js tutorial.

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

## 2. Questions I will ask next week (15 min)

1. Point to M, V, P in your code. What is the product order?
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

## 3. Studio rules

### Must be true before they leave today

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

## Lab

The studio **is** the lab. Checkpoint: complete / incomplete from Week 13 plus today’s README/debug-view check.

---

## Homework

Finish the report draft and the 30-second recording. Submit the recording before Week 15.

---

## Quiz

None.

---

## Common failure modes

- Pretty Three.js, no student matrix.
- Report is a Blender tutorial.
- No debug view.
- Three people, one git author.

---

## Board

Write only:

1. The 8 report headings
2. The 8 defense questions
3. The 12 + 5 clock
