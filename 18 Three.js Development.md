# Three.js Development

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Scene graph, materials, glTF, lights, picking-as-oracle, and performance — after students can draw a WebGL triangle.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[ThreeJS Development/00 Lectures]]  
**Exercises:** [[ThreeJS Development/exercises/00 Index]]

---

## Where this course sits

Semester **3**. [[17 WebGL Programming]] first. Three.js is a map of that pipeline.

---

## Course goal

By the end, a student can load a glTF, light it, pick a mesh, and say which WebGL objects the engine hid.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** three r170 from [[08 Three.js Snippets]] `ThreeJS/vendor/` (offline, no CDN).

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
| 1 | Scene, camera, renderer | the three objects |
| 2 | Object3D and transforms | position rotation scale |
| 3 | Materials and geometries | BoxGeometry, Standard vs Basic |
| 4 | Lights and shadows intro | dir/point/ambient |
| 5 | Animation | clock, mixer name |
| 6 | glTF loading | GLTFLoader, scale, shadows |
| 7 | Textures and color space | map, colorSpace |
| 8 | Midterm and raycaster | midterm; picking oracle |
| 9 | Environment and IBL taste | envMap, PMREM name |
| 10 | Shadows deeper | types, bias |
| 11 | Post and composer | EffectComposer name |
| 12 | Performance | draw calls, instancing, LOD name |
| 13 | R3F teaser | declarative three |
| 14 | Project studio | interactive 3D scene |
| 15 | Presentations | 12+5 |

---

## What to skip

Writing Three.js core, full CSS3D, Force-graph libraries as the course.

---

## Textbooks / refs

three.js manual. Discover three.js. WebGL notes.

---

## One-sentence teaching principle

If they cannot map Mesh to a draw call, they are using a magic box.
