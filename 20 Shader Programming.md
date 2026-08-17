# Shader Programming

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

GLSL as a craft: varyings, gamma, procedural UV, noise, SDF, ray marching, and a small post pass — mesh shaders and Shadertoy in one course.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Shader Programming/00 Lectures]]  
**Exercises:** [[Shader Programming/exercises/00 Index]]

---

## Where this course sits

Semester **4**. [[17 WebGL Programming]] and [[14 Mathematics for Computer Graphics]].

---

## Course goal

By the end, a student can write and debug GLSL, cite sources, and show a four-look gallery with a distance or uv debug view.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** WebGL2 + existing [[WebGL/shadertoy]] harness. Desktop GLSL optional.

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
| 1 | The shader as a program | VS/FS, varyings |
| 2 | Color and gamma | linear vs sRGB |
| 3 | UV patterns | grid, polar, repeat |
| 4 | Value noise | hash, lerp |
| 5 | fBm and octaves | sum scaled noise |
| 6 | SDF 2D | circle, union, smooth |
| 7 | Shading an SDF | normals from gradient |
| 8 | Midterm and ray marching intro | midterm; sphere trace idea |
| 9 | Ray marched lighting | soft shadow, AO names |
| 10 | Fire water smoke | domain, lookup, noise |
| 11 | Terrain | heightmap fBm, lod name |
| 12 | Fullscreen post | scene tex → FS |
| 13 | A look catalog | portfolio of 4 looks |
| 14 | Gallery studio | polish the four |
| 15 | Presentations | 12+5 |

---

## What to skip

Writing a compiler, full path tracer (Advanced CG), HLSL-only tooling.

---

## Textbooks / refs

The Book of Shaders (selected). IQ articles as reference. Khronos GLSL ES spec.

---

## One-sentence teaching principle

A shader you cannot pause, uniform, and debug is a clip, not a program.
