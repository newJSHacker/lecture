# Blender for Real-Time Graphics

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Author real-time assets: meters, topology, UVs, Principled maps, modest animation, glTF, and a Three.js load — not a Cycles feature film.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Blender/00 Lectures]]  
**Exercises:** [[Blender/exercises/00 Index]]

---

## Where this course sits

Semester **3**. [[18 Three.js Development]] in parallel or just after. Modeling can start earlier if needed.

---

## Course goal

By the end, a student can export a budgeted glb that lights correctly in Three.js and explain every map slot.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** Blender LTS. Offline glTF check in Three.js (`ThreeJS/vendor/`). No Substance required.

Never lecture from slides only.

---

## Assessment

| Component | Weight | Notes |
| --- | --- | --- |
| Labs (12) | 25% | Must run |
| Homework (8) | 20% | Mix of code and written |
| Quizzes (10) | 10% | Weekly |
| Midterm (Week 8) | 15% | Written |
| Final project | 30% | Demo + 6–8 page report |

---

## Week-by-week summary

| Week | Topic | Students do |
| ---: | --- | --- |
| 1 | Blender UI and units | viewport, meters, save |
| 2 | Mesh modeling | verts edges faces |
| 3 | Modifiers | mirror, array, bevel |
| 4 | UV unwrapping | seams, islands, texel |
| 5 | Principled BSDF | base color, metal, roughness |
| 6 | Lights and cameras | area vs sun; exposure |
| 7 | Keyframe animation | I-key, graph editor |
| 8 | Midterm and rigging start | midterm; armature idea |
| 9 | Armatures and export pose | rest pose, apply |
| 10 | Baking and maps | normal, AO names |
| 11 | glTF export | glb, transform, extras |
| 12 | Real-time budgets | tris, batches, maps |
| 13 | Import in Three.js | scale, shadows, colors |
| 14 | Asset pack studio | one pack, one viewer |
| 15 | Presentations | 12+5 |

---

## What to skip

Geometry Nodes as the course, fluid sims, VFX, full character production, Nanite speeches.

---

## Textbooks / refs

Blender manual (selected). glTF 2.0 spec overview. Three.js loading docs.

---

## One-sentence teaching principle

If it is wrong in a glTF viewer, the engine is not the bug.
