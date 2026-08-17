# Advanced Computer Graphics

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

GI ideas, a tiny path tracer, volumes, many-light tiling, named modern techniques, paper reading, and one measured advanced piece — not a film studio.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Advanced Computer Graphics/00 Lectures]]  
**Exercises:** [[Advanced Computer Graphics/exercises/00 Index]]

---

## Where this course sits

Semester **6**. [[21 Real-Time Rendering]] and [[20 Shader Programming]]. [[04 Computational Geometry]] helps for tracer BVH extra.

---

## Course goal

By the end, a student can explain indirect light, run a teaching tracer or volume march, read one paper, and defend limits.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** JS/Canvas or WebGL. Three.js path tracers as oracles only.

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
| 1 | Global illumination idea | direct vs indirect |
| 2 | Radiosity idea | patches, form factors |
| 3 | Path tracing teaching | Monte Carlo, cosine sample |
| 4 | Materials in a tracer | metal, glass names |
| 5 | Volumes idea | emission, absorption, scatter |
| 6 | Volume marching | heterogeneous, woodcock name |
| 7 | Deferred review + tiled | lights in tiles |
| 8 | Midterm and shadow research names | midterm; VSM, CSM, PCSS |
| 9 | Geometric detail names | LOD, tessellation, Nanite idea |
| 10 | Optimization as a method | profile, cut, measure |
| 11 | How to read a paper | figures first, claims, threats |
| 12 | Survey talks | 12 min teaching talk |
| 13 | Survey presentations | the talks |
| 14 | Project studio | one advanced piece |
| 15 | Presentations | 12+5 |

---

## What to skip

Production Renderman, full NeRF training as required, Nanite implementation.

---

## Textbooks / refs

PBRT (selected). Real-Time Rendering GI chapters. One assigned paper.

---

## One-sentence teaching principle

If they cannot state the claim and the limitation, they copied a demo.
